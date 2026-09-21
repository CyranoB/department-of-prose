# Pattern 21: Emojis in structure

**Decorating headings, bullets, or section breaks with emojis as if they were visual punctuation.**

## Why LLMs do this

A specific subgenre of training data, including corporate blog posts, social-media captions, and Notion-style documentation, uses emojis as structural decoration. Stars for tips, rockets for launches, lightbulbs for ideas, checkmarks for completed items. The model learned that decorative emojis signal a friendly, modern register.

Some RLHF feedback also rewards emoji use as making content feel "approachable" or "human." This is exactly backwards in many contexts. The pattern is now so associated with corporate-tech writing that it reads as the opposite of human.

## Why readers notice it

The decoration is mechanical and consistent. Every section heading gets an emoji. Every bullet starts with one. The selection is almost always the same small palette. The repetition flattens the meaning of each individual emoji into pure ornament.

Human writers who use emojis tend to use them for genuine emphasis or humor, not as section decorations. When someone uses a star at the start of every paragraph, they have stopped using emoji as a communication choice and started using it as wallpaper.

The pattern is especially jarring in technical documentation or formal writing, where the decorative tone clashes with the content.

## Examples

After:
> ## What we shipped this quarter
>
> The team launched three new features and reduced p95 latency by 40%.

Before:
> ## 🚀 What We Shipped This Quarter
>
> - ✨ The team launched three new features
> - ⚡ Reduced p95 latency by 40%
> - 🎯 On track for Q4 goals

Notice that the human version trusts the structure of headings and prose to do the visual work. The AI version uses emojis to substitute for that structure.

## How to self-spot

Count emojis in your draft, especially those at the start of headings or bullets. If they are decorative (just to make a section "pop") rather than meaningful (carrying actual information), remove them.

The test: would the emoji be missed if it were gone? If no, it was decoration. If yes (for example, a bug glyph in a bug-tracker line that signals "this is the bug"), it is functional.

Emojis in body text used for tone (rare humor, a single thank-you gesture, a reaction at the end of a casual line) are different and usually fine. The pattern is about emojis as structural decoration.

## Related patterns

- **Pattern 18 (boldface overuse):** same urge to add visual weight.
- **Pattern 20 (Title Case headings):** the same misjudged formality.
