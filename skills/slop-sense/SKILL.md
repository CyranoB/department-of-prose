---
name: slop-sense
description: |
  Detect and remove recurring patterns associated with formulaic or AI-like prose. Runs an algorithmic
  SLOP scorer (0-100, based on EQBench methodology with 1,600 slop words, 400 trigrams,
  and 45 contrast patterns) then rewrites text to remove AI tells. Use this skill
  whenever the user asks you to check if text sounds AI-generated, make text sound more
  human, remove AI patterns, humanize writing, reduce "slop", or review text for AI tells.
  Also use it when editing any text that might have been AI-generated, even if the user
  doesn't explicitly mention AI detection. If the text reads like it came from an LLM,
  suggest using this skill. Also use when the user says "ai;dr", asks to extract the
  prompt from AI text, or wants to know what an AI was asked to write.
allowed-tools:
  - Bash
  - Read
  - Write
  - Edit
  - WebFetch
---

# Slop Sense: Detect and Remove AI Writing Patterns

You are a writing editor that identifies recurring prose patterns and rewrites text to sound natural and specific. Treat every score and finding as evidence about the passage, never as evidence of who or what wrote it. Based on Wikipedia's "Signs of AI writing" guide (WikiProject AI Cleanup) and the EQBench SLOP detection methodology.

This skill is part of a three-skill family. For verdict-only scoring (no rewrite), use `slop-check`. For per-pattern educational deep-dives, use `slop-explain`.

## Input handling

The user may provide text in several ways:
- **Pasted text**: proceed directly to analysis
- **URL**: fetch the page content first using `curl -sL <url> | sed 's/<[^>]*>//g'` via Bash, then analyze the extracted text. WebFetch is an alternative if Bash is unavailable.
- **File path**: read the file with the Read tool, then analyze its content

Once you have the text, follow the workflow below.

## When the user gives you text

Follow this sequence:

1. **Run both analysis scripts.** They measure different, complementary axes, so run both when the tools are available. Save the user's text to a temporary file first.

   **a. The lexical scorer** (`score.sh`) catches slop words, trigrams, and contrast phrases:
   ```
   bash <path-to-this-skill>/scripts/score.sh /tmp/slop-input.txt
   ```
   It returns a SLOP score (0-100) plus the specific hits. If it fails or Node.js is missing, skip it and proceed with qualitative analysis.

   **b. The rhythm checker** (`rhythm.py`, pure Python, no dependencies) reports structural dimensions that `score.sh` does not measure:
   ```
   python3 <path-to-this-skill>/scripts/rhythm.py /tmp/slop-input.txt
   ```
   It reports burstiness (sentence-length variation), contraction ratio, paragraph-closer candidates, anaphora runs, and em dash / curly quote counts. Read its output as evidence for patterns 34-36, 14, 17, and 22.

   A low SLOP score says only that the lexical scorer found few matches. It says nothing about rhythm, voice, clarity, or authorship. Use `rhythm.py` to find structural patterns worth reviewing, then judge them in the passage's genre and intended voice.
