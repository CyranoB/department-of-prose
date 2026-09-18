# Slop Sense

[![skills.sh](https://skills.sh/b/CyranoB/slop-sense)](https://skills.sh/CyranoB/slop-sense)

A three-skill plugin that detects, scores, and explains AI-generated text. Paste text in, get back an analysis of which AI patterns it contains, a rewritten version that sounds human, or a deep-dive on a specific pattern you want to understand.

## The three skills

| Skill | Use when you want to... | Output |
|---|---|---|
| `slop-sense` | Rewrite AI text to sound human | score + named patterns + draft + audit + final rewrite |
| `slop-check` | Just score the text, no rewrite | score + named patterns + one-line evidence per pattern |
| `slop-explain` | Learn why a specific pattern is a tell | per-pattern deep-dive (why LLMs do it, why it reads as AI, how to self-spot) |

All three share the same 36-pattern catalog and the same scoring scripts. They differ in workflow and output.

## What slop-sense does

1. Runs the [slop-detector](https://github.com/CyranoB/slop-detector) algorithmic scorer via `npx` (no install needed, just Node.js). Returns a 0-100 SLOP score with specific word hits, trigram matches, and contrast patterns found.
2. Runs a bundled rhythm checker (`rhythm.py`, pure Python, no dependencies) that measures what the SLOP scorer can't: sentence-length variation (burstiness), contraction ratio, aphoristic paragraph closers, and anaphora. These are the structural tells perplexity detectors like GPTZero score, and a text can rate "very human" on SLOP while failing badly here.
3. Scans for 36 qualitative AI writing patterns: significance inflation, promotional language, AI vocabulary, copula avoidance, em dash overuse, sycophantic tone, invented concept labels, rhetorical Q&A, false vulnerability, uniform sentence rhythm (low burstiness), and more.
4. Rewrites the text with a two-pass process: draft, then an anti-AI audit that catches what the first pass missed.
5. **ai;dr mode**: extracts the probable prompt that generated a piece of AI text, with an inflation ratio showing how many words the AI used to say something simple.

Both scripts are optional. The SLOP scorer needs Node.js; the rhythm checker needs only Python 3. Without either, the skill still does the full qualitative analysis and rewrite.

Accepts pasted text, URLs (fetches and analyzes the page), or file paths.

## What slop-check does

A read-only verdict skill for when you want a score but plan to fix the text yourself (or run it in CI). Same input handling, same 36-pattern scan, same scoring scripts (lexical + rhythm). Output is a compact table of patterns found with one-line evidence per pattern, plus the verdict band. No rewrite, no audit, no edits to your text.

Triggers on requests like "score this," "rate this text," "how AI is this," "verdict only," "don't rewrite, just check."

## What slop-explain does

A teaching skill. Ask "explain pattern 17" or "why is the rule of three a tell" and get a deep-dive on that single pattern: why LLMs produce it, why it reads as AI to a reader, two or three example rewrites, and a checklist for spotting the pattern in your own writing. Pairs naturally with `slop-check` — check flags pattern #17, explain teaches you why it matters.

Triggers on requests like "explain pattern N," "why is X a tell," "teach me about em dash overuse."

## Quickstart

Install the skill with one command. It works for 50+ coding agents:

```bash
npx skills@latest add CyranoB/slop-sense
```

The installer detects your agents, asks which to install for, and places the skill
in the right location.

Common variations:

```bash
npx skills@latest add CyranoB/slop-sense --list
npx skills@latest add CyranoB/slop-sense -a claude-code -y
npx skills@latest add CyranoB/slop-sense -a claude-code -g
```

## Install For Your Coding Tool

Install as a skill/plugin when your agent supports them. The Quickstart command
above is the cross-agent path; per-agent details follow for anyone who wants the
specifics.

<details>
<summary><strong>Claude Code</strong></summary>

Install from the plugin marketplace:

```
/plugin marketplace add CyranoB/slop-sense
/plugin install slop-sense@slop-sense
```

Or install as a skill via the cross-agent command:

```bash
npx skills@latest add CyranoB/slop-sense -a claude-code
```

Install globally instead:

```bash
npx skills@latest add CyranoB/slop-sense -a claude-code -g
```

</details>

<details>
<summary><strong>Codex CLI</strong></summary>

Install all three skills from the plugin marketplace:

```bash
codex plugin marketplace add CyranoB/slop-sense
codex plugin add slop-sense@slop-sense
```

Or install as a skill for the current project:

```bash
npx skills@latest add CyranoB/slop-sense -a codex
```

Install globally instead:

```bash
npx skills@latest add CyranoB/slop-sense -a codex -g
```

</details>

<details>
<summary><strong>Gemini CLI</strong></summary>

Install the skill for the current project:

```bash
npx skills@latest add CyranoB/slop-sense -a gemini-cli
```

Install globally instead:

```bash
npx skills@latest add CyranoB/slop-sense -a gemini-cli -g
```

</details>

<details>
<summary><strong>Pi Coding Agent</strong></summary>

Install the skill for the current project:

```bash
npx skills@latest add CyranoB/slop-sense -a pi
```

Install globally instead:

```bash
npx skills@latest add CyranoB/slop-sense -a pi -g
```

</details>

<details>
<summary><strong>Kiro CLI</strong></summary>

Install the skill for the current workspace:

```bash
npx skills@latest add CyranoB/slop-sense -a kiro-cli
```

Install globally instead:

```bash
npx skills@latest add CyranoB/slop-sense -a kiro-cli -g
```

</details>

<details>
<summary><strong>Other Agent Skills-compatible tools</strong></summary>

```bash
npx skills@latest add CyranoB/slop-sense
```

Direct skill URLs also work:

```bash
npx skills@latest add https://github.com/CyranoB/slop-sense/tree/main/skills/slop-sense
```

</details>

After installing, ask your agent to check any text for AI patterns. The skill
triggers automatically.

## Score interpretation

| Score | Meaning |
|-------|---------|
| 0-20 | Reads like a human wrote it |
| 20-40 | Mostly human, some AI characteristics |
| 40-60 | Could go either way |
| 60-80 | Probably AI-generated |
| 80-100 | Almost certainly AI-generated |

Anything above 30 is worth a second look.

## The 36 patterns

The skill checks for these AI writing tells, grouped by category:

**Content** (1-7): significance inflation, notability name-dropping, superficial -ing analyses, promotional language, vague attributions, formulaic challenges sections, invented concept labels

**Language** (8-16): AI vocabulary overuse, copula avoidance ("serves as" instead of "is"), negative parallelisms, rule of three, synonym cycling, false ranges, anaphora abuse, "not X. not Y. just Z." countdown, rhetorical Q&A

**Style** (17-22): em dash overuse, boldface overuse, inline-header lists, Title Case headings, emojis in structure, curly quotes

**Communication** (23-29): chatbot artifacts, knowledge-cutoff disclaimers, sycophantic tone, "here's the kicker" false suspense, "think of it as..." patronizing analogies, "imagine a world where..." futurism, false vulnerability

**Filler** (30-33): filler phrases, excessive hedging, "the truth is simple" assertions, generic positive conclusions

**Rhythm and Voice** (34-36): uniform sentence rhythm (low burstiness), aphoristic paragraph closers, reflexive formality (contraction avoidance). These are the tells lexical scorers miss and perplexity detectors like GPTZero live on; the bundled `rhythm.py` measures them.

Based on [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), the [EQBench SLOP score](https://eqbench.com/slop-score.html) methodology, and [tropes.fyi](https://tropes.fyi/).

## Credits

Algorithmic scorer: [slop-detector](https://github.com/CyranoB/slop-detector), built on [slop-score](https://github.com/sam-paech/slop-score) by Samuel J. Paech.

AI writing patterns: [WikiProject AI Cleanup](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_AI_Cleanup).

Additional tropes: [tropes.fyi](https://tropes.fyi/) by Ossama.

Humanizer methodology: [blader/humanizer](https://github.com/blader/humanizer).

## License

MIT
