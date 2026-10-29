#!/usr/bin/env sh
# Turns a title into a URL slug: lowercase words joined by single dashes.
# An optional second argument limits the slug to that many characters.
slug=$(printf '%s\n' "$1" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9 ]//g; s/  */-/g; s/^-//; s/-$//')
if [ -n "$2" ]; then slug=$(printf '%s' "$slug" | cut -c1-"$2"); fi
printf '%s\n' "$slug"
