---
type: Data Product Type
okf_version: '0.1'
timestamp: '2026-11-08T19:52:00Z'
definition: "Lives entirely on APIs + events; emits files, streams, and APIs — including bulk exports built from incremental change logs. The full MDM / integration hub: events and APIs in; files, stream, and API out. The feed-out is the interesting surface — it is a change feed derived from the hub's state, not a pass-through of the input stream."
example: "The product is the \"system-of-record glue\" (master data hub, order hub)."
altLabel:
- "RS → BRS"
- "Cell 4.1"
- "MDM / integration hub with full out"
title: 'Cell 4.1: MDM / integration hub with full out'
tags:
- data-product-type
- in-rs
- out-brs
- plausible
related:
- /concepts/pattern-batch
- /concepts/pattern-request-response
- /concepts/pattern-streaming
- /concepts/data-product
---

# 4.1 — MDM / integration hub with full out

**Interface:** IN `{R, S}` → OUT `{B, R, S}`&emsp;&emsp;**Verdict:** plausible

Lives entirely on APIs + events; emits files, streams, and APIs — including bulk exports built from incremental change logs. The full MDM / integration hub: events and APIs in; files, stream, and API out. The feed-out is the interesting surface — it is a change feed derived from the hub's state, not a pass-through of the input stream.

![Interface diagram: IN RS to OUT BRS](/assets/cells/128.svg)

## When to use

The product is the "system-of-record glue" (master data hub, order hub).

A system-of-record glue: master data or an order hub that publishes both the current state (API), the history (files), and the changes (a change feed) to a mixed consumer base.

## What's inside

- A **stream consumer** plus a **poller** feeding a **canonical store** (the system of record).
- A **change-capture layer** over the store (CDC-style) driving a **producer** for the change feed.
- A **query service** (R) and a **publication job** (B) over the store.
- State: the canonical store, the change log (feed), the reference anchor, and the last publication — the widest footprint of the row-4 cells.

## State & cost

Heaviest cell of row 4: canonical store plus a full change log plus artifacts, all maintained from two input legs. Justified only where all three consumer families are real — a full MDM — or several surfaces are dead weight.

## Watch out

Full-load exports need a complete state store — build it.

- The store must be complete for the B surface (full loads) and current for the R and S surfaces; a single projection failure degrades all three at once.
- The change feed is **derived from the store, not a raw pass-through** of the input stream: consumers who expect the input's ordering or idempotency on the output feed will find it re-keyed and re-sequenced by the hub's projection. (The feed is native — S is in IN — but it is *computed*, so its semantics are a contract, not an inheritance.)

## Typical next step

At this corner the pattern space is exhausted; growth is horizontal (domains, tenants, history) or an input-side maturation — a push feed replacing a polled leg, or files replacing events — that simplifies IN. The common contraction is dropping the change feed (the most expensive-to-trust surface), yielding **4.2**.

## Verdict

**plausible** — the canonical full MDM/integration hub — a plausible, defensible, but expensive shape, met where a mixed consumer base genuinely needs all three surfaces over one system of record.

## Related

* [batch](/concepts/pattern-batch)
* [request/response](/concepts/pattern-request-response)
* [streaming](/concepts/pattern-streaming)
* [data-product](/concepts/data-product) — the overall model
* [verdict](/concepts/verdict) — what the common / plausible / niche tag means
