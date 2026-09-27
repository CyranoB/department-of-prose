#!/usr/bin/env python3
"""Build the runtime catalogue copies from the reviewed policy and source audit."""

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SPEC = ROOT / "docs/pattern-catalogue-spec.md"
AUDIT = ROOT / "docs/pattern-catalogue-source-audit.md"
TARGETS = (
    ROOT / "skills/slop-sense/catalogue.md",
    ROOT / "skills/slop-check/catalogue.md",
    ROOT / "skills/slop-explain/catalogue.md",
    ROOT / "dist-src/slop-sense-bundle/catalogue.md",
)
POLICY = {"Current": "current_contextual", "Past": "historical_only", "None": "none"}


def evidence_class(number, source):
    if number == 25:
        return "empirical", "supported within interactive assistant responses"
    if number in (34, 36):
        return "empirical", "limited for this specific pattern"
    if "repo editorial judgment" in source or "project editorial judgment" in source:
        return "editorial", "unsubstantiated as an AI association"
    return "observation", "limited to the source's stated context"


def read_entries(spec, audit):
    rows = re.findall(
        r"^\| (\d\d) \| ([^|]+) \| (Current|Past|None) \| "
        r"(Candidate|Advisory|None) \| (.+) \|$",
        spec,
        re.MULTILINE,
    )
    sections = {
        int(match.group(1)): match.group(2)
        for match in re.finditer(
            r"^## (\d\d)\b[^\n]*\n(.*?)(?=^## \d\d\b|^## Audit implications|\Z)",
            audit,
            re.MULTILINE | re.DOTALL,
        )
    }
    if [int(row[0]) for row in rows] != list(range(1, 37)):
        raise ValueError("Spec must contain exactly the ordered pattern IDs 01–36")
    if sorted(sections) != list(range(1, 37)):
        raise ValueError("Source audit must contain exactly pattern IDs 01–36")
    return rows, sections


def source_lines(section):
    source = re.search(r"^- \*\*Source/type:\*\* (.+)$", section, re.MULTILINE)
    limit = re.search(r"^- \*\*Strength/limit:\*\* (.+)$", section, re.MULTILINE)
    if not source or not limit:
        raise ValueError("Every audit entry needs source/type and strength/limit")
    source_text = source.group(1)
    limit_text = limit.group(1)
    return source_text, limit_text


def render(spec, audit):
    rows, sections = read_entries(spec, audit)
    parts = [
        "# Slop Sense editorial pattern catalogue",
        "",
        "Catalogue version: **1.0.0**. Reviewed: **2026-09-27**.",
        "",
        "The optional scorer's score and hits are raw measurements. This catalogue",
        "governs contextual editorial findings. `current_contextual` permits a",
        "scoped AI-style observation, `historical_only` describes a past association,",
        "and `none` permits no AI-style claim. None proves authorship. An editorial",
        "`candidate` becomes actionable only when the quoted passage shows the",
        "problem and its guard has been checked; `advisory` is an optional style",
        "note, and `none` creates no finding. Preserve facts, qualifications,",
        "quotations, and authorial voice when repairing a finding. One span creates",
        "one primary finding even when it matches several pattern IDs.",
        "",
    ]
    for number, name, signal, action, guard in rows:
        n = int(number)
        source, limit = source_lines(sections[n])
        evidence_type, evidence_strength = evidence_class(n, source)
        parts.extend(
            [
                f"## {number} {name}",
                "",
                f"- **ID:** {number}. **Lifecycle:** {'retired' if n == 22 else 'current'}. "
                f"**AI signal:** {POLICY[signal]}. **Editorial action:** {action.lower()}.",
                f"- **Trigger and false-positive guard:** {guard}",
                f"- **Source and evidence type:** {source}",
                f"- **Evidence class:** {evidence_type}; {evidence_strength}.",
                f"- **Evidence strength and scope:** {limit}",
            ]
        )
        if n == 29:
            parts.append("- **Previous name:** False vulnerability (lookup alias).")
        parts.append("")
    vocabulary = re.search(
        r"^## Pattern #8 editorial vocabulary, version .*?\n(.*?)(?=^## Deduplication and migration)",
        spec,
        re.MULTILINE | re.DOTALL,
    )
    if not vocabulary:
        raise ValueError("Spec is missing the versioned #8 vocabulary")
    parts.extend(
        [
            "## Pattern #8 vocabulary",
            "",
            vocabulary.group(1).strip(),
            "",
            "## Migration",
            "",
            "IDs 01–36 stay reserved. #22 is retired as an AI pattern; old references",
            "resolve to its entry above. #29 is renamed to “Disclosure without",
            "substance”; its previous name remains a lookup alias. #15 is a narrow",
            "shape of #10 and must not be counted as a second finding.",
            "",
            "## Change from the unversioned catalogue",
            "",
            "Version 1.0.0 adds source provenance, evidence limits, false-positive",
            "guards, and separate AI-signal and editorial-action decisions for all",
            "36 IDs. #12 moves to historical-only AI use; #17 loses its current",
            "AI-signal use; #21 is historical-only; #22 is retired as an AI",
            "pattern; #29 has the new display name above. #8 uses the explicit",
            "sense-guarded vocabulary list. The optional external scorer and its",
            "version are unchanged.",
            "",
        ]
    )
    return "\n".join(parts)


