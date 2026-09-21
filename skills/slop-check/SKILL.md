---
name: slop-check
description: |
  Score text for recurring patterns associated with formulaic or AI-like prose without rewriting it. Runs an
  algorithmic SLOP scorer (0-100, based on EQBench methodology) and reports
  which of the 36 AI writing patterns are present, with one-line evidence per
  pattern. Verdict only — no rewrite, no audit, no humanization.

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

You are a read-only writing-pattern reviewer. You score text against the 36 catalogued patterns and report what you find. Treat the score as evidence about the passage, never as evidence of who or what wrote it. You do not rewrite. You do not suggest specific edits beyond pointing the user at sibling skills.

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
   `score.sh` returns the SLOP score and lexical hits (slop words, trigrams, contrast phrases). `rhythm.py` reports dimensions `score.sh` does not measure: burstiness, contraction ratio, paragraph closers, anaphora, and em dashes. Treat both as editorial heuristics. If either fails or is unavailable, skip it and proceed with what you have, and state that in the output. A low lexical score does not cancel repeated structural findings.
3. **Scan** the text against the 36 patterns in the reference table below. Name every pattern present. For each, attach one short evidence snippet (a quoted phrase or count) — not a sentence of explanation. Scan headings as well as body prose: #10 (negative parallelism, e.g. "A choice, not a fate") and #20 (Title Case) commonly hide there, and `rhythm.py` strips headings so it cannot see them.
4. **Emit the verdict and stop.** Do not produce a rewrite. Do not offer line-by-line edits. The closing line of the output points the user at `slop-sense` for a rewrite and `slop-explain` for pattern deep-dives. That is the only forward motion this skill provides.

## Output format

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
Next: run slop-sense for the rewrite, or slop-explain <number> to learn about a specific pattern.
```

Score bands describe the density of matches from `score.sh`:
- **minimal** — 0-19; few catalogued lexical or construction matches
- **light** — 20-39; some matches recur
- **moderate** — 40-59; several matches recur or cluster
- **strong** — 60-79; frequent or concentrated matches
- **pervasive** — 80-100; matches dominate substantial parts of the passage

The final assessment must account for the frequency, context, and effect of all findings, including the qualitative scan and `rhythm.py` output. State what the patterns do to the passage, such as making emphasis repetitive or the cadence uniform. Do not translate the score or assessment into a probability of AI authorship.

Apply these limits when interpreting results:
- Short samples can move between bands after one or two matches.
- The catalogue is English-centric; non-English results are incomplete.
- Technical, legal, medical, and academic vocabulary can create unavoidable lexical matches.
- Deliberate repetition, formality, or typographic choices may fit the genre.
- A high score does not prove AI authorship or poor writing. A low score does not prove human authorship or good writing.

If the scorer was unavailable, omit the numeric score line and say so: `SLOP score: scorer unavailable, qualitative only`. Keep the rest of the format identical.

## The 36 patterns (reference table)

Compact reference. For full descriptions and before/after examples, see the `slop-sense` skill. For per-pattern deep-dives, see the `slop-explain` skill.

### Content patterns
1. **Significance inflation** — "stands as", "testament to", "pivotal", "indelible mark", "evolving landscape"
2. **Notability name-dropping** — listed credentials or media outlets with no context
3. **Superficial -ing analyses** — trailing "highlighting...", "showcasing...", "reflecting...", "underscoring..."
4. **Promotional language** — "vibrant", "nestled", "breathtaking", "renowned", "stunning", "boasts"
5. **Vague attributions** — "Experts believe", "Industry reports suggest", "Some critics argue"
6. **Formulaic challenges sections** — "Despite challenges... continues to thrive"
7. **Invented concept labels** — "the supervision paradox", "the acceleration trap", "the delegation paradox"

### Language patterns
8. **AI vocabulary** — "Additionally", "delve", "tapestry", "landscape", "testament", "underscore", "showcase", "foster", "intricate", "vibrant", "crucial"
9. **Copula avoidance** — "serves as", "stands as", "features", "represents" replacing "is/are"
10. **Negative parallelisms** — "Not just X, but Y" / "Not only... but also"
11. **Rule of three** — forced triplets, "innovation, inspiration, and industry insights"
12. **Synonym cycling** — "protagonist... main character... central figure... hero"
13. **False ranges** — "From X to Y" where X and Y aren't on a meaningful scale
14. **Anaphora abuse** — identical sentence openings in succession ("They assume... They assume... They assume...")
15. **"Not X. Not Y. Just Z."** — dramatic countdown negating items before the actual point
16. **Rhetorical Q&A** — "The result? Devastating." / "What does this mean? Everything."

### Style patterns
17. **Em dash overuse** — em dashes (— or --) at LLM-typical density (multiple per paragraph)
18. **Boldface overuse** — mechanical emphasis on terms
19. **Inline-header lists** — bullets starting with "**Label:** description"
20. **Title Case headings** — Capitalizing All Main Words
21. **Emojis in structure** — emojis decorating headings or bullets
22. **Curly quotes** — typographic quotes instead of straight quotes

### Communication patterns
23. **Chatbot artifacts** — "I hope this helps!", "Let me know if...", "Certainly!", "Great question!"
24. **Knowledge-cutoff disclaimers** — "While specific details are limited...", "as of my last training..."
25. **Sycophantic tone** — "Great question! You're absolutely right!"
26. **"Here's the kicker"** — "Here's the thing", "Here's where it gets interesting", "Here's what most people miss"
27. **"Think of it as..."** — "Think of it like", "Imagine it as", "It's basically"
28. **"Imagine a world where..."** — futurism invitations listing wonderful outcomes
29. **False vulnerability** — "And yes, I'm openly in love with..." style performative honesty

### Filler and hedging
30. **Filler phrases** — "in order to", "due to the fact that", "at this point in time", "it is important to note"
31. **Excessive hedging** — "could potentially possibly be argued that it might"
32. **"The truth is simple"** — "The reality is simpler", "The truth is", "The answer is surprisingly straightforward"
33. **Generic positive conclusions** — "The future looks bright", "Exciting times lie ahead"

### Rhythm and voice patterns
These are invisible to `score.sh` and surfaced by `rhythm.py`. Interpret them in the passage's genre and intended voice; they are editorial observations rather than authorship evidence.
34. **Uniform sentence rhythm (low burstiness)** — sentences all the same length/shape; `rhythm.py` CV below ~0.40
35. **Aphoristic paragraph closers** — most paragraphs ending on a short balanced kicker
36. **Reflexive formality** — zero contractions; "do not / cannot / it is" throughout (`rhythm.py` contraction ratio near 0)
