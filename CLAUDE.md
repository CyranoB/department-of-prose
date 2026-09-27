# The Department of Prose

A Claude Code plugin / cross-agent skill family for contextual writing review and revision. Three sibling skills share one versioned editorial catalogue. The optional lexical scorer and rhythm checker produce raw measurements, not authorship verdicts.

## Structure

- `skills/slop-sense/SKILL.md` — the rewriter (36 patterns, workflow, ai;dr mode). Edit this for rewrite-behavior changes.
- `skills/slop-sense/scripts/score.sh` — optional algorithmic scorer wrapper around `npx slop-detector`. Falls back to qualitative-only if Node is missing. Measures *lexical* tells only (slop words, trigrams, contrast phrases). Reused by `slop-check` via the sibling path `../slop-sense/scripts/score.sh`.
- `skills/slop-sense/scripts/rhythm.py` — pure-Python (stdlib only) structural checker for dimensions `score.sh` does not measure: burstiness, contraction ratio, aphoristic closers, anaphora, raw punctuation counts, and conservative prose cadence candidates. These are editorial heuristics rather than authorship evidence. Reused by `slop-check` via the sibling path `../slop-sense/scripts/rhythm.py` and vendored into the claude.ai bundle.
- `skills/slop-check/SKILL.md` — review-only skill (no rewrite). Uses the shared versioned catalogue; allowed-tools deliberately exclude Write/Edit.
- `skills/slop-explain/SKILL.md` — per-pattern educational skill. Resolves user request to a pattern number 1-36 via the lookup table, then reads the matching `patterns/NN-name.md` file.
- `skills/slop-explain/patterns/` — 36 generated per-pattern evidence notes (`01-significance-inflation.md` through `36-reflexive-formality.md`). The versioned catalogue is their policy source.
- `docs/pattern-catalogue-spec.md` and `docs/pattern-catalogue-source-audit.md` — editorial decisions and primary-source limits. `scripts/sync-catalogue.py` generates the four runtime catalogue copies and 36 evidence notes; `--check` detects drift.
- `.claude-plugin/plugin.json` — plugin manifest. Lists all three skills in `skills[]` so `npx skills@latest` can enumerate them together.
- `.claude-plugin/marketplace.json` — Claude Code marketplace listing. Mirrors the shared plugin version from `plugin.json`.
- `.codex-plugin/plugin.json` — Codex plugin manifest. Points at the same top-level `skills/` directory and includes Codex install-surface metadata.
- `.agents/plugins/marketplace.json` — Codex repository marketplace. Exposes the repository root as the `department-of-prose` plugin.
- `scripts/plugin_version.py` — checks or bumps the shared version across both plugin formats and enforces version bumps for plugin changes.
- `scripts/link-skills.sh` — dogfooding helper; auto-discovers every `SKILL.md` under `skills/` and symlinks each into `~/.claude/skills` (override with `SKILLS_DEST`).
- `dist-src/slop-sense-bundle/SKILL.md` — hand-crafted merged super-skill for the claude.ai / Claude Desktop upload path (one ZIP per skill, so all three modes collapse into one `slop-sense` skill). Source of truth for the bundle.
- `scripts/package-claude-ai.sh` — builds `dist/slop-sense.zip` from the bundle SKILL.md + vendored `score.sh` + vendored `rhythm.py` + vendored `patterns/`. Asserts exactly 36 pattern files. Output is gitignored.
- `evaluation/` — two-layer quality suite. `fixtures/deterministic.json` drives executable regressions, `coverage.json` maps in-scope behaviors, `baseline.json` tracks strict expected failures, and `golden/` holds rubric-reviewed editorial contracts.
- `package.json` / `package-lock.json` — exact `slop-detector` development dependency used only for reproducible real-scorer integration tests.
- `.github/workflows/evaluation.yml` — installs the locked scorer and runs `npm run evaluate` without model calls.

## When making changes

- **Bump the shared plugin version with `python scripts/plugin_version.py bump X.Y.Z`** for any user-visible change. The helper updates both plugin manifests plus the Claude marketplace mirrors; installed clients use this version as the update cache key.
- The plugin is distributed through Claude Code and Codex marketplaces plus `npx skills@latest add CyranoB/department-of-prose` (50+ agents). Don't add client-specific paths in any SKILL.md — they have to work cross-agent.
- **Trigger disambiguation matters.** All three skills share vocabulary domain. When editing any SKILL.md description, keep the "Prefer X if..." cross-references intact so the agent's router picks the right skill.
- The scorer is optional by design. Don't make `score.sh` a hard dependency; the skills must still do useful qualitative analysis when Node is unavailable.
- The `slop-check` skill calls the scorer via the sibling path `../slop-sense/scripts/score.sh`. If a cross-agent install ever flattens directory structure such that the relative path breaks, vendor a per-skill copy inside `slop-check/scripts/` rather than refactoring the path scheme.
- Pattern numbering (1-36) is the load-bearing convention across all three skills. Change policy in the spec and source audit, then run `python3 scripts/sync-catalogue.py`; update both lookup tables and packaging rules when IDs change. Re-run `bash scripts/package-claude-ai.sh` after any catalogue change.
- Packaging checks use the Python standard library. Run `python -m unittest discover -s tests -v`, both plugin validators, and `bash scripts/package-claude-ai.sh` before release.
- Run `npm ci && npm run evaluate` for deterministic regression coverage. Expected failures are executable assertions: an unexpected pass fails CI until its exemption is deliberately removed.
- Read the diff, run `bash scripts/link-skills.sh`, and try affected skills in a session for changes outside the deterministic scope.

## Release flow

1. Edit `SKILL.md` files / scripts / deep-dives.
2. Run `python scripts/plugin_version.py bump X.Y.Z` with a higher semantic version.
3. Run `python scripts/plugin_version.py check --base origin/main` and the packaging checks.
4. Commit, PR to `main`. Both marketplaces pick up the new version on push.
