# Pattern 12: Synonym cycling

**Rotating synonyms to avoid repeating a word: "protagonist... main character... central figure... hero."**

## Why LLMs do this

Many style guides (especially high-school and college writing guides) tell writers to avoid repetition. Training data includes a lot of writing that follows this advice, and RLHF evaluators sometimes flag word repetition as a defect. The model learned to swap in synonyms aggressively whenever the same noun would appear twice in close proximity.

The problem is that the rule is bad. "Elegant variation," as Fowler called it, was a Victorian instinct that even Victorian editors warned against. Modern good writing repeats the clearest term, because repetition is invisible and the synonym dance is not.

## Why readers notice it

The synonyms get progressively worse as the cycle continues. The first term is the right one. The second is acceptable. The third is a reach. The fourth is comically off. "Protagonist... main character... central figure... hero... primary actor" sounds like a thesaurus exploding.

The reader notices the dance even when they cannot name the pattern. The prose appears to strain against repeating the clearest word, forcing the reader to track whether each new synonym names the same thing. Repeating "the protagonist" may be clearer.

The pattern is especially visible in articles about a single subject, such as a person, company, or place, where the noun must recur. Too many substitutes turn the paragraph into a guided tour through every available synonym.

## Examples

After:
> Tesfaye is a coffee farmer in southern Ethiopia. Tesfaye took over the cooperative in 2019 after his uncle retired. Tesfaye says the work has gotten harder as the climate shifts.

Before:
> Tesfaye is a coffee farmer in southern Ethiopia. The agriculturalist took over the cooperative in 2019 after his uncle retired. The grower says the work has gotten harder as the climate shifts.

After:
> The bridge is in Pittsburgh. The bridge was built in 1928 and renovated in 2003. The bridge carries about 12,000 cars a day.

Before:
> The bridge is in Pittsburgh. The structure was built in 1928 and renovated in 2003. The crossing carries about 12,000 cars a day.

Notice that the edited versions repeat the clearest word. The reader reads "Tesfaye" or "bridge" three times and does not notice. The before versions force the reader to track what "the agriculturalist" or "the crossing" refers to.

## How to self-spot

When you find yourself reaching for a synonym, ask why. If you have just used a noun in the previous sentence, the reflex is to vary. Resist it. Repetition of a clear noun is invisible. The synonym is visible.

A useful test: replace all the synonyms in a paragraph with the original noun. If the paragraph reads more clearly, the synonyms were the problem.

Pronouns ("he," "she," "it") are different. They are the natural alternative to a name and they do not draw attention. The issue is full-noun synonyms used as if pronouns were forbidden.

## Related patterns

- **Pattern 8 (AI vocabulary):** synonym cycling often reaches for AI-vocabulary alternatives ("the framework" then "the system" then "the infrastructure" then "the architecture").
- **Pattern 9 (copula avoidance):** the verb-side equivalent of the same instinct.
