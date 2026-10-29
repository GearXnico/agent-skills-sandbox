# AGENTS.md

A small notes API used to test agent skills. Python standard library only, data in SQLite.

## Git workflow

- Base branch: security
- Branch names: `feature/`, `fix/` plus 2 to 4 lowercase words
- Commits: Conventional Commits
- Checks: ./test.sh
- Changelog: none
- Update method: rebase
- task-flow mode: safe

## Rules

- Every query uses parameters, never string formatting.
- Admin routes check the `ADMIN_TOKEN` environment variable with `require_admin`.
- Errors return a short message, never internal details.
