# Pattern 16: Rhetorical Q&A

**Self-posed questions answered immediately, asking questions nobody asked for dramatic effect.**

## Why LLMs do this

The technique appears constantly in op-eds, motivational writing, and explainer content (three genres heavily represented in training data). The form gives a writer a way to introduce a claim with a beat of suspense: pose the question, deliver the answer.

For a model trying to add weight to a sentence, the question-answer split is a free expansion. "It was devastating" becomes "The result? Devastating." The expansion adds zero content but doubles the word count and adds a rhetorical flourish.

The model also defaults to it when transitioning between ideas. Rather than build a smooth bridge, it can pose a question that the next sentence answers. The question acts as a hinge, and the model does not have to think about how the ideas actually connect.

## Why readers notice it

The questions are almost always ones the reader was not asking. "The result? Devastating." The reader was not wondering about the result; the writer is performing curiosity on their behalf. The technique is so common in AI text that any one-word answer to a self-posed question reads as filler.

The form is also visually distinct. The fragment-plus-question-mark followed by a single-word answer creates a recognizable rhythm. When this rhythm repeats in a piece, every instance after the first becomes obviously mechanical.

It pairs with the "Here's the kicker" family (pattern 26) to produce paragraphs that are almost entirely transitions and reveals, with very little actual content in between.

## Examples

After:
> The result was devastating.

Before:
> The result? Devastating.

After:
> The cost was hidden in the operational budget for years.

Before:
> Where did the cost go? Hidden in the operational budget for years.

After:
> The team underestimated the migration by six months.

Before:
> What went wrong? The team underestimated the migration by six months.

Notice that the human versions deliver the information directly. The AI versions stage a discovery the reader was not part of.

## How to self-spot

Search for question marks followed by a sentence fragment or short clause. For each, ask: "was the reader wondering this?" If not, fold the question and answer into a single declarative sentence.

The construction is legitimate when the question is one the reader genuinely is asking and you are answering it for them. Most of the time, however, it is the writer asking themselves a question to set up an answer they already knew.

A useful test: read the surrounding paragraph aloud. If the question feels like a tap on the shoulder rather than a genuine pause, cut it.

## Related patterns

- **Pattern 26 ("Here's the kicker"):** another false-suspense transition.
- **Pattern 14 (anaphora abuse):** rhetorical questions often repeat in clusters.
- **Pattern 15 ("Not X. Not Y. Just Z."):** another theatrical reveal pattern.
