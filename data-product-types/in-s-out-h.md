---
type: Data Product Type
okf_version: '0.1'
timestamp: '2026-11-08T19:24:00Z'
description: Data product ingesting via streaming (pub/sub feed) and serving via human.
definition: "A live event feed folded into the state people watch: the control room, the operations dashboard, the live status wall. The stream is the input; the human surface is the product. It is 'the wall that must be right right now'."
example: "Operators need to see live state as it changes — metering, fleet, market, device — and the audience is people on a screen, not machines."
altLabel:
- "S → H"
- "Cell 5.15"
- "Live feed as a control-room dashboard"
title: 'Cell 5.15: Live feed as a control-room dashboard'
tags:
- data-product-type
- in-s
- out-h
- common
related:
- /concepts/pattern-streaming
- /concepts/pattern-human
- /concepts/data-product
- /concepts/verdict
---

# 5.15 — Live feed as a control-room dashboard

**Interface:** IN {S} → OUT {H}&emsp;&emsp;**Verdict:** common

A live event feed folded into the state people watch: the control room, the operations dashboard, the live status wall. The stream is the input; the human surface is the product. It is 'the wall that must be right right now'.

![Interface diagram: IN S to OUT H](/assets/cells/in-s-out-h.svg)

## When to use

Operators need to see live state as it changes — metering, fleet, market, device — and the audience is people on a screen, not machines.

## What's inside

- Ingest: a **stream consumer** (offsets, replay) for the live leg.
- Core: a **transform** (filter/shape/route) over the live leg
- Serve: a **human-facing surface** (dashboard, report, printout, or review screen) — the layer people actually read.
- State: a durable **state store** and the **feed log** (retention).

## State & cost

Dominated by the durable state store (grows with entity/state breadth). Serving people is cheap to run and cheap to trust — a presentation layer over a queryable backend.

## Watch out

- A human-facing surface inherits the state behind it: the report/dashboard carries every as-of and correctness rule of the store, and a person spots a stale number faster than an API client will.
- This is machine-produced, human-read: make sure a person actually reviews/approves the served view rather than the pipeline writing it straight through.

## Typical next step

add **human curation on the input side** → cell [12.15](/data-product-types/in-sh-out-h) when the data should not be purely machine-fed, add a **query API** → cell [5.13](/data-product-types/in-s-out-rh), and add a **bulk file** → cell [5.14](/data-product-types/in-s-out-bh); or the source world gains a leg this product does not yet take, and it migrates to a richer IN-state on the same row.

## Verdict

**common** — A product that ingests live feeds and serves a human-facing surface (a report, dashboard, or shared record the same people maintain). It is the right shape where the reader is a person rather than a service, and the human-shaped view is itself what the next consumer — or the next machine in the loop — needs to act on.

## Related

* [streaming](/concepts/pattern-streaming)
* [human](/concepts/pattern-human)
* [data-product](/concepts/data-product) — the overall model
* [verdict](/concepts/verdict) — what the common / plausible / niche tag means
