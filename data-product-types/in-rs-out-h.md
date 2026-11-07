---
type: Data Product Type
okf_version: '0.1'
timestamp: '2026-11-06T21:15:00Z'
description: Data product ingesting via request/response (on-demand query) + streaming (pub/sub feed) and serving via human.
title: 'Cell 4.15: live + lookup → human-only'
tags:
- data-product-type
- in-rs
- out-h
- common
related:
- /knowledge-concepts/pattern-request-response
- /knowledge-concepts/pattern-streaming
- /knowledge-concepts/pattern-human
- /knowledge-concepts/data-product
- /knowledge-concepts/verdict
---

# 4.15 — live + lookup → human-only

**Interface:** IN {R, S} → OUT {H}&emsp;&emsp;**Verdict:** common

A product that takes on-demand APIs and live streams and serves a human-facing surface (dashboard/report). Machine-side inputs ({R, S}) drive it — a report or dashboard is the product, not the pipe.

![Interface diagram: IN RS to OUT H](/assets/cells/in-rs-out-h.svg)

## When to use

The data the audience wants is real, but the reader is a person, not a service: they need a report or dashboard over a single leg of upstream APIs and a live feed, not raw events or a bulk drop.

## What's inside

- Ingest: a **poller/connector** over the upstream API (version anchor, pagination, retry) and a **stream consumer** (offsets, replay) for the live leg.
- Core: a **transform** (filter/shape/route) over the live leg
- Serve: a **human-facing surface** (dashboard, report, printout, or review screen) — the layer people actually read.
- State: a durable **state store** and the **feed log** (retention).

## State & cost

Dominated by the durable state store (grows with entity/state breadth). Serving people is cheap to run and cheap to trust — a presentation layer over a queryable backend.

## Watch out

- A human-facing surface inherits the state behind it: the report/dashboard carries every as-of and correctness rule of the store, and a person spots a stale number faster than an API client will.
- **Mixed time bases** in the inputs (live vs. poll/cycle/human): fix the authoritative as-of per surface, or each output looks correct alone and wrong cross-checked.
- This is machine-produced, human-read: make sure a person actually reviews/approves the served view rather than the pipeline writing it straight through.

## Typical next step

add **human curation on the input side** → cell [11.15](/data-product-types/in-rsh-out-h) when the data should not be purely machine-fed, add a **query API** → cell [4.13](/data-product-types/in-rs-out-rh), and add a **bulk file** → cell [4.14](/data-product-types/in-rs-out-bh); or the source world gains a leg this product does not yet take, and it migrates to a richer IN-state on the same row.

## Verdict

**common** — human-facing output (reports/dashboards) is among the most common ways people actually consume data, and its demand is real where this audience exists.

## Related

* [request/response](/knowledge-concepts/pattern-request-response)
* [streaming](/knowledge-concepts/pattern-streaming)
* [human](/knowledge-concepts/pattern-human)
* [data-product](/knowledge-concepts/data-product) — the overall model
* [verdict](/knowledge-concepts/verdict) — what the common / plausible / niche tag means
