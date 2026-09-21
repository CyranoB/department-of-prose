# Pattern 18: Boldface overuse

**Mechanical emphasis on terms or phrases that do not actually need emphasis.**

## Why LLMs do this

Markdown is well-represented in training data, especially in technical documentation, blog posts, and "how-to" content. In those genres, key terms are often bolded so readers scanning the page can find them. The model learned that bold means "important" and applies it to anything that seems definition-like or topic-introducing.

The model has no visual feedback loop while generating markup, so it may keep adding bold wherever a term seems important. In the rendered passage, repeated emphasis creates visual noise and makes the hierarchy harder to see.

## Why readers notice it

Bold loses its meaning when it is everywhere. If every paragraph has three bolded phrases, none of them feel important. The reader's eye has nothing to anchor to. The page looks like a textbook study guide rather than prose.

The selection may also feel arbitrary: nearly every concept noun is bold, including terms the reader could find without help. Effective emphasis is sparse and tied to a clear reading purpose.

Bold is most jarring in narrative or argumentative prose where it has no functional role. A blog post about a personal experience does not need bolded **fear** and **hope** and **discovery**. The bolding suggests the writer is afraid the reader will miss the words.

## Examples

After:
> The team adopted a new framework last quarter and shipped two features in six weeks.

Before:
> The team adopted a **new framework** last quarter and shipped **two features** in just **six weeks**.

After:
> What surprised me was how much resistance came from middle management.

Before:
> What surprised me was the **resistance** that came from **middle management**.

Notice that the edited versions trust the reader to find the important words on their own. The before versions decorate them, which only flattens the emphasis.

## How to self-spot

Count bold spans per paragraph in your draft. More than one is usually too many. None is often correct.

For each bolded phrase, ask: "is this a defined term, a heading, or a UI label?" If yes, bold is appropriate. If no, if it is just a phrase that "feels important," remove the bold and let the sentence carry the weight.

A useful test: render the draft without any bold and see if the meaning is clear. Almost always it is. The bold was decoration.

## Related patterns

- **Pattern 19 (inline-header lists):** boldface is the load-bearing element in those bullets.
- **Pattern 21 (emojis in structure):** same instinct (visual decoration) in a different medium.
