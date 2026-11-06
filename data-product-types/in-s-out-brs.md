---
type: Data Product Type
okf_version: '0.1'
timestamp: '2026-11-06T12:50:00Z'
description: Data product ingesting via streaming (pub/sub feed) and serving via batch (bulk/file) + request/response (on-demand query) + streaming (pub/sub feed) — stream processor + full platform.
title: 'Cell 5.1: Stream processor + full platform'
tags:
- data-product-type
- in-s
- out-brs
- common
related:
- /knowledge-concepts/pattern-batch
- /knowledge-concepts/pattern-request-response
- /knowledge-concepts/pattern-streaming
- /knowledge-concepts/data-product
---# 5.1 — Stream processor + full platform

**Interface:** IN `{S}` → OUT `{B, R, S}`&emsp;&emsp;**Verdict:** common

Stream in → stream processor / stateful aggregation → all serving modes (Flink/Kafka + state store + sink world).

## When to use

The product owns the aggregation layer between events and consumers.

## Related

* [batch](/knowledge-concepts/pattern-batch)
* [request/response](/knowledge-concepts/pattern-request-response)
* [streaming](/knowledge-concepts/pattern-streaming)
* [data-product](/knowledge-concepts/data-product) — the overall model

