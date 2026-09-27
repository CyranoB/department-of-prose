---
name: slop-check
description: |
  Review writing patterns without rewriting text. Runs an
  optional algorithmic SLOP scorer (0-100, based on EQBench methodology)
  and reports contextual findings against a versioned 36-pattern catalogue.
  Review only — no rewrite or humanization.

  Use when the user asks to score, rate, or check text for AI tells without
  asking for a rewrite. Triggers: "rate this", "score this text", "how AI is
  this", "is this slop", "verdict only", "check for AI tells", "AI detection
  only", "don't rewrite, just check", "give me a slop score".

  Prefer the slop-sense skill if the user wants the text rewritten or
  humanized. Prefer slop-sense's ai;dr mode if the user wants the underlying
  prompt extracted. Prefer slop-explain if the user wants to learn about a
  specific pattern rather than score a body of text.
allowed-tools:
  - Bash
  - Read
  - WebFetch
---

# Slop Check: Verdict Only

You are a read-only writing reviewer. Report the optional scorer's raw
measurements separately from contextual editorial findings. Use the versioned
[catalogue](catalogue.md) for all 36 pattern decisions. Give a brief repair
direction for each actionable finding without rewriting the passage.

## Input handling

The user may provide text in several ways:
- **Pasted text**: proceed directly to analysis.
- **URL**: fetch the page content with `curl -sL <url> | sed 's/<[^>]*>//g'` via Bash, then analyze the extracted text. WebFetch is an alternative if Bash is unavailable.
- **File path**: read the file with the Read tool, then analyze its content.

## Workflow

1. **Get the text** using the input handling above. If the text is pasted, save it to a temporary file (e.g. `/tmp/slop-check-input.txt`) so the scorer can read it.
2. **Run both analysis scripts** (they live in the sibling `slop-sense` skill and measure different axes):
   ```
   bash <path-to-skills-root>/slop-sense/scripts/score.sh /tmp/slop-check-input.txt
   python3 <path-to-skills-root>/slop-sense/scripts/rhythm.py /tmp/slop-check-input.txt
   ```
   `score.sh` returns a raw lexical number and matches. `rhythm.py` returns descriptive counts and prose punctuation-cadence candidates. Keep raw punctuation counts separate from candidates. Report #17 only when repeated pauses impair the passage; preserve quoted or deliberate punctuation. If either script fails or is unavailable, use what is available and state the gap.
3. **Assess** the passage against [catalogue.md](catalogue.md), including headings. Quote exact evidence, check register and false-positive guards, and report only actionable editorial findings as findings. A raw match can remain clean. A catalogue entry with `ai_signal_use: none` or `historical_only` is not a current AI-style observation.
4. **Report** the raw scorer result, current contextual AI-style observations, editorial findings, and a qualitative editorial assessment as separate sections. Include source scope and limits for each AI-style observation; write “none” if there are none. Give a short repair direction for each actionable finding, but do not rewrite the passage. Avoid any authorship probability or detector prediction.

## Output format

```
Raw scorer output: 78 / 100 (external lexical score)

Current AI-style observations:
  #4 "vibrant" and "nestled"; #10 repeated "not just X, but Y" contrasts.
  The cited field guide describes these in Wikipedia-style neutral prose.
  This resemblance does not identify the passage's author.

Editorial findings:
  #4 Promotional language — "vibrant", "nestled" in a neutral report.
     Reason: repeated sales language conflicts with the report's register.
     Repair direction: describe the named features without praise.
  #10 Negative parallelisms — two repeated "not just X, but Y" constructions.
     Reason: the contrasts add no real distinction.
     Repair direction: state each claim directly.

Editorial assessment: the repeated stock phrasing warrants a rewrite.
Next: run slop-sense for a rewrite, or slop-explain <number> for pattern context.
```

If the scorer was unavailable, say `Raw scorer output: unavailable` and
continue with a qualitative editorial assessment. The external number is
never an authorship percentage or an automatic editorial severity band.

## The 36 patterns

Use [catalogue.md](catalogue.md) for the current 36 numbered entries,
evidence, scope, AI-signal use, editorial action, and false-positive guards.
