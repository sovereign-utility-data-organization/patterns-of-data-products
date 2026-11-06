---
type: Data Product Type
okf_version: '0.1'
timestamp: '2026-11-06T12:50:00Z'
description: Data product ingesting via batch (bulk/file) + request/response (on-demand query) + streaming (pub/sub feed) and serving via request/response (on-demand query) — unified query api over messy sources.
title: 'Cell 1.6: Unified query API over messy sources'
tags:
- data-product-type
- in-brs
- out-r
- common
related:
- /knowledge-concepts/pattern-batch
- /knowledge-concepts/pattern-request-response
- /knowledge-concepts/pattern-streaming
- /knowledge-concepts/data-product
---# 1.6 — Unified query API over messy sources

**Interface:** IN `{B, R, S}` → OUT `{R}`&emsp;&emsp;**Verdict:** common

The BFF / service façade: files + upstream APIs + event feeds behind one request/response contract.

## When to use

The product's value is *normalisation*: consumers want one schema and one endpoint (unified "customer" or "order" API over CRM/ERP/events).

## Related

* [batch](/knowledge-concepts/pattern-batch)
* [request/response](/knowledge-concepts/pattern-request-response)
* [streaming](/knowledge-concepts/pattern-streaming)
* [data-product](/knowledge-concepts/data-product) — the overall model

