---
type: Data Product Type
okf_version: '0.1'
timestamp: '2026-11-06T12:50:00Z'
description: Data product ingesting via streaming (pub/sub feed) and serving via batch (bulk/file) — stream → settlement/rollup file.
title: 'Cell 5.7: Stream → settlement/rollup file'
tags:
- data-product-type
- in-s
- out-b
- plausible
related:
- /knowledge-concepts/pattern-batch
- /knowledge-concepts/pattern-streaming
- /knowledge-concepts/data-product
---
# 5.7 — Stream → settlement/rollup file

**Interface:** IN `{S}` → OUT `{B}`&emsp;&emsp;**Verdict:** plausible

Events in → periodic bulk out (meter-reading stream → daily interval file; clickstream → EOD usage files).

## When to use

The contract is a file but the data is inherently streaming — very common in utility settlement.

## Related

* [batch](/knowledge-concepts/pattern-batch)
* [streaming](/knowledge-concepts/pattern-streaming)
* [data-product](/knowledge-concepts/data-product) — the overall model
* [verdict](/knowledge-concepts/verdict) — what the common / plausible / niche tag means

