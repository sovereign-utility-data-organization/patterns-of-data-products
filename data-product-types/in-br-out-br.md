---
type: Data Product Type
okf_version: '0.1'
timestamp: '2026-11-08T19:24:00Z'
description: Data product ingesting via batch (bulk/file) + request/response (on-demand query) and serving via batch (bulk/file) + request/response (on-demand query) — classic data api + file feed.
definition: "The bread and butter: refresh from feeds and APIs, serve a clean API plus daily bundles (a weather/price API that also serves files). Files and an API in; API and files out: the refreshed hub of the reference world. The product is a canonical store refreshed from two inputs, serving both an online query and a bulk file."
example: "Consumers are a mix of online pollers and ETL consumers; no live requirement."
altLabel:
- "BR → BR"
- "Cell 2.2"
- "Classic data API + file feed"
title: 'Cell 2.2: Classic data API + file feed'
tags:
- data-product-type
- in-br
- out-br
- common
related:
- /concepts/pattern-batch
- /concepts/pattern-request-response
- /concepts/data-product
---

# 2.2 — Classic data API + file feed

**Interface:** IN `{B, R}` → OUT `{B, R}`&emsp;&emsp;**Verdict:** common

The bread and butter: refresh from feeds and APIs, serve a clean API plus daily bundles (a weather/price API that also serves files). Files and an API in; API and files out: the refreshed hub of the reference world. The product is a canonical store refreshed from two inputs, serving both an online query and a bulk file.

![Interface diagram: IN BR to OUT BR](/assets/cells/298.svg)

## When to use

Consumers are a mix of online pollers and ETL consumers; no live requirement.

Consumers need both a queryable reference and a bulk file, and the source is a batch feed plus a polled/lookup API (a master-data or tariff hub) — no streaming requirement.

## What's inside

- A **batch loader** for the file leg plus a **poller/connector** (anchor) for the API leg, feeding a **canonical store**.
- A **merge/transform** reconciling the two inputs into the canonical model.
- A **query service** (API) and a **publication job** (file) over the same store.
- State: the canonical store, the API anchor, and the last published file.

## State & cost

The canonical store is the cost centre, refreshed and re-merged every cycle — it grows with the breadth of the reference, not the volume of changes. Plus the file artifacts and the anchor. Heavier than a 2.7 (the query store) and the default "reference hub" footprint.

## Watch out

- The API and the file surfaces must reflect the same merged and committed state; a publication that reads the store mid-merge will produce a file that disagrees with the API.
- The two input legs have different freshness (a file load vs a poll); the store must state which as-of applies per field, or a consumer will treat a stale polled field as current.

## Typical next step

Growth is adding the live surface: a change-reactive consumer appears and a synthetic change feed over the anchor is added — **cell 2.1** (full) or **2.3** (feed + file). A push feed or a second API leg broadens IN toward **row 4**/**row 1**. A steady-state reference hub often lands here and stays.

## Verdict

**common** — the canonical refreshed reference hub — the common, defensible answer to "give us a clean queryable reference plus a bulk file over a batch-plus-API source."

## Related

* [batch](/concepts/pattern-batch)
* [request/response](/concepts/pattern-request-response)
* [data-product](/concepts/data-product) — the overall model
* [verdict](/concepts/verdict) — what the common / plausible / niche tag means
