---
type: Knowledge Concept
okf_version: '0.1'
timestamp: '2026-11-06T12:50:00Z'
description: A data product is data + contract + interface; classified here by the integration patterns on its input side and output side (7 x 7 = 49 types).
title: Data product
tags:
- data-product
- interface
- taxonomy
related:
- /knowledge-concepts/pattern-batch
- /knowledge-concepts/pattern-request-response
- /knowledge-concepts/pattern-streaming
- /knowledge-concepts/synthetic-stream
- /knowledge-concepts/cross-cutting-observations
---
# Data product

A **data product** is a self-contained offering of data to external consumers.
It comprises:

1. the **data** itself,
2. a **contract** — schema, semantics, update cycle, as-of and availability
   guarantees, access conditions — and
3. one or more **interfaces** through which consumers actually obtain the data.

The value is in the *product*, not in the underlying store: two products on
the same data can be fundamentally different depending on how it is exposed.

## The interface model

An interface is described by two factors:

1. **Integration pattern** — the mode of data movement, independent of the
   concrete protocol:
   - [batch](/knowledge-concepts/pattern-batch) — bulk/file delivery on a schedule
   - [request/response](/knowledge-concepts/pattern-request-response) — synchronous on-demand query
   - [streaming](/knowledge-concepts/pattern-streaming) — continuous pub/sub push
2. **Side** — the pattern applies to the product's **input** side (how it
   ingests) or its **output** side (how it serves).

Each side may carry **any non-empty subset** of the three patterns, giving
**7 side states**:

| Code | Working name | Patterns |
|---|---|---|
| `BRS` | omni-channel | batch + request/response + streaming |
| `BR`  | query + file | request/response + batch |
| `BS`  | hot & cold | streaming + batch |
| `RS`  | live + lookup | streaming + request/response |
| `S`   | stream-only | streaming |
| `R`   | request-response only | request/response |
| `B`   | batch-only | batch |

A **data product type** is the pair (IN-state × OUT-state) → a space of
**7 × 7 = 49 types**, each with its own concept doc in
[data-product-types](/data-product-types/).

> Cells are numbered row-major in the order above: cell `r.c` has IN = the
> r-th row state and OUT = the c-th column state (e.g. `7.6` = IN `B`, OUT `R`).

## Quick map

| IN \ OUT | BRS | BR | BS | RS | S | R | B |
|---|---|---|---|---|---|---|---|
| **BRS** | [1.1](/data-product-types/in-brs-out-brs) | [1.2](/data-product-types/in-brs-out-br) | [1.3](/data-product-types/in-brs-out-bs) | [1.4](/data-product-types/in-brs-out-rs) | [1.5](/data-product-types/in-brs-out-s) | [1.6](/data-product-types/in-brs-out-r) | [1.7](/data-product-types/in-brs-out-b) |
| **BR**  | [2.1](/data-product-types/in-br-out-brs) | [2.2](/data-product-types/in-br-out-br) | [2.3](/data-product-types/in-br-out-bs) | [2.4](/data-product-types/in-br-out-rs) | [2.5](/data-product-types/in-br-out-s) | [2.6](/data-product-types/in-br-out-r) | [2.7](/data-product-types/in-br-out-b) |
| **BS**  | [3.1](/data-product-types/in-bs-out-brs) | [3.2](/data-product-types/in-bs-out-br) | [3.3](/data-product-types/in-bs-out-bs) | [3.4](/data-product-types/in-bs-out-rs) | [3.5](/data-product-types/in-bs-out-s) | [3.6](/data-product-types/in-bs-out-r) | [3.7](/data-product-types/in-bs-out-b) |
| **RS**  | [4.1](/data-product-types/in-rs-out-brs) | [4.2](/data-product-types/in-rs-out-br) | [4.3](/data-product-types/in-rs-out-bs) | [4.4](/data-product-types/in-rs-out-rs) | [4.5](/data-product-types/in-rs-out-s) | [4.6](/data-product-types/in-rs-out-r) | [4.7](/data-product-types/in-rs-out-b) |
| **S**   | [5.1](/data-product-types/in-s-out-brs) | [5.2](/data-product-types/in-s-out-br) | [5.3](/data-product-types/in-s-out-bs) | [5.4](/data-product-types/in-s-out-rs) | [5.5](/data-product-types/in-s-out-s) | [5.6](/data-product-types/in-s-out-r) | [5.7](/data-product-types/in-s-out-b) |
| **R**   | [6.1](/data-product-types/in-r-out-brs) | [6.2](/data-product-types/in-r-out-br) | [6.3](/data-product-types/in-r-out-bs) | [6.4](/data-product-types/in-r-out-rs) | [6.5](/data-product-types/in-r-out-s) | [6.6](/data-product-types/in-r-out-r) | [6.7](/data-product-types/in-r-out-b) |
| **B**   | [7.1](/data-product-types/in-b-out-brs) | [7.2](/data-product-types/in-b-out-br) | [7.3](/data-product-types/in-b-out-bs) | [7.4](/data-product-types/in-b-out-rs) | [7.5](/data-product-types/in-b-out-s) | [7.6](/data-product-types/in-b-out-r) | [7.7](/data-product-types/in-b-out-b) |

A state on *no* patterns is not a data product: a pure file drop with no
contract, or a pure sink with nothing to serve, has no consumable interface.

## Navigating the space

- **Figure of all 49 combinations:** `/assets/all-possible-data-product-patterns.svg`
- **One description per type** (what it is, when to use it, verdict): `/data-product-types/`
- **Structural properties of the whole space:** [cross-cutting observations](/knowledge-concepts/cross-cutting-observations)
- **The pseudo-stream hazard** (stream out from non-stream in): [synthetic stream](/knowledge-concepts/synthetic-stream)
- **How to classify a real product** into this space: [classify-a-data-product](/playbooks/classify-a-data-product)
