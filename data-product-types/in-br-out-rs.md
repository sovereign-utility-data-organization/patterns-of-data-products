---
type: Data Product Type
okf_version: "0.1"
timestamp: 2026-11-06T12:50:00Z
description: Data product ingesting via batch (bulk/file) + request/response (on-demand query) and serving via request/response (on-demand query) + streaming (pub/sub feed) — poll/file-derived live + query.
title: Cell 2.4: Poll/file-derived live + query
tags:
  - data-product-type
  - in-br
  - out-rs
  - niche
related:

  - /knowledge-concepts/pattern-batch
  - /knowledge-concepts/pattern-request-response
  - /knowledge-concepts/pattern-streaming
  - /knowledge-concepts/synthetic-stream
  - /knowledge-concepts/data-product
---
# 2.4 — Poll/file-derived live + query

**Interface:** IN `{B, R}` → OUT `{R, S}`&emsp;&emsp;**Verdict:** niche

Stream + query API built on polled/file inputs.

## When to use

A dashboard wants "live" data but the only source is scheduled polls (device registries, market pages).

## Watch out

Every data point must carry a freshness stamp; polling latency is the truth.

## Related

* [batch](/knowledge-concepts/pattern-batch)
* [request/response](/knowledge-concepts/pattern-request-response)
* [streaming](/knowledge-concepts/pattern-streaming)
* [synthetic-stream](/knowledge-concepts/synthetic-stream) — this cell's stream out is not backed by a stream in
* [data-product](/knowledge-concepts/data-product) — the overall model

