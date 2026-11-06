# The 49 Data-Product Interface Patterns

> Companion to the figure `all-possible-data-product-patterns.svg`.
> Each cell is one **data product type**, defined by:
> - **IN** — the set of integration patterns the product uses to *take in* data
> - **OUT** — the set of integration patterns the product *serves* data on
>
> Patterns (short names): **B** = batch (file/bulk), **R** = request/response
> (synchronous API/query), **S** = streaming (pub/sub, event feed).
> Any non-empty subset of {B, R, S} is possible on each side → **7 × 7 = 49
> combinations** (a side with no patterns at all is not a data product — a
> pure file dump or a pure sink is not a *product*).

## Side states (the 7 rows/columns)

| Code | Patterns | Working name | Typical meaning on a side |
|---|---|---|---|
| `O` | B+R+S | **omni-channel** | all three: files, on-demand query, live feed |
| `RB` | B+R | **query + file** | on-demand access plus bulk/file delivery |
| `BS` | B+S | **hot & cold** | live feed plus bulk archive |
| `RS` | R+S | **live + lookup** | live feed plus on-demand query |
| `S` | S | **stream-only** | continuous pub/sub only |
| `R` | R | **request-response** | synchronous on-demand only |
| `B` | B | **batch-only** | file/bulk only |

## The 7 × 7 matrix (quick map)

Rows = **IN**, columns = **OUT**. Each cell links to its description below.

| IN \ OUT | O (B+R+S) | RB (B+R) | BS (B+S) | RS (R+S) | S | R | B |
|---|---|---|---|---|---|---|---|
| **O** (B+R+S) | 1.1 | 1.2 | 1.3 | 1.4 | 1.5 | 1.6 | 1.7 |
| **RB** (B+R) | 2.1 | 2.2 | 2.3 | 2.4 | 2.5 | 2.6 | 2.7 |
| **BS** (B+S) | 3.1 | 3.2 | 3.3 | 3.4 | 3.5 | 3.6 | 3.7 |
| **RS** (R+S) | 4.1 | 4.2 | 4.3 | 4.4 | 4.5 | 4.6 | 4.7 |
| **S** | 5.1 | 5.2 | 5.3 | 5.4 | 5.5 | 5.6 | 5.7 |
| **R** | 6.1 | 6.2 | 6.3 | 6.4 | 6.5 | 6.6 | 6.7 |
| **B** | 7.1 | 7.2 | 7.3 | 7.4 | 7.5 | 7.6 | 7.7 |

Verdict legend: 🟢 **common** · 🟡 **plausible, project-specific** · 🔵 **niche / bridge role** · 🔴 **awkward or usually wrong**

---

## Row 1 — IN = B+R+S (ingests from files, on demand, and live)

A product that pulls from all three kinds of upstream. Usually a **consolidation
layer**: it exists because the source world is messy and consumers want a single,
clean view.

**1.1 — in: B+R+S → out: B+R+S — "Data platform / warehouse façade"** 🟢
Ingests from every kind of source; serves live events, on-demand queries, *and*
bulk files. This is the full data platform (data lakehouse, CDP).
*Use when:* one organisation must serve many consumer types (BI, API clients,
settlement, real-time dashboards) from a consolidated view.
*Watch out:* the most expensive option — you own all three serving stacks.

**1.2 — in: B+R+S → out: B+R — "Consolidation hub with API + reports"** 🟢
Everything goes in; consumers get a clean query API plus scheduled files — no
streaming out. The most economical "good facade" when consumers are
pollers and report writers.
*Use when:* no real-time requirement; you just need one API + one file feed.

**1.3 — in: B+R+S → out: B+S — "Hub with live feed + bulk export"** 🟢
Consolidated source data exposed as a continuous stream and as bulk archives.
*Use when:* consumers react to change but also need full loads (historians,
downstream stream consumers, reconciliation).
*Example:* enterprise event spine with S3 archive.

**1.4 — in: B+R+S → out: R+S — "Unified real-time view"** 🟢
Consumers query current state *and* subscribe to changes — no bulk files.
*Use when:* all consumers are online; historical depth is served by query, not
by file.
*Example:* IOT/time-series platform with event + state APIs.
*Watch out:* long-term archive may still be needed off-line (B) to keep
storage sane.

