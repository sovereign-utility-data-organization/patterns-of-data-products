---
type: Data Product Type
okf_version: '0.1'
timestamp: '2026-11-06T12:50:00Z'
description: Data product ingesting via batch (bulk/file) and serving via batch (bulk/file) + request/response (on-demand query) + streaming (pub/sub feed) — batch-loaded platform with all out.
title: 'Cell 7.1: Batch-loaded platform with all out'
tags:
- data-product-type
- in-b
- out-brs
- plausible
related:
- /knowledge-concepts/pattern-batch
- /knowledge-concepts/pattern-request-response
- /knowledge-concepts/pattern-streaming
- /knowledge-concepts/synthetic-stream
- /knowledge-concepts/data-product
---
# 7.1 — Batch-loaded platform with all out

**Interface:** IN `{B}` → OUT `{B, R, S}`&emsp;&emsp;**Verdict:** plausible

A nightly-loaded warehouse that also serves a (CDC or refresh-derived) stream + API + files.

## When to use

Full consumer mix is needed, but the source world is batch-only.

## Watch out

The "stream out" is synthetic (CDC on a refreshed table) — make the semantics explicit.

## Related

* [batch](/knowledge-concepts/pattern-batch)
* [request/response](/knowledge-concepts/pattern-request-response)
* [streaming](/knowledge-concepts/pattern-streaming)
* [synthetic-stream](/knowledge-concepts/synthetic-stream) — this cell's stream out is not backed by a stream in
* [data-product](/knowledge-concepts/data-product) — the overall model
* [verdict](/knowledge-concepts/verdict) — what the common / plausible / niche tag means

