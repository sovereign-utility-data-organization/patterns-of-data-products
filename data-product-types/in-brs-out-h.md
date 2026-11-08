---
type: Data Product Type
okf_version: '0.1'
timestamp: '2026-11-08T19:52:00Z'
definition: "A product that takes files (batch), on-demand APIs, and live streams and serves a human-facing surface (dashboard/report). Machine-side inputs ({B, R, S}) drive it — a report or dashboard is the product, not the pipe."
example: "The data the audience wants is real, but the reader is a person, not a service: they need a report or dashboard over live data, upstream APIs, and bulk files, not raw events or a bulk drop."
altLabel:
- "BRS → H"
- "Cell 1.15"
- "omni-channel → human-only"
title: 'Cell 1.15: omni-channel → human-only'
tags:
- data-product-type
- in-brs
- out-h
- common
related:
- /concepts/pattern-batch
- /concepts/pattern-request-response
- /concepts/pattern-streaming
- /concepts/pattern-human
- /concepts/data-product
- /concepts/verdict
---

# 1.15 — omni-channel → human-only

**Interface:** IN {B, R, S} → OUT {H}&emsp;&emsp;**Verdict:** common

A product that takes files (batch), on-demand APIs, and live streams and serves a human-facing surface (dashboard/report). Machine-side inputs ({B, R, S}) drive it — a report or dashboard is the product, not the pipe.

![Interface diagram: IN BRS to OUT H](/assets/cells/in-brs-out-h.svg)

## When to use

The data the audience wants is real, but the reader is a person, not a service: they need a report or dashboard over live data, upstream APIs, and bulk files, not raw events or a bulk drop.

## What's inside

- Ingest: a scheduled **bulk ingest** (pickup, parse, validate, load), a **poller/connector** over the upstream API (version anchor, pagination, retry), and a **stream consumer** (offsets, replay) for the live leg.
- Core: a **transform** (filter/shape/route) over the live leg and a **merge/normalisation core** unifying the non-streaming legs into one canonical view
- Serve: a **human-facing surface** (dashboard, report, printout, or review screen) — the layer people actually read.
- State: a durable **state store** and the **feed log** (retention).

## State & cost

Dominated by the durable state store (grows with entity/state breadth). Serving people is cheap to run and cheap to trust — a presentation layer over a queryable backend.

## Watch out

- A human-facing surface inherits the state behind it: the report/dashboard carries every as-of and correctness rule of the store, and a person spots a stale number faster than an API client will.
- **Mixed time bases** in the inputs (live vs. poll/cycle/human): fix the authoritative as-of per surface, or each output looks correct alone and wrong cross-checked.
- This is machine-produced, human-read: make sure a person actually reviews/approves the served view rather than the pipeline writing it straight through.

## Typical next step

add **human curation on the input side** → cell [8.15](/data-product-types/in-brsh-out-h) when the data should not be purely machine-fed, add a **query API** → cell [1.13](/data-product-types/in-brs-out-rh), and add a **bulk file** → cell [1.14](/data-product-types/in-brs-out-bh); or the source world gains a leg this product does not yet take, and it migrates to a richer IN-state on the same row.

## Verdict

**common** — A product that ingests bulk files, query APIs, and live feeds and serves a human-facing surface (a report, dashboard, or shared record the same people maintain). It is the right shape where the reader is a person rather than a service, and the human-shaped view is itself what the next consumer — or the next machine in the loop — needs to act on.

## Related

* [batch](/concepts/pattern-batch)
* [request/response](/concepts/pattern-request-response)
* [streaming](/concepts/pattern-streaming)
* [human](/concepts/pattern-human)
* [data-product](/concepts/data-product) — the overall model
* [verdict](/concepts/verdict) — what the common / plausible / niche tag means
