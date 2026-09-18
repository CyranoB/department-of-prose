#!/usr/bin/env python3
"""Bump the shared plugin version or check it against a base revision."""

import argparse
import json
import re
import subprocess
from pathlib import Path

PLUGIN_NAME = "slop-sense"
CLAUDE_MANIFEST = Path(".claude-plugin/plugin.json")
CLAUDE_MARKETPLACE = Path(".claude-plugin/marketplace.json")
CODEX_MANIFEST = Path(".codex-plugin/plugin.json")
CODEX_MARKETPLACE = Path(".agents/plugins/marketplace.json")
PLUGIN_PATHS = ("skills", ".claude-plugin", ".codex-plugin", ".agents/plugins")


def version_tuple(value):
    if not isinstance(value, str) or not re.fullmatch(
        r"(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)", value
    ):
        raise ValueError(f"Expected a major.minor.patch version, got {value!r}")
    return tuple(map(int, value.split(".")))


def load_json(root, path):
    return json.loads((root / path).read_text(encoding="utf-8"))


def write_json(root, path, value):
    (root / path).write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def claude_plugin_entry(marketplace):
    return next(
        plugin for plugin in marketplace["plugins"] if plugin["name"] == PLUGIN_NAME
    )


def codex_plugin_entry(marketplace):
    return next(
        plugin for plugin in marketplace["plugins"] if plugin["name"] == PLUGIN_NAME
    )


def versions(claude_manifest, claude_marketplace, codex_manifest):
    return {
        "Claude manifest": claude_manifest["version"],
        "Claude marketplace metadata": claude_marketplace["metadata"]["version"],
        "Claude marketplace plugin": claude_plugin_entry(claude_marketplace)[
            "version"
        ],
        "Codex manifest": codex_manifest["version"],
    }


def git(root, *args):
    return subprocess.check_output(["git", *args], cwd=root, text=True).strip()


def validate_packaging(root, claude_manifest, claude_marketplace, codex_manifest):
    actual_skills = {
        path.parent.name for path in (root / "skills").glob("*/SKILL.md")
    }
    declared_skills = {Path(path).name for path in claude_manifest["skills"]}
    if actual_skills != declared_skills:
        raise ValueError(
            f"Claude manifest skills {sorted(declared_skills)} do not match "
            f"published skills {sorted(actual_skills)}"
        )
    if codex_manifest["skills"].rstrip("/") != "./skills":
        raise ValueError("Codex manifest must load the shared ./skills/ directory")
    if claude_manifest["name"] != PLUGIN_NAME or codex_manifest["name"] != PLUGIN_NAME:
        raise ValueError("Plugin manifest names must be slop-sense")
    if claude_plugin_entry(claude_marketplace)["source"] != "./":
        raise ValueError("Claude marketplace must install from the repository root")

    codex_marketplace = load_json(root, CODEX_MARKETPLACE)
    if codex_marketplace["name"] != PLUGIN_NAME:
        raise ValueError("Codex marketplace name must be slop-sense")
    entry = codex_plugin_entry(codex_marketplace)
    expected_source = {"source": "local", "path": "./"}
    expected_policy = {"installation": "AVAILABLE", "authentication": "ON_INSTALL"}
    if entry["source"] != expected_source:
        raise ValueError("Codex marketplace must install from the repository root")
    if entry["policy"] != expected_policy:
        raise ValueError("Codex marketplace install policy is invalid")
    if entry["category"] != "Productivity":
        raise ValueError("Codex marketplace category must be Productivity")


def check(root, base=None):
    claude_manifest = load_json(root, CLAUDE_MANIFEST)
    claude_marketplace = load_json(root, CLAUDE_MARKETPLACE)
    codex_manifest = load_json(root, CODEX_MANIFEST)
    current_versions = versions(claude_manifest, claude_marketplace, codex_manifest)
    for value in current_versions.values():
        version_tuple(value)
    current = claude_manifest["version"]
    if any(value != current for value in current_versions.values()):
        details = ", ".join(
            f"{label}={value}" for label, value in current_versions.items()
        )
        raise ValueError(f"Plugin and marketplace versions differ: {details}")

    validate_packaging(root, claude_manifest, claude_marketplace, codex_manifest)
    if base:
        previous = json.loads(git(root, "show", f"{base}:{CLAUDE_MANIFEST.as_posix()}"))
        previous_version = previous["version"]
        changed = git(root, "diff", "--name-only", base, "--", *PLUGIN_PATHS)
        if changed and version_tuple(current) <= version_tuple(previous_version):
            raise ValueError(
                f"Plugin changes require a version greater than {previous_version}"
            )
    return current


def bump(root, version):
    new_tuple = version_tuple(version)
    claude_manifest = load_json(root, CLAUDE_MANIFEST)
    claude_marketplace = load_json(root, CLAUDE_MARKETPLACE)
    codex_manifest = load_json(root, CODEX_MANIFEST)
    current_versions = versions(claude_manifest, claude_marketplace, codex_manifest)
    current = max(current_versions.values(), key=version_tuple)
    if new_tuple <= version_tuple(current):
        raise ValueError(f"New version must be greater than {current}")

    claude_manifest["version"] = version
    claude_marketplace["metadata"]["version"] = version
    claude_plugin_entry(claude_marketplace)["version"] = version
    codex_manifest["version"] = version
    for path, value in (
        (CLAUDE_MANIFEST, claude_manifest),
        (CLAUDE_MARKETPLACE, claude_marketplace),
        (CODEX_MANIFEST, codex_manifest),
    ):
        write_json(root, path, value)
    check(root)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("check").add_argument("--base")
    commands.add_parser("bump").add_argument("version")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    try:
        if args.command == "bump":
            bump(root, args.version)
        print(check(root, getattr(args, "base", None)))
    except (ValueError, KeyError, StopIteration, subprocess.CalledProcessError) as error:
        parser.exit(1, f"Version check failed: {error}\n")


if __name__ == "__main__":
    main()
