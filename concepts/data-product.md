---
type: Knowledge Concept
okf_version: '0.1'
timestamp: '2026-11-08T18:45:00Z'
description: "A data product (in the data-mesh sense) is a self-contained, domain-owned architectural quantum — the domain's data + what makes it usable (semantics, schema, quality, provenance) + the code + the infrastructure, served through one or more output ports (interfaces). Its identity is the data it offers, not the ports it exposes. Classified here by the integration patterns on its input side and output side (4 patterns, 15 states per side, 15 x 15 = 225 types)."
title: Data product
tags:
- data-product
- data-mesh
- interface
- taxonomy
related:
- /concepts/pattern-batch
- /concepts/pattern-request-response
- /concepts/pattern-streaming
- /concepts/pattern-human
- /concepts/synthetic-stream
- /concepts/cross-cutting-observations
---
# Data product

A **data product** is the fundamental unit of data architecture, in the sense
of [data mesh](https://martinfowler.com/articles/data-mesh-principles.html):
an **architectural quantum** — a self-contained unit that can be deployed
and operated *independently* and contains all of the structural elements
required for its function. It is a *logical* unit, not a technology: the
analytical data of a domain **together with everything that is needed to
make that data usable** for other teams.

[Dehghani's account](https://martinfowler.com/articles/data-mesh-principles.html)
says a data product encapsulates three structural components:

1. **Data and metadata** — the underlying analytical and historical data,
   together with what makes it *usable*: semantic and syntactic schema,
   quality metrics, provenance and lineage, and documentation.
2. **Code** — the pipelines that consume and transform upstream data, the
   services that make the data available, and the enforcement of access and
   compliance policies.
3. **Infrastructure** — the storage, compute, and access the product needs
   to be built, deployed, and run.

A product is owned by the **domain team closest to the data**. That team is
accountable for the product's **quality, availability, and cost** across its
entire lifecycle, and consumers use the product the way they use any product
— they **discover** it, **understand** it, and **trust** it — not the way
they use a raw extract from someone else's store. On its **input side** the
product connects to sources — operational systems or other data products —
and transforms what it receives; on its **output side** it serves the
result through one or more **output ports** (its interfaces, or in this
catalog: patterns on the IN and OUT sides).

> Sources: Z. Dehghani, *Data Mesh Principles and Logical Architecture*,
> [martinfowler.com](https://martinfowler.com/articles/data-mesh-principles.html)
> (data product = "architectural quantum"; data "served as events, batch
> files, relational tables, graphs, etc., while maintaining the same
> semantic"); and *Data Mesh Architecture*
> ([datamesh-architecture.com](https://www.datamesh-architecture.com/)): a
> data product is "a logical unit that contains all components to process
> and store domain data ... and makes them available to other teams via
> output ports", owned by the domain team, which "needs to continuously
> monitor and ensure data quality, availability, and costs".

### Identity vs. interface

A product's **identity** is the data it offers. The way that data is *made
available* — its output ports — is not part of its identity. These are
different axes, and conflating them inverts the idea of a product:

- **Same product, different shapes.** As Dehghani puts it, data "can be
  served as events, batch files, relational tables, graphs, etc., *while
  maintaining the same semantic*". Those shapes are the product's output
  ports, and a product may expose **one or many** of them. The same records
  served as a file drop, a query API, and an event stream are **one data
  product** with three ports — not three different products. It is the same
  flour in different bag sizes (500 g and 1 kg): what matters is the flour,
  not the bag.
- **Adding a port changes the *type*, not the *product*.** When a product
  gains a new way of serving (e.g. a query API added to a file drop), the
  product stays the same while its type moves to a different cell of this
  catalog (`7.2` → `7.1` for a batch-loaded product).
- **What splits a product** is a difference in *what the owning team stands
  behind* — the scope or meaning of the data, or the quality the team is
  accountable for — or a different owning team. Not the channel.

This catalog therefore classifies the **type** of a data product — the shape
of its input and output sides — not the product's identity. Type and product
are not one and the same: a single product occupies exactly **one** cell,
whose patterns enumerate the ports it currently exposes. A *different*
product is one with different data or a different owning team — not one over
a different port.

## The interface model

An interface is described by two factors:

1. **Integration pattern** — the mode of data movement, independent of the
   concrete protocol:
   - [batch](/concepts/pattern-batch) — bulk/file delivery on a schedule
   - [request/response](/concepts/pattern-request-response) — synchronous on-demand query
   - [streaming](/concepts/pattern-streaming) — continuous pub/sub push
   - [human](/concepts/pattern-human) — data produced by people in, or a
     human-facing surface (report/dashboard/review) out
2. **Side** — the pattern applies to the product's **input** side (how it
   ingests) or its **output** side (how it serves).

Each side may carry **any non-empty subset** of the four patterns, giving
**15 side states**:

| Code | Working name | Patterns |
|---|---|---|
| `BRS`  | omni-channel | batch + request/response + streaming |
| `BR`   | query + file | request/response + batch |
| `BS`   | hot & cold | streaming + batch |
| `RS`   | live + lookup | streaming + request/response |
| `S`    | stream-only | streaming |
| `R`    | request-response only | request/response |
| `B`    | batch-only | batch |
| `BRSH` | omni-channel + human | batch + request/response + streaming + human |
| `BHR`  | file/API + human | batch + request/response + human |
| `BHS`  | file/stream + human | batch + streaming + human |
| `RSH`  | API/stream + human | request/response + streaming + human |
| `SH`   | stream + human | streaming + human |
| `RH`   | API + human | request/response + human |
| `BH`   | file + human | batch + human |
| `H`    | human-only | human |

A **data product type** is the pair (IN-state × OUT-state) → a space of
**15 × 15 = 225 types**, each with its own concept doc in
[data-product-types](/data-product-types/).

> Cells are numbered row-major in the order above (1–15): cell `r.c` has
> IN = the r-th row state and OUT = the c-th column state (e.g. `7.6` = IN `B`,
> OUT `R`; `15.6` = IN `H`, OUT `R`). The original machine-only cells keep
> their historical `1`–`7` numbering; the human states are `8`–`15`.

## Quick map

Full 15 × 15. The left 7×7 block is the machine-only space (unchanged); the
8th–15th row/column are the human pattern.

| IN \ OUT | BRS | BR | BS | RS | S | R | B | BRSH | BHR | BHS | RSH | SH | RH | BH | H |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **BRS** | [1.1](/data-product-types/in-brs-out-brs) | [1.2](/data-product-types/in-brs-out-br) | [1.3](/data-product-types/in-brs-out-bs) | [1.4](/data-product-types/in-brs-out-rs) | [1.5](/data-product-types/in-brs-out-s) | [1.6](/data-product-types/in-brs-out-r) | [1.7](/data-product-types/in-brs-out-b) | [1.8](/data-product-types/in-brs-out-brsh) | [1.9](/data-product-types/in-brs-out-bhr) | [1.10](/data-product-types/in-brs-out-bhs) | [1.11](/data-product-types/in-brs-out-rsh) | [1.12](/data-product-types/in-brs-out-sh) | [1.13](/data-product-types/in-brs-out-rh) | [1.14](/data-product-types/in-brs-out-bh) | [1.15](/data-product-types/in-brs-out-h) |
| **BR**  | [2.1](/data-product-types/in-br-out-brs) | [2.2](/data-product-types/in-br-out-br) | [2.3](/data-product-types/in-br-out-bs) | [2.4](/data-product-types/in-br-out-rs) | [2.5](/data-product-types/in-br-out-s) | [2.6](/data-product-types/in-br-out-r) | [2.7](/data-product-types/in-br-out-b) | [2.8](/data-product-types/in-br-out-brsh) | [2.9](/data-product-types/in-br-out-bhr) | [2.10](/data-product-types/in-br-out-bhs) | [2.11](/data-product-types/in-br-out-rsh) | [2.12](/data-product-types/in-br-out-sh) | [2.13](/data-product-types/in-br-out-rh) | [2.14](/data-product-types/in-br-out-bh) | [2.15](/data-product-types/in-br-out-h) |
| **BS**  | [3.1](/data-product-types/in-bs-out-brs) | [3.2](/data-product-types/in-bs-out-br) | [3.3](/data-product-types/in-bs-out-bs) | [3.4](/data-product-types/in-bs-out-rs) | [3.5](/data-product-types/in-bs-out-s) | [3.6](/data-product-types/in-bs-out-r) | [3.7](/data-product-types/in-bs-out-b) | [3.8](/data-product-types/in-bs-out-brsh) | [3.9](/data-product-types/in-bs-out-bhr) | [3.10](/data-product-types/in-bs-out-bhs) | [3.11](/data-product-types/in-bs-out-rsh) | [3.12](/data-product-types/in-bs-out-sh) | [3.13](/data-product-types/in-bs-out-rh) | [3.14](/data-product-types/in-bs-out-bh) | [3.15](/data-product-types/in-bs-out-h) |
| **RS**  | [4.1](/data-product-types/in-rs-out-brs) | [4.2](/data-product-types/in-rs-out-br) | [4.3](/data-product-types/in-rs-out-bs) | [4.4](/data-product-types/in-rs-out-rs) | [4.5](/data-product-types/in-rs-out-s) | [4.6](/data-product-types/in-rs-out-r) | [4.7](/data-product-types/in-rs-out-b) | [4.8](/data-product-types/in-rs-out-brsh) | [4.9](/data-product-types/in-rs-out-bhr) | [4.10](/data-product-types/in-rs-out-bhs) | [4.11](/data-product-types/in-rs-out-rsh) | [4.12](/data-product-types/in-rs-out-sh) | [4.13](/data-product-types/in-rs-out-rh) | [4.14](/data-product-types/in-rs-out-bh) | [4.15](/data-product-types/in-rs-out-h) |
| **S**   | [5.1](/data-product-types/in-s-out-brs) | [5.2](/data-product-types/in-s-out-br) | [5.3](/data-product-types/in-s-out-bs) | [5.4](/data-product-types/in-s-out-rs) | [5.5](/data-product-types/in-s-out-s) | [5.6](/data-product-types/in-s-out-r) | [5.7](/data-product-types/in-s-out-b) | [5.8](/data-product-types/in-s-out-brsh) | [5.9](/data-product-types/in-s-out-bhr) | [5.10](/data-product-types/in-s-out-bhs) | [5.11](/data-product-types/in-s-out-rsh) | [5.12](/data-product-types/in-s-out-sh) | [5.13](/data-product-types/in-s-out-rh) | [5.14](/data-product-types/in-s-out-bh) | [5.15](/data-product-types/in-s-out-h) |
| **R**   | [6.1](/data-product-types/in-r-out-brs) | [6.2](/data-product-types/in-r-out-br) | [6.3](/data-product-types/in-r-out-bs) | [6.4](/data-product-types/in-r-out-rs) | [6.5](/data-product-types/in-r-out-s) | [6.6](/data-product-types/in-r-out-r) | [6.7](/data-product-types/in-r-out-b) | [6.8](/data-product-types/in-r-out-brsh) | [6.9](/data-product-types/in-r-out-bhr) | [6.10](/data-product-types/in-r-out-bhs) | [6.11](/data-product-types/in-r-out-rsh) | [6.12](/data-product-types/in-r-out-sh) | [6.13](/data-product-types/in-r-out-rh) | [6.14](/data-product-types/in-r-out-bh) | [6.15](/data-product-types/in-r-out-h) |
| **B**   | [7.1](/data-product-types/in-b-out-brs) | [7.2](/data-product-types/in-b-out-br) | [7.3](/data-product-types/in-b-out-bs) | [7.4](/data-product-types/in-b-out-rs) | [7.5](/data-product-types/in-b-out-s) | [7.6](/data-product-types/in-b-out-r) | [7.7](/data-product-types/in-b-out-b) | [7.8](/data-product-types/in-b-out-brsh) | [7.9](/data-product-types/in-b-out-bhr) | [7.10](/data-product-types/in-b-out-bhs) | [7.11](/data-product-types/in-b-out-rsh) | [7.12](/data-product-types/in-b-out-sh) | [7.13](/data-product-types/in-b-out-rh) | [7.14](/data-product-types/in-b-out-bh) | [7.15](/data-product-types/in-b-out-h) |
| **BRSH** | [8.1](/data-product-types/in-brsh-out-brs) | [8.2](/data-product-types/in-brsh-out-br) | [8.3](/data-product-types/in-brsh-out-bs) | [8.4](/data-product-types/in-brsh-out-rs) | [8.5](/data-product-types/in-brsh-out-s) | [8.6](/data-product-types/in-brsh-out-r) | [8.7](/data-product-types/in-brsh-out-b) | [8.8](/data-product-types/in-brsh-out-brsh) | [8.9](/data-product-types/in-brsh-out-bhr) | [8.10](/data-product-types/in-brsh-out-bhs) | [8.11](/data-product-types/in-brsh-out-rsh) | [8.12](/data-product-types/in-brsh-out-sh) | [8.13](/data-product-types/in-brsh-out-rh) | [8.14](/data-product-types/in-brsh-out-bh) | [8.15](/data-product-types/in-brsh-out-h) |
| **BHR** | [9.1](/data-product-types/in-bhr-out-brs) | [9.2](/data-product-types/in-bhr-out-br) | [9.3](/data-product-types/in-bhr-out-bs) | [9.4](/data-product-types/in-bhr-out-rs) | [9.5](/data-product-types/in-bhr-out-s) | [9.6](/data-product-types/in-bhr-out-r) | [9.7](/data-product-types/in-bhr-out-b) | [9.8](/data-product-types/in-bhr-out-brsh) | [9.9](/data-product-types/in-bhr-out-bhr) | [9.10](/data-product-types/in-bhr-out-bhs) | [9.11](/data-product-types/in-bhr-out-rsh) | [9.12](/data-product-types/in-bhr-out-sh) | [9.13](/data-product-types/in-bhr-out-rh) | [9.14](/data-product-types/in-bhr-out-bh) | [9.15](/data-product-types/in-bhr-out-h) |
| **BHS** | [10.1](/data-product-types/in-bhs-out-brs) | [10.2](/data-product-types/in-bhs-out-br) | [10.3](/data-product-types/in-bhs-out-bs) | [10.4](/data-product-types/in-bhs-out-rs) | [10.5](/data-product-types/in-bhs-out-s) | [10.6](/data-product-types/in-bhs-out-r) | [10.7](/data-product-types/in-bhs-out-b) | [10.8](/data-product-types/in-bhs-out-brsh) | [10.9](/data-product-types/in-bhs-out-bhr) | [10.10](/data-product-types/in-bhs-out-bhs) | [10.11](/data-product-types/in-bhs-out-rsh) | [10.12](/data-product-types/in-bhs-out-sh) | [10.13](/data-product-types/in-bhs-out-rh) | [10.14](/data-product-types/in-bhs-out-bh) | [10.15](/data-product-types/in-bhs-out-h) |
| **RSH** | [11.1](/data-product-types/in-rsh-out-brs) | [11.2](/data-product-types/in-rsh-out-br) | [11.3](/data-product-types/in-rsh-out-bs) | [11.4](/data-product-types/in-rsh-out-rs) | [11.5](/data-product-types/in-rsh-out-s) | [11.6](/data-product-types/in-rsh-out-r) | [11.7](/data-product-types/in-rsh-out-b) | [11.8](/data-product-types/in-rsh-out-brsh) | [11.9](/data-product-types/in-rsh-out-bhr) | [11.10](/data-product-types/in-rsh-out-bhs) | [11.11](/data-product-types/in-rsh-out-rsh) | [11.12](/data-product-types/in-rsh-out-sh) | [11.13](/data-product-types/in-rsh-out-rh) | [11.14](/data-product-types/in-rsh-out-bh) | [11.15](/data-product-types/in-rsh-out-h) |
| **SH**  | [12.1](/data-product-types/in-sh-out-brs) | [12.2](/data-product-types/in-sh-out-br) | [12.3](/data-product-types/in-sh-out-bs) | [12.4](/data-product-types/in-sh-out-rs) | [12.5](/data-product-types/in-sh-out-s) | [12.6](/data-product-types/in-sh-out-r) | [12.7](/data-product-types/in-sh-out-b) | [12.8](/data-product-types/in-sh-out-brsh) | [12.9](/data-product-types/in-sh-out-bhr) | [12.10](/data-product-types/in-sh-out-bhs) | [12.11](/data-product-types/in-sh-out-rsh) | [12.12](/data-product-types/in-sh-out-sh) | [12.13](/data-product-types/in-sh-out-rh) | [12.14](/data-product-types/in-sh-out-bh) | [12.15](/data-product-types/in-sh-out-h) |
| **RH**  | [13.1](/data-product-types/in-rh-out-brs) | [13.2](/data-product-types/in-rh-out-br) | [13.3](/data-product-types/in-rh-out-bs) | [13.4](/data-product-types/in-rh-out-rs) | [13.5](/data-product-types/in-rh-out-s) | [13.6](/data-product-types/in-rh-out-r) | [13.7](/data-product-types/in-rh-out-b) | [13.8](/data-product-types/in-rh-out-brsh) | [13.9](/data-product-types/in-rh-out-bhr) | [13.10](/data-product-types/in-rh-out-bhs) | [13.11](/data-product-types/in-rh-out-rsh) | [13.12](/data-product-types/in-rh-out-sh) | [13.13](/data-product-types/in-rh-out-rh) | [13.14](/data-product-types/in-rh-out-bh) | [13.15](/data-product-types/in-rh-out-h) |
| **BH**  | [14.1](/data-product-types/in-bh-out-brs) | [14.2](/data-product-types/in-bh-out-br) | [14.3](/data-product-types/in-bh-out-bs) | [14.4](/data-product-types/in-bh-out-rs) | [14.5](/data-product-types/in-bh-out-s) | [14.6](/data-product-types/in-bh-out-r) | [14.7](/data-product-types/in-bh-out-b) | [14.8](/data-product-types/in-bh-out-brsh) | [14.9](/data-product-types/in-bh-out-bhr) | [14.10](/data-product-types/in-bh-out-bhs) | [14.11](/data-product-types/in-bh-out-rsh) | [14.12](/data-product-types/in-bh-out-sh) | [14.13](/data-product-types/in-bh-out-rh) | [14.14](/data-product-types/in-bh-out-bh) | [14.15](/data-product-types/in-bh-out-h) |
| **H**   | [15.1](/data-product-types/in-h-out-brs) | [15.2](/data-product-types/in-h-out-br) | [15.3](/data-product-types/in-h-out-bs) | [15.4](/data-product-types/in-h-out-rs) | [15.5](/data-product-types/in-h-out-s) | [15.6](/data-product-types/in-h-out-r) | [15.7](/data-product-types/in-h-out-b) | [15.8](/data-product-types/in-h-out-brsh) | [15.9](/data-product-types/in-h-out-bhr) | [15.10](/data-product-types/in-h-out-bhs) | [15.11](/data-product-types/in-h-out-rsh) | [15.12](/data-product-types/in-h-out-sh) | [15.13](/data-product-types/in-h-out-rh) | [15.14](/data-product-types/in-h-out-bh) | [15.15](/data-product-types/in-h-out-h) |

A state on *no* patterns is not a data product: a raw drop into someone
else's bucket, or a pure sink with nothing to serve, has no usable interface
and no one standing behind it.

## Navigating the space

- **Figure of the four patterns (all interfaces):** `/assets/all-possible-interaction-patern-data-product.svg`
- **Figure of the 49 machine-only cells:** `/assets/all-possible-data-product-patterns.svg`
- **One description per type** (what it is, when to use it, verdict): `/data-product-types/`
- **Structural properties of the whole space:** [cross-cutting observations](/concepts/cross-cutting-observations)
- **The verdict tag** on each type (common / plausible / niche): [verdict](/concepts/verdict)
- **The human pattern (H):** [human](/concepts/pattern-human) — the 4th, orthogonal integration layer
- **How this relates to architecture paradigms** (serverless, event-driven, CQRS, …): [architectural paradigms](/concepts/architectural-paradigms)
- **The synthetic-stream hazard** (stream out, no stream in — a red flag; synthetic when events are manufactured off a state-only source, not when a human action is the event): [synthetic stream](/concepts/synthetic-stream)
- **How to classify a real product** into this space: [classify-a-data-product](/playbooks/classify-a-data-product)
