---
type: Knowledge Concept
okf_version: '0.1'
timestamp: '2026-11-08T14:00:00Z'
description: How architectural paradigms (serverless, event-driven, event sourcing, CQRS, microservices, stream processing, ETL/ELT, CDC, data mesh) relate to — but are distinct from — the data product interface taxonomy.
title: Architectural paradigms
tags:
- architecture
- serverless
- event-driven
- cqrs
- data-mesh
related:
- /knowledge-concepts/data-product
- /knowledge-concepts/cross-cutting-observations
---

# Architectural paradigms

This page relates **software architecture paradigms** to the
[data-product interface taxonomy](/knowledge-concepts/data-product). It exists
so that people who think in serverless / event-driven / microservices terms
can recognise what a data product *is* — without conflating the two.

## The core distinction: interface vs. implementation

The two concepts live on **different axes**:

| | What it describes | What this taxonomy classifies |
|---|---|---|
| **Data product** | The **domain-owned offering**: what data (and at what quality), and on which integration patterns its **input** and **output** sides are served. | ✅ |
| **Architecture paradigm** | The **runtime/implementation**: how the product is built and operated (stateless functions, event logs, service mesh, batch pipelines). | ❌ — orthogonal |

Consequences of this separation:

- **Same interface, many implementations.** Cell `5.5` (stream → stream) can
  be a serverless streaming function, a Kafka Streams app, or a hand-written
  TCP relay. The *interface* is identical; the *architecture* is a choice.
- **Same architecture, many interfaces.** A single serverless function can
  serve `S → B`, `S → R`, or `S → S` depending on what it emits — the
  paradigm does not determine the cell.
- **The data product is the offering, not the code.** When you classify a
  product, you classify what it offers and on which interfaces. The
  architecture is a *recommendation* about how to implement that interface,
  not part of the classification.

So the table below is **not** "this cell *is* paradigm X". It is "this cell's
behaviour is *commonly and naturally implemented as* paradigm X, and naming
that helps you recognise the shape."

## Paradigms and the cells they characteristically implement

| Paradigm | In one line | Characteristic interface | Cells |
|---|---|---|---|
| **Serverless / FaaS** | Stateless, event-triggered, scale-to-zero compute | stream → stream (pure transform) | [5.5](/data-product-types/in-s-out-s) |
| **Event-driven architecture (EDA)** | Components communicate via events on a bus/stream | stream in ↔ stream out | [5.5](/data-product-types/in-s-out-s), [5.3](/data-product-types/in-s-out-bs), [3.3](/data-product-types/in-bs-out-bs) |
| **Event sourcing** | State persisted as an append-only event log; current state = fold over the log | stream in → state/derived out | [5.6](/data-product-types/in-s-out-r), [5.2](/data-product-types/in-s-out-br), [5.3](/data-product-types/in-s-out-bs) |
| **CQRS** | Separate read model from write model (often paired with event sourcing) | event/state in → queryable read model out | [5.6](/data-product-types/in-s-out-r), [4.6](/data-product-types/in-rs-out-r) |
| **Stream processing (CEP)** | Stateful continuous computation over a stream (Flink, ksqlDB) | stream in → enriched/aggregated state out (all serving modes) | [5.1](/data-product-types/in-s-out-brs), [5.2](/data-product-types/in-s-out-br), [5.6](/data-product-types/in-s-out-r) |
| **Microservices / API gateway / BFF** | Independently deployable services behind a routing/composing front door | many inputs → one clean request/response API | [6.6](/data-product-types/in-r-out-r), [1.6](/data-product-types/in-brs-out-r), [4.2](/data-product-types/in-rs-out-br) |
| **ETL / ELT / data warehouse** | Extract-Transform-Load into a warehouse/lake, then serve | batch in → batch/query out | [7.7](/data-product-types/in-b-out-b), [7.2](/data-product-types/in-b-out-br), [5.2](/data-product-types/in-s-out-br) |
| **CDC (change data capture)** | Read a source DB log and emit the changes as events | batch/state in → synthetic stream out | [7.5](/data-product-types/in-b-out-s), [7.3](/data-product-types/in-b-out-bs), [7.4](/data-product-types/in-b-out-rs) |

## Per-paradigm notes

