---
type: Knowledge Concept
okf_version: '0.1'
timestamp: '2026-11-08T19:52:00Z'
definition: "A stream a product manufactures rather than relays: the source exposes state, not events - a batch table, a bulk file, a register or document updated out of band - and the product computes change detection (poll-cadence diffs, or CDC over an observed refresh) and emits the result as events; event time equals observation time, not occurrence time."
example: "A product polling a state-only API on a cadence and emitting a change-detection feed (cells 2.5, 6.5), or CDC over a batch-refreshed table (cell 7.5)"
altLabel:
- "pseudo-stream"
- "manufactured feed"
- "diff-based feed"
- "S in OUT, no S in IN"
scopeNote: "The red flag - S in OUT but not in IN (56 cells) - is reliable for machine IN sides (rows BR, R, B); for H-in cells it is shape-dependent: a human action delivered through the product's own surface is a real trigger-based event, not a synthetic one. A synthetic stream must pin down change semantics, latency, idempotency, backfill, and ordering explicitly."
title: Synthetic stream
tags:
- streaming
- anti-pattern
- semantics
related:
- /concepts/pattern-streaming
- /concepts/pattern-request-response
- /concepts/pattern-batch
- /concepts/pattern-human
- /concepts/data-product
---
# Synthetic stream

A data product emits a **synthetic stream** when it *manufactures* the events
it serves: the source exposes **state, not events** — a batch table, a bulk
file, a register or document updated out of band — and the product computes
change-detection (poll-cadence diffs, or CDC over a table it observed being
refreshed) and emits the result as events. The signature is temporal:
**event time = observation time**, not occurrence time.

## When a stream is *not* synthetic

- **Machine source:** if the source genuinely exposes events, the IN side is
  `S` in the first place — that is what the `S` leg means. The flag below only
  bites when the source has no event leg of its own.
- **Human action:** an action delivered through the product's own surface — a
  form submission, an approval, an entry — is itself a discrete event with an
  occurrence time. Relaying those actions as a feed is a **trigger-based**
  (real) event stream *even though the IN side has no `S`*: `H` is there
  because a person produced the data, not because the events are being
  manufactured.

## Red flag: S in OUT, not in IN

The operational red flag in this space is *S in the **OUT** set but not the
**IN** set* — **56 cells** — but it is a red flag, not the definition, and its
force depends on what the IN side is:

- **Machine IN** (rows `BR`, `R`, `B`): the source exposes state only, so the
  flag is reliable — the feed is synthetic. In the original three-pattern
  space that is exactly **12 cells**, the machine-only table below:

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

- **`H` in OUT only** (e.g. [2.8](/data-product-types/in-br-out-brsh),
  [6.8](/data-product-types/in-r-out-brsh), [7.8](/data-product-types/in-b-out-brsh)):
  the source is the same state-only machine and the `H` is a human reader on
  top of the feed — synthetic, like the machine cells.
- **`H` in IN** (rows `BHR`, `RH`, `BH`, `H` — the remaining 32 cells of the
  flag set): the flag is **shape-dependent** — the same cell can host a
  *trigger-based* feed (human actions delivered through the product's own
  surface) or an *observed-state* feed (a shared register, sheet, or document
  the product discovers by refresh). The contract must state which shape it
  is.

(Cells with `S` in both IN and OUT are *not* synthetic — see e.g.
[3.7](/data-product-types/in-bs-out-b), [4.6](/data-product-types/in-rs-out-r).)

## Contract items that must be explicit (observed-state shape)

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

> If the consumer side is built around events, the *producers* of a
> synthetic stream must be able to answer "what changed since last time?"
> deterministically — otherwise the product is a firehose wearing a mask.
