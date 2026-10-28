# 1. Postgres for orders

Status: Accepted

## Context

Orders need transactions and simple reporting.

## Decision

Orders, products and payments live in one Postgres database shared by `api` and `worker`.

## Consequences

Both services depend on the same schema; a schema change has to be deployed to both together.
