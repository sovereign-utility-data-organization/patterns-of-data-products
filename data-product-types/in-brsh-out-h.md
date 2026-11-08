---
type: Data Product Type
okf_version: '0.1'
timestamp: '2026-11-08T19:52:00Z'
definition: "Everything the org has — live feeds, APIs, files, *and* human-entered data — consolidated behind one human-facing surface. The BI platform that also eats manual adjustments: the widest IN in the space serving the surface people use every day."
example: "When a dashboard/report must reflect live data, upstream APIs, bulk files, *and* human-curated adjustments, all in one view for people — a full BI/console product."
altLabel:
- "BRSH → H"
- "Cell 8.15"
- "Omni-source platform, human read"
title: 'Cell 8.15: Omni-source platform, human read'
tags:
- data-product-type
- in-brsh
- out-h
- common
related:
- /concepts/pattern-batch
- /concepts/pattern-request-response
- /concepts/pattern-streaming
- /concepts/pattern-human
- /concepts/data-product
- /concepts/verdict
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

- **Softness is a cost, not a value judgement.** Human-entered data is the softest input — irregular, subjective, error-prone, expensive to re-issue — so it needs **validation, provenance, and a correction path**, and trust leans on the audit trail, not the schedule. It is also the most expensive channel: where a machine source *can* carry the same meaning, prefer it, and keep the human leg for what only a person can supply.
- **Human input can be the value-driver.** Where the human act *is* the value — a judgement, a design intent, creative or social content, an accountable decision — and cannot be automated, human input is the **most valuable input** the product has, and the other legs exist to *enrich* it (see [the role of human input](/concepts/role-of-human-input)).
- A human-facing surface inherits the state behind it: the report/dashboard carries every as-of and correctness rule of the store, and a person spots a stale number faster than an API client will.
- **Mixed time bases** in the inputs (live vs. poll/cycle/human): fix the authoritative as-of per surface, or each output looks correct alone and wrong cross-checked.

## Typical next step

add a **query API** → cell [8.13](/data-product-types/in-brsh-out-rh), add a **bulk file** → cell [8.14](/data-product-types/in-brsh-out-bh), and add a **feed** → cell [8.12](/data-product-types/in-brsh-out-sh); or the source world gains a leg this product does not yet take, and it migrates to a richer IN-state on the same row.

## Verdict

**common** — A product that ingests human input layered on top of bulk files, query APIs, and live feeds and serves a human-facing surface (a report, dashboard, or shared record the same people maintain). It is a natural fit where the human act *is* the value — a judgement, a decision, a curated record — so the softest, costliest channel is then the *cost of having that value*; where the act *could* be automated the cheaper machine path wins.

## Related

* [batch](/concepts/pattern-batch)
* [request/response](/concepts/pattern-request-response)
* [streaming](/concepts/pattern-streaming)
* [human](/concepts/pattern-human)
* [data-product](/concepts/data-product) — the overall model
* [verdict](/concepts/verdict) — what the common / plausible / niche tag means
