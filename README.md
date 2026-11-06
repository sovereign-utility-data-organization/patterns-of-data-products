# Data Product Classification by Interface

A working project to classify **data products** based on the **interface** they
expose to consumers.

A data product is treated as a self-contained unit — the data, its
metadata/contract, and the interface through which it is consumed — rather than
as a raw dataset. The interface is the primary axis of differentiation: two
data products on the same underlying data can be fundamentally different
products depending on how they are exposed (e.g. file download vs. query API
vs. event stream).

## Status

- [x] Interface model settled: 3 integration patterns (batch, request/response,
      streaming) × input/output side → 7 × 7 = **49 data product types**
- [x] Full combinatoric space figured (`docs/all-possible-data-product-patterns.svg`)
- [x] One description per combination: what it is, when to use it, verdict
      (`docs/options.md`)
- [ ] Map existing known data products onto the 49 cells
- [ ] Classification dimensions (per side and/or per cell)
- [ ] Formalization (candidate: LinkML / SHACL)
- [ ] Review and v0.1

## Structure

| Path | Purpose |
|---|---|
| `docs/classification.md` | Main working document: definitions, interface model, dimensions, open questions |
| `docs/options.md` | Description of each of the 49 data product types (input patterns × output patterns) |
| `docs/all-possible-data-product-patterns.svg` | The 7 × 7 grid figure of all combinations |
| `assets/` | Other figures and diagrams |

## Related work

- Data management practice: `utility-data-management-course`, `data-management-colab-eu`
- Standards context: `standards-catalog`
- Formalization tooling: `linkml` profiles (see `kg-generator`, `cim-linkml-owl` if reused)

## Contributing

This is a working repo: push branches, open issues for open questions, keep the
`docs/classification.md` checklists up to date.
