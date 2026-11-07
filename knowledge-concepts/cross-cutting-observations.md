---
type: Knowledge Concept
okf_version: '0.1'
timestamp: '2026-11-06T21:15:00Z'
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

Any cell with `S` in **OUT** but not in **IN** —
[2.1, 2.3, 2.4, 2.5](/data-product-types/), [6.1, 6.3, 6.4, 6.5](/data-product-types/),
[7.1, 7.3, 7.4, 7.5](/data-product-types/), in the machine-only space — is a
*pseudo-stream*. The product is computing change-detection on top of a
non-streaming source. In the human-expanded space the family grows to **56
cells** (the same rule now also admits `H` on either side). Always document:
what "change" means, the poll/refresh lag, idempotency, and backfill. See
[synthetic stream](/knowledge-concepts/synthetic-stream).

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
  human analogue of the machine pass-throughs: a shared human-scale record —
  the ledger and the filing cabinet, the oldest data product there is.

The verdicts tilt accordingly: human-facing **output** leans *common*,
human-facing **input** leans *plausible*, and the many-pattern
`BH`/`RH`/`SH`/`BRH`/`BRSH` shapes lean wherever the demand is real in the
domain.
