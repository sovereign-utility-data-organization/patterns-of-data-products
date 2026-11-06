---
type: Data Product Type
okf_version: "0.1"
timestamp: 2026-11-06T12:50:00Z
description: Data product ingesting via batch (bulk/file) + request/response (on-demand query) + streaming (pub/sub feed) and serving via batch (bulk/file) + request/response (on-demand query) + streaming (pub/sub feed) — data platform / warehouse facade.
title: Cell 1.1: Data platform / warehouse facade
tags:
  - data-product-type
  - in-brs
  - out-brs
  - common
related:

  - /knowledge-concepts/pattern-batch
  - /knowledge-concepts/pattern-request-response
  - /knowledge-concepts/pattern-streaming
  - /knowledge-concepts/data-product
---
# 1.1 — Data platform / warehouse facade

**Interface:** IN `{B, R, S}` → OUT `{B, R, S}`&emsp;&emsp;**Verdict:** common

Ingests from files, on-demand upstreams, and live streams; serves live events, on-demand queries, *and* bulk files. The full data platform (data lakehouse, CDP).

## When to use

One organisation must serve many consumer types (BI, API clients, settlement, real-time dashboards) from a consolidated view.

## Watch out

The most expensive option — the product owns all three serving stacks.

## Related

* [batch](/knowledge-concepts/pattern-batch)
* [request/response](/knowledge-concepts/pattern-request-response)
* [streaming](/knowledge-concepts/pattern-streaming)
* [data-product](/knowledge-concepts/data-product) — the overall model

