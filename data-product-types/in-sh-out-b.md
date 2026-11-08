---
type: Data Product Type
okf_version: '0.1'
timestamp: '2026-11-08T16:00:00Z'
description: Data product ingesting via streaming (pub/sub feed) + human and serving via batch (bulk/file).
title: 'Cell 12.7: stream + human → batch-only'
tags:
- data-product-type
- in-sh
- out-b
- plausible
related:
- /concepts/pattern-batch
- /concepts/pattern-streaming
- /concepts/pattern-human
- /concepts/data-product
- /concepts/verdict
---

# 12.7 — stream + human → batch-only

**Interface:** IN {S, H} → OUT {B}&emsp;&emsp;**Verdict:** plausible

A product that takes live streams and human-produced data and serves bulk files. Human-entered data is one leg of the source, alongside live streams; the product carries that mix through to bulk files.

![Interface diagram: IN SH to OUT B](/assets/cells/in-sh-out-b.svg)

## When to use

The data is partly human-curated, alongside live streams, and the audience needs it as bulk files — the product is the layer between a person's editing and the consumer.

## What's inside

- Ingest: a **stream consumer** (offsets, replay) for the live leg and **human entry / curation** — data produced by people (forms, editors, review UIs), validated and audit-trailed on every change.
- Core: a **fold/aggregation core** that folds the live leg into queryable state or windowed files
- Serve: a **publication job** that materialises bulk artifacts (files/bundles) with a manifest and as-of.
- State: a durable **state store**, the **feed log** (retention), the **retained bulk artifacts**, and an **audit trail** of human changes.

## State & cost

Dominated by the durable state store (grows with entity/state breadth), the retained bulk artifacts, and the audit trail of human edits.

## Watch out

- **Softness is a cost, not a value judgement.** Human-entered data is the softest input — irregular, subjective, error-prone, expensive to re-issue — so it needs **validation, provenance, and a correction path**, and trust leans on the audit trail, not the schedule. It is also the most expensive channel: where a machine source *can* carry the same meaning, prefer it, and keep the human leg for what only a person can supply.
- **Human input can be the value-driver.** Where the human act *is* the value — a judgement, a design intent, creative or social content, an accountable decision — and cannot be automated, human input is the **most valuable input** the product has, and the other legs exist to *enrich* it (see [the role of human input](/concepts/role-of-human-input)).
- Late and out-of-order events are a **first-class** question: a watermark and a re-issue/correction rule, or history gains holes and duplicate facts.

## Typical next step

add a **human-facing surface** → cell [12.14](/data-product-types/in-sh-out-bh), add a **query API** → cell [12.2](/data-product-types/in-sh-out-br), and add a **feed** → cell [12.3](/data-product-types/in-sh-out-bs); or the source world gains a leg this product does not yet take, and it migrates to a richer IN-state on the same row.

## Verdict

**plausible** — A product that ingests human input layered on top of live feeds and serves bulk files. It is a deliberate, project-shaped choice — not a default pipe — because human input is the softest and costliest channel, so where the value *could* be automated the machine path is preferred; where the human act *is* the irreplaceable value it is the most valuable input the product has and the machine legs exist to *enrich* it.

## Related

* [batch](/concepts/pattern-batch)
* [streaming](/concepts/pattern-streaming)
* [human](/concepts/pattern-human)
* [data-product](/concepts/data-product) — the overall model
* [verdict](/concepts/verdict) — what the common / plausible / niche tag means
