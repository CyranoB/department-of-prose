# Pattern 27: "Think of it as..."

**Patronizing analogies that assume readers need metaphors. "Think of it like a highway for data." "Imagine it as a library."**

## Why LLMs do this

The construction is heavily represented in popular-science writing, business explainers, and educational content. All are genres where simplifying for a lay audience is the goal. The model learned that a "think of it as" analogy is a marker of accessible writing.

The problem is that the model deploys the construction by default whenever introducing a concept, regardless of whether the concept needs simplifying. The result is patronizing analogies for concepts the reader could grasp directly.

The analogies themselves are also often worse than the actual thing. A highway is not a useful model of data flow. A library is not a useful model of a vector database. The analogy obscures more than it reveals.

## Why readers notice it

The phrasing is recognizable: "Think of it like", "Imagine it as", "It's basically", "Picture it as", "It's a bit like". An analogy can help when it maps the difficult parts accurately. Repeated invitations to imagine can delay a direct explanation or introduce comparisons that do not hold.

The pattern also tends to over-simplify. The analogy gives the reader a vague impression of the concept instead of a precise understanding. Readers who actually wanted to learn the concept feel short-changed; readers who did not feel patronized.

Real analogies are powerful when the analogy genuinely illuminates the concept and the writer trusts the reader to extend it. AI analogies are weak because they substitute for explanation rather than illuminating it.

## Examples

After:
> Embeddings are arrays of numbers that represent the meaning of a piece of text. Words and sentences with similar meanings produce similar arrays.

Before:
> Think of embeddings like a fingerprint for meaning. Each piece of text gets its own unique numerical signature, and similar meanings produce similar fingerprints.

After:
> A cache is a fast, small storage layer that holds copies of data the system has fetched before.

Before:
> Think of a cache like the desk in your office. You keep the things you use most often within arm's reach so you do not have to walk to the file cabinet every time.

Notice that the edited versions describe the actual thing. The before versions reach for an analogy that does not actually help.

## How to self-spot

Search for the trigger phrases: "Think of it like," "Think of it as," "Imagine it as," "Imagine a," "Picture it as," "It's basically a," "It's a bit like."

For each hit, ask: "could I just describe the thing directly?" If yes, do that. The analogy is almost certainly less precise than the direct explanation.

If the analogy is genuinely powerful and you have crafted it deliberately, keep it. Most of the time, however, it is a reflex you can replace with a sentence of plain description.

## Related patterns

- **Pattern 28 ("Imagine a world where..."):** the futurism cousin.
- **Pattern 25 (sycophantic tone):** both can read as condescension toward the reader.
