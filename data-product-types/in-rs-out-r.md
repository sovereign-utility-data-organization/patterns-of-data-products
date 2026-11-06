---
type: Data Product Type
okf_version: '0.1'
timestamp: '2026-11-06T12:50:00Z'
description: Data product ingesting via request/response (on-demand query) + streaming (pub/sub feed) and serving via request/response (on-demand query) — event-sourced query service (cqrs).
title: 'Cell 4.6: Event-sourced query service (CQRS)'
tags:
- data-product-type
- in-rs
- out-r
- common
related:
- /knowledge-concepts/pattern-request-response
- /knowledge-concepts/pattern-streaming
- /knowledge-concepts/data-product
---
# 4.6 — Event-sourced query service (CQRS)

**Interface:** IN `{R, S}` → OUT `{R}`&emsp;&emsp;**Verdict:** common

Ingest the stream, build the read model, serve the API — the canonical event-sourcing read side (e.g., an order-status API from order events + master data APIs). A "stream → state" product.

![Interface diagram: IN RS to OUT R](/assets/cells/1036.svg)

## When to use

Consumers don't want to consume a stream; they want the answer.

## Related

* [request/response](/knowledge-concepts/pattern-request-response)
* [streaming](/knowledge-concepts/pattern-streaming)
* [data-product](/knowledge-concepts/data-product) — the overall model
* [verdict](/knowledge-concepts/verdict) — what the common / plausible / niche tag means

