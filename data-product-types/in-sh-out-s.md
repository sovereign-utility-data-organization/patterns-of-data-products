---
type: Data Product Type
okf_version: '0.1'
timestamp: '2026-11-08T09:30:00Z'
description: Data product ingesting via streaming (pub/sub feed) + human and serving via streaming (pub/sub feed).
title: 'Cell 12.5: stream + human → stream-only'
tags:
- data-product-type
- in-sh
- out-s
- plausible
related:
- /knowledge-concepts/pattern-streaming
- /knowledge-concepts/pattern-human
- /knowledge-concepts/data-product
- /knowledge-concepts/verdict
---

# 12.5 — stream + human → stream-only

**Interface:** IN {S, H} → OUT {S}&emsp;&emsp;**Verdict:** plausible

A product that takes live streams and human-produced data and serves a live feed. Human-entered data is one leg of the source, alongside live streams; the product carries that mix through to a live feed.

![Interface diagram: IN SH to OUT S](/assets/cells/in-sh-out-s.svg)

## When to use

The data is partly human-curated, alongside live streams, and the audience needs it as a live feed — the product is the layer between a person's editing and the consumer.

## What's inside

- Ingest: a **stream consumer** (offsets, replay) for the live leg and **human entry / curation** — data produced by people (forms, editors, review UIs), validated and audit-trailed on every change.
- Core: a **transform** (filter/shape/route) over the live leg
- Serve: a **producer** re-exposing the (transformed) live feed.
- State: a durable **state store**, the **feed log** (retention), and an **audit trail** of human changes.

## State & cost

Dominated by the durable state store (grows with entity/state breadth), the input and output feed logs, and the audit trail of human edits.

## Watch out

- **Softness is a cost, not a value judgement.** Human-entered data is the softest input — irregular, subjective, error-prone, expensive to re-issue — so it needs **validation, provenance, and a correction path**, and trust leans on the audit trail, not the schedule. It is also the most expensive channel: where a machine source *can* carry the same meaning, prefer it, and keep the human leg for what only a person can supply.
- **Human input can be the value-driver.** Where the human act *is* the value — a judgement, a design intent, creative or social content, an accountable decision — and cannot be automated, human input is the **most valuable input** the product has, and the other legs exist to *enrich* it (see [the role of human input](/knowledge-concepts/role-of-human-input)).

## Typical next step

add a **human-facing surface** → cell [12.12](/data-product-types/in-sh-out-sh), add a **query API** → cell [12.4](/data-product-types/in-sh-out-rs), and add a **bulk file** → cell [12.3](/data-product-types/in-sh-out-bs); or the source world gains a leg this product does not yet take, and it migrates to a richer IN-state on the same row.

## Verdict

**plausible** — a product whose *source* is human is a conscious, project-shaped choice, not a default pipe: human input is the most expensive channel, so where it could be meaningfully automated it would usually be. But where the human act *is* the irreplaceable value, it becomes the natural product, and its demand is real wherever this audience exists.

## Related

* [streaming](/knowledge-concepts/pattern-streaming)
* [human](/knowledge-concepts/pattern-human)
* [data-product](/knowledge-concepts/data-product) — the overall model
* [verdict](/knowledge-concepts/verdict) — what the common / plausible / niche tag means
