---
type: Data Product Type
okf_version: "0.1"
timestamp: 2026-11-06T12:50:00Z
description: Data product ingesting via streaming (pub/sub feed) and serving via request/response (on-demand query) + streaming (pub/sub feed) — event + state, no files.
title: Cell 5.4: Event + state, no files
tags:
  - data-product-type
  - in-s
  - out-rs
  - niche
related:

  - /knowledge-concepts/pattern-request-response
  - /knowledge-concepts/pattern-streaming
  - /knowledge-concepts/data-product
---
# 5.4 — Event + state, no files

**Interface:** IN `{S}` → OUT `{R, S}`&emsp;&emsp;**Verdict:** niche

Stream in → event feed + state API; no bulk out (archival handled off-product).

## When to use

All consumers are online and archival is a separate product's job.

## Watch out

Same retention concern as the file-less serving cells — verify where history lives.

## Related

* [request/response](/knowledge-concepts/pattern-request-response)
* [streaming](/knowledge-concepts/pattern-streaming)
* [data-product](/knowledge-concepts/data-product) — the overall model

