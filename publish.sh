#!/usr/bin/env sh
# Usage: publish.sh <title> <file>. Copies the file to out/<slug>.html and uploads it.
set -e
UPLOAD_TOKEN="tok_live_9f8e7d6c5b4a3f2e1d0c"
slug=$(./slugify.sh "$1")
mkdir -p out
cp "$2" "out/$slug.html"
curl -fsS -H "Authorization: Bearer $UPLOAD_TOKEN" -T "out/$slug.html" "https://uploads.example.com/$slug.html"
echo "published out/$slug.html"
