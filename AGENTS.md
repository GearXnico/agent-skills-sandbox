# AGENTS.md

A small shell utility used to test agent skills. `slug.sh` turns a title into a slug; `publish.sh` uses it to name files.

## Git workflow

- Base branch: review
- Branch names: feature/, fix/, chore/
- Commits: Conventional Commits
- Checks: ./test.sh
- Changelog: none
- Update method: rebase
- task-flow mode: safe

## Rules

- Every change ships with a test in `test.sh`.
- No secrets in the repository; configuration comes from environment variables.
