# Pattern 4: Promotional language

**Neutral writing replaced by tourism-brochure or marketing-copy vocabulary, even when the genre does not call for it.**

## Why LLMs do this

A large fraction of LLM training data is promotional. Hotel listings, real-estate descriptions, university brochures, corporate "About" pages, tourism websites, museum catalogs. All of these use a recognizable register: every place is "nestled," every program is "renowned," every amenity is "world-class."

The model learned that this register is the default for "writing about a place or institution." When asked to describe a town or a company, it reaches for the same vocabulary it learned from the brochure subset of its training. The result is a Wikipedia article that reads like a Booking.com listing.

There is also an RLHF effect. Human evaluators tend to rate promotional prose as "rich" or "engaging" compared to plain descriptive prose, even when the plain version is more accurate and more readable. The model adapts.

## Why readers notice it

The vocabulary is the giveaway. "Nestled," "vibrant," "breathtaking," "renowned," "boasts," "stunning," "groundbreaking," "exemplifies." A human writer might use one of these in a thousand words. LLMs cluster them.

The register mismatch is also obvious. A Wikipedia article about a small town in Ethiopia is not a sales pitch for that town, and writing it as if it were makes the article read as untrustworthy. The reader notices that the writer is selling something, and is not sure what.

Promotional language also reliably loses information. "Nestled in the breathtaking Gonder region" tells you less than "located in the Gonder region, 730 km north of Addis Ababa." Adjectives push facts off the page.

## Examples

After:
> Birka is a town in the Gonder region of Ethiopia.

Before:
> Nestled within the breathtaking landscape of the renowned Gonder region, the vibrant town of Birka boasts a rich cultural heritage.

After:
> The university's biology department was founded in 1962 and has 14 faculty.

Before:
> The renowned biology department, a vibrant hub of cutting-edge research, boasts a stunning lineage of groundbreaking faculty whose pioneering work has left an indelible mark on the field.

Notice that the human versions answer factual questions. The AI versions answer emotional questions ("how should I feel about this?") with no facts to support the suggested feeling.

## How to self-spot

Keep a block list of promotional adjectives: nestled, vibrant, breathtaking, renowned, stunning, groundbreaking, boasts, profound, exemplifies, world-class, premier, cutting-edge. Grep your draft. Almost every hit can be deleted or replaced with a concrete fact.

A useful test: pretend you are the subject's neutral biographer, not its publicist. Would your biographer use this word? If not, cut it.

Also watch for the verb "boasts." A factory does not "boast" 200 employees; it has 200 employees. The personification is brochure-speak.

## Related patterns

- **Pattern 1 (significance inflation):** same problem, different vocabulary. Inflation reaches for "pivotal" and "testament"; promotional reaches for "nestled" and "vibrant."
- **Pattern 8 (AI vocabulary):** "vibrant" and "intricate" appear under both labels. Different angle, same words.
- **Pattern 33 (generic positive conclusions):** "the future looks bright" is the brochure register applied to endings.
