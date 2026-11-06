---
type: Data Product Type
okf_version: '0.1'
timestamp: '2026-11-06T12:50:00Z'
description: Data product ingesting via batch (bulk/file) + request/response (on-demand query) and serving via batch (bulk/file) + streaming (pub/sub feed) — rt + eod from polled sources.
title: 'Cell 2.3: RT + EOD from polled sources'
tags:
- data-product-type
- in-br
- out-bs
- plausible
related:
- /knowledge-concepts/pattern-batch
- /knowledge-concepts/pattern-request-response
- /knowledge-concepts/pattern-streaming
- /knowledge-concepts/synthetic-stream
- /knowledge-concepts/data-product
---
# 2.3 — RT + EOD from polled sources

**Interface:** IN `{B, R}` → OUT `{B, S}`&emsp;&emsp;**Verdict:** plausible

Served as both a "live" feed and end-of-day files, but the live feed is re-poll-derived (e.g., polling market data into a stream, plus EOD files).

![Interface diagram: IN BR to OUT BS](/assets/cells/515.svg)

## When to use

Market/utility data consumers expect both a real-time feed and an EOD file, but the upstream is only file/API.

## Watch out

"Real-time" is bounded by poll interval.

## Related

* [batch](/knowledge-concepts/pattern-batch)
* [request/response](/knowledge-concepts/pattern-request-response)
* [streaming](/knowledge-concepts/pattern-streaming)
* [synthetic-stream](/knowledge-concepts/synthetic-stream) — this cell's stream out is not backed by a stream in
* [data-product](/knowledge-concepts/data-product) — the overall model
* [verdict](/knowledge-concepts/verdict) — what the common / plausible / niche tag means

