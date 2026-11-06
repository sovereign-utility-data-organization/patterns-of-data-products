---
type: Knowledge Concept
okf_version: "0.1"
timestamp: 2026-11-06T12:50:00Z
description: The request/response integration pattern (R) — synchronous on-demand query, applied on a product's input side (polling upstream) or output side (API/query serving).
title: Request/response integration pattern
tags:
  - integration-pattern
  - request-response
  - api
related:
  - /knowledge-concepts/data-product
  - /knowledge-concepts/pattern-batch
  - /knowledge-concepts/pattern-streaming
  - /knowledge-concepts/synthetic-stream
---

# Request/response pattern (`R`)

Synchronous, on-demand data access: the consumer asks, the product answers.
Protocol-agnostic at this level; typical bindings: REST/JSON, OData, GraphQL,
JDBC/ODBC, SOAP, or any query interface.

## On the input side (polling)

The product *pulls* from upstream on demand or on a schedule it presents as
"on demand": polling upstream APIs, device registries, or market pages.
Semantics in the contract:

- **poll cadence** — the real latency guarantee,
- **change detection** — how "new" is computed between polls (version
  stamps, row counts, content hashes),
- **idempotency** — re-polling must not duplicate state.

## On the output side (query serving)

Consumers obtain data per request: current state, historical queries,
filtering/aggregation. Query serving *requires a durable state store* —
unlike pure streaming cells — and is the natural shape for anything
"analytical" (a consumer wants an answer, not a firehose).

## Where it appears

- Pure cells: `6.*` (polling ingest) and `*.6` (query-only serving)
- Mixed: `BR` (query + file), `RS` (live + lookup), `BRS` (omni-channel)
- Note: a cell that *serves* `S` without taking `S` as input is not
  affected by this pattern directly — see [synthetic stream](/knowledge-concepts/synthetic-stream)
