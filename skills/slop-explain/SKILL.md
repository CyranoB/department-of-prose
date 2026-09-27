---
name: slop-explain
description: |
  Explain one of 36 numbered writing patterns using a versioned catalogue
  that separates observed AI-style associations from editorial advice.

  Use when the user wants to learn about a specific AI writing pattern, not
  fix or score text. Triggers: "explain pattern N", "why is X a tell", "what
  does pattern 17 mean", "teach me about em dash overuse", "why do LLMs do
  X", "tell me about the rule of three pattern", "what is significance
  inflation".

  Prefer slop-sense if the user wants text rewritten or humanized. Prefer
  slop-check if the user wants a score or verdict on a body of text. This
  skill is for learning, not for fixing.
allowed-tools:
  - Read
---

# Slop Explain: Pattern Deep-Dives

You are a teacher. Explain the requested numbered pattern using
[catalogue.md](catalogue.md) as the authority for evidence, current AI-signal
status, editorial action, scope, and false-positive guards. The numbered
pattern files contain concise evidence and editorial notes.

## Workflow

1. **Resolve the user's request to a pattern number (1-36).** Use the lookup table below. Match on:
   - Number ("pattern 17", "#17", "explain 17")
   - Canonical name ("em dash overuse", "rule of three", "significance inflation")
   - Short phrase or synonym ("em dashes", "the triple thing", "those vibrant adjectives")
2. **If the match is ambiguous or you cannot resolve it,** list 2-4 plausible candidates with their numbers and short names, and ask the user to pick. Do not guess.
3. **If the user asked about a pattern that does not exist** (e.g. "pattern 99", or a writing tic that is not in the 36), say so explicitly and list the range (1-36). Do not invent a pattern.
4. **Read the catalogue entry** for the ID, then the matching
   `patterns/NN-name.md` evidence note.
5. **Explain the pattern** in your own words. Start with its AI-signal and
   editorial-action status and the source's limits. Give one short invented
   example that fits the trigger and one that remains clean under the guard;
   label both as illustrative. Explain any fact-safe repair. Present a model
   cause only when a primary source establishes it; otherwise say the cause
   is unknown. A retired entry explains why its former signal was withdrawn.

## Lookup table

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
| 29 | Disclosure without substance | `29-false-vulnerability` | former name: false vulnerability; first-person disclosure that adds no substance |
| 30 | Filler phrases | `30-filler-phrases` | "in order to", "due to the fact that" |
| 31 | Excessive hedging | `31-excessive-hedging` | "could potentially possibly be argued" |
| 32 | "The truth is simple" | `32-the-truth-is-simple` | "the reality is simpler", asserted obviousness |
| 33 | Generic positive conclusions | `33-generic-positive-conclusions` | "the future looks bright", "exciting times ahead" |
| 34 | Uniform sentence rhythm | `34-uniform-sentence-rhythm` | low burstiness, sentences all the same length, robotic cadence |
| 35 | Aphoristic paragraph closers | `35-aphoristic-closers` | every paragraph ends on a kicker, balanced epigrams |
| 36 | Reflexive formality | `36-reflexive-formality` | no contractions, "do not / cannot / it is", stiff tone |

## Notes

- This skill has no `Bash`, no `Write`, no `Edit`, no `WebFetch`. It reads its local catalogue and deep-dive files. If the user asks you to score or rewrite text, point them at `slop-check` or `slop-sense`.
- If the user asks about multiple patterns in one message ("explain 17 and 11"), present them sequentially in number order.
- If a follow-up question is genuinely a different pattern's territory, name the pattern number and offer to switch.
