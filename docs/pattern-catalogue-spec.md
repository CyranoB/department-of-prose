# Pattern catalogue decision spec

Status: implemented catalogue policy, version `1.0.0` (2026-09-27). This
document specifies the editorial decisions for issue #14. The companion [source audit](pattern-catalogue-source-audit.md)
records the primary source and evidence limit for each pattern.

## Scope and meaning

The catalogue contains the 36 numbered editorial patterns currently taught by
Slop Sense. A pattern is an editing lens, not proof that AI wrote a passage.
Two questions need separate answers: whether a primary source supports a
current AI-style association in a stated context, and whether this passage
has an editorial problem worth repairing. For example, synonym cycling can
harm clarity even though its AI association is historical; a false range can
misstate scope without any established AI association.
The optional `slop-detector@1.2.0` word, trigram, and construction lists are
separate raw measurements. Its number and hit counts must remain identifiable
as raw scorer output. The catalogue has its own version; changing this policy
does not change the scorer version or retroactively change its measurements.

The WikiProject AI Cleanup field guide is descriptive and primarily about
Wikipedia text. It says its signs can occur in human writing and that a sign
is not itself the underlying problem. EQ-Bench likewise says Slop Score is not
an AI detector and is optimized for creative writing and essays. Thus a source
that describes a pattern does not by itself justify a rewrite in every genre.
See the [WikiProject caveats](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
and [EQ-Bench method and limits](https://eqbench.com/slop-score.html).

## Entry format

Each catalogue entry must include these fields. Store them in a single
versioned catalogue when implementing #14; skill prose can be generated from
or checked against it.

```yaml
id: 12                         # Stable, never reused
name: Synonym cycling
previous_names: []
lifecycle: current              # current | retired
ai_signal_use: historical_only  # current_contextual | historical_only | none
editorial_action: candidate     # candidate | advisory | none
evidence_type: observation      # empirical | observation | editorial
evidence_strength: limited      # supported | limited | unsubstantiated
sources:
  - url: https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing?oldid=1376815715
    section: Historical indicators / Lexical diversity/elegant variation
    reviewed: 2026-09-27
scope: Older model output; over-varied references to one subject
trigger: Repeated, unnecessary synonym substitution that obscures reference
guard: Deliberate variation, a change of referent, or useful precise terms
reason: The cited guide treats the AI association as historical, but confusing
  substitutions can still be a clarity problem.
supersedes: []                 # Stable IDs of entries consolidated into this one
```

`evidence_strength` describes support for a general AI association, not the
cost of a real writing defect. `supported` requires directly relevant empirical
evidence with stated corpus and limits; `limited` covers a first-party field
guide or narrow study; `unsubstantiated` means the catalogue has only an
editorial judgment. A source can support an editing recommendation without
supporting an AI-authorship claim. Do not turn these labels into probabilities
or numeric severity weights.

## Decision axes and output rules

**AI signal use** describes what may be said about a pattern's association
with model output. `current_contextual` permits a carefully scoped AI-style
observation when the source and passage support it. `historical_only` permits
an explanation of past model behavior, never a current AI-style finding.
`none` permits no AI-style finding. None of these labels permits a claim,
score, or probability about who wrote the passage.

**Editorial action** describes what to do with the writing.
`candidate` means a finding and repair are allowed only if the exact passage
shows a problem, the guard is checked, and the repair preserves facts and
voice. `advisory` means an optional style note, with a change only when the
user requests that style. `none` means no finding or repair under this
pattern. A pattern can be a candidate for an editorial repair while its
`ai_signal_use` is `historical_only` or `none`.

The report must display the optional scorer's number, matches, and counts as
**raw scorer output**. It must label contextual editorial findings separately.
When a user asks for AI-writing signals, only entries marked
`current_contextual` may appear in that evidence summary, with their scope
and limits. An editorial finding with `ai_signal_use: none` must never
increase an “AI tells” count or band. A raw match also cannot increase a
contextual severity judgment until its meaning and guard are assessed.
`slop-check` may give a short repair direction for an actionable editorial
finding but never a rewritten passage. `slop-sense` may apply a fact-safe
repair. The existing “heavy AI tells” output bands must be revised before
using this catalogue, because the editorial findings are not authorship
evidence.

All 36 IDs remain reserved. A retired entry keeps a numbered lookup and a
short explanation; it does not vanish from existing links. If a later change
must rename or merge entries, publish an old-to-new ID map and update all
references. A raw scorer hit never overrides a catalogue guard.

## Proposed decisions for the 36 current patterns

The [source audit](pattern-catalogue-source-audit.md) records each pattern's
source, evidence type, strength, and limits. The table gives its two policy
decisions and the minimum guard. `Current` abbreviates
`current_contextual`, `Past` abbreviates `historical_only`, and `None`
means no AI-style finding. Editorial `Candidate` always requires an
actionable problem in this passage; it never means “rewrite every match.”

| ID | Pattern | AI signal | Editorial action | Trigger and guard |
| --- | --- | --- | --- | --- |
| 01 | Significance inflation | Current | Candidate | Unsupported claims of historic importance or broad impact; preserve importance supported by cited facts. |
| 02 | Notability name-dropping | Current | Candidate | Credentials or outlet lists that substitute for a relevant claim, especially in encyclopedic prose; keep coverage that explains why it matters. |
| 03 | Superficial `-ing` analyses | Current | Candidate | A trailing clause asserts new cause or meaning without support; keep a clause that adds a sourced fact. |
| 04 | Promotional language | Current | Candidate | Sales language appears in neutral or analytical prose; keep suitable advertising copy and attributed quotations. |
| 05 | Vague attributions | Current | Candidate | Unnamed experts or studies make a claim seem better sourced than it is; preserve genuine anonymity and never invent a source. |
| 06 | Formulaic challenges sections | Current | Candidate | A generic challenges-and-future paragraph contains no specific evidence; keep actual problems and outcomes. |
| 07 | Invented concept labels | None | Candidate | A new label obscures meaning or lacks a definition; preserve defined, useful terms. This is a clarity edit, not an AI signal. |
| 08 | AI vocabulary | Current | Candidate | A cluster of stock senses appears relative to passage length; preserve isolated precise, technical, literal, or quoted uses. Apply the versioned #8 list below. |
| 09 | Copula avoidance | Current | Candidate | Repeated inflated substitutes for simple verbs blur meaning; keep verbs such as `features` and `represents` when exact. |
| 10 | Negative parallelisms | Current | Candidate | Repeated stock contrasts manufacture a surprise; keep a contrast that makes a real distinction. |
| 11 | Rule of three | Current | Candidate | Repeated triplets add empty third items; preserve genuine three-part inventories and rhetorical triplets that fit the genre. |
| 12 | Synonym cycling | Past | Candidate | Needless synonym substitution obscures reference. Repair that clarity problem without calling it a current AI tell; keep deliberate variation and precise terms. |
| 13 | False ranges | None | Candidate | `From X to Y` misleadingly implies a continuum or coverage the text cannot support; keep true time, place, size, and skill ranges. |
| 14 | Anaphora abuse | None | Candidate | A long mechanical run weakens the passage; preserve deliberate cadence, especially in speech or poetry. |
| 15 | `Not X. Not Y. Just Z.` | None | Advisory | Treat as a narrower shape of #10; do not create a second finding or extra weight. Preserve a purposeful contrast. |
| 16 | Rhetorical Q&A | None | Advisory | Note canned question-answer beats when they waste space; keep questions a reader needs answered. |
| 17 | Em dash overuse | None | Candidate | Repeated interruptions impair reading; one dash, quoted dashes, and a consistent authorial style remain clean. Current source support as an AI signal is disputed. |
| 18 | Boldface overuse | Current | Candidate | Mechanical emphasis impairs reading; keep emphasis required by document format, accessibility, or house style. |
| 19 | Inline-header lists | Current | Advisory | A labelled list can aid scanning in documentation; note only monotonous or redundant labels, and limit any AI-style observation to the source's Wikipedia context. |
| 20 | Title Case headings | Current | Advisory | Follow the document's house style; Title Case alone is never an actionable finding, and source observations are specific to Wikipedia headings. |
| 21 | Emojis in structure | Past | Advisory | Follow the audience and house style; the source describes a waning pattern in Wikipedia discussion areas. Preserve intentional emoji labels. |
| 22 | Curly quotes | None | None | Retire as an AI pattern. Smart quotes are normal in publishing and software. Handle inconsistent typography as a separate copyedit. |
| 23 | Chatbot artifacts | Current | Candidate | Assistant-addressed boilerplate or model markup appears in prose for readers; keep quoted dialogue, documentation, and transcripts. |
| 24 | Knowledge-cutoff disclaimers | Current | Candidate | Literal model self-disclosure appears in ordinary prose; keep honest time limits, dated evidence, and quotations. |
| 25 | Sycophantic tone | Current | Candidate | Limit this pattern to an assistant response that flatters or agrees instead of answering. Sincere, reasoned praise stays clean; published promotional prose belongs under #04. |
| 26 | `Here's the kicker` | None | Advisory | A repeated scripted opener may be a style tic; keep a transition that introduces a genuine reveal. |
| 27 | `Think of it as` | None | Advisory | Check an analogy for explanatory accuracy; keep one that clarifies a hard concept. |
| 28 | `Imagine a world where` | None | Advisory | This is ordinary speculative or persuasive language; assess unsupported promises under #01 or #04. |
| 29 | Disclosure without substance | None | Advisory | A first-person disclosure contributes no fact or argument. Do not infer sincerity from the phrase; preserve genuine personal disclosure. Former name: “false vulnerability.” |
| 30 | Filler phrases | None | Advisory | Offer concision edits on request; preserve legal, technical, or rhythmically useful phrasing. Isolated wordiness is not an AI tell. |
| 31 | Excessive hedging | None | Candidate | Stacked qualifiers hide the claim; preserve every real uncertainty and source limitation. An isolated hedge stays clean. |
| 32 | `The truth is simple` | None | Advisory | The phrase alone is no defect; assess an unsupported claim under #01 or #05. |
| 33 | Generic positive conclusions | None | Candidate | A conclusion promises a positive future without evidence or content; keep a sourced forecast or suitable promotional close. #06 covers the narrow Wikipedia formula. |
| 34 | Uniform sentence rhythm | None | Advisory | Rhythm measurements are descriptive. Offer a cadence edit only if the prose itself suffers and the sample is long enough; keep deliberate form and formal register. |
| 35 | Aphoristic closers | None | Advisory | Repeated generic closers may flatten a piece; keep a purposeful concise closing line. |
| 36 | Reflexive formality | None | Advisory | Formal prose may require no contractions; change register only when the user's document calls for it and meaning survives. |

## Pattern #8 editorial vocabulary, version `1.0.0`

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

## Deduplication and migration

Use the most specific supported finding as the primary one. One span can be
evidence for several patterns, but it should not inflate the verdict by being
counted several times. In particular, #15 is a narrower shape of #10; #25
may overlap #23; and #08 lexical words may also support #01 or #04. Preserve
the original IDs in explanations and migration records. Proposed version
`1.0.0` keeps IDs 01–36 and retires #22 as an AI pattern, so no ID is
renumbered. Old references to #22 resolve to its retired entry. #29 keeps its
ID but changes its display name from “False vulnerability” to “Disclosure
without substance”; lookups for the old name resolve to #29. Record both
changes in the catalogue change log.

## How to apply this spec

1. Review the source audit for all 36 entries. Where a source
   does not support the old explanation, revise the policy or explanation; do
   not manufacture empirical support.
2. Publish the versioned catalogue with one record per ID, including retired
   IDs. Record the changes from the previous unversioned catalogue.
3. Update `slop-sense`, `slop-check`, `slop-explain`, README, the bundle source,
   and packaging checks together. Separate raw scorer output, editorial
   findings, and current contextual AI-style observations in every report;
   replace the existing “AI tells” verdict bands.
4. Review the existing golden cases and add the cases needed for changed
   decisions. Then use the catalogue as the policy input for issue #13.

This spec sets editorial policy. It does not set deterministic thresholds for
model judgment or claim a measured detection accuracy for the 36 patterns.
