---
type: Data Product Type
okf_version: '0.1'
timestamp: '2026-11-06T12:50:00Z'
description: Data product ingesting via streaming (pub/sub feed) and serving via request/response (on-demand query) — event-sourced read model.
title: 'Cell 5.6: Event-sourced read model'
tags:
- data-product-type
- in-s
- out-r
- common
related:
- /knowledge-concepts/pattern-request-response
- /knowledge-concepts/pattern-streaming
- /knowledge-concepts/data-product
---
# 5.6 — Event-sourced read model

**Interface:** IN `{S}` → OUT `{R}`&emsp;&emsp;**Verdict:** common

Events in → state out via API (order status, device state, meter state APIs). A special case of the "stream → lake + API" type without the file side.

## When to use

Consumers don't want to consume a stream; they want the answer.

## Related

* [request/response](/knowledge-concepts/pattern-request-response)
* [streaming](/knowledge-concepts/pattern-streaming)
* [data-product](/knowledge-concepts/data-product) — the overall model
* [verdict](/knowledge-concepts/verdict) — what the common / plausible / niche tag means

