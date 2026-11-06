---
type: Data Product Type
okf_version: '0.1'
timestamp: '2026-11-06T12:50:00Z'
description: Data product ingesting via request/response (on-demand query) and serving via request/response (on-demand query) + streaming (pub/sub feed) — poll-derived live + query.
title: 'Cell 6.4: Poll-derived live + query'
tags:
- data-product-type
- in-r
- out-rs
- niche
related:
- /knowledge-concepts/pattern-request-response
- /knowledge-concepts/pattern-streaming
- /knowledge-concepts/synthetic-stream
- /knowledge-concepts/data-product
---# 6.4 — Poll-derived live + query

**Interface:** IN `{R}` → OUT `{R, S}`&emsp;&emsp;**Verdict:** niche

API poll in, live feed + API out. "Live" over a polled world.

## When to use

Consumers want push + query, the only source is pollable.

## Watch out

Latency bounded by poll cadence; freshness stamps required.

## Related

* [request/response](/knowledge-concepts/pattern-request-response)
* [streaming](/knowledge-concepts/pattern-streaming)
* [synthetic-stream](/knowledge-concepts/synthetic-stream) — this cell's stream out is not backed by a stream in
* [data-product](/knowledge-concepts/data-product) — the overall model

