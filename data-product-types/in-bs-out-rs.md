---
type: Data Product Type
okf_version: '0.1'
timestamp: '2026-11-06T12:50:00Z'
description: Data product ingesting via batch (bulk/file) + streaming (pub/sub feed) and serving via request/response (on-demand query) + streaming (pub/sub feed) — event + state query, no files.
title: 'Cell 3.4: Event + state query, no files'
tags:
- data-product-type
- in-bs
- out-rs
- niche
related:
- /knowledge-concepts/pattern-batch
- /knowledge-concepts/pattern-request-response
- /knowledge-concepts/pattern-streaming
- /knowledge-concepts/data-product
---
# 3.4 — Event + state query, no files

**Interface:** IN `{B, S}` → OUT `{R, S}`&emsp;&emsp;**Verdict:** niche

Live events and on-demand state queries; no bulk serving.

![Interface diagram: IN BS to OUT RS](/assets/cells/750.svg)

## When to use

Consumers are online and bulk export is a different product's job.

## Watch out

Long-term retention usually still wants a cold/file tier — verify history isn't just being dropped.

## Related

* [batch](/knowledge-concepts/pattern-batch)
* [request/response](/knowledge-concepts/pattern-request-response)
* [streaming](/knowledge-concepts/pattern-streaming)
* [data-product](/knowledge-concepts/data-product) — the overall model
* [verdict](/knowledge-concepts/verdict) — what the common / plausible / niche tag means

