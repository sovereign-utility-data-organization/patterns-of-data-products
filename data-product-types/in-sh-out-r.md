---
type: Data Product Type
okf_version: '0.1'
timestamp: '2026-11-08T19:24:00Z'
description: Data product ingesting via streaming (pub/sub feed) + human and serving via request/response (on-demand query).
definition: "A product that takes live streams and human-produced data and serves a query API. Human-entered data is one leg of the source, alongside live streams; the product carries that mix through to a query API."
example: "The data is partly human-curated, alongside live streams, and the audience needs it as a query API — the product is the layer between a person's editing and the consumer."
altLabel:
- "SH → R"
- "Cell 12.6"
- "stream + human → request-response-only"
title: 'Cell 12.6: stream + human → request-response-only'
tags:
- data-product-type
- in-sh
- out-r
- plausible
related:
- /concepts/pattern-request-response
- /concepts/pattern-streaming
- /concepts/pattern-human
- /concepts/data-product
- /concepts/verdict
---

# 12.6 — stream + human → request-response-only

**Interface:** IN {S, H} → OUT {R}&emsp;&emsp;**Verdict:** plausible

A product that takes live streams and human-produced data and serves a query API. Human-entered data is one leg of the source, alongside live streams; the product carries that mix through to a query API.

![Interface diagram: IN SH to OUT R](/assets/cells/in-sh-out-r.svg)

## When to use

The data is partly human-curated, alongside live streams, and the audience needs it as a query API — the product is the layer between a person's editing and the consumer.

## What's inside

- Ingest: a **stream consumer** (offsets, replay) for the live leg and **human entry / curation** — data produced by people (forms, editors, review UIs), validated and audit-trailed on every change.
- Core: a **fold/aggregation core** that folds the live leg into queryable state or windowed files
- Serve: a **query service** (the API surface) over the state store.
- State: a durable **state store**, the **feed log** (retention), and an **audit trail** of human changes.

## State & cost

Dominated by the durable state store (grows with entity/state breadth) and the audit trail of human edits.

## Watch out

- **Softness is a cost, not a value judgement.** Human-entered data is the softest input — irregular, subjective, error-prone, expensive to re-issue — so it needs **validation, provenance, and a correction path**, and trust leans on the audit trail, not the schedule. It is also the most expensive channel: where a machine source *can* carry the same meaning, prefer it, and keep the human leg for what only a person can supply.
- **Human input can be the value-driver.** Where the human act *is* the value — a judgement, a design intent, creative or social content, an accountable decision — and cannot be automated, human input is the **most valuable input** the product has, and the other legs exist to *enrich* it (see [the role of human input](/concepts/role-of-human-input)).
- Late and out-of-order events are a **first-class** question: a watermark and a re-issue/correction rule, or history gains holes and duplicate facts.

## Typical next step

add a **human-facing surface** → cell [12.13](/data-product-types/in-sh-out-rh), add a **bulk file** → cell [12.2](/data-product-types/in-sh-out-br), and add a **feed** → cell [12.4](/data-product-types/in-sh-out-rs); or the source world gains a leg this product does not yet take, and it migrates to a richer IN-state on the same row.

## Verdict

**plausible** — A product that ingests human input layered on top of live feeds and serves query APIs. It is a deliberate, project-shaped choice — not a default pipe — because human input is the softest and costliest channel, so where the value *could* be automated the machine path is preferred; where the human act *is* the irreplaceable value it is the most valuable input the product has and the machine legs exist to *enrich* it.

## Related

* [request/response](/concepts/pattern-request-response)
* [streaming](/concepts/pattern-streaming)
* [human](/concepts/pattern-human)
* [data-product](/concepts/data-product) — the overall model
* [verdict](/concepts/verdict) — what the common / plausible / niche tag means
