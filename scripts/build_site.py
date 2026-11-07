#!/usr/bin/env python3
"""Render the canonical OKF bundle into a Jekyll site for GitHub Pages.

The canonical knowledge catalog links with OKF v0.1 internal links --
bundle-root-absolute, extension-less:

    ](/knowledge-concepts/data-product)     a concept doc      ->  .../data-product.md
    ](/data-product-types/)                 a section index    ->  .../index.md
    ](/assets/cells/1022.svg)               an asset           ->  .../1022.svg

That convention is correct for the OKF renderer and is what the audit enforces.
GitHub, however, is not an OKF renderer: a browser resolves ``/foo`` against the
*site* root (which drops the repo sub-path on a project page) and there is no
file named ``foo`` (it is ``foo.md``). So the links 404.

This script bridges the two WITHOUT touching the canonical bundle. It reads the
bundle and emits a self-contained Jekyll project in ``site-src/``:

  * every internal link is rewritten to a path that is **relative to the source
    page** and **resolved to a real file** (``...data-product.html``,
    ``...index.html``, ``...1022.svg``) so a plain static host serves it;
  * a minimal Jekyll scaffold is generated: ``_config.yml``, a ``default``
    layout with a global search bar, and a small stylesheet;
  * a client-side, dependency-free search script and a JSON search index of every
    page are emitted.

Only the Python standard library is used. The canonical ``*.md`` files and
``assets/`` are read but never modified.
"""
import json
import os
import re
import shutil
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
OUT = os.path.join(ROOT, "site-src")

# Directories/files that are NOT part of the published site.
EXCLUDE_DIR_NAMES = {".git", "scripts", ".github", "__pycache__", "site-src", "site"}

# Root-level pages to publish.
ROOT_PAGES = ["index.md", "log.md", "README.md"]

# Section directories whose markdown pages are published.
PAGE_DIRS = ["knowledge-concepts", "data-product-types", "playbooks"]

# Static asset tree copied verbatim (SVGs etc.).
ASSET_DIR = "assets"

# File extensions that are static assets (served as-is) rather than markdown.
ASSET_EXT = (".svg", ".png", ".jpg", ".jpeg", ".gif", ".webp", ".toml", ".yaml", ".yml")

SITE_TITLE = "Data Product Classification by Interface"
SITE_DESC = (
    "An Open Knowledge Format (OKF v0.1) catalog classifying data products by "
    "the interface they expose to consumers."
)
SOURCE_URL = "https://github.com/sovereign-utility-data-organization/patterns-of-data-products"

# --------------------------------------------------------------------------- #
# Link rewriting
# --------------------------------------------------------------------------- #
LINK_RE = re.compile(r"(\]\(\s*)(/[^)\s]+?)(\s*\))")
FM_TITLE_RE = re.compile(r"^title:\s*(.+?)\s*$", re.MULTILINE)


def is_asset(target: str) -> bool:
    return target.lower().endswith(ASSET_EXT)


def resolve_target(target: str) -> str:
    """Map an OKF internal target to the file it resolves to at the site root."""
    if is_asset(target):
        return target
    if target.endswith("/"):
        return target + "index.html"          # section index
    return target + ".html"                    # concept doc: /x/y -> x/y.html


def rewrite_links(text: str, source_dir: str) -> str:
    """Rewrite OKF ``/...`` internal links to relative, resolved paths.

    ``source_dir`` is the directory of the page doing the linking, as a
    bundle-root-relative path ('' for the root).
    start = source_dir or curdir keeps os.path.relpath lexical and cwd-independent.
    """
    start = source_dir or os.curdir

    def repl(match: re.Match) -> str:
        target = match.group(2).lstrip("/")                 # OKF targets are bundle-root-absolute
        site_file = resolve_target(target)                  # bundle-root-relative output file
        link = os.path.relpath(site_file, start=start)      # relative to this page's dir
        return match.group(1) + link + match.group(3)

    return LINK_RE.sub(repl, text)


