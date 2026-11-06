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

- [ ] Scope and definitions settled
- [ ] Candidate interface categories drafted
- [ ] Classification dimensions identified
- [ ] Catalog of example data products per category
- [ ] Formalization (candidate: LinkML / SHACL)
- [ ] Review and v0.1

## Structure

| Path | Purpose |
|---|---|
| `docs/classification.md` | Main working document: definitions, candidate categories, dimensions, open questions |
| `docs/` | Further working documents (dimensions, examples, formalization notes) as they are split out |
| `assets/` | Figures and diagrams |

## Related work

- Data management practice: `utility-data-management-course`, `data-management-colab-eu`
- Standards context: `standards-catalog`
- Formalization tooling: `linkml` profiles (see `kg-generator`, `cim-linkml-owl` if reused)

## Contributing

This is a working repo: push branches, open issues for open questions, keep the
`docs/classification.md` checklists up to date.
