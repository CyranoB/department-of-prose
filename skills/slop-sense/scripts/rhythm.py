#!/usr/bin/env python3
"""
rhythm.py - structural writing-pattern checker for slop-sense.

The bundled `score.sh` (slop-detector) measures lexical matches: slop words,
trigrams, and contrast phrases. It does not measure rhythm or register.

This script measures the dimensions score.sh can't see, so the model has ground
truth instead of having to eyeball them:

  - Burstiness: sentence-length variation
  - Contraction ratio: contractions vs. uncontracted "do not / it is" forms
  - Aphoristic closers: paragraphs ending on a short, balanced kicker (pattern 35)
  - Anaphora runs: consecutive sentences opening with the same word (pattern 14)
  - Em dashes & curly quotes: typographic observations (patterns 17, 22)

All thresholds are editing heuristics, not authorship verdicts. Treat the numbers
as prompts to inspect frequency, context, and effect in the passage.

Usage:
    python3 rhythm.py <file>
    cat file.md | python3 rhythm.py
"""

import re
import sys
import statistics

# --- input handling ---------------------------------------------------------

def read_input(argv):
    if len(argv) > 1:
        with open(argv[1], "r", encoding="utf-8") as f:
            return f.read()
    if not sys.stdin.isatty():
        return sys.stdin.read()
    sys.exit("usage: python3 rhythm.py <file>   (or pipe text via stdin)")


def strip_markdown(text):
    """Drop fenced code blocks and light formatting so they don't pollute
    word counts. Paragraph and sentence structure is preserved."""
    text = re.sub(r"```.*?```", "", text, flags=re.S)        # fenced code
    text = re.sub(r"`[^`]*`", "", text)                       # inline code
    text = re.sub(r"^---\s*$.*", "", text, flags=re.S | re.M) # trailing hr/footer onward kept simple
    lines = []
    for line in text.splitlines():
        if line.lstrip().startswith("#"):      # headings: keep as paragraph breaks, not prose
            lines.append("")
            continue
        line = re.sub(r"\*\*([^*]+)\*\*", r"\1", line)  # bold
        line = re.sub(r"\*([^*]+)\*", r"\1", line)        # italic
        line = re.sub(r"^\s*[-*+]\s+", "", line)           # list bullets
        line = re.sub(r"^\s*>\s?", "", line)               # blockquotes
        lines.append(line)
    return "\n".join(lines)


# --- sentence / paragraph segmentation --------------------------------------

ABBREV = {"mr", "mrs", "ms", "dr", "st", "vs", "etc", "inc", "ltd", "co",
          "jan", "feb", "mar", "apr", "jun", "jul", "aug", "sep", "sept",
          "oct", "nov", "dec", "u.s", "e.g", "i.e", "no"}

def split_sentences(block):
    # Protect decimals/money ("$2.3 billion", "12.5") and known abbreviations
    # so their periods don't trigger a split.
    protected = re.sub(r"(\d)\.(\d)", r"\1<DOT>\2", block)
    for ab in ABBREV:
        protected = re.sub(rf"(?i)\b{re.escape(ab)}\.", ab + "<DOT>", protected)
    parts = re.split(r'(?<=[.!?])["\'”’]?\s+(?=["\'“‘]?[A-Z0-9])', protected)
    out = []
    for p in parts:
        p = p.replace("<DOT>", ".").strip()
        if p:
            out.append(p)
    return out


def word_count(sentence):
    return len(re.findall(r"\b[\w']+\b", sentence))


def paragraphs(text):
    blocks = re.split(r"\n\s*\n", text)
    return [b.strip() for b in blocks if b.strip()]


# --- metrics ----------------------------------------------------------------

CONTRACTION_RE = re.compile(r"\b\w+['’](t|s|re|ve|ll|d|m)\b", re.I)
FORMAL_FORMS = [
    r"\bdo not\b", r"\bdoes not\b", r"\bdid not\b", r"\bis not\b", r"\bare not\b",
    r"\bwas not\b", r"\bwere not\b", r"\bhas not\b", r"\bhave not\b", r"\bhad not\b",
    r"\bwill not\b", r"\bwould not\b", r"\bshould not\b", r"\bcould not\b",
    r"\bcan not\b", r"\bcannot\b", r"\bmust not\b",
    r"\bit is\b", r"\bthat is\b", r"\bthere is\b", r"\bthey are\b", r"\byou are\b",
    r"\bwe are\b", r"\bI am\b", r"\bwhat is\b", r"\bwho is\b", r"\blet us\b",
]
FORMAL_RE = re.compile("|".join(FORMAL_FORMS), re.I)

SUMMARY_NOUNS = {"argument", "story", "point", "truth", "difference", "question",
                 "answer", "matter", "matters", "problem", "choice", "fate",
                 "prize", "dividend", "sovereignty", "future", "beginning",
                 "end", "game", "thing", "miniature", "foundation"}


def burstiness(lengths):
    if len(lengths) < 2:
        return 0.0, 0.0, 0.0
    mean = statistics.mean(lengths)
    sd = statistics.pstdev(lengths)
    cv = sd / mean if mean else 0.0
    return mean, sd, cv


def contraction_stats(text):
    c = len(CONTRACTION_RE.findall(text))
    f = len(FORMAL_RE.findall(text))
    ratio = c / (c + f) if (c + f) else 0.0
    return c, f, ratio


def _is_generalization(segment):
    low = segment.lower()
    has_copula = re.search(r"\b(is|are|was|were)\b", low) is not None
    ends_summary = any(low.rstrip(".!?\"' ").endswith(n) for n in SUMMARY_NOUNS)
    has_neg = re.search(r"\bnot\b", low) is not None
    return has_copula or ends_summary or has_neg


