#!/usr/bin/env sh
set -e
grep -q '<footer>' index.html
grep -qE '^[0-9]+\.[0-9]+\.[0-9]+$' VERSION
grep -q "## \[$(cat VERSION)\]" CHANGELOG.md
echo ok
