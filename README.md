# Data Product Classification by Interface

A working project to classify **data products** based on the **interface** they
expose to consumers.

A data product is treated as a self-contained unit — the data, its
metadata/contract, and the interface(s) through which it is consumed — rather
than as a raw dataset. The term is used in the sense of **data mesh**: a data
product is a domain-owned, self-describing unit of data architecture that
consumers can depend on. A product's identity is the data it offers and the
contract it serves under — not how the data is exposed: the same records
served as a file download, a query API, or an event stream are one data
product through several interfaces, not different products. The interface is
the axis on which this catalog distinguishes **types** of data products (the
IN × OUT pattern combination) — it is what the 225 types differ by, not what
makes a product a product.

## This repo is an OKF catalog

This repository **is** the catalog — an
[Open Knowledge Format (OKF) v0.1](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)
bundle and the **authoritative source of truth**: markdown concept docs with
YAML frontmatter, `index.md` section listings, and an update `log.md`.
Conformance (frontmatter, ISO-8601 timestamps, and every internal link
resolving to a real doc or section) is enforced by `scripts/okf_audit.py`.
The bundle is complete and self-contained here, in the repository.

## Published site

The site at <https://sovereign-utility-data-organization.github.io/patterns-of-data-products/>
is not a second copy — it is **generated from this OKF bundle**. It is a
derived, read-only artifact that is never hand-edited: every push to `main`
runs `scripts/build_site.py` via GitHub Actions (`.github/workflows/pages.yml`),
which **reads the bundle unchanged**, rewrites each bundle-absolute OKF link to
a path a static host resolves, renders every page to HTML, and adds a global
search bar. The build is self-contained Python (no Docker or framework) and
leaves the bundle byte-for-byte intact. So the canonical OKF source stays in
this repository, and the published site is always a faithful rendering of it.

## Structure

This repository **is** the knowledge catalog — an
[Open Knowledge Format (OKF) v0.1](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)
bundle: a directory of markdown concept docs with YAML frontmatter,
`index.md` listings (no frontmatter), and an update `log.md`.

| Path | Purpose |
|---|---|
| `index.md` | Home page (entry point): the interface model, the all-interface figure, the 15 side states, the 225-type matrix, and the section listing |
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

This is a working repo: push branches, open issues for open questions, and keep
the classification guidance (the [classify playbook](/playbooks/classify-a-data-product)
and the [knowledge concepts](/knowledge-concepts/)) consistent with the cells.

## License

The content of this catalog is licensed under
[Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/) —
see [`LICENSE`](LICENSE). You are free to share and adapt the material; you
must give appropriate credit, indicate any changes, and distribute your
contributions under the same license.
