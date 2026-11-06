---
type: Data Product Type
okf_version: '0.1'
timestamp: '2026-11-06T12:50:00Z'
description: Data product ingesting via batch (bulk/file) + streaming (pub/sub feed) and serving via streaming (pub/sub feed) — stream join / stream enrichment.
title: 'Cell 3.5: Stream join / stream enrichment'
tags:
- data-product-type
- in-bs
- out-s
- plausible
related:
- /knowledge-concepts/pattern-batch
- /knowledge-concepts/pattern-streaming
- /knowledge-concepts/data-product
---
# 3.5 — Stream join / stream enrichment

**Interface:** IN `{B, S}` → OUT `{S}`&emsp;&emsp;**Verdict:** plausible

Enriches an event stream with bulk-loaded reference data and emits an enriched stream (e.g., meter events + tariff/reference → enriched market events).

![Interface diagram: IN BS to OUT S](/assets/cells/896.svg)

## When to use

The product's value is enrichment; consumers are stream consumers.

## Related

* [batch](/knowledge-concepts/pattern-batch)
* [streaming](/knowledge-concepts/pattern-streaming)
* [data-product](/knowledge-concepts/data-product) — the overall model
* [verdict](/knowledge-concepts/verdict) — what the common / plausible / niche tag means

