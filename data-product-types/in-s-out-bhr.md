---
type: Data Product Type
okf_version: '0.1'
timestamp: '2026-11-08T16:00:00Z'
description: Data product ingesting via streaming (pub/sub feed) and serving via batch (bulk/file) + request/response (on-demand query) + human.
title: 'Cell 5.9: stream-only → file/API + human'
tags:
- data-product-type
- in-s
- out-bhr
- common
related:
- /concepts/pattern-batch
- /concepts/pattern-request-response
- /concepts/pattern-streaming
- /concepts/pattern-human
- /concepts/data-product
- /concepts/verdict
---

# 5.9 — stream-only → file/API + human

**Interface:** IN {S} → OUT {B, R, H}&emsp;&emsp;**Verdict:** common

A product that takes live streams and serves bulk files, a query API, and a human-facing surface (dashboard/report). Machine-side inputs ({S}) drive it — the multi-surface serves people, not just machines.

![Interface diagram: IN S to OUT BHR](/assets/cells/in-s-out-bhr.svg)

## When to use

The data the audience wants is real, but the reader is a person, not a service: they need a report or dashboard over a single leg of a live feed, not raw events or a bulk drop.

## What's inside

- Ingest: a **stream consumer** (offsets, replay) for the live leg.
- Core: a **fold/aggregation core** that folds the live leg into queryable state or windowed files
- Serve: a **publication job** that materialises bulk artifacts (files/bundles) with a manifest and as-of, a **query service** (the API surface) over the state store, and a **human-facing surface** (dashboard, report, printout, or review screen) — the layer people actually read.
- State: a durable **state store**, the **feed log** (retention), and the **retained bulk artifacts**.

## State & cost

Dominated by the durable state store (grows with entity/state breadth) and the retained bulk artifacts.

## Watch out

- A human-facing surface inherits the state behind it: the report/dashboard carries every as-of and correctness rule of the store, and a person spots a stale number faster than an API client will.
- Late and out-of-order events are a **first-class** question: a watermark and a re-issue/correction rule, or history gains holes and duplicate facts.
- This is machine-produced, human-read: make sure a person actually reviews/approves the served view rather than the pipeline writing it straight through.

## Typical next step

add **human curation on the input side** → cell [12.9](/data-product-types/in-sh-out-bhr) when the data should not be purely machine-fed and add a **feed** → cell [5.8](/data-product-types/in-s-out-brsh); or the source world gains a leg this product does not yet take, and it migrates to a richer IN-state on the same row.

## Verdict

**common** — A product that ingests live feeds and serves bulk files and query APIs plus a human-facing surface (a dashboard, report, or review). It is the right shape where the reader is a person rather than a service, and the human-shaped view is itself what the next consumer — or the next machine in the loop — needs to act on.

## Related

* [batch](/concepts/pattern-batch)
* [request/response](/concepts/pattern-request-response)
* [streaming](/concepts/pattern-streaming)
* [human](/concepts/pattern-human)
* [data-product](/concepts/data-product) — the overall model
* [verdict](/concepts/verdict) — what the common / plausible / niche tag means
