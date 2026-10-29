# Use SQLite for storage

Status: Accepted
Date: 2026-03-09

## Context and Problem Statement

The service stores a few thousand notes for one team and runs as a single process on one machine.

## Considered Options

* SQLite file next to the service
* Postgres server

## Decision Outcome

Chosen option: "SQLite file next to the service", because one process and a few thousand rows do not need a database server, and backups are a file copy.

### Consequences

* Good, because there is nothing else to run or pay for.
* Bad, because only one process can write at a time; revisit if the service needs more than one instance.
