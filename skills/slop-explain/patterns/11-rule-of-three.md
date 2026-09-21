# Pattern 11: Rule of three

**Forcing ideas into groups of three for rhetorical effect, even when the natural number of items is different.**

## Why LLMs do this

Three-item lists have a long history in rhetoric, from Cicero to advertising copy. They feel complete, balanced, and memorable, and model training data contains many examples. The construction works when three is the natural count. It becomes formulaic when every list is forced into that shape.

The model also has a generation-side incentive. When listing items, it has to stop somewhere. Two items can feel thin. Four can feel awkward. Three is the safest stopping point that still produces a list. So the model lands on three whether the underlying topic has three items or five or just one.

## Why readers notice it

Frequency is the finding: every list has three items, every adjective arrives in a triplet, and every conclusion offers three things to remember. Across a passage, the rhythm becomes a chant.

The forced version often shows its seams. The first two items are crisp; the third is a synonym for one of the first two, or a vaguer category that does not quite fit. "Innovation, inspiration, and industry insights" is the structure of a real triplet, but the third item was added to complete the count.

When the list could have been two items or five items, three becomes a tell. Real writing has the natural number of items. AI writing has three of everything.

## Examples

After:
> The course covers algorithms and data structures.

Before:
> The course covers algorithms, data structures, and computational thinking.

After:
> The conference brings together researchers from biology, physics, computer science, philosophy, and the arts.

Before:
> The conference brings together researchers across disciplines, fostering innovation, inspiration, and industry insights.

After:
> The cooperative grows coffee. That is the business.

Before:
> The cooperative is dedicated to growing, processing, and exporting premium coffee, embodying excellence, sustainability, and community at every step.

Notice that the edited versions use the natural count, which is sometimes two, sometimes five, sometimes one. The before versions always find three.

## How to self-spot

Search your draft for comma-and-comma constructions. For each triplet, ask: "do I have exactly three items here because there are exactly three items, or because triplets sound good?"

If the third item is a vague abstraction (innovation, inspiration, *insights*) or a synonym for the second, drop it and consider whether the actual count is two.

If you find yourself reaching for a third item to "round out" a list, do not. Two-item lists are fine. So are one-item lists, which are just sentences.

## Related patterns

- **Pattern 3 (superficial -ing analyses):** -ing tails often arrive as triplets.
- **Pattern 8 (AI vocabulary):** the third item is often the most AI-flavored: "vibrant, intricate, *enduring*."
- **Pattern 14 (anaphora abuse):** the triplet of repeated openings is the rule of three applied to sentence structure.
