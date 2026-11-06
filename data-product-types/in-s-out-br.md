---
type: Data Product Type
okf_version: '0.1'
timestamp: '2026-11-06T12:50:00Z'
description: Data product ingesting via streaming (pub/sub feed) and serving via batch (bulk/file) + request/response (on-demand query) — streaming etl into lake + api.
title: 'Cell 5.2: Streaming ETL into lake + API'
tags:
- data-product-type
- in-s
- out-br
- common
related:
- /knowledge-concepts/pattern-batch
- /knowledge-concepts/pattern-request-response
- /knowledge-concepts/pattern-streaming
- /knowledge-concepts/data-product
---
# 5.2 — Streaming ETL into lake + API

**Interface:** IN `{S}` → OUT `{B, R}`&emsp;&emsp;**Verdict:** common

Events → queryable store + data-lake files. The standard modern ingestion architecture (Kafka → S3 + API over a query engine / Iceberg).

![Interface diagram: IN S to OUT BR](/assets/cells/386.svg)

## When to use

Consumers want analysis (API) + archival (files); no need to keep the stream out.

## Related

* [batch](/knowledge-concepts/pattern-batch)
* [request/response](/knowledge-concepts/pattern-request-response)
* [streaming](/knowledge-concepts/pattern-streaming)
* [data-product](/knowledge-concepts/data-product) — the overall model
* [verdict](/knowledge-concepts/verdict) — what the common / plausible / niche tag means
* [architectural paradigms](/knowledge-concepts/architectural-paradigms) — this cell maps to: Event sourcing / streaming ELT and stream processing: Kafka -> lake + queryable API.

