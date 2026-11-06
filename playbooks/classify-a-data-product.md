---
type: Playbook
okf_version: '0.1'
timestamp: '2026-11-06T12:50:00Z'
description: Classification procedure — take a real (or proposed) data product and place it on the 7x7 grid of data-product types.
title: Classify a data product
tags:
- playbook
- classification
- data-product
related:
- /knowledge-concepts/data-product
- /knowledge-concepts/synthetic-stream
- /data-product-types
---
# Playbook: classify a data product

Take a real or proposed data product and put it where it belongs in the
[data-product-type space](/data-product-types/).

## 1. Fix boundaries

- **What data** is the product offering? (scope)
- **Who are the consumers** and on **what contract**? (the *contract*
  distinguishes a data product from a raw table).

## 2. Read the **input** side

Ask *how the product takes in data*:

- Bulk / file / EOD snapshot? → **B**
- Polls an upstream, on demand or on a schedule? → **R**
- Subscribes to events / streams? → **S**

Write the IN-set as one of the 7 side states:
`BRS` / `BR` / `BS` / `RS` / `S` / `R` / `B`.

> If nothing fits — the product has no ingest — it's not a data product by
> the interface model; it's a pure source (record that and stop).

## 3. Read the **output** side

Ask *what interfaces the product exposes to consumers*:

- File / bulk delivery? → **B**
- Queryable API / endpoint? → **R**
- Feed / subscription / event stream? → **S**

Write the OUT-set the same way.

> Watch for the **pseudo-stream**: if you put `S` in OUT and it isn't in IN,
> the product is *synthesising* events from polls/files — see
> [synthetic stream](/knowledge-concepts/synthetic-stream), and be ready to
> answer the five contract questions (change semantics, latency,
> idempotency, backfill, ordering).

## 4. Read the cell

Map `(IN, OUT)` to the matrix — row = IN, column = OUT — and open the
matching concept doc under `/data-product-types/`:

- **What it is** — confirm the model fits
- **When to use** — compare against the real motivation
- **Watch out** — the known pitfalls
- **Verdict** — common / plausible / niche; if the product is the first
  you've seen of that type, that's a flag, not an error.

## 5. Record the instance

For each classified product record:

| Field | Note |
|---|---|
| name / owner | human-identified product |
| cell | e.g. `3.7` |
| IN / OUT letters | e.g. `BS → B` |
| verdict (common/plausible/niche) | from the concept doc |
| contract as-of semantics | snapshot? delta? event time? wall time? |
| known consumers | the ones the product actually serves |
| known non-consumers | useful for spotting a *missing* product |
| notes / caveats | anything the cell doc's "watch out" didn't catch |

## 6. Sanity checks

- **Single pattern on both sides** (`7.6`, `7.7`, `6.6`): the product is a
  *surface* product — verify the real value is normalisation, not
  transformation.
- **Diagonal** (IN = OUT): pass-through — verify the value is one of
  routing / auth / schema / policy.
- **`B` in OUT**: storage for full snapshots is the cost driver — verify
  retention is priced in.
- **Only `S` in OUT**: stateless — verify no hidden state (e.g. join
  tables) is being under-accounted.
