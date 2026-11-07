---
type: Data Product Type
okf_version: '0.1'
timestamp: '2026-11-06T21:15:00Z'
description: Data product ingesting via batch (bulk/file) + streaming (pub/sub feed) and serving via request/response (on-demand query) + human.
title: 'Cell 3.13: hot & cold → API + human'
tags:
- data-product-type
- in-bs
- out-rh
- common
related:
- /knowledge-concepts/pattern-batch
- /knowledge-concepts/pattern-request-response
- /knowledge-concepts/pattern-streaming
- /knowledge-concepts/pattern-human
- /knowledge-concepts/data-product
- /knowledge-concepts/verdict
---

# 3.13 — hot & cold → API + human

**Interface:** IN {B, S} → OUT {R, H}&emsp;&emsp;**Verdict:** common

A product that takes files (batch) and live streams and serves a query API and a human-facing surface (dashboard/report). Machine-side inputs ({B, S}) drive it — the multi-surface serves people, not just machines.

![Interface diagram: IN BS to OUT RH](/assets/cells/in-bs-out-rh.svg)

## When to use

The data the audience wants is real, but the reader is a person, not a service: they need a report or dashboard over a single leg of bulk files and a live feed, not raw events or a bulk drop.

## What's inside

- Ingest: a scheduled **bulk ingest** (pickup, parse, validate, load) and a **stream consumer** (offsets, replay) for the live leg.
- Core: a **fold/aggregation core** that folds the live leg into queryable state or windowed files
- Serve: a **query service** (the API surface) over the state store and a **human-facing surface** (dashboard, report, printout, or review screen) — the layer people actually read.
- State: a durable **state store** and the **feed log** (retention).

## State & cost

Dominated by the durable state store (grows with entity/state breadth).

## Watch out

- A human-facing surface inherits the state behind it: the report/dashboard carries every as-of and correctness rule of the store, and a person spots a stale number faster than an API client will.
- **Mixed time bases** in the inputs (live vs. poll/cycle/human): fix the authoritative as-of per surface, or each output looks correct alone and wrong cross-checked.
- Late and out-of-order events are a **first-class** question: a watermark and a re-issue/correction rule, or history gains holes and duplicate facts.
- This is machine-produced, human-read: make sure a person actually reviews/approves the served view rather than the pipeline writing it straight through.

## Typical next step

add **human curation on the input side** → cell [10.13](/data-product-types/in-bhs-out-rh) when the data should not be purely machine-fed, add a **bulk file** → cell [3.9](/data-product-types/in-bs-out-bhr), and add a **feed** → cell [3.11](/data-product-types/in-bs-out-rsh); or the source world gains a leg this product does not yet take, and it migrates to a richer IN-state on the same row.

## Verdict

**common** — human-facing output (reports/dashboards) is among the most common ways people actually consume data, and its demand is real where this audience exists.

## Related

* [batch](/knowledge-concepts/pattern-batch)
* [request/response](/knowledge-concepts/pattern-request-response)
* [streaming](/knowledge-concepts/pattern-streaming)
* [human](/knowledge-concepts/pattern-human)
* [data-product](/knowledge-concepts/data-product) — the overall model
* [verdict](/knowledge-concepts/verdict) — what the common / plausible / niche tag means
