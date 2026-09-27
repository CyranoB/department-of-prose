# Pattern 17: Em dash overuse

**Repeated em dashes can flatten punctuation choices and give prose a mannered, stop-start rhythm.**

## Why LLMs do this

Em dashes are the most flexible punctuation in English. They can interrupt, emphasize, set off parentheticals, replace colons, replace semicolons, introduce lists, and end sentences with a flourish. Because they work everywhere, a model with weak commitments to any one structure defaults to the dash. It is a punctuation choice that almost never trips a syntax check.

Training data also rewards the habit. The corpora LLMs train on contain polished modern prose, including magazine articles, blog posts, and edited fiction, where em dashes are common. A model can reproduce that punctuation choice without considering whether its frequency fits the current passage.

Generation interfaces also emit an em dash as easily as a comma or period, while some typing environments make the character less convenient. That difference can reinforce the model's habit, but it says nothing conclusive about the source of any particular dash.

## Why readers notice it

Frequency and effect matter more than any single usage. One em dash may pass unnoticed. Several in a short paragraph can make every sentence pause the same way. A dash-heavy house style, quoted material, or fiction may support a higher density than technical or conversational prose.

Readers may feel the effect before they can articulate it. Repeated mid-sentence breaks, asides, and hedges can make the rhythm feel over-managed. The useful question is whether those pauses support the intended voice or keep interrupting it.

The dash is also semantically flexible. It can stand in for so many other marks that an over-dashed passage may lose precision. A writer can choose between a comma, a colon, a period, and parentheses based on what the sentence is doing. Repeated dashes flatten those choices into one mark.

## Examples

Before (the same pause in three nearby sentences):
> The draft stalled—again. The meeting ran long—again. The decision slipped—again.

After (the facts remain, but the pauses vary):
> The draft stalled again. The meeting ran long, and the decision slipped too.

A single dash can also carry a useful hesitation:
> The handle moved—barely. I tried it once more.

That last passage needs no punctuation edit. The question is what the repeated marks do to the passage, not whether a dash appears at all.

## How to self-spot

Use the rhythm checker’s cadence candidate as a prompt to read the passage, not an automatic edit. It requires three dashes within 150 words of one paragraph and at least 40% of nearby pause marks. Count em dashes per 100 words in your draft, then inspect how they function. A cluster may make the passage feel mannered or interrupt its pace, while a single dash or a dash-heavy house style may be entirely appropriate. A quick search in your editor will count them in seconds.

When you have one, ask what it is doing. If it is interrupting a sentence, try a comma pair or parentheses. If it is introducing a clause, try a colon or a period. If it is at the end for emphasis, just end the sentence.

If several nearby sentences reach for the dash, pause and ask which punctuation best expresses each relationship. Keep the dashes that earn their interruption and restructure the rest. A similar semicolon cadence merits the same review; quoted punctuation stays intact.

## Related patterns

- **Pattern 9 (copula avoidance):** often paired. "Gallery 825 — the exhibition space — features..." stacks both tells.
- **Pattern 10 (negative parallelisms):** the "not just X, but Y" structure almost always arrives dashed.
- **Pattern 19 (inline-header lists):** the bullet "**Label:** description" sometimes appears as "**Label** — description" instead. Same problem, different mark.
