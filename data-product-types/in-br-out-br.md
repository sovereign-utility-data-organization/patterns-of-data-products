---
type: Data Product Type
okf_version: '0.1'
timestamp: '2026-11-06T12:50:00Z'
description: Data product ingesting via batch (bulk/file) + request/response (on-demand query) and serving via batch (bulk/file) + request/response (on-demand query) — classic data api + file feed.
title: 'Cell 2.2: Classic data API + file feed'
tags:
- data-product-type
- in-br
- out-br
- common
related:
- /knowledge-concepts/pattern-batch
- /knowledge-concepts/pattern-request-response
- /knowledge-concepts/data-product
---
# 2.2 — Classic data API + file feed

**Interface:** IN `{B, R}` → OUT `{B, R}`&emsp;&emsp;**Verdict:** common

The bread and butter: refresh from feeds and APIs, serve a clean API plus daily bundles (a weather/price API that also serves files).

![Interface diagram: IN BR to OUT BR](/assets/cells/298.svg)

## When to use

Consumers are a mix of online pollers and ETL consumers; no live requirement.

## Related

* [batch](/knowledge-concepts/pattern-batch)
* [request/response](/knowledge-concepts/pattern-request-response)
* [data-product](/knowledge-concepts/data-product) — the overall model
* [verdict](/knowledge-concepts/verdict) — what the common / plausible / niche tag means