def aphoristic_closers(paras):
    """Surface candidate paragraph-ending kickers. Two forms catch the common
    AI shapes: a short punchy closer, and a long sentence resolving into a short
    balanced tail after the final comma ("..., and the difference is the entire
    argument"). This is the noisiest signal in the script: deliberate short
    fragments are good writing, not tells. The point is to read the closers as a
    *set* — the tell is when many paragraphs land the same way and the lines feel
    interchangeable, not any single one."""
    flagged = []
    multi = [p for p in paras if split_sentences(p)]
    for p in multi:
        last = split_sentences(p)[-1]
        wc = word_count(last)
        if wc == 0:
            continue
        if wc <= 14 and _is_generalization(last):
            flagged.append(("short", wc, last))
        elif wc > 14 and "," in last:
            tail = last.rsplit(",", 1)[1].strip()
            if 0 < word_count(tail) <= 10 and _is_generalization(tail):
                flagged.append(("tail", wc, last))
    return flagged, len(multi)


def anaphora_runs(sentences, min_run=3):
    firsts = []
    for s in sentences:
        m = re.match(r"\s*([A-Za-z']+)", s)
        firsts.append(m.group(1).lower() if m else None)
    runs = []
    i = 0
    n = len(firsts)
    while i < n:
        j = i
        while j + 1 < n and firsts[j + 1] and firsts[j + 1] == firsts[i]:
            j += 1
        if firsts[i] and (j - i + 1) >= min_run:
            runs.append((firsts[i], j - i + 1))
        i = j + 1
    return runs


# --- report -----------------------------------------------------------------

def band(cv):
    if cv < 0.40:
        return "LOW VARIATION — sentence lengths cluster closely"
    if cv < 0.55:
        return "MODERATE VARIATION — sentence lengths vary somewhat"
    return "HIGH VARIATION — sentence lengths vary widely"


def main():
    raw = read_input(sys.argv)
    text = strip_markdown(raw)
    paras = paragraphs(text)
    sentences = [s for p in paras for s in split_sentences(p)]
    lengths = [word_count(s) for s in sentences if word_count(s) > 0]

    print("=== Rhythm & Structure Analysis ===\n")
    print(f"Paragraphs: {len(paras)} | Sentences: {len(sentences)}\n")

    if not lengths:
        print("No prose sentences found.")
        return

    mean, sd, cv = burstiness(lengths)
    short = sum(1 for w in lengths if w <= 8)
    long_ = sum(1 for w in lengths if w >= 30)
    print("Burstiness (sentence-length variation):")
    print(f"  mean {mean:.1f}w  stddev {sd:.1f}  CV {cv:.2f}  <- {band(cv)}")
    print(f"  short (<=8w): {short}    long (>=30w): {long_}")
    print(f"  shortest {min(lengths)}w   longest {max(lengths)}w")
    if cv < 0.40:
        print("  fix: put short sentences next to long ones; break up uniform runs (pattern 34)")
    print()

    c, f, ratio = contraction_stats(text)
    print("Contractions vs. formal forms:")
    print(f"  contractions: {c}    uncontracted (do not / it is / cannot): {f}    ratio {ratio:.2f}")
    if c == 0 and f > 0:
        print("  review: no contractions; check whether this fits the passage's intended register (pattern 36)")
    print()

    closers, n_par = aphoristic_closers(paras)
    print("Paragraph closers (pattern 35) — read these as a set, not individually:")
    print(f"  {len(closers)}/{n_par} paragraphs resolve into a balanced kicker")
    for kind, wc, txt in closers[:10]:
        snippet = txt if len(txt) <= 72 else "..." + txt[-69:]
        print(f"    [{kind} {wc}w] {snippet}")
    if n_par and len(closers) / n_par > 0.5:
        print("  the tell is the relentlessness: if these feel interchangeable, vary the endings (pattern 35)")
    else:
        print("  (a handful is fine; the tell is when most paragraphs land the same way)")
    print()

    runs = anaphora_runs(sentences)
    print("Anaphora runs (pattern 14):")
    if runs:
        for word, length in runs:
            print(f"  {length} consecutive sentences open with \"{word}\"")
        print("  fix: vary sentence openings; combine related points")
    else:
        print("  none (no 3+ consecutive sentences with the same opening word)")
    print()

    em = raw.count("—") + len(re.findall(r"(?<!-)--(?!-)", raw))
    curly = raw.count("“") + raw.count("”") + raw.count("‘") + raw.count("’")
    print("Typographic observations:")
    print(f"  em dashes (— or --): {em}   curly quotes: {curly}")
    if em:
        print("  review: inspect dash frequency and effect; isolated uses may fit the passage (pattern 17)")
    if curly:
        print("  review: make quote style consistent with the document's house style (pattern 22)")
    print()

    # --- synthesized summary ---
    flags = []
    if cv < 0.40:
        flags.append("low burstiness")
    if c == 0 and f > 0:
        flags.append("no contractions")
    if n_par and len(closers) / n_par > 0.5:
        flags.append("relentless aphoristic closers")
    if runs:
        flags.append("anaphora")
    if em:
        flags.append("em dashes")
    print("Structural pattern summary:")
    if flags:
        print(f"  Review in context: {', '.join(flags)}.")
        print("  score.sh does not measure these dimensions; assess their frequency and effect separately.")
    else:
        print("  No strong structural patterns under these heuristic thresholds.")
        print("  This result does not establish authorship or overall writing quality.")


if __name__ == "__main__":
    main()
