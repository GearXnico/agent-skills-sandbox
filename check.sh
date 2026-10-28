#!/usr/bin/env sh
# Stand-in for a test suite: the page needs a title and a footer.
# --verbose prints each check as it runs.
set -e
verbose=false
[ "$1" = "--verbose" ] && verbose=true
check() {
  $verbose && echo "checking $1"
  grep -q "$1" index.html || { echo "check failed: index.html has no $1"; exit 1; }
}
check "<title>"
check "<footer>"
echo "checks passed"
