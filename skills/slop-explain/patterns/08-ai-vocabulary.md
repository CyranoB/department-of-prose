# Pattern 8: AI vocabulary

**A cluster of polished, abstract words can make prose feel generic when they recur without adding precision.**

## Why LLMs do this

LLMs do not have a vocabulary in the human sense. They have probability distributions over tokens. When a model is choosing the next word and several are plausible, it tends to pick the one that scored highest during training, weighted by RLHF reward signals.

A small set of words happen to win that competition disproportionately often. "Delve" can displace "explore", "tapestry" can displace "mix", and "underscore" can displace "show" because the alternatives sound sophisticated, vivid, or analytical. Each individual choice is defensible. In aggregate, a dense cluster can make the vocabulary feel generic or selected for polish rather than precision.

Some of these words are also relics of human writing styles that the training data over-represented: academic papers, marketing copy, opinion essays. The model learned that "landscape" is the right metaphor for "the state of a field" because thousands of consulting reports said so. Now it uses the word for everything.

## Why readers notice it

The finding is not any one word. Plenty of writers use "showcase" or "vibrant." What matters is density, repetition, and the company those words keep. A cluster such as "additionally", "underscore", and "intricate tapestry" in one paragraph is worth reviewing because it can make the prose feel generic; it does not establish who wrote it.

Some of the words also have a recognizable timbre. "Delve" has become almost a meme. African English speakers have pointed out that "delve" is more common in their dialect, and that the word's sudden ubiquity in LLM output may reflect outsourced RLHF labor. Whatever the cause, the word now signals AI to most readers.

The category overlaps with promotional language (pattern 4). "Vibrant" and "intricate" can appear under either label. The difference: pattern 4 is about tone (brochure-like), pattern 8 is about vocabulary frequency (these specific words at this specific rate).

## Examples

After:
> The festival also includes street performances and food stalls. Both have been part of the event since the 1970s.

Before:
> Additionally, an enduring testament to the city's cultural tapestry, the festival showcases a vibrant array of street performances and food stalls, underscoring its commitment to fostering community.

After:
> The team built the new feature in six weeks. It shipped on time.

Before:
> The team meticulously crafted the groundbreaking new feature in just six weeks, ultimately delivering a pivotal milestone in the company's evolving landscape.

Notice that the edited versions are shorter and more specific. The before versions add words that decorate without informing.

## How to self-spot

Keep a personal block list. The highest-frequency AI tells:

- delve
- tapestry
- landscape (used abstractly, as in "the X landscape")
- pivotal
- testament
- underscore
- showcase
- foster (as a verb for things that are not children)
- intricate
- vibrant
- crucial
- meticulous
- enduring
- align with
- additionally (especially as a sentence opener)

Run a grep over your draft for these. Each hit is a candidate for replacement. The replacements are almost always shorter and more concrete.

Also notice the cumulative effect. One "underscore" is fine. Two "underscores" and a "showcase" in a single paragraph is slop.

## Related patterns

- **Pattern 4 (promotional language):** overlapping vocabulary, different angle. Both flag tone problems.
- **Pattern 9 (copula avoidance):** "serves as a testament" stacks both tells.
- **Pattern 11 (rule of three):** AI vocab loves triplets. "Vibrant, intricate, and enduring" is two patterns in one phrase.
