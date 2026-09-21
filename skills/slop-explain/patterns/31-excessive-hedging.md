# Pattern 31: Excessive hedging

**Stacked qualifiers: "could potentially possibly be argued that it might."**

## Why LLMs do this

LLMs are trained to avoid overclaiming. Hedging is rewarded by safety and accuracy criteria: a sentence that says "this might be true" cannot be wrong in the way a sentence that says "this is true" can. The model learned to add hedges almost reflexively whenever a claim approaches anything contested.

The hedges also stack. "Could" softens, "potentially" softens further, "possibly" further still, "it might be argued that" pulls back even more. Each layer is individually defensible. The cumulative effect is a sentence that has retreated so far from its own claim that there is nothing left to evaluate.

## Why readers notice it

The stacking is the tell. A human writer uses one hedge per claim, sometimes none. An LLM uses three or four, because each layer was selected independently by a model trying to be careful.

The resulting sentences cannot be acted on or disagreed with. They have nothing concrete to grip. Readers learn to skim past them, which means the writer has spent words for no information transfer.

The pattern is especially common in policy writing, opinion pieces, and analysis where the writer (or the model) is afraid of being wrong. The fear shows.

## Examples

After:
> The new policy may reduce hiring in low-margin sectors.

Before:
> It could potentially be argued that the new policy might possibly lead to a reduction in hiring in certain low-margin sectors.

After:
> The migration will probably take two weeks.

Before:
> The migration could possibly potentially take approximately around two weeks, give or take.

After:
> The model probably handles this case correctly.

Before:
> It seems likely that the model may potentially handle this case in a way that could be considered correct, though there is some chance it might not.

Notice that the human versions use one hedge (or none) per claim. The AI versions stack three or four, draining the sentence of any usable content.

## How to self-spot

Search for hedge clusters. The common stack:

- modal: "may," "might," "could," "would"
- adverb: "potentially," "possibly," "probably," "perhaps," "arguably"
- frame: "it could be argued that," "it seems likely that," "there is some chance that"
- range: "approximately," "around," "roughly," "give or take"

Each of these alone is fine. Two together is suspect. Three or four is slop.

The fix: pick at most one hedge per claim. If the claim genuinely needs more uncertainty, name the source of the uncertainty ("the 2023 figures may not reflect post-merger changes") rather than stacking modal verbs.

## Related patterns

- **Pattern 5 (vague attributions):** hedging often hides behind attribution.
- **Pattern 24 (knowledge-cutoff disclaimers):** another hedge category.
- **Pattern 30 (filler phrases):** the two stack frequently.
