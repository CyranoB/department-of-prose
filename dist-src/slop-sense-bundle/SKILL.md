---
name: slop-sense
description: |
  Review, rewrite, and explain 36 numbered writing patterns. Keep the
  optional raw scorer separate from contextual editorial findings. Four modes:
  (1) Rewrite — revise actionable findings. Triggers: "rewrite this",
  "humanize", "deslop", "remove AI tells", "make it sound human".
  (2) Verdict only — report raw score and editorial findings, no rewrite. Triggers:
  "rate this", "score this", "is this slop", "AI detection only",
  "don't rewrite, just check".
  (3) Pattern deep-dive — explain one of the 36 patterns. Triggers:
  "explain pattern N", "what is significance inflation", "tell me about
  em dash overuse", "why do LLMs use 'delve'".
  (4) ai;dr — extract the probable prompt behind AI text. Triggers:
  "ai;dr", "what was this AI asked to write", "extract the prompt".
allowed-tools:
  - Bash
  - Read
  - Write
  - Edit
  - WebFetch
---

# Slop Sense

A bundled writing editor that reports raw scoring separately from contextual
editorial findings. The versioned [catalogue](catalogue.md) is the authority
for pattern evidence, AI-signal status, editorial action, and false-positive
guards. Neither the scorer nor the catalogue identifies the author.

## How to dispatch

First, pick the mode that matches the user's request. If multiple could apply, ask.

