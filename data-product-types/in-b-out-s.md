---
type: Data Product Type
okf_version: '0.1'
timestamp: '2026-11-06T12:50:00Z'
description: Data product ingesting via batch (bulk/file) and serving via streaming (pub/sub feed) — batch → event feed.
title: 'Cell 7.5: Batch → event feed'
tags:
- data-product-type
- in-b
- out-s
- niche
related:
- /knowledge-concepts/pattern-batch
- /knowledge-concepts/pattern-streaming
- /knowledge-concepts/synthetic-stream
- /knowledge-concepts/data-product
---
# 7.5 — Batch → event feed

**Interface:** IN `{B}` → OUT `{S}`&emsp;&emsp;**Verdict:** niche

Turn a daily bulk load into a stream of events (snapshots → deltas) — a *replay* product.

## When to use

Downstream is a pure event world and the source is a legacy batch world.

## Watch out

Consumers must treat each batch as a batch of synthetic events, not a continuous feed.

## Related

* [batch](/knowledge-concepts/pattern-batch)
* [streaming](/knowledge-concepts/pattern-streaming)
* [synthetic-stream](/knowledge-concepts/synthetic-stream) — this cell's stream out is not backed by a stream in
* [data-product](/knowledge-concepts/data-product) — the overall model
* [verdict](/knowledge-concepts/verdict) — what the common / plausible / niche tag means
* [architectural paradigms](/knowledge-concepts/architectural-paradigms) — this cell maps to: CDC (change data capture): a batch-refreshed store emits a synthetic change stream.

