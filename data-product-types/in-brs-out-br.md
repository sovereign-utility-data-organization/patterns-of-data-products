---
type: Data Product Type
okf_version: '0.1'
timestamp: '2026-11-06T12:50:00Z'
description: Data product ingesting via batch (bulk/file) + request/response (on-demand query) + streaming (pub/sub feed) and serving via batch (bulk/file) + request/response (on-demand query) — consolidation hub with api + reports.
title: 'Cell 1.2: Consolidation hub with API + reports'
tags:
- data-product-type
- in-brs
- out-br
- common
related:
- /knowledge-concepts/pattern-batch
- /knowledge-concepts/pattern-request-response
- /knowledge-concepts/pattern-streaming
- /knowledge-concepts/data-product
---
# 1.2 — Consolidation hub with API + reports

**Interface:** IN `{B, R, S}` → OUT `{B, R}`&emsp;&emsp;**Verdict:** common

Everything ingested (files, APIs, streams); consumers get a clean query API plus scheduled files — no streaming out. The most economical "good facade" for pollers and report writers.

<img src="/assets/cells/260.svg" alt="Cell diagram: IN BRS to OUT BR" width="380" style="background:#000;padding:8px;border-radius:6px"/>

## When to use

No real-time requirement; the need is just one clean API plus one file feed.

## Related

* [batch](/knowledge-concepts/pattern-batch)
* [request/response](/knowledge-concepts/pattern-request-response)
* [streaming](/knowledge-concepts/pattern-streaming)
* [data-product](/knowledge-concepts/data-product) — the overall model
* [verdict](/knowledge-concepts/verdict) — what the common / plausible / niche tag means

