# AGENTS.md

A one-page site used to test agent skills. Work goes to `release-dev`; releases go to `release-main`.

## Git workflow

- Base branch: release-dev
- Branch names: feature/, fix/, docs/, chore/, release/
- Commits: Conventional Commits
- Checks: ./check.sh
- Changelog: CHANGELOG.md, under [Unreleased]
- Update method: rebase
- task-flow mode: safe
- Release: git-flow; `release/x.y.z` from release-dev, pull request to release-main, then a back-merge pull request from release-main to release-dev. The maintainer merges and tags.
