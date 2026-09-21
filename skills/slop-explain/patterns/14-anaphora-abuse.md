# Pattern 14: Anaphora abuse

**Repeating identical sentence openings in quick succession for false emphasis.**

## Why LLMs do this

Anaphora is a real rhetorical device. Used sparingly, it carries weight: "We shall fight on the beaches. We shall fight on the landing grounds. We shall fight in the fields." The repetition does work because the items are non-trivially distinct and the cumulative effect is the point.

The training data is full of speeches and persuasive essays that use this device. The model learned it as "a way to make a paragraph feel emphatic." But the model deploys it whenever it wants emphasis, not just when the underlying items support the structure. The result is anaphora applied to mundane lists where the rhetorical heat is unearned.

The form also extends sentences in a predictable way. "X happens" is short. "X happens. X happens. X happens" is longer and feels more substantial. For a model padding toward an appropriate word count, the device is a reliable filler.

## Why readers notice it

The repetition draws attention to itself, and once you notice it the magic dies. "They assume users will pay. They assume developers will build. They assume the market will grow" reads as theatrical when the underlying observation could have been a single sentence: "They assume too much."

The pattern also clusters with rule of three (pattern 11). Anaphora often comes in triplets because three repetitions establish an obvious cadence. Used once, that cadence can land a point; repeated across sections, it becomes predictable.

Real anaphora is rare and earns its weight by lining up genuinely distinct claims. AI anaphora lines up near-synonyms or trivially varied versions of the same claim.

## Examples

After:
> They assume too much: that users will pay, that developers will build, and that the market will grow.

Before:
> They assume users will pay. They assume developers will build. They assume the market will grow.

After:
> The framework is fast, well-documented, and has a real community behind it.

Before:
> The framework is fast. The framework is well-documented. The framework has a real community.

Notice that the edited versions either consolidate the repeated structure into a single sentence or vary the openings. The before versions hammer the same opening for theatrical effect that the content does not earn.

## How to self-spot

Scan your paragraphs for two or three consecutive sentences starting with the same word or phrase. For each cluster, ask: "is this repetition doing rhetorical work, or am I just inflating?"

The test: would a serious writer choose this repetition deliberately to make a point? If yes, keep it. If you cannot articulate why, vary the structure or combine the sentences.

Anaphora used once or twice in a long piece can be powerful. Anaphora used reflexively in every paragraph is a tic.

## Related patterns

- **Pattern 11 (rule of three):** anaphora is almost always a triplet.
- **Pattern 15 ("Not X. Not Y. Just Z."):** the negative form of the same instinct.
- **Pattern 16 (rhetorical Q&A):** another false-emphasis device that pairs with this one.
