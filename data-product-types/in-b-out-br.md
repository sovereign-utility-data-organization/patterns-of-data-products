---
type: Data Product Type
okf_version: "0.1"
timestamp: 2026-11-06T12:50:00Z
description: Data product ingesting via batch (bulk/file) and serving via batch (bulk/file) + request/response (on-demand query) — the classic data warehouse.
title: Cell 7.2: The classic data warehouse
tags:
  - data-product-type
  - in-b
  - out-br
  - common
related:

  - /knowledge-concepts/pattern-batch
  - /knowledge-concepts/pattern-request-response
  - /knowledge-concepts/data-product
---
# 7.2 — The classic data warehouse

**Interface:** IN `{B}` → OUT `{B, R}`&emsp;&emsp;**Verdict:** common

Files in → API + files out. Standard ETL/ELT target that also serves a query API on top (EOD price files → price API + downstream files).

## When to use

Consumers need both an analytical API and bulk delivery; upstream is batch.

## Related

* [batch](/knowledge-concepts/pattern-batch)
* [request/response](/knowledge-concepts/pattern-request-response)
* [data-product](/knowledge-concepts/data-product) — the overall model

