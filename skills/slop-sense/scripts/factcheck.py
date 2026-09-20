#!/usr/bin/env python3
"""Deterministic fact-preservation check between an original and a rewrite.

Companion to rhythm.py. Same contract: pure Python standard library, no
network, no model calls, no Node. Where score.sh measures lexical slop and
rhythm.py measures structure, this measures what survived the edit.

It answers the mechanical half of the pattern-17 audit question "did the facts
change?", so the rewrite is not asked to certify its own arithmetic:

  numbers      figures, percentages, money, and years present on each side
  quotations   quoted spans that must appear verbatim in the rewrite
  entities     capitalised names dropped or newly introduced
  hedges       uncertainty, attribution and scope markers, pooled by bucket
  burstiness   the CV delta that rhythm.py reports, computed not asserted

It cannot judge meaning, and it works on token sets rather than positions. A
number that survives in a sentence that now claims something different still
counts as present. A hedge that moves from the claim it qualified to somewhere
harmless still counts as present. So the editorial fact check in SKILL.md is
still required: this narrows it, it does not replace it.

usage:
  python3 factcheck.py --original before.txt --rewrite after.txt
  python3 factcheck.py before.txt after.txt
  python3 factcheck.py --original before.txt --rewrite after.txt --strict

--strict exits 1 on a hard finding: a lost or added number, a broken quotation,
a dropped entity, or an uncertainty/attribution bucket emptied entirely. Scope
markers and per-term hedge reductions are reported but never gate, because
compressing "could potentially" to "may" is the correct repair and a scope limit
can be carried by a clause with no keyword in it. Default exits 0 and reports,
so the script stays advisory like rhythm.py.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

# rhythm.py is the sibling source of truth for segmentation and burstiness.
# Import it when available so the two scripts cannot disagree; fall back to a
# local copy of the same logic when this file is used standalone.
try:
    import importlib.util

    _spec = importlib.util.spec_from_file_location(
        "_slop_rhythm", Path(__file__).with_name("rhythm.py")
    )
    if _spec is None or _spec.loader is None:
        raise ImportError("rhythm.py not loadable")
    _rhythm = importlib.util.module_from_spec(_spec)
    _spec.loader.exec_module(_rhythm)
except Exception:  # pragma: no cover - exercised only when rhythm.py is absent
    _rhythm = None


# --- input ------------------------------------------------------------------

def read_text(path: str) -> str:
    if path == "-":
        return sys.stdin.read()
    return Path(path).read_text(encoding="utf-8")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="factcheck.py",
        description="Compare an original and a rewrite for dropped facts.",
    )
    parser.add_argument("--original", help="path to the original text, or - for stdin")
    parser.add_argument("--rewrite", help="path to the rewritten text, or - for stdin")
    parser.add_argument("positional", nargs="*", help="original and rewrite paths")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="exit 1 when any hard finding is present",
    )
    args = parser.parse_args(argv)
    if args.original and args.rewrite:
        return args
    if len(args.positional) == 2:
        args.original, args.rewrite = args.positional
        return args
    parser.error("give --original and --rewrite, or two positional paths")


# --- numbers ----------------------------------------------------------------

# Matches 12, 12.5, 1,200, 12%, $25, 12 percent, 2023. Keeps the unit attached
# so "12 percent" and "12" are not treated as the same claim.
NUMBER_RE = re.compile(
    r"""
    (?P<currency>[$£€]\s?)?
    (?P<value>\d{1,3}(?:,\d{3})+(?:\.\d+)?|\d+(?:\.\d+)?)
    \s*
    (?P<unit>%|percent|per\s?cent|bn|billion|m|million|k|thousand)?
    """,
    re.I | re.X,
)


def normalise_number(match: re.Match) -> str:
    value = match.group("value").replace(",", "")
    unit = (match.group("unit") or "").lower().replace(" ", "")
    unit = {"per cent": "percent", "percent": "percent", "%": "percent"}.get(unit, unit)
    unit = {"bn": "billion", "m": "million", "k": "thousand"}.get(unit, unit)
    currency = (match.group("currency") or "").strip()
    return f"{currency}{value}{(' ' + unit) if unit else ''}"


def numbers(text: str) -> list[str]:
    return [normalise_number(m) for m in NUMBER_RE.finditer(text)]


# --- quotations -------------------------------------------------------------

QUOTE_RE = re.compile(r"[“”\"]([^“”\"]{4,})[“”\"]")


def quotations(text: str) -> list[str]:
    return [m.group(1).strip() for m in QUOTE_RE.finditer(text)]


def normalise_quote(span: str) -> str:
    """Compare quote content ignoring quote-mark style and whitespace runs."""
    span = span.replace("’", "'").replace("‘", "'")
    span = span.replace("—", "--").replace("–", "-")
    return re.sub(r"\s+", " ", span).strip().lower()


# --- entities ---------------------------------------------------------------

# Sentence-initial capitals are not evidence of a proper noun, so drop the
# first word of every sentence before collecting candidates.
STOP_CAPS = {
    "A", "An", "And", "As", "At", "But", "By", "For", "From", "I", "If", "In",
    "It", "Its", "Not", "Of", "On", "Or", "So", "The", "Then", "There", "This",
    "To", "We", "What", "When", "Where", "Which", "While", "With", "You",
}

ENTITY_RE = re.compile(r"\b[A-Z][\w&.'-]*(?:\s+[A-Z][\w&.'-]*)*")


def entities(text: str) -> set[str]:
    found: set[str] = set()
    for sentence in split_sentences(text):
        body = re.sub(r"^[\"“(]*\S+\s*", "", sentence, count=1)
        for match in ENTITY_RE.finditer(body):
            token = match.group(0).strip(".,;:")
            if not token or token in STOP_CAPS:
                continue
            if token.isupper() and len(token) <= 2:
                continue
            found.add(token)
    # Stripping the sentence-initial word leaves a tail behind when a name opens
    # a sentence ("Meridian Freight Lines expects..." yields "Freight Lines"),
    # so drop any candidate fully contained in a longer one.
    return {
        name for name in found
        if not any(other != name and name in other for other in found)
    }


# --- hedges -----------------------------------------------------------------

# Deliberately narrow. Every term here has to be a hedge in nearly all of its
# uses, because a word that is only sometimes a qualifier produces noise that
# trains the reader to ignore the report. "some", "only" and "early" were tried
# and removed: "invest early" and "only three" are different animals and the
# script cannot tell them apart.
HEDGE_CLASSES: dict[str, tuple[str, ...]] = {
    "modal": ("may", "might", "could"),
    "reporting": ("suggest", "suggests", "suggested", "indicate", "indicates",
                  "appear", "appears", "seem", "seems", "estimate", "estimates",
                  "estimated", "reported", "reportedly", "according to"),
    "approximation": ("roughly", "approximately", "or so"),
    "scope": ("self-reported", "self reported", "preliminary", "partial",
              "internal", "unverified", "unconfirmed", "provisional",
              "not yet", "so far", "to date"),
    "negated_certainty": ("unlikely", "uncertain", "unclear", "possible",
                          "possibly", "potentially", "probably", "likely"),
}

# Approximators that only hedge when they sit in front of a quantity.
NUMERIC_APPROX = ("about", "around", "nearly", "almost", "up to", "at least",
                  "more than", "fewer than", "less than")


# Modals, approximations and adverbs of doubt are interchangeable carriers of
# uncertainty, so they are pooled. Cutting "could potentially" down to "may" is
# the correct pattern-31 repair and must not register as a loss; cutting the
# doubt out altogether must. Reporting verbs and scope limits are separate
# buckets because nothing else in the sentence can carry them.
HEDGE_BUCKETS: dict[str, tuple[str, ...]] = {
    "uncertainty": ("modal", "approximation", "negated_certainty"),
    "attribution": ("reporting",),
    "scope": ("scope",),
}

# Buckets whose elimination is a hard finding. Scope is reported but never
# gates, because a scope limit can be carried by a clause with no keyword in it
# ("among the 40 who finished") and a keyword-based check would miss that and
# then cry wolf on the cases it does see.
HARD_BUCKETS = ("uncertainty", "attribution")


def hedge_counts(text: str) -> dict[str, dict[str, int]]:
    lowered = text.lower()
    out: dict[str, dict[str, int]] = {}
    for label, terms in HEDGE_CLASSES.items():
        hits: dict[str, int] = {}
        for term in terms:
            pattern = r"\b" + re.escape(term).replace(r"\ ", r"\s+") + r"\b"
            count = len(re.findall(pattern, lowered))
            if count:
                hits[term] = count
        if label == "approximation":
            for term in NUMERIC_APPROX:
                pattern = (r"\b" + re.escape(term).replace(r"\ ", r"\s+")
                           + r"\s+(?=[\d$£€])")
                count = len(re.findall(pattern, lowered))
                if count:
                    hits[f"{term} <number>"] = count
        out[label] = hits
    return out


# --- burstiness -------------------------------------------------------------

def split_sentences(text: str) -> list[str]:
    if _rhythm is not None:
        stripped = _rhythm.strip_markdown(text)
        found: list[str] = []
        for para in _rhythm.paragraphs(stripped):
            found.extend(_rhythm.split_sentences(para))
        return found
    return [s for s in re.split(r"(?<=[.!?])\s+", text.strip()) if s]


def cv(text: str) -> float | None:
    sentences = split_sentences(text)
    lengths = [len(re.findall(r"\b[\w']+\b", s)) for s in sentences]
    lengths = [n for n in lengths if n]
    if len(lengths) < 2:
        return None
    if _rhythm is not None:
        return _rhythm.burstiness(lengths)[2]
    mean = sum(lengths) / len(lengths)
    variance = sum((n - mean) ** 2 for n in lengths) / len(lengths)
    return (variance ** 0.5) / mean if mean else 0.0


# --- comparison -------------------------------------------------------------

def multiset_lost(before: list[str], after: list[str]) -> list[str]:
    remaining = list(after)
    lost = []
    for item in before:
        if item in remaining:
            remaining.remove(item)
        else:
            lost.append(item)
    return lost


def compare(original: str, rewrite: str) -> dict:
    before_numbers, after_numbers = numbers(original), numbers(rewrite)
    before_quotes, after_quotes = quotations(original), quotations(rewrite)
    after_normalised = [normalise_quote(q) for q in after_quotes]
    rewrite_flat = normalise_quote(rewrite)

    broken_quotes = []
    for quote in before_quotes:
        wanted = normalise_quote(quote)
        if wanted not in after_normalised and wanted not in rewrite_flat:
            broken_quotes.append(quote)

    before_entities, after_entities = entities(original), entities(rewrite)
    dropped_entities = sorted(
        name for name in before_entities - after_entities
        if not any(name in other for other in after_entities)
    )
    added_entities = sorted(
        name for name in after_entities - before_entities
        if not any(name in other for other in before_entities)
    )

    before_hedges, after_hedges = hedge_counts(original), hedge_counts(rewrite)
    reduced_terms: dict[str, list[str]] = {}
    for label in HEDGE_CLASSES:
        lost = []
        for term, count in before_hedges[label].items():
            kept = after_hedges[label].get(term, 0)
            if kept < count:
                lost.append(f"{term} ({count} -> {kept})")
        if lost:
            reduced_terms[label] = lost

    buckets: dict[str, dict[str, int]] = {}
    eliminated: list[str] = []
    for bucket, labels in HEDGE_BUCKETS.items():
        before_total = sum(sum(before_hedges[l].values()) for l in labels)
        after_total = sum(sum(after_hedges[l].values()) for l in labels)
        buckets[bucket] = {"before": before_total, "after": after_total}
        if before_total and not after_total and bucket in HARD_BUCKETS:
            eliminated.append(bucket)

    before_cv, after_cv = cv(original), cv(rewrite)

    return {
        "numbers": {
            "before": before_numbers,
            "after": after_numbers,
            "lost": multiset_lost(before_numbers, after_numbers),
            "added": multiset_lost(after_numbers, before_numbers),
        },
        "quotations": {"before": before_quotes, "broken": broken_quotes},
        "entities": {"dropped": dropped_entities, "added": added_entities},
        "hedges": {
            "eliminated": eliminated,
            "reduced": reduced_terms,
            "buckets": buckets,
        },
        "burstiness": {"before_cv": before_cv, "after_cv": after_cv},
    }


def hard_findings(result: dict) -> list[str]:
    found = []
    if result["numbers"]["lost"]:
        found.append("lost numbers")
    if result["numbers"]["added"]:
        found.append("added numbers")
    if result["quotations"]["broken"]:
        found.append("broken quotations")
    if result["entities"]["dropped"]:
        found.append("dropped entities")
    for bucket in result["hedges"]["eliminated"]:
        found.append(f"{bucket} eliminated")
    return found


# --- report -----------------------------------------------------------------

def fmt_cv(value: float | None) -> str:
    return "n/a" if value is None else f"{value:.2f}"


def report(result: dict) -> str:
    lines = ["=== Fact Preservation Check ===", ""]

    nums = result["numbers"]
    lines.append("Numbers:")
    if nums["lost"]:
        lines.append("  LOST: " + ", ".join(nums["lost"]))
        lines.append("  fix: every figure in the original must survive the rewrite")
    if nums["added"]:
        lines.append("  ADDED: " + ", ".join(nums["added"]))
        lines.append("  fix: a figure not in the original is a fabrication")
    if not nums["lost"] and not nums["added"]:
        count = len(nums["before"])
        lines.append(f"  ok - all {count} preserved" if count else "  ok - none present")
    lines.append("")

    quotes = result["quotations"]
    lines.append("Quotations:")
    if quotes["broken"]:
        for span in quotes["broken"]:
            lines.append(f'  BROKEN: "{span}"')
        lines.append("  fix: quoted text is a record of what someone said; restore it verbatim")
    else:
        count = len(quotes["before"])
        lines.append(f"  ok - all {count} verbatim" if count else "  ok - none present")
    lines.append("")

    ents = result["entities"]
    lines.append("Named entities:")
    if ents["dropped"]:
        lines.append("  DROPPED: " + ", ".join(ents["dropped"]))
        lines.append("  fix: repeat the name or use a pronoun; do not paraphrase it (pattern 12)")
    if ents["added"]:
        lines.append("  ADDED: " + ", ".join(ents["added"]))
        lines.append("  check: a name not in the original may be invented support")
    if not ents["dropped"] and not ents["added"]:
        lines.append("  ok - unchanged")
    lines.append("")

    hedges = result["hedges"]
    lines.append("Hedges and qualifications:")
    for bucket, counts in hedges["buckets"].items():
        if bucket in hedges["eliminated"]:
            marker = "  ELIMINATED"
        elif counts["before"] and not counts["after"]:
            marker = "  check"
        else:
            marker = "  ok"
        note = "" if bucket in HARD_BUCKETS else "   (advisory only)"
        lines.append(
            f"{marker} [{bucket}]: {counts['before']} -> {counts['after']}{note}")
    if hedges["eliminated"]:
        lines.append("  fix: the rewrite carries none of this qualification; the original did")
    if hedges["reduced"]:
        lines.append("  reduced (expected when compressing stacked qualifiers, pattern 31):")
        for label, items in hedges["reduced"].items():
            lines.append(f"    {label}: " + ", ".join(items))
        lines.append("    check each against the claim it qualified; a bucket total above")
        lines.append("    zero does not prove the right hedge survived in the right place")
    lines.append("")

    burst = result["burstiness"]
    before, after = burst["before_cv"], burst["after_cv"]
    lines.append("Burstiness (computed, not asserted):")
    lines.append(f"  CV {fmt_cv(before)} -> {fmt_cv(after)}")
    if before is not None and after is not None:
        if after > before:
            lines.append("  ok - sentence-length variation rose")
        elif after < before:
            lines.append("  DOWN - the rewrite is more uniform than the original (pattern 34)")
        else:
            lines.append("  flat - no change")
    lines.append("")

    found = hard_findings(result)
    lines.append("Verdict:")
    if found:
        lines.append("  Hard findings: " + ", ".join(found) + ".")
        lines.append("  This script cannot see meaning. Fix these, then still run the")
        lines.append("  editorial fact check for claims that shifted without losing a token.")
    else:
        lines.append("  No mechanical loss detected.")
        lines.append("  This is not a clean bill of health: a claim can change while every")
        lines.append("  number, name, quote and hedge survives. Run the editorial fact check.")
    return "\n".join(lines)


def main() -> None:
    args = parse_args(sys.argv[1:])
    try:
        original = read_text(args.original)
        rewrite = read_text(args.rewrite)
    except OSError as exc:
        sys.exit(f"error: {exc}")
    result = compare(original, rewrite)
    print(report(result))
    if args.strict and hard_findings(result):
        sys.exit(1)


if __name__ == "__main__":
    main()
