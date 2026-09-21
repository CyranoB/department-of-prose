# Pattern 34: Uniform sentence rhythm (low burstiness)

**Sentences that barely vary in length or shape, producing a flat, even cadence with no rhythmic surprise.**

## Why LLMs do this

A language model generates each sentence by predicting the most probable continuation. Left to its own devices, that process converges on a comfortable middle: clauses of similar weight, joined in similar ways, landing at a similar length. There is no internal pressure toward variety, because variety is not what "most probable next token" optimizes for. The safe, well-formed, medium-long sentence is always available, so the model reaches for it again and again.

Human writers vary sentence length for reasons a model does not feel: to control pace, to land a point, to breathe. We write a long sentence that builds and qualifies and accumulates, and then we stop short. The short one hits harder because the long one set it up. That contrast — researchers call it "burstiness" — is a fingerprint of a mind deciding, sentence by sentence, how much room each thought needs. The model is not deciding that. It is averaging.

## Why readers notice it

Sentence-length variation is one dimension readers notice when prose feels flat or over-smoothed. A passage where every sentence runs 18 to 24 words, each a tidy subject-verb-object with one subordinate clause, can sound monotonous even when the vocabulary is clean and the argument is sharp. Genre matters: procedural and technical writing may benefit from consistency, while an essay or speech often needs more movement.

The pattern is structural rather than lexical, so a word-level score will not capture it. The words may be fine while the rhythm still feels like a metronome. That observation supports an editing decision, not an authorship conclusion.

## Examples

Before:
> The invention happened in Toronto, and the company that captured what it was worth happened somewhere else, and that gap between where the breakthrough was made and where the money landed is the whole story.

After:
> The invention happened in Toronto. The company that captured what it was worth happened somewhere else. That gap is what this whole piece is about.

Before:
> The framework is fast and well-documented, and it has a large community of contributors, and the maintainers respond quickly to issues, which makes it a reliable choice for production work.

After:
> The framework is fast and well-documented. It has a real community. The maintainers actually answer issues. For production work, that reliability is the whole game.

Notice that the human versions swing: a long sentence next to a three-word one, a fragment, a clause that runs on by design. The AI versions hold one length and one shape.

## How to self-spot

Read your draft and mark the word count of each sentence. If the numbers cluster in a narrow band — say, almost everything between 15 and 25 words — you have a burstiness problem even if nothing else is wrong.

Look for runs of three or more consecutive sentences with the same structure (subject, verb, object, trailing clause). Break one. Add a short declarative. Let a fragment stand. Combine two short ones into a long one so a later short one can punch.

The `rhythm.py` script in the `slop-sense` skill reports sentence-length coefficient of variation (CV). It marks values below about 0.40 as low variation, a heuristic threshold for finding passages worth reading aloud. Sample length and genre can move the number, so use the sentence list and the passage itself before deciding whether to edit.

## Related patterns

- **Pattern 35 (aphoristic paragraph closers):** the rhythmic counterpart at the paragraph level — same length, same shape, ending after ending.
- **Pattern 36 (reflexive formality):** another structural tell invisible to word-level scorers.
- **Pattern 14 (anaphora abuse):** the opposite failure — repetition so identical it draws attention — but both come from the model averaging instead of deciding.
