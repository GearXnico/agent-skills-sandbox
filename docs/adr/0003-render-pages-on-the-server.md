# Render pages on the server

Status: Proposed
Date: 2026-04-14

## Context and Problem Statement

The pages are simple lists and forms. A client-side framework would add a build step.

## Considered Options

* Server-rendered HTML templates
* A single-page app

## Decision Outcome

Chosen option: "Server-rendered HTML templates", because the pages need no client state and the team wants no build step.

### Consequences

* Good, because there is no JavaScript bundle to build or ship.
* Bad, because interactive features would need a page reload.
