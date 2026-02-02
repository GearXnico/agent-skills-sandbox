#!/usr/bin/env sh
set -e
LEDGER=$(mktemp); export LEDGER
./worker.sh 42 1990 >/dev/null
charges=$(wc -l < "$LEDGER" | tr -d ' ')
[ "$charges" -eq 1 ] || { echo "FAIL: order 42 charged $charges times"; exit 1; }
echo "ok"
