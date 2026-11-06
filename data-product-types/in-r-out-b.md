---
type: Data Product Type
okf_version: '0.1'
timestamp: '2026-11-06T12:50:00Z'
description: Data product ingesting via request/response (on-demand query) and serving via batch (bulk/file) — api feed → scheduled file.
title: 'Cell 6.7: API feed → scheduled file'
tags:
- data-product-type
- in-r
- out-b
- common
related:
- /knowledge-concepts/pattern-batch
- /knowledge-concepts/pattern-request-response
- /knowledge-concepts/data-product
---# 6.7 — API feed → scheduled file

**Interface:** IN `{R}` → OUT `{B}`&emsp;&emsp;**Verdict:** common

Poll from upstream, publish a file. The classic fetch-and-drop integration (supplier portal API → settlement file; tariff API → rate-table file).

## When to use

The contract is file-based delivery; the source is API-based.

## Related

* [batch](/knowledge-concepts/pattern-batch)
* [request/response](/knowledge-concepts/pattern-request-response)
* [data-product](/knowledge-concepts/data-product) — the overall model

