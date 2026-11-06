---
type: Data Product Type
okf_version: '0.1'
timestamp: '2026-11-06T12:50:00Z'
description: Data product ingesting via batch (bulk/file) and serving via request/response (on-demand query) + streaming (pub/sub feed) — batch → live query + pseudo-events.
title: 'Cell 7.4: Batch → live query + pseudo-events'
tags:
- data-product-type
- in-b
- out-rs
- niche
related:
- /knowledge-concepts/pattern-batch
- /knowledge-concepts/pattern-request-response
- /knowledge-concepts/pattern-streaming
- /knowledge-concepts/synthetic-stream
- /knowledge-concepts/data-product
---
# 7.4 — Batch → live query + pseudo-events

**Interface:** IN `{B}` → OUT `{R, S}`&emsp;&emsp;**Verdict:** niche

Serve "live" over a nightly refresh: events (synthetic) + query API from batch inputs.

![Interface diagram: IN B to OUT RS](/assets/cells/821.svg)

## When to use

Consumers are online and events-only; the source is batch.

## Watch out

"Live" is an illusion — label it "as-of last refresh".

## Related

* [batch](/knowledge-concepts/pattern-batch)
* [request/response](/knowledge-concepts/pattern-request-response)
* [streaming](/knowledge-concepts/pattern-streaming)
* [synthetic-stream](/knowledge-concepts/synthetic-stream) — this cell's stream out is not backed by a stream in
* [data-product](/knowledge-concepts/data-product) — the overall model
* [verdict](/knowledge-concepts/verdict) — what the common / plausible / niche tag means
* [architectural paradigms](/knowledge-concepts/architectural-paradigms) — this cell maps to: CDC (change data capture): a batch-refreshed store emits a synthetic stream + query API.