def inject_frontmatter(text: str, asset_root: str) -> str:
    """Ensure the page uses the default layout and knows its root-relative base.

    Adds ``layout: default`` and ``asset_root: <root>`` to the frontmatter (or
    creates a frontmatter block). Existing frontmatter keys are left untouched.
    """
    asset_value = json.dumps(asset_root)  # always a quoted YAML double-quoted string

    def block(*extra: str) -> str:
        lines = ["layout: default", "asset_root: " + asset_value]
        lines.extend(extra)
        return "---\n" + "\n".join(lines) + "\n---\n"

    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end == -1:
            # Malformed frontmatter; prepend defensively.
            return block() + "\n" + text
        opening = text[:4]                                  # '---\n'
        existing = text[4:end]                              # the current FM body
        if re.search(r"^layout:\s*", existing, re.MULTILINE):
            layout_line = ""
        else:
            layout_line = "layout: default\n"
        if re.search(r"^asset_root:\s*", existing, re.MULTILINE):
            root_line = ""
        else:
            root_line = "asset_root: " + asset_value + "\n"
        return opening + layout_line + root_line + existing + text[end:]
    # No frontmatter: create one.
    return block() + "\n" + text


# --------------------------------------------------------------------------- #
# Search index helpers
# --------------------------------------------------------------------------- #
def extract_title(text: str, fallback: str) -> str:
    m = FM_TITLE_RE.search(text)
    if m:
        title = m.group(1).strip().strip("'\"")
        if title:
            return title
    h1 = re.search(r"^#\s+(.+?)\s*$", text, re.MULTILINE)
    if h1:
        return h1.group(1).strip()
    return fallback


def strip_markdown(text: str) -> str:
    """Reduce a page to plain-ish text for the search snippet."""
    body = text
    if body.startswith("---\n"):
        end = body.find("\n---", 4)
        if end != -1:
            body = body[end + 4:]
    body = re.sub(r"```.*?```", " ", body, flags=re.DOTALL)      # code fences
    body = re.sub(r"!\[([^\]]*)\]\([^)]*\)", r"\1", body)        # images -> alt
    body = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", body)          # links -> text
    body = re.sub(r"^#{1,6}\s+", "", body, flags=re.MULTILINE)    # heading marks
    body = re.sub(r"[*_`>]+", " ", body)
    body = re.sub(r"&[a-z]+;|&#\d+;", " ", body)                   # entities
    body = re.sub(r"\s+", " ", body)
    return body.strip()


# --------------------------------------------------------------------------- #
# Page collection / build
# --------------------------------------------------------------------------- #
def iter_pages():
    """Yield bundle-root-relative paths of every markdown page to publish."""
    for name in ROOT_PAGES:
        if os.path.exists(os.path.join(ROOT, name)):
            yield name
    for d in PAGE_DIRS:
        base = os.path.join(ROOT, d)
        if not os.path.isdir(base):
            continue
        for dp, dns, fns in os.walk(base):
            dns[:] = [x for x in dns if x not in EXCLUDE_DIR_NAMES]
            for fn in fns:
                if fn.endswith(".md"):
                    rel = os.path.relpath(os.path.join(dp, fn), ROOT)
                    yield os.path.normpath(rel)


