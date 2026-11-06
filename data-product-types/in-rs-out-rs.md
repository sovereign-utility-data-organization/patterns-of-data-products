---
type: Data Product Type
okf_version: '0.1'
timestamp: '2026-11-06T12:50:00Z'
description: Data product ingesting via request/response (on-demand query) + streaming (pub/sub feed) and serving via request/response (on-demand query) + streaming (pub/sub feed) — unified live view.
title: 'Cell 4.4: Unified live view'
tags:
- data-product-type
- in-rs
- out-rs
- common
related:
- /knowledge-concepts/pattern-request-response
- /knowledge-concepts/pattern-streaming
- /knowledge-concepts/data-product
---
# 4.4 — Unified live view

**Interface:** IN `{R, S}` → OUT `{R, S}`&emsp;&emsp;**Verdict:** common

A clean real-time façade: one stream + one query API over the combined inputs.

![Interface diagram: IN RS to OUT RS](/assets/cells/768.svg)

## When to use

All consumers are online and a single consistent contract is wanted (unified telemetry/asset platform).

## Related

* [request/response](/knowledge-concepts/pattern-request-response)
* [streaming](/knowledge-concepts/pattern-streaming)
* [data-product](/knowledge-concepts/data-product) — the overall model
* [verdict](/knowledge-concepts/verdict) — what the common / plausible / niche tag means

