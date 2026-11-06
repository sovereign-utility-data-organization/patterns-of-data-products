---
type: Data Product Type
okf_version: '0.1'
timestamp: '2026-11-06T12:50:00Z'
description: Data product ingesting via batch (bulk/file) and serving via request/response (on-demand query) — the classic "load files, serve api".
title: 'Cell 7.6: The classic "load files, serve API"'
tags:
- data-product-type
- in-b
- out-r
- common
related:
- /knowledge-concepts/pattern-batch
- /knowledge-concepts/pattern-request-response
- /knowledge-concepts/data-product
---
# 7.6 — The classic "load files, serve API"

**Interface:** IN `{B}` → OUT `{R}`&emsp;&emsp;**Verdict:** common

Files in → one clean API out (nightly price/tariff files → price/tariff API). The most common single-pattern data product in regulated/utility domains.

<img src="/assets/cells/1077.svg" alt="Cell diagram: IN B to OUT R" width="380" style="background:#000;padding:8px;border-radius:6px"/>

## When to use

Upstream is file-based, consumers are online.

## Related

* [batch](/knowledge-concepts/pattern-batch)
* [request/response](/knowledge-concepts/pattern-request-response)
* [data-product](/knowledge-concepts/data-product) — the overall model
* [verdict](/knowledge-concepts/verdict) — what the common / plausible / niche tag means

