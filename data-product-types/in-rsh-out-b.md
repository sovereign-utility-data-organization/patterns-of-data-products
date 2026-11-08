---
type: Data Product Type
okf_version: '0.1'
timestamp: '2026-11-08T09:30:00Z'
description: Data product ingesting via request/response (on-demand query) + streaming (pub/sub feed) + human and serving via batch (bulk/file).
title: 'Cell 11.7: API/stream + human → batch-only'
tags:
- data-product-type
- in-rsh
- out-b
- plausible
related:
- /knowledge-concepts/pattern-batch
- /knowledge-concepts/pattern-request-response
- /knowledge-concepts/pattern-streaming
- /knowledge-concepts/pattern-human
- /knowledge-concepts/data-product
- /knowledge-concepts/verdict
---

# 11.7 — API/stream + human → batch-only

**Interface:** IN {R, S, H} → OUT {B}&emsp;&emsp;**Verdict:** plausible

A product that takes on-demand APIs, live streams, and human-produced data and serves bulk files. Human-entered data is one leg of the source, alongside upstream APIs and live streams; the product carries that mix through to bulk files.

![Interface diagram: IN RSH to OUT B](/assets/cells/in-rsh-out-b.svg)

## When to use

The data is partly human-curated, alongside upstream APIs and live streams, and the audience needs it as bulk files — the product is the layer between a person's editing and the consumer.

## What's inside

- Ingest: a **poller/connector** over the upstream API (version anchor, pagination, retry), a **stream consumer** (offsets, replay) for the live leg, and **human entry / curation** — data produced by people (forms, editors, review UIs), validated and audit-trailed on every change.
- Core: a **fold/aggregation core** that folds the live leg into queryable state or windowed files and a **merge layer** that unifies human-entered data with the machine legs into one canonical view
- Serve: a **publication job** that materialises bulk artifacts (files/bundles) with a manifest and as-of.
- State: a durable **state store**, the **feed log** (retention), the **retained bulk artifacts**, and an **audit trail** of human changes.

## State & cost

Dominated by the durable state store (grows with entity/state breadth), the retained bulk artifacts, and the audit trail of human edits.

## Watch out

- **Softness is a cost, not a value judgement.** Human-entered data is the softest input — irregular, subjective, error-prone, expensive to re-issue — so it needs **validation, provenance, and a correction path**, and trust leans on the audit trail, not the schedule. It is also the most expensive channel: where a machine source *can* carry the same meaning, prefer it, and keep the human leg for what only a person can supply.
- **Human input can be the value-driver.** Where the human act *is* the value — a judgement, a design intent, creative or social content, an accountable decision — and cannot be automated, human input is the **most valuable input** the product has, and the other legs exist to *enrich* it (see [the role of human input](/knowledge-concepts/role-of-human-input)).
- **Mixed time bases** in the inputs (live vs. poll/cycle/human): fix the authoritative as-of per surface, or each output looks correct alone and wrong cross-checked.
- Late and out-of-order events are a **first-class** question: a watermark and a re-issue/correction rule, or history gains holes and duplicate facts.

## Typical next step

add a **human-facing surface** → cell [11.14](/data-product-types/in-rsh-out-bh), add a **query API** → cell [11.2](/data-product-types/in-rsh-out-br), and add a **feed** → cell [11.3](/data-product-types/in-rsh-out-bs); or the source world gains a leg this product does not yet take, and it migrates to a richer IN-state on the same row.

## Verdict

**plausible** — a product whose *source* is human is a conscious, project-shaped choice, not a default pipe: human input is the most expensive channel, so where it could be meaningfully automated it would usually be. But where the human act *is* the irreplaceable value, it becomes the natural product, and its demand is real wherever this audience exists.

## Related

* [batch](/knowledge-concepts/pattern-batch)
* [request/response](/knowledge-concepts/pattern-request-response)
* [streaming](/knowledge-concepts/pattern-streaming)
* [human](/knowledge-concepts/pattern-human)
* [data-product](/knowledge-concepts/data-product) — the overall model
* [verdict](/knowledge-concepts/verdict) — what the common / plausible / niche tag means
