---
type: Data Product Type
okf_version: '0.1'
timestamp: '2026-11-08T19:52:00Z'
definition: "Ingest the stream, build the read model, serve the API — the canonical event-sourcing read side (e.g., an order-status API from order events + master data APIs). A \"stream → state\" product. The canonical event-sourced query service (CQRS): events and a context API in, one query API out. The product is the read model plus the API over it — the write side is upstream, and there is no feed or file out."
example: "an order-status API from order events + master data APIs"
altLabel:
- "RS → R"
- "Cell 4.6"
- "Event-sourced query service (CQRS)"
title: 'Cell 4.6: Event-sourced query service (CQRS)'
tags:
- data-product-type
- in-rs
- out-r
- common
related:
- /concepts/pattern-request-response
- /concepts/pattern-streaming
- /concepts/data-product
---

# 4.6 — Event-sourced query service (CQRS)

**Interface:** IN `{R, S}` → OUT `{R}`&emsp;&emsp;**Verdict:** common

Ingest the stream, build the read model, serve the API — the canonical event-sourcing read side (e.g., an order-status API from order events + master data APIs). A "stream → state" product. The canonical event-sourced query service (CQRS): events and a context API in, one query API out. The product is the read model plus the API over it — the write side is upstream, and there is no feed or file out.

![Interface diagram: IN RS to OUT R](/assets/cells/1036.svg)

## When to use

Consumers don't want to consume a stream; they want the answer.

When consumers want the answer and not the feed — an order-status API over order events plus master-data APIs, a device-state API over device events plus a registry.

## What's inside

- A **stream consumer** (offsets) plus a **poller** (context anchor) feeding a **read-model store**.
- A **projection/fold** that merges the live events and the polled context (the join is the heart of the product).
- A **query service** (the sole surface) with auth, pagination, and versioning.
- State: the read-model store, the context anchor/last-fetch, and the consumer offsets.

## State & cost

Bounded by entity count, not event volume — a fold, not a log — so the state cost is predictable and modest. The context cache is small. No feed, no artifacts: the lightest durable cell in row 4, and often the cheapest way to expose a live world as a query.

## Watch out

- The join between the live and the polled context is the core correctness risk: which context version a given event carries is a decision, and a stale context bound produces subtly wrong query results that are hard to attribute.
- Projection bugs rewrite the read model silently — keep the log replayable and the projection independently testable; a bad fold is a data incident, not a bad request.

## Typical next step

Growth is adding surfaces: a change feed for reactive consumers — **cell 4.5** or **4.4**; files for settlement/reporting — **4.2**. A file leg replacing the polled context broadens IN toward **row 3** (the 3.6 historian shape is the classic destination). This cell is the row's default starting point and where most CQRS read sides live.

## Verdict

**common** — the default "stream to query" product — the canonical CQRS read side, and the cheapest way to give a live, event-based world a stable query surface.

## Related

* [request/response](/concepts/pattern-request-response)
* [streaming](/concepts/pattern-streaming)
* [data-product](/concepts/data-product) — the overall model
* [verdict](/concepts/verdict) — what the common / plausible / niche tag means
