---
type: Data Product Type
okf_version: '0.1'
timestamp: '2026-11-06T12:50:00Z'
description: Data product ingesting via request/response (on-demand query) + streaming (pub/sub feed) and serving via batch (bulk/file) + request/response (on-demand query) + streaming (pub/sub feed) — mdm / integration hub with full out.
title: 'Cell 4.1: MDM / integration hub with full out'
tags:
- data-product-type
- in-rs
- out-brs
- plausible
related:
- /knowledge-concepts/pattern-batch
- /knowledge-concepts/pattern-request-response
- /knowledge-concepts/pattern-streaming
- /knowledge-concepts/data-product
---
# 4.1 — MDM / integration hub with full out

**Interface:** IN `{R, S}` → OUT `{B, R, S}`&emsp;&emsp;**Verdict:** plausible

Lives entirely on APIs + events; emits files, streams, and APIs — including bulk exports built from incremental change logs.

![Interface diagram: IN RS to OUT BRS](/assets/cells/128.svg)

## When to use

The product is the "system-of-record glue" (master data hub, order hub).

## Watch out

Full-load exports need a complete state store — build it.

## Related

* [batch](/knowledge-concepts/pattern-batch)
* [request/response](/knowledge-concepts/pattern-request-response)
* [streaming](/knowledge-concepts/pattern-streaming)
* [data-product](/knowledge-concepts/data-product) — the overall model
* [verdict](/knowledge-concepts/verdict) — what the common / plausible / niche tag means

