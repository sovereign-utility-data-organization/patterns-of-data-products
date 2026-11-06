---
type: Data Product Type
okf_version: '0.1'
timestamp: '2026-11-06T12:50:00Z'
description: Data product ingesting via batch (bulk/file) + request/response (on-demand query) and serving via streaming (pub/sub feed) — poll-to-stream bridge.
title: 'Cell 2.5: Poll-to-stream bridge'
tags:
- data-product-type
- in-br
- out-s
- niche
related:
- /knowledge-concepts/pattern-batch
- /knowledge-concepts/pattern-request-response
- /knowledge-concepts/pattern-streaming
- /knowledge-concepts/synthetic-stream
- /knowledge-concepts/data-product
---
# 2.5 — Poll-to-stream bridge

**Interface:** IN `{B, R}` → OUT `{S}`&emsp;&emsp;**Verdict:** niche

A bridge product whose whole job is "files/APIs → topics".

<img src="/assets/cells/873.svg" alt="Cell diagram: IN BR to OUT S" width="380" style="background:#000;padding:8px;border-radius:6px"/>

## When to use

A Kafka-first world must consume legacy file/API sources.

## Watch out

Consumers may expect push semantics the source can't honour — document deltas, snapshots, and backfill rules.

## Related

* [batch](/knowledge-concepts/pattern-batch)
* [request/response](/knowledge-concepts/pattern-request-response)
* [streaming](/knowledge-concepts/pattern-streaming)
* [synthetic-stream](/knowledge-concepts/synthetic-stream) — this cell's stream out is not backed by a stream in
* [data-product](/knowledge-concepts/data-product) — the overall model
* [verdict](/knowledge-concepts/verdict) — what the common / plausible / niche tag means

