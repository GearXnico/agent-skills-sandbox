#!/usr/bin/env sh
# Stand-in for a test suite: the page needs a title and a footer.
set -e
grep -q "<title>" index.html || { echo "check failed: index.html has no <title>"; exit 1; }
grep -q "<footer>" index.html || { echo "check failed: index.html has no <footer>"; exit 1; }
echo "checks passed"
