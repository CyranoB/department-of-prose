# Pattern 5: Vague attributions

**Attributing opinions or claims to unnamed authorities: "experts believe," "industry reports suggest," "some critics argue."**

## Why LLMs do this

The model often does not know who actually said the thing. It learned the *shape* of a claim like "experts believe X" from countless news articles, but the underlying citations are not present in its weights as discrete facts. So when it needs to support a claim, it reaches for the form of attribution without the substance.

There is also a hedging incentive. A specific attribution ("Smith argued in his 2023 paper that Y") is checkable. A vague attribution ("some scholars argue that Y") is not. If the underlying claim is fuzzy or the model is uncertain, vague attribution is the safer move.

Finally, news writing genuinely uses this construction sometimes for sourced reporting that aggregates multiple background sources. The model learned the form there and over-applies it everywhere.

## Why readers notice it

The vagueness flags itself. "Experts believe" raises the question "which experts?" and the answer never arrives. The reader is left with an unsupported claim wearing the costume of a sourced one.

The construction also clusters. Real journalism uses vague attribution sparingly and pairs it with specific attribution elsewhere in the piece. LLM text uses it as a default and stacks it: "experts believe... industry reports suggest... some critics argue... observers note..." Every paragraph has its own anonymous chorus.

Readers who care about evidence stop trusting the text. Readers who do not still sense that something is off, because the same phrasing recurs every time anyone "believes" or "suggests" anything.

## Examples

After:
> In a March 2024 paper, Stanford economist Maria Lee found that minimum-wage increases above $18 reduced full-time hiring in three out of five sectors studied.

Before:
> Some economists believe that high minimum wages may negatively impact hiring in certain sectors.

After:
> A 2023 Gartner report estimated that 35% of enterprise AI projects would be abandoned before reaching production.

Before:
> Industry reports suggest that a significant portion of enterprise AI projects are at risk of failure.

Notice that the human versions tell you who, when, and what specifically. The AI versions tell you that someone, somewhere, has an opinion related to the topic.

## How to self-spot

Search for the construction phrases: "experts believe," "experts say," "industry reports suggest," "studies show," "research indicates," "some argue," "some critics," "observers note," "many feel," "it is widely believed."

For each hit, ask: "who? when? where?" If you cannot answer, do one of three things:
1. Find the actual source and name it.
2. State the claim as your own opinion, with stakes.
3. Delete the sentence.

The third option is often correct. Many vague attributions exist only to give a paragraph more weight. Without them the paragraph either stands on its other claims or collapses, and either outcome is better than the hedged version.

## Related patterns

- **Pattern 2 (notability name-dropping):** the opposite failure. Both refuse to do the specific work of source-and-claim.
- **Pattern 31 (excessive hedging):** vague attribution is a hedge dressed up as a citation.
