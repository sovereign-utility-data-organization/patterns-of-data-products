---
type: Data Product Type
okf_version: '0.1'
timestamp: '2026-11-06T12:50:00Z'
description: Data product ingesting via batch (bulk/file) + request/response (on-demand query) and serving via batch (bulk/file) — the classic etl.
title: 'Cell 2.7: The classic ETL'
tags:
- data-product-type
- in-br
- out-b
- common
related:
- /knowledge-concepts/pattern-batch
- /knowledge-concepts/pattern-request-response
- /knowledge-concepts/data-product
---
# 2.7 — The classic ETL

**Interface:** IN `{B, R}` → OUT `{B}`&emsp;&emsp;**Verdict:** common

Files + APIs in → file(s) out. The oldest and most common data product that exists (supplier feeds + master APIs → settlement/report files).

<img src="/assets/cells/1134.svg" alt="Cell diagram: IN BR to OUT B" width="380" style="background:#000;padding:8px;border-radius:6px"/>

## When to use

The contract with consumers is a file on a schedule.

## Related

* [batch](/knowledge-concepts/pattern-batch)
* [request/response](/knowledge-concepts/pattern-request-response)
* [data-product](/knowledge-concepts/data-product) — the overall model
* [verdict](/knowledge-concepts/verdict) — what the common / plausible / niche tag means

