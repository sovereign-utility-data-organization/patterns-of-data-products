---
type: Knowledge Concept
okf_version: '0.1'
timestamp: '2026-11-06T21:15:00Z'
description: The streaming integration pattern (S) — continuous pub/sub push, applied on a product's input side (event consumption) or output side (feed serving).
title: Streaming integration pattern
tags:
- integration-pattern
- streaming
- pubsub
related:
- /knowledge-concepts/data-product
- /knowledge-concepts/pattern-batch
- /knowledge-concepts/pattern-request-response
- /knowledge-concepts/pattern-human
- /knowledge-concepts/synthetic-stream
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

If a product serves `S` **without** taking `S` as input, its stream is
*synthetic* — derived from polls or bulk loads. Such cells need explicit
change-detection and replay semantics, or they are a *pseudo-stream* —
see [synthetic stream](/knowledge-concepts/synthetic-stream).

## Where it appears

- Pure cells: `row 5` (stream-only in) and `column 5` (stream-only out)
- Mixed: `BS` (hot & cold), `RS` (live + lookup), `BRS` (omni-channel)
