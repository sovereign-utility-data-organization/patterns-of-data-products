---
type: Data Product Type
okf_version: '0.1'
timestamp: '2026-11-06T12:50:00Z'
description: Data product ingesting via request/response (on-demand query) and serving via batch (bulk/file) + streaming (pub/sub feed) — poller with stream + files.
title: 'Cell 6.3: Poller with stream + files'
tags:
- data-product-type
- in-r
- out-bs
- niche
related:
- /knowledge-concepts/pattern-batch
- /knowledge-concepts/pattern-request-response
- /knowledge-concepts/pattern-streaming
- /knowledge-concepts/synthetic-stream
- /knowledge-concepts/data-product
---
# 6.3 — Poller with stream + files

**Interface:** IN `{R}` → OUT `{B, S}`&emsp;&emsp;**Verdict:** niche

API in, stream out (synthetic) + files out — a bridge from a polled world into a streaming world plus an archival file set.

## When to use

Downstream wants push and archives; source is poll-only.

## Watch out

Synthetic-stream caveats apply (change semantics, cadence, backfill).

## Related

* [batch](/knowledge-concepts/pattern-batch)
* [request/response](/knowledge-concepts/pattern-request-response)
* [streaming](/knowledge-concepts/pattern-streaming)
* [synthetic-stream](/knowledge-concepts/synthetic-stream) — this cell's stream out is not backed by a stream in
* [data-product](/knowledge-concepts/data-product) — the overall model
* [verdict](/knowledge-concepts/verdict) — what the common / plausible / niche tag means

