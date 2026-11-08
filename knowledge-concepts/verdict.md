---
type: Knowledge Concept
okf_version: '0.1'
timestamp: '2026-11-08T09:30:00Z'
description: The verdict tag attached to each of the 49 data product types — common, plausible, or niche — and what each means.
title: Verdict
tags:
- verdict
- taxonomy
related:
- /knowledge-concepts/data-product
- /knowledge-concepts/cross-cutting-observations
- /knowledge-concepts/role-of-human-input
---

# Verdict

Each of the 49 [data product types](/data-product-types/) carries a **verdict**
tag in its frontmatter and its body. The verdict is a coarse judgement about
how *likely* that combination is to be a sensible, real-world product — it
reflects the *economics* of the interface, not whether the combination is
technically possible (every one of the 49 is technically possible).

## The three verdicts

| Verdict | Meaning |
|---|---|
| **common** | A well-established, frequently seen product shape. The combination is economically sensible and you will meet it in production. |
| **plausible** | A sensible product, but project- or domain-specific. It makes sense in some contexts and not others. |
| **niche** | A real but unusual shape — usually a bridge between two worlds (e.g. a file/API source feeding a streaming consumer). It works, but it is not a default choice. |

> There is **no "awkward" / impossible** verdict. Any input side can in
> principle be re-served on any output side, so none of the 49 cells is
> nonsensical. Where a combination *feels* wrong, the awkwardness is almost
> always an economic or latency concern — that is captured per-cell in the
> "Watch out" section, not as a verdict.

## What the verdict does not capture

- **Whether the product is worth building.** A niche cell can be the right and
  only option for a given constraint.
- **Correctness of the contract.** A "common" cell with a wrong as-of
  semantic is still broken.
- **The synthetic-stream hazard.** A cell whose stream output is not backed by
  a stream input is a *synthetic-stream suspect*: pseudo when the source
  exposes state only (events are manufactured), but a real
  **trigger-based** feed when a human action delivered through the product's
  own surface is the event — see [synthetic stream](/knowledge-concepts/synthetic-stream). The verdict is independent of that distinction.

## Where the verdicts are stored

- Frontmatter: the `verdict` field on each
  [data product type](/data-product-types/) doc (values: `common`,
  `plausible`, `niche`).
- Body: the **Verdict** line in each type's heading.
- Aggregate view: the per-type index under
  [data-product-types](/data-product-types/) lists each type with its
  description (the verdict is also visible on the cell page).

## Reading the distribution

Most cells are **common** or **plausible**; the **niche** verdicts cluster in
two families:

1. **Synthetic-stream bridges** — stream output from a non-stream input
   (e.g. poller→stream, batch→stream). See
   [synthetic stream](/knowledge-concepts/synthetic-stream).
2. **Fully synthetic consolidation** — the "everything in, everything out"
   shapes where the product carries all three patterns on both sides.

The [cross-cutting observations](/knowledge-concepts/cross-cutting-observations)
page explains these clusters structurally.

## A separate axis: human input vs. human output

The `H`-in / `H`-out split is **economic, not about value**. A human-facing
*surface* (`H` in OUT) is cheap to build and is where people actually read, so
those cells lean *common*. Human *entry* (`H` in IN) is the softest and most
expensive channel, so cells where it is the source are **reserved** (lean
*plausible*, "not a default pipe" — the default being *automate where possible*).
That reservation reflects the **cost and scarcity** of the channel, not the size
of its value: where the human act is the irreplaceable value, it is the **most
valuable input** the product has, and the machine legs exist to *enrich*. A
*plausible* human-input cell is therefore not a *low-value* cell. See
[the role of human input](/knowledge-concepts/role-of-human-input).
