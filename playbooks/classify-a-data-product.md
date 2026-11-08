---
type: Playbook
okf_version: '0.1'
timestamp: '2026-11-08T19:52:00Z'
definition: "The procedure for placing a real or proposed data product on the 15x15 grid: fix the boundaries (data, owner, consumers), read the input and output sides as one of the 15 side-states each, open the resulting cell, and record the instance with its contract semantics."
example: "A product that polls a state-only register on a cadence and serves a change-detection feed: IN R, OUT S - cell 6.5, and the synthetic-stream contract questions (change semantics, latency, idempotency, backfill, ordering) apply"
altLabel:
- "cell-placement procedure"
- "classification how-to"
scopeNote: "The synthetic-stream red flag - S in OUT but not in IN - triggers the contract-question set unless the events are human actions delivered through the product's own surface (then the feed is trigger-based, not synthetic)."
title: Classify a data product
tags:
- playbook
- classification
- data-product
related:
- /concepts/data-product
- /concepts/synthetic-stream
- /data-product-types
---
# Playbook: classify a data product

Take a real or proposed data product and put it where it belongs in the
[data-product-type space](/data-product-types/).

## 1. Fix boundaries

- **What data** is the product offering? (scope)
- **Which team owns it**, and **who are the consumers**? What does the
  owning team stand behind — semantics, quality, availability, timeliness?
  (That *product thinking* — usable semantics, owned quality, documented
  provenance — is what separates a data product from a raw table.)

## 2. Read the **input** side

Ask *how the product takes in data*:

- Bulk / file / EOD snapshot? → **B**
- Polls an upstream, on demand or on a schedule? → **R**
- Subscribes to events / streams? → **S**
- Data produced by people (entry, review, curation)? → **H**

Write the IN-set as one of the 15 side states (all of them on the
[data product](/concepts/data-product) page).

> If nothing fits — the product has no ingest — it's not a data product by
> the interface model; it's a pure source (record that and stop).

## 3. Read the **output** side

Ask *what interfaces the product exposes to consumers*:

- File / bulk delivery? → **B**
- Queryable API / endpoint? → **R**
- Feed / subscription / event stream? → **S**
- A human-facing surface (report, dashboard, review)? → **H**

Write the OUT-set the same way.

> Watch for the **synthetic-stream red flag**: if `S` lands in OUT and not in
> IN, ask how the events get made. With a state-only machine source the
> product is *manufacturing* events off polls/files — see [synthetic stream](/concepts/synthetic-stream),
> and be ready to answer the five contract questions (change semantics,
> latency, idempotency, backfill, ordering). With a human source acting
> through the product's own surface, each action is a real event
> (a **trigger-based** feed) and the contract is the lighter one.

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
