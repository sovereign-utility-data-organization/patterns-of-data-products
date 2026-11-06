---
type: Knowledge Concept
okf_version: "0.1"
timestamp: 2026-11-06T12:50:00Z
description: A synthetic (pseudo-)stream — a data product that serves a streaming output without a streaming input, deriving events from polling or batch sources.
title: Synthetic stream
tags:
  - streaming
  - anti-pattern
  - semantics
related:
  - /knowledge-concepts/pattern-streaming
  - /knowledge-concepts/pattern-request-response
  - /knowledge-concepts/pattern-batch
  - /knowledge-concepts/data-product
---

# Synthetic stream

A data product whose **output** side includes streaming (`S`) but whose
**input** side does not is producing a *synthetic stream*: it computes
change-detection on top of a non-streaming source (poll-cadence diffs, or
CDC over a batch-refreshed table) and emits the result as events.

## Affected cells (S in OUT only)

| Cell | IN → OUT |
|---|---|
| [2.1](/data-product-types/in-br-out-brs) | `BR → BRS` |
| [2.3](/data-product-types/in-br-out-bs) | `BR → BS` |
| [2.4](/data-product-types/in-br-out-rs) | `BR → RS` |
| [2.5](/data-product-types/in-br-out-s) | `BR → S` |
| [6.1](/data-product-types/in-r-out-brs) | `R → BRS` |
| [6.3](/data-product-types/in-r-out-bs) | `R → BS` |
| [6.4](/data-product-types/in-r-out-rs) | `R → RS` |
| [6.5](/data-product-types/in-r-out-s) | `R → S` |
| [7.1](/data-product-types/in-b-out-brs) | `B → BRS` |
| [7.3](/data-product-types/in-b-out-bs) | `B → BS` |
| [7.4](/data-product-types/in-b-out-rs) | `B → RS` |
| [7.5](/data-product-types/in-b-out-s) | `B → S` |

(Cells with `S` in both IN and OUT are *not* synthetic — see e.g.
[3.7](/data-product-types/in-bs-out-b), [4.6](/data-product-types/in-rs-out-r).)

## Contract items that must be explicit

A synthetic stream is an *illusion over a cadence*. The contract has to pin
down:

1. **What counts as "change"** — field-level diff? row version? whole
   snapshot?
2. **Latency guarantee** — bounded by poll cadence / batch refresh, not by
   the source's event time.
3. **Idempotency** — re-polling / re-loading must not duplicate events.
4. **Backfill semantics** — how history is (re)issued after gaps or
   correction: snapshot-then-delta? delta-only with a version anchor?
5. **Ordering** — whether the stream preserves source ordering at all.

## Rule of thumb

> If the consumer side is built around events, the *producers* of the
> synthetic stream must be able to answer "what changed since last time?"
> deterministically — otherwise the product is a firehose wearing a mask.