### Serverless / Functions as a Service
The natural fit is the **stateless** cells — especially
[5.5](/data-product-types/in-s-out-s) (stream → stream, pure filter/transform/
project). Serverless is a poor fit for cells that need durable state (any cell
with `R` in OUT requires a state store the function does not own) or full
snapshots (any cell with `B` in OUT must persist a complete artifact). This is
the [state vs. stateless](/knowledge-concepts/cross-cutting-observations)
distinction restated in runtime terms.

### Event-driven architecture (EDA)
EDA is the umbrella: any product whose inputs and/or outputs are events on a
bus participates in it. The cells that are *purely* event-in/event-out
([5.5](/data-product-types/in-s-out-s), [5.3](/data-product-types/in-s-out-bs),
[3.3](/data-product-types/in-bs-out-bs)) are the "EDA-native" ones. A product
that mixes `S` with `B` or `R` is event-driven *for part* of its interface.

### Event sourcing
The event log **is** the system of record; the current state is derived by
replaying it. This is why event-sourced products characteristically take `S`
as input and serve a derived state/record out ([5.6](/data-product-types/in-s-out-r),
[5.2](/data-product-types/in-s-out-br)). Note the implication for the taxonomy:
an event-sourced product's *interface* can look identical to a non-event-sourced
one — the difference is internal, not in the cell.

### CQRS (Command Query Responsibility Segregation)
CQRS splits a system into a **write model** (command) and a **read model**
(query). The **read side** is exactly a data product whose interface is
"event/state in → queryable out":
[5.6](/data-product-types/in-s-out-r) and [4.6](/data-product-types/in-rs-out-r).
The write side is usually *not* a data product in this taxonomy (it ingests
commands but does not serve data to external consumers). CQRS and event
sourcing are frequently paired.

### Stream processing (CEP)
Stateful, continuous aggregation/join over a stream (Apache Flink, ksqlDB,
Spark Streaming). Its natural home is the rich-serving cells where a stream is
turned into a full platform:
[5.1](/data-product-types/in-s-out-brs),
[5.2](/data-product-types/in-s-out-br),
[5.6](/data-product-types/in-s-out-r).

### Microservices / API gateway / Backend-for-Frontend (BFF)
The **facade** cells — many inputs normalised into one clean request/response
API — are what an API gateway or BFF typically implements:
[6.6](/data-product-types/in-r-out-r) (thin proxy),
[1.6](/data-product-types/in-brs-out-r) (BFF / composition over files + APIs +
streams),
[4.2](/data-product-types/in-rs-out-br) (hub facade). The data product here is
the *composed API contract*; the microservices behind it are the
implementation.

### ETL / ELT / data warehouse
The classic batch pipeline into a warehouse or lake, then serve. This is the
batch-anchored core:
[7.7](/data-product-types/in-b-out-b) (pure ETL),
[7.2](/data-product-types/in-b-out-br) (warehouse: batch in, query + file out),
[5.2](/data-product-types/in-s-out-br) (streaming ELT: Kafka → lake + API).
"ELT" is the modern variant — load first, transform in-lake — but the *cell*
is the same.

### CDC (Change Data Capture)
Read a source database's transaction log and emit the changes as events. CDC
turns a batch/stateful source into a **synthetic stream** — see
[synthetic stream](/knowledge-concepts/synthetic-stream):
[7.5](/data-product-types/in-b-out-s),
[7.3](/data-product-types/in-b-out-bs),
[7.4](/data-product-types/in-b-out-rs). The taxonomy flags these as
pseudo-streams precisely because the "stream" is derived, not native.

## Data mesh

**Data mesh** is the one paradigm that sits *above* this taxonomy rather than
beside it. Data mesh treats the **data product** as the fundamental unit of
data architecture — domain-owned, self-describing, served over a platform.
This taxonomy is complementary: it classifies the **interface** of those
products regardless of how they are built. A data-mesh organisation still has
products that fall into one of the 225 cells; the paradigm says *who owns it
and how it is governed*, this taxonomy says *what interface it exposes*.

## Using this page

When you read a cell and wonder "isn't this just a serverless function / a
CQRS read model / a data warehouse?" — check the mapping table above. The
answer is almost always "this interface is *commonly implemented as* that
paradigm, but the product is the *offering*, and the architecture is a choice."
