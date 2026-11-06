---
type: Data Product Type
okf_version: '0.1'
timestamp: '2026-11-06T12:50:00Z'
description: Data product ingesting via streaming (pub/sub feed) and serving via batch (bulk/file) + streaming (pub/sub feed) — hot & cold streaming platform.
title: 'Cell 5.3: Hot & cold streaming platform'
tags:
- data-product-type
- in-s
- out-bs
- common
related:
- /knowledge-concepts/pattern-batch
- /knowledge-concepts/pattern-streaming
- /knowledge-concepts/data-product
---
# 5.3 — Hot & cold streaming platform

**Interface:** IN `{S}` → OUT `{B, S}`&emsp;&emsp;**Verdict:** common

Events in → events out (transformed/joined) + files out (archival); a market event spine: enriched events + daily bundles.

## When to use

Consumers include stream consumers (downstream processors, CEP) and file consumers (analytics, settlement).

## Related

* [batch](/knowledge-concepts/pattern-batch)
* [streaming](/knowledge-concepts/pattern-streaming)
* [data-product](/knowledge-concepts/data-product) — the overall model
* [verdict](/knowledge-concepts/verdict) — what the common / plausible / niche tag means

