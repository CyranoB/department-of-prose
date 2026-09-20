#!/usr/bin/env bash
set -euo pipefail

# Builds dist/slop-sense.zip — a single merged super-skill ZIP for upload to
# claude.ai / Claude Desktop via Customize > Skills. Collapses the three
# sibling Claude Code skills (slop-sense, slop-check, slop-explain) into one
# claude.ai-uploadable skill folder.
#
# Source of truth for the merged SKILL.md is dist-src/slop-sense-bundle/SKILL.md.
# Patterns and score.sh are vendored from the per-skill folders at build time.

REPO="$(cd "$(dirname "$0")/.." && pwd)"
STAGE="$REPO/dist/staging/slop-sense"
OUT="$REPO/dist/slop-sense.zip"

rm -rf "$REPO/dist/staging" "$OUT"
mkdir -p "$STAGE/scripts" "$STAGE/patterns"

cp "$REPO/dist-src/slop-sense-bundle/SKILL.md" "$STAGE/SKILL.md"
cp "$REPO/skills/slop-sense/scripts/score.sh"  "$STAGE/scripts/score.sh"
cp "$REPO/skills/slop-sense/scripts/rhythm.py" "$STAGE/scripts/rhythm.py"
cp "$REPO/skills/slop-sense/scripts/factcheck.py" "$STAGE/scripts/factcheck.py"
cp "$REPO/skills/slop-explain/patterns/"*.md   "$STAGE/patterns/"

find "$STAGE" -name '.DS_Store' -delete

pattern_count="$(find "$STAGE/patterns" -name '*.md' | wc -l | tr -d ' ')"
if [ "$pattern_count" -ne 36 ]; then
  echo "error: expected 36 pattern files, found $pattern_count" >&2
  exit 1
fi

# claude.ai enforces a 1024-char limit on the SKILL.md `description` field.
desc_len="$(python3 -c '
import re, sys
with open(sys.argv[1]) as f:
    content = f.read()
fm = content.split("---", 2)[1]
m = re.search(r"description: \|\n(.*?)(?=\n[a-z][a-z\-]*:)", fm, re.DOTALL)
lines = [l[2:] if l.startswith("  ") else l for l in m.group(1).split("\n")]
print(len("\n".join(lines).rstrip()))
' "$STAGE/SKILL.md")"
if [ "$desc_len" -gt 1024 ]; then
  echo "error: SKILL.md description is $desc_len chars, max 1024 (claude.ai limit)" >&2
  exit 1
fi

( cd "$REPO/dist/staging" && zip -rq "$OUT" slop-sense )

if ! unzip -l "$OUT" | grep -q 'slop-sense/SKILL.md'; then
  echo "error: ZIP missing slop-sense/SKILL.md at root" >&2
  exit 1
fi

echo "built $OUT"
