# Pattern 30: Filler phrases

**Multi-word constructions that say nothing one word would say.**

## Why LLMs do this

The training data contains a lot of business writing, legal writing, and academic prose, all of which use heavy multi-word constructions. "In order to," "due to the fact that," "at this point in time," "it is important to note that." Each is grammatically fine; each is also longer than the single word that would do the job.

The model picks the heavy version when generating because the heavy version was more common in formal training data. It does not have a strong incentive to compress, so it does not.

There is also a length-pressure incentive. A request for a paragraph response gets a fuller-feeling answer if it has 200 words of filler than if it has 100 words of substance. The model has been trained to fill space.

## Why readers notice it

The filler is recognizable in aggregate. A sentence with one "in order to" is unremarkable. A paragraph with three of them is bloated. Several pages of writing that consistently uses the long forms over the short reads as bureaucratic in a way that signals "no editor touched this."

The filler also crowds out specifics. "It is important to note that the budget was exceeded" is the same claim as "the budget was exceeded," but the first version wastes nine words that could have been a number, a date, or a cause.

## Examples

After:
> To run the tests, use this command.

Before:
> In order to run the tests, please use the following command.

After:
> The project missed its deadline because the API broke.

Before:
> The project missed its deadline due to the fact that the API broke.

After:
> The budget was exceeded.

Before:
> It is important to note that the budget was exceeded at this point in time.

Notice that the edited versions are 30-50% shorter and lose nothing. The before versions inflate the same content with grammatical scaffolding.

## How to self-spot

Keep a substitution list. The common ones:

- "in order to" becomes "to"
- "due to the fact that" becomes "because"
- "at this point in time" becomes "now"
- "in the event that" becomes "if"
- "it is important to note that" becomes deleted
- "it should be mentioned that" becomes deleted
- "with regards to" becomes "about"
- "in spite of the fact that" becomes "although"
- "for the purpose of" becomes "for" or "to"
- "in the process of" becomes "while" or deleted

Grep your draft for each. Almost every hit shortens.

## Related patterns

- **Pattern 31 (excessive hedging):** the filler often pairs with a hedge.
- **Pattern 8 (AI vocabulary):** both inflate word count.
