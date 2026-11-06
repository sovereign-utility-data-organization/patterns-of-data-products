---
type: Data Product Type
okf_version: '0.1'
timestamp: '2026-11-06T12:50:00Z'
description: 'Data product ingesting via request/response (on-demand query) + streaming (pub/sub feed) and serving via batch (bulk/file) + request/response (on-demand query) — hub facade: stream + api in, api + file out.'
title: 'Cell 4.2: Hub facade: stream + API in, API + file out'
tags:
- data-product-type
- in-rs
- out-br
- common
related:
- /knowledge-concepts/pattern-batch
- /knowledge-concepts/pattern-request-response
- /knowledge-concepts/pattern-streaming
- /knowledge-concepts/data-product
---
# 4.2 — Hub facade: stream + API in, API + file out

**Interface:** IN `{R, S}` → OUT `{B, R}`&emsp;&emsp;**Verdict:** common

Events + service APIs in; consumers get the query API and nightly exports (e.g., billing: events + tariff API → invoice API + D01 files).

![Interface diagram: IN RS to OUT BR](/assets/cells/361.svg)

## When to use

Consumer mix is online + batch, and sources are online.

## Related

* [batch](/knowledge-concepts/pattern-batch)
* [request/response](/knowledge-concepts/pattern-request-response)
* [streaming](/knowledge-concepts/pattern-streaming)
* [data-product](/knowledge-concepts/data-product) — the overall model
* [verdict](/knowledge-concepts/verdict) — what the common / plausible / niche tag means
* [architectural paradigms](/knowledge-concepts/architectural-paradigms) — this cell maps to: Hub facade / microservices: stream + API in, API + file out.

