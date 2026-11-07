---
type: Data Product Type
okf_version: '0.1'
timestamp: '2026-11-06T21:15:00Z'
description: Data product ingesting via batch (bulk/file) and serving via human.
title: 'Cell 7.15: Batch data as a report / dashboard'
tags:
- data-product-type
- in-b
- out-h
- common
related:
- /knowledge-concepts/pattern-batch
- /knowledge-concepts/pattern-human
- /knowledge-concepts/data-product
- /knowledge-concepts/verdict
---

# 7.15 — Batch data as a report / dashboard

**Interface:** IN {B} → OUT {H}&emsp;&emsp;**Verdict:** common

Nightly or scheduled bulk data becomes the thing people actually read: the morning report, the standing dashboard, the printed schedule. The product's job is to turn a flat, complete file world into a clear, current view for a human audience — the EOD report is the archetypal cell.

![Interface diagram: IN B to OUT H](/assets/cells/in-b-out-h.svg)

## When to use

The data lands in bulk files, but the audience is people who want a readable report or dashboard rather than a raw file — the classic 'load at night, read in the morning' shape.

## What's inside

- Ingest: a scheduled **bulk ingest** (pickup, parse, validate, load).
- Core: a light transform between ingest and serve
- Serve: a **human-facing surface** (dashboard, report, printout, or review screen) — the layer people actually read.
- State: a durable **state store**.

## State & cost

Dominated by the durable state store (grows with entity/state breadth). Serving people is cheap to run and cheap to trust — a presentation layer over a queryable backend.

## Watch out

- A human-facing surface inherits the state behind it: the report/dashboard carries every as-of and correctness rule of the store, and a person spots a stale number faster than an API client will.
- This is machine-produced, human-read: make sure a person actually reviews/approves the served view rather than the pipeline writing it straight through.

## Typical next step

add **human curation on the input side** → cell [14.15](/data-product-types/in-bh-out-h) when the data should not be purely machine-fed, add a **query API** → cell [7.13](/data-product-types/in-b-out-rh), and add a **bulk file** → cell [7.14](/data-product-types/in-b-out-bh); or the source world gains a leg this product does not yet take, and it migrates to a richer IN-state on the same row.

## Verdict

**common** — turning settled bulk data into a report or dashboard is one of the most frequent data products in the world; the pattern is cheap (a state store plus a presentation layer) and the demand is universal.

## Related

* [batch](/knowledge-concepts/pattern-batch)
* [human](/knowledge-concepts/pattern-human)
* [data-product](/knowledge-concepts/data-product) — the overall model
* [verdict](/knowledge-concepts/verdict) — what the common / plausible / niche tag means
