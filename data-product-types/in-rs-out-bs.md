---
type: Data Product Type
okf_version: '0.1'
timestamp: '2026-11-06T12:50:00Z'
description: Data product ingesting via request/response (on-demand query) + streaming (pub/sub feed) and serving via batch (bulk/file) + streaming (pub/sub feed) — telemetry platform.
title: 'Cell 4.3: Telemetry platform'
tags:
- data-product-type
- in-rs
- out-bs
- plausible
related:
- /knowledge-concepts/pattern-batch
- /knowledge-concepts/pattern-request-response
- /knowledge-concepts/pattern-streaming
- /knowledge-concepts/data-product
---
# 4.3 — Telemetry platform

**Interface:** IN `{R, S}` → OUT `{B, S}`&emsp;&emsp;**Verdict:** plausible

Events + device/service APIs in; live feeds + bulk archives out (e.g., vehicle/IoT telemetry: CAN-stream + OBD API → fleet stream + daily trip files).

## When to use

Consumers want both push and periodic full loads.

## Related

* [batch](/knowledge-concepts/pattern-batch)
* [request/response](/knowledge-concepts/pattern-request-response)
* [streaming](/knowledge-concepts/pattern-streaming)
* [data-product](/knowledge-concepts/data-product) — the overall model
* [verdict](/knowledge-concepts/verdict) — what the common / plausible / niche tag means

