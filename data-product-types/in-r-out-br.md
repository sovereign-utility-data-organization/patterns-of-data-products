---
type: Data Product Type
okf_version: '0.1'
timestamp: '2026-11-06T12:50:00Z'
description: Data product ingesting via request/response (on-demand query) and serving via batch (bulk/file) + request/response (on-demand query) — poll + serve api + files.
title: 'Cell 6.2: Poll + serve API + files'
tags:
- data-product-type
- in-r
- out-br
- plausible
related:
- /knowledge-concepts/pattern-batch
- /knowledge-concepts/pattern-request-response
- /knowledge-concepts/data-product
---
# 6.2 — Poll + serve API + files

**Interface:** IN `{R}` → OUT `{B, R}`&emsp;&emsp;**Verdict:** plausible

A refreshed service: polls upstream, exposes a cleaner API, and also emits periodic full-load files (supplier meter API → reading API + daily snapshot files).

<img src="/assets/cells/409.svg" alt="Cell diagram: IN R to OUT BR" width="380" style="background:#000;padding:8px;border-radius:6px"/>

## When to use

Consumers are a mix of online pollers + ETL consumers, and the upstream is API-only.

## Related

* [batch](/knowledge-concepts/pattern-batch)
* [request/response](/knowledge-concepts/pattern-request-response)
* [data-product](/knowledge-concepts/data-product) — the overall model
* [verdict](/knowledge-concepts/verdict) — what the common / plausible / niche tag means

