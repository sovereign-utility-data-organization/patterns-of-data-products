# Data Product Types

* [data-product](/knowledge-concepts/data-product) - Interface model, side-state table, and the 7 × 7 quick map

## In = B+R+S

* [Data platform / warehouse facade](/data-product-types/in-brs-out-brs) - Data product ingesting via batch (bulk/file) + request/response (on-demand query) + streaming (pub/sub feed) and serving via batch (bulk/file) + request/response (on-demand query) + streaming (pub/sub feed) — data platform / warehouse facade
* [Consolidation hub with API + reports](/data-product-types/in-brs-out-br) - Data product ingesting via batch (bulk/file) + request/response (on-demand query) + streaming (pub/sub feed) and serving via batch (bulk/file) + request/response (on-demand query) — consolidation hub with api + reports
* [Hub with live feed + bulk export](/data-product-types/in-brs-out-bs) - Data product ingesting via batch (bulk/file) + request/response (on-demand query) + streaming (pub/sub feed) and serving via batch (bulk/file) + streaming (pub/sub feed) — hub with live feed + bulk export
* [Unified real-time view](/data-product-types/in-brs-out-rs) - Data product ingesting via batch (bulk/file) + request/response (on-demand query) + streaming (pub/sub feed) and serving via request/response (on-demand query) + streaming (pub/sub feed) — unified real-time view
* [All-in, single stream](/data-product-types/in-brs-out-s) - Data product ingesting via batch (bulk/file) + request/response (on-demand query) + streaming (pub/sub feed) and serving via streaming (pub/sub feed) — all-in, single stream
* [Unified query API over messy sources](/data-product-types/in-brs-out-r) - Data product ingesting via batch (bulk/file) + request/response (on-demand query) + streaming (pub/sub feed) and serving via request/response (on-demand query) — unified query api over messy sources
* [Multi-source ETL feed](/data-product-types/in-brs-out-b) - Data product ingesting via batch (bulk/file) + request/response (on-demand query) + streaming (pub/sub feed) and serving via batch (bulk/file) — multi-source etl feed

## In = B+R

* [Refreshed model serving all three out](/data-product-types/in-br-out-brs) - Data product ingesting via batch (bulk/file) + request/response (on-demand query) and serving via batch (bulk/file) + request/response (on-demand query) + streaming (pub/sub feed) — refreshed model serving all three out
* [Classic data API + file feed](/data-product-types/in-br-out-br) - Data product ingesting via batch (bulk/file) + request/response (on-demand query) and serving via batch (bulk/file) + request/response (on-demand query) — classic data api + file feed
* [RT + EOD from polled sources](/data-product-types/in-br-out-bs) - Data product ingesting via batch (bulk/file) + request/response (on-demand query) and serving via batch (bulk/file) + streaming (pub/sub feed) — rt + eod from polled sources
* [Poll/file-derived live + query](/data-product-types/in-br-out-rs) - Data product ingesting via batch (bulk/file) + request/response (on-demand query) and serving via request/response (on-demand query) + streaming (pub/sub feed) — poll/file-derived live + query
* [Poll-to-stream bridge](/data-product-types/in-br-out-s) - Data product ingesting via batch (bulk/file) + request/response (on-demand query) and serving via streaming (pub/sub feed) — poll-to-stream bridge
* [Upstream facade / proxy API](/data-product-types/in-br-out-r) - Data product ingesting via batch (bulk/file) + request/response (on-demand query) and serving via request/response (on-demand query) — upstream facade / proxy api
* [The classic ETL](/data-product-types/in-br-out-b) - Data product ingesting via batch (bulk/file) + request/response (on-demand query) and serving via batch (bulk/file) — the classic etl

## In = B+S

* [Event platform with full serving](/data-product-types/in-bs-out-brs) - Data product ingesting via batch (bulk/file) + streaming (pub/sub feed) and serving via batch (bulk/file) + request/response (on-demand query) + streaming (pub/sub feed) — event platform with full serving
* [Smart-meter platform shape](/data-product-types/in-bs-out-br) - Data product ingesting via batch (bulk/file) + streaming (pub/sub feed) and serving via batch (bulk/file) + request/response (on-demand query) — smart-meter platform shape
* [Hot & cold in → hot & cold out](/data-product-types/in-bs-out-bs) - Data product ingesting via batch (bulk/file) + streaming (pub/sub feed) and serving via batch (bulk/file) + streaming (pub/sub feed) — hot & cold in → hot & cold out
* [Event + state query, no files](/data-product-types/in-bs-out-rs) - Data product ingesting via batch (bulk/file) + streaming (pub/sub feed) and serving via request/response (on-demand query) + streaming (pub/sub feed) — event + state query, no files
* [Stream join / stream enrichment](/data-product-types/in-bs-out-s) - Data product ingesting via batch (bulk/file) + streaming (pub/sub feed) and serving via streaming (pub/sub feed) — stream join / stream enrichment
* [Stream + reference → queryable historian](/data-product-types/in-bs-out-r) - Data product ingesting via batch (bulk/file) + streaming (pub/sub feed) and serving via request/response (on-demand query) — stream + reference → queryable historian
* [Stream → settlement files](/data-product-types/in-bs-out-b) - Data product ingesting via batch (bulk/file) + streaming (pub/sub feed) and serving via batch (bulk/file) — stream → settlement files

## In = R+S