def build():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)

    # 1. Copy static assets verbatim.
    asset_src = os.path.join(ROOT, ASSET_DIR)
    if os.path.isdir(asset_src):
        shutil.copytree(asset_src, os.path.join(OUT, ASSET_DIR))

    index = []
    pages = sorted(set(iter_pages()))
    for rel in pages:
        src = os.path.join(ROOT, rel)
        text = open(src, encoding="utf-8").read()
        source_dir = os.path.dirname(rel)
        depth = len(source_dir.split(os.sep)) if source_dir else 0
        asset_root = "../" * depth

        out_text = rewrite_links(text, source_dir)
        out_text = inject_frontmatter(out_text, asset_root)

        dest = os.path.join(OUT, rel)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        with open(dest, "w", encoding="utf-8") as fh:
            fh.write(out_text)

        url = os.path.splitext(rel)[0] + ".html"
        index.append({
            "title": extract_title(text, os.path.splitext(os.path.basename(rel))[0].replace("-", " ").title()),
            "url": url,
            "content": strip_markdown(text)[:1200],
        })

    # 2. Emit the Jekyll scaffold + search machinery.
    write_config()
    write_layout()
    write_css()
    write_search_js()
    with open(os.path.join(OUT, "search_index.json"), "w", encoding="utf-8") as fh:
        json.dump(index, fh, ensure_ascii=False, indent=0)

    validate(OUT, index)
    print(f"build_site: wrote {len(pages)} pages + {len(index)} search entries to {OUT}")
    return 0


# --------------------------------------------------------------------------- #
# Generated site files (no Liquid beyond variable output; no external deps)
# --------------------------------------------------------------------------- #
def write_config():
    with open(os.path.join(OUT, "_config.yml"), "w", encoding="utf-8") as fh:
        fh.write(
            "title: " + json.dumps(SITE_TITLE) + "\n"
            "description: " + json.dumps(SITE_DESC) + "\n"
            "markdown: kramdown\n"
            "kramdown:\n"
            "  input: GFM\n"
            "  auto_ids: true\n"
            "syntax_highlighter: null\n"
        )


def write_layout():
    layout = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{{ page.title | default: site.title | escape }}</title>
  <meta name="description" content="{{ page.description | default: site.description | escape }}">
  <link rel="stylesheet" href="{{ page.asset_root }}site.css">
  <script>window.SITE_BASE = "{{ page.asset_root }}";</script>
  <script src="{{ page.asset_root }}search.js" defer></script>
</head>
<body>
  <header class="site-header">
    <a class="brand" href="{{ page.asset_root }}index.html">{{ site.title }}</a>
    <div class="search" id="search">
      <input id="search-input" type="search" placeholder="Search the catalog&hellip;"
             autocomplete="off" spellcheck="false" aria-label="Search the catalog">
      <ul id="search-results" class="search-results" hidden></ul>
    </div>
    <nav class="site-nav">
      <a href="{{ page.asset_root }}knowledge-concepts/index.html">Concepts</a>
      <a href="{{ page.asset_root }}data-product-types/index.html">Types</a>
      <a href="{{ page.asset_root }}playbooks/index.html">Playbooks</a>
      <a href="{{ page.asset_root }}log.html">Log</a>
    </nav>
  </header>
  <main class="page">
{{ content }}
  </main>
  <footer class="site-footer">
    <span class="muted">OKF v0.1 knowledge catalog</span>
    <a href="{{ page.asset_root }}README.html">README</a>
    <a href="SOURCE_URL" target="_blank" rel="noopener">Source on GitHub</a>
  </footer>
</body>
</html>
""".replace("SOURCE_URL", SOURCE_URL)
    os.makedirs(os.path.join(OUT, "_layouts"), exist_ok=True)
    with open(os.path.join(OUT, "_layouts", "default.html"), "w", encoding="utf-8") as fh:
        fh.write(layout)


def write_css():
    css = """
