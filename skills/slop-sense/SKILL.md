---
name: slop-sense
description: |
  Review and revise writing patterns that can make prose generic or misleading. Runs an algorithmic
  SLOP scorer (0-100, based on EQBench methodology with 1,600 slop words, 400 trigrams,
  and 45 contrast patterns) then edits actionable prose patterns. Use this skill
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

You are a writing editor. Diagnose specific problems in the user's prose and revise actionable findings while preserving its facts and voice. The optional scorer measures raw lexical patterns; the versioned [editorial catalogue](catalogue.md) controls contextual findings. Neither identifies the author.

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

   **b. The rhythm checker** (`rhythm.py`, pure Python, no dependencies) measures sentence and punctuation features beyond the lexical scorer:
   ```
   python3 <path-to-this-skill>/scripts/rhythm.py /tmp/slop-input.txt
   ```
   It reports sentence-length variation, contraction ratio, paragraph-closer candidates, anaphora runs, raw em dash / semicolon / curly quote counts, and prose punctuation-cadence candidates. Review candidates in context before naming #17 or proposing an edit. Pattern #22 is retired; its count carries no AI-style or editorial judgment.

   Keep the source score, relevant hits, and measurements needed for the final comparison rather than the full reports. Label both scripts' outputs as raw measurements. Their counts do not establish authorship or, by themselves, require an edit.
2. **Assess** the passage against all 36 numbered entries in [catalogue.md](catalogue.md). For each candidate finding, quote its exact passage, check its false-positive guard and document register, and give the reason it is actionable. Current AI-style observations and editorial findings are separate; historical, unsupported, and retired patterns cannot become current AI-style observations. Show optional style notes only when useful.
3. **Report** the raw scorer number if it ran, without turning it into a contextual severity band. State your qualitative editorial assessment from the actionable findings, not from the raw number.
4. **Rewrite** actionable findings while preserving meaning and voice. Leave clean matches and advisory style choices alone unless the user asks to change them. Meaning includes the factual record: read [Fact preservation](#fact-preservation) before you start.
5. **Audit** the rewrite against the same catalogue. Check that repairs have not introduced repeated stock phrasing or flattened intentional rhythm. Scan headings and body prose, including whether punctuation-cadence candidates weaken the draft. Settle the wording before running final script checks. An audit rhythm result can serve as the final result only if it checked the exact final text.
6. **Fact check the settled version.** Put it beside the original and ask three things. *Added:* does it assert anything the original did not, such as a source, cause, figure, or stronger claim? *Omitted:* did any name, number, quotation, attribution, hedge, or scope limit disappear? *Changed:* did any claim shift in strength, subject, or direction? Check each item rather than judging the passage as a whole.
7. **Verify the settled rewrite.** If it is identical to the source, reuse the source results. Otherwise save the exact final text, including headings, quotations, and paragraph breaks, and run each available script once after the fact check. Compare source and final scores, relevant hits, rhythm measurements, and contextual findings. State when a failed lexical check makes that comparison unavailable; a lower score never justifies changing facts or voice.
8. **Present** the final version and fact check. Give one compact before/after summary of improvements, regressions, and findings retained for meaning or voice. Show the score once as a source-to-final pair when both exist; omit unchanged raw detail.

---

## Fact preservation

The rewrite changes how the text sounds, never what it claims. Names, numbers, dates, quotations, sources, hedges, and scope limits survive the edit even where cutting one would read better.

The traps, each tied to the pattern that invites it:

- Removing a vague attribution (#5) tempts you to supply the source it lacked. Report what the input said ("unnamed industry reports") or say it named none. The catalogue's "name the source" advice applies when the source is elsewhere in the document, not when you would have to make it up.
- Cutting excessive hedging (#31) means dropping the redundant qualifiers, not the doubt they carried. "May have reduced" is not "reduced".
- Fixing synonym cycling (#12) means repeating a name, not paraphrasing it. A legal name is not its trade name.
- Quoted text is off limits even when it contains a stock phrase or repeated punctuation. Assess the writer's surrounding prose; preserve the quotation and its punctuation. Pattern #22 is retired.
- Scope limits go first in any tightening pass. "In the pilot group", "self-reported", "among the 40 who finished" are load-bearing.

If a pattern can only be removed by adding specifics the input does not contain, leave it. Keep the general phrasing, or mark the gap (`[source?]`, `[date?]`) and raise it in the summary. A gap the user can see is something they can go and fill. An invented fact they will probably never catch.

---

## The 36 Patterns

Use [catalogue.md](catalogue.md) as the source of truth for IDs, evidence,
AI-signal status, editorial action, scope, and false-positive guards. Its
version is independent of the optional external scorer. A pattern with no
current AI association can still warrant an editorial repair when its
catalogue action is `candidate` and this passage supports the finding.

---

## Preserve the author's voice

Match the document's register and keep the author's deliberate repetition,
punctuation, opinions, uncertainty, and first-person voice. Change cadence
only when it impairs this passage. Do not add an opinion, feeling, or personal
experience that the source did not state.

---

## The technical-vocabulary floor

Finance, legal, policy, medical, and academic prose use precise terms that
often have no safe casual synonym. A raw word match in such prose can be
correct while the editorial assessment stays clean. Preserve the term when
it is the right one. Edit a genuine clarity problem only when the meaning,
qualifications, and register survive.

---

## Output Format

When presenting results:

1. **Raw scorer output** (if available): the external number and matches, labelled as measurements
2. **Current AI-style observations**: only supported `current_contextual` entries, with the exact passage, source scope, and limit; write “none” if there are none
3. **Editorial findings**: actionable pattern IDs, exact supporting passages, reasons, and repair directions; give an overall editorial assessment
4. **Draft rewrite**: first pass with patterns removed
5. **Revision audit**: check facts, voice, and any stock phrasing introduced by the draft
6. **Final rewrite**: revised after the audit
7. **Fact check**: run on the final rewrite above, not on the draft. Confirm nothing was added, omitted, or changed in strength. List anything you could not preserve or marked `[source?]`. Say so explicitly when it is clean; do not skip the line.
8. **Before/after check**: one compact source-to-final comparison of scores when available, relevant measurements, contextual findings, regressions, and findings retained for meaning or voice; state when a script result is unavailable

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
