---
type: Knowledge Concept
okf_version: '0.1'
timestamp: '2026-11-08T19:19:00Z'
description: The human integration pattern (H) — data produced by people on the input side, and a human-facing surface (report/dashboard/review) on the output side. The fourth pattern, orthogonal to batch, request/response, and streaming.
definition: "The human integration pattern (H): data movement mediated by a person - data produced by people (manual entry, review, curation) on the input side, and a human-facing surface (report, dashboard, review) on the output side; the fourth pattern, orthogonal to B, R, and S, layered on (or standing alone from) the machine patterns."
example: "A shared approval ledger read back as a sign-off dashboard - H in, H out - cell 15.15, the pre-automation pattern"
altLabel:
- "H"
- "human-in-the-loop"
- "human-mediated"
- "report/dashboard layer"
scopeNote: "A side state is a non-empty subset of {B, R, S, H}, so H layers onto (or stands alone from) the machine patterns - that is what splits 7 side-states into 15 and the 7x7 grid into 225. H-in is a cost to manage - automate where a machine source can carry the same meaning - and, where the human act is the value, the value-driver."
title: Human integration pattern
tags:
- integration-pattern
- human
- human-in-the-loop
- report
- dashboard
related:
- /concepts/data-product
- /concepts/pattern-batch
- /concepts/pattern-request-response
- /concepts/pattern-streaming
- /concepts/role-of-human-input
---
# Human pattern (`H`)

A distinct integration pattern: data movement **mediated by a person**, on either
side of the product. Where [batch](/concepts/pattern-batch),
[request/response](/concepts/pattern-request-response), and
[streaming](/concepts/pattern-streaming) are all *machine-mediated*
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
That mediation is a **cost** to manage (human input is the softest and the most
expensive channel), not a demotion of value: the default is to *automate where
a machine source can carry the same meaning*, and to reserve the human leg for
what only a person can supply. Where the human act is itself the value — a
judgement, a design intent, content, an accountable decision — human input is
the **value-driver** of the product and the machine legs exist to *enrich*. See
[the role of human input](/concepts/role-of-human-input).

## On the output side (H in OUT)

The product presents data **for a person to read**: a report, a dashboard, a
screen, a printout, an approval view. This is the *human-facing surface* — the
layer people actually use, as opposed to the raw file, API, or feed underneath
it. The served view inherits whatever is in the state behind it, and a person
notices a stale or wrong value faster than an API client does, so the surface's
correctness is bound to the backend's as-of.

`H`-out is a **genuine shape**, not a thin wrapper and not a new *protocol*. It
is a **presentation and consolidation** step — aggregation, selection,
narrative, layout, approval framing — that re-casts the machine data into a
form a person can actually act on. That is not a 1:1 projection of the file,
API, or feed: a dashboard consolidates many tables behind one view, a report
compresses a stream into a story, and an approval view turns a record into a
*decision*. The transform does real work and is a real integration boundary. It
usually sits on the machine patterns below it (a dashboard over a query API on
a state store); the human surface *adds* presentation — it does not merely
relabel the machine output.

The transform also runs **the other way** in the field, which is exactly why
`H`-out is a first-class interface axis and not a footnote about who is
reading. **Human-shaped output is often the input to the next system**
precisely because the raw stream would be the wrong artifact — a downstream
consumer may be handed the *report* (the consolidated, human-shaped summary)
rather than the complete data. The form and the meaning are changed, not just
the encoding. So the human pattern on the output side is a distinct,
shape-changing layer of the interface, on equal footing with the three
machine patterns.

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

- **Pure human:** cell [15.15](/data-product-types/in-h-out-h) — human in,
  human out: the pre-automation shared record, the cell every growth path on
  that row starts from.
- **Human in** (8 IN-states containing `H`, i.e. cells with rows 8–15): the
  human-curated input side.
- **Human out** (8 OUT-states containing `H`, i.e. the `.8`–`.15` columns):
  the report/dashboard layer over any machine-source row.
- **Mixed legs:** `BH`, `RH`, `SH` (cells `14`, `13`, `12`), `BHR`/`BHS`/`RSH`
  (rows `9`, `10`, `11`), and the full `BRSH` (row `8`).
- Full list: [data-product-types](/data-product-types/); structural
  properties of the now 225-type space:
  [cross-cutting observations](/concepts/cross-cutting-observations).
