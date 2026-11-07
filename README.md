# Data Product Classification by Interface

A working project to classify **data products** based on the **interface** they
expose to consumers.

A data product is treated as a self-contained unit — the data, its
metadata/contract, and the interface through which it is consumed — rather than
as a raw dataset. The interface is the primary axis of differentiation: two
data products on the same underlying data can be fundamentally different
products depending on how they are exposed (e.g. file download vs. query API
vs. event stream).

## Published site

This catalog is also published as a browsable site at
<https://sovereign-utility-data-organization.github.io/patterns-of-data-products/>.
Every push to `main` builds and redeploys it via GitHub Actions
(`.github/workflows/pages.yml`): `scripts/build_site.py` rewrites the canonical
OKF links to paths a static host resolves, renders each page with Jekyll, and
adds a search box. The bundle in this repository remains the authoritative,
OKF-conformant source.

## Structure

This repository **is** the knowledge catalog — an
[Open Knowledge Format (OKF) v0.1](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)
bundle: a directory of markdown concept docs with YAML frontmatter,
`index.md` listings (no frontmatter), and an update `log.md`.

| Path | Purpose |
|---|---|
| `index.md` | Root directory listing (entry point) |
| `log.md` | Update log |
| `knowledge-concepts/` | Core vocabulary: data product, the 4 integration patterns, interface model, human pattern, synthetic stream, cross-cutting observations |
| `data-product-types/` | The 225 data product types (IN × OUT) — one concept doc each, plus the matrix index |
| `playbooks/` | How to use the catalog (classify a real data product) |
| `assets/` | The human-pattern interface figure and the 49-cell (3-pattern) grid figure, plus per-cell diagrams |
| `scripts/okf_audit.py` | OKF v0.1 conformance audit (frontmatter + cross-link checks); run `python3 scripts/okf_audit.py` |

## Related work

- Data management practice: `utility-data-management-course`, `data-management-colab-eu`
- Standards context: `standards-catalog`
- Formalization tooling: `linkml` profiles (see `kg-generator`, `cim-linkml-owl` if reused)

## Contributing

This is a working repo: push branches, open issues for open questions, keep the
`docs/classification.md` checklists up to date.
