# Golden-case review rubric

Golden reviews assess meaning and editorial judgment, not whether a model emits
one preferred sentence. Run the candidate workflow on each relevant case and
save a review record based on `golden/review-template.json`.

## Review steps

1. Record the golden case schema revision, this rubric revision, the exact git
   revision of the skill, and the case IDs reviewed.
2. Record the model identifier plus every available version, date, temperature,
   seed, reasoning, and system/prompt setting. Use `unknown` when the provider
   does not expose a value; never guess it.
3. Preserve the complete model output in the review record or a linked immutable
   artifact. Do not review a hand-edited reconstruction.
4. Score each dimension below as `pass`, `minor`, or `fail` and give a concrete
   reason quoting only the smallest necessary excerpt from the output.
5. Give the case an overall `pass` only when every critical dimension passes.
   Style can vary freely inside the fixture's permitted outcomes.

## Dimensions

| Dimension | Pass | Minor | Fail | Critical |
|---|---|---|---|---|
| Finding coverage | All required findings appear; permitted findings may appear; forbidden findings do not. | A permitted label is debatable but does not alter the edit. | A required finding is missing or a forbidden finding is asserted. | Yes |
| Contextual assessment | Raw signals are distinguished from actionable defects in this passage. | The distinction is implied but not clearly stated. | A legitimate technical, quoted, formal, or deliberate voice feature is treated as an automatic defect. | Yes |
| Fact preservation | Every listed fact survives with the same relationships and quantities. | A nonessential detail becomes less explicit but remains recoverable. | A fact is removed, contradicted, or materially changed. | Yes |
| Qualification and verification | Uncertainty, source limits, attribution, and verification status survive. | Wording is slightly stronger or weaker without changing the reader's practical conclusion. | An estimate becomes fact, a caveat disappears, or verification is invented. | Yes |
| No invention | No prohibited addition or unsupported fact appears. | A harmless connective inference appears and is clearly framed as inference. | The rewrite invents evidence, dates, causes, outcomes, identities, or support. | Yes |
| Voice and register | Required voice markers, deliberate repetition, quotations, punctuation, and genre register remain. | Cadence changes slightly without flattening the named marker. | A named voice marker is normalized away or a quotation is altered. | Yes |
| Pattern reduction | Items named under `must_change` are removed or repaired without collateral damage. | One residue remains but no critical contract is harmed. | The target pattern remains substantially unchanged or the rewrite introduces another forbidden pattern. | No |
| Readability | The result is coherent, grammatical for its intended voice, and no more cumbersome than the source. | A local phrase is awkward. | Meaning is difficult to follow or the rewrite is materially worse. | No |

`minor` is not an automatic failure for noncritical dimensions. The reviewer
must explain why an overall pass still represents an acceptable editorial
outcome. Any critical `minor` or `fail` makes the overall result fail.

## Comparing a change

Use the same case set and settings when comparing revisions. Review outputs
blind to revision name where practical. A baseline update requires a written
reason per changed dimension; nondeterministic wording drift is not itself a
regression. Prefer contracts that admit multiple good rewrites over adding an
exact expected string.

Rubric revision: `1`
