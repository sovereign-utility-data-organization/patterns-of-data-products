---
type: Data Product Type
okf_version: "0.1"
timestamp: 2026-11-06T12:50:00Z
description: Data product ingesting via batch (bulk/file) and serving via batch (bulk/file) — the pure etl file product.
title: Cell 7.7: The pure ETL file product
tags:
  - data-product-type
  - in-b
  - out-b
  - common
related:

  - /knowledge-concepts/pattern-batch
  - /knowledge-concepts/data-product
---
# 7.7 — The pure ETL file product

**Interface:** IN `{B}` → OUT `{B}`&emsp;&emsp;**Verdict:** common

Files in → files out. The original data product: transformation + publication, no serving stack beyond the file contract (any "settlement input bundle" product).

## When to use

The contract is a file and the load is scheduled; the cheapest possible product.

## Watch out

No live semantics at all — publish with explicit as-of.

## Related

* [batch](/knowledge-concepts/pattern-batch)
* [data-product](/knowledge-concepts/data-product) — the overall model

