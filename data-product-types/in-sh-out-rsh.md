---
type: Data Product Type
okf_version: '0.1'
timestamp: '2026-11-08T16:00:00Z'
description: Data product ingesting via streaming (pub/sub feed) + human and serving via request/response (on-demand query) + streaming (pub/sub feed) + human.
title: 'Cell 12.11: stream + human → API/stream + human'
tags:
- data-product-type
- in-sh
- out-rsh
- common
related:
- /concepts/pattern-request-response
- /concepts/pattern-streaming
- /concepts/pattern-human
- /concepts/data-product
- /concepts/verdict
---

# 12.11 — stream + human → API/stream + human

**Interface:** IN {S, H} → OUT {R, S, H}&emsp;&emsp;**Verdict:** common

A product that takes live streams and human-produced data and serves a query API, a live feed, and a human-facing surface (dashboard/report). People both produce and read the data: the human pattern is on both sides.

![Interface diagram: IN SH to OUT RSH](/assets/cells/in-sh-out-rsh.svg)

## When to use

A small group of people both maintains and reads the data, with no machine consumer — a shared, human-scale record rather than an automated interface.

## What's inside

- Ingest: a **stream consumer** (offsets, replay) for the live leg and **human entry / curation** — data produced by people (forms, editors, review UIs), validated and audit-trailed on every change.
- Core: a **fold/aggregation core** that folds the live leg into queryable state or windowed files
- Serve: a **query service** (the API surface) over the state store, a **producer** re-exposing the (transformed) live feed, and a **human-facing surface** (dashboard, report, printout, or review screen) — the layer people actually read.
- State: a durable **state store**, the **feed log** (retention), and an **audit trail** of human changes.

## State & cost

Dominated by the durable state store (grows with entity/state breadth), the input and output feed logs, and the audit trail of human edits.

## Watch out

- **Softness is a cost, not a value judgement.** Human-entered data is the softest input — irregular, subjective, error-prone, expensive to re-issue — so it needs **validation, provenance, and a correction path**, and trust leans on the audit trail, not the schedule. It is also the most expensive channel: where a machine source *can* carry the same meaning, prefer it, and keep the human leg for what only a person can supply.
- **Human input can be the value-driver.** Where the human act *is* the value — a judgement, a design intent, creative or social content, an accountable decision — and cannot be automated, human input is the **most valuable input** the product has, and the other legs exist to *enrich* it (see [the role of human input](/concepts/role-of-human-input)).
- A human-facing surface inherits the state behind it: the report/dashboard carries every as-of and correctness rule of the store, and a person spots a stale number faster than an API client will.
- Late and out-of-order events are a **first-class** question: a watermark and a re-issue/correction rule, or history gains holes and duplicate facts.

## Typical next step

add a **bulk file** → cell [12.8](/data-product-types/in-sh-out-brsh); or the source world gains a leg this product does not yet take, and it migrates to a richer IN-state on the same row.

## Verdict

**common** — A product that ingests human input layered on top of live feeds and serves query APIs and live feeds plus a human-facing surface (a dashboard, report, or review). It is a natural fit where the human act *is* the value — a judgement, a decision, a curated record — so the softest, costliest channel is then the *cost of having that value*; where the act *could* be automated the cheaper machine path wins.

## Related

* [request/response](/concepts/pattern-request-response)
* [streaming](/concepts/pattern-streaming)
* [human](/concepts/pattern-human)
* [data-product](/concepts/data-product) — the overall model
* [verdict](/concepts/verdict) — what the common / plausible / niche tag means
