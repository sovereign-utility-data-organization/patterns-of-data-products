---
type: Knowledge Concept
okf_version: '0.1'
timestamp: '2026-11-06T21:15:00Z'
description: The human integration pattern (H) — data produced by people on the input side, and a human-facing surface (report/dashboard/review) on the output side. The fourth pattern, orthogonal to batch, request/response, and streaming.
title: Human integration pattern
tags:
- integration-pattern
- human
- human-in-the-loop
- report
- dashboard
related:
- /knowledge-concepts/data-product
- /knowledge-concepts/pattern-batch
- /knowledge-concepts/pattern-request-response
- /knowledge-concepts/pattern-streaming
---
# Human pattern (`H`)

A distinct integration pattern: data movement **mediated by a person**, on either
side of the product. Where [batch](/knowledge-concepts/pattern-batch),
[request/response](/knowledge-concepts/pattern-request-response), and
[streaming](/knowledge-concepts/pattern-streaming) are all *machine-mediated*
(file, API, feed), `H` is the **human-mediated** mode — people are the source of
the data in, or the readers of the data out.

`H` is orthogonal to the other three: a side state is a non-empty subset of
`{B, R, S, H}`, so a human pattern is layered on top of (or stands alone from)
the machine patterns. This is what splits the 7 side-states into 15 and the
`7 × 7` grid into `15 × 15 = 225` [data product types](/data-product-types/).

## On the input side (H in IN)

The data **originates with people**, not with a machine source: manual entry in
forms or editors, review and approval, re-keying, curation. Semantics in the
contract:

- **provenance** — who changed what, and when,
- **validation** — how obviously wrong entries are caught at the door,
- **correction path** — how a person's later fix supersedes an earlier one,
- **audit trail** — a durable, replayable record of human edits (which is why
  `H`-in products almost always keep a state store).

A product that takes `H` in is what stands between a person's editing and the
consumer; its trustworthiness lives in that mediation, not in the schedule.

## On the output side (H in OUT)

The product presents data **for a person to read**: a report, a dashboard, a
screen, a printout, an approval view. This is the *human-facing surface* — the
layer people actually use, as opposed to the raw file, API, or feed underneath
it. The served view inherits whatever is in the state behind it, and a person
notices a stale or wrong value faster than an API client does, so the surface's
correctness is bound to the backend's as-of.

`H`-out is not a new serving *protocol*; it is a consumption *audience*. It
usually rides on the machine patterns below it — a dashboard reads through a
query API over a state store — but the product's reason for existing is that
**people are the consumers**, not machines.

## Distinction from the machine patterns

- A `B` file, `R` API, or `S` feed *can* be consumed by a person, but at the
  machine layer: they are protocol-shaped. `H` is the person-shaped layer.
- The difference the pattern makes is **disambiguation**: `R` (cell 6.6, API
  proxy) and `H` (cell 15.15, human-curated view) deliver data to different
  kinds of reader with different failure modes — API consumers tolerate
  stale-ness, a person does not.
- The verdict distribution shifts accordingly: human-facing **output** cells
  lean *common* (reports and dashboards are everywhere), human-facing **input**
  cells lean *plausible* (curation products are real but project-shaped), and
  the many-pattern `BRH`/`BRSH` shapes lean wherever the demand is real.

## Where it appears

- **Pure human:** cell [15.15](/data-product-types/in-h-out-h) — human in, human out.
- **Human in** (8 IN-states containing `H`, i.e. cells with rows 8–15): the
  human-curated input side.
- **Human out** (8 OUT-states containing `H`, i.e. the `.8`–`.15` columns):
  the report/dashboard layer over any machine-source row.
- **Mixed legs:** `BH`, `RH`, `SH` (cells `14`, `13`, `12`), `BHR`/`BHS`/`RSH`
  (rows `9`, `10`, `11`), and the full `BRSH` (row `8`).
- Full list: [data-product-types](/data-product-types/); structural
  properties of the now 225-type space:
  [cross-cutting observations](/knowledge-concepts/cross-cutting-observations).
