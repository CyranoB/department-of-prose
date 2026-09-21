# Pattern 20: Title Case headings

**Capitalizing All Main Words In Headings, which is uncommon in modern web prose.**

## Why LLMs do this

Title Case is the older convention. It survives in newspaper headlines, academic paper titles, and many books, so the training data contains a lot of it. RLHF and instruction tuning reinforce it as the polite default. Many style guides for formal writing still prefer Title Case.

But web writing has largely moved to sentence case for headings. Most modern blogs, technical documentation, and online publications use sentence case because it reads more naturally and matches how the rest of the text is capitalized. The model is overweighted toward the older convention and applies Title Case even when sentence case would fit the surrounding prose better.

## Why readers notice it

Sentence case is dominant on the modern web. When a piece uses Title Case headings, the reader notices, especially in casual or conversational writing. The headings read as formal or old-fashioned in a way that does not match the body text.

The tell is not Title Case itself. Many publications still use it well. The tell is Title Case in a context that otherwise reads as informal, blog-like, or technical. The mismatch suggests the model defaulted to its training convention rather than matching the actual register.

## Examples

After:
> ## How the migration broke production

Before:
> ## How The Migration Broke Production

After:
> ### A short note on naming things

Before:
> ### A Short Note On Naming Things

Notice that sentence case is unobtrusive and matches the body text. Title Case stands out in a way the heading content does not earn.

## How to self-spot

Look at the headings in any draft. If they are Title Case ("How To Build A Robot") and the body text is informal, switch to sentence case ("How to build a robot"). The exception: if the publication explicitly uses Title Case (some still do), match the house style.

A useful test: imagine the heading as the title of a tweet, blog post, or doc page in your normal style. Would you capitalize it that way? If not, the heading is in the wrong register.

## Related patterns

- **Pattern 18 (boldface overuse):** both decorate text in ways that do not match modern web conventions.
- **Pattern 21 (emojis in structure):** same instinct to dress up headings.
