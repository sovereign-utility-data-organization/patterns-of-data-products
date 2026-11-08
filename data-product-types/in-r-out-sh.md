---
type: Data Product Type
okf_version: '0.1'
timestamp: '2026-11-08T19:24:00Z'
description: Data product ingesting via request/response (on-demand query) and serving via streaming (pub/sub feed) + human.
definition: "A product that takes on-demand APIs and serves a live feed and a human-facing surface (dashboard/report). Machine-side inputs ({R}) drive it — the multi-surface serves people, not just machines."
example: "The data the audience wants is real, but the reader is a person, not a service: they need a report or dashboard over a single leg of upstream APIs, not raw events or a bulk drop."
altLabel:
- "R → SH"
- "Cell 6.12"
- "request-response-only → stream + human"
title: 'Cell 6.12: request-response-only → stream + human'
tags:
- data-product-type
- in-r
- out-sh
- common
related:
- /concepts/pattern-request-response
- /concepts/pattern-streaming
- /concepts/pattern-human
- /concepts/synthetic-stream
- /concepts/data-product
- /concepts/verdict
---

# 6.12 — request-response-only → stream + human

**Interface:** IN {R} → OUT {S, H}&emsp;&emsp;**Verdict:** common

A product that takes on-demand APIs and serves a live feed and a human-facing surface (dashboard/report). Machine-side inputs ({R}) drive it — the multi-surface serves people, not just machines.

![Interface diagram: IN R to OUT SH](/assets/cells/in-r-out-sh.svg)

## When to use

The data the audience wants is real, but the reader is a person, not a service: they need a report or dashboard over a single leg of upstream APIs, not raw events or a bulk drop.

## What's inside

- Ingest: a **poller/connector** over the upstream API (version anchor, pagination, retry).
- Core: a **change-detection engine** that manufactures the feed off the non-streaming inputs
- Serve: a **change-detection layer** diffing each refresh, driving a **producer** (a *synthetic* feed) and a **human-facing surface** (dashboard, report, printout, or review screen) — the layer people actually read.
- State: a durable **state store**, a **diff baseline**, and the **feed log** (retention).

## State & cost

Dominated by the durable state store (grows with entity/state breadth) and the diff baseline plus the manufactured feed's log.

## Watch out

- A human-facing surface inherits the state behind it: the report/dashboard carries every as-of and correctness rule of the store, and a person spots a stale number faster than an API client will.
- The **feed is synthetic** (S out, not in): "change" is a computed diff bounded by the refresh cadence — pin what counts as a change, idempotency, and backfill.
- This is machine-produced, human-read: make sure a person actually reviews/approves the served view rather than the pipeline writing it straight through.

## Synthetic stream

This cell serves **S** without taking **S** as input, so its stream is a **synthetic stream**: change-detection computed on top of a non-streaming source. The contract must pin down the five items (see [synthetic stream](/concepts/synthetic-stream)):

1. **What counts as a "change"** — field-level, row version, or full snapshot?
2. **Latency bound** — bounded by the refresh cadence, not source event time.
3. **Idempotency** — re-polling / re-loading must not duplicate events.
4. **Backfill semantics** — how history is (re)issued after a gap or correction.
5. **Ordering** — whether the stream preserves source ordering at all.

## Typical next step

add **human curation on the input side** → cell [13.12](/data-product-types/in-rh-out-sh) when the data should not be purely machine-fed, add a **query API** → cell [6.11](/data-product-types/in-r-out-rsh), and add a **bulk file** → cell [6.10](/data-product-types/in-r-out-bhs); or the source world gains a leg this product does not yet take, and it migrates to a richer IN-state on the same row.

## Verdict

**common** — A product that ingests query APIs and serves live feeds plus a human-facing surface (a dashboard, report, or review). It is the right shape where the reader is a person rather than a service, and the human-shaped view is itself what the next consumer — or the next machine in the loop — needs to act on.

## Related

* [request/response](/concepts/pattern-request-response)
* [streaming](/concepts/pattern-streaming)
* [human](/concepts/pattern-human)
* [synthetic stream](/concepts/synthetic-stream) — the pseudo-stream hazard
* [data-product](/concepts/data-product) — the overall model
* [verdict](/concepts/verdict) — what the common / plausible / niche tag means