**1.5 — in: B+R+S → out: S — "All-in → single stream"** 🔵
A "one topic for the world": all sources (files included, replayed as events)
funneled into one pub/sub.
*Use when:* downstream is a pure stream topology (Kafka mesh, CEP fabric).
*Watch out:* file-based sources become synthetic streams — backfill is loud.

**1.6 — in: B+R+S → out: R — "Unified query API over messy sources"** 🟢
The BFF / service façade: files + upstream APIs + event feeds behind one
request/response contract.
*Use when:* the product's value is *normalisation*: consumers want one
schema + one endpoint.
*Example:* unified "customer" or "order" API over CRM/ERP/events.

**1.7 — in: B+R+S → out: B — "Multi-source ETL feed"** 🟡
Everything in, one file out. The consolidation layer with a single
publication surface (e.g., a settlement or reporting bundle).
*Use when:* the consumer side is contractual (file delivery) — very common in
utility settlement (meter events + tariff APIs + reference files in → one
settlement file out).
*Watch out:* latency expectations collapse to the batch cycle.

---

## Row 2 — IN = B+R (ingests files + on-demand pull; no live source)

The most common "integration service" shape: the product refreshes from
upstream feeds and APIs, and re-serves in its chosen patterns.

**2.1 — in: B+R → out: B+R+S — "Refreshed model with every out, incl. stream"** 🟡
A polled/file-fed state store that publishes a *synthetic* change stream
in addition to API + files.
*Use when:* consumers need events, but the source world only offers files/APIs
→ the product computes change detection.
*Watch out:* streams derived from polling are chatty and lossy-ish; define
"change" semantics explicitly.

**2.2 — in: B+R → out: B+R — "Classic data API + file feed"** 🟢
The bread and butter: e.g., a weather/price API that also serves daily
bundles. *Use when:* consumers are a mix of online pollers and ETL consumers;
no live requirement.
*Example:* tariff/product API + nightly snapshot files.

**2.3 — in: B+R → out: B+S — "RT + EOD from polled sources"** 🟡
Served as both a "live" feed and end-of-day files, but the live feed is
re-poll-derived (e.g., polling market data into a stream, plus EOD files).
*Use when:* market/utility data consumers expect both a real-time feed and an
EOD file, but the upstream is only file/API.
*Watch out:* "real-time" is bounded by poll interval.

**2.4 — in: B+R → out: R+S — "Poll-derived live + query"** 🔵
Stream + query API built on polled/file inputs.
*Use when:* a dashboard wants "live" data but the only source is scheduled
polls (device registries, market pages).
*Watch out:* every data point must carry a freshness stamp; polling latency
is the truth.

**2.5 — in: B+R → out: S — "Poll-to-stream bridge"** 🔵
A bridge product whose whole job is "files/APIs → topics".
*Use when:* a Kafka-first world must consume legacy file/API sources.
*Watch out:* mostly a glue role; consumers may expect push semantics the
source can't honour — document deltas, snapshots, and backfill rules.

**2.6 — in: B+R → out: R — "Upstream façade / proxy API"** 🟢
Polled from upstream, served as one cleaner API.
*Use when:* value = schema/semantics + caching, not transformation volume.
*Example:* tariff API over supplier web-services + rate tables.

**2.7 — in: B+R → out: B — "The classic ETL"** 🟢
Files + APIs in → file(s) out. The oldest and most common data product that
exists (supplier feeds + master APIs → settlement/report files).
*Use when:* the contract with consumers is a file on a schedule.

---

## Row 3 — IN = B+S (ingests live feed + bulk loads; no API pull)

The **hot & cold** ingestion shape: real-time events *and* reference/bulk data.
Very common in telemetry, markets, and metering.

**3.1 — in: B+S → out: B+R+S — "Event platform with full serving"** 🟢
Hot & cold ingest (e.g., Kafka + S3) served via streams, APIs, and bulk
exports. The modern streaming platform (e.g., Kafka + Iceberg/Delta).
*Use when:* you need all three consumer types on top of event data.

