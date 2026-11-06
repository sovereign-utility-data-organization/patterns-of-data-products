---
type: Data Product Type
okf_version: '0.1'
timestamp: '2026-11-06T12:50:00Z'
description: Data product ingesting via request/response (on-demand query) and serving via streaming (pub/sub feed) — poller → stream bridge.
title: 'Cell 6.5: Poller → stream bridge'
tags:
- data-product-type
- in-r
- out-s
- niche
related:
- /knowledge-concepts/pattern-request-response
- /knowledge-concepts/pattern-streaming
- /knowledge-concepts/synthetic-stream
- /knowledge-concepts/data-product
---
# 6.5 — Poller → stream bridge

**Interface:** IN `{R}` → OUT `{S}`&emsp;&emsp;**Verdict:** niche

The canonical "bridge an API world into a Kafka world" product.

![Interface diagram: IN R to OUT S](/assets/cells/932.svg)

## When to use

A stream-driven consumer architecture with only file/API sources.

## Watch out

The most common source of "why is my stream lagging" complaints — define poll interval, idempotency, and backfill explicitly.

## Related

* [request/response](/knowledge-concepts/pattern-request-response)
* [streaming](/knowledge-concepts/pattern-streaming)
* [synthetic-stream](/knowledge-concepts/synthetic-stream) — this cell's stream out is not backed by a stream in
* [data-product](/knowledge-concepts/data-product) — the overall model
* [verdict](/knowledge-concepts/verdict) — what the common / plausible / niche tag means