* [MDM / integration hub with full out](/data-product-types/in-rs-out-brs) - Data product ingesting via request/response (on-demand query) + streaming (pub/sub feed) and serving via batch (bulk/file) + request/response (on-demand query) + streaming (pub/sub feed) — mdm / integration hub with full out
* [Hub facade: stream + API in, API + file out](/data-product-types/in-rs-out-br) - Data product ingesting via request/response (on-demand query) + streaming (pub/sub feed) and serving via batch (bulk/file) + request/response (on-demand query) — hub facade: stream + api in, api + file out
* [Telemetry platform](/data-product-types/in-rs-out-bs) - Data product ingesting via request/response (on-demand query) + streaming (pub/sub feed) and serving via batch (bulk/file) + streaming (pub/sub feed) — telemetry platform
* [Unified live view](/data-product-types/in-rs-out-rs) - Data product ingesting via request/response (on-demand query) + streaming (pub/sub feed) and serving via request/response (on-demand query) + streaming (pub/sub feed) — unified live view
* [API-backed fan-out stream](/data-product-types/in-rs-out-s) - Data product ingesting via request/response (on-demand query) + streaming (pub/sub feed) and serving via streaming (pub/sub feed) — api-backed fan-out stream
* [Event-sourced query service (CQRS)](/data-product-types/in-rs-out-r) - Data product ingesting via request/response (on-demand query) + streaming (pub/sub feed) and serving via request/response (on-demand query) — event-sourced query service (cqrs)
* [Live activity → T+1 report/file](/data-product-types/in-rs-out-b) - Data product ingesting via request/response (on-demand query) + streaming (pub/sub feed) and serving via batch (bulk/file) — live activity → t+1 report/file

## In = S

* [Stream processor + full platform](/data-product-types/in-s-out-brs) - Data product ingesting via streaming (pub/sub feed) and serving via batch (bulk/file) + request/response (on-demand query) + streaming (pub/sub feed) — stream processor + full platform
* [Streaming ETL into lake + API](/data-product-types/in-s-out-br) - Data product ingesting via streaming (pub/sub feed) and serving via batch (bulk/file) + request/response (on-demand query) — streaming etl into lake + api
* [Hot & cold streaming platform](/data-product-types/in-s-out-bs) - Data product ingesting via streaming (pub/sub feed) and serving via batch (bulk/file) + streaming (pub/sub feed) — hot & cold streaming platform
* [Event + state, no files](/data-product-types/in-s-out-rs) - Data product ingesting via streaming (pub/sub feed) and serving via request/response (on-demand query) + streaming (pub/sub feed) — event + state, no files
* [Event transformer / relay](/data-product-types/in-s-out-s) - Data product ingesting via streaming (pub/sub feed) and serving via streaming (pub/sub feed) — event transformer / relay
* [Event-sourced read model](/data-product-types/in-s-out-r) - Data product ingesting via streaming (pub/sub feed) and serving via request/response (on-demand query) — event-sourced read model
* [Stream → settlement/rollup file](/data-product-types/in-s-out-b) - Data product ingesting via streaming (pub/sub feed) and serving via batch (bulk/file) — stream → settlement/rollup file

## In = R

* [Polling facade with synthetic stream](/data-product-types/in-r-out-brs) - Data product ingesting via request/response (on-demand query) and serving via batch (bulk/file) + request/response (on-demand query) + streaming (pub/sub feed) — polling facade with synthetic stream
* [Poll + serve API + files](/data-product-types/in-r-out-br) - Data product ingesting via request/response (on-demand query) and serving via batch (bulk/file) + request/response (on-demand query) — poll + serve api + files
* [Poller with stream + files](/data-product-types/in-r-out-bs) - Data product ingesting via request/response (on-demand query) and serving via batch (bulk/file) + streaming (pub/sub feed) — poller with stream + files
* [Poll-derived live + query](/data-product-types/in-r-out-rs) - Data product ingesting via request/response (on-demand query) and serving via request/response (on-demand query) + streaming (pub/sub feed) — poll-derived live + query
* [Poller → stream bridge](/data-product-types/in-r-out-s) - Data product ingesting via request/response (on-demand query) and serving via streaming (pub/sub feed) — poller → stream bridge
* [API proxy / facade](/data-product-types/in-r-out-r) - Data product ingesting via request/response (on-demand query) and serving via request/response (on-demand query) — api proxy / facade
* [API feed → scheduled file](/data-product-types/in-r-out-b) - Data product ingesting via request/response (on-demand query) and serving via batch (bulk/file) — api feed → scheduled file

## In = B

* [Batch-loaded platform with all out](/data-product-types/in-b-out-brs) - Data product ingesting via batch (bulk/file) and serving via batch (bulk/file) + request/response (on-demand query) + streaming (pub/sub feed) — batch-loaded platform with all out
* [The classic data warehouse](/data-product-types/in-b-out-br) - Data product ingesting via batch (bulk/file) and serving via batch (bulk/file) + request/response (on-demand query) — the classic data warehouse
* [Batch data, stream + files out](/data-product-types/in-b-out-bs) - Data product ingesting via batch (bulk/file) and serving via batch (bulk/file) + streaming (pub/sub feed) — batch data, stream + files out
* [Batch → live query + pseudo-events](/data-product-types/in-b-out-rs) - Data product ingesting via batch (bulk/file) and serving via request/response (on-demand query) + streaming (pub/sub feed) — batch → live query + pseudo-events
* [Batch → event feed](/data-product-types/in-b-out-s) - Data product ingesting via batch (bulk/file) and serving via streaming (pub/sub feed) — batch → event feed
* [The classic "load files, serve API"](/data-product-types/in-b-out-r) - Data product ingesting via batch (bulk/file) and serving via request/response (on-demand query) — the classic "load files, serve api"
* [The pure ETL file product](/data-product-types/in-b-out-b) - Data product ingesting via batch (bulk/file) and serving via batch (bulk/file) — the pure etl file product
