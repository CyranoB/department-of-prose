# Pattern catalogue source audit

Reviewed: **2026-09-27**. Scope: the 36 editorial entries in [`skills/slop-explain/patterns/`](../skills/slop-explain/patterns/). This is an evidence audit for catalogue decisions, not an authorship detector or a replacement for the pinned raw scorer.

## Source and evidence rules

- **Field observation** means WikiProject AI Cleanup's [*Signs of AI writing*](https://en.wikipedia.org/w/index.php?title=Wikipedia:Signs_of_AI_writing&oldid=1376815715) (revision `1376815715`, retrieved 2026-09-27) documents a pattern in Wikipedia material. It is an advice page, not Wikipedia policy or a controlled comparison. Its examples are specific to Wikipedia; the page itself says the list is descriptive, that some signs do not transfer to other genres, and that no sign by itself proves AI authorship. Section links below point into this recorded revision.
- **Corpus/benchmark evidence** means a primary study or benchmark compares sampled model and human output. It supports only the measured feature, tested models, prompts, genres, and date. [EQBench Slop Score](https://eqbench.com/slop-score.html) compares selected words, trigrams, and contrast patterns in essays and creative writing; it does **not** validate each of these 36 editorial patterns or classify authorship. Its [source code and methodology](https://github.com/sam-paech/slop-score) describe that narrower task.
- **Repo editorial judgment** means we found no independent primary source that validates the specific pattern as a current AI association. Its prose quality concern may still be useful if a passage actually suffers from it. A permalink to the former unversioned entry documents the claim being audited; it is not independent corroboration.
- **Evidence strength** rates support for the specific AI association in this entry, so an indirect empirical source can still leave that claim unsubstantiated. **Strength/limit** below refers to support for an *AI association*, not to the seriousness of a writing problem. No row gives a reliable probability of AI authorship. Several pattern explanations currently assert training causes, RLHF effects, or comparative frequencies without supporting experiments. These mechanisms remain hypotheses unless independently tested.

## 01 Significance inflation

- **Evidence type:** observation.
- **Evidence strength:** limited.
- **Source/type:** [WikiProject AI Cleanup, “Undue emphasis on significance, legacy, and broader trends”](https://en.wikipedia.org/w/index.php?title=Wikipedia:Signs_of_AI_writing&oldid=1376815715#Undue_emphasis_on_significance,_legacy,_and_broader_trends) — field observation.
- **Strength/limit:** Direct match to the editorial pattern, with concrete Wikipedia examples. It supports checking whether the asserted significance is earned; it does not establish that a given writer used AI or that the training incentives asserted in the [former unversioned entry](https://github.com/CyranoB/department-of-prose/blob/f09a61b2369e5e01efff2d99f54efa2dc2453601/skills/slop-explain/patterns/01-significance-inflation.md) caused it. **Reviewed:** 2026-09-27.

## 02 Notability name-dropping

- **Evidence type:** observation.
- **Evidence strength:** limited.
- **Source/type:** [WikiProject AI Cleanup, “Canned emphasis on notability, attribution, and media coverage”](https://en.wikipedia.org/w/index.php?title=Wikipedia:Signs_of_AI_writing&oldid=1376815715#Canned_emphasis_on_notability,_attribution,_and_media_coverage) — field observation.
- **Strength/limit:** Direct in Wikipedia biographies and drafts, where notability is a policy concept. The field guide distinguishes this narrow source-focused phrasing from ordinary press releases. Transfer to general bios or essays is uncertain. **Reviewed:** 2026-09-27.

## 03 Superficial -ing analyses

- **Evidence type:** observation.
- **Evidence strength:** limited.
- **Source/type:** [WikiProject AI Cleanup, “Superficial analyses”](https://en.wikipedia.org/w/index.php?title=Wikipedia:Signs_of_AI_writing&oldid=1376815715#Superficial_analyses) — field observation.
- **Strength/limit:** Direct observation of trailing participial phrases that attach unsupported significance or impact claims. The problem is the unsupported inference, not the `-ing` grammar alone. **Reviewed:** 2026-09-27.

## 04 Promotional language

- **Evidence type:** observation.
- **Evidence strength:** limited.
- **Source/type:** [WikiProject AI Cleanup, “Promotional and advertisement-like language”](https://en.wikipedia.org/w/index.php?title=Wikipedia:Signs_of_AI_writing&oldid=1376815715#Promotional_and_advertisement-like_language) — field observation.
- **Strength/limit:** Direct examples in encyclopedic writing; Wikipedia's neutral register makes promotional words conspicuous. Promotional language is normal in ads and sales copy, and the source does not prove the training-data or RLHF account in the [former unversioned entry](https://github.com/CyranoB/department-of-prose/blob/f09a61b2369e5e01efff2d99f54efa2dc2453601/skills/slop-explain/patterns/04-promotional-language.md). **Reviewed:** 2026-09-27.

## 05 Vague attributions

- **Evidence type:** observation.
- **Evidence strength:** limited.
- **Source/type:** [WikiProject AI Cleanup, “Vague attributions and overgeneralization of opinions”](https://en.wikipedia.org/w/index.php?title=Wikipedia:Signs_of_AI_writing&oldid=1376815715#Vague_attributions_and_overgeneralization_of_opinions) — field observation.
- **Strength/limit:** Direct support for checking unnamed authorities or overstated source counts. It is also a general sourcing defect in human writing. Judge whether attribution is warranted in the specific passage. **Reviewed:** 2026-09-27.

## 06 Formulaic challenges sections

- **Evidence type:** observation.
- **Evidence strength:** limited.
- **Source/type:** [WikiProject AI Cleanup, “Outline-like conclusions about challenges and future prospects”](https://en.wikipedia.org/w/index.php?title=Wikipedia:Signs_of_AI_writing&oldid=1376815715#Outline-like_conclusions_about_challenges_and_future_prospects) — field observation.
- **Strength/limit:** Direct support for a rigid, vague section formula in Wikipedia-style articles. The guide explicitly says mentioning real challenges is not the sign. **Reviewed:** 2026-09-27.

## 07 Invented concept labels

- **Evidence type:** editorial.
- **Evidence strength:** unsubstantiated.
- **Source/type:** [Former unversioned entry](https://github.com/CyranoB/department-of-prose/blob/f09a61b2369e5e01efff2d99f54efa2dc2453601/skills/slop-explain/patterns/07-invented-concept-labels.md) — repo editorial judgment; no independent primary comparison located for the specific “X paradox/trap” pattern.
- **Strength/limit:** The useful question is whether a coined term is defined, attributed, and necessary. Coining a concept is legitimate, and absence from a web search does not show AI origin. The entry's training-data mechanism is unverified. **Reviewed:** 2026-09-27.

## 08 AI vocabulary

- **Evidence type:** observation.
- **Evidence strength:** limited.
- **Source/type:** [WikiProject AI Cleanup, “High density of ‘AI vocabulary’ words”](https://en.wikipedia.org/w/index.php?title=Wikipedia:Signs_of_AI_writing&oldid=1376815715#High_density_of_%22AI_vocabulary%22_words) — field observation; [EQBench Slop Score methodology](https://eqbench.com/slop-score.html) — corpus benchmark for its *separate, versioned* word and trigram lists.
- **Strength/limit:** Both support looking at concentration relative to genre and meaning, never treating a single word as proof. EQBench's sampled model outputs and human baseline do not validate this editorial entry's whole list, dialect claims, or proposed causes of individual choices. **Reviewed:** 2026-09-27.

## 09 Copula avoidance

- **Evidence type:** observation.
- **Evidence strength:** limited.
- **Source/type:** [WikiProject AI Cleanup, “Avoidance of basic copulatives”](https://en.wikipedia.org/w/index.php?title=Wikipedia:Signs_of_AI_writing&oldid=1376815715#Avoidance_of_basic_copulatives_(%22is%22/%22are%22_phrases)) — field observation with cited corpus research.
- **Strength/limit:** Direct support for repeated unnecessary substitutes such as “serves as” in Wikipedia prose. It does not show that every non-copular verb is evasive or that RLHF caused the substitution. **Reviewed:** 2026-09-27.

## 10 Negative parallelisms

- **Evidence type:** observation.
- **Evidence strength:** limited.
- **Source/type:** [WikiProject AI Cleanup, “Negative parallelisms”](https://en.wikipedia.org/w/index.php?title=Wikipedia:Signs_of_AI_writing&oldid=1376815715#Negative_parallelisms) — field observation; [EQBench Slop Score methodology](https://eqbench.com/slop-score.html) — quantitative comparison for selected “not X, but Y” constructions.
- **Strength/limit:** Direct support for overuse of a defined family of contrasts in sampled genres. Both sources acknowledge ordinary human uses. The test is whether the contrast conveys a real distinction. **Reviewed:** 2026-09-27.

## 11 Rule of three

- **Evidence type:** observation.
- **Evidence strength:** limited.
- **Source/type:** [WikiProject AI Cleanup, “Rule of three”](https://en.wikipedia.org/w/index.php?title=Wikipedia:Signs_of_AI_writing&oldid=1376815715#Rule_of_three) — field observation.
- **Strength/limit:** Support concerns repetitive use or needless third items, not any three-part list. Triplets are an established human rhetorical device. **Reviewed:** 2026-09-27.

## 12 Synonym cycling

- **Evidence type:** observation.
- **Evidence strength:** limited.
- **Source/type:** [WikiProject AI Cleanup, “Lexical diversity/elegant variation”](https://en.wikipedia.org/w/index.php?title=Wikipedia:Signs_of_AI_writing&oldid=1376815715#Lexical_diversity/elegant_variation) — **historical** field observation.
- **Strength/limit:** The field guide moved this to historical indicators: older models and some Wikipedia comparisons showed it, but it is not presented as a strong current sign. Swapping a clear technical term for looser synonyms can still harm reference clarity. Do not infer current AI use from it. **Reviewed:** 2026-09-27.

## 13 False ranges

- **Evidence type:** editorial.
- **Evidence strength:** unsubstantiated.
- **Source/type:** [Former unversioned entry](https://github.com/CyranoB/department-of-prose/blob/f09a61b2369e5e01efff2d99f54efa2dc2453601/skills/slop-explain/patterns/13-false-ranges.md) — repo editorial judgment; no independent primary source located tying “from X to Y” over unrelated items to AI output.
- **Strength/limit:** It can be an imprecise scope claim. The relation between endpoints must be judged semantically; a broad metaphorical range can be intentional. No current AI association established. **Reviewed:** 2026-09-27.

## 14 Anaphora abuse

- **Evidence type:** editorial.
- **Evidence strength:** unsubstantiated.
- **Source/type:** [Former unversioned entry](https://github.com/CyranoB/department-of-prose/blob/f09a61b2369e5e01efff2d99f54efa2dc2453601/skills/slop-explain/patterns/14-anaphora-abuse.md) — repo editorial judgment; no primary comparison located for excessive anaphora in LLM output.
- **Strength/limit:** Repetition can produce empty emphasis in a passage, but anaphora is a standard human rhetorical device. The entry's causal and frequency claims are unsupported. **Reviewed:** 2026-09-27.

## 15 “Not X. Not Y. Just Z.”

- **Evidence type:** observation.
- **Evidence strength:** unsubstantiated.
- **Source/type:** [WikiProject AI Cleanup, “Negative parallelisms”](https://en.wikipedia.org/w/index.php?title=Wikipedia:Signs_of_AI_writing&oldid=1376815715#Negative_parallelisms) — related field observation; [EQBench contrast-pattern methodology](https://github.com/sam-paech/slop-score#not-x-but-y-pattern-detection) — related benchmark family.
- **Strength/limit:** The broader negative-contrast family is supported; neither source establishes this exact three-sentence template as a distinct indicator. Avoid double-counting with #10. **Reviewed:** 2026-09-27.

## 16 Rhetorical Q&A

- **Evidence type:** editorial.
- **Evidence strength:** unsubstantiated.
- **Source/type:** [Former unversioned entry](https://github.com/CyranoB/department-of-prose/blob/f09a61b2369e5e01efff2d99f54efa2dc2453601/skills/slop-explain/patterns/16-rhetorical-qa.md) — repo editorial judgment; no primary comparative evidence located for rhetorical question/answer pairs as a specific AI sign.
- **Strength/limit:** A staged answer can waste space when the question is artificial; it can also aid teaching and live argument. Treat as a prose function judgment, not a provenance clue. **Reviewed:** 2026-09-27.

## 17 Em dash overuse

- **Evidence type:** observation.
- **Evidence strength:** unsubstantiated.
- **Source/type:** [WikiProject AI Cleanup, “Overuse of em dashes”](https://en.wikipedia.org/w/index.php?title=Wikipedia:Signs_of_AI_writing&oldid=1376815715#Overuse_of_em_dashes) — qualified field observation.
- **Strength/limit:** The source itself says this may need moving to historical indicators, is most useful with other signals, and cites a July 2026 comparison in which only Claude among contemporary models exceeded professional writers' em dash rate while ChatGPT used fewer. Human writers and style guides also use em dashes. **Reviewed:** 2026-09-27.

## 18 Boldface overuse

- **Evidence type:** observation.
- **Evidence strength:** limited.
- **Source/type:** [WikiProject AI Cleanup, “Overuse of boldface”](https://en.wikipedia.org/w/index.php?title=Wikipedia:Signs_of_AI_writing&oldid=1376815715#Overuse_of_boldface) — field observation.
- **Strength/limit:** Supports a mechanical, repeated emphasis pattern in Wikipedia content. Bold is normal for scannability in many genres. The issue is whether emphasis helps the reader. **Reviewed:** 2026-09-27.

## 19 Inline-header lists

- **Evidence type:** observation.
- **Evidence strength:** limited.
- **Source/type:** [WikiProject AI Cleanup, “Inline-header vertical lists”](https://en.wikipedia.org/w/index.php?title=Wikipedia:Signs_of_AI_writing&oldid=1376815715#Inline-header_vertical_lists) — field observation.
- **Strength/limit:** Direct support for a distinctive list shape in Wikipedia, especially when Markdown is pasted into wikitext. In documentation and UI copy, the same form is often useful and conventional. **Reviewed:** 2026-09-27.

## 20 Title Case headings

- **Evidence type:** observation.
- **Evidence strength:** limited.
- **Source/type:** [WikiProject AI Cleanup, “Title case”](https://en.wikipedia.org/w/index.php?title=Wikipedia:Signs_of_AI_writing&oldid=1376815715#Title_case) — field observation.
- **Strength/limit:** Wikipedia's heading convention makes this relevant there. Other style guides require title case. Do not use title case alone as an AI sign or edit it against a document's house style. **Reviewed:** 2026-09-27.

## 21 Emojis in structure

- **Evidence type:** observation.
- **Evidence strength:** limited.
- **Source/type:** [WikiProject AI Cleanup, “Emoji as formatting”](https://en.wikipedia.org/w/index.php?title=Wikipedia:Signs_of_AI_writing&oldid=1376815715#Emoji_as_formatting) — historical/qualified field observation.
- **Strength/limit:** The guide says the examples were mostly on Wikipedia talk pages and edit summaries and have become rare. Emoji can be deliberate in informal copy, accessible UI labels, or social posts. **Reviewed:** 2026-09-27.

## 22 Curly quotes

- **Evidence type:** observation.
- **Evidence strength:** unsubstantiated.
- **Source/type:** [WikiProject AI Cleanup, “Curly quotation marks and apostrophes”](https://en.wikipedia.org/w/index.php?title=Wikipedia:Signs_of_AI_writing&oldid=1376815715#Curly_quotation_marks_and_apostrophes) — explicitly weak field observation.
- **Strength/limit:** The guide says curly marks alone do not prove LLM use; Word, macOS, iOS, grammar tools, and professional typesetting produce them, while some models typically do not. They are an issue only where the target format requires straight ASCII quotes, such as code or JSON. The [former unversioned entry](https://github.com/CyranoB/department-of-prose/blob/f09a61b2369e5e01efff2d99f54efa2dc2453601/skills/slop-explain/patterns/22-curly-quotes.md) overstates reliability. **Reviewed:** 2026-09-27.

## 23 Chatbot artifacts

- **Evidence type:** observation.
- **Evidence strength:** limited.
- **Source/type:** [WikiProject AI Cleanup, “Collaborative communication”](https://en.wikipedia.org/w/index.php?title=Wikipedia:Signs_of_AI_writing&oldid=1376815715#Collaborative_communication) and [“Internal formatting and reference markup bugs”](https://en.wikipedia.org/w/index.php?title=Wikipedia:Signs_of_AI_writing&oldid=1376815715#Internal_formatting_and_reference_markup_bugs) — first-hand field examples.
- **Strength/limit:** Unedited assistant-addressed text or model-specific markup in a published article is strong evidence of a misplaced chat response, but generic politeness is not. Quoted dialogue, documentation, and intentionally preserved transcripts are legitimate. **Reviewed:** 2026-09-27.

## 24 Knowledge-cutoff disclaimers

- **Evidence type:** observation.
- **Evidence strength:** limited.
- **Source/type:** [WikiProject AI Cleanup, “Knowledge-cutoff disclaimers and speculation about gaps in sources”](https://en.wikipedia.org/w/index.php?title=Wikipedia:Signs_of_AI_writing&oldid=1376815715#Knowledge-cutoff_disclaimers_and_speculation_about_gaps_in_sources) — first-hand field examples.
- **Strength/limit:** Literal “my last training update” is an assistant artifact in ordinary published prose. The guide says these date-cutoff formulations were more common in older models; vague claims that sources are unavailable require separate factual checking. A quoted transcript is exempt. **Reviewed:** 2026-09-27.

## 25 Sycophantic tone

- **Evidence type:** empirical.
- **Evidence strength:** supported.
- **Source/type:** [Anthropic, “Towards understanding sycophancy in language models”](https://www.anthropic.com/research/towards-understanding-sycophancy-in-language-models) — primary model-behavior research; [OpenAI's GPT-4o postmortem](https://openai.com/index/sycophancy-in-gpt-4o/) — first-party product incident; [WikiProject “Collaborative communication”](https://en.wikipedia.org/w/index.php?title=Wikipedia:Signs_of_AI_writing&oldid=1376815715#Collaborative_communication) — pasted-output examples.
- **Strength/limit:** The research supports model agreement and flattery in interactive assistant responses. It does not establish that compliments in published prose are AI-written. The proposed catalogue therefore limits #25 to assistant responses; promotional praise in published prose is assessed under #04. **Reviewed:** 2026-09-27.

## 26 “Here's the kicker”

- **Evidence type:** editorial.
- **Evidence strength:** unsubstantiated.
- **Source/type:** [Former unversioned entry](https://github.com/CyranoB/department-of-prose/blob/f09a61b2369e5e01efff2d99f54efa2dc2453601/skills/slop-explain/patterns/26-heres-the-kicker.md) — repo editorial judgment; no primary comparative source located for this exact transition.
- **Strength/limit:** A promised surprise that adds no information is a writing defect; a genuine reveal may use the phrase well. The entry's claim that it occurs more in AI output is not verified. **Reviewed:** 2026-09-27.

## 27 “Think of it as...”

- **Evidence type:** editorial.
- **Evidence strength:** unsubstantiated.
- **Source/type:** [Former unversioned entry](https://github.com/CyranoB/department-of-prose/blob/f09a61b2369e5e01efff2d99f54efa2dc2453601/skills/slop-explain/patterns/27-think-of-it-as.md) — repo editorial judgment; no primary comparative source located for this exact analogy introduction.
- **Strength/limit:** An analogy should be tested for explanatory accuracy. Some are useful. No evidence here that the phrase itself is disproportionately generated. **Reviewed:** 2026-09-27.

## 28 “Imagine a world where...”

- **Evidence type:** editorial.
- **Evidence strength:** unsubstantiated.
- **Source/type:** [Former unversioned entry](https://github.com/CyranoB/department-of-prose/blob/f09a61b2369e5e01efff2d99f54efa2dc2453601/skills/slop-explain/patterns/28-imagine-a-world-where.md) — repo editorial judgment; no primary comparative source located for this exact opening.
- **Strength/limit:** It is a normal marketing and speculative-writing frame. Flag only an unsupported, one-sided claim in a genre where evidence is expected. No independent AI association established. **Reviewed:** 2026-09-27.

## 29 Disclosure without substance (formerly “false vulnerability”)

- **Evidence type:** editorial.
- **Evidence strength:** unsubstantiated.
- **Source/type:** [Former unversioned entry](https://github.com/CyranoB/department-of-prose/blob/f09a61b2369e5e01efff2d99f54efa2dc2453601/skills/slop-explain/patterns/29-false-vulnerability.md) — repo editorial judgment; no primary study located that can validate the sincerity or AI association of this pattern.
- **Strength/limit:** The former name “false vulnerability” imputes an inner state that the text alone cannot prove, for either a human or a model-assisted writer. The new name asks only whether the disclosure supplies a fact or argument. This is an editorial question, not an AI-origin signal. **Reviewed:** 2026-09-27.

## 30 Filler phrases

- **Evidence type:** observation.
- **Evidence strength:** unsubstantiated.
- **Source/type:** [WikiProject AI Cleanup, “Ineffective indicators” / “Signs of human writing: Syntax”](https://en.wikipedia.org/w/index.php?title=Wikipedia:Signs_of_AI_writing&oldid=1376815715#Syntax) — counterevidence to using isolated wordy phrases as AI signs; [former unversioned entry](https://github.com/CyranoB/department-of-prose/blob/f09a61b2369e5e01efff2d99f54efa2dc2453601/skills/slop-explain/patterns/30-filler-phrases.md) — editorial judgment about concision.
- **Strength/limit:** The guide explicitly lists isolated “in order to,” “as a result of,” and similar constructions as observed more often in human Wikipedia prose. A phrase can still be unnecessary, but the current AI-origin and training-data claims are unsupported. **Reviewed:** 2026-09-27.

## 31 Excessive hedging

- **Evidence type:** observation.
- **Evidence strength:** unsubstantiated.
- **Source/type:** [WikiProject AI Cleanup, “Signs of human writing: Syntax”](https://en.wikipedia.org/w/index.php?title=Wikipedia:Signs_of_AI_writing&oldid=1376815715#Syntax) — counterevidence for simple hedges; [former unversioned entry](https://github.com/CyranoB/department-of-prose/blob/f09a61b2369e5e01efff2d99f54efa2dc2453601/skills/slop-explain/patterns/31-excessive-hedging.md) — editorial judgment about stacked qualifiers.
- **Strength/limit:** The guide lists “perhaps,” “tends to,” and similar qualifiers as more frequent in human Wikipedia prose. It does not test the distinct case of several stacked hedges. Stacking can weaken a claim, but no AI association is established here; uncertainty may be essential in science and legal writing. **Reviewed:** 2026-09-27.

## 32 “The truth is simple”

- **Evidence type:** editorial.
- **Evidence strength:** unsubstantiated.
- **Source/type:** [Former unversioned entry](https://github.com/CyranoB/department-of-prose/blob/f09a61b2369e5e01efff2d99f54efa2dc2453601/skills/slop-explain/patterns/32-the-truth-is-simple.md) — repo editorial judgment; no primary comparative source located for this exact authority phrase.
- **Strength/limit:** It can overstate certainty when the evidence is complex. Do not assume AI origin or delete a substantiated plain-language conclusion. **Reviewed:** 2026-09-27.

## 33 Generic positive conclusions

- **Evidence type:** observation.
- **Evidence strength:** unsubstantiated.
- **Source/type:** [WikiProject AI Cleanup, “Outline-like conclusions about challenges and future prospects”](https://en.wikipedia.org/w/index.php?title=Wikipedia:Signs_of_AI_writing&oldid=1376815715#Outline-like_conclusions_about_challenges_and_future_prospects) — partial field observation; [former unversioned entry](https://github.com/CyranoB/department-of-prose/blob/f09a61b2369e5e01efff2d99f54efa2dc2453601/skills/slop-explain/patterns/33-generic-positive-conclusions.md) — wider editorial claim.
- **Strength/limit:** The source documents a particular upbeat ending inside Wikipedia's rigid “Challenges/Future Prospects” template. It does not validate every optimistic conclusion as an AI sign. Judge whether the conclusion says something specific and supported. **Reviewed:** 2026-09-27.

## 34 Uniform sentence rhythm

- **Evidence type:** empirical.
- **Evidence strength:** unsubstantiated.
- **Source/type:** [Reinhart et al., “Do LLMs write like humans? Variation in grammatical and rhetorical styles”](https://doi.org/10.1073/pnas.2422455122) — controlled comparison of selected models and human genres; [WikiProject AI Cleanup, “Ineffective indicators”](https://en.wikipedia.org/w/index.php?title=Wikipedia:Signs_of_AI_writing&oldid=1376815715#Ineffective_indicators) — warning about “robotic” prose as a vague tell.
- **Strength/limit:** The study supports genre-dependent grammatical and rhetorical differences; it does **not** establish the entry's universal 18–24-word rhythm, “fingerprint,” or detector-score claims. The field guide specifically rejects generic “robotic” impressions as an effective indicator. Sentence-length variation may matter to editing, but needs a defined measurement, sample length, and genre baseline before use as an AI association. **Reviewed:** 2026-09-27.

## 35 Aphoristic paragraph closers

- **Evidence type:** editorial.
- **Evidence strength:** unsubstantiated.
- **Source/type:** [Former unversioned entry](https://github.com/CyranoB/department-of-prose/blob/f09a61b2369e5e01efff2d99f54efa2dc2453601/skills/slop-explain/patterns/35-aphoristic-closers.md) — repo editorial judgment; no primary comparative source located for a repeated epigram at paragraph ends.
- **Strength/limit:** Repetition of a closing device can make prose monotonous. The entry's “tell,” model-cause, and perplexity-detector claims are unverified. An aphorism can be an intentional and effective human choice. **Reviewed:** 2026-09-27.

## 36 Reflexive formality

- **Evidence type:** empirical.
- **Evidence strength:** unsubstantiated.
- **Source/type:** [Reinhart et al., PNAS study](https://doi.org/10.1073/pnas.2422455122) — broader register-comparison research; [WikiProject AI Cleanup, “Ineffective indicators”](https://en.wikipedia.org/w/index.php?title=Wikipedia:Signs_of_AI_writing&oldid=1376815715#Ineffective_indicators) — direct caution against using formal prose as a tell; [former unversioned entry](https://github.com/CyranoB/department-of-prose/blob/f09a61b2369e5e01efff2d99f54efa2dc2453601/skills/slop-explain/patterns/36-reflexive-formality.md) — unsupported contraction-specific claim.
- **Strength/limit:** The study finds some model/genre register mismatch; it does not establish that absence of contractions is a reliable AI signal. The field guide explicitly says formal or academic prose is ineffective as a general indicator. Many human documents avoid contractions by house style or genre. The current entry's “most reliable” and detector assertions need removal or direct evidence. **Reviewed:** 2026-09-27.

## Audit implications

1. Keep the external scorer's measured word/trigram/contrast output separate from these editorial judgments. Its methodology does not certify all 36 patterns.
2. The clearest source-supported editorial problems are unsupported significance, analysis, attribution, and copied assistant artifacts. Even these require genre and passage context.
3. Reassess #12, #17, #21, #22, and #30–36 before letting them affect a verdict. #12 is historical; #17 and #21 are qualified or waning; #22 has abundant legitimate causes; #30, #31, #34, and #36 encounter explicit counterevidence or caveats in the field guide. #13–16 and #26–29 lack pattern-specific primary validation.
4. Audit the “Why LLMs do this” sections separately. Most tell causal stories about training corpora, RLHF, or token prediction without direct experiments for that pattern. Retain them only as labeled hypotheses or replace them with observed behavior.
