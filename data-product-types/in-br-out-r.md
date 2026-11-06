---
type: Data Product Type
okf_version: "0.1"
timestamp: 2026-11-06T12:50:00Z
description: Data product ingesting via batch (bulk/file) + request/response (on-demand query) and serving via request/response (on-demand query) — upstream facade / proxy api.
title: Cell 2.6: Upstream facade / proxy API
tags:
  - data-product-type
  - in-br
  - out-r
  - common
related:

  - /knowledge-concepts/pattern-batch
  - /knowledge-concepts/pattern-request-response
  - /knowledge-concepts/data-product
---
# 2.6 — Upstream facade / proxy API

**Interface:** IN `{B, R}` → OUT `{R}`&emsp;&emsp;**Verdict:** common

Polled from upstream, served as one cleaner API. Value = schema/semantics + caching, not transformation volume (e.g., a tariff API over supplier web services + rate tables).

## When to use

No transformation-heavy load; the value is integration experience (canonical schema + auth + semantics).

## Related

* [batch](/knowledge-concepts/pattern-batch)
* [request/response](/knowledge-concepts/pattern-request-response)
* [data-product](/knowledge-concepts/data-product) — the overall model

