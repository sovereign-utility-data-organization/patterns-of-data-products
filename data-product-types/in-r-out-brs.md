---
type: Data Product Type
okf_version: '0.1'
timestamp: '2026-11-06T12:50:00Z'
description: Data product ingesting via request/response (on-demand query) and serving via batch (bulk/file) + request/response (on-demand query) + streaming (pub/sub feed) — polling facade with synthetic stream.
title: 'Cell 6.1: Polling facade with synthetic stream'
tags:
- data-product-type
- in-r
- out-brs
- niche
related:
- /knowledge-concepts/pattern-batch
- /knowledge-concepts/pattern-request-response
- /knowledge-concepts/pattern-streaming
- /knowledge-concepts/synthetic-stream
- /knowledge-concepts/data-product
---# 6.1 — Polling facade with synthetic stream

**Interface:** IN `{R}` → OUT `{B, R, S}`&emsp;&emsp;**Verdict:** niche

Polls upstream, computes deltas, serves file + API + a *synthetic* change stream.

## When to use

The source world is file/API-only and downstream is event-driven.

## Watch out

The product owns change-detection semantics + backfill rules; the "stream" is an illusion over polling cadence.

## Related

* [batch](/knowledge-concepts/pattern-batch)
* [request/response](/knowledge-concepts/pattern-request-response)
* [streaming](/knowledge-concepts/pattern-streaming)
* [synthetic-stream](/knowledge-concepts/synthetic-stream) — this cell's stream out is not backed by a stream in
* [data-product](/knowledge-concepts/data-product) — the overall model

