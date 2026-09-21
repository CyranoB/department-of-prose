# Pattern 17: Em dash overuse

**LLMs use em dashes (— or --) at densities no human writer matches.**

## Why LLMs do this

Em dashes are the most flexible punctuation in English. They can interrupt, emphasize, set off parentheticals, replace colons, replace semicolons, introduce lists, and end sentences with a flourish. Because they work everywhere, a model with weak commitments to any one structure defaults to the dash. It is a punctuation choice that almost never trips a syntax check.

Training data also rewards the habit. The corpora LLMs train on are full of polished modern prose: New Yorker articles, blog posts, well-edited fiction. All of these use em dashes more than the average human writer does. The model averages those frequencies and produces more.

Finally, there is no friction. A human typing on a standard keyboard has to reach for Option+Shift+Hyphen on macOS, or copy-paste, or rely on autocorrect. Most people use hyphens or comma-pause-comma instead, even when an em dash would technically be correct. LLMs have no fingers and no friction. Every dash is free.

## Why readers notice it

The density is the tell, not any single usage. One em dash in an essay is fine. Three in a paragraph is suspicious. Six in 312 words is a flashing neon sign.

Readers feel it before they can articulate it. The text has a rhythm of mid-sentence breaks, asides, and hedges that does not match how people actually write. Even readers who could not name the pattern will say the writing feels "polished but artificial" or "off somehow." They are counting dashes subliminally.

The dash is also semantically lossy. It can stand in for so many other marks that an over-dashed text loses precision. A human writer chooses between a comma, a colon, a period, and parentheses based on what the sentence is doing. An over-dashed text has flattened all those choices into one mark.

## Examples

After:
> The tools are useful, even essential, for modern teams.

Before:
> The tools are useful — even essential — for modern teams.

After:
> It works most of the time.

Before:
> It works — most of the time.

After:
> She arrived late. The meeting had already started.

Before:
> She arrived late — the meeting had already started.

Notice that the human versions use different punctuation each time: commas, a period, nothing at all. The LLM version reaches for the same mark every time.

## How to self-spot

Count em dashes per 100 words in your draft, then inspect how they function. A cluster may make the passage feel mannered or interrupt its pace, while a single dash or a dash-heavy house style may be entirely appropriate. A quick search in your editor will count them in seconds.

When you have one, ask what it is doing. If it is interrupting a sentence, try a comma pair or parentheses. If it is introducing a clause, try a colon or a period. If it is at the end for emphasis, just end the sentence.

If you find yourself reaching for the dash while writing, stop. That is the LLM-trained voice in your head. Restructure the sentence to work without it.

## Related patterns

- **Pattern 9 (copula avoidance):** often paired. "Gallery 825 — the exhibition space — features..." stacks both tells.
- **Pattern 10 (negative parallelisms):** the "not just X, but Y" structure almost always arrives dashed.
- **Pattern 19 (inline-header lists):** the bullet "**Label:** description" sometimes appears as "**Label** — description" instead. Same problem, different mark.
