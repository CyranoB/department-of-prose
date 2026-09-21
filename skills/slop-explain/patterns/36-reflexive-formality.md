# Pattern 36: Reflexive formality

**Never contracting — defaulting to "do not", "cannot", "it is", "you have" everywhere, even in casual or first-person writing where a human would say "don't", "can't", "it's".**

## Why LLMs do this

Expanded forms are the safe register. "Do not" is correct in every context; "don't" is correct in most but carries a casualness the model treats as risk. Instruction-tuned assistants are nudged toward a polished, professional default, and the uncontracted form is the lowest-common-denominator choice that never reads as too flip. So the model reaches for it by reflex, including in places where a human writer would never be that stiff.

The result is consistency where humans are inconsistent. A real writer contracts when the sentence wants to move quickly and expands when they want weight or emphasis — "I don't think that's right" versus "I do not, under any circumstances, agree." The mix is unconscious and constant. The model does not mix; it picks the formal form and stays there.

## Why readers notice it

The absence of contractions can make casual or first-person prose sound overly formal, robotic, or impersonal. In a personal essay, opinion column, or blog post, a first-person argument that never says "I'm" or "don't" may feel out of register. In legal, academic, ceremonial, or translated prose, the same choice may be appropriate. The mismatch with the intended voice is the finding; it is not proof of how the text was produced.

It is also easy to over-correct in the wrong direction. The fix is not to contract everything — that produces its own uniform, flattened tone. The fix is variation, which is exactly what the model fails to produce.

## Examples

Before:
> It is not a question of capacity. You cannot commercialize what you do not own, and that is the whole problem. We are not going to solve this by pretending it is simple.

After:
> It isn't a question of capacity. You can't commercialize what you don't own, and that's the whole problem. We're not going to solve this by pretending it's simple.

Before (over-corrected — now uniformly casual):
> It's not capacity. You can't own it. That's the problem. We won't fix it by pretending it's easy.

After (varied — contract by default, expand for emphasis):
> It isn't capacity. You can't commercialize what you don't own. And we are not — not under any reading of the budget — going to fix that by pretending it is simple.

The last version contracts where the prose moves and expands where it wants to land a blow. That mix is the human signal.

## How to self-spot

Search your draft for "do not", "does not", "cannot", "it is", "they are", "you are", "I am". Count them against the contracted forms. If the contracted forms are near zero in casual or first-person writing, you are being reflexively formal.

Read a paragraph aloud. If it sounds like a press release or a legal notice when it is supposed to sound like a person talking, contractions are usually the missing ingredient. Then resist contracting *everything* — leave the expanded form where you genuinely want emphasis.

The `rhythm.py` script reports a contraction ratio: a value near 0 with many expanded forms present is the flag.

## Related patterns

- **Pattern 34 (uniform sentence rhythm):** another structural/register tell that word-level scorers miss.
- **Pattern 35 (aphoristic paragraph closers):** like this one, it comes from the model defaulting to a "polished" register instead of a human one.
- **Pattern 25 (sycophantic tone):** part of the same instruction-tuned politeness that produces stiff, safe prose.
