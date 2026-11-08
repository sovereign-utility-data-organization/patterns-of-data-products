---
type: Knowledge Concept
okf_version: '0.1'
timestamp: '2026-11-08T19:19:00Z'
description: The streaming integration pattern (S) — continuous pub/sub push, applied on a product's input side (event consumption) or output side (feed serving).
definition: "The streaming integration pattern (S): continuous, push-based movement of an ordered sequence of events or records at the producer's pace - pub/sub - applied on either side of a data product: consuming events on the input side, serving a feed on the output side."
example: "Consuming meter telemetry on IN; serving an enriched event feed to settlement engines on OUT"
altLabel:
- "S"
- "pub/sub"
- "event streaming"
- "feed serving"
scopeNote: "Protocol-agnostic at the pattern level; typical bindings are Kafka/Pulsar topics, MQTT, gRPC/WebSocket streams, CDC event streams, pub/sub message buses. A cell that serves S without taking S in is a synthetic-stream suspect."
title: Streaming integration pattern
tags:
- integration-pattern
- streaming
- pubsub
related:
- /concepts/data-product
- /concepts/pattern-batch
- /concepts/pattern-request-response
- /concepts/pattern-human
- /concepts/synthetic-stream
---
# Streaming pattern (`S`)

Continuous, push-based data movement: the product emits (or consumes) a
continuous sequence of events/records, ordered, at the producer's pace.
Protocol-agnostic at this level; typical bindings: Kafka/Pulsar topics,
MQTT, gRPC/WebSocket streams, CDC event streams, pub/sub message buses.

## On the input side

The product *subscribes* to live sources: meter events, telemetry, market
events, system events. Semantics in the contract:

- **ordering and partitioning** — what ordering guarantees mean,
- **replay/backfill** — how historical events are re-issued,
- **consumer lag policy** — how much latency is normal.

## On the output side

Consumers *subscribe*: downstream processors, CEP, dashboards,
settlement engines ingesting in real time. Serving on `S` can be
**stateless** (the product merely transforms or routes events — cell type
`5.5`) or **stateful** (events are joined with state and projected forward —
cell types `5.1`, `3.3`, …).

## The catch

If a product serves `S` **without** taking `S` as input, that is a
red flag: the stream is *synthetic* — derived from polls or bulk loads off a
state-only source — unless the events are **delivered actions** (a human
acting through the product's own surface), in which case the feed is
**trigger-based**, i.e. a real event stream. Synthetic cells need explicit
change-detection and replay semantics — see
[synthetic stream](/concepts/synthetic-stream).

## Where it appears

- Pure cells: `row 5` (stream-only in) and `column 5` (stream-only out)
- Mixed: `BS` (hot & cold), `RS` (live + lookup), `BRS` (omni-channel)
