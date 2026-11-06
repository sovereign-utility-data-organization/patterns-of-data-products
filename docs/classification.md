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

## 2. Candidate interface categories

Draft list — to be pruned, renamed, split, merged. Grouping by *consumption
pattern* rather than by protocol, with protocols as secondary attribute.

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

## 3. Classification dimensions

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

## 4. Examples to file under categories

To collect:
- [ ] Market data: published price files (day-ahead auction results)
- [ ] Grid/SCADA feeds (streaming)
- [ ] Settlement files (batch, contractual)
- [ ] Device telemetry (Kafka/MQTT)
- [ ] SPARQL endpoints over master data
- [ ] OData/ESDP endpoints (energy sector)
- [ ] "Just a shared folder" cases

## 5. Open questions

- [ ] What is the unit of classification: a product, an interface instance,
      or an interface *kind*?
- [ ] Multi-interface products: do we classify the product by its *primary*
      interface, or list all with weights?
- [ ] How close should the taxonomy be to existing vocabularies (ODRL, DCAT,
      schema.org `DigitalDocument`/`APIReference`, W3C data activity vocabulary)?
- [ ] Target consumers of the taxonomy: cataloging, API design review,
      procurement?
- [ ] Formalization target: simple markdown table → LinkML → SHACL/SHACL shapes?

## 6. Changelog

- 2026-11-06: initial scaffolding (repo setup on Gitea)
