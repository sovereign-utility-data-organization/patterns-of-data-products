---
type: Data Product Type
okf_version: '0.1'
timestamp: '2026-11-08T19:52:00Z'
definition: "A product that takes files (batch) and serves a query API and a human-facing surface (dashboard/report). Machine-side inputs ({B}) drive it — the multi-surface serves people, not just machines."
example: "The data the audience wants is real, but the reader is a person, not a service: they need a report or dashboard over a single leg of bulk files, not raw events or a bulk drop."
altLabel:
- "B → RH"
- "Cell 7.13"
- "batch-only → API + human"
title: 'Cell 7.13: batch-only → API + human'
tags:
- data-product-type
- in-b
- out-rh
- common
related:
- /concepts/pattern-batch
- /concepts/pattern-request-response
- /concepts/pattern-human
- /concepts/data-product
- /concepts/verdict
---

# 7.13 — batch-only → API + human

**Interface:** IN {B} → OUT {R, H}&emsp;&emsp;**Verdict:** common

A product that takes files (batch) and serves a query API and a human-facing surface (dashboard/report). Machine-side inputs ({B}) drive it — the multi-surface serves people, not just machines.

![Interface diagram: IN B to OUT RH](/assets/cells/in-b-out-rh.svg)

## When to use

The data the audience wants is real, but the reader is a person, not a service: they need a report or dashboard over a single leg of bulk files, not raw events or a bulk drop.

## What's inside

- Ingest: a scheduled **bulk ingest** (pickup, parse, validate, load).
- Core: a light transform between ingest and serve
- Serve: a **query service** (the API surface) over the state store and a **human-facing surface** (dashboard, report, printout, or review screen) — the layer people actually read.
- State: a durable **state store**.

## State & cost

Dominated by the durable state store (grows with entity/state breadth).

## Watch out

- A human-facing surface inherits the state behind it: the report/dashboard carries every as-of and correctness rule of the store, and a person spots a stale number faster than an API client will.
- This is machine-produced, human-read: make sure a person actually reviews/approves the served view rather than the pipeline writing it straight through.

## Typical next step

add **human curation on the input side** → cell [14.13](/data-product-types/in-bh-out-rh) when the data should not be purely machine-fed, add a **bulk file** → cell [7.9](/data-product-types/in-b-out-bhr), and add a **feed** → cell [7.11](/data-product-types/in-b-out-rsh) (a *synthetic* stream, since S is absent from IN); or the source world gains a leg this product does not yet take, and it migrates to a richer IN-state on the same row.

## Verdict

**common** — A product that ingests bulk files and serves query APIs plus a human-facing surface (a dashboard, report, or review). It is the right shape where the reader is a person rather than a service, and the human-shaped view is itself what the next consumer — or the next machine in the loop — needs to act on.

## Related

* [batch](/concepts/pattern-batch)
* [request/response](/concepts/pattern-request-response)
* [human](/concepts/pattern-human)
* [data-product](/concepts/data-product) — the overall model
* [verdict](/concepts/verdict) — what the common / plausible / niche tag means
