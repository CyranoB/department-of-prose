# Pattern 7: Invented concept labels

**Fabricated compound terms that sound analytical but are ungrounded: "the supervision paradox," "the acceleration trap," "the alignment creep."**

## Why LLMs do this

The training data is full of essays and analyses that name new phenomena: "the great resignation," "the productivity paradox," "moral hazard," "the bullwhip effect." These named concepts are valuable when they refer to something real and well-defined. LLMs absorbed the pattern (specific noun + abstract noun = analytical insight) without absorbing the part where the named thing is real.

So when an LLM is reasoning through a topic and wants to mark a tension or pattern as important, it generates a new compound: domain word + paradox / trap / creep / loop / problem. The compound has the cadence of a known concept. It is not one.

There is also a self-citation move: the passage coins a term mid-paragraph and then refers to it as if it were established. A new label can be useful when it is defined, defended, and reused to clarify an argument. Without that work, "what I call the supervision paradox" adds confidence without analysis.

## Why readers notice it

The reader cannot find the term anywhere else. Search "supervision paradox" in scholarly databases and you find either nothing or a different unrelated concept. The term has no community, no literature, no definition beyond what the model just made up.

The construction is also recognizable. The compounds tend to use the same abstract nouns: paradox, trap, creep, problem, dilemma, loop, illusion, fallacy. Once you see the move, you cannot unsee it. Any phrase of the form "the X paradox" or "what I call the Y trap" in an AI-generated essay deserves immediate skepticism.

## Examples

After:
> The more time managers spend reviewing AI-generated code, the more skeptical they become of their team's ability to write code independently. This creates a tension: oversight that was meant to maintain quality starts to erode the autonomy that produces quality.

Before:
> This creates what I call the "delegation paradox": the very act of supervising AI work undermines the human capability the supervision was meant to protect.

After:
> Companies that adopted AI tools faster reported higher short-term productivity but lower long-term retention. The cause appears to be that early adopters relied on tooling for tasks that were also the main on-the-job training for junior staff.

Before:
> This is the acceleration trap in action: speed today eats capability tomorrow.

Notice that the edited versions describe the dynamic in concrete terms and let the reader draw the framing conclusion. The before versions skip the description and ship a brand name.

## How to self-spot

When you write the phrase "what I call the X paradox" or "the X trap" or "the X loop," stop. Either you are introducing an established term (in which case cite it) or you are inventing one (in which case the reader will not recognize it and you have not earned the naming move).

A useful rewrite: describe the tension in two or three sentences and let the reader name it themselves. Names that catch on do so because the underlying observation was clear. Names that do not catch on are dead weight regardless of how clever they sound.

If you genuinely want to introduce a new term, do it explicitly: "I want to give this a name because I will refer back to it. I will call it X." Then justify the name. Most of the time you will discover you did not need it.

## Related patterns

- **Pattern 1 (significance inflation):** both inflate without earning.
- **Pattern 32 ("the truth is simple"):** both assert as a shortcut to argument.
