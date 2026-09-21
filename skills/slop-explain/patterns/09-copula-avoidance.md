# Pattern 9: Copula avoidance

**Replacing "is/are/has" with fancier constructions: "serves as," "stands as," "features," "boasts," "represents."**

## Why LLMs do this

The verb "to be" is the most common verb in English. RLHF evaluators sometimes rate prose with more varied verbs as more sophisticated, even when the variation is gratuitous. The model learned to swap out plain "is" for elevated alternatives whenever it could.

The substitutes also feel safer in some contexts. "Serves as" sounds more analytical than "is." "Represents" sounds more interpretive. "Features" sounds richer than "has." For a model trying to sound polished, these are reflex replacements.

Many of the substitute verbs are also genre-tied. "Boasts" comes from real-estate listings and tourism copy. "Stands as" comes from monument inscriptions. "Serves as" comes from institutional descriptions. The model learned each in its native register and over-applies them everywhere.

## Why readers notice it

The variants are almost always heavier and less precise than "is." "Gallery 825 serves as the exhibition space" gives you no more information than "Gallery 825 is the exhibition space," and the word "serves" suggests an active role the gallery is not actually performing.

The variants also cluster. One "serves as" may fit the sentence. A run of "serves as", "stands as", and "features" can make simple identity claims sound needlessly ceremonial.

The pattern is most visible at the *exact* moments when "is" would be clearest. Definitions, identifications, classifications: places where the writer's job is to say "this thing is this other thing." Swapping in a verb of action or representation distorts the basic identity claim.

## Examples

After:
> The library is the oldest building on campus.

Before:
> The library stands as the oldest building on campus.

After:
> The committee has seven members.

Before:
> The committee features a total of seven members.

After:
> The Mona Lisa is in the Louvre.

Before:
> The Mona Lisa resides in the Louvre, where it serves as one of the museum's most iconic holdings.

Notice that the edited versions are shorter, clearer, and lose no meaning. The before versions add verbal ceremony around an identity claim.

## How to self-spot

Search your draft for the substitutes: "serves as," "stands as," "features," "boasts," "represents," "constitutes," "embodies," "resides," "comprises," "encompasses."

For each hit, try replacing it with "is," "are," "has," or "contains." If the simpler version works, use it. If it does not work (because the verb actually carries meaning the simpler form does not), keep it. You will find that the substitute was carrying real meaning maybe 10% of the time.

Also watch for the pattern at the start of definitional sentences. "X serves as Y" almost always wants to be "X is Y."

## Related patterns

- **Pattern 4 (promotional language):** "boasts" sits at the intersection.
- **Pattern 17 (em dash overuse):** the copula-avoidant construction often pairs with em dashes around an interrupted clause.
