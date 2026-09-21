# Pattern 13: False ranges

**"From X to Y" where X and Y are not on a meaningful scale, used to imply comprehensive coverage that does not actually exist.**

## Why LLMs do this

"From X to Y" is a real construction for describing a span: from January to March, from Tokyo to Osaka, from beginner to expert. The endpoints define a continuum and the construction promises coverage between them.

LLMs learned the form but apply it to non-continuums. "From the Big Bang to dark matter" treats two unrelated topics as if they were endpoints of a scale. The form *sounds* comprehensive because it borrows the rhythm of a real span. The content is just two items that happen to belong to the same general area.

The pattern serves the model's coverage instinct. When asked what something covers, the model wants to claim breadth. The from-to construction lets it claim breadth without listing everything in between, because there is no "in between" to list.

## Why readers notice it

The reader half-tries to imagine the continuum and fails. "The course covers everything from neural networks to ethics" prompts the question "what is between neural networks and ethics on what scale?" The answer is nothing. They are two topics in the same field, not endpoints of a range.

The construction also tends to use very far-apart items to imply dramatic span. "From quantum mechanics to French poetry." The further apart the items, the more dramatic the claim of coverage, and the less the construction makes literal sense.

Real ranges work: "the book covers the period from 1914 to 1945" is fine because the years define a continuum. The pattern only flags when the endpoints are not on any continuum at all.

## Examples

After:
> The conference covers neural networks, robotics, ethics, and policy.

Before:
> The conference covers everything from neural networks to ethics.

After:
> The team has worked on payment systems, customer-facing dashboards, and internal tooling.

Before:
> The team has worked on everything from payment systems to internal tooling.

After:
> The festival features rock, classical, and traditional Ethiopian music.

Before:
> The festival features everything from rock to traditional Ethiopian music.

Notice that the edited versions list the actual items. The before versions imply that the listed endpoints are just samples of an unstated continuum, when they are actually the whole set.

## How to self-spot

Search for "from X to Y" and "everything from X to Y." For each hit, ask: "what is the scale that X and Y are endpoints of?" If you cannot name the scale, the range is false.

The fix is usually to just list the items: "X, Y, and Z." This is shorter, more honest, and does not promise breadth that is not there.

The construction is legitimate when X and Y really do define a span: time periods, geographic distances, difficulty levels, sizes. Use it there. Avoid it for grab-bag claims of comprehensiveness.

## Related patterns

- **Pattern 1 (significance inflation):** both inflate the apparent scope of the subject.
- **Pattern 11 (rule of three):** false ranges sometimes pair with triplets to multiply the inflation.
