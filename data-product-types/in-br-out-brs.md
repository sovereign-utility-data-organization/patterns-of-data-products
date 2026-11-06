---
type: Data Product Type
okf_version: "0.1"
timestamp: 2026-11-06T12:50:00Z
description: Data product ingesting via batch (bulk/file) + request/response (on-demand query) and serving via batch (bulk/file) + request/response (on-demand query) + streaming (pub/sub feed) — refreshed model serving all three out.
title: Cell 2.1: Refreshed model serving all three out
tags:
  - data-product-type
  - in-br
  - out-brs
  - plausible
related:

  - /knowledge-concepts/pattern-batch
  - /knowledge-concepts/pattern-request-response
  - /knowledge-concepts/pattern-streaming
  - /knowledge-concepts/synthetic-stream
  - /knowledge-concepts/data-product
---
# 2.1 — Refreshed model serving all three out

**Interface:** IN `{B, R}` → OUT `{B, R, S}`&emsp;&emsp;**Verdict:** plausible

A polled/file-fed state store that publishes a *synthetic* change stream in addition to API + files.

## When to use

Consumers need events, but the source world only offers files/APIs — the product computes change detection.

## Watch out

Streams derived from polling are chatty and lossy-ish; define "change" semantics explicitly.

## Related

* [batch](/knowledge-concepts/pattern-batch)
* [request/response](/knowledge-concepts/pattern-request-response)
* [streaming](/knowledge-concepts/pattern-streaming)
* [synthetic-stream](/knowledge-concepts/synthetic-stream) — this cell's stream out is not backed by a stream in
* [data-product](/knowledge-concepts/data-product) — the overall model

