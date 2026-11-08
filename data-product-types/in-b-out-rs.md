---
type: Data Product Type
okf_version: '0.1'
timestamp: '2026-11-08T19:24:00Z'
description: Data product ingesting via batch (bulk/file) and serving via request/response (on-demand query) + streaming (pub/sub feed) — batch → live query + pseudo-events.
definition: "Serve \"live\" over a nightly refresh: events (synthetic) + query API from batch inputs. A \"near-real-time\" facade over a batch source: a query API plus a synthetic change feed, both derived from the refresh. Both surfaces are as live as the load cycle allows."
example: "Consumers are online and events-only; the source is batch."
altLabel:
- "B → RS"
- "Cell 7.4"
- "Batch → live query + pseudo-events"
title: 'Cell 7.4: Batch → live query + pseudo-events'
tags:
- data-product-type
- in-b
- out-rs
- niche
related:
- /concepts/pattern-batch
- /concepts/pattern-request-response
- /concepts/pattern-streaming
- /concepts/synthetic-stream
- /concepts/data-product
---

# 7.4 — Batch → live query + pseudo-events

**Interface:** IN `{B}` → OUT `{R, S}`&emsp;&emsp;**Verdict:** niche

Serve "live" over a nightly refresh: events (synthetic) + query API from batch inputs. A "near-real-time" facade over a batch source: a query API plus a synthetic change feed, both derived from the refresh. Both surfaces are as live as the load cycle allows.

![Interface diagram: IN B to OUT RS](/assets/cells/821.svg)

## When to use

Consumers are online and events-only; the source is batch.

Chosen when consumers are online and change-reactive, but the upstream only ever publishes a scheduled file.

## What's inside

- Scheduled **ingest + load** into the state store.
- A **diff engine** (refresh N vs N-1) producing change events for the **producer** (synthetic feed).
- A **query service** over the store.
- State: store, diff baseline, feed log.

## State & cost

Store plus feed log plus diff baseline. The query store and the feed duplicate parts of the same data in different shapes — expect the combined footprint to be larger than either alone.

## Watch out

"Live" is an illusion — label it "as-of last refresh".

- Every event carries the poll-cycle timestamp, not a source event time — consumers building on "event time" will be wrong about freshness.
- The feed is a burst at refresh time, not a stream; burst-size and backpressure are contract, not implementation detail.

## Synthetic stream

This cell's stream **out** is not backed by a stream **in** — it is a **synthetic stream**: change-detection computed on top of a non-streaming source. The contract must pin down five things (see [synthetic stream](/concepts/synthetic-stream)):

1. **What counts as a "change"** — field-level, row version, or full snapshot?
2. **Latency bound** — bounded by the poll/refresh cadence, not the source's event time.
3. **Idempotency** — re-polling / re-loading must not duplicate events.
4. **Backfill semantics** — how history is (re)issued after a gap or correction.
5. **Ordering** — whether the stream preserves source ordering at all.

## Typical next step

Adding the file surface yields **cell 7.1** (the full batch platform); dropping the feed in favour of queries contracts to **7.6** or **7.2**. The durable escape route is a source-side upgrade — a real feed or API — which moves the product to row **3** or **4** and retires the diff machinery.

## Verdict

**niche** — plausible as a bridge to consumers who need push from a batch-only world; the synthetic-feed cost keeps it out of the "common" tier.

## Related

* [batch](/concepts/pattern-batch)
* [request/response](/concepts/pattern-request-response)
* [streaming](/concepts/pattern-streaming)
* [synthetic-stream](/concepts/synthetic-stream) — this cell's stream out is not backed by a stream in
* [data-product](/concepts/data-product) — the overall model
* [verdict](/concepts/verdict) — what the common / plausible / niche tag means
* [architectural paradigms](/concepts/architectural-paradigms) — this cell maps to: CDC (change data capture): a batch-refreshed store emits a synthetic stream + query API.
