#!/usr/bin/env python3
"""Run Slop Sense's deterministic and fixture-contract evaluations.

This runner intentionally uses only the Python standard library. It never calls
a language model. The pinned Node scorer is exercised only by fixtures marked
``real_scorer``; wrapper behavior is tested with temporary controlled programs.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
from pathlib import Path
import re
import stat
import subprocess
import sys
import tempfile
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
EVALUATION = ROOT / "evaluation"
RHYTHM_PATH = ROOT / "skills/slop-sense/scripts/rhythm.py"
WRAPPER_PATH = ROOT / "skills/slop-sense/scripts/score.sh"
SCORER_PATH = ROOT / "node_modules/.bin/slop-score"
SCORER_PACKAGE = ROOT / "node_modules/slop-detector/package.json"


def load_json(path: Path) -> Any:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def load_rhythm():
    spec = importlib.util.spec_from_file_location("slop_sense_rhythm", RHYTHM_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {RHYTHM_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


RHYTHM = load_rhythm()


def compare(actual: Any, assertion: dict[str, Any]) -> None:
    def json_shape(value: Any) -> Any:
        if isinstance(value, (list, tuple)):
            return [json_shape(item) for item in value]
        if isinstance(value, dict):
            return {key: json_shape(item) for key, item in value.items()}
        return value

    actual = json_shape(actual)
    if "equals" in assertion and actual != assertion["equals"]:
        raise AssertionError(f"expected {assertion['equals']!r}, got {actual!r}")
    if "approx" in assertion:
        wanted = assertion["approx"]
        if abs(float(actual) - float(wanted["value"])) > float(wanted["tolerance"]):
            raise AssertionError(
                f"expected {wanted['value']} ± {wanted['tolerance']}, got {actual}"
            )
    rendered = str(actual)
    for needle in assertion.get("contains", []):
        if needle not in rendered:
            raise AssertionError(f"expected output to contain {needle!r}; got {rendered!r}")
    for needle in assertion.get("not_contains", []):
        if needle in rendered:
            raise AssertionError(f"expected output not to contain {needle!r}; got {rendered!r}")
    for pattern in assertion.get("matches", []):
        if not re.search(pattern, rendered, re.MULTILINE):
            raise AssertionError(f"expected output to match {pattern!r}; got {rendered!r}")


def run_python_call(fixture: dict[str, Any]) -> Any:
    call = fixture["call"]
    function = getattr(RHYTHM, call["function"])
    result = function(*call.get("args", []), **call.get("kwargs", {}))
    for index in call.get("select", []):
        result = result[index]
    return result


def run_rhythm_cli(fixture: dict[str, Any]) -> dict[str, Any]:
    cli = fixture["cli"]
    command = [sys.executable, str(RHYTHM_PATH)]
    input_text = cli.get("stdin")
    temporary_file = None
    if "file_text" in cli:
        temporary_file = tempfile.NamedTemporaryFile(
            mode="w", encoding="utf-8", suffix=".md", delete=False
        )
        temporary_file.write(cli["file_text"])
        temporary_file.close()
        command.append(temporary_file.name)
        input_text = None
    if cli.get("missing_file"):
        command.append(str(ROOT / "evaluation/fixtures/does-not-exist.txt"))
    try:
        completed = subprocess.run(
            command,
            input=input_text,
            text=True,
            capture_output=True,
            timeout=15,
            check=False,
        )
    finally:
        if temporary_file:
            Path(temporary_file.name).unlink(missing_ok=True)
    return {
        "returncode": completed.returncode,
        "stdout": completed.stdout,
        "stderr": completed.stderr,
    }


def make_executable(path: Path, source: str) -> None:
    path.write_text(source, encoding="utf-8")
    path.chmod(path.stat().st_mode | stat.S_IXUSR)


def run_wrapper(fixture: dict[str, Any]) -> dict[str, Any]:
    config = fixture["wrapper"]
    with tempfile.TemporaryDirectory() as temp_dir:
        bin_dir = Path(temp_dir)
        for name, spec in config.get("programs", {}).items():
            make_executable(bin_dir / name, spec)
        env = os.environ.copy()
        env["PATH"] = str(bin_dir)
        completed = subprocess.run(
            ["/bin/bash", str(WRAPPER_PATH), *config.get("args", [])],
            input=config.get("stdin", ""),
            text=True,
            capture_output=True,
            env=env,
            timeout=15,
            check=False,
        )
        return {
            "returncode": completed.returncode,
            "stdout": completed.stdout,
            "stderr": completed.stderr,
        }


def run_real_scorer(fixture: dict[str, Any]) -> dict[str, Any]:
    wanted_version = (EVALUATION / "SCORER_VERSION").read_text(encoding="utf-8").strip()
    if not SCORER_PATH.is_file() or not SCORER_PACKAGE.is_file():
        raise AssertionError("pinned scorer is missing; run `npm ci` before evaluation")
    installed_version = load_json(SCORER_PACKAGE)["version"]
    if installed_version != wanted_version:
        raise AssertionError(
            f"expected slop-detector {wanted_version}, installed {installed_version}"
        )
    completed = subprocess.run(
        [str(SCORER_PATH), "-"],
        input=fixture["scorer"]["stdin"],
        text=True,
        capture_output=True,
        timeout=30,
        check=False,
        env={**os.environ, "NO_COLOR": "1"},
    )
    score_match = re.search(r"Final Score:\s*([0-9.]+)/100", completed.stdout)
    return {
        "returncode": completed.returncode,
        "version": installed_version,
        "score": float(score_match.group(1)) if score_match else None,
        "stdout": completed.stdout,
        "stderr": completed.stderr,
    }


def assert_process(actual: dict[str, Any], assertion: dict[str, Any]) -> None:
    if "returncode" in assertion and actual["returncode"] != assertion["returncode"]:
        raise AssertionError(
            f"expected exit {assertion['returncode']}, got {actual['returncode']}; "
            f"stderr={actual['stderr']!r}"
        )
    for stream in ("stdout", "stderr"):
        rules = assertion.get(stream, {})
        compare(actual[stream], rules)
    if "version" in assertion:
        compare(actual.get("version"), {"equals": assertion["version"]})
    if "score" in assertion:
        score = actual.get("score")
        if score is None:
            raise AssertionError(f"scorer output had no Final Score: {actual['stdout']!r}")
        limits = assertion["score"]
        if "min" in limits and score < limits["min"]:
            raise AssertionError(f"expected score >= {limits['min']}, got {score}")
        if "max" in limits and score > limits["max"]:
            raise AssertionError(f"expected score <= {limits['max']}, got {score}")


def execute(fixture: dict[str, Any]) -> None:
    kind = fixture["kind"]
    if kind == "python_call":
        compare(run_python_call(fixture), fixture["assert"])
    elif kind == "rhythm_cli":
        assert_process(run_rhythm_cli(fixture), fixture["assert"])
    elif kind == "wrapper":
        assert_process(run_wrapper(fixture), fixture["assert"])
    elif kind == "real_scorer":
        assert_process(run_real_scorer(fixture), fixture["assert"])
    else:
        raise AssertionError(f"unknown fixture kind {kind!r}")


REQUIRED_FIXTURE_FIELDS = {
    "id",
    "target",
    "layer",
    "polarity",
    "status",
    "expected_outcome",
    "rationale",
    "kind",
    "assert",
}


def validate_fixture_contract(fixture: dict[str, Any], seen: set[str]) -> None:
    missing = REQUIRED_FIXTURE_FIELDS - fixture.keys()
    if missing:
        raise AssertionError(f"fixture missing fields: {sorted(missing)}")
    if fixture["id"] in seen:
        raise AssertionError(f"duplicate fixture ID {fixture['id']}")
    seen.add(fixture["id"])
    if fixture["layer"] != "deterministic":
        raise AssertionError("executable regression fixtures must use deterministic layer")
    if fixture["polarity"] not in {"positive", "negative", "boundary", "contract"}:
        raise AssertionError(f"invalid polarity {fixture['polarity']!r}")
    if fixture["status"] == "xfail":
        for field in ("owner", "desired_result", "current_failure"):
            if not fixture.get(field):
                raise AssertionError(f"xfail {fixture['id']} missing {field}")
    elif fixture["status"] != "pass":
        raise AssertionError(f"invalid status {fixture['status']!r}")


def validate_coverage(fixtures: list[dict[str, Any]]) -> None:
    coverage = load_json(EVALUATION / "coverage.json")
    fixtures_by_id = {fixture["id"]: fixture for fixture in fixtures}
    mapped: set[str] = set()
    for item in coverage["inventory"]:
        for category in ("positive", "negative", "boundary"):
            references = item[category]
            if not references and category not in item.get("not_applicable", {}):
                raise AssertionError(
                    f"coverage target {item['target']} needs {category} fixtures or a reason"
                )
            for fixture_id in references:
                if fixture_id not in fixtures_by_id:
                    raise AssertionError(
                        f"coverage target {item['target']} references unknown {fixture_id}"
                    )
                mapped.add(fixture_id)
    uncovered = {
        fixture["id"]
        for fixture in fixtures
        if fixture["polarity"] in {"positive", "negative", "boundary"}
    } - mapped
    if uncovered:
        raise AssertionError(f"fixtures absent from coverage inventory: {sorted(uncovered)}")
    if not coverage.get("exclusions") or not coverage.get("future_behavior"):
        raise AssertionError("coverage must state exclusions and future behavior")


def validate_baseline(fixtures: list[dict[str, Any]]) -> None:
    baseline = load_json(EVALUATION / "baseline.json")
    fixture_xfails = {
        fixture["id"]: fixture["owner"]
        for fixture in fixtures
        if fixture["status"] == "xfail"
    }
    baseline_xfails = {
        item["id"]: item["owner"] for item in baseline["expected_failures"]
    }
    if fixture_xfails != baseline_xfails:
        raise AssertionError(
            "baseline expected failures differ from executable fixtures: "
            f"fixtures={fixture_xfails}, baseline={baseline_xfails}"
        )


GOLDEN_REQUIRED = {
    "id",
    "target",
    "layer",
    "expected_outcome",
    "rationale",
    "source",
    "required_findings",
    "permitted_findings",
    "forbidden_findings",
    "facts_to_preserve",
    "qualifications_to_preserve",
    "prohibited_additions",
    "voice_markers_to_retain",
    "rewrite_expectations",
}


def validate_golden_cases() -> int:
    cases = load_json(EVALUATION / "golden/cases.json")["cases"]
    seen: set[str] = set()
    for case in cases:
        missing = GOLDEN_REQUIRED - case.keys()
        if missing:
            raise AssertionError(f"golden case missing fields: {sorted(missing)}")
        if case["id"] in seen:
            raise AssertionError(f"duplicate golden ID {case['id']}")
        seen.add(case["id"])
        if case["layer"] != "editorial":
            raise AssertionError(f"golden case {case['id']} must use editorial layer")
        if case["source"]["provenance"] not in {"original", "CC0", "public-domain"}:
            raise AssertionError(f"golden case {case['id']} has unsafe provenance")
        if not case["source"].get("text"):
            raise AssertionError(f"golden case {case['id']} has empty source text")
    return len(cases)


def run_all(selected: str | None = None) -> int:
    payload = load_json(EVALUATION / "fixtures/deterministic.json")
    fixtures = payload["fixtures"]
    seen: set[str] = set()
    for fixture in fixtures:
        validate_fixture_contract(fixture, seen)
    validate_coverage(fixtures)
    validate_baseline(fixtures)
    golden_count = validate_golden_cases()

    pass_count = xfail_count = fail_count = xpass_count = 0
    for fixture in fixtures:
        if selected and selected not in fixture["id"]:
            continue
        try:
            execute(fixture)
        except Exception as exc:  # the fixture ID and expectation make failures diagnosable
            if fixture["status"] == "xfail":
                xfail_count += 1
                print(f"XFAIL {fixture['id']} [{fixture['owner']}] {exc}")
            else:
                fail_count += 1
                print(
                    f"FAIL  {fixture['id']}\n"
                    f"      expected: {fixture['expected_outcome']}\n"
                    f"      actual:   {exc}"
                )
        else:
            if fixture["status"] == "xfail":
                xpass_count += 1
                print(
                    f"XPASS {fixture['id']} [{fixture['owner']}] desired behavior now passes; "
                    "remove the exemption"
                )
            else:
                pass_count += 1
                print(f"PASS  {fixture['id']}")

    print(
        f"\nSummary: {pass_count} passed, {xfail_count} expected failures, "
        f"{fail_count} unexpected failures, {xpass_count} unexpected passes; "
        f"{golden_count} golden contracts validated"
    )
    return 1 if fail_count or xpass_count else 0


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--id", help="run fixture IDs containing this text")
    args = parser.parse_args()
    raise SystemExit(run_all(args.id))


if __name__ == "__main__":
    main()
