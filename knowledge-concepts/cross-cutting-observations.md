---
type: Knowledge Concept
okf_version: '0.1'
timestamp: '2026-11-06T12:50:00Z'
description: 'Four structural observations about the 49-type space: synthetic-stream family, diagonal pass-throughs, batch-anchored utility core, state vs. stateless products.'
title: Cross-cutting observations
tags:
- taxonomy
- structure
related:
- /knowledge-concepts/data-product
- /knowledge-concepts/synthetic-stream
---
# Cross-cutting observations

Four patterns that recur across the 7 × 7 space of
[data-product types](/data-product-types/).

## 1. The synthetic-stream family

Any cell with `S` in **OUT** but not in **IN** —
[2.1, 2.3, 2.4, 2.5](/data-product-types/), [6.1, 6.3, 6.4, 6.5](/data-product-types/),
[7.1, 7.3, 7.4, 7.5](/data-product-types/) — is a *pseudo-stream*.
The product is computing change-detection on top of a non-streaming source.
Always document: what "change" means, the poll/refresh lag, idempotency,
and backfill. See [synthetic stream](/knowledge-concepts/synthetic-stream).

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
