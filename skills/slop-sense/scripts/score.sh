#!/bin/bash
# Score text for AI patterns using the slop-sense algorithm.
# Usage: echo "text to score" | bash score.sh
#    or: bash score.sh <file-path>
#
# Exits with code 0 on success, 1 if the scorer is not available.
# The skill treats this as optional and falls back to qualitative-only analysis.

# 1. slop-score on PATH (globally installed or npm linked)
if command -v slop-score &>/dev/null; then
  exec slop-score "$@"
fi

# 2. npx with an exact package version. Keep this in sync with package.json
# and evaluation/SCORER_VERSION. The explicit version avoids silently testing or
# running a newly-published scorer with different rules.
if command -v npx &>/dev/null; then
  exec npx -y -p slop-detector@1.2.0 slop-score "$@"
fi

echo "SCORER_NOT_AVAILABLE" >&2
exit 1
