#!/usr/bin/env sh
# Usage: publish.sh <title> <file>. Copies the file to out/<slug>.html.
set -e
slug=$(./slugify.sh "$1")
mkdir -p out
cp "$2" "out/$slug.html"
echo "published out/$slug.html"
