---
type: Data Product Type
okf_version: '0.1'
timestamp: '2026-11-08T19:52:00Z'
definition: "A product that takes files (batch) and serves bulk files, a live feed, and a human-facing surface (dashboard/report). Machine-side inputs ({B}) drive it — the multi-surface serves people, not just machines."
example: "The data the audience wants is real, but the reader is a person, not a service: they need a report or dashboard over a single leg of bulk files, not raw events or a bulk drop."
altLabel:
- "B → BHS"
- "Cell 7.10"
- "batch-only → file/stream + human"
title: 'Cell 7.10: batch-only → file/stream + human'
tags:
- data-product-type
- in-b
- out-bhs
- common
related:
- /concepts/pattern-batch
- /concepts/pattern-streaming
- /concepts/pattern-human
- /concepts/synthetic-stream
- /concepts/data-product
- /concepts/verdict
---

# 7.10 — batch-only → file/stream + human

**Interface:** IN {B} → OUT {B, S, H}&emsp;&emsp;**Verdict:** common

A product that takes files (batch) and serves bulk files, a live feed, and a human-facing surface (dashboard/report). Machine-side inputs ({B}) drive it — the multi-surface serves people, not just machines.

![Interface diagram: IN B to OUT BHS](/assets/cells/in-b-out-bhs.svg)

## When to use

The data the audience wants is real, but the reader is a person, not a service: they need a report or dashboard over a single leg of bulk files, not raw events or a bulk drop.

## What's inside

- Ingest: a scheduled **bulk ingest** (pickup, parse, validate, load).
- Core: a **change-detection engine** that manufactures the feed off the non-streaming inputs
- Serve: a **publication job** that materialises bulk artifacts (files/bundles) with a manifest and as-of, a **change-detection layer** diffing each refresh, driving a **producer** (a *synthetic* feed), and a **human-facing surface** (dashboard, report, printout, or review screen) — the layer people actually read.
- State: a durable **state store**, a **diff baseline**, the **feed log** (retention), and the **retained bulk artifacts**.

## State & cost

Dominated by the durable state store (grows with entity/state breadth), the diff baseline plus the manufactured feed's log, and the retained bulk artifacts.

## Watch out

- A human-facing surface inherits the state behind it: the report/dashboard carries every as-of and correctness rule of the store, and a person spots a stale number faster than an API client will.
- The **feed is synthetic** (S out, not in): "change" is a computed diff bounded by the refresh cadence — pin what counts as a change, idempotency, and backfill.
- A published file is a **completeness claim**: a manifest-first publish and a supersession rule belong in the contract.
- This is machine-produced, human-read: make sure a person actually reviews/approves the served view rather than the pipeline writing it straight through.

## Synthetic stream

This cell serves **S** without taking **S** as input, so its stream is a **synthetic stream**: change-detection computed on top of a non-streaming source. The contract must pin down the five items (see [synthetic stream](/concepts/synthetic-stream)):

1. **What counts as a "change"** — field-level, row version, or full snapshot?
2. **Latency bound** — bounded by the refresh cadence, not source event time.
3. **Idempotency** — re-polling / re-loading must not duplicate events.
4. **Backfill semantics** — how history is (re)issued after a gap or correction.
5. **Ordering** — whether the stream preserves source ordering at all.

## Typical next step

add **human curation on the input side** → cell [14.10](/data-product-types/in-bh-out-bhs) when the data should not be purely machine-fed and add a **query API** → cell [7.8](/data-product-types/in-b-out-brsh); or the source world gains a leg this product does not yet take, and it migrates to a richer IN-state on the same row.

## Verdict

**common** — A product that ingests bulk files and serves bulk files and live feeds plus a human-facing surface (a dashboard, report, or review). It is the right shape where the reader is a person rather than a service, and the human-shaped view is itself what the next consumer — or the next machine in the loop — needs to act on.

## Related

* [batch](/concepts/pattern-batch)
* [streaming](/concepts/pattern-streaming)
* [human](/concepts/pattern-human)
* [synthetic stream](/concepts/synthetic-stream) — the pseudo-stream hazard
* [data-product](/concepts/data-product) — the overall model
* [verdict](/concepts/verdict) — what the common / plausible / niche tag means
