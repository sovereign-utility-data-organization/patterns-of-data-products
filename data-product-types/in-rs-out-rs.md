---
type: Data Product Type
okf_version: '0.1'
timestamp: '2026-11-08T19:24:00Z'
description: Data product ingesting via request/response (on-demand query) + streaming (pub/sub feed) and serving via request/response (on-demand query) + streaming (pub/sub feed) — unified live view.
definition: "A clean real-time façade: one stream + one query API over the combined inputs. A unified real-time view: events and a context API in; query and feed out; no files. The product serves the two live surfaces — the current state and the stream of changes — and nothing else."
example: "All consumers are online and a single consistent contract is wanted (unified telemetry/asset platform)."
altLabel:
- "RS → RS"
- "Cell 4.4"
- "Unified live view"
title: 'Cell 4.4: Unified live view'
tags:
- data-product-type
- in-rs
- out-rs
- common
related:
- /concepts/pattern-request-response
- /concepts/pattern-streaming
- /concepts/data-product
---

# 4.4 — Unified live view

**Interface:** IN `{R, S}` → OUT `{R, S}`&emsp;&emsp;**Verdict:** common

A clean real-time façade: one stream + one query API over the combined inputs. A unified real-time view: events and a context API in; query and feed out; no files. The product serves the two live surfaces — the current state and the stream of changes — and nothing else.

![Interface diagram: IN RS to OUT RS](/assets/cells/768.svg)

## When to use

All consumers are online and a single consistent contract is wanted (unified telemetry/asset platform).

When all consumers are online — they both query current state and subscribe to change — and long-term bulk is handled elsewhere (a warehouse, a separate archive product).

## What's inside

- A **stream consumer** (offsets) plus a **poller** (context anchor) feeding a **state store**.
- A **projection/fold** producing both the queryable state and the change events (one source of truth for R and S).
- A **query service** (R) and a **producer** for the change feed (S).
- State: the state store, the change feed log, the context anchor, and the offsets.

## State & cost

The state store plus feed-log retention dominate, with a small context cache. Heavier than a 4.6 (the feed log) and lighter than a 4.1/4.3 (no artifacts). Justified when both live surfaces are real and files are genuinely out of scope.

## Watch out

- The feed is derived from the state, not a raw pass-through: consumers who expect the input stream's ordering, granularity, or idempotency will find the output feed re-keyed and re-sequenced.
- With no file surface there is no artifact anchor for durability or reconciliation — the state store and the feed log are the only recovery paths, and both must be retained on purpose.

## Typical next step

The natural addition is the file surface: bulk/settlement or audit consumers appear and files are added — **cell 4.3** (feed + files) or **4.2** (hub). A reference leg (file) replacing the polled context broadens IN toward **row 3** (the 3.6/3.4 shapes).

## Verdict

**common** — a clean, defensible real-time view — the common answer when both query and feed consumers live online and files are explicitly out of scope.

## Related

* [request/response](/concepts/pattern-request-response)
* [streaming](/concepts/pattern-streaming)
* [data-product](/concepts/data-product) — the overall model
* [verdict](/concepts/verdict) — what the common / plausible / niche tag means
