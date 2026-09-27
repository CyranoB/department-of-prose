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

In a format that requires ASCII quotation marks, change:
> She said “the meeting was a disaster” and walked out.

to:
> She said "the meeting was a disaster" and walked out.

In typeset prose that uses curly quotation marks, keep the first version. The mark itself provides no authorship evidence.

## How to self-spot

Search your draft for the Unicode characters. The four common offenders are U+2018, U+2019, U+201C, and U+201D (left and right single and double typographic quotes). Change them only when the publication or rendering context calls for straight quotes; otherwise preserve the supplied typography, especially in quotations.

If a tool auto-converts quote style, check the output against the document’s required format before publishing.

A regex like `[‘’“”]` will find all of them. A conversion tool can change them when the house style requires it.

## Related patterns

- **Pattern 17 (em dash overuse):** another punctuation pattern whose frequency and effect need context.
- **Pattern 18 (boldface overuse):** another formatting choice to assess in context.
