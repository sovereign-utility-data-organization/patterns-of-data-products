---
type: Data Product Type
okf_version: "0.1"
timestamp: 2026-11-06T12:50:00Z
description: Data product ingesting via request/response (on-demand query) + streaming (pub/sub feed) and serving via streaming (pub/sub feed) — api-backed fan-out stream.
title: Cell 4.5: API-backed fan-out stream
tags:
  - data-product-type
  - in-rs
  - out-s
  - niche
related:

  - /knowledge-concepts/pattern-request-response
  - /knowledge-concepts/pattern-streaming
  - /knowledge-concepts/data-product
---
# 4.5 — API-backed fan-out stream

**Interface:** IN `{R, S}` → OUT `{S}`&emsp;&emsp;**Verdict:** niche

Changes (computed from event + API state) fanned out as one stream.

## When to use

Downstream is stream-first; the stream *is* the product.

## Watch out

API-polled changes become synthetic events — define exactly what "change" means (field-level? version bump?).

## Related

* [request/response](/knowledge-concepts/pattern-request-response)
* [streaming](/knowledge-concepts/pattern-streaming)
* [data-product](/knowledge-concepts/data-product) — the overall model

