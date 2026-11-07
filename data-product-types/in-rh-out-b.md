---
type: Data Product Type
okf_version: '0.1'
timestamp: '2026-11-07T09:00:00Z'
description: Data product ingesting via request/response (on-demand query) + human and serving via batch (bulk/file).
title: 'Cell 13.7: API + human → batch-only'
tags:
- data-product-type
- in-rh
- out-b
- plausible
related:
- /knowledge-concepts/pattern-batch
- /knowledge-concepts/pattern-request-response
- /knowledge-concepts/pattern-human
- /knowledge-concepts/data-product
- /knowledge-concepts/verdict
---

# 13.7 — API + human → batch-only

**Interface:** IN {R, H} → OUT {B}&emsp;&emsp;**Verdict:** plausible

A product that takes on-demand APIs and human-produced data and serves bulk files. Human-entered data is one leg of the source, alongside upstream APIs; the product carries that mix through to bulk files.

![Interface diagram: IN RH to OUT B](/assets/cells/in-rh-out-b.svg)

## When to use

The data is partly human-curated, alongside upstream APIs, and the audience needs it as bulk files — the product is the layer between a person's editing and the consumer.

## What's inside

- Ingest: a **poller/connector** over the upstream API (version anchor, pagination, retry) and **human entry / curation** — data produced by people (forms, editors, review UIs), validated and audit-trailed on every change.
- Core: a **merge layer** that unifies human-entered data with the machine legs into one canonical view
- Serve: a **publication job** that materialises bulk artifacts (files/bundles) with a manifest and as-of.
- State: a durable **state store**, the **retained bulk artifacts**, and an **audit trail** of human changes.

## State & cost

Dominated by the durable state store (grows with entity/state breadth), the retained bulk artifacts, and the audit trail of human edits.

## Watch out

- Human-entered data is the softest input: it arrives irregularly, carries intent and errors, and needs **validation, provenance, and a correction path** — trust leans on the audit trail, not the schedule.

## Typical next step

add a **human-facing surface** → cell [13.14](/data-product-types/in-rh-out-bh), add a **query API** → cell [13.2](/data-product-types/in-rh-out-br), and add a **feed** → cell [13.3](/data-product-types/in-rh-out-bs) (synthetic only if the human change is observed state rather than delivered actions — see [synthetic stream](/knowledge-concepts/synthetic-stream)); or the source world gains a leg this product does not yet take, and it migrates to a richer IN-state on the same row.

## Verdict

**plausible** — turning human-entered data into a downstream surface is sensible but project-shaped — a curation product, not a default pipe, and its demand is real where this audience exists.

## Related

* [batch](/knowledge-concepts/pattern-batch)
* [request/response](/knowledge-concepts/pattern-request-response)
* [human](/knowledge-concepts/pattern-human)
* [data-product](/knowledge-concepts/data-product) — the overall model
* [verdict](/knowledge-concepts/verdict) — what the common / plausible / niche tag means
