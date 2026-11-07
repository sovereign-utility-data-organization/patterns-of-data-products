---
type: Knowledge Concept
okf_version: '0.1'
timestamp: '2026-11-07T09:00:00Z'
description: 'Five structural observations about the 225-type space: synthetic-stream family, diagonal pass-throughs, batch-anchored utility core, state vs. stateless products, and the human layer.'
title: Cross-cutting observations
tags:
- taxonomy
- structure
related:
- /knowledge-concepts/data-product
- /knowledge-concepts/synthetic-stream
- /knowledge-concepts/pattern-human
---
# Cross-cutting observations

Five patterns that recur across the 15 × 15 space of
[data-product types](/data-product-types/).

## 1. The synthetic-stream family

Any cell with `S` in **OUT** but not in **IN** is a
*synthetic-stream suspect* — **56 cells** in the human-expanded space — and
the verdict depends on what the IN side is:

- **Machine IN** (rows `BR`, `R`, `B`) — e.g.
  [2.1, 2.3, 2.4, 2.5](/data-product-types/),
  [6.1, 6.3, 6.4, 6.5](/data-product-types/),
  [7.1, 7.3, 7.4, 7.5](/data-product-types/): the source exposes state only,
  so the feed is **synthetic** — change-detection computed on top of a
  non-streaming source.
- **`H` in IN** (rows `BHR`, `RH`, `BH`, `H`; 32 cells) — the flag is
  *shape-dependent*: synthetic only when the human change reaches the product
  as **observed state** (edited elsewhere, found by refresh). When the change
  is an **action** delivered through the product's own surface (submission,
  approval, entry), each action is a real event and the feed is
  **trigger-based**, not synthetic. The contract must state which shape it is.
- **`H` in OUT only** — the source is still the machine state store; the feed
  is synthetic and the `H` is just the human reader on top of it.

Where synthetic, always document what "change" means, the poll/refresh lag,
idempotency, and backfill. See [synthetic stream](/knowledge-concepts/synthetic-stream).

## 2. Diagonal = pass-through

Cells on the matrix diagonal (IN-state = OUT-state) are usually
*pass-throughs*: little transformation value, existing for routing,
authentication, schema normalisation, or policy enforcement.
Cells **off** the diagonal do real *shape or temporal* conversion
(file↔query, file↔stream, batch↔real-time).

## 3. Batch is the settlement core

The batch-anchored archetypes are the most load-bearing data products in
energy/utility and finance:

- **batch in → query out**: [7.6](/data-product-types/in-b-out-r), [7.2](/data-product-types/in-b-out-br)
- **stream in → batch out (settlement file)**: [5.7](/data-product-types/in-s-out-b), [3.7](/data-product-types/in-bs-out-b), [4.7](/data-product-types/in-rs-out-b)

Regulated markets are still file-anchored on the consumer side and event- or
API-anchored on the source side — which is why 7.6 and 5.7 are
disproportionately common.

## 4. State is the cost driver

- Cells with `R` in **OUT** (queryable) need a durable state store.
- Cells with `B` in **OUT** need storage sized for a *full snapshot* at
  every publish.
- Cells with only `S` in **OUT** (e.g. [5.5](/data-product-types/in-s-out-s),
  [1.5](/data-product-types/in-brs-out-s)) can be stateless by design —
  the cheapest to operate for their surface area.

Storage & freshness together determine the *cost profile* of a
data-product type, independent of how many patterns it exposes.

## 5. The human layer is a cross-cutting axis

The [human pattern](/knowledge-concepts/pattern-human) (`H`) is orthogonal to
the machine patterns, so it cuts **across** this space rather than adding a
corner:

- **`H` in OUT** (the `.8`–`.15` columns) turns any machine-sourced product into
  a **report / dashboard** over it — the surface people actually read. This is
  almost always *common*: reports and dashboards are the most frequent data
  products.
- **`H` in IN** (rows `12`–`15`) makes the product what stands between a
  person's editing and the consumer — a **curation** product. More
  *plausible* than common: real, but project-shaped, and it always carries the
  audit-trail and correction cost.
- The diagonal `H`→`H` cell, [15.15](/data-product-types/in-h-out-h), is the
  **pre-automation pattern** — a shared record between people, no machine
  mediation on either side (not paper): the ledger and the filing cabinet
  before automation, the Word document, the spreadsheet, and the wiki page
  today. Every other cell on that row is a growth step out of it.

The verdicts tilt accordingly: human-facing **output** leans *common*,
human-facing **input** leans *plausible*, and the many-pattern
`BH`/`RH`/`SH`/`BRH`/`BRSH` shapes lean wherever the demand is real in the
domain.
