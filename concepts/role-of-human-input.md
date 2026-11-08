---
type: Knowledge Concept
okf_version: '0.1'
timestamp: '2026-11-08T09:30:00Z'
description: The role of human input (H in IN) in a data product. Three distinct facts that are easily conflated into one word — softness (a quality and cost property), the automate-where-possible default, and irreplaceability (human input as the value-driver) — and how H interacts with B, R, and S.
title: The role of human input
tags:
- human
- integration-pattern
- value
- semantics
related:
- /concepts/pattern-human
- /concepts/pattern-batch
- /concepts/pattern-request-response
- /concepts/pattern-streaming
- /concepts/verdict
- /concepts/synthetic-stream
---
# The role of human input

A data product whose input side carries **H** (the rows `BRSH`, `BHR`, `BHS`,
`RSH`, `SH`, `RH`, `BH`, `H`) takes *human input* — data produced by people —
alongside machine input (batch, request/response, streaming). The catalogue's
earliest instinct, to summarise human input with a single word — *soft*,
*manual*, *the softest* — is where it went wrong: **softness** is a real fact
about human input, but it was silently carrying the work of a **value
judgement**. Those are different things. Separate them and the position on
human input follows, and so does "when to use it."

## Three distinct facts about human input

**1. Softness is a quality-and-cost property, not a value judgement.**
Human input is the softest source in a precise, defensible sense: it arriving
irregularly, it carries intent as well as errors, it is hard to catch at the
door, and it is expensive to re-issue. That is a **cost to manage** — it is
what makes the contract carry *validation*, *provenance*, and a *correction
path*, and why `H`-in products almost always keep a durable state store and an
audit trail. But softness says nothing about the *value* of the data. A soft
input can still be the most valuable input in the product. The catalogue's
earlier error was letting "the softest input" imply "the least important."

**2. The default is *automate where you can*.**
Because human input is soft *and* expensive — every unit of it costs a person's
time and attention — the sound engineering stance is: *where a machine source
can carry the same meaning, prefer the machine input.* Human input is the
**more expensive channel**, so it is the fallback, not the gold standard. This
is exactly *why* the human-input cells read "a curation product, not a default
pipe" and why their verdicts lean *plausible*: the reservation reflects the
**economics of the channel**, not the smallness of its value. That reservation
is defensible and should stay.

**3. Irreplaceability is what makes human input central.**
Where the act *cannot* be automated — because the value **is** the human act,
and no machine reproduces it yet — human input stops being "the soft fallback"
and becomes the **value-driver** of the product. The machine legs, if present,
are there to *enrich*: provide context, validate, or distribute. In that case
scarcity (cost, low throughput) is the **reason** it is central and protected,
not a defect. The catalogue had previously had no home for this reading — it
framed `H`-in as "one leg alongside the machine leg" and, when it touched
value at all, named only the mitigation (the audit trail). It never said "this
product exists because the human act *is* the irreplaceable value it serves."

These three facts are **orthogonal**, and a human input can carry all of them
at once: it is *soft* (always — manage that), the *default is to automate*
(where possible), and *the value-driver* (where it is irreplaceable). Softness
is the cost to manage; automation is the default; irreplaceability is where the
value concentrates.

## What the value-driver looks like

The human act is the value the product exists to deliver, and a machine cannot
replace it (yet):

- **Creative and social content** — posts, messages, media. The human content
  *is* the product; the recommendation graph, metadata, and embeddings are
  enrichment. (`H`-only, `H`+`S`, `H`+`R`)
- **Customer support** — the conversation, the decision, the resolution. The
  agent's act is the value; the ticket ID, CRM fields, and SLA timers enrich
  it. (`H`+`R`, `H`+`S`)
- **Engineering and design intent** — the engineer's design, the spec, the
  choice. The intent is the most valuable artifact; the CAD mesh, the BOM, and
  the simulation results validate and enrich it. (`H`+`B`, `H`+`R`)
- **Clinical judgement** — the diagnosis, the treatment decision. The vitals,
  the labs, the imaging enrich it. (`H`+`R`)
- **Accountable, high-stakes decision** — approvals, sign-off, adjudication.
  The decision carries **responsibility**, which a machine does not bear.
  (`H`+`B`, `H`+`R`)

In each of these, human input is not "the soft leg" — it is the **core value**,
and the expensive channel is the *cost of having that value*.

When human input is **not** the value-driver — an analyst annotating a
market-data dump, a person confirming an auto-detected event — the machine leg
leads, the human adds curation, and the *automate-where-possible* default
applies cleanly. Both readings are legitimate; the catalogue must not assume the
machine-led one.

## How H interacts with B / R / S

- **H + B (file)** — human judgement *over* bulk material (a design intent on
  top of a BOM/FEA file) **or** bulk material a person annotates. Both are real;
  the value-driver reading is the first one.
- **H + R (API)** — an API that **distributes** human-made decisions or content
  as the value ("fetch the agent's call", "fetch the design intent") **or** a
  person reaching into an API. In the first, the API does not demote the human
  act — it is the *distribution of the irreplaceable judgement*.
- **H + S (stream)** — human-authored events **are** the stream (the post feed,
  the live ticket stream, the approval stream). Under the
  [synthetic stream](/concepts/synthetic-stream) distinction, a human
  act is itself a real event, so human-input streaming is a **first-class**
  product shape — not a pseudo-stream hazard.
- **H alone** — a judgement, a design, a conversation, a ledger: value-dense,
  high-cost, irreplaceable where it lives. The oldest data product in the space,
  and one of the most valuable — not the least.

## What it means for the verdict

The `H`-in cells' verdict distribution encodes facts **2** and **3** together,
and should be read that way:

- Human-input *cells* lean *plausible* / "not the default pipe" because human
  input is the **more expensive channel** — a fallback (fact 2). That
  reservation is right, and the tiers stand.
- But the *reason a product exists* in these cells is usually fact **3** — the
  human act is the **irreplaceable value**. So a *plausible* `H`-in cell is not
  a *low-value* cell; the tier reflects the **cost and scarcity** of the
  channel, not the value of its data.
- Human-*output* cells (people read) lean *common* because the surface is cheap
  to build and people are the usual reader. The asymmetry is one fact: `H`-out
  is a cheap, common surface; `H`-in is a costly, reserved channel — and where
  the input is the point, it is the most valuable input there is.

See [verdict](/concepts/verdict) for what the tags mean and
[pattern human](/concepts/pattern-human) for the `H` pattern itself.
