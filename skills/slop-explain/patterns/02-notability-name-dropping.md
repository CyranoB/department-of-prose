# Pattern 2: Notability name-dropping

**Listing media outlets, awards, or credentials without context, as if the names themselves constitute information.**

## Why LLMs do this

The training data is full of Wikipedia biographies and PR-style press releases. Both genres establish notability by listing credentials. Wikipedia does this because notability is a sourcing requirement; PR does it because credentials are a sales pitch. LLMs absorb both as templates for "writing about a person or institution" and produce credential lists whether or not the surrounding context calls for them.

There is also a defensive incentive. Listing real outlets is verifiably true. Saying anything specific about what those outlets actually wrote is harder to verify and easier to get wrong. The model picks the safer move.

## Why readers notice it

Names without context are decorations, not information. A useful mention explains what an interview was about, when it happened, or why it matters. Without that follow-through, the outlet name merely borrows prestige.

The reader notices the gap. A list of outlets like "her work has appeared in NYT, BBC, FT, and The Hindu" tells you nothing about her work. It tells you she has had work appear places. The reader can already assume that, since that is why you are writing about her.

The pattern is especially common in introductory paragraphs and bios, where the LLM mistakes credential-stacking for establishing the subject's importance.

## Examples

After:
> In a 2024 New York Times interview, she argued that climate adaptation policy has been dangerously underfunded in the Global South.

Before:
> Her work has been cited in the New York Times, BBC, Financial Times, and The Hindu, establishing her as a leading voice in climate policy discourse.

After:
> The institute's 2023 study on rural broadband was covered by Reuters and Bloomberg and is now the basis for two pending Senate bills.

Before:
> The institute has been featured in numerous prominent outlets, including Reuters, Bloomberg, the Wall Street Journal, and the Financial Times.

Notice that the edited versions name the outlet because something happened there. The before versions name outlets because naming outlets is what you do in this kind of paragraph.

## How to self-spot

Every time you list a publication, organization, or credential in your draft, ask: "what is this name doing here?" If the answer is "establishing notability," cut it and write a specific claim instead.

A rough test: can the reader retell what they just read about the subject without using the listed names? If the names disappear and the sentence loses no information, the names were not doing work.

Allow lists when they ARE the information ("the company has acquired five startups in the last year: A, B, C, D, E"). Cut them when they are stand-ins for information.

## Related patterns

- **Pattern 1 (significance inflation):** similar move, different mechanism. Inflation asserts importance via adjectives. Name-dropping asserts it via lists.
- **Pattern 5 (vague attributions):** the opposite failure mode. Both refuse to attach a specific claim to a specific source.
