---
type: Data Product Type
okf_version: '0.1'
timestamp: '2026-11-08T09:30:00Z'
description: Data product ingesting via human and serving via streaming (pub/sub feed) + human.
title: 'Cell 15.12: human-only → stream + human'
tags:
- data-product-type
- in-h
- out-sh
- common
related:
- /knowledge-concepts/pattern-streaming
- /knowledge-concepts/pattern-human
- /knowledge-concepts/synthetic-stream
- /knowledge-concepts/data-product
- /knowledge-concepts/verdict
---

# 15.12 — human-only → stream + human

**Interface:** IN {H} → OUT {S, H}&emsp;&emsp;**Verdict:** common

A product that takes human-produced data and serves a live feed and a human-facing surface (dashboard/report). People both produce and read the data: the human pattern is on both sides.

![Interface diagram: IN H to OUT SH](/assets/cells/in-h-out-sh.svg)

## When to use

A small group of people both maintains and reads the data, with no machine consumer — a shared, human-scale record rather than an automated interface.

## What's inside

- Ingest: **human entry / curation** — data produced by people (forms, editors, review UIs), validated and audit-trailed on every change.
- Core: a **stream core** that turns each change into an event — **trigger-based**, where each human action delivered through this product's own surface (form submission, approval, entry) is itself a discrete event, or **observed-state**, where a **change-detection engine** manufactures the events by diffing the non-streaming inputs on a refresh cadence
- Serve: a **producer** that emits the event feed to subscribers and a **human-facing surface** (dashboard, report, printout, or review screen) — the layer people actually read.
- State: a durable **state store**, the **event log** (retention), an **audit trail** of human changes, and — in the observed-state shape — a **diff baseline**.

## State & cost

Dominated by the durable state store (grows with entity/state breadth), the event log, and the audit trail of human edits (plus a diff baseline in the observed-state shape). The cost is not infrastructure but discipline: human-entered data needs validation, provenance, and a correction path.

## Watch out

- **Softness is a cost, not a value judgement.** Human-entered data is the softest input — irregular, subjective, error-prone, expensive to re-issue — so it needs **validation, provenance, and a correction path**, and trust leans on the audit trail, not the schedule. It is also the most expensive channel: where a machine source *can* carry the same meaning, prefer it, and keep the human leg for what only a person can supply.
- **Human input can be the value-driver.** Where the human act *is* the value — a judgement, a design intent, creative or social content, an accountable decision — and cannot be automated, human input is the **most valuable input** the product has, and the other legs exist to *enrich* it (see [the role of human input](/knowledge-concepts/role-of-human-input)).
- A human-facing surface inherits the state behind it: the report/dashboard carries every as-of and correctness rule of the store, and a person spots a stale number faster than an API client will.
- **Where the feed is synthetic, and where it is not:** when human actions are delivered through this product's own surface (a submission, an approval, an entry), each action is a discrete, real event and the feed is *not* synthetic. When changes arrive as *modified state* (edited elsewhere, found by refresh), the feed is a **synthetic stream** — "change" is a computed diff bounded by the refresh cadence — and the contract must pin what counts as a change, idempotency, and backfill (see [synthetic stream](/knowledge-concepts/synthetic-stream)).

## The stream: trigger-based or synthetic

This cell serves **S** without taking **S** as input, and it hosts two shapes — only one of which is synthetic:

- **Trigger-based** — a real event stream: the human action itself (a submission, an approval, an entry through this product's own surface) is the discrete event, with its occurrence time. S is absent from the IN side because a person produced the data, not because the events are being manufactured.
- **Observed-state** — a **synthetic stream**: changes in a shared register, sheet, or document reach this product only as modified state, and the events are manufactured by diffing on a refresh cadence (event time = observation time).

In the observed-state shape the contract must pin down the five items (see [synthetic stream](/knowledge-concepts/synthetic-stream)):

1. **What counts as a "change"** — field-level, row version, or full snapshot?
2. **Latency bound** — bounded by the refresh cadence, not source event time.
3. **Idempotency** — re-polling / re-loading must not duplicate events.
4. **Backfill semantics** — how history is (re)issued after a gap or correction.
5. **Ordering** — whether the stream preserves source ordering at all.

## Typical next step

add a **query API** → cell [15.11](/data-product-types/in-h-out-rsh) and add a **bulk file** → cell [15.10](/data-product-types/in-h-out-bhs); or the source world gains a leg this product does not yet take, and it migrates to a richer IN-state on the same row.

## Verdict

**common** — people are the source and people read the data back; where the human contribution *is* the irreplaceable value (content, judgement, curation), this is the natural product and its demand is real wherever this audience exists. It is a costlier build — human input is the softest and most expensive channel — which is exactly why it is built only where a person's contribution is the point.

## Related

* [streaming](/knowledge-concepts/pattern-streaming)
* [human](/knowledge-concepts/pattern-human)
* [synthetic stream](/knowledge-concepts/synthetic-stream) — the observed-state shape of this feed
* [data-product](/knowledge-concepts/data-product) — the overall model
* [verdict](/knowledge-concepts/verdict) — what the common / plausible / niche tag means
