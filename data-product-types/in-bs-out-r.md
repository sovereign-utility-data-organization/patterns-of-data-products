---
type: Data Product Type
okf_version: "0.1"
timestamp: 2026-11-06T12:50:00Z
description: Data product ingesting via batch (bulk/file) + streaming (pub/sub feed) and serving via request/response (on-demand query) — stream + reference → queryable historian.
title: Cell 3.6: Stream + reference → queryable historian
tags:
  - data-product-type
  - in-bs
  - out-r
  - common
related:

  - /knowledge-concepts/pattern-batch
  - /knowledge-concepts/pattern-request-response
  - /knowledge-concepts/pattern-streaming
  - /knowledge-concepts/data-product
---
# 3.6 — Stream + reference → queryable historian

**Interface:** IN `{B, S}` → OUT `{R}`&emsp;&emsp;**Verdict:** common

The historian pattern: events land in a time-series/state DB, reference data is periodically loaded, consumers query (e.g., SCADA historian + historian API).

## When to use

Consumers want analysis over history, not push.

## Related

* [batch](/knowledge-concepts/pattern-batch)
* [request/response](/knowledge-concepts/pattern-request-response)
* [streaming](/knowledge-concepts/pattern-streaming)
* [data-product](/knowledge-concepts/data-product) — the overall model

