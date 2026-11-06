---
type: Data Product Type
okf_version: "0.1"
timestamp: 2026-11-06T12:50:00Z
description: Data product ingesting via batch (bulk/file) + request/response (on-demand query) + streaming (pub/sub feed) and serving via streaming (pub/sub feed) — all-in, single stream.
title: Cell 1.5: All-in, single stream
tags:
  - data-product-type
  - in-brs
  - out-s
  - niche
related:

  - /knowledge-concepts/pattern-batch
  - /knowledge-concepts/pattern-request-response
  - /knowledge-concepts/pattern-streaming
  - /knowledge-concepts/data-product
---
# 1.5 — All-in, single stream

**Interface:** IN `{B, R, S}` → OUT `{S}`&emsp;&emsp;**Verdict:** niche

"One topic for the world": all sources (files included, replayed as events) funneled into one pub/sub interface.

## When to use

Downstream is a pure stream topology (Kafka mesh, CEP fabric).

## Watch out

File-based sources become synthetic streams — backfill is loud.

## Related

* [batch](/knowledge-concepts/pattern-batch)
* [request/response](/knowledge-concepts/pattern-request-response)
* [streaming](/knowledge-concepts/pattern-streaming)
* [data-product](/knowledge-concepts/data-product) — the overall model

