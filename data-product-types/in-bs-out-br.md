---
type: Data Product Type
okf_version: '0.1'
timestamp: '2026-11-06T18:30:00Z'
description: Data product ingesting via batch (bulk/file) + streaming (pub/sub feed) and serving via batch (bulk/file) + request/response (on-demand query) — smart-meter platform shape.
title: 'Cell 3.2: Smart-meter platform shape'
tags:
- data-product-type
- in-bs
- out-br
- common
related:
- /concepts/pattern-batch
- /concepts/pattern-request-response
- /concepts/pattern-streaming
- /concepts/data-product
---

# 3.2 — Smart-meter platform shape

**Interface:** IN `{B, S}` → OUT `{B, R}`&emsp;&emsp;**Verdict:** common

Live meter events + tariff reference (batch) in → reading API + settlement files out. The common utility shape; consumers pull, no pure stream out. A smart-meter platform: live meter stream plus batch tariff in; a readings API plus settlement files out. The product serves online consumers (the API) and bulk consumers (the files) from one metered world.

![Interface diagram: IN BS to OUT BR](/assets/cells/334.svg)

## When to use

Utility/energy domain: metered streams plus reference files, served to both online and bulk consumers.

The utility/energy shape: metered events and a tariff/master reference in; a readings/current-state API and settlement or interval files out.

## What's inside

- A **stream consumer** (offsets) for the metered events, plus a **batch loader** for the tariff/master reference.
- A **readings store** (per-meter current/latched readings) plus a **windowed accumulator** for settlement.
- A **query service** (the readings API) and a **publication job** (settlement/interval files) over the same store.
- State: the readings store, the open settlement accumulators, the loaded reference, and the published files.

## State & cost

The readings store grows with the meter base times the readings retained — a large but predictable state. Settlement accumulators are bounded by the cycle. Reference and files add retention. Heavier than a 3.7 (the readings store for the API) and lighter than a 3.2's full query platform.

## Watch out

- The API and the files must agree on the same metered interval or consumers will reconcile against each other and find a discrepancy — derive both from the same committed store.
- Late meter data affects both the current-state API (a latch correction) and the settlement file (a re-open); the two correction paths must be consistent or the API and the file will disagree.

## Typical next step

Growth is adding the live surface: a change/reaction consumer appears and the meter stream is re-exposed — **cell 3.3** or **3.5**; a query platform beyond readings appears — **3.6**. A live reference (API) replaces the batch tariff and the product moves to **row 4** (the 4.2/4.7 shapes). This is a stable, mature utility platform cell.

## Verdict

**common** — the canonical smart-meter platform — a common, defensible shape serving both online and bulk consumers from a live-plus-batch metered source.

## Related

* [batch](/concepts/pattern-batch)
* [request/response](/concepts/pattern-request-response)
* [streaming](/concepts/pattern-streaming)
* [data-product](/concepts/data-product) — the overall model
* [verdict](/concepts/verdict) — what the common / plausible / niche tag means
