#!/usr/bin/env sh
# Usage: worker.sh <order-id> <amount>
. ./worker.env
attempt=0
until ./provider.sh charge "$1" "$2" "$PAYMENT_TIMEOUT"; do
  attempt=$((attempt + 1))
  echo "order $1 charge failed (attempt $attempt), retrying" >&2
done
echo "order $1 paid"
