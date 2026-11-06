---
type: Data Product Type
okf_version: '0.1'
timestamp: '2026-11-06T12:50:00Z'
description: Data product ingesting via batch (bulk/file) + streaming (pub/sub feed) and serving via batch (bulk/file) + request/response (on-demand query) — smart-meter platform shape.
title: 'Cell 3.2: Smart-meter platform shape'
tags:
- data-product-type
- in-bs
- out-br
- common
related:
- /knowledge-concepts/pattern-batch
- /knowledge-concepts/pattern-request-response
- /knowledge-concepts/pattern-streaming
- /knowledge-concepts/data-product
---
# 3.2 — Smart-meter platform shape

**Interface:** IN `{B, S}` → OUT `{B, R}`&emsp;&emsp;**Verdict:** common

Live meter events + tariff reference (batch) in → reading API + settlement files out. The common utility shape; consumers pull, no pure stream out.

![Interface diagram: IN BS to OUT BR](/assets/cells/334.svg)

## When to use

Utility/energy domain: metered streams plus reference files, served to both online and bulk consumers.

## Related

* [batch](/knowledge-concepts/pattern-batch)
* [request/response](/knowledge-concepts/pattern-request-response)
* [streaming](/knowledge-concepts/pattern-streaming)
* [data-product](/knowledge-concepts/data-product) — the overall model
* [verdict](/knowledge-concepts/verdict) — what the common / plausible / niche tag means

