---
type: Data Product Type
okf_version: '0.1'
timestamp: '2026-11-06T21:15:00Z'
description: Data product ingesting via batch (bulk/file) + request/response (on-demand query) + streaming (pub/sub feed) + human and serving via human.
title: 'Cell 8.15: Omni-source platform, human read'
tags:
- data-product-type
- in-brsh
- out-h
- common
related:
- /knowledge-concepts/pattern-batch
- /knowledge-concepts/pattern-request-response
- /knowledge-concepts/pattern-streaming
- /knowledge-concepts/pattern-human
- /knowledge-concepts/data-product
- /knowledge-concepts/verdict
---

# 8.15 — Omni-source platform, human read

**Interface:** IN {B, R, S, H} → OUT {H}&emsp;&emsp;**Verdict:** common

Everything the org has — live feeds, APIs, files, *and* human-entered data — consolidated behind one human-facing surface. The BI platform that also eats manual adjustments: the widest IN in the space serving the surface people use every day.

![Interface diagram: IN BRSH to OUT H](/assets/cells/in-brsh-out-h.svg)

## When to use

When a dashboard/report must reflect live data, upstream APIs, bulk files, *and* human-curated adjustments, all in one view for people — a full BI/console product.

## What's inside

- Ingest: a scheduled **bulk ingest** (pickup, parse, validate, load), a **poller/connector** over the upstream API (version anchor, pagination, retry), a **stream consumer** (offsets, replay) for the live leg, and **human entry / curation** — data produced by people (forms, editors, review UIs), validated and audit-trailed on every change.
- Core: a **transform** (filter/shape/route) over the live leg and a **merge layer** that unifies human-entered data with the machine legs into one canonical view
- Serve: a **human-facing surface** (dashboard, report, printout, or review screen) — the layer people actually read.
- State: a durable **state store**, the **feed log** (retention), and an **audit trail** of human changes.

## State & cost

Dominated by the durable state store (grows with entity/state breadth) and the audit trail of human edits. Serving people is cheap to run and cheap to trust — a presentation layer over a queryable backend.

## Watch out

- Human-entered data is the softest input: it arrives irregularly, carries intent and errors, and needs **validation, provenance, and a correction path** — trust leans on the audit trail, not the schedule.
- A human-facing surface inherits the state behind it: the report/dashboard carries every as-of and correctness rule of the store, and a person spots a stale number faster than an API client will.
- **Mixed time bases** in the inputs (live vs. poll/cycle/human): fix the authoritative as-of per surface, or each output looks correct alone and wrong cross-checked.

## Typical next step

add a **query API** → cell [8.13](/data-product-types/in-brsh-out-rh), add a **bulk file** → cell [8.14](/data-product-types/in-brsh-out-bh), and add a **feed** → cell [8.12](/data-product-types/in-brsh-out-sh); or the source world gains a leg this product does not yet take, and it migrates to a richer IN-state on the same row.

## Verdict

**common** — 'one view for people over everything' is the defining product of any consolidated-data estate (BI/CDP); expensive to build, but the demand is universal.

## Related

* [batch](/knowledge-concepts/pattern-batch)
* [request/response](/knowledge-concepts/pattern-request-response)
* [streaming](/knowledge-concepts/pattern-streaming)
* [human](/knowledge-concepts/pattern-human)
* [data-product](/knowledge-concepts/data-product) — the overall model
* [verdict](/knowledge-concepts/verdict) — what the common / plausible / niche tag means
