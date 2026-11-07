---
type: Data Product Type
okf_version: '0.1'
timestamp: '2026-11-06T21:15:00Z'
description: Data product ingesting via human and serving via human.
title: 'Cell 15.15: Human-curated catalog, human read'
tags:
- data-product-type
- in-h
- out-h
- plausible
related:
- /knowledge-concepts/pattern-human
- /knowledge-concepts/data-product
- /knowledge-concepts/verdict
---

# 15.15 — Human-curated catalog, human read

**Interface:** IN {H} → OUT {H}&emsp;&emsp;**Verdict:** plausible

People enter the data (forms, editors, review) and people read the same data back (a report, a screen, a printout). A diagonal cell in the pattern space: the value is a single, shared, human-scale record — not a feed, not an API, not a bulk file. The oldest data product there is: the ledger, the paper filing cabinet, the shared spreadsheet.

![Interface diagram: IN H to OUT H](/assets/cells/in-h-out-h.svg)

## When to use

The audience is a small group of people who both maintain and read the data — a team tracker, a manual register, an approval log — with no machine consumer at all.

## What's inside

- Ingest: **human entry / curation** — data produced by people (forms, editors, review UIs), validated and audit-trailed on every change.
- Core: a light transform between ingest and serve
- Serve: a **human-facing surface** (dashboard, report, printout, or review screen) — the layer people actually read.
- State: a durable **state store** and an **audit trail** of human changes.

## State & cost

Dominated by the durable state store (grows with entity/state breadth) and the audit trail of human edits. Serving people is cheap to run and cheap to trust — a presentation layer over a queryable backend. The cost is not infrastructure but discipline: human-entered data needs validation, provenance, and a correction path.

## Watch out

- Human-entered data is the softest input: it arrives irregularly, carries intent and errors, and needs **validation, provenance, and a correction path** — trust leans on the audit trail, not the schedule.
- A human-facing surface inherits the state behind it: the report/dashboard carries every as-of and correctness rule of the store, and a person spots a stale number faster than an API client will.

## Typical next step

add a **query API** → cell [15.13](/data-product-types/in-h-out-rh), add a **bulk file** → cell [15.14](/data-product-types/in-h-out-bh), and add a **feed** → cell [15.12](/data-product-types/in-h-out-sh) (a *synthetic* stream, since S is absent from IN); or the source world gains a leg this product does not yet take, and it migrates to a richer IN-state on the same row.

## Verdict

**plausible** — a human-curated, human-read record is a completely sensible product; it is kept out of the "common" tier only because real data products rarely serve *only* people once the data grows — a query or a file usually joins.

## Related

* [human](/knowledge-concepts/pattern-human)
* [data-product](/knowledge-concepts/data-product) — the overall model
* [verdict](/knowledge-concepts/verdict) — what the common / plausible / niche tag means
