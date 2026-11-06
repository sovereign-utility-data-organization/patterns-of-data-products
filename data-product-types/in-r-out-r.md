---
type: Data Product Type
okf_version: "0.1"
timestamp: 2026-11-06T12:50:00Z
description: Data product ingesting via request/response (on-demand query) and serving via request/response (on-demand query) — api proxy / facade.
title: Cell 6.6: API proxy / facade
tags:
  - data-product-type
  - in-r
  - out-r
  - common
related:

  - /knowledge-concepts/pattern-request-response
  - /knowledge-concepts/data-product
---
# 6.6 — API proxy / facade

**Interface:** IN `{R}` → OUT `{R}`&emsp;&emsp;**Verdict:** common

The cleanest "value = a better surface" product: normalise schemas, add caching/semantics, hide auth quirks, serve one clean API (OData/ESDP façade over supplier REST).

## When to use

No transformation-heavy load; value is integration experience (canonical schema + auth + semantics).

## Related

* [request/response](/knowledge-concepts/pattern-request-response)
* [data-product](/knowledge-concepts/data-product) — the overall model

