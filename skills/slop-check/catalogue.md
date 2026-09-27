# Slop Sense editorial pattern catalogue

Catalogue version: **1.0.0**. Reviewed: **2026-09-27**.

The optional scorer's score and hits are raw measurements. This catalogue
governs contextual editorial findings. `current_contextual` permits a
scoped AI-style observation, `historical_only` describes a past association,
and `none` permits no AI-style claim. None proves authorship. An editorial
`candidate` becomes actionable only when the quoted passage shows the
problem and its guard has been checked; `advisory` is an optional style
note, and `none` creates no finding. Preserve facts, qualifications,
quotations, and authorial voice when repairing a finding. One span creates
one primary finding even when it matches several pattern IDs.

## 01 Significance inflation

- **ID:** 01. **Lifecycle:** current. **AI signal:** current_contextual. **Editorial action:** candidate.
- **Trigger and false-positive guard:** Unsupported claims of historic importance or broad impact; preserve importance supported by cited facts.
- **Source and evidence type:** [WikiProject AI Cleanup, “Undue emphasis on significance, legacy, and broader trends”](https://en.wikipedia.org/w/index.php?title=Wikipedia:Signs_of_AI_writing&oldid=1376815715#Undue_emphasis_on_significance,_legacy,_and_broader_trends) — field observation.
- **Evidence type:** observation. **AI-association support:** limited.
- **Evidence strength and scope:** Direct match to the editorial pattern, with concrete Wikipedia examples. It supports checking whether the asserted significance is earned; it does not establish that a given writer used AI or that the training incentives asserted in the [former unversioned entry](https://github.com/CyranoB/department-of-prose/blob/f09a61b2369e5e01efff2d99f54efa2dc2453601/skills/slop-explain/patterns/01-significance-inflation.md) caused it. **Reviewed:** 2026-09-27.

## 02 Notability name-dropping

- **ID:** 02. **Lifecycle:** current. **AI signal:** current_contextual. **Editorial action:** candidate.
- **Trigger and false-positive guard:** Credentials or outlet lists that substitute for a relevant claim, especially in encyclopedic prose; keep coverage that explains why it matters.
- **Source and evidence type:** [WikiProject AI Cleanup, “Canned emphasis on notability, attribution, and media coverage”](https://en.wikipedia.org/w/index.php?title=Wikipedia:Signs_of_AI_writing&oldid=1376815715#Canned_emphasis_on_notability,_attribution,_and_media_coverage) — field observation.
- **Evidence type:** observation. **AI-association support:** limited.
- **Evidence strength and scope:** Direct in Wikipedia biographies and drafts, where notability is a policy concept. The field guide distinguishes this narrow source-focused phrasing from ordinary press releases. Transfer to general bios or essays is uncertain. **Reviewed:** 2026-09-27.

## 03 Superficial `-ing` analyses

- **ID:** 03. **Lifecycle:** current. **AI signal:** current_contextual. **Editorial action:** candidate.
- **Trigger and false-positive guard:** A trailing clause asserts new cause or meaning without support; keep a clause that adds a sourced fact.
- **Source and evidence type:** [WikiProject AI Cleanup, “Superficial analyses”](https://en.wikipedia.org/w/index.php?title=Wikipedia:Signs_of_AI_writing&oldid=1376815715#Superficial_analyses) — field observation.
- **Evidence type:** observation. **AI-association support:** limited.
- **Evidence strength and scope:** Direct observation of trailing participial phrases that attach unsupported significance or impact claims. The problem is the unsupported inference, not the `-ing` grammar alone. **Reviewed:** 2026-09-27.

## 04 Promotional language

- **ID:** 04. **Lifecycle:** current. **AI signal:** current_contextual. **Editorial action:** candidate.
- **Trigger and false-positive guard:** Sales language appears in neutral or analytical prose; keep suitable advertising copy and attributed quotations.
- **Source and evidence type:** [WikiProject AI Cleanup, “Promotional and advertisement-like language”](https://en.wikipedia.org/w/index.php?title=Wikipedia:Signs_of_AI_writing&oldid=1376815715#Promotional_and_advertisement-like_language) — field observation.
- **Evidence type:** observation. **AI-association support:** limited.
- **Evidence strength and scope:** Direct examples in encyclopedic writing; Wikipedia's neutral register makes promotional words conspicuous. Promotional language is normal in ads and sales copy, and the source does not prove the training-data or RLHF account in the [former unversioned entry](https://github.com/CyranoB/department-of-prose/blob/f09a61b2369e5e01efff2d99f54efa2dc2453601/skills/slop-explain/patterns/04-promotional-language.md). **Reviewed:** 2026-09-27.

## 05 Vague attributions

- **ID:** 05. **Lifecycle:** current. **AI signal:** current_contextual. **Editorial action:** candidate.
- **Trigger and false-positive guard:** Unnamed experts or studies make a claim seem better sourced than it is; preserve genuine anonymity and never invent a source.
- **Source and evidence type:** [WikiProject AI Cleanup, “Vague attributions and overgeneralization of opinions”](https://en.wikipedia.org/w/index.php?title=Wikipedia:Signs_of_AI_writing&oldid=1376815715#Vague_attributions_and_overgeneralization_of_opinions) — field observation.
- **Evidence type:** observation. **AI-association support:** limited.
- **Evidence strength and scope:** Direct support for checking unnamed authorities or overstated source counts. It is also a general sourcing defect in human writing. Judge whether attribution is warranted in the specific passage. **Reviewed:** 2026-09-27.

## 06 Formulaic challenges sections

- **ID:** 06. **Lifecycle:** current. **AI signal:** current_contextual. **Editorial action:** candidate.
- **Trigger and false-positive guard:** A generic challenges-and-future paragraph contains no specific evidence; keep actual problems and outcomes.
- **Source and evidence type:** [WikiProject AI Cleanup, “Outline-like conclusions about challenges and future prospects”](https://en.wikipedia.org/w/index.php?title=Wikipedia:Signs_of_AI_writing&oldid=1376815715#Outline-like_conclusions_about_challenges_and_future_prospects) — field observation.
- **Evidence type:** observation. **AI-association support:** limited.
- **Evidence strength and scope:** Direct support for a rigid, vague section formula in Wikipedia-style articles. The guide explicitly says mentioning real challenges is not the sign. **Reviewed:** 2026-09-27.

## 07 Invented concept labels

- **ID:** 07. **Lifecycle:** current. **AI signal:** none. **Editorial action:** candidate.
- **Trigger and false-positive guard:** A new label obscures meaning or lacks a definition; preserve defined, useful terms. This is a clarity edit, not an AI signal.
- **Source and evidence type:** [Former unversioned entry](https://github.com/CyranoB/department-of-prose/blob/f09a61b2369e5e01efff2d99f54efa2dc2453601/skills/slop-explain/patterns/07-invented-concept-labels.md) — repo editorial judgment; no independent primary comparison located for the specific “X paradox/trap” pattern.
- **Evidence type:** editorial. **AI-association support:** unsubstantiated.
- **Evidence strength and scope:** The useful question is whether a coined term is defined, attributed, and necessary. Coining a concept is legitimate, and absence from a web search does not show AI origin. The entry's training-data mechanism is unverified. **Reviewed:** 2026-09-27.

## 08 AI vocabulary

- **ID:** 08. **Lifecycle:** current. **AI signal:** current_contextual. **Editorial action:** candidate.
- **Trigger and false-positive guard:** A cluster of stock senses appears relative to passage length; preserve isolated precise, technical, literal, or quoted uses. Apply the versioned #8 list below.
- **Source and evidence type:** [WikiProject AI Cleanup, “High density of ‘AI vocabulary’ words”](https://en.wikipedia.org/w/index.php?title=Wikipedia:Signs_of_AI_writing&oldid=1376815715#High_density_of_%22AI_vocabulary%22_words) — field observation; [EQBench Slop Score methodology](https://eqbench.com/slop-score.html) — corpus benchmark for its *separate, versioned* word and trigram lists.
- **Evidence type:** observation. **AI-association support:** limited.
- **Evidence strength and scope:** Both support looking at concentration relative to genre and meaning, never treating a single word as proof. EQBench's sampled model outputs and human baseline do not validate this editorial entry's whole list, dialect claims, or proposed causes of individual choices. **Reviewed:** 2026-09-27.

## 09 Copula avoidance

- **ID:** 09. **Lifecycle:** current. **AI signal:** current_contextual. **Editorial action:** candidate.
- **Trigger and false-positive guard:** Repeated inflated substitutes for simple verbs blur meaning; keep verbs such as `features` and `represents` when exact.
- **Source and evidence type:** [WikiProject AI Cleanup, “Avoidance of basic copulatives”](https://en.wikipedia.org/w/index.php?title=Wikipedia:Signs_of_AI_writing&oldid=1376815715#Avoidance_of_basic_copulatives_(%22is%22/%22are%22_phrases)) — field observation with cited corpus research.
- **Evidence type:** observation. **AI-association support:** limited.
- **Evidence strength and scope:** Direct support for repeated unnecessary substitutes such as “serves as” in Wikipedia prose. It does not show that every non-copular verb is evasive or that RLHF caused the substitution. **Reviewed:** 2026-09-27.

## 10 Negative parallelisms

- **ID:** 10. **Lifecycle:** current. **AI signal:** current_contextual. **Editorial action:** candidate.
- **Trigger and false-positive guard:** Repeated stock contrasts manufacture a surprise; keep a contrast that makes a real distinction.
- **Source and evidence type:** [WikiProject AI Cleanup, “Negative parallelisms”](https://en.wikipedia.org/w/index.php?title=Wikipedia:Signs_of_AI_writing&oldid=1376815715#Negative_parallelisms) — field observation; [EQBench Slop Score methodology](https://eqbench.com/slop-score.html) — quantitative comparison for selected “not X, but Y” constructions.
- **Evidence type:** observation. **AI-association support:** limited.
- **Evidence strength and scope:** Direct support for overuse of a defined family of contrasts in sampled genres. Both sources acknowledge ordinary human uses. The test is whether the contrast conveys a real distinction. **Reviewed:** 2026-09-27.

## 11 Rule of three

- **ID:** 11. **Lifecycle:** current. **AI signal:** current_contextual. **Editorial action:** candidate.
- **Trigger and false-positive guard:** Repeated triplets add empty third items; preserve genuine three-part inventories and rhetorical triplets that fit the genre.
- **Source and evidence type:** [WikiProject AI Cleanup, “Rule of three”](https://en.wikipedia.org/w/index.php?title=Wikipedia:Signs_of_AI_writing&oldid=1376815715#Rule_of_three) — field observation.
- **Evidence type:** observation. **AI-association support:** limited.
- **Evidence strength and scope:** Support concerns repetitive use or needless third items, not any three-part list. Triplets are an established human rhetorical device. **Reviewed:** 2026-09-27.

## 12 Synonym cycling

- **ID:** 12. **Lifecycle:** current. **AI signal:** historical_only. **Editorial action:** candidate.
- **Trigger and false-positive guard:** Needless synonym substitution obscures reference. Repair that clarity problem without calling it a current AI tell; keep deliberate variation and precise terms.
- **Source and evidence type:** [WikiProject AI Cleanup, “Lexical diversity/elegant variation”](https://en.wikipedia.org/w/index.php?title=Wikipedia:Signs_of_AI_writing&oldid=1376815715#Lexical_diversity/elegant_variation) — **historical** field observation.
- **Evidence type:** observation. **AI-association support:** limited.
- **Evidence strength and scope:** The field guide moved this to historical indicators: older models and some Wikipedia comparisons showed it, but it is not presented as a strong current sign. Swapping a clear technical term for looser synonyms can still harm reference clarity. Do not infer current AI use from it. **Reviewed:** 2026-09-27.

## 13 False ranges

- **ID:** 13. **Lifecycle:** current. **AI signal:** none. **Editorial action:** candidate.
- **Trigger and false-positive guard:** `From X to Y` misleadingly implies a continuum or coverage the text cannot support; keep true time, place, size, and skill ranges.
- **Source and evidence type:** [Former unversioned entry](https://github.com/CyranoB/department-of-prose/blob/f09a61b2369e5e01efff2d99f54efa2dc2453601/skills/slop-explain/patterns/13-false-ranges.md) — repo editorial judgment; no independent primary source located tying “from X to Y” over unrelated items to AI output.
- **Evidence type:** editorial. **AI-association support:** unsubstantiated.
- **Evidence strength and scope:** It can be an imprecise scope claim. The relation between endpoints must be judged semantically; a broad metaphorical range can be intentional. No current AI association established. **Reviewed:** 2026-09-27.

## 14 Anaphora abuse

- **ID:** 14. **Lifecycle:** current. **AI signal:** none. **Editorial action:** candidate.
- **Trigger and false-positive guard:** A long mechanical run weakens the passage; preserve deliberate cadence, especially in speech or poetry.
- **Source and evidence type:** [Former unversioned entry](https://github.com/CyranoB/department-of-prose/blob/f09a61b2369e5e01efff2d99f54efa2dc2453601/skills/slop-explain/patterns/14-anaphora-abuse.md) — repo editorial judgment; no primary comparison located for excessive anaphora in LLM output.
- **Evidence type:** editorial. **AI-association support:** unsubstantiated.
- **Evidence strength and scope:** Repetition can produce empty emphasis in a passage, but anaphora is a standard human rhetorical device. The entry's causal and frequency claims are unsupported. **Reviewed:** 2026-09-27.

## 15 `Not X. Not Y. Just Z.`

- **ID:** 15. **Lifecycle:** current. **AI signal:** none. **Editorial action:** advisory.
- **Trigger and false-positive guard:** Treat as a narrower shape of #10; do not create a second finding or extra weight. Preserve a purposeful contrast.
- **Source and evidence type:** [WikiProject AI Cleanup, “Negative parallelisms”](https://en.wikipedia.org/w/index.php?title=Wikipedia:Signs_of_AI_writing&oldid=1376815715#Negative_parallelisms) — related field observation; [EQBench contrast-pattern methodology](https://github.com/sam-paech/slop-score#not-x-but-y-pattern-detection) — related benchmark family.
- **Evidence type:** observation. **AI-association support:** unsubstantiated.
- **Evidence strength and scope:** The broader negative-contrast family is supported; neither source establishes this exact three-sentence template as a distinct indicator. Avoid double-counting with #10. **Reviewed:** 2026-09-27.

## 16 Rhetorical Q&A

- **ID:** 16. **Lifecycle:** current. **AI signal:** none. **Editorial action:** advisory.
- **Trigger and false-positive guard:** Note canned question-answer beats when they waste space; keep questions a reader needs answered.
- **Source and evidence type:** [Former unversioned entry](https://github.com/CyranoB/department-of-prose/blob/f09a61b2369e5e01efff2d99f54efa2dc2453601/skills/slop-explain/patterns/16-rhetorical-qa.md) — repo editorial judgment; no primary comparative evidence located for rhetorical question/answer pairs as a specific AI sign.
- **Evidence type:** editorial. **AI-association support:** unsubstantiated.
- **Evidence strength and scope:** A staged answer can waste space when the question is artificial; it can also aid teaching and live argument. Treat as a prose function judgment, not a provenance clue. **Reviewed:** 2026-09-27.

## 17 Em dash overuse

- **ID:** 17. **Lifecycle:** current. **AI signal:** none. **Editorial action:** candidate.
- **Trigger and false-positive guard:** Repeated interruptions impair reading; one dash, quoted dashes, and a consistent authorial style remain clean. Current source support as an AI signal is disputed.
- **Source and evidence type:** [WikiProject AI Cleanup, “Overuse of em dashes”](https://en.wikipedia.org/w/index.php?title=Wikipedia:Signs_of_AI_writing&oldid=1376815715#Overuse_of_em_dashes) — qualified field observation.
- **Evidence type:** observation. **AI-association support:** unsubstantiated.
- **Evidence strength and scope:** The source itself says this may need moving to historical indicators, is most useful with other signals, and cites a July 2026 comparison in which only Claude among contemporary models exceeded professional writers' em dash rate while ChatGPT used fewer. Human writers and style guides also use em dashes. **Reviewed:** 2026-09-27.

## 18 Boldface overuse

- **ID:** 18. **Lifecycle:** current. **AI signal:** current_contextual. **Editorial action:** candidate.
- **Trigger and false-positive guard:** Mechanical emphasis impairs reading; keep emphasis required by document format, accessibility, or house style.
- **Source and evidence type:** [WikiProject AI Cleanup, “Overuse of boldface”](https://en.wikipedia.org/w/index.php?title=Wikipedia:Signs_of_AI_writing&oldid=1376815715#Overuse_of_boldface) — field observation.
- **Evidence type:** observation. **AI-association support:** limited.
- **Evidence strength and scope:** Supports a mechanical, repeated emphasis pattern in Wikipedia content. Bold is normal for scannability in many genres. The issue is whether emphasis helps the reader. **Reviewed:** 2026-09-27.

## 19 Inline-header lists

- **ID:** 19. **Lifecycle:** current. **AI signal:** current_contextual. **Editorial action:** advisory.
- **Trigger and false-positive guard:** A labelled list can aid scanning in documentation; note only monotonous or redundant labels, and limit any AI-style observation to the source's Wikipedia context.
- **Source and evidence type:** [WikiProject AI Cleanup, “Inline-header vertical lists”](https://en.wikipedia.org/w/index.php?title=Wikipedia:Signs_of_AI_writing&oldid=1376815715#Inline-header_vertical_lists) — field observation.
- **Evidence type:** observation. **AI-association support:** limited.
- **Evidence strength and scope:** Direct support for a distinctive list shape in Wikipedia, especially when Markdown is pasted into wikitext. In documentation and UI copy, the same form is often useful and conventional. **Reviewed:** 2026-09-27.

## 20 Title Case headings

- **ID:** 20. **Lifecycle:** current. **AI signal:** current_contextual. **Editorial action:** advisory.
- **Trigger and false-positive guard:** Follow the document's house style; Title Case alone is never an actionable finding, and source observations are specific to Wikipedia headings.
- **Source and evidence type:** [WikiProject AI Cleanup, “Title case”](https://en.wikipedia.org/w/index.php?title=Wikipedia:Signs_of_AI_writing&oldid=1376815715#Title_case) — field observation.
- **Evidence type:** observation. **AI-association support:** limited.
- **Evidence strength and scope:** Wikipedia's heading convention makes this relevant there. Other style guides require title case. Do not use title case alone as an AI sign or edit it against a document's house style. **Reviewed:** 2026-09-27.

## 21 Emojis in structure

- **ID:** 21. **Lifecycle:** current. **AI signal:** historical_only. **Editorial action:** advisory.
- **Trigger and false-positive guard:** Follow the audience and house style; the source describes a waning pattern in Wikipedia discussion areas. Preserve intentional emoji labels.
- **Source and evidence type:** [WikiProject AI Cleanup, “Emoji as formatting”](https://en.wikipedia.org/w/index.php?title=Wikipedia:Signs_of_AI_writing&oldid=1376815715#Emoji_as_formatting) — historical/qualified field observation.
- **Evidence type:** observation. **AI-association support:** limited.
- **Evidence strength and scope:** The guide says the examples were mostly on Wikipedia talk pages and edit summaries and have become rare. Emoji can be deliberate in informal copy, accessible UI labels, or social posts. **Reviewed:** 2026-09-27.

## 22 Curly quotes

- **ID:** 22. **Lifecycle:** retired. **AI signal:** none. **Editorial action:** none.
- **Trigger and false-positive guard:** Retire as an AI pattern. Smart quotes are normal in publishing and software. Handle inconsistent typography as a separate copyedit.
- **Source and evidence type:** [WikiProject AI Cleanup, “Curly quotation marks and apostrophes”](https://en.wikipedia.org/w/index.php?title=Wikipedia:Signs_of_AI_writing&oldid=1376815715#Curly_quotation_marks_and_apostrophes) — explicitly weak field observation.
- **Evidence type:** observation. **AI-association support:** unsubstantiated.
- **Evidence strength and scope:** The guide says curly marks alone do not prove LLM use; Word, macOS, iOS, grammar tools, and professional typesetting produce them, while some models typically do not. They are an issue only where the target format requires straight ASCII quotes, such as code or JSON. The [former unversioned entry](https://github.com/CyranoB/department-of-prose/blob/f09a61b2369e5e01efff2d99f54efa2dc2453601/skills/slop-explain/patterns/22-curly-quotes.md) overstates reliability. **Reviewed:** 2026-09-27.

## 23 Chatbot artifacts

- **ID:** 23. **Lifecycle:** current. **AI signal:** current_contextual. **Editorial action:** candidate.
- **Trigger and false-positive guard:** Assistant-addressed boilerplate or model markup appears in prose for readers; keep quoted dialogue, documentation, and transcripts.
- **Source and evidence type:** [WikiProject AI Cleanup, “Collaborative communication”](https://en.wikipedia.org/w/index.php?title=Wikipedia:Signs_of_AI_writing&oldid=1376815715#Collaborative_communication) and [“Internal formatting and reference markup bugs”](https://en.wikipedia.org/w/index.php?title=Wikipedia:Signs_of_AI_writing&oldid=1376815715#Internal_formatting_and_reference_markup_bugs) — first-hand field examples.
- **Evidence type:** observation. **AI-association support:** limited.
- **Evidence strength and scope:** Unedited assistant-addressed text or model-specific markup in a published article is strong evidence of a misplaced chat response, but generic politeness is not. Quoted dialogue, documentation, and intentionally preserved transcripts are legitimate. **Reviewed:** 2026-09-27.

## 24 Knowledge-cutoff disclaimers

- **ID:** 24. **Lifecycle:** current. **AI signal:** current_contextual. **Editorial action:** candidate.
- **Trigger and false-positive guard:** Literal model self-disclosure appears in ordinary prose; keep honest time limits, dated evidence, and quotations.
- **Source and evidence type:** [WikiProject AI Cleanup, “Knowledge-cutoff disclaimers and speculation about gaps in sources”](https://en.wikipedia.org/w/index.php?title=Wikipedia:Signs_of_AI_writing&oldid=1376815715#Knowledge-cutoff_disclaimers_and_speculation_about_gaps_in_sources) — first-hand field examples.
- **Evidence type:** observation. **AI-association support:** limited.
- **Evidence strength and scope:** Literal “my last training update” is an assistant artifact in ordinary published prose. The guide says these date-cutoff formulations were more common in older models; vague claims that sources are unavailable require separate factual checking. A quoted transcript is exempt. **Reviewed:** 2026-09-27.

## 25 Sycophantic tone

- **ID:** 25. **Lifecycle:** current. **AI signal:** current_contextual. **Editorial action:** candidate.
- **Trigger and false-positive guard:** Limit this pattern to an assistant response that flatters or agrees instead of answering. Sincere, reasoned praise stays clean; published promotional prose belongs under #04.
- **Source and evidence type:** [Anthropic, “Towards understanding sycophancy in language models”](https://www.anthropic.com/research/towards-understanding-sycophancy-in-language-models) — primary model-behavior research; [OpenAI's GPT-4o postmortem](https://openai.com/index/sycophancy-in-gpt-4o/) — first-party product incident; [WikiProject “Collaborative communication”](https://en.wikipedia.org/w/index.php?title=Wikipedia:Signs_of_AI_writing&oldid=1376815715#Collaborative_communication) — pasted-output examples.
- **Evidence type:** empirical. **AI-association support:** supported.
- **Evidence strength and scope:** The research supports model agreement and flattery in interactive assistant responses. It does not establish that compliments in published prose are AI-written. The proposed catalogue therefore limits #25 to assistant responses; promotional praise in published prose is assessed under #04. **Reviewed:** 2026-09-27.

## 26 `Here's the kicker`

- **ID:** 26. **Lifecycle:** current. **AI signal:** none. **Editorial action:** advisory.
- **Trigger and false-positive guard:** A repeated scripted opener may be a style tic; keep a transition that introduces a genuine reveal.
- **Source and evidence type:** [Former unversioned entry](https://github.com/CyranoB/department-of-prose/blob/f09a61b2369e5e01efff2d99f54efa2dc2453601/skills/slop-explain/patterns/26-heres-the-kicker.md) — repo editorial judgment; no primary comparative source located for this exact transition.
- **Evidence type:** editorial. **AI-association support:** unsubstantiated.
- **Evidence strength and scope:** A promised surprise that adds no information is a writing defect; a genuine reveal may use the phrase well. The entry's claim that it occurs more in AI output is not verified. **Reviewed:** 2026-09-27.

## 27 `Think of it as`

- **ID:** 27. **Lifecycle:** current. **AI signal:** none. **Editorial action:** advisory.
- **Trigger and false-positive guard:** Check an analogy for explanatory accuracy; keep one that clarifies a hard concept.
- **Source and evidence type:** [Former unversioned entry](https://github.com/CyranoB/department-of-prose/blob/f09a61b2369e5e01efff2d99f54efa2dc2453601/skills/slop-explain/patterns/27-think-of-it-as.md) — repo editorial judgment; no primary comparative source located for this exact analogy introduction.
- **Evidence type:** editorial. **AI-association support:** unsubstantiated.
- **Evidence strength and scope:** An analogy should be tested for explanatory accuracy. Some are useful. No evidence here that the phrase itself is disproportionately generated. **Reviewed:** 2026-09-27.

## 28 `Imagine a world where`

- **ID:** 28. **Lifecycle:** current. **AI signal:** none. **Editorial action:** advisory.
- **Trigger and false-positive guard:** This is ordinary speculative or persuasive language; assess unsupported promises under #01 or #04.
- **Source and evidence type:** [Former unversioned entry](https://github.com/CyranoB/department-of-prose/blob/f09a61b2369e5e01efff2d99f54efa2dc2453601/skills/slop-explain/patterns/28-imagine-a-world-where.md) — repo editorial judgment; no primary comparative source located for this exact opening.
- **Evidence type:** editorial. **AI-association support:** unsubstantiated.
- **Evidence strength and scope:** It is a normal marketing and speculative-writing frame. Flag only an unsupported, one-sided claim in a genre where evidence is expected. No independent AI association established. **Reviewed:** 2026-09-27.

## 29 Disclosure without substance

- **ID:** 29. **Lifecycle:** current. **AI signal:** none. **Editorial action:** advisory.
- **Trigger and false-positive guard:** A first-person disclosure contributes no fact or argument. Do not infer sincerity from the phrase; preserve genuine personal disclosure. Former name: “false vulnerability.”
- **Source and evidence type:** [Former unversioned entry](https://github.com/CyranoB/department-of-prose/blob/f09a61b2369e5e01efff2d99f54efa2dc2453601/skills/slop-explain/patterns/29-false-vulnerability.md) — repo editorial judgment; no primary study located that can validate the sincerity or AI association of this pattern.
- **Evidence type:** editorial. **AI-association support:** unsubstantiated.
- **Evidence strength and scope:** The former name “false vulnerability” imputes an inner state that the text alone cannot prove, for either a human or a model-assisted writer. The new name asks only whether the disclosure supplies a fact or argument. This is an editorial question, not an AI-origin signal. **Reviewed:** 2026-09-27.
- **Previous name:** False vulnerability (lookup alias).

## 30 Filler phrases

- **ID:** 30. **Lifecycle:** current. **AI signal:** none. **Editorial action:** advisory.
- **Trigger and false-positive guard:** Offer concision edits on request; preserve legal, technical, or rhythmically useful phrasing. Isolated wordiness is not an AI tell.
- **Source and evidence type:** [WikiProject AI Cleanup, “Ineffective indicators” / “Signs of human writing: Syntax”](https://en.wikipedia.org/w/index.php?title=Wikipedia:Signs_of_AI_writing&oldid=1376815715#Syntax) — counterevidence to using isolated wordy phrases as AI signs; [former unversioned entry](https://github.com/CyranoB/department-of-prose/blob/f09a61b2369e5e01efff2d99f54efa2dc2453601/skills/slop-explain/patterns/30-filler-phrases.md) — editorial judgment about concision.
- **Evidence type:** observation. **AI-association support:** unsubstantiated.
- **Evidence strength and scope:** The guide explicitly lists isolated “in order to,” “as a result of,” and similar constructions as observed more often in human Wikipedia prose. A phrase can still be unnecessary, but the current AI-origin and training-data claims are unsupported. **Reviewed:** 2026-09-27.

## 31 Excessive hedging

- **ID:** 31. **Lifecycle:** current. **AI signal:** none. **Editorial action:** candidate.
- **Trigger and false-positive guard:** Stacked qualifiers hide the claim; preserve every real uncertainty and source limitation. An isolated hedge stays clean.
- **Source and evidence type:** [WikiProject AI Cleanup, “Signs of human writing: Syntax”](https://en.wikipedia.org/w/index.php?title=Wikipedia:Signs_of_AI_writing&oldid=1376815715#Syntax) — counterevidence for simple hedges; [former unversioned entry](https://github.com/CyranoB/department-of-prose/blob/f09a61b2369e5e01efff2d99f54efa2dc2453601/skills/slop-explain/patterns/31-excessive-hedging.md) — editorial judgment about stacked qualifiers.
- **Evidence type:** observation. **AI-association support:** unsubstantiated.
- **Evidence strength and scope:** The guide lists “perhaps,” “tends to,” and similar qualifiers as more frequent in human Wikipedia prose. It does not test the distinct case of several stacked hedges. Stacking can weaken a claim, but no AI association is established here; uncertainty may be essential in science and legal writing. **Reviewed:** 2026-09-27.

## 32 `The truth is simple`

- **ID:** 32. **Lifecycle:** current. **AI signal:** none. **Editorial action:** advisory.
- **Trigger and false-positive guard:** The phrase alone is no defect; assess an unsupported claim under #01 or #05.
- **Source and evidence type:** [Former unversioned entry](https://github.com/CyranoB/department-of-prose/blob/f09a61b2369e5e01efff2d99f54efa2dc2453601/skills/slop-explain/patterns/32-the-truth-is-simple.md) — repo editorial judgment; no primary comparative source located for this exact authority phrase.
- **Evidence type:** editorial. **AI-association support:** unsubstantiated.
- **Evidence strength and scope:** It can overstate certainty when the evidence is complex. Do not assume AI origin or delete a substantiated plain-language conclusion. **Reviewed:** 2026-09-27.

## 33 Generic positive conclusions

- **ID:** 33. **Lifecycle:** current. **AI signal:** none. **Editorial action:** candidate.
- **Trigger and false-positive guard:** A conclusion promises a positive future without evidence or content; keep a sourced forecast or suitable promotional close. #06 covers the narrow Wikipedia formula.
- **Source and evidence type:** [WikiProject AI Cleanup, “Outline-like conclusions about challenges and future prospects”](https://en.wikipedia.org/w/index.php?title=Wikipedia:Signs_of_AI_writing&oldid=1376815715#Outline-like_conclusions_about_challenges_and_future_prospects) — partial field observation; [former unversioned entry](https://github.com/CyranoB/department-of-prose/blob/f09a61b2369e5e01efff2d99f54efa2dc2453601/skills/slop-explain/patterns/33-generic-positive-conclusions.md) — wider editorial claim.
- **Evidence type:** observation. **AI-association support:** unsubstantiated.
- **Evidence strength and scope:** The source documents a particular upbeat ending inside Wikipedia's rigid “Challenges/Future Prospects” template. It does not validate every optimistic conclusion as an AI sign. Judge whether the conclusion says something specific and supported. **Reviewed:** 2026-09-27.

## 34 Uniform sentence rhythm

- **ID:** 34. **Lifecycle:** current. **AI signal:** none. **Editorial action:** advisory.
- **Trigger and false-positive guard:** Rhythm measurements are descriptive. Offer a cadence edit only if the prose itself suffers and the sample is long enough; keep deliberate form and formal register.
- **Source and evidence type:** [Reinhart et al., “Do LLMs write like humans? Variation in grammatical and rhetorical styles”](https://doi.org/10.1073/pnas.2422455122) — controlled comparison of selected models and human genres; [WikiProject AI Cleanup, “Ineffective indicators”](https://en.wikipedia.org/w/index.php?title=Wikipedia:Signs_of_AI_writing&oldid=1376815715#Ineffective_indicators) — warning about “robotic” prose as a vague tell.
- **Evidence type:** empirical. **AI-association support:** unsubstantiated.
- **Evidence strength and scope:** The study supports genre-dependent grammatical and rhetorical differences; it does **not** establish the entry's universal 18–24-word rhythm, “fingerprint,” or detector-score claims. The field guide specifically rejects generic “robotic” impressions as an effective indicator. Sentence-length variation may matter to editing, but needs a defined measurement, sample length, and genre baseline before use as an AI association. **Reviewed:** 2026-09-27.

## 35 Aphoristic closers

- **ID:** 35. **Lifecycle:** current. **AI signal:** none. **Editorial action:** advisory.
- **Trigger and false-positive guard:** Repeated generic closers may flatten a piece; keep a purposeful concise closing line.
- **Source and evidence type:** [Former unversioned entry](https://github.com/CyranoB/department-of-prose/blob/f09a61b2369e5e01efff2d99f54efa2dc2453601/skills/slop-explain/patterns/35-aphoristic-closers.md) — repo editorial judgment; no primary comparative source located for a repeated epigram at paragraph ends.
- **Evidence type:** editorial. **AI-association support:** unsubstantiated.
- **Evidence strength and scope:** Repetition of a closing device can make prose monotonous. The entry's “tell,” model-cause, and perplexity-detector claims are unverified. An aphorism can be an intentional and effective human choice. **Reviewed:** 2026-09-27.

## 36 Reflexive formality

- **ID:** 36. **Lifecycle:** current. **AI signal:** none. **Editorial action:** advisory.
- **Trigger and false-positive guard:** Formal prose may require no contractions; change register only when the user's document calls for it and meaning survives.
- **Source and evidence type:** [Reinhart et al., PNAS study](https://doi.org/10.1073/pnas.2422455122) — broader register-comparison research; [WikiProject AI Cleanup, “Ineffective indicators”](https://en.wikipedia.org/w/index.php?title=Wikipedia:Signs_of_AI_writing&oldid=1376815715#Ineffective_indicators) — direct caution against using formal prose as a tell; [former unversioned entry](https://github.com/CyranoB/department-of-prose/blob/f09a61b2369e5e01efff2d99f54efa2dc2453601/skills/slop-explain/patterns/36-reflexive-formality.md) — unsupported contraction-specific claim.
- **Evidence type:** empirical. **AI-association support:** unsubstantiated.
- **Evidence strength and scope:** The study finds some model/genre register mismatch; it does not establish that absence of contractions is a reliable AI signal. The field guide explicitly says formal or academic prose is ineffective as a general indicator. Many human documents avoid contractions by house style or genre. The current entry's “most reliable” and detector assertions need removal or direct evidence. **Reviewed:** 2026-09-27.

## Pattern #8 vocabulary

This is the explicit vocabulary considered by editorial pattern #8. It is not
the external scorer's list and does not alter its raw matches. Inflected forms
can be considered only when they carry the same listed sense. A listed word
alone is never an actionable finding. Look for a cluster of stock uses in a
passage, judge its length and register, and quote the uses that support the
finding. An overlap with #01, #03, #04, or #09 is one editorial finding, not
several added together.

| Included words or forms | Sense that can support #8 | Uses that stay clean |
| --- | --- | --- |
| `Additionally` | Repeated sentence-opening transition with no needed logical link. | A useful transition, especially a single occurrence. |
| `delve`, `delves`, `delving` | Formulaic figurative exploration of a topic. | A literal use or an otherwise apt, isolated verb. |
| `landscape`, `tapestry`, `interplay`, `intricate` | Abstract metaphors that substitute for naming the actual relation or setting. | Geography, textiles, precise technical relations, or a metaphor that adds meaning. |
| `pivotal`, `crucial`, `testament`, `enduring` | Unearned importance or legacy claim. | A supported claim, a legal or religious sense of `testament`, or a literal pivot. |
| `vibrant`, `showcase`, `showcasing` | Generic promotional praise where neutral description is required. | Actual colour, a literal showcase, or suitable promotional copy. |
| `underscore`, `underscoring`, `highlight`, `highlighting` | Stock emphasis or trailing analysis that adds no supported information. | The punctuation mark, musical underscoring, physical highlighting, or a specific supported point. |
| `foster`, `fostering`, `garner`, `bolster`, `bolstered`, `enhance`, `enhancing` | Vague positive action without a stated mechanism or result. | Foster care, a measured effect, or a precise domain use. |

`robust`, `key`, `valuable`, `meticulous`, and `align with` are **not**
standalone editorial #8 triggers in this version. They can still appear in
raw scorer output, and a broader sentence may warrant a different editorial
finding. This boundary is deliberately conservative because technical and
ordinary uses are common. Revisit the list when a new primary source or
golden-case review supports a change; record added and removed forms and bump
the catalogue version. The [current field guide's vocabulary section](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing#High_density_of_%22AI_vocabulary%22_words)
is an observation about changing word frequencies, not a permanent blacklist.

## Migration

IDs 01–36 stay reserved. #22 is retired as an AI pattern; old references
resolve to its entry above. #29 is renamed to “Disclosure without
substance”; its previous name remains a lookup alias. #15 is a narrow
shape of #10 and must not be counted as a second finding.

## Change from the unversioned catalogue

Version 1.0.0 includes source provenance, evidence limits, false-positive
guards, and separate AI-signal and editorial-action decisions for all
36 IDs. #12 moves to historical-only AI use; #17 loses its current
AI-signal use; #21 is historical-only; #22 is retired as an AI
pattern; #29 has the new display name above. #8 uses the explicit
sense-guarded vocabulary list. The optional external scorer and its
version are unchanged.