**3.2 — in: B+S → out: B+R — "Smart-meter platform shape"** 🟢
Live events in, API + files out: e.g., smart-meter readings (stream) + tariff
reference (batch) → reading API + settlement files. *The* common utility
shape. No pure stream out — consumers pull.

**3.3 — in: B+S → out: B+S — "Hot & cold in → hot & cold out"** 🟢
A pass-through streaming platform: events stay events; bulk in becomes bulk
out (or is merged in).
*Use when:* consumers subscribe to feeds *and* consume archives; you want a
single consistent pipeline.
*Example:* Kafka mirror + S3 archive service.

**3.4 — in: B+S → out: R+S — "Event + state query, no files"** 🔵
Live events and on-demand state queries; no bulk serving.
*Use when:* consumers are online and bulk export is a different product's job.
*Watch out:* long-term retention usually still wants a cold tier/file tier —
verify you're not just deleting history.

**3.5 — in: B+S → out: S — "Stream-join / stream enrich"** 🟡
Enriches an event stream with bulk-loaded reference data, emits enriched
stream. *Use when:* the product's value = enrichment; consumers are stream
consumers.
*Example:* meter event stream + tariff/version reference → enriched market
events.

**3.6 — in: B+S → out: R — "Stream + reference → queryable historian"** 🟢
The historian pattern: events land in a time-series DB, reference data is
periodically loaded, consumers query. (e.g., SCADA historian + historian API)
*Use when:* consumers want analysis over history, not push.

**3.7 — in: B+S → out: B — "Stream → settlement files"** 🟢
Real-time metered events + reference data in → daily settlement file out.
*Use when:* the market contract is file-based (day-ahead / imbalance
settlement) but data is inherently streaming. *This is the heart of many
utility settlement engines.*

---

## Row 4 — IN = R+S (ingests on demand + live; no bulk in)

The product's inputs are *live*: it watches the world via events and refreshes
itself via calls. No nightly file ingestion.

**4.1 — in: R+S → out: B+R+S — "MDM / integration hub with full out"** 🟡
Lives entirely on APIs + events; emits files, streams, and APIs — including
bulk exports built from incremental change logs.
*Use when:* you are the "system of record glue" (master data hub, order hub).
*Watch out:* full-load exports need a complete state store — build it.

**4.2 — in: R+S → out: B+R — "Order/hub façade: stream + API in, API + file out"** 🟢
Classic: events + service APIs in; consumers get the query API and nightly
exports (e.g., billing: events + tariff API → invoice API + D01 files).
*Use when:* consumer mix is online + batch, and source is online.

**4.3 — in: R+S → out: B+S — "Telemetry platform"** 🟡
Events + device/service APIs in; live feeds + bulk archives out.
*Use when:* consumers want both push and periodic full loads.
*Example:* vehicle/IoT telemetry: CAN-stream + OBD API → fleet stream + daily
trip files.

**4.4 — in: R+S → out: R+S — "Unified live view"** 🟢
A clean real-time façade: one stream + one query API over the combined
inputs. *Use when:* consumers are all online and you want one consistent
contract. *Example:* unified telemetry/asset platform.

**4.5 — in: R+S → out: S — "API-backed fan-out stream"** 🔵
Changes (computed from event + API state) fanned out as one stream.
*Use when:* downstream is stream-first; the stream *is* the product.
*Watch out:* API-polled changes become synthetic events — define exactly what
"change" means (field-level? version bump?).

**4.6 — in: R+S → out: R — "Event-sourced query service (CQRS)"** 🟢
Ingest the stream, build the read model, serve the API. The canonical
event-sourcing read side (e.g., order-status API from order events +
master data APIs). *Very common* when you want a queryable view without
exposing the event world.
- *Note:* this is the "stream → state" product; 4.5 is the same inputs with
  the stream as output.

**4.7 — in: R+S → out: B — "Live activity → T+1 report/file"** 🟡
Consumes live events + APIs, publishes a file once a day (activity report,
usage file, billing input). *Use when:* the contract is a file but the data
is inherently live.
*Watch out:* consumers get T+1 of a T+0 world — publish with clear
"as-of" semantics if you can.

