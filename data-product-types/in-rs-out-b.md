---
type: Data Product Type
okf_version: '0.1'
timestamp: '2026-11-06T12:50:00Z'
description: Data product ingesting via request/response (on-demand query) + streaming (pub/sub feed) and serving via batch (bulk/file) — live activity → t+1 report/file.
title: 'Cell 4.7: Live activity → T+1 report/file'
tags:
- data-product-type
- in-rs
- out-b
- plausible
related:
- /knowledge-concepts/pattern-batch
- /knowledge-concepts/pattern-request-response
- /knowledge-concepts/pattern-streaming
- /knowledge-concepts/data-product
---
# 4.7 — Live activity → T+1 report/file

**Interface:** IN `{R, S}` → OUT `{B}`&emsp;&emsp;**Verdict:** plausible

Consumes live events + APIs, publishes a file once a day (activity report, usage file, billing input).

<img src="/assets/cells/1189.svg" alt="Cell diagram: IN RS to OUT B" width="380" style="background:#000;padding:8px;border-radius:6px"/>

## When to use

The contract is a file but the data is inherently live.

## Watch out

Consumers get T+1 of a T+0 world — publish with clear as-of semantics.

## Related

* [batch](/knowledge-concepts/pattern-batch)
* [request/response](/knowledge-concepts/pattern-request-response)
* [streaming](/knowledge-concepts/pattern-streaming)
* [data-product](/knowledge-concepts/data-product) — the overall model
* [verdict](/knowledge-concepts/verdict) — what the common / plausible / niche tag means

