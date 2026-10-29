#!/usr/bin/env sh
# Runs slugify.sh against known titles. Exits 1 if any case fails.
fail=0
expect() {
  got=$(./slugify.sh "$1")
  if [ "$got" = "$2" ]; then echo "ok: '$1'"; else echo "FAIL: '$1' gave '$got', expected '$2'"; fail=1; fi
}
expect "Hello World" "hello-world"
expect "Hello  World" "hello-world"
expect " Release 2.0 " "release-20"
expect "" ""
exit $fail
