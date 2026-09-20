# Evaluation set

Slop Sense uses two evaluation layers because a lexical match and a good edit
are different claims.

## Run the deterministic layer

Install the locked scorer once, then run the evaluation:

```bash
npm ci
npm run evaluate
```

`npm run evaluate` is the single CI evaluation command. It makes no model calls.
It exercises the Python rhythm measurements, Markdown/input handling, CLI
failure behavior, the shell wrapper with controlled substitute programs, the
repository-local pinned scorer, fixture contracts, coverage inventory, expected
failure baseline, and golden-case schemas. To isolate a case while debugging:

```bash
python3 evaluation/run.py --id DET-EXTRACT-002
```

Every failure prints the stable fixture ID, its expected outcome, and the actual
assertion result. The full fixture contract is in
[`fixtures/deterministic.json`](fixtures/deterministic.json); each entry names
its target, layer, polarity, expected outcome, and rationale.

## What each layer means

The deterministic layer records raw behavior that can be repeated exactly:

- measurements and matches: extracted text, counts, matched words,
  constructions, metric bands, and process exit status;
- deterministic policy: only classifications explicitly implemented in the
  current scripts;
- integration behavior: the output of exactly `slop-detector@1.2.0`, kept
  separate from wrapper-substitute tests.

The editorial layer records contextual assessment and rewrite behavior:

- whether a raw signal warrants an actionable finding in the passage;
- what a rewrite must, may, and must not change;
- what facts, qualifications, quotations, register, and voice must survive.

Accordingly, “must stay clean” always names the outcome. A technical use of
`robust` may have a correct **raw lexical match** while requiring **no actionable
finding and no rewrite**. Intentional repeated openings may have a correct raw
anaphora measurement while the editorial case requires that the repetition
remain. Register and voice do not become deterministic merely because the
catalogue discusses them.

## Coverage and known failures

[`coverage.json`](coverage.json) is the auditable inventory. It maps every
in-scope bundled behavior and external scorer rule family to positive, relevant
negative, and applicable boundary fixtures. It also lists exclusions and future
behavior, so the inventory does not imply that all 36 qualitative patterns have
deterministic implementations.

[`baseline.json`](baseline.json) lists downstream behavior that is intentionally
red today. These are executable expected failures, never skips:

- `DET-EXTRACT-002` — Markdown link extraction, owned by #8;
- `DET-PUNCT-002` — contextual punctuation guidance, owned by #9;
- `DET-PUNCT-003` — contextual severity, owned by #13;
- `DET-SCORER-WORD-003` — unresolved catalogue policy, owned by #14.

An expected failure prints `XFAIL`. If its desired assertion begins to pass, the
runner prints `XPASS` and exits non-zero so the exemption cannot remain silently.
Unexpected failures also exit non-zero.

## Golden editorial cases

[`golden/cases.json`](golden/cases.json) contains original fixture prose for
representative AI patterns, precise technical language, quotations, formal
prose, intentional repetition, authorial punctuation, and fact-verification
behavior. These cases are reviewed with [`RUBRIC.md`](RUBRIC.md), not exact
rewrite equality. CI validates that every golden case contains all required
contract fields but does not call a model.

Start a review by copying [`golden/review-template.json`](golden/review-template.json).
Review records belong in a branch or PR under `evaluation/golden/reviews/`; they
are evidence for a proposed skill, prompt, model, or baseline change, not a
required artifact for ordinary deterministic runs.

## Scorer reproducibility and upgrades

Three files must agree on the scorer version:

- `package.json` pins the direct dependency exactly;
- `package-lock.json` locks its complete dependency graph;
- `evaluation/SCORER_VERSION` is verified against the installed package by the
  harness;
- `skills/slop-sense/scripts/score.sh` pins the optional npx fallback exactly.

The real integration invokes only `node_modules/.bin/slop-score`; it never
inherits `slop-score` from `PATH` and never downloads a latest version. The
wrapper selection and forwarding tests use temporary substitutes and make no
claim about lexical quality.

To upgrade the scorer, change all version pins, run `npm install` to regenerate
the lockfile, run the full evaluation, and inspect every changed match and score.
The PR must list the old and new versions, explain each baseline change, and name
the reviewer who approved the lexical/construction changes. Do not update
expected values merely to make CI green.

Fixture prose in this directory is original unless a case explicitly records
`CC0` or `public-domain` provenance. Do not copy third-party marketing examples
into the corpus.
