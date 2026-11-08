---
type: Data Product Type
okf_version: '0.1'
timestamp: '2026-11-08T16:00:00Z'
description: Data product ingesting via batch (bulk/file) + request/response (on-demand query) + streaming (pub/sub feed) and serving via batch (bulk/file) + streaming (pub/sub feed) + human.
title: 'Cell 1.10: omni-channel → file/stream + human'
tags:
- data-product-type
- in-brs
- out-bhs
- common
related:
- /concepts/pattern-batch
- /concepts/pattern-request-response
- /concepts/pattern-streaming
- /concepts/pattern-human
- /concepts/data-product
- /concepts/verdict
---

# 1.10 — omni-channel → file/stream + human

**Interface:** IN {B, R, S} → OUT {B, S, H}&emsp;&emsp;**Verdict:** common

A product that takes files (batch), on-demand APIs, and live streams and serves bulk files, a live feed, and a human-facing surface (dashboard/report). Machine-side inputs ({B, R, S}) drive it — the multi-surface serves people, not just machines.

![Interface diagram: IN BRS to OUT BHS](/assets/cells/in-brs-out-bhs.svg)

## When to use

The data the audience wants is real, but the reader is a person, not a service: they need a report or dashboard over live data, upstream APIs, and bulk files, not raw events or a bulk drop.

## What's inside

- Ingest: a scheduled **bulk ingest** (pickup, parse, validate, load), a **poller/connector** over the upstream API (version anchor, pagination, retry), and a **stream consumer** (offsets, replay) for the live leg.
- Core: a **fold/aggregation core** that folds the live leg into queryable state or windowed files and a **merge/normalisation core** unifying the non-streaming legs into one canonical view
- Serve: a **publication job** that materialises bulk artifacts (files/bundles) with a manifest and as-of, a **producer** re-exposing the (transformed) live feed, and a **human-facing surface** (dashboard, report, printout, or review screen) — the layer people actually read.
- State: a durable **state store**, the **feed log** (retention), and the **retained bulk artifacts**.

## State & cost

Dominated by the durable state store (grows with entity/state breadth), the input and output feed logs, and the retained bulk artifacts.

## Watch out

- A human-facing surface inherits the state behind it: the report/dashboard carries every as-of and correctness rule of the store, and a person spots a stale number faster than an API client will.
- **Mixed time bases** in the inputs (live vs. poll/cycle/human): fix the authoritative as-of per surface, or each output looks correct alone and wrong cross-checked.
- Late and out-of-order events are a **first-class** question: a watermark and a re-issue/correction rule, or history gains holes and duplicate facts.
- A published file is a **completeness claim**: a manifest-first publish and a supersession rule belong in the contract.
- This is machine-produced, human-read: make sure a person actually reviews/approves the served view rather than the pipeline writing it straight through.

## Typical next step

add **human curation on the input side** → cell [8.10](/data-product-types/in-brsh-out-bhs) when the data should not be purely machine-fed and add a **query API** → cell [1.8](/data-product-types/in-brs-out-brsh); or the source world gains a leg this product does not yet take, and it migrates to a richer IN-state on the same row.

## Verdict

**common** — A product that ingests bulk files, query APIs, and live feeds and serves bulk files and live feeds plus a human-facing surface (a dashboard, report, or review). It is the right shape where the reader is a person rather than a service, and the human-shaped view is itself what the next consumer — or the next machine in the loop — needs to act on.

## Related

* [batch](/concepts/pattern-batch)
* [request/response](/concepts/pattern-request-response)
* [streaming](/concepts/pattern-streaming)
* [human](/concepts/pattern-human)
* [data-product](/concepts/data-product) — the overall model
* [verdict](/concepts/verdict) — what the common / plausible / niche tag means
