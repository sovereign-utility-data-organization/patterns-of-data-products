---
type: Knowledge Concept
okf_version: '0.1'
timestamp: '2026-11-08T19:52:00Z'
definition: "The batch integration pattern (B): bulk, file-oriented data movement driven by a schedule or an explicit delivery event, applied on either side of a data product - periodic bulk loads on the input side, bulk artifacts served on the output side."
example: "A nightly warehouse load from EOD market files on IN; a settlement file published to consumers on OUT"
altLabel:
- "B"
- "bulk delivery"
- "file pattern"
- "scheduled bulk load"
scopeNote: "Protocol-agnostic at the pattern level; typical bindings are SFTP, S3/object-store, shared volumes, portal file downloads, EOD feeds. Serving on B has the highest storage cost: every snapshot must be durable and complete."
title: Batch integration pattern
tags:
- integration-pattern
- batch
related:
- /concepts/data-product
- /concepts/pattern-request-response
- /concepts/pattern-streaming
- /concepts/pattern-human
---
# Batch pattern (`B`)

Bulk, file-oriented data movement driven by a schedule or an explicit
delivery event. Protocol-agnostic at this level; typical bindings: SFTP,
S3/object-store, shared volumes, portal file downloads, EOD feeds.

## On the input side

The product ingests upstream data as periodic bulk loads: nightly warehouse
loads, EOD market files, reference-data refreshes, or on-demand full loads.
Semantics that must be pinned down in the contract:

- **as-of** semantics / snapshot vs. delta,
- **completeness** guarantees (what "done" means on a partial load),
- **refresh cadence** and expected freshness.

## On the output side

The product serves consumers as bulk artifacts: settlement files, report
bundles, full-load archives. This is the *file contract* — the oldest and
most load-bearing way to exchange regulated/utility and financial data.
Serving on `B` also has the highest storage cost: every snapshot must be
durable and complete.

## Where it appears

- Pure batch cells: `7.*` (ingest) and `*.7` (serve) — see [data-product-types](/data-product-types/)
- Mixed cells: `BR` (query + file), `BS` (hot & cold), `BRS` (omni-channel)
- The settlement core of the utility sector is batch-anchored on one or both
  sides — see [cross-cutting observations](/concepts/cross-cutting-observations)
