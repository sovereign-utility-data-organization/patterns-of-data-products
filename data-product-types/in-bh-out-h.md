---
type: Data Product Type
okf_version: '0.1'
timestamp: '2026-11-07T09:00:00Z'
description: Data product ingesting via batch (bulk/file) + human and serving via human.
title: 'Cell 14.15: file + human → human-only'
tags:
- data-product-type
- in-bh
- out-h
- plausible
related:
- /knowledge-concepts/pattern-batch
- /knowledge-concepts/pattern-human
- /knowledge-concepts/data-product
- /knowledge-concepts/verdict
---

# 14.15 — file + human → human-only

**Interface:** IN {B, H} → OUT {H}&emsp;&emsp;**Verdict:** plausible

A product that takes files (batch) and human-produced data and serves a human-facing surface (dashboard/report). People both produce and read the data: the human pattern is on both sides.

![Interface diagram: IN BH to OUT H](/assets/cells/in-bh-out-h.svg)

## When to use

A small group of people both maintains and reads the data, with no machine consumer — a shared, human-scale record rather than an automated interface.

## What's inside

- Ingest: a scheduled **bulk ingest** (pickup, parse, validate, load) and **human entry / curation** — data produced by people (forms, editors, review UIs), validated and audit-trailed on every change.
- Core: a **merge layer** that unifies human-entered data with the machine legs into one canonical view
- Serve: a **human-facing surface** (dashboard, report, printout, or review screen) — the layer people actually read.
- State: a durable **state store** and an **audit trail** of human changes.

## State & cost

Dominated by the durable state store (grows with entity/state breadth) and the audit trail of human edits. Serving people is cheap to run and cheap to trust — a presentation layer over a queryable backend.

## Watch out

- Human-entered data is the softest input: it arrives irregularly, carries intent and errors, and needs **validation, provenance, and a correction path** — trust leans on the audit trail, not the schedule.
- A human-facing surface inherits the state behind it: the report/dashboard carries every as-of and correctness rule of the store, and a person spots a stale number faster than an API client will.

## Typical next step

add a **query API** → cell [14.13](/data-product-types/in-bh-out-rh), add a **bulk file** → cell [14.14](/data-product-types/in-bh-out-bh), and add a **feed** → cell [14.12](/data-product-types/in-bh-out-sh) (synthetic only if the human change is observed state rather than delivered actions — see [synthetic stream](/knowledge-concepts/synthetic-stream)); or the source world gains a leg this product does not yet take, and it migrates to a richer IN-state on the same row.

## Verdict

**plausible** — people both feed and read the data, so it is a natural product, and its demand is real where this audience exists.

## Related

* [batch](/knowledge-concepts/pattern-batch)
* [human](/knowledge-concepts/pattern-human)
* [data-product](/knowledge-concepts/data-product) — the overall model
* [verdict](/knowledge-concepts/verdict) — what the common / plausible / niche tag means
