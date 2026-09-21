# Pattern 22: Curly quotes

**Typographic ("smart") quotes appearing where the document's format or house style calls for straight quotes.**

## Why LLMs do this

Language models may reproduce curly quotes from typeset training material or from the interface rendering their output. Word processors and publishing tools also convert straight quotes automatically.

Because many human-operated tools make the same conversion, quote style alone carries no useful authorship conclusion. It matters when it conflicts with the surrounding format.

## Why readers notice it

In technical documentation, code, JSON, and some web publishing systems, straight quotes are required or conventional. In typeset prose, curly quotes may be preferred. Readers notice inconsistency more than either choice by itself.

The mismatch is especially visible in code blocks or technical content, where curly quotes are actively wrong. They will break a string literal or fail a JSON parser.

The editorial question is therefore consistency and compatibility: use the quote style the medium requires, and do not treat typography as proof of provenance.

## Examples

After (straight quotes, the ASCII " character):
> She said "the meeting was a disaster" and walked out.

Before (curly quotes, the typographic characters U+201C and U+201D):
> She said “the meeting was a disaster” and walked out.

The shift is subtle visually but obvious to anyone running a script over the text, and to many readers' eyes once they know to look. The left and right typographic quotes are different Unicode characters from the straight double-quote.

## How to self-spot

Search your draft for the Unicode characters. The four common offenders are U+2018, U+2019, U+201C, and U+201D (left and right single and double typographic quotes). Replace them with straight quotes (' and ") unless the publication or rendering context specifically calls for typographic quotes.

If you write in a tool that auto-converts (Word, Google Docs, some Markdown editors), turn off the auto-conversion or run a normalization pass before publishing.

A regex like `[‘’“”]` will find all of them. A quick `tr` or sed substitution will fix them.

## Related patterns

- **Pattern 17 (em dash overuse):** also a typographic-character pattern. ChatGPT outputs both.
- **Pattern 18 (boldface overuse):** another formatting tell from the same generation pipeline.
