# Concepts

* [data-product](/concepts/data-product) - What a data product is (in the data-mesh sense): a self-contained, domain-owned unit — data + usable semantics/quality/provenance + code + infrastructure — served through one or more output ports (interfaces); identity is the data, not the ports; the interface model (4 patterns × 2 sides → 15 side states → 15×15 = 225 types)
* [pattern-batch](/concepts/pattern-batch) - Batch (B): bulk/file on a schedule, on input or output side
* [pattern-request-response](/concepts/pattern-request-response) - Request/response (R): synchronous on-demand query; polling upstream or serving APIs
* [pattern-streaming](/concepts/pattern-streaming) - Streaming (S): continuous pub/sub push; event consumption or feed serving
* [pattern-human](/concepts/pattern-human) - Human (H): data produced by people (in) or a human-facing surface (out); the 4th, orthogonal pattern
* [synthetic-stream](/concepts/synthetic-stream) - Pseudo-streams: the cells that serve S without ingesting S, and the contract items they need
* [role-of-human-input](/concepts/role-of-human-input) - What human input (H in IN) actually is: softness (quality cost), the automate-where-possible default, and irreplaceability (human input as the value-driver), and how H plays with B/R/S
* [cross-cutting-observations](/concepts/cross-cutting-observations) - Structural properties of the 225-type space: pass-through diagonal, batch core, state vs. cost, the human layer
* [verdict](/concepts/verdict) - The verdict tag (common / plausible / niche) attached to each data product type, and what each means
* [architectural-paradigms](/concepts/architectural-paradigms) - How serverless, event-driven, event sourcing, CQRS, stream processing, microservices, ETL, CDC, and data mesh relate to (but are distinct from) the interface taxonomy
