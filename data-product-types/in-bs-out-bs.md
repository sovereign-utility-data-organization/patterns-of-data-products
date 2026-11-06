---
type: Data Product Type
okf_version: "0.1"
timestamp: 2026-11-06T12:50:00Z
description: Data product ingesting via batch (bulk/file) + streaming (pub/sub feed) and serving via batch (bulk/file) + streaming (pub/sub feed) — hot & cold in → hot & cold out.
title: Cell 3.3: Hot & cold in → hot & cold out
tags:
  - data-product-type
  - in-bs
  - out-bs
  - common
related:

  - /knowledge-concepts/pattern-batch
  - /knowledge-concepts/pattern-streaming
  - /knowledge-concepts/data-product
---
# 3.3 — Hot & cold in → hot & cold out

**Interface:** IN `{B, S}` → OUT `{B, S}`&emsp;&emsp;**Verdict:** common

Pass-through streaming platform: events stay events; bulk in merges in or becomes bulk out (e.g., Kafka mirror + S3 archive service).

## When to use

Consumers subscribe to feeds *and* consume archives; goal is a single consistent pipeline.

## Related

* [batch](/knowledge-concepts/pattern-batch)
* [streaming](/knowledge-concepts/pattern-streaming)
* [data-product](/knowledge-concepts/data-product) — the overall model

