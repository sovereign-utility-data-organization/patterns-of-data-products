---
type: Data Product Type
okf_version: '0.1'
timestamp: '2026-11-06T21:15:00Z'
description: Data product ingesting via human and serving via streaming (pub/sub feed).
title: 'Cell 15.5: human-only → stream-only'
tags:
- data-product-type
- in-h
- out-s
- plausible
related:
- /knowledge-concepts/pattern-streaming
- /knowledge-concepts/pattern-human
- /knowledge-concepts/synthetic-stream
- /knowledge-concepts/data-product
- /knowledge-concepts/verdict
---

# 15.5 — human-only → stream-only

**Interface:** IN {H} → OUT {S}&emsp;&emsp;**Verdict:** plausible

A product that takes human-produced data and serves a live feed. Human-entered data is the source; the product turns what people put in into a live feed for downstream use.

![Interface diagram: IN H to OUT S](/assets/cells/in-h-out-s.svg)

## When to use

Data originates with people (entry, review, curation) rather than a machine source, and the audience needs it as a live feed — the product is what stands between a person's editing and the consumer.

## What's inside

- Ingest: **human entry / curation** — data produced by people (forms, editors, review UIs), validated and audit-trailed on every change.
- Core: a **change-detection engine** that manufactures the feed off the non-streaming inputs
- Serve: a **change-detection layer** diffing each refresh, driving a **producer** (a *synthetic* feed).
- State: a **diff baseline**, the **feed log** (retention), and an **audit trail** of human changes.

## State & cost

Light on durable state: the diff baseline plus the manufactured feed's log and the audit trail of human edits. The cost is not infrastructure but discipline: human-entered data needs validation, provenance, and a correction path.

## Watch out

- Human-entered data is the softest input: it arrives irregularly, carries intent and errors, and needs **validation, provenance, and a correction path** — trust leans on the audit trail, not the schedule.
- The **feed is synthetic** (S out, not in): "change" is a computed diff bounded by the refresh cadence — pin what counts as a change, idempotency, and backfill.

## Synthetic stream

This cell serves **S** without taking **S** as input, so its stream is a **synthetic stream**: change-detection computed on top of a non-streaming source. The contract must pin down the five items (see [synthetic stream](/knowledge-concepts/synthetic-stream)):

1. **What counts as a "change"** — field-level, row version, or full snapshot?
2. **Latency bound** — bounded by the refresh cadence, not source event time.
3. **Idempotency** — re-polling / re-loading must not duplicate events.
4. **Backfill semantics** — how history is (re)issued after a gap or correction.
5. **Ordering** — whether the stream preserves source ordering at all.

## Typical next step

add a **human-facing surface** → cell [15.12](/data-product-types/in-h-out-sh), add a **query API** → cell [15.4](/data-product-types/in-h-out-rs), and add a **bulk file** → cell [15.3](/data-product-types/in-h-out-bs); or the source world gains a leg this product does not yet take, and it migrates to a richer IN-state on the same row.

## Verdict

**plausible** — turning human-entered data into a downstream surface is sensible but project-shaped — a curation product, not a default pipe, and its demand is real where this audience exists.

## Related

* [streaming](/knowledge-concepts/pattern-streaming)
* [human](/knowledge-concepts/pattern-human)
* [synthetic stream](/knowledge-concepts/synthetic-stream) — the pseudo-stream hazard
* [data-product](/knowledge-concepts/data-product) — the overall model
* [verdict](/knowledge-concepts/verdict) — what the common / plausible / niche tag means
