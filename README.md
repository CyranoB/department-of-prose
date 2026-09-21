# The Department of Prose

![A goblin clerk reduces a wizard’s extravagant love letter to “Fancy a shag?”, delighting its recipient.](assets/header.webp)

[![skills.sh](https://skills.sh/b/CyranoB/department-of-prose)](https://skills.sh/CyranoB/department-of-prose)

> The Department of Prose believes every sentence should say what it means, a principle widely supported until it is applied to love letters. Several promising courtships have survived the removal of “celestial.” Fewer have survived the plain-language summary.

A plugin for Claude Code and Codex with three writing skills: `slop-check` flags and scores recurring patterns associated with formulaic or AI-like prose, `slop-explain` explains them, and `slop-sense` rewrites the text. Accepts pasted text, URLs, or files.

## The three skills

| Skill | Use when you want to... | Output |
|---|---|---|
| `slop-sense` | Rewrite formulaic text in a more natural voice | score + named patterns + draft + audit + final rewrite |
| `slop-check` | Just score the text, no rewrite | score + named patterns + one-line evidence per pattern |
| `slop-explain` | Learn why a specific pattern matters | per-pattern deep-dive (why LLMs may produce it, why readers notice it, how to self-spot) |

All three share the same 36-pattern catalog and the same scoring scripts. They differ in workflow and output.

## What slop-sense does

1. Runs the [slop-detector](https://github.com/CyranoB/slop-detector) algorithmic scorer via `npx` (no install needed, just Node.js). Returns a 0-100 SLOP score with specific word hits, trigram matches, and contrast patterns found.
2. Runs a bundled rhythm checker (`rhythm.py`, pure Python, no dependencies) that measures what the SLOP scorer can't: sentence-length variation (burstiness), contraction ratio, aphoristic paragraph closers, and anaphora. These measurements add structural context to the lexical score; neither script determines who wrote the text.
3. Scans for 36 qualitative writing patterns associated with formulaic or AI-like prose: significance inflation, promotional language, AI vocabulary, copula avoidance, em dash overuse, sycophantic tone, invented concept labels, rhetorical Q&A, false vulnerability, uniform sentence rhythm (low burstiness), and more.
4. Rewrites the text with a two-pass process: draft, then a pattern audit that catches what the first pass missed.
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

A read-only verdict skill for when you want a score but plan to fix the text yourself (or run it in CI). Same input handling, same 36-pattern scan, same scoring scripts (lexical + rhythm). Output is a compact table of patterns found with one-line evidence per pattern, plus the verdict band. No rewrite, no audit, no edits to your text.

Triggers on requests like "score this," "rate this text," "how AI is this," "verdict only," "don't rewrite, just check."

## What slop-explain does

A teaching skill. Ask "explain pattern 17" or "why is the rule of three a tell" and get a deep-dive on that single pattern: why LLMs may produce it, why readers notice it, two or three example rewrites, and a checklist for spotting the pattern in your own writing. Pairs naturally with `slop-check` — check flags pattern #17, explain teaches you why it matters.

Triggers on requests like "explain pattern N," "why is X a tell," "teach me about em dash overuse."

## Upgrading from Slop Sense

Version 3.0.0 renames the plugin and marketplace to `department-of-prose`. Existing users should remove the old `slop-sense` plugin and marketplace registration in their client, then follow the installation instructions below using `CyranoB/department-of-prose` and `department-of-prose@department-of-prose`.

The individual skills remain `slop-sense`, `slop-check`, and `slop-explain`; their names and behavior are unchanged.

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

The SLOP score measures the density of catalogued words, phrases, and constructions. It is pattern evidence, not an estimate of the probability that AI wrote the text.

| Score | Pattern evidence | Practical reading |
|-------|------------------|-------------------|
| 0-19 | Minimal | Few catalogued patterns; review any isolated findings in context |
| 20-39 | Light | Some recurring patterns may be worth editing |
| 40-59 | Moderate | Several patterns recur or cluster in the passage |
| 60-79 | Strong | Frequent or concentrated patterns are likely to affect the prose |
| 80-100 | Pervasive | Catalogued patterns dominate substantial parts of the passage |

Use the score to decide where to look, then judge each finding by its frequency, context, and effect on the passage. Short samples can swing sharply. Technical, legal, medical, academic, and non-English text may not fit the scorer's English-language catalogue. Deliberate repetition or formality can also raise the score. A high score does not prove AI authorship or poor writing, and a low score does not prove human authorship or good writing.

## The 36 patterns

The skill checks for these AI writing tells, grouped by category:

**Content** (1-7): significance inflation, notability name-dropping, superficial -ing analyses, promotional language, vague attributions, formulaic challenges sections, invented concept labels

**Language** (8-16): AI vocabulary overuse, copula avoidance ("serves as" instead of "is"), negative parallelisms, rule of three, synonym cycling, false ranges, anaphora abuse, "not X. not Y. just Z." countdown, rhetorical Q&A

**Style** (17-22): em dash overuse, boldface overuse, inline-header lists, Title Case headings, emojis in structure, curly quotes

**Communication** (23-29): chatbot artifacts, knowledge-cutoff disclaimers, sycophantic tone, "here's the kicker" false suspense, "think of it as..." patronizing analogies, "imagine a world where..." futurism, false vulnerability

**Filler** (30-33): filler phrases, excessive hedging, "the truth is simple" assertions, generic positive conclusions

**Rhythm and Voice** (34-36): uniform sentence rhythm (low burstiness), aphoristic paragraph closers, reflexive formality (contraction avoidance). The lexical scorer does not measure these features; the bundled `rhythm.py` reports them as separate editorial evidence.

Based on [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), the [EQBench SLOP score](https://eqbench.com/slop-score.html) methodology, and [tropes.fyi](https://tropes.fyi/).

## Credits

Algorithmic scorer: [slop-detector](https://github.com/CyranoB/slop-detector), built on [slop-score](https://github.com/sam-paech/slop-score) by Samuel J. Paech.

AI writing patterns: [WikiProject AI Cleanup](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_AI_Cleanup).

Additional tropes: [tropes.fyi](https://tropes.fyi/) by Ossama.

Humanizer methodology: [blader/humanizer](https://github.com/blader/humanizer).

## License

MIT
