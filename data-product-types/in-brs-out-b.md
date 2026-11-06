---
type: Data Product Type
okf_version: '0.1'
timestamp: '2026-11-06T12:50:00Z'
description: Data product ingesting via batch (bulk/file) + request/response (on-demand query) + streaming (pub/sub feed) and serving via batch (bulk/file) — multi-source etl feed.
title: 'Cell 1.7: Multi-source ETL feed'
tags:
- data-product-type
- in-brs
- out-b
- plausible
related:
- /knowledge-concepts/pattern-batch
- /knowledge-concepts/pattern-request-response
- /knowledge-concepts/pattern-streaming
- /knowledge-concepts/data-product
---# 1.7 — Multi-source ETL feed

**Interface:** IN `{B, R, S}` → OUT `{B}`&emsp;&emsp;**Verdict:** plausible

Everything in, one file out — the consolidation layer with a single publication surface (settlement or reporting bundle).

## When to use

The consumer-side contract is file delivery; very common in utility settlement (meter events + tariff APIs + reference files in, one settlement file out).

## Watch out

Latency expectations collapse to the batch cycle.

## Related

* [batch](/knowledge-concepts/pattern-batch)
* [request/response](/knowledge-concepts/pattern-request-response)
* [streaming](/knowledge-concepts/pattern-streaming)
* [data-product](/knowledge-concepts/data-product) — the overall model

