---
type: Data Product Type
okf_version: '0.1'
timestamp: '2026-11-06T12:50:00Z'
description: Data product ingesting via batch (bulk/file) + request/response (on-demand query) + streaming (pub/sub feed) and serving via request/response (on-demand query) + streaming (pub/sub feed) — unified real-time view.
title: 'Cell 1.4: Unified real-time view'
tags:
- data-product-type
- in-brs
- out-rs
- common
related:
- /knowledge-concepts/pattern-batch
- /knowledge-concepts/pattern-request-response
- /knowledge-concepts/pattern-streaming
- /knowledge-concepts/data-product
---
# 1.4 — Unified real-time view

**Interface:** IN `{B, R, S}` → OUT `{R, S}`&emsp;&emsp;**Verdict:** common

Consumers query current state *and* subscribe to changes; no bulk files served. Historical depth is served by query, not by file.

## When to use

All consumers are online (e.g., an IoT/time-series platform with event + state APIs).

## Watch out

Long-term archive may still need an off-product cold tier to keep storage sane.

## Related

* [batch](/knowledge-concepts/pattern-batch)
* [request/response](/knowledge-concepts/pattern-request-response)
* [streaming](/knowledge-concepts/pattern-streaming)
* [data-product](/knowledge-concepts/data-product) — the overall model
* [verdict](/knowledge-concepts/verdict) — what the common / plausible / niche tag means

