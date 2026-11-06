---
type: Data Product Type
okf_version: '0.1'
timestamp: '2026-11-06T12:50:00Z'
description: Data product ingesting via batch (bulk/file) + streaming (pub/sub feed) and serving via batch (bulk/file) + request/response (on-demand query) + streaming (pub/sub feed) — event platform with full serving.
title: 'Cell 3.1: Event platform with full serving'
tags:
- data-product-type
- in-bs
- out-brs
- common
related:
- /knowledge-concepts/pattern-batch
- /knowledge-concepts/pattern-request-response
- /knowledge-concepts/pattern-streaming
- /knowledge-concepts/data-product
---
# 3.1 — Event platform with full serving

**Interface:** IN `{B, S}` → OUT `{B, R, S}`&emsp;&emsp;**Verdict:** common

Hot & cold ingest (e.g., Kafka + S3) served via streams, APIs, and bulk exports — the modern streaming platform (Kafka + Iceberg/Delta).

![Interface diagram: IN BS to OUT BRS](/assets/cells/97.svg)

## When to use

All three consumer types are needed on top of event data.

## Related

* [batch](/knowledge-concepts/pattern-batch)
* [request/response](/knowledge-concepts/pattern-request-response)
* [streaming](/knowledge-concepts/pattern-streaming)
* [data-product](/knowledge-concepts/data-product) — the overall model
* [verdict](/knowledge-concepts/verdict) — what the common / plausible / niche tag means

