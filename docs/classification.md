# Classification of Data Products by Interface

Working document. Mark decisions with `[decided]`, open items with `[open]`.

## 1. Definitions

**Data product** `[proposed]`
> A self-contained offering of data to external consumers, comprising the data
> itself, a contract/metadata describing it (schema, semantics, update cycle,
> access conditions), and one or more interfaces for consumption. The value is
> in the product, not the underlying database.

**Interface** `[open]`
> The mechanism a consumer uses to access or subscribe to the data: protocol,
> interaction pattern (request/response vs. subscription), and the level of
> abstraction exposed (raw bytes, tabular/query result, semantic query).

Questions to close:
- [ ] Is the interface a technical property (protocol) or a functional one
  (consumption pattern)? Or both, on different axes?
- [ ] Do we classify **single-interface** products or **multi-interface**
  products (one product, several interfaces)?

## 2. Interface model `[decided 2026-11-06]`

An interface is described by **three atomic integration patterns**, each
independent of any particular protocol:

1. **Batch** — bulk/file delivery on a schedule (ftp, S3, files on a portal)
2. **Request/response** — synchronous on-demand query (REST, OData, GraphQL, JDBC)
3. **Streaming** — continuous pub/sub push (Kafka, MQTT, CDC events)

And a **side**: the pattern applies to the product's **input** side or its
**output** side. Any non-empty subset of the three patterns can occur on
each side → 7 side states (3 singles + 3 pairs + all-three). A data product
type is a pair (IN-state × OUT-state) → **7 × 7 = 49 combinations**.

- Figure: `all-possible-data-product-patterns.svg`
- One description per combination (what it is, when to use it, verdict
  common / plausible / niche / awkward): `options.md`

The older candidate category list below is kept as a starting point for
mapping *specific* products into the matrix, not as an alternative taxonomy.

## 3. Candidate interface categories

| Category | Consumption pattern | Example bindings |
|---|---|---|
| File-based / batch pull | Consumer pulls files on a schedule | FTP, S3/object store, SFTP, web download, CSV/Parquet/JSON feed |
| Query / request–response | Consumer asks, provider answers per request | REST/SQL-over-HTTP, GraphQL, OData, JDBC/ODBC |
| Streaming / subscription | Provider pushes continuously, consumer subscribes | Kafka topics, MQTT, gRPC streams, WebSocket push, CDC (change data capture) |
| Event-driven / message | Provider emits discrete events, consumer reacts | Message queues (AMQP, JMS), event bus, Pub/Sub, WebHook callbacks |
| Semantic / knowledge access | Consumer queries meaning, not just records | SPARQL endpoint, RDF/JSON-LD API, ontology-based access |
| Portal / manual | Human interaction, no machine binding | Data portal, spreadsheet download, API-key–gated catalog |

`[open]` Candidates not yet placed:
- Streaming file delivery (chunked/object-part)
- Batch "push" to consumer (provider delivers to consumer's endpoint)
- Embedded / SDK-style access vs. networked access
- Access via identity/permission boundaries (is "authorized API" its own class, or an attribute?)

## 4. Classification dimensions

Candidate axes to attach to every category `[open]`:

1. **Synchronicity** — synchronous request/response vs. asynchronous delivery
2. **Cardinality of interaction** — single pull vs. continuous feed
3. **Binding level** — raw bytes → structured records → semantic query
4. **Initiator** — consumer pulls vs. provider pushes
5. **Coupling** — direct (consumer needs protocol knowledge) vs. mediated
   (service/schema abstraction)
6. **State exposure** — point-in-time snapshot vs. change history / latest
7. **Transport/protocol family** — HTTP-based, socket-based, file-based,
   semantic (SPARQL), in-process
8. **Contract style** — schema-registry-based vs. free-form vs. ontology-based

## 5. Examples to file under categories

To collect:
- [ ] Market data: published price files (day-ahead auction results)
- [ ] Grid/SCADA feeds (streaming)
- [ ] Settlement files (batch, contractual)
- [ ] Device telemetry (Kafka/MQTT)
- [ ] SPARQL endpoints over master data
- [ ] OData/ESDP endpoints (energy sector)
- [ ] "Just a shared folder" cases

## 6. Open questions

- [ ] What is the unit of classification: a product, an interface instance,
      or an interface *kind*?
- [ ] Multi-interface products: do we classify the product by its *primary*
      interface, or list all with weights?
- [ ] How close should the taxonomy be to existing vocabularies (ODRL, DCAT,
      schema.org `DigitalDocument`/`APIReference`, W3C data activity vocabulary)?
- [ ] Target consumers of the taxonomy: cataloging, API design review,
      procurement?
- [ ] Formalization target: simple markdown table → LinkML → SHACL/SHACL shapes?

## 7. Changelog

- 2026-11-06: interface model decided — 3 integration patterns (batch,
  request/response, streaming) × input/output side → 7 × 7 = 49 product
  combinations; figure `all-possible-data-product-patterns.svg` and
  per-combination descriptions in `options.md`
- 2026-11-06: initial scaffolding (repo setup on Gitea)