def render_deep_dive(row, audit_section):
    number, name, signal, action, guard = row
    source, limit = source_lines(audit_section)
    evidence_type, evidence_strength = evidence_class(int(number), source)
    signal_text = {
        "Current": (
            "The source describes a current, context-dependent AI-style "
            "association. It does not identify the author of a passage."
        ),
        "Past": (
            "The source treats this as a historical association. It is not "
            "a current AI-style finding."
        ),
        "None": (
            "The audit does not support using this pattern as a current "
            "AI-style finding."
        ),
    }[signal]
    action_text = {
        "Candidate": (
            "An editorial repair can be useful when the exact passage shows "
            "the problem and the false-positive guard has been checked."
        ),
        "Advisory": (
            "This is optional style advice. Change it only when the user "
            "asks for that style."
        ),
        "None": (
            "This pattern creates no editorial finding or repair."
        ),
    }[action]
    notes = {
        8: (
            "Use the explicit versioned word and sense list in "
            "[catalogue.md](../catalogue.md#pattern-8-vocabulary). A lone "
            "listed word is not a finding."
        ),
        12: (
            "Confusing synonym swaps can still be repaired for clarity. "
            "Keep precise terms and intentional changes of referent."
        ),
        15: (
            "This is a narrower form of #10. One span receives one primary "
            "finding, not two."
        ),
        17: (
            "Assess readability and authorial punctuation. A dash count "
            "alone cannot support an AI-style claim or a mandatory edit."
        ),
        22: (
            "This entry is retired as an AI pattern. Curly quotes are normal "
            "in typeset prose; use straight quotes when a target format such "
            "as code or JSON requires them."
        ),
        25: (
            "Apply this pattern to an interactive assistant response. "
            "Published promotional praise belongs under #04."
        ),
        29: (
            "Former name: “false vulnerability.” The new name asks what "
            "a disclosure contributes without judging the writer's sincerity."
        ),
        34: (
            "Rhythm measurements need enough text and a genre baseline "
            "before they can help editing. A number alone does not require "
            "more variation."
        ),
        36: (
            "A formal notice, technical report, or legal text may correctly "
            "avoid contractions."
        ),
    }
    lines = [
        f"# Pattern {int(number)}: {name}",
        "",
        "Catalogue version **1.0.0**. [Full entry](../catalogue.md).",
        "",
        "## What to assess",
        "",
        guard,
        "",
        "## Evidence and limits",
        "",
        signal_text,
        "",
        f"**Source and evidence type:** {source}",
        "",
        f"**Evidence class:** {evidence_type}; {evidence_strength}.",
        "",
        f"**Strength and scope:** {limit}",
        "",
        "## Editorial use",
        "",
        action_text,
    ]
    note = notes.get(int(number))
    if note:
        lines.extend(["", note])
    lines.append("")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail if copies differ")
    args = parser.parse_args()
    spec = SPEC.read_text(encoding="utf-8")
    audit = AUDIT.read_text(encoding="utf-8")
    content = render(spec, audit)
    rows, sections = read_entries(spec, audit)
    outputs = {target: content for target in TARGETS}
    pattern_dir = ROOT / "skills/slop-explain/patterns"
    for row in rows:
        number = row[0]
        files = list(pattern_dir.glob(number + "-*.md"))
        if len(files) != 1:
            raise ValueError(f"Expected one deep-dive file for pattern {number}")
        outputs[files[0]] = render_deep_dive(row, sections[int(number)])
    stale = []
    for target, expected in outputs.items():
        if args.check:
            if not target.exists() or target.read_text(encoding="utf-8") != expected:
                stale.append(target.relative_to(ROOT).as_posix())
        else:
            target.write_text(expected, encoding="utf-8")
    if stale:
        parser.error("stale catalogue copies: " + ", ".join(stale))
    print("checked" if args.check else "updated", len(outputs), "catalogue files")


if __name__ == "__main__":
    main()