---

## Row 5 — IN = S (pure streaming in)

The product only accepts pushes. Everything it knows to do comes from the
stream(s).

**5.1 — in: S → out: B+R+S — "Stream processor + full platform"** 🟢
A stream in → stream processor / stateful aggregation → *all* serving modes.
(The Flink/Kafka + state store + sink world.)
*Use when:* the product owns the aggregation layer between events and
consumers.

**5.2 — in: S → out: B+R — "Streaming ETL into lake + API"** 🟢
Events → queryable store + data-lake files. *The* standard modern
ingestion architecture (Kafka → S3 + API over a query engine / Iceberg).
*Use when:* consumers want analysis (API) + archival (files); no need to
keep the stream out.

**5.3 — in: S → out: B+S — "Hot & cold streaming platform"** 🟢
Events in → events out (transformed/joined) + files out (archival).
*Use when:* consumers include stream consumers (downstream processors, CEP)
and file consumers (analytics, settlement).
*Example:* a market event spine: enriched events + daily bundles.

**5.4 — in: S → out: R+S — "Event + state, no files"** 🔵
Stream in → event feed + state API; no bulk out. *Use when:* all consumers
are online and archival is handled off-product.
*Watch out:* same retention concern as 3.4.

**5.5 — in: S → out: S — "Event transformer / relay"** 🟢
A pure stream-to-stream product: filter, route, enrich, project. (Kafka
topology: topic in → topics out.)
*Use when:* consumers need a *derived* topic; the value is in the
transformation, not the serving.
*Watch out:* no state persistence beyond the topic — the product is
stateless by nature.

**5.6 — in: S → out: R — "Event-sourced read model"** 🟢
Events in → state out via API. The canonical "stream → queryable state"
product (order status, device state, meter state APIs).
*Use when:* consumers don't want to consume a stream, they want the answer.
*Note:* this is a *special case* of 5.2 (S → B+R) without the file side.

**5.7 — in: S → out: B — "Stream → settlement/rollup file"** 🟡
Events in → periodic bulk out. E.g., meter reading stream → daily interval
file; clickstream → EOD usage files.
*Use when:* the contract is a file but the data is inherently streaming
(very common in utility settlement).

---

## Row 6 — IN = R (pure request/response in; poll upstream)

The product only *pulls* from upstream, on demand (or on a schedule it
disguises as "on demand").

**6.1 — in: R → out: B+R+S — "Polling façade with synthetic stream"** 🔵
Polls upstream, computes deltas, serves file + API + a *synthetic* change
stream. *Use when:* the source world is file/API-only and downstream is
event-driven.
*Watch out:* you own the change-detection semantics + backfill rules; the
"stream" is an illusion over polling cadence.

**6.2 — in: R → out: B+R — "Poll + serve API + files"** 🟡
A refreshed service: polls upstream, exposes a cleaner API, and also emits
periodic full-load files.
*Use when:* consumers are a mix of online pollers + ETL consumers, and the
upstream is API-only. (E.g., supplier meter API → reading API + daily
snapshot files.)

**6.3 — in: R → out: B+S — "Poller with stream + files"** 🔵
API in, stream out (synthetic) + files out. Bridge from a polled world into a
streaming world + an archival file set.
*Watch out:* same synthetic-stream caveat.

**6.4 — in: R → out: R+S — "Poll-derived live + query"** 🔵
API in, live feed + API out. *Use when:* consumers want push + query and the
only source is pollable.
*Watch out:* same synthetic caveats; latency is bounded by poll cadence.

**6.5 — in: R → out: S — "Poller → stream bridge"** 🔵
The canonical "bridge an API world into a Kafka world" product.
*Use when:* you have a stream-driven consumer architecture and only
file/API sources exist.
*Watch out:* this is the *most common* source of "why is my stream lagging"
complaints; define poll interval, idempotency, and backfill explicitly.

