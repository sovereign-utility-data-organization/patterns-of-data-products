---
type: Data Product Type
okf_version: "0.1"
timestamp: 2026-11-06T12:50:00Z
description: Data product ingesting via batch (bulk/file) + streaming (pub/sub feed) and serving via batch (bulk/file) — stream → settlement files.
title: Cell 3.7: Stream → settlement files
tags:
  - data-product-type
  - in-bs
  - out-b
  - common
related:

  - /knowledge-concepts/pattern-batch
  - /knowledge-concepts/pattern-streaming
  - /knowledge-concepts/data-product
---
# 3.7 — Stream → settlement files

**Interface:** IN `{B, S}` → OUT `{B}`&emsp;&emsp;**Verdict:** common

Real-time metered events + reference data in → daily settlement file out. The heart of many utility settlement engines.

## When to use

The market contract is file-based (day-ahead / imbalance settlement) but the data is inherently streaming.

## Related

* [batch](/knowledge-concepts/pattern-batch)
* [streaming](/knowledge-concepts/pattern-streaming)
* [data-product](/knowledge-concepts/data-product) — the overall model

