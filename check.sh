#!/usr/bin/env sh
# Stands in for a test suite: every decision record has a title and a status.
set -e
for f in docs/adr/[0-9]*.md; do
  grep -q '^# ' "$f" || { echo "$f: missing title"; exit 1; }
  grep -qi '^status:' "$f" || { echo "$f: missing status"; exit 1; }
done
echo "ok"
