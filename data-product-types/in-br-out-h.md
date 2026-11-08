---
type: Data Product Type
okf_version: '0.1'
timestamp: '2026-11-08T16:00:00Z'
description: Data product ingesting via batch (bulk/file) + request/response (on-demand query) and serving via human.
title: 'Cell 2.15: query + file → human-only'
tags:
- data-product-type
- in-br
- out-h
- common
related:
- /knowledge-concepts/pattern-batch
- /knowledge-concepts/pattern-request-response
- /knowledge-concepts/pattern-human
- /knowledge-concepts/data-product
- /knowledge-concepts/verdict
---

# 2.15 — query + file → human-only

**Interface:** IN {B, R} → OUT {H}&emsp;&emsp;**Verdict:** common

A product that takes files (batch) and on-demand APIs and serves a human-facing surface (dashboard/report). Machine-side inputs ({B, R}) drive it — a report or dashboard is the product, not the pipe.

![Interface diagram: IN BR to OUT H](/assets/cells/in-br-out-h.svg)

## When to use

The data the audience wants is real, but the reader is a person, not a service: they need a report or dashboard over a single leg of bulk files and upstream APIs, not raw events or a bulk drop.

## What's inside

- Ingest: a scheduled **bulk ingest** (pickup, parse, validate, load) and a **poller/connector** over the upstream API (version anchor, pagination, retry).
- Core: a **merge/normalisation core** unifying the non-streaming legs into one canonical view
- Serve: a **human-facing surface** (dashboard, report, printout, or review screen) — the layer people actually read.
- State: a durable **state store**.

## State & cost

Dominated by the durable state store (grows with entity/state breadth). Serving people is cheap to run and cheap to trust — a presentation layer over a queryable backend.

## Watch out

- A human-facing surface inherits the state behind it: the report/dashboard carries every as-of and correctness rule of the store, and a person spots a stale number faster than an API client will.
- This is machine-produced, human-read: make sure a person actually reviews/approves the served view rather than the pipeline writing it straight through.

## Typical next step

add **human curation on the input side** → cell [9.15](/data-product-types/in-bhr-out-h) when the data should not be purely machine-fed, add a **query API** → cell [2.13](/data-product-types/in-br-out-rh), and add a **bulk file** → cell [2.14](/data-product-types/in-br-out-bh); or the source world gains a leg this product does not yet take, and it migrates to a richer IN-state on the same row.

## Verdict

**common** — A product that ingests bulk files and query APIs and serves a human-facing surface (a report, dashboard, or shared record the same people maintain). It is the right shape where the reader is a person rather than a service, and the human-shaped view is itself what the next consumer — or the next machine in the loop — needs to act on.

## Related

* [batch](/knowledge-concepts/pattern-batch)
* [request/response](/knowledge-concepts/pattern-request-response)
* [human](/knowledge-concepts/pattern-human)
* [data-product](/knowledge-concepts/data-product) — the overall model
* [verdict](/knowledge-concepts/verdict) — what the common / plausible / niche tag means
