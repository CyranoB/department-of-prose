# The Department of Prose

![A goblin clerk reduces a wizard’s extravagant love letter to “Fancy a shag?”, delighting its recipient.](assets/header.webp)

[![skills.sh](https://skills.sh/b/CyranoB/department-of-prose)](https://skills.sh/CyranoB/department-of-prose)

The Department of Prose occupies a small office between what you wrote and what you meant. Its staff were originally employed to remove unnecessary words, but the arrival of artificial intelligence has required a second kettle.

Documents are inspected for inflated importance, unlicensed metaphors, and conclusions which have continued trading after the point has closed. Most can be returned to their owners in working order. Occasionally a paragraph must be taken outside and quietly reduced to a sentence.

A plugin for Claude Code and Codex with three writing skills:
`slop-check` reviews text, `slop-explain` explains patterns, and
`slop-sense` rewrites actionable findings. The optional scorer's raw
measurements stay separate from contextual editorial judgments. Accepts
pasted text, URLs, or files.

## The three skills

| Skill | Use when you want to... | Output |
|---|---|---|
| `slop-sense` | Revise specific writing problems | raw score + evidence-backed findings + fact-safe rewrite |
| `slop-check` | Review the text without rewriting it | raw score + evidence-backed findings + brief repair directions |
| `slop-explain` | Understand one numbered pattern | source, evidence limit, legitimate uses, and editing advice |

All three use version 1.0.0 of the [editorial catalogue](skills/slop-sense/catalogue.md).
The external lexical scorer is separately versioned and optional.

## What slop-sense does

1. Runs the [slop-detector](https://github.com/CyranoB/slop-detector) algorithmic scorer via `npx` (no install needed, just Node.js). Returns a 0-100 SLOP score with specific word hits, trigram matches, and contrast patterns found.
2. Runs a bundled rhythm checker (`rhythm.py`, pure Python, no dependencies) that measures sentence-length variation, contraction ratio, paragraph-closer candidates, anaphora, raw punctuation counts, and prose punctuation-cadence candidates. These are descriptive measurements.
3. Assesses 36 numbered editorial patterns using the catalogue's source, scope, and false-positive guard. A raw match can remain clean.
4. Rewrites actionable findings with a draft, fact-preservation check, final revision, and a compact before/after verification on the settled text.
5. **ai;dr mode**: extracts the probable prompt that generated a piece of AI text, with an inflation ratio showing how many words the AI used to say something simple.

Both scripts are optional. The SLOP scorer needs Node.js; the rhythm checker needs only Python 3. Without either, the skill still does the full qualitative analysis and rewrite.

Accepts pasted text, URLs (fetches and analyzes the page), or file paths.

## Evaluation

The repository includes a two-layer evaluation set: deterministic regression
fixtures for measurements, extraction, CLI behavior, wrapper behavior, and the
exact pinned scorer; plus rubric-reviewed golden rewrite cases for contextual
judgment, fact preservation, and voice. Run the deterministic suite with:

```bash
npm ci
npm run evaluate
```

See [`evaluation/README.md`](evaluation/README.md) for the coverage inventory,
known expected failures, scorer-upgrade policy, and golden review procedure.

## What slop-check does

A read-only review skill for when you want to inspect the text and make the
edits yourself. It reports the optional raw score separately from
contextual findings. Each actionable finding has exact evidence, a reason,
and a brief repair direction. It does not rewrite your text.

Triggers on requests like "score this," "rate this text," "how AI is this," "verdict only," "don't rewrite, just check."

## What slop-explain does

A teaching skill. Ask "explain pattern 17" to see its source, evidence
limits, legitimate uses, and when a repair helps. Some patterns remain
useful editorial advice without being current AI-style signals.

Triggers on requests like "explain pattern N," "why is X a tell," "teach me about em dash overuse."

## Upgrading from Slop Sense

Version 3.0.0 renames the plugin and marketplace to `department-of-prose`. Existing users should remove the old `slop-sense` plugin and marketplace registration in their client, then follow the installation instructions below using `CyranoB/department-of-prose` and `department-of-prose@department-of-prose`.

The individual skill names remain `slop-sense`, `slop-check`, and `slop-explain`.

## Quickstart

**Establish a local branch of the Department.**

Install the skill with one command. It works for 50+ coding agents:

```bash
npx skills@latest add CyranoB/department-of-prose
```

The installer detects your agents, asks which to install for, and places the skill
in the right location.

Common variations:

```bash
npx skills@latest add CyranoB/department-of-prose --list
npx skills@latest add CyranoB/department-of-prose -a claude-code -y
npx skills@latest add CyranoB/department-of-prose -a claude-code -g
```

## Install For Your Coding Tool

Install as a skill/plugin when your agent supports them. The Quickstart command
above is the cross-agent path; per-agent details follow for anyone who wants the
specifics.

<details>
<summary><strong>Claude Code</strong></summary>

Install from the plugin marketplace:

```
/plugin marketplace add CyranoB/department-of-prose
/plugin install department-of-prose@department-of-prose
```

Or install as a skill via the cross-agent command:

```bash
npx skills@latest add CyranoB/department-of-prose -a claude-code
```

Install globally instead:

```bash
npx skills@latest add CyranoB/department-of-prose -a claude-code -g
```

</details>

<details>
<summary><strong>Codex CLI</strong></summary>

Install all three skills from the plugin marketplace:

```bash
codex plugin marketplace add CyranoB/department-of-prose
codex plugin add department-of-prose@department-of-prose
```

Or install as a skill for the current project:

```bash
npx skills@latest add CyranoB/department-of-prose -a codex
```

Install globally instead:

```bash
npx skills@latest add CyranoB/department-of-prose -a codex -g
```

</details>

<details>
<summary><strong>Gemini CLI</strong></summary>

Install the skill for the current project:

```bash
npx skills@latest add CyranoB/department-of-prose -a gemini-cli
```

Install globally instead:

```bash
npx skills@latest add CyranoB/department-of-prose -a gemini-cli -g
```

</details>

<details>
<summary><strong>Pi Coding Agent</strong></summary>

Install the skill for the current project:

```bash
npx skills@latest add CyranoB/department-of-prose -a pi
```

Install globally instead:

```bash
npx skills@latest add CyranoB/department-of-prose -a pi -g
```

</details>

<details>
<summary><strong>Kiro CLI</strong></summary>

Install the skill for the current workspace:

```bash
npx skills@latest add CyranoB/department-of-prose -a kiro-cli
```

Install globally instead:

```bash
npx skills@latest add CyranoB/department-of-prose -a kiro-cli -g
```

</details>

<details>
<summary><strong>Other Agent Skills-compatible tools</strong></summary>

```bash
npx skills@latest add CyranoB/department-of-prose
```

Direct skill URLs also work:

```bash
npx skills@latest add https://github.com/CyranoB/department-of-prose/tree/main/skills/slop-sense
```

</details>

After installing, ask your agent to check any text for AI patterns. The skill
triggers automatically.

## Score interpretation

The optional 0–100 SLOP score is the external scorer's **raw lexical metric**.
It counts selected words, trigrams, and constructions in its own corpus-based
model. It is not an authorship percentage, an editorial severity band, or a
reason by itself to rewrite a passage. Read its exact matches alongside the
passage's length, meaning, register, and the catalogue's false-positive guards.
The rhythm script's counts are likewise descriptive.

Reports keep three things distinct: raw scorer output, actionable editorial
findings, and any source-supported current AI-style observations. An editorial
problem can need a repair without being an AI-writing signal. No report infers
who wrote the text from these patterns. See [EQ-Bench's own limits](https://eqbench.com/slop-score.html).

## The 36 patterns

The versioned [editorial catalogue](skills/slop-sense/catalogue.md) lists each
numbered pattern's source, evidence limit, current AI-signal use, editorial
action, and false-positive guard. The [source audit](docs/pattern-catalogue-source-audit.md)
records the review of the 36 patterns. Pattern #12 (synonym cycling) is a
historical AI association that can still warrant a clarity edit. Pattern #22
(curly quotes) is retired as an AI indicator. Pattern #29 now uses the name
“Disclosure without substance”; its former name remains a lookup alias.

The catalogue version is independent of the plugin version and the pinned
external scorer version. Each change to its words or pattern decisions
requires a source review, a change record, and updated distribution copies.

## Credits

Algorithmic scorer: [slop-detector](https://github.com/CyranoB/slop-detector), built on [slop-score](https://github.com/sam-paech/slop-score) by Samuel J. Paech.

AI writing patterns: [WikiProject AI Cleanup](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_AI_Cleanup).

Additional tropes: [tropes.fyi](https://tropes.fyi/) by Ossama.

Humanizer methodology: [blader/humanizer](https://github.com/blader/humanizer).

## License

MIT
