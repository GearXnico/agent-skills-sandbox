#!/usr/bin/env sh
# Turns a title into a URL slug: lowercase words joined by single dashes.
printf '%s\n' "$1" | tr '[:upper:]_' '[:lower:] ' | sed 's/[^a-z0-9 ]//g; s/  */-/g; s/^-//; s/-$//'
