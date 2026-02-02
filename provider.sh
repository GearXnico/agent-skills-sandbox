#!/usr/bin/env sh
# Stand-in for the payment provider.
# Usage: provider.sh charge <order-id> <amount> <timeout-seconds>
latency=${PROVIDER_LATENCY:-1}
echo "$2 $3" >> "${LEDGER:-ledger.txt}"
[ "$latency" -le "$4" ]
