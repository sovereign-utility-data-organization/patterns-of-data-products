---
type: Data Product Type
okf_version: '0.1'
timestamp: '2026-11-06T12:50:00Z'
description: Data product ingesting via streaming (pub/sub feed) and serving via streaming (pub/sub feed) — event transformer / relay.
title: 'Cell 5.5: Event transformer / relay'
tags:
- data-product-type
- in-s
- out-s
- common
related:
- /knowledge-concepts/pattern-streaming
- /knowledge-concepts/data-product
---
# 5.5 — Event transformer / relay

**Interface:** IN `{S}` → OUT `{S}`&emsp;&emsp;**Verdict:** common

A pure stream-to-stream product: filter, route, enrich, project (topic in → topics out). The value is the transformation, not the serving.

## When to use

Consumers need a *derived* topic and the product can be stateless by nature.

## Watch out

No state persistence beyond the topic — the product is ephemeral by design.

## Related

* [streaming](/knowledge-concepts/pattern-streaming)
* [data-product](/knowledge-concepts/data-product) — the overall model
* [verdict](/knowledge-concepts/verdict) — what the common / plausible / niche tag means

