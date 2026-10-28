# 1. One check script

Status: Accepted

## Context

Contributors forgot to run some checks when there were several scripts.

## Decision

Every check lives in `check.sh`, and it is the only command to run before a pull request.

## Consequences

Adding a check means adding it to `check.sh`, not a new script.
