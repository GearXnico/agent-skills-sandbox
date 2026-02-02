#!/usr/bin/env sh
# Usage: worker.sh <order-id> <amount>
. ./worker.env
if ./provider.sh charge "$1" "$2" "$PAYMENT_TIMEOUT"; then
  echo "order $1 paid"
else
  echo "order $1 charge failed" >&2
  exit 1
fi
