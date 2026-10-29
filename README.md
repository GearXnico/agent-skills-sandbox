# agent-skills-sandbox

Test fixtures for [agent-skills](https://github.com/GearXnico/agent-skills). Each scenario is a branch with a small project, a check that stands in for a test suite, and an `AGENTS.md` with its own git workflow. The evals of a skill run against every scenario, so a skill only passes if it follows each repository's rules instead of one fixed workflow.

| Base branch | Scenario | Rules |
| --- | --- | --- |
| `trunk` | Everything lands on one branch | No prefixes, no changelog, branches updated by merge |
| `integration-dev` | Work goes to an integration branch; releases go to `integration-main` | Conventional Commits, changelog under `[Unreleased]`, pull request template, branches updated by rebase, tasks linked to GitHub issues (issue #4 is a fixture) |
| `no-rules` | The repository declares no workflow | None: the skill has to ask, and offer to write the rules down |
| `bugfix` | A shell utility with a known bug and its tests | Checks with `./test.sh`, no changelog |
| `docs` | A site whose README, `AGENTS.md` and an accepted ADR describe its check script | Checks with `./check.sh`, changelog under `[Unreleased]` |
| `services` | An order system described by `compose.yml`, service READMEs and an ADR, with known design flaws | Checks with `docker compose config -q`, no changelog |
| `deps` | A Node.js script with an outdated, vulnerable dependency | Checks with `npm test`, changelog under `[Unreleased]` |
| `python-poetry` | A Python command-line tool managed with Poetry, with CI and a Dockerfile | Checks with `poetry run pytest -q`, changelog under `[Unreleased]` |
| `python-pip` | A Python script with a loose `requirements.txt` and no package manager | Checks with `python -m pytest -q`, no changelog |
| `review` | A shell utility and a script that uses it, with five branches to review against it: `review-bug`, `review-secret`, `review-no-test`, `review-outside` (breaks a file the diff does not touch) and `review-clean` | Checks with `./test.sh`, every change needs a test |
| `incident` | A payment worker whose history, deploy log, worker logs and on-call notes record a double-charge incident: a recent change triggered a bug that had been latent for months | Checks with `./test.sh`, no changelog |
| `adr` | A notes service with three decision records in MADR format and an index in `docs/adr/` | Checks with `./check.sh` (every record has a title and a status), no changelog |
| `security` | A notes API in Python with SQLite, with five branches to review against it: `security-sql`, `security-secret`, `security-auth`, `security-error` and `security-clean`. Every branch passes its tests | Checks with `./test.sh`, rules for queries, admin routes and errors in `AGENTS.md` |
| `release-dev` | A site at 1.2.0 on `release-main`, with a feature and a fix on `release-dev` to release; `release-breaking` adds a breaking change on top | Checks with `./check.sh`, changelog under `[Unreleased]`, a `Release:` rule for git-flow releases |

`main` only holds this README. Pull requests opened during an eval target the scenario's base branch and are closed afterwards without merging.

## Run an eval

1. Clone the repository and check out the scenario's base branch.
2. Install the skill under test from agent-skills into `.agents/skills/` (or `.claude/skills/` for Claude Code).
3. Give the agent the request from the skill's `evals/` file and compare what it does with the expected behaviour.
4. Close any pull request the eval opened and delete its branch.
