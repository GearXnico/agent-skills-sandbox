# agent-skills-sandbox

Test fixtures for [agent-skills](https://github.com/GearXnico/agent-skills). Each scenario is a branch with a one-page site, a `check.sh` that stands in for a test suite, and an `AGENTS.md` with its own git workflow. The evals of a skill run against every scenario, so a skill only passes if it follows each repository's rules instead of one fixed workflow.

| Base branch | Scenario | Rules |
| --- | --- | --- |
| `trunk` | Everything lands on one branch | No prefixes, no changelog, branches updated by merge |
| `integration-dev` | Work goes to an integration branch; releases go to `integration-main` | Conventional Commits, changelog under `[Unreleased]`, pull request template, branches updated by rebase |
| `no-rules` | The repository declares no workflow | None: the skill has to ask, and offer to write the rules down |

`main` only holds this README. Pull requests opened during an eval target the scenario's base branch and are closed afterwards without merging.

## Run an eval

1. Clone the repository and check out the scenario's base branch.
2. Install the skill under test from agent-skills into `.agents/skills/` (or `.claude/skills/` for Claude Code).
3. Give the agent the request from the skill's `evals/` file and compare what it does with the expected behaviour.
4. Close any pull request the eval opened and delete its branch.
