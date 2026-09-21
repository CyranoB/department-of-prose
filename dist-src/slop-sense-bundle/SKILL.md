---
name: slop-sense
description: |
  Detect, score, rewrite, and explain recurring patterns associated with formulaic or AI-like prose (36 catalogued patterns,
  EQBench SLOP methodology). Four modes:
  (1) Rewrite — humanize text, remove AI tells. Triggers: "rewrite this",
  "humanize", "deslop", "remove AI tells", "make it sound human".
  (2) Verdict only — score 0-100 and list patterns, no rewrite. Triggers:
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

A bundled writing editor that identifies recurring prose patterns, scores them, and rewrites or explains them on demand. Scores and findings describe the passage, not who or what wrote it. Based on Wikipedia's "Signs of AI writing" guide (WikiProject AI Cleanup) and the EQBench SLOP detection methodology.

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
python3 scripts/rhythm.py /tmp/slop-input.txt     # structural: burstiness, contractions, closers, anaphora
```

(Save pasted text to `/tmp/slop-input.txt` first. If running from outside the skill directory, use absolute paths.)

`score.sh` wraps `npx slop-detector` and is **optional by design** — if it fails or exits with `SCORER_NOT_AVAILABLE`, skip the numeric score and say so (e.g. `SLOP score: scorer unavailable, qualitative only`). `rhythm.py` is pure Python (no dependencies).

A low SLOP score says only that the lexical scorer found few matches. It says nothing about rhythm, voice, clarity, or authorship. Use `rhythm.py` to find structural patterns worth reviewing, then judge them in the passage's genre and intended voice.

### Interpreting findings

The SLOP score measures the density of catalogued lexical and construction matches: **minimal** (0-19), **light** (20-39), **moderate** (40-59), **strong** (60-79), or **pervasive** (80-100). These bands describe pattern evidence, not authorship probability or overall writing quality.

Short samples can change bands after one or two matches. The catalogue is English-centric, and technical or domain-specific vocabulary can create unavoidable hits. Deliberate repetition, formality, or typography may suit the genre. Base the editorial assessment on each pattern's frequency, context, and effect on the passage, and explain those effects to the user.

---

## Mode 1: Rewrite

You are a writing editor. Identify recurring patterns and rewrite the passage to sound natural and specific.

### Workflow

1. **Try the scorer.** Save the user's text to `/tmp/slop-input.txt`, then run `bash scripts/score.sh /tmp/slop-input.txt`. If it returns a score, use it as evidence. If it fails, proceed without.
2. **Scan** the text against the [36 patterns catalog](#the-36-patterns-catalog) below. Name exactly which ones you found.
3. **Score** — report the algorithmic number if available, plus its pattern-evidence band (minimal / light / moderate / strong / pervasive). Add a qualitative assessment based on the frequency, context, and effect of all findings. Never translate the score into a probability of AI authorship.
4. **Rewrite** the text, removing the identified patterns while preserving meaning. Meaning includes the factual record: read [Fact preservation](#fact-preservation) first.
5. **Audit** — ask yourself "Which repeated patterns still weaken this passage?" Read once more for rhythm (pattern 34) and watch for over-correction: do not fix every negative parallelism (#10) by splitting it into the same "X isn't this. It's that." two-beat. Scan the headings too, not just body prose — they host #10 negative parallelism ("A choice, not a fate") and #20 Title Case, and `rhythm.py` strips headings so it cannot see them. Re-run `python3 scripts/rhythm.py` on your rewrite to confirm the measurements changed where intended. List remaining patterns and their effect, then revise once more.
6. **Fact check the version you are about to present.** Do this last, after the revision in step 5, so it covers the delivered text rather than an earlier draft. Beside the original, ask whether anything was *added* (a source, cause, figure, or stronger claim the original lacked), *omitted* (a name, number, quotation, attribution, hedge, or scope limit), or *changed* in strength, subject, or direction. Check each item on its own; a rewrite can read as cautious overall while one specific hedge has gone missing.
7. **Present** the final version, the fact-check result, and a brief summary of what changed.

### Fact preservation

The rewrite changes how the text sounds, never what it claims. Names, numbers, dates, quotations, sources, hedges, and scope limits survive the edit even where cutting one would read better.

The traps, each tied to the pattern that invites it:

- Removing a vague attribution (#5) tempts you to supply the source it lacked. Report what the input said ("unnamed industry reports") or say it named none. "Name the source" applies when the source is elsewhere in the document, not when you would have to make it up.
- Cutting excessive hedging (#31) means dropping the redundant qualifiers, not the doubt they carried. "May have reduced" is not "reduced".
- Fixing synonym cycling (#12) means repeating a name, not paraphrasing it. A legal name is not its trade name.
- Quoted text is off limits even when full of tells. Report a #10, #17, or #22 hit inside a quotation as the speaker's and fix the reporting clause instead. This outranks #17's zero-em-dash target: a quoted dash stays.
- Scope limits go first in any tightening pass. "In the pilot group", "self-reported", "among the 40 who finished" are load-bearing.

If a pattern can only be removed by adding specifics the input does not contain, leave it. Keep the general phrasing, or mark the gap (`[source?]`, `[date?]`) and raise it in the summary.

### Output format

1. **SLOP score** (if scorer ran) — algorithmic score plus interpretation
2. **Pattern summary** — which patterns you found, their frequency and context, and how they affect the passage
3. **Draft rewrite** — first pass with patterns removed
4. **Pattern audit** — bullets listing repeated constructions or rhythm problems that still weaken the draft
5. **Final rewrite** — revised after the audit, no em dashes of your own
6. **Fact check** — run on the final rewrite above, not the draft. Confirm nothing was added, omitted, or changed in strength; list anything you could not preserve or marked `[source?]`. State it explicitly when clean, never skip the line
7. **Changes summary** — what was fixed (optional, if helpful)

### Adding soul

Removing bad patterns is half the job. Sterile, voiceless writing is still weak. Good writing carries a distinct point of view.

Signs of soulless writing (even if technically clean):
- Every sentence has the same length and structure
- No opinions, just neutral reporting
- No acknowledgment of uncertainty or mixed feelings
- No humor, no edge, no personality

How to fix this:
- **Have opinions.** React to facts, don't just report them.
- **Vary rhythm.** Short sentences. Then longer ones that take their time.
- **Acknowledge complexity.** "This is impressive but also kind of unsettling" beats "This is impressive."
- **Use "I" when it fits.** First person signals a real person thinking.
- **Let some mess in.** Perfect structure feels algorithmic.
- **Be specific about feelings.** Not "this is concerning" but name the actual feeling.

Example:

Before (clean but soulless):
> The experiment produced interesting results. The agents generated 3 million lines of code. Some developers were impressed while others were skeptical.

After (has a pulse):
> I genuinely don't know how to feel about this one. 3 million lines of code, all of it agent-written. Some developers are impressed. Some are sceptical. I can't tell which camp I'm in either.

Note what the rewrite does *not* do. It keeps "some" instead of sharpening it to "half", and it keeps "developers" instead of widening to "the dev community". The voice comes from the narrator taking a position, not from making someone else's facts more definite than they were.

---

## Mode 2: Verdict only

Read-only writing-pattern review. Score and report. **Do not rewrite. Do not suggest specific edits.**

### Workflow

1. **Get the text** using the input handling above. If pasted, save it to `/tmp/slop-check-input.txt`.
2. **Run both scripts**: `bash scripts/score.sh /tmp/slop-check-input.txt` and `python3 scripts/rhythm.py /tmp/slop-check-input.txt`. If either fails, skip it and continue with what you have. A low lexical score does not cancel repeated structural findings.
3. **Scan** the text against the [36 patterns catalog](#the-36-patterns-catalog) below. Name every pattern present. For each, attach one short evidence snippet (a quoted phrase or count) — not a sentence of explanation.
4. **Emit the verdict and stop.** Do not produce a rewrite. The closing line points the user at Rewrite mode or Pattern deep-dive mode.

### Output format

```
SLOP score: 78 / 100 (strong pattern evidence)

