---
type: Data Product Type
okf_version: '0.1'
timestamp: '2026-11-08T09:30:00Z'
description: Data product ingesting via request/response (on-demand query) + human and serving via batch (bulk/file) + request/response (on-demand query) + human.
title: 'Cell 13.9: API + human → file/API + human'
tags:
- data-product-type
- in-rh
- out-bhr
- common
related:
- /knowledge-concepts/pattern-batch
- /knowledge-concepts/pattern-request-response
- /knowledge-concepts/pattern-human
- /knowledge-concepts/data-product
- /knowledge-concepts/verdict
---

# 13.9 — API + human → file/API + human

**Interface:** IN {R, H} → OUT {B, R, H}&emsp;&emsp;**Verdict:** common

A product that takes on-demand APIs and human-produced data and serves bulk files, a query API, and a human-facing surface (dashboard/report). People both produce and read the data: the human pattern is on both sides.

![Interface diagram: IN RH to OUT BHR](/assets/cells/in-rh-out-bhr.svg)

## When to use

A small group of people both maintains and reads the data, with no machine consumer — a shared, human-scale record rather than an automated interface.

## What's inside

- Ingest: a **poller/connector** over the upstream API (version anchor, pagination, retry) and **human entry / curation** — data produced by people (forms, editors, review UIs), validated and audit-trailed on every change.
- Core: a **merge layer** that unifies human-entered data with the machine legs into one canonical view
- Serve: a **publication job** that materialises bulk artifacts (files/bundles) with a manifest and as-of, a **query service** (the API surface) over the state store, and a **human-facing surface** (dashboard, report, printout, or review screen) — the layer people actually read.
- State: a durable **state store**, the **retained bulk artifacts**, and an **audit trail** of human changes.

## State & cost

Dominated by the durable state store (grows with entity/state breadth), the retained bulk artifacts, and the audit trail of human edits.

## Watch out

- **Softness is a cost, not a value judgement.** Human-entered data is the softest input — irregular, subjective, error-prone, expensive to re-issue — so it needs **validation, provenance, and a correction path**, and trust leans on the audit trail, not the schedule. It is also the most expensive channel: where a machine source *can* carry the same meaning, prefer it, and keep the human leg for what only a person can supply.
- **Human input can be the value-driver.** Where the human act *is* the value — a judgement, a design intent, creative or social content, an accountable decision — and cannot be automated, human input is the **most valuable input** the product has, and the other legs exist to *enrich* it (see [the role of human input](/knowledge-concepts/role-of-human-input)).
- A human-facing surface inherits the state behind it: the report/dashboard carries every as-of and correctness rule of the store, and a person spots a stale number faster than an API client will.

## Typical next step

add a **feed** → cell [13.8](/data-product-types/in-rh-out-brsh) (synthetic only if the human change is observed state rather than delivered actions — see [synthetic stream](/knowledge-concepts/synthetic-stream)); or the source world gains a leg this product does not yet take, and it migrates to a richer IN-state on the same row.

## Verdict

**common** — people are the source and people read the data back; where the human contribution *is* the irreplaceable value (content, judgement, curation), this is the natural product and its demand is real wherever this audience exists. It is a costlier build — human input is the softest and most expensive channel — which is exactly why it is built only where a person's contribution is the point.

## Related

* [batch](/knowledge-concepts/pattern-batch)
* [request/response](/knowledge-concepts/pattern-request-response)
* [human](/knowledge-concepts/pattern-human)
* [data-product](/knowledge-concepts/data-product) — the overall model
* [verdict](/knowledge-concepts/verdict) — what the common / plausible / niche tag means
