# Pattern 19: Inline-header lists

**Bullet points formatted as "**Label:** description," used where prose would be clearer.**

## Why LLMs do this

The format is everywhere in technical documentation, product specs, and listicles. These are high-volume training corpora. Each bullet is structured: a bolded noun-phrase label, a colon, then a sentence or two of explanation. The shape is comfortable for the model because it pattern-matches "listing related items."

The model defaults to it whenever a topic has multiple aspects, even when the aspects are not really list items. A discussion of three trade-offs becomes three labeled bullets. A description of how a process works becomes labeled steps. The format imposes a list structure on content that would read better as connected prose.

## Why readers notice it

Inline-header lists fragment ideas that belong together. Real lists work when the items are parallel and discrete: ingredients, steps, options, criteria. They fail when the items have relationships, dependencies, or narrative flow, because the bullets cannot show those relationships.

The format also tends to repeat verbs and structure. Every bullet ends up with the same shape: noun phrase, colon, two sentences of expansion. The visual rhythm becomes monotonous quickly. Readers scrolling past three pages of bullets cannot remember what any of them said.

It is especially obvious when the content is fundamentally argumentative or narrative. An essay about why a strategy failed does not want to be five labeled bullets explaining the reasons. It wants to be three paragraphs that connect the reasons to each other.

## Examples

After:
> The framework is hard to learn for three reasons. First, the documentation assumes a Python background that most JavaScript developers do not have. Second, the configuration system is undocumented and changes between minor versions. Third, the community is small and the most active threads are in a private Discord.

Before:
> The framework is hard to learn for several reasons:
>
> - **Documentation gap:** the docs assume a Python background.
> - **Unstable configuration:** the configuration system changes between minor versions.
> - **Small community:** most active discussion is in a private Discord.

Notice that the human version connects the reasons with "first / second / third" and lets each one expand into a real sentence. The AI version chunks them into labels that strip the connective tissue.

## How to self-spot

When you find yourself writing a list of inline-header bullets, ask: "could this be three sentences of prose instead?" In most cases the answer is yes, and the prose version flows better.

The format earns its place when:
- The items are genuinely parallel (e.g., a feature comparison)
- The reader will scan rather than read
- The labels are stable handles the reader can refer back to

Outside those cases, prose is almost always clearer.

## Related patterns

- **Pattern 18 (boldface overuse):** inline headers depend on bold.
- **Pattern 20 (Title Case headings):** the labels are often Title Case too.