Patterns detected (7):
  #4  Promotional language     — "vibrant", "nestled", "boasts"
  #8  AI vocabulary            — "additionally", "underscore", "tapestry" (×3)
  #10 Negative parallelisms    — "not just X, but Y" (×2)
  #11 Rule of three            — 4 instances
  #17 Em dash overuse          — 6 em dashes in 312 words
  #23 Chatbot artifacts        — "I hope this helps!"
  #30 Filler phrases           — "in order to" (×2)

Assessment: strong pattern evidence. Several repeated patterns affect the passage's tone and rhythm.
Next: ask for a rewrite, or "explain pattern N" to learn about a specific pattern.
```

Score bands describe the density of matches from `score.sh`:
- **minimal** — 0-19; few catalogued lexical or construction matches
- **light** — 20-39; some matches recur
- **moderate** — 40-59; several matches recur or cluster
- **strong** — 60-79; frequent or concentrated matches
- **pervasive** — 80-100; matches dominate substantial parts of the passage

The final assessment must account for frequency, context, and effect across the scorer, structural measurements, and qualitative scan. State what the patterns do to the passage. Do not infer authorship.

If the scorer was unavailable, omit the numeric score line and say so: `SLOP score: scorer unavailable, qualitative only`. Keep the rest of the format identical.

---

## Mode 3: Pattern deep-dive

You are a teacher. The user wants to understand one pattern in depth — not fix their text, not score it. Explain the pattern's frequency, context, and effect. A pattern may be common in model output without proving AI authorship.

### Workflow

1. **Resolve the user's request to a pattern number (1-36).** Use the [lookup table](#pattern-lookup-table) below. Match on number ("pattern 17"), canonical name ("em dash overuse"), or short phrase ("the dash thing", "those vibrant adjectives").
2. **If ambiguous,** list 2-4 plausible candidates with numbers and short names, and ask the user to pick. Do not guess.
3. **If the pattern does not exist** (e.g. "pattern 99", or a tic outside the 36), say so explicitly and state the range (1-36). Do not invent a pattern.
4. **Read the deep-dive file**: `patterns/NN-name.md` from this skill's directory, where `NN` is zero-padded and `name` is the kebab-case slug from the table.
5. **Present the deep-dive.** Render the markdown directly. Do not summarize, paraphrase, or add commentary unless the user asked a follow-up.

If the user asks about multiple patterns in one message ("explain 17 and 11"), present them sequentially in number order. If a follow-up is genuinely a different pattern's territory, name the pattern number and offer to switch.

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
| 29 | False vulnerability | `29-false-vulnerability` | performative honesty, safe vulnerability |
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
>
> **Detected patterns:** negative parallelism, em dash addiction, grandiose stakes inflation, invented concept labels

---

## The 36 patterns catalog

Used by Modes 1 and 2 for scanning. Pattern deep-dives (Mode 3) live in `patterns/NN-name.md`.

Some After-examples below draw on facts from elsewhere in the source document (a date, a named outlet, a place). They are shorthand for "replace the puffery with the specifics the source already gives you", never licence to supply specifics the text does not contain. See [Fact preservation](#fact-preservation).

### Content patterns (1-7)

**1. Significance inflation**
Puffing up importance with sweeping claims about legacy, broader trends, pivotal moments.
Watch for: "stands as", "testament to", "pivotal/crucial/vital role", "evolving landscape", "setting the stage", "indelible mark", "deeply rooted", "reflects broader"
> Before: "marking a pivotal moment in the evolution of regional statistics"
> After: "was established in 1989 to collect regional statistics"

**2. Notability name-dropping**
Listing media outlets or credentials without context.
> Before: "cited in NYT, BBC, FT, and The Hindu"
> After: "In a 2024 NYT interview, she argued..."

**3. Superficial -ing analyses**
Tacking "-ing" phrases onto sentences for fake depth.
Watch for: "highlighting...", "showcasing...", "reflecting...", "underscoring...", "fostering..."
> Before: "symbolizing the community's deep connection to the land"
> After: Remove entirely, or replace with sourced claim.

**4. Promotional language**
Neutral tone lost to tourism-brochure writing.
Watch for: "vibrant", "nestled", "breathtaking", "renowned", "groundbreaking", "stunning", "boasts", "profound", "exemplifies", "commitment to"
> Before: "Nestled within the breathtaking region..."
> After: "is a town in the Gonder region"

**5. Vague attributions**
Opinions attributed to unnamed authorities.
Watch for: "Experts believe", "Industry reports suggest", "Some critics argue"
> After: Name the source, date, and specific claim.

**6. Formulaic challenges sections**
"Despite challenges... continues to thrive" structure.
> After: State specific facts about actual challenges.

**7. Invented concept labels**
Fabricated compound terms that sound analytical but are ungrounded. Appending abstract nouns (paradox, trap, creep) to domain words.
Watch for: "the supervision paradox", "the acceleration trap", "the alignment creep", "the delegation paradox"
> Before: "This creates what I call the 'delegation paradox'"
> After: State the tension directly without branding it.

### Language patterns (8-16)

**8. AI vocabulary**
Words that appear far more often in post-2023 LLM text.
High-frequency tells: "Additionally", "delve", "tapestry", "landscape" (abstract), "pivotal", "testament", "underscore", "showcase", "foster", "garner", "interplay", "intricate", "enhance", "vibrant", "crucial", "enduring", "align with", "bolstered", "meticulous", "valuable", "key" (adjective), "highlighting" (verb)
> Before: "Additionally, an enduring testament to... in the culinary landscape, showcasing..."
> After: "also includes... remain common"

**9. Copula avoidance**
Replacing "is/are/has" with fancier constructions.
Watch for: "serves as", "stands as", "features", "boasts", "represents"
> Before: "Gallery 825 serves as the exhibition space"
> After: "Gallery 825 is the exhibition space"

**10. Negative parallelisms**
Common forms: "Not just X, but Y" / "Not only... but also..." / "It's not X, it's Y". Splitting it across two sentences ("It isn't X. It's Y.") is the same construction in disguise, and repeating that two-beat is its own tell, so vary the repair. See also #15 for the triple-negation variant.
> Before: "It's not just about the music, it's about the community."
> After: "The community matters as much as the music."

**11. Rule of three**
Forcing ideas into groups of three for rhetorical effect.
> Before: "innovation, inspiration, and industry insights"
> After: Use the natural number of items.

**12. Synonym cycling**
Rotating synonyms to avoid repeating words ("protagonist... main character... central figure... hero").
> After: Repeat the clearest term. Repetition is fine.

**13. False ranges**
"From X to Y" where X and Y aren't on a meaningful scale.
> Before: "from the Big Bang to dark matter"
> After: List topics directly.

**14. Anaphora abuse**
Repeating identical sentence openings in quick succession for false emphasis. Even three consecutive sentences opening with the same word ("The..., The..., The...") trips automated trope detectors.
> Before: "They assume users will pay. They assume developers will build. They assume the market will grow."
> After: Vary the structure. Combine related points.

**15. "Not X. Not Y. Just Z."**
Dramatic countdown negating multiple items before the actual point. Distinct from the two-part negative parallelism in #10.
> Before: "Not a bug. Not a feature. A fundamental design flaw."
> After: "It's a design flaw."

**16. Rhetorical Q&A**
Self-posed questions answered immediately. Asking questions nobody asked for dramatic effect.
> Before: "The result? Devastating."
> After: "The result was devastating."

### Style patterns (17-22)

**17. Em dash overuse (the hardest pattern to fix)**
LLMs use em dashes (— and --) far more than human writers do. This is one of the strongest AI tells and also the one you are most likely to leave in your own rewrites, because dashes feel natural to you. They are not natural at the rate you use them. A human writer might use one em dash per page. LLMs use multiple per paragraph.
Every time you are about to write an em dash, stop and use a comma, a period, or parentheses instead. If the sentence needs restructuring to work without the dash, restructure it.
> Before: "The tools are useful — even essential — for modern teams."
> After: "The tools are useful, even essential, for modern teams."
> Before: "It works — most of the time."
> After: "It works most of the time."
Zero em dashes *of your own* in the final rewrite is the target. If you find yourself reaching for one, that is the habit talking. A dash inside a quotation you are preserving belongs to the speaker: leave it, and do not count it against the rewrite.

**18. Boldface overuse**
Mechanical emphasis on terms.
> After: Remove boldface unless genuinely needed.

**19. Inline-header lists**
Bullet points starting with "**Label:** description"
> After: Convert to prose.

**20. Title Case headings**
Capitalizing All Main Words In Headings.
> After: Sentence case.

**21. Emojis in structure**
Decorating headings or bullets with emojis.
> After: Remove them.

**22. Curly quotes**
ChatGPT uses curly quotes instead of straight quotes.
> After: Use straight quotes.

### Communication patterns (23-29)

**23. Chatbot artifacts**
"I hope this helps!", "Let me know if...", "Certainly!", "Of course!", "Great question!"
> After: Remove entirely.

**24. Knowledge-cutoff disclaimers**
"While specific details are limited...", "as of my last training..."
> After: Find the actual information, or remove the hedge.

**25. Sycophantic tone**
"Great question! You're absolutely right!"
> After: Respond to the substance directly.

**26. "Here's the kicker"**
False suspense transitions promising revelations before unremarkable observations.
Watch for: "Here's the thing", "Here's where it gets interesting", "Here's what most people miss"
> Before: "Here's the kicker: it was never about the technology."
> After: Just make the point.

**27. "Think of it as..."**
Patronizing analogies assuming readers need metaphors. Often produces less-clear explanations than just describing the actual thing.
Watch for: "Think of it like", "Imagine it as", "It's basically"
> Before: "Think of it like a highway system for data."
> After: Explain the actual thing.

**28. "Imagine a world where..."**
AI futurism invitation listing wonderful outcomes if readers agree with the premise.
> Before: "Imagine a world where every tool you use has quiet intelligence behind it."
> After: State the specific capability being proposed.

**29. False vulnerability**
Simulated self-awareness or honesty that reads as performative. Real vulnerability is specific and uncomfortable; AI vulnerability is polished and safe.
> Before: "And yes, I'm openly in love with the platform model."
> After: State the actual opinion with real stakes.

### Filler and hedging (30-33)

**30. Filler phrases**
"In order to" -> "To". "Due to the fact that" -> "Because". "At this point in time" -> "Now". "It is important to note that" -> delete.

**31. Excessive hedging**
"could potentially possibly be argued that it might"
> After: "may"

**32. "The truth is simple"**
Asserting obviousness instead of proving arguments. Declaring simplicity rather than demonstrating it.
Watch for: "The reality is simpler", "The truth is", "The answer is surprisingly straightforward"
> Before: "The reality is simpler and less flattering."
> After: Present the reality and let the reader judge.

**33. Generic positive conclusions**
"The future looks bright. Exciting times lie ahead."
> After: State specific plans or facts.

### Rhythm and Voice (34-36)

The lexical scorer does not measure these dimensions. `rhythm.py` reports all three as editorial heuristics; interpret them in context.

**34. Uniform sentence rhythm (low burstiness)**
Sentences barely vary in length or shape, producing a flat, even cadence. Variation can create pace and emphasis, while a long run of similarly shaped sentences can feel monotonous. Genre matters: procedural prose may benefit from consistency.
> Before: "The invention happened in Toronto, and the company that captured what it was worth happened somewhere else, and that gap is the whole story."
> After: "The invention happened in Toronto. The company that captured what it was worth happened somewhere else. That gap is what this whole piece is about."
Put short sentences next to long ones. If three in a row share a shape, break one.

**35. Aphoristic paragraph closers**
Ending nearly every paragraph on a polished, balanced kicker. One or two read as sharp; a dozen read as a machine that learned the move. The tell is the relentlessness, not any single line.
> After: Let most paragraphs end on an ordinary sentence. Earn the occasional kicker.

**36. Reflexive formality**
Never contracting — "do not", "cannot", "it is" everywhere, even in casual or first-person writing. This can make an informal passage sound stiff, while the same choice may suit legal, academic, or ceremonial prose.
> Before: "It is not capacity. You cannot commercialize what you do not own."
> After: "It isn't capacity. You can't commercialize what you don't own."
Mix registers; the point is variation, not contracting everything.