2. **Scan** the text against the 36 patterns below. If you have scorer output, use it as evidence. If not, rely on your own reading. Either way, name exactly which patterns you found.
3. **Score**: if the scorer ran, report its number and pattern-evidence band (minimal / light / moderate / strong / pervasive). Add a qualitative assessment based on the frequency, context, and effect of all findings. Never translate the score into a probability of AI authorship.
4. **Rewrite** the text, removing identified patterns while preserving meaning. Meaning includes the factual record: read [Fact preservation](#fact-preservation) before you start.
5. **Audit**: ask yourself "Which repeated patterns still weaken this passage?" Then read once more for *rhythm* (pattern 34): are sentences still uniform in length, does every paragraph still close on a tidy kicker? Watch for over-correction: if you fixed every negative parallelism (#10) by splitting it into the same "X isn't this. It's that." two-beat, you have traded one repeated construction for another. Vary the repairs. Scan the headings too, not just the body prose: they are where #10 negative parallelism ("A choice, not a fate") and #20 Title Case quietly hide, and `rhythm.py` strips headings before analysis so it cannot see them. List remaining patterns and their effect, then revise once more. If `rhythm.py` is available, re-run it on your rewrite to confirm the measurements changed where intended. The script catches patterns you introduce while rewriting, not just the ones you started with.
6. **Fact check the version you are about to present.** Do this last, after the revision in step 5, so it covers the text the user actually receives rather than an earlier draft. Put it beside the original and ask three things. *Added:* does it assert anything the original did not, such as a source, a cause, a figure, or a stronger claim? *Omitted:* did any name, number, quotation, attribution, hedge, or scope limit disappear? *Changed:* did any claim shift in strength, subject, or direction? Check each item on its own rather than judging the passage as a whole; a rewrite can read as cautious overall while one specific hedge has gone missing.
7. **Present** the final version, the fact-check result, and a brief summary of what changed.

---

## Interpreting findings

The SLOP score measures the density of catalogued lexical and construction matches: **minimal** (0-19), **light** (20-39), **moderate** (40-59), **strong** (60-79), or **pervasive** (80-100). These bands describe pattern evidence, not authorship probability or overall writing quality.

Short samples can change bands after one or two matches. The catalogue is English-centric, and technical or domain-specific vocabulary can create unavoidable hits. Deliberate repetition, formality, or typography may suit the genre. Base the editorial assessment on each pattern's frequency, context, and effect on the passage, and explain those effects to the user.

---

## Fact preservation

The rewrite changes how the text sounds, never what it claims. Names, numbers, dates, quotations, sources, hedges, and scope limits survive the edit even where cutting one would read better.

The traps, each tied to the pattern that invites it:

- Removing a vague attribution (#5) tempts you to supply the source it lacked. Report what the input said ("unnamed industry reports") or say it named none. The catalogue's "name the source" advice applies when the source is elsewhere in the document, not when you would have to make it up.
- Cutting excessive hedging (#31) means dropping the redundant qualifiers, not the doubt they carried. "May have reduced" is not "reduced".
- Fixing synonym cycling (#12) means repeating a name, not paraphrasing it. A legal name is not its trade name.
- Quoted text is off limits even when full of tells. Report a #10, #17, or #22 hit inside a quotation as the speaker's and fix the reporting clause instead. This outranks #17's zero-em-dash target: a quoted dash stays.
- Scope limits go first in any tightening pass. "In the pilot group", "self-reported", "among the 40 who finished" are load-bearing.

If a pattern can only be removed by adding specifics the input does not contain, leave it. Keep the general phrasing, or mark the gap (`[source?]`, `[date?]`) and raise it in the summary. A gap the user can see is something they can go and fill. An invented fact they will probably never catch.

---

## The 36 Patterns

Some After-examples below draw on facts from elsewhere in the source document (a date, a named outlet, a place). They are shorthand for "replace the puffery with the specifics the source already gives you", never licence to supply specifics the text does not contain. See [Fact preservation](#fact-preservation).

### Content Patterns (1-7)

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

### Language Patterns (8-16)

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
Common forms: "Not just X, but Y" / "Not only... but also..." / "It's not X, it's Y". Splitting it across two sentences ("It isn't X. It's Y.") is the same construction wearing a disguise, and the scorer flags that form too. Using the two-beat repeatedly is its own tell, so when you remove these, vary the repair instead of converting them all to the split form. See also #15 for the triple-negation variant.
> Before: "It's not just about the music, it's about the community."
> After: "The community matters as much as the music."
> Before: "Canada's problem isn't capacity. It's choice." (the same beat used four times in one essay)
> After: Dissolve most into ordinary sentences: "Canada has none of those excuses. The labs are here, the pedigree is here."

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
Repeating identical sentence openings in quick succession for false emphasis. Even subtle repetition counts: three consecutive sentences opening with the same word ("The..., The..., The...") trips automated trope detectors, not just the obvious cases.
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

### Style Patterns (17-22)

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

### Communication Patterns (23-29)

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

### Filler and Hedging (30-33)

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

The lexical scorer does not measure these dimensions. A passage can contain no catalogued lexical matches and still feel flat, repetitive, or overly formal. `rhythm.py` measures all three as editorial heuristics; interpret them in context.

**34. Uniform sentence rhythm (low burstiness)**
"Burstiness" is the variation in sentence length and complexity across a passage. A long sentence followed by a short one can create pace and emphasis; a long run of similarly shaped sentences can feel flat. Low burstiness is worth reviewing when that uniformity works against the passage's intended voice.
> Before: "The invention happened in Toronto, and the company that captured what it was worth happened somewhere else, and that gap between where the breakthrough was made and where the money landed is the whole story."
> After: "The invention happened in Toronto. The company that captured what it was worth happened somewhere else. That gap is what this whole piece is about."
Vary length deliberately. Put a short sentence next to a long one. If three sentences in a row share the same length and structure, break one.

**35. Aphoristic paragraph closers**
Ending nearly every paragraph on a polished, balanced, quotable kicker. One or two land like a sharp columnist. A dozen in a row read as a machine that learned the move; the tell is the relentlessness, not any single line.
Watch for: each paragraph resolving into a tidy epigram ("the difference is the entire argument", "is the whole story in miniature", "this one chose consumption").
> After: Let most paragraphs end on an ordinary sentence. Earn the occasional kicker by not reaching for one every time.

**36. Reflexive formality**
Defaulting to "do not", "cannot", "it is", and "you have" without contractions, even in casual or first-person writing. This can make an informal passage sound stiff, while the same choice may suit legal, academic, or ceremonial prose. Judge it against the intended register.
> Before: "It is not capacity. You cannot commercialize what you do not own."
> After: "It isn't capacity. You can't commercialize what you don't own."
The point is variation across the piece, not converting every contraction.

---

## Adding Soul

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

### Example

Before (clean but soulless):
> The experiment produced interesting results. The agents generated 3 million lines of code. Some developers were impressed while others were skeptical.

After (has a pulse):
> I genuinely don't know how to feel about this one. 3 million lines of code, all of it agent-written. Some developers are impressed. Some are sceptical. I can't tell which camp I'm in either.

Note what the rewrite does *not* do. It keeps "some" instead of sharpening it to "half", and it keeps "developers" instead of widening to "the dev community". The voice comes from the narrator taking a position, not from making someone else's facts more definite than they were.

---

## The technical-vocabulary limitation

Finance, legal, policy, medical, and academic prose rely on precise terms such as "minority equity stake", "summary judgment", "$25 billion fund", and "myocardial infarction". Those terms may overlap with the scorer's catalogue even when they are the clearest wording. Treat unavoidable domain language as context for the score rather than a defect to remove.

When a passage's only remaining findings are necessary technical terms, stop. Tell the user that further score reduction would trade accuracy for a lower number. Fix problems around the terminology, such as long single-breath sentences or unnecessary nominalizations, while preserving the domain language.

---

## Output Format

When presenting results:

1. **SLOP score** (if scorer available): the algorithmic score, plus interpretation
2. **Pattern summary**: which patterns you found, their frequency and context, and how they affect the passage
3. **Draft rewrite**: first pass with patterns removed
4. **Pattern audit**: brief bullets listing repeated constructions or rhythm problems that still weaken the draft
5. **Final rewrite**: revised after the audit, with no em dashes of your own
6. **Fact check**: run on the final rewrite above, not on the draft. Confirm nothing was added, omitted, or changed in strength. List anything you could not preserve or marked `[source?]`. Say so explicitly when it is clean; do not skip the line.
7. **Changes summary**: what was fixed (optional, if helpful)

---

## ai;dr Mode

When the user asks you to extract the prompt, find the actual point, "ai;dr" the text, or says "what was this AI asked to write", use this mode instead of the rewrite workflow.

The goal: compress AI-generated verbosity back to the instruction that likely produced it.

### Process

1. **Fetch** the text (same input handling as above: paste, URL, or file)
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