:root{--bg:#fff;--fg:#1b1f24;--muted:#57606a;--accent:#0969da;--border:#d0d7de;--code:#f6f8fa}
*{box-sizing:border-box}
body{margin:0;font:16px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif;color:var(--fg);background:var(--bg)}
a{color:var(--accent);text-decoration:none}a:hover{text-decoration:underline}
.site-header{position:sticky;top:0;z-index:10;display:flex;align-items:center;gap:16px;flex-wrap:wrap;padding:10px 20px;background:#fff;border-bottom:1px solid var(--border)}
.brand{font-weight:600;color:var(--fg);font-size:15px;white-space:nowrap}
.site-nav{margin-left:auto;display:flex;gap:14px;font-size:14px}
.site-nav a{color:var(--muted)}.site-nav a:hover{color:var(--accent)}
.search{position:relative;display:flex}
.search input{width:min(340px,60vw);padding:6px 10px;border:1px solid var(--border);border-radius:6px;font-size:14px;background:#fff}
.search-results{position:absolute;top:100%;left:0;right:0;margin:4px 0 0;padding:4px;list-style:none;background:#fff;border:1px solid var(--border);border-radius:8px;box-shadow:0 8px 24px rgba(140,149,159,.25);max-height:60vh;overflow:auto;z-index:20}
.search-results li a{display:block;padding:8px 10px;border-radius:6px;color:var(--fg);text-decoration:none}
.search-results li a:hover{background:#f6f8fa}
.search-results li a strong{font-weight:600}
.search-results li a span{color:var(--muted);font-size:13px}
.search-results li.none{color:var(--muted);padding:8px 10px}
.page{max-width:920px;margin:0 auto;padding:26px 20px 60px}
.page h1{font-size:28px;line-height:1.25;margin:.2em 0 .6em}
.page h2{font-size:22px;margin:1.4em 0 .5em;padding-bottom:.2em;border-bottom:1px solid var(--border)}
.page h3{font-size:18px;margin:1.2em 0 .4em}
.page p,.page li{max-width:72ch}
table{border-collapse:collapse;margin:1em 0;display:block;overflow-x:auto;max-width:100%}
th,td{border:1px solid var(--border);padding:6px 12px;text-align:left}
th{background:var(--code)}
code{background:var(--code);padding:.15em .4em;border-radius:4px;font-family:ui-monospace,SFMono-Regular,"SF Mono",Menlo,Consolas,monospace;font-size:85%}
pre{background:var(--code);padding:14px;border-radius:8px;overflow:auto}pre code{background:none;padding:0}
blockquote{margin:1em 0;padding:.2em 1em;color:var(--muted);border-left:3px solid var(--border)}
img{max-width:100%;height:auto}
.site-footer{max-width:920px;margin:0 auto;padding:20px;border-top:1px solid var(--border);color:var(--muted);font-size:13px;display:flex;gap:16px;flex-wrap:wrap;align-items:center}
.site-footer a{color:var(--muted)}
.muted{color:var(--muted)}
@media (max-width:640px){.site-nav{order:3;width:100%}.search{flex:1}.search input{width:100%}}
"""
    with open(os.path.join(OUT, "site.css"), "w", encoding="utf-8") as fh:
        fh.write(css)


def write_search_js():
    js = """(function () {
  var base = window.SITE_BASE || "";
  var input = document.getElementById("search-input");
  var results = document.getElementById("search-results");
  if (!input || !results) return;
  var index = null;

  function load() {
    if (index) return Promise.resolve(index);
    return fetch(base + "search_index.json", { cache: "force-cache" })
      .then(function (r) { return r.json(); })
      .then(function (d) { index = d || []; return index; })
      .catch(function () { index = []; return index; });
  }
  function esc(s) {
    return String(s).replace(/[&<>"]/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c];
    });
  }
  function hide() { results.hidden = true; results.innerHTML = ""; }

  function run(raw) {
    var q = raw.trim().toLowerCase();
    if (q.length < 2) { hide(); return; }
    load().then(function (docs) {
      var hits = docs.map(function (d) {
        var t = (d.title || "").toLowerCase();
        var c = (d.content || "").toLowerCase();
        var score = 0;
        if (t.indexOf(q) === 0) score += 100; else if (t.indexOf(q) !== -1) score += 50;
        if (c.indexOf(q) !== -1) score += 10;
        return score ? { s: score, d: d } : null;
      }).filter(Boolean).sort(function (a, b) { return b.s - a.s; }).slice(0, 15);

      if (!hits.length) {
        results.innerHTML = '<li class="none">No matches</li>';
        results.hidden = false;
        return;
      }
      results.innerHTML = hits.map(function (h) {
        var d = h.d;
        var ci = (d.content || "").toLowerCase().indexOf(q);
        var span = "";
        if (ci >= 0) {
          var s = d.content.slice(Math.max(0, ci - 40), ci + 80);
          span = "<span>&hellip;" + esc(s) + "</span>";
        }
        return '<li><a href="' + base + d.url + '"><strong>' + esc(d.title) + "</strong>" + span + "</a></li>";
      }).join("");
      results.hidden = false;
    });
  }

  var timer;
  input.addEventListener("input", function () {
    clearTimeout(timer);
    var v = input.value;
    timer = setTimeout(function () { run(v); }, 120);
  });
  input.addEventListener("focus", function () { if (input.value.trim().length >= 2) run(input.value); });
  input.addEventListener("keydown", function (e) {
    if (e.key === "Enter") {
      var a = results.querySelector("a");
      if (a) window.location.href = a.href;
    } else if (e.key === "Escape") { hide(); input.blur(); }
  });
  document.addEventListener("click", function (e) {
    if (!results.contains(e.target) && e.target !== input) hide();
  });
})();
"""
    with open(os.path.join(OUT, "search.js"), "w", encoding="utf-8") as fh:
        fh.write(js)


# --------------------------------------------------------------------------- #
# Local validation: every link the pages now contain must resolve inside OUT
# --------------------------------------------------------------------------- #
def _exists_in_site(path: str) -> bool:
    """A target is valid in the *generated* site if it resolves to a file that
    will exist after Jekyll renders (``.md`` -> ``.html``) or to a static asset.
    """
    if os.path.exists(path) or os.path.isdir(path):
        return True
    if os.path.isdir(os.path.dirname(path)) and os.path.basename(path) in ("index.html", "index"):
        d = os.path.dirname(path)
        return os.path.exists(os.path.join(d, "index.md")) or os.path.exists(os.path.join(d, "index.html"))
    if path.endswith(".html"):
        return os.path.exists(path[: -len(".html")] + ".md")
    return False


def _real_link_targets(text: str) -> list:
    """Extract markdown link targets, ignoring those inside code spans/fences
    (prose examples like ``](assets/cells/in-….svg)`` are not real links)."""
    text = re.sub(r"```.*?```", " ", text, flags=re.DOTALL)   # fenced code
    text = re.sub(r"`[^`]*`", " ", text)                       # inline code
    return re.findall(r"\]\(([^)\s]+?)\)", text)


def validate(out_root: str, index: list) -> None:
    errors = []
    for dp, dns, fns in os.walk(out_root):
        dns[:] = [d for d in dns if d not in EXCLUDE_DIR_NAMES and not d.startswith("_layouts")]
        for fn in fns:
            if not fn.endswith(".md"):
                continue
            p = os.path.join(dp, fn)
            base = os.path.dirname(p)
            for target in _real_link_targets(open(p, encoding="utf-8").read()):
                if target.startswith(("http://", "https://", "mailto:", "#")):
                    continue
                resolved = os.path.normpath(os.path.join(base, target))
                if not _exists_in_site(resolved):
                    errors.append(f"{os.path.relpath(p, out_root)} -> {target} is broken")
    if errors:
        for e in errors:
            print("VALIDATION ERROR:", e, file=sys.stderr)
        sys.exit(1)
    # sanity: search index non-empty and its urls resolve to generated pages
    if not index:
        print("VALIDATION ERROR: search index is empty", file=sys.stderr)
        sys.exit(1)
    for entry in index:
        if not _exists_in_site(os.path.join(out_root, entry["url"])):
            print(f"VALIDATION ERROR: search url missing: {entry['url']}", file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    sys.exit(build())
