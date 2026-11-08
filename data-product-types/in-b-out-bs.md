---
type: Data Product Type
okf_version: '0.1'
timestamp: '2026-11-08T19:52:00Z'
definition: "Nightly load + a stream out (CDC from the refreshed table — a pseudo-stream). Stream plus file out, batch in: a settlement-and-feed hybrid where the feed is a synthetic stream over the refresh. The \"hot\" surface (the feed) is actually a diff, and the \"cold\" surface (the file) is a full snapshot."
example: "Consumers want to react to change but the upstream only publishes files."
altLabel:
- "B → BS"
- "Cell 7.3"
- "Batch data, stream + files out"
title: 'Cell 7.3: Batch data, stream + files out'
tags:
- data-product-type
- in-b
- out-bs
- niche
related:
- /concepts/pattern-batch
- /concepts/pattern-streaming
- /concepts/synthetic-stream
- /concepts/data-product
---

# 7.3 — Batch data, stream + files out

**Interface:** IN `{B}` → OUT `{B, S}`&emsp;&emsp;**Verdict:** niche

Nightly load + a stream out (CDC from the refreshed table — a pseudo-stream). Stream plus file out, batch in: a settlement-and-feed hybrid where the feed is a synthetic stream over the refresh. The "hot" surface (the feed) is actually a diff, and the "cold" surface (the file) is a full snapshot.

![Interface diagram: IN B to OUT BS](/assets/cells/658.svg)

## When to use

Consumers want to react to change but the upstream only publishes files.

A utility settlement case: an interval file in; settlement files and a "live" change feed out — where the feed must exist even though the source is batch.

## What's inside

- Scheduled **ingest + transform** into a state store.
- A **diff engine** over successive refreshes driving a **producer** (the synthetic feed).
- A **publication job** for the files.
- State: store, diff baseline, feed log, last artifact.

## State & cost

Close to 7.1's cost profile but without the query store if the API is absent or thin: store plus feed log plus artifacts still dominates. The diff baseline must be retained — it is the anchor for idempotent re-emission.

## Watch out

Latency = batch cadence; document clearly.

- Feed consumers will assume continuous delivery; in reality events arrive in bursts at refresh time. Backpressure and burst handling belong in the contract.
- The file and the feed describe the same data at different granularities; a consumer joining both must know the feed is a delta, not a full state.

## Synthetic stream

This cell's stream **out** is not backed by a stream **in** — it is a **synthetic stream**: change-detection computed on top of a non-streaming source. The contract must pin down five things (see [synthetic stream](/concepts/synthetic-stream)):

1. **What counts as a "change"** — field-level, row version, or full snapshot?
2. **Latency bound** — bounded by the poll/refresh cadence, not the source's event time.
3. **Idempotency** — re-polling / re-loading must not duplicate events.
4. **Backfill semantics** — how history is (re)issued after a gap or correction.
5. **Ordering** — whether the stream preserves source ordering at all.

## Typical next step

Typical growth is the missing online surface: adding the query API yields **cell 7.1** (the full platform) or, if the feed is dropped in favour of queries, **7.2**. A push feed from the source world collapses the synthetic machinery and migrates the product toward row **3** or **4**.

## Verdict

**niche** — plausible where a regulated consumer needs both a file and a push surface from a batch source — the cost of the synthetic feed is the price of that bridge.

## Related

* [batch](/concepts/pattern-batch)
* [streaming](/concepts/pattern-streaming)
* [synthetic-stream](/concepts/synthetic-stream) — this cell's stream out is not backed by a stream in
* [data-product](/concepts/data-product) — the overall model
* [verdict](/concepts/verdict) — what the common / plausible / niche tag means
* [architectural paradigms](/concepts/architectural-paradigms) — this cell maps to: CDC (change data capture): a batch-refreshed store emits a synthetic stream + archive.