**6.6 — in: R → out: R — "API proxy / façade"** 🟢
The cleanest "value = a better surface" product: normalise schemas, add
caching/semantics, hide auth quirks, serve one clean API.
*Use when:* no transformation-heavy load; the value is *integration
experience* (canonical schema + auth + semantics).
*Example:* OData/ESDP façade over supplier REST.

**6.7 — in: R → out: B — "API feed → scheduled file"** 🟢
Poll from upstream, publish a file. The classic "fetch-and-drop" integration
(e.g., supplier portal API → settlement file; or tariff API → rate
table file).
*Use when:* the contract is file-based delivery; the source is API-based.

---

## Row 7 — IN = B (pure batch in)

The product's world is: files in, something out. The oldest data-products
pattern.

**7.1 — in: B → out: B+R+S — "Batch-loaded platform with all out"** 🟡
A nightly-loaded warehouse that also serves a (CDC or refresh-derived)
stream + API + files. *Use when:* you need the full consumer mix but the
source world is batch-only.
*Watch out:* the "stream out" is synthetic (CDC on a refreshed table); make
the semantics explicit.

**7.2 — in: B → out: B+R — "The classic data warehouse"** 🟢
Files in → API + files out. The standard ETL/ELT target that also serves a
query API on top (e.g., EOD price files → price API + downstream files).
*Use when:* consumers need both an analytical API and bulk delivery;
upstream is batch.
*Example:* market price files → price API + settlement files.

**7.3 — in: B → out: B+S — "Batch data, stream + files out"** 🔵
Nightly load + a stream out (CDC from the refreshed table — a "pseudo-stream").
*Use when:* consumers want to react to changes but upstream only publishes
files. *Watch out:* latency = batch cadence; document clearly.

**7.4 — in: B → out: R+S — "Batch → live query + pseudo-events"** 🔵
Same inputs as 7.3 but with a query API instead of files. *Use when:* consumers
are online and events-only; you serve "live" over a nightly refresh.
*Watch out:* "live" is a lie — label it "as-of last refresh".

**7.5 — in: B → out: S — "Batch → event feed"** 🔵
Turn a daily bulk load into a stream of events (snapshots → deltas).
*Use when:* downstream is a pure event world and the source is a legacy
batch world. *Watch out:* this is a *replay* product; consumers must treat
each batch as a batch of synthetic events, not a continuous feed.

**7.6 — in: B → out: R — "The classic 'load files, serve API'"** 🟢
Files in → one clean API out (e.g., nightly price/tariff files → price/tariff
API). *The most common single-pattern data product* in regulated/utility
domains (where upstream is file-based and consumers are online).

**7.7 — in: B → out: B — "The pure ETL file product"** 🟢
Files in → files out. The original data product: transformation +
publication, no serving stack beyond the file contract.
*Example:* any "settlement input bundle" product.
*Use when:* the contract is a file and the load is scheduled; you want the
cheapest possible product. *Watch out:* no live semantics at all; publish
with explicit as-of.

---

## Cross-cutting notes

1. **Synthetic streams.** Any cell with `S` in **OUT** but not in **IN**
   (2.1, 2.3–2.5; 6.1, 6.3–6.5; 7.1, 7.3–7.5) is a *pseudo-stream* — the
   product computes change-detection on top of a non-streaming source. Always
   document: what counts as a change, the poll cadence / refresh lag,
   idempotency, and backfill semantics.
2. **Symmetry is a smell.** Cells on the diagonal (IN = OUT pattern set) are
   usually *pass-throughs* with little transformation value — they exist
   mainly for routing, auth, or schema normalisation. Products off the
   diagonal are doing real *format/temporal* conversion.
3. **Batch-anchored products dominate the utility sector:** batch in → API
   out (7.6, 7.2) and streaming in → file out (5.7, 3.7, 4.7) are the two
   most load-bearing data product archetypes in energy/utility markets.
4. **State vs. stateless.** Products with `R` in OUT (queryable) need a
   durable state store; products with only `S` in OUT (1.5, 5.5, 6.5, 7.5)
   can be stateless. Products with `B` in OUT need storage sized for a
   *full snapshot* (a big cost factor).
