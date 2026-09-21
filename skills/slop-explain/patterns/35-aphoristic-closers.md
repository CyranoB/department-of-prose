# Pattern 35: Aphoristic paragraph closers

**Ending nearly every paragraph on a short, polished, balanced kicker — a quotable epigram that resolves the point with a satisfying click.**

## Why LLMs do this

The training data rewards closure. Essays, op-eds, and blog posts in the corpus tend to end paragraphs on a strong line, because editors taught generations of writers to do exactly that. The model learned the move as "this is how a paragraph is supposed to feel finished," and it applies the move everywhere, because every paragraph wants to feel finished.

The aphorism is also a structurally convenient landing. After a few sentences of setup, a short balanced clause — "and the difference is the entire argument", "that gap is the whole story" — provides a clean exit without requiring the model to commit to a messy, specific, or unresolved thought. It is the prose equivalent of a sitcom button: the scene needs to end, so deliver a line that sounds like an ending.

## Why readers notice it

A great closing line is a gift. A polished closing line in *every paragraph* can become predictable. Paragraphs can hand directly to the next one, end on a plain fact, or stop with some tension unresolved. When every paragraph instead snaps shut on a balanced epigram, the reader may start to feel handled. The issue is the repeated effect across the passage, not the authorship of any one line.

Crucially, the tell is the *relentlessness*, not any single kicker. Each line, read alone, looks like good writing. Read as a set, they feel interchangeable: the same "X is Y, and that is the point" shape, over and over. The cumulative effect is a piece that sounds like it is constantly concluding.

## Examples

Before (every paragraph lands the same way):
> ...and so the policy fails on its own terms, which is the quiet tragedy of the whole thing.
>
> ...and that, in the end, is the difference between owning and renting.
>
> ...which is exactly what the budget reveals once you look closely.

After (vary the endings; let most be ordinary):
> ...and so the policy fails on its own terms.
>
> Owning and renting are not the same, and the budget is where you see it. The line item for commercialization is thirty times smaller than the one for adoption programs. Read it and the priorities are obvious.
>
> The critics noticed within hours. Several of them had been consulted on the plan.

Notice the human version ends paragraphs on a plain sentence, a concrete number, an unresolved observation — not a polished button each time.

## How to self-spot

Read only the last sentence of each paragraph, in sequence, ignoring everything else. If they sound like a string of fortune cookies — short, balanced, each one "wise" — you are over-closing.

Count how many of your paragraphs end on a kicker. A handful in a long piece is fine and even good. If it is most of them, cut the kickers from the weaker paragraphs and let them end flat. Save the epigram for the one or two places it is actually earned.

The `rhythm.py` script flags both forms: the short punchy closer and the long sentence that resolves into a short balanced tail after the final comma.

## Related patterns

- **Pattern 34 (uniform sentence rhythm):** the same averaging instinct, applied to sentence length instead of paragraph endings.
- **Pattern 10 (negative parallelisms):** aphoristic closers very often *are* negative parallelisms ("a dividend, not sovereignty").
- **Pattern 32 ("the truth is simple"):** another way of asserting a tidy resolution the argument has not actually earned.
