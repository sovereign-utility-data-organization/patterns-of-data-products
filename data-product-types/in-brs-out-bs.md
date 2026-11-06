---
type: Data Product Type
okf_version: '0.1'
timestamp: '2026-11-06T12:50:00Z'
description: Data product ingesting via batch (bulk/file) + request/response (on-demand query) + streaming (pub/sub feed) and serving via batch (bulk/file) + streaming (pub/sub feed) — hub with live feed + bulk export.
title: 'Cell 1.3: Hub with live feed + bulk export'
tags:
- data-product-type
- in-brs
- out-bs
- common
related:
- /knowledge-concepts/pattern-batch
- /knowledge-concepts/pattern-request-response
- /knowledge-concepts/pattern-streaming
- /knowledge-concepts/data-product
---# 1.3 — Hub with live feed + bulk export

**Interface:** IN `{B, R, S}` → OUT `{B, S}`&emsp;&emsp;**Verdict:** common

Consolidated source data exposed as a continuous stream and as bulk archives (e.g., an enterprise event spine with S3 archive).

## When to use

Consumers react to change but also need full loads (historians, downstream stream consumers, reconciliation).

## Related

* [batch](/knowledge-concepts/pattern-batch)
* [request/response](/knowledge-concepts/pattern-request-response)
* [streaming](/knowledge-concepts/pattern-streaming)
* [data-product](/knowledge-concepts/data-product) — the overall model