| Signal in the user's message | Mode | Jump to |
|---|---|---|
| Pastes text + asks to rewrite, humanize, deslop, fix, edit, make human | **Rewrite** | [Mode 1](#mode-1-rewrite) |
| Says "ai;dr", "extract the prompt", "what was this AI asked to write" | **ai;dr** | [ai;dr mode](#aidr-mode) |
| Pastes text + asks to rate, score, check, detect, "is this AI", "verdict only" | **Verdict only** | [Mode 2](#mode-2-verdict-only) |
| Asks to explain pattern N, what a specific pattern is, why LLMs do X | **Pattern deep-dive** | [Mode 3](#mode-3-pattern-deep-dive) |

If the request is ambiguous (e.g. "check this" — could be rewrite or verdict), ask which one before doing work. Default to **Rewrite** only when the user explicitly says "fix" or pastes text with no instruction.

## Input handling (Modes 1, 2, and ai;dr)

The user may provide text in several ways:
- **Pasted text** — proceed directly to analysis.
- **URL** — fetch the page first with `curl -sL <url> | sed 's/<[^>]*>//g'` via Bash, then analyze the extracted text. WebFetch is an alternative if Bash is unavailable.
- **File path** — read the file with the Read tool, then analyze its content.

## Running the analysis scripts

Two scripts ship in this skill's `scripts/` directory and measure different, complementary axes. Run both when available.

```bash
bash scripts/score.sh /tmp/slop-input.txt        # lexical: slop words, trigrams, contrast phrases
python3 scripts/rhythm.py /tmp/slop-input.txt     # descriptive: rhythm, punctuation counts and cadence candidates
```

(Save pasted text to `/tmp/slop-input.txt` first. If running from outside the skill directory, use absolute paths.)

`score.sh` wraps `npx slop-detector` and is optional. If it fails or exits
with `SCORER_NOT_AVAILABLE`, say `Raw scorer output: unavailable` and
continue qualitatively. `rhythm.py` is pure Python. Its measurements are
descriptive; neither script's numbers are authorship probabilities or
automatic editorial severity bands.

---

## Mode 1: Rewrite

Edit actionable findings using [catalogue.md](catalogue.md). A raw scorer hit
can remain clean. A pattern with no current AI association can still warrant
an editorial repair when the passage itself has a problem.

### Workflow

1. Get the text and run both optional scripts. Label their output as raw
   measurements. Keep only the score, hits, and measurements needed for the
   final comparison; a punctuation-cadence candidate is not an edit instruction.
2. Read the catalogue. For each candidate finding, quote the exact passage,
   check its false-positive guard and the document register, and explain why
   this instance needs a change. Keep current AI-style observations separate
   from editorial findings.
3. Rewrite only actionable findings. Preserve names, numbers, dates, sources,
   quotations, qualifications, scope limits, and the author's deliberate voice.
   If a safe repair needs facts the input lacks, mark the gap instead of
   inventing them.
4. Audit the draft against the original and catalogue. Repair stock phrasing
   introduced by the draft and inspect cadence candidates in context. Settle
   the wording before final script checks.
5. Fact check the settled version against the original for added, omitted,
   or strengthened claims, including quotations and scope limits.
6. If the final text is unchanged, reuse the source results. Otherwise run
   each available script once on the exact final text after the fact check.
   Compare source and final scores, relevant hits, rhythm measurements, and
   contextual findings. An audit rhythm result may be reused only when it
   checked the exact final text. State when either script was unavailable.
7. Present the current contextual AI-style observations with source limits,
   editorial findings, final rewrite, fact check, and a compact before/after
   comparison of improvements, regressions, and findings deliberately kept.

A quoted phrase belongs to its speaker. Keep quoted wording intact and edit
only the surrounding text. A technical term with an exact meaning stays even
when the raw lexical scorer matches it. For #12, a confusing synonym can be
fixed for clarity without calling it a current AI signal. For #17, repeated
dashes can be edited for readability without treating them as authorship
evidence. #22 is retired as an AI pattern; preserve supplied typography unless
the output format requires a change.

### Output format

1. **Raw scorer output:** external number and matches if available; otherwise
   state that it was unavailable.
2. **Current AI-style observations:** only `current_contextual` entries with
   exact passages and source limits; state “none” if there are none.
3. **Editorial findings:** actionable pattern IDs, exact supporting passages,
   reasons, and safe repair directions. Give a qualitative editorial assessment.
4. **Draft and final rewrite:** show the revision and its final audited form.
5. **Fact check:** confirm the final version adds, omits, or strengthens no
   claims; list any unresolved gap explicitly.
6. **Before/after check:** show the score once as a source-to-final pair when
   available, plus relevant measurement and finding changes. Omit unchanged
   raw detail and state when a script comparison is unavailable.

Preserve the voice the author actually used. Do not add an opinion, personal
experience, or contraction merely to make a passage look less formal.

---

## Mode 2: Verdict only

Review without rewriting. Give a short repair direction for each actionable
editorial finding while leaving the supplied passage intact.

1. Get the text and run both optional scripts. Report their outputs as raw
   measurements and state when either is unavailable.
2. Read [catalogue.md](catalogue.md), including its #8 vocabulary and guards.
   Scan headings and body text. Quote exact evidence and explain why an
   editorial candidate is actionable in this passage. A raw match can remain
   clean. An entry with `ai_signal_use: none` or `historical_only` is
   not a current AI-style observation.
3. Report current contextual AI-style observations with source limits,
   editorial findings, a qualitative editorial assessment, and brief repair
   directions. State “none” when there are no AI-style observations.
   Do not rewrite text or claim a probability of AI authorship.

Example:

```text
Raw scorer output: 78 / 100 (external lexical score)
Current AI-style observations:
  #4 "vibrant" and "nestled"; #10 repeated "not just X, but Y" contrasts.
  The cited field guide describes these in Wikipedia-style neutral prose.
  This resemblance does not identify the passage's author.
Editorial findings:
  #4 Promotional language — "vibrant" and "nestled" in a neutral report.
     Repair direction: describe the named features without praise.
  #10 Negative parallelisms — two repeated stock contrasts.
     Repair direction: state each claim directly.
Editorial assessment: the repeated stock phrasing warrants a rewrite.
```

---

## Mode 3: Pattern deep-dive

Use [catalogue.md](catalogue.md) for the pattern's source, AI-signal status,
editorial action, scope, and false-positive guard. Read its `patterns/NN-name.md`
file for a concise evidence note. Explain the evidence limit and any safe
repair. Give one short invented example that fits the trigger and one that
stays clean under the guard; label both as illustrative. A retired entry
explains why the old AI signal was withdrawn.

### Pattern lookup table

| # | Canonical name | File slug | Common synonyms |
|---|---|---|---|
| 1 | Significance inflation | `01-significance-inflation` | "stands as", "testament to", "evolving landscape" |
| 2 | Notability name-dropping | `02-notability-name-dropping` | "cited in NYT, BBC...", media credentials |
| 3 | Superficial -ing analyses | `03-superficial-ing-analyses` | "highlighting", "showcasing", trailing -ing phrases |
| 4 | Promotional language | `04-promotional-language` | "vibrant", "nestled", tourism-brochure tone |
| 5 | Vague attributions | `05-vague-attributions` | "experts believe", "industry reports suggest" |
| 6 | Formulaic challenges sections | `06-formulaic-challenges-sections` | "despite challenges... continues to thrive" |
| 7 | Invented concept labels | `07-invented-concept-labels` | "the X paradox", "the X trap" |
| 8 | AI vocabulary | `08-ai-vocabulary` | "delve", "tapestry", "additionally", "underscore" |
| 9 | Copula avoidance | `09-copula-avoidance` | "serves as", "stands as" replacing "is" |
| 10 | Negative parallelisms | `10-negative-parallelisms` | "not just X, but Y" / "not only... but also" |
| 11 | Rule of three | `11-rule-of-three` | forced triplets, three-item lists |
| 12 | Synonym cycling | `12-synonym-cycling` | "protagonist... main character... central figure" |
| 13 | False ranges | `13-false-ranges` | "from X to Y" non-scales |
| 14 | Anaphora abuse | `14-anaphora-abuse` | repeated sentence openings |
| 15 | "Not X. Not Y. Just Z." | `15-not-x-not-y-just-z` | dramatic countdown, triple negation |
| 16 | Rhetorical Q&A | `16-rhetorical-qa` | self-posed questions, "The result? X." |
| 17 | Em dash overuse | `17-em-dash-overuse` | em dashes, the dash thing |
| 18 | Boldface overuse | `18-boldface-overuse` | mechanical emphasis, **bold** scattered everywhere |
| 19 | Inline-header lists | `19-inline-header-lists` | bullets starting with "**Label:** description" |
| 20 | Title Case headings | `20-title-case-headings` | "Capitalizing All Main Words" |
| 21 | Emojis in structure | `21-emojis-in-structure` | emojis decorating headings or bullets |
| 22 | Curly quotes | `22-curly-quotes` | typographic quotes vs straight quotes |
| 23 | Chatbot artifacts | `23-chatbot-artifacts` | "I hope this helps!", "Certainly!", "Of course!" |
| 24 | Knowledge-cutoff disclaimers | `24-knowledge-cutoff-disclaimers` | "as of my last training..." |
| 25 | Sycophantic tone | `25-sycophantic-tone` | "Great question!", "You're absolutely right!" |
| 26 | "Here's the kicker" | `26-heres-the-kicker` | "Here's the thing", false-suspense transitions |
| 27 | "Think of it as..." | `27-think-of-it-as` | "Think of it like", "Imagine it as" |
| 28 | "Imagine a world where..." | `28-imagine-a-world-where` | AI futurism invitations |
| 29 | Disclosure without substance | `29-false-vulnerability` | former name: false vulnerability; disclosure without a point |
| 30 | Filler phrases | `30-filler-phrases` | "in order to", "due to the fact that" |
| 31 | Excessive hedging | `31-excessive-hedging` | "could potentially possibly be argued" |
| 32 | "The truth is simple" | `32-the-truth-is-simple` | "the reality is simpler", asserted obviousness |
| 33 | Generic positive conclusions | `33-generic-positive-conclusions` | "the future looks bright", "exciting times ahead" |
| 34 | Uniform sentence rhythm | `34-uniform-sentence-rhythm` | low burstiness, sentences all the same length, robotic cadence |
| 35 | Aphoristic paragraph closers | `35-aphoristic-closers` | every paragraph ends on a kicker, balanced epigrams |
| 36 | Reflexive formality | `36-reflexive-formality` | no contractions, "do not / cannot / it is", stiff tone |

---

## ai;dr mode

When the user asks to extract the prompt, find the actual point, "ai;dr" the text, or says "what was this AI asked to write", use this mode instead of Rewrite.

Goal: compress AI-generated verbosity back to the instruction that likely produced it.

### Process

1. **Fetch** the text (same input handling as Rewrite mode)
2. **Score** using the algorithmic scorer if available
3. **Identify** the core claim or instruction buried in the text
4. **Extract** a probable prompt: one sentence, under 40 words, that would generate this output
5. **Report** the inflation ratio (original word count / prompt word count)

### Output format

> **Probable prompt:** "Write a blog post about why platform businesses beat product businesses"
>
> **Original:** 2,847 words | **Prompt:** 12 words | **Inflation:** 237x

---

## The 36 patterns catalogue

The versioned [catalogue.md](catalogue.md) contains every numbered pattern,
source, evidence limit, current AI-signal use, editorial action, and
false-positive guard. It is shared with the three individual skills.
