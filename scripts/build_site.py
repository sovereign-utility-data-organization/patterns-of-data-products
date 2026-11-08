#!/usr/bin/env python3
"""Render the canonical OKF bundle into a static website (no build framework).

Why this shape
--------------
OKF v0.1 internal links are bundle-root-absolute and extension-less
(``](/concepts/data-product)`), which an OKF *renderer* resolves but a plain
static host (GitHub Pages, a GitHub repo view) does not: a browser resolves ``/foo``
against the site root (dropping the repo sub-path on a project page) and there is no
file named ``foo`` (it is ``foo.md``). So those links 404.

This script bridges the two WITHOUT touching the canonical bundle. It reads the
bundle and writes a **finished** static site to ``site/``:

  * every internal link is rewritten to a path that is **relative to the source
    page** and **resolves to a real file** (``data-product.html``, section
    ``index.html``, or an asset) -- so any static host serves it;
  * each markdown page is rendered to HTML with ``python-markdown`` (tables,
    fenced code, heading anchors, sane lists);
  * a shared layout is wrapped around every page: a collapsible sidebar page
    tree (derived from each section's ``index.md`` so it can never drift from
    the catalog, with the current page highlighted and its branch auto-opened)
    plus a global, dependency-free search bar; a JSON search index is emitted.

Only two things are needed at build time: ``python3`` and ``python-markdown``
(pip). There is no Docker, no Jekyll, no native extension. The canonical ``*.md``
and ``assets/`` are read but never modified; ``site/`` is the gitignored output.
"""
import json
import os
import re
import shutil
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
OUT = os.path.join(ROOT, "site")          # finished static site (gitignored)

ASSET_DIR = "assets"                       # copied verbatim
ROOT_PAGES = ["index.md", "log.md", "README.md"]
PAGE_DIRS = ["concepts", "data-product-types", "playbooks"]
ASSET_EXT = (".svg", ".png", ".jpg", ".jpeg", ".gif", ".webp", ".toml", ".yaml", ".yml")

SITE_TITLE = "Data Product Classification by Interface"
SITE_DESC = ("An Open Knowledge Format (OKF v0.1) catalog classifying data product "
             "types by their interface (IN and OUT integration patterns) — the "
             "interface is the shape of a product's type, not its identity.")
SOURCE_URL = "https://github.com/sovereign-utility-data-organization/patterns-of-data-products"

try:
    import markdown  # provided by `pip install markdown`
except ImportError:
    print("ERROR: 'markdown' is required. Install with: python3 -m pip install markdown",
          file=sys.stderr)
    sys.exit(1)

MD_EXTENSIONS = ["extra", "toc", "sane_lists"]

# --------------------------------------------------------------------------- #
# Link rewriting + frontmatter + text helpers
# --------------------------------------------------------------------------- #
LINK_RE = re.compile(r"(\]\(\s*)(/[^)\s]+?)(\s*\))")


def is_asset(t: str) -> bool:
    return t.lower().endswith(ASSET_EXT)


def resolve_target(t: str) -> str:
    """OKF internal target -> bundle-root-relative output file."""
    if is_asset(t):
        return t
    if t.endswith("/"):
        return t + "index.html"
    return t + ".html"


def rewrite_links(text: str, source_dir: str) -> str:
    start = source_dir or os.curdir

    def repl(m: re.Match) -> str:
        target = m.group(2).lstrip("/")           # drop the bundle-root slash
        site_file = resolve_target(target)        # bundle-root-relative output file
        link = os.path.relpath(site_file, start=start)
        return m.group(1) + link + m.group(3)

    return LINK_RE.sub(repl, text)


def split_frontmatter(text: str):
    """Return (fm: dict, body: str). Handles the flat scalar keys we care about
    (title, definition); list fields are ignored (not needed for rendering)."""
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---", 4)
    if end == -1:
        return {}, text
    fm = {}
    for line in text[4:end].splitlines():
        if line.startswith((" ", "-", "\t")) or not line.strip():
            continue
        if ":" in line:
            k, _, v = line.partition(":")
            fm[k.strip()] = v.strip().strip('"').strip("'")
    body = text[end + 4:]
    if body.startswith("\n"):
        body = body[1:]
    return fm, body


def pick_title(fm: dict, body: str, rel: str) -> str:
    if fm.get("title"):
        return fm["title"]
    m = re.search(r"^#\s+(.+?)\s*$", body, re.MULTILINE)
    if m:
        return m.group(1).strip()
    return os.path.splitext(os.path.basename(rel))[0].replace("-", " ").title()


def strip_markdown(text: str) -> str:
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end != -1:
            text = text[end + 4:]
    text = re.sub(r"```.*?```", " ", text, flags=re.DOTALL)
    text = re.sub(r"!\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"^#{1,6}\s+", "", text, flags=re.MULTILINE)
    text = re.sub(r"[*_`>]+", " ", text)
    text = re.sub(r"&[a-z]+;|&#\d+;", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def real_link_targets(markdown_text: str) -> list:
    """Markdown link targets, ignoring those inside code spans/fences (examples)."""
    t = re.sub(r"```.*?```", " ", markdown_text, flags=re.DOTALL)
    t = re.sub(r"`[^`]*`", " ", t)
    return re.findall(r"\]\(([^)\s]+?)\)", t)


# --------------------------------------------------------------------------- #
# Page collection
# --------------------------------------------------------------------------- #
def iter_pages():
    for name in ROOT_PAGES:
        if os.path.exists(os.path.join(ROOT, name)):
            yield name
    for d in PAGE_DIRS:
        base = os.path.join(ROOT, d)
        if not os.path.isdir(base):
            continue
        for dp, dns, fns in os.walk(base):
            dns[:] = [x for x in dns if x not in {".git", "__pycache__", "site", "site-src", ".github"}]
            for fn in fns:
                if fn.endswith(".md"):
                    yield os.path.normpath(os.path.relpath(os.path.join(dp, fn), ROOT))


# --------------------------------------------------------------------------- #
# Page tree (sidebar navigation)
# --------------------------------------------------------------------------- #
# Sections' index.md files are prose bullets: ``* [label](/target) - desc``.
# The page tree is derived from them, so it stays in sync with the catalog.
H2_RE = re.compile(r"^##\s+(.*?)\s*$")
BULLET_RE = re.compile(r"^\s*[*-]\s+\[([^\]]+)\]\((/[^)\s]+)\)")


def index_groups(dir_name: str) -> list:
    """Parse ``{dir}/index.md`` into ``[(heading: str|None, [(label, target)])]``."""
    path = os.path.join(ROOT, dir_name, "index.md")
    if not os.path.exists(path):
        return []
    groups = []
    heading, items = None, []
    for line in open(path, encoding="utf-8").read().splitlines():
        m = H2_RE.match(line)
        if m:
            if items:
                groups.append((heading, items))
            heading, items = m.group(1), []
            continue
        b = BULLET_RE.match(line)
        if b:
            items.append((b.group(1), b.group(2).lstrip("/")))
    if items:
        groups.append((heading, items))
    return groups


def section_h1(dir_name: str) -> str:
    """The page tree's top-level label for a section (its index.md H1)."""
    try:
        for line in open(os.path.join(ROOT, dir_name, "index.md"), encoding="utf-8"):
            m = re.match(r"^#\s+(.*?)\s*$", line)
            if m:
                return m.group(1)
    except OSError:
        pass
    return dir_name.replace("-", " ").title()


def render_sidebar(rel: str) -> str:
    """Collapse the whole catalog into a tree of nested <details> blocks.

    Sections come from the PAGE_DIRS index.md files; their group headings
    (e.g. the In-state rows of the 225-cell matrix) become nested collapsibles.
    The section/group containing the current page starts open, the others close.
    """
    page_dir = os.path.dirname(rel) or os.curdir
    current = os.path.splitext(rel)[0] + ".html"
    current_n = os.path.normpath(current)

    def site_file(target: str) -> str:
        return target + "index.html" if target.endswith("/") else target + ".html"

    def anchor(label: str, target: str) -> str:
        cur = ' class="side-current" aria-current="page"' \
            if os.path.normpath(site_file(target)) == current_n else ""
        return (f'<a{cur} href="{esc(os.path.relpath(site_file(target), start=page_dir))}">'
                f"{esc(label)}</a>")

    parts = ['<nav class="side-nav" aria-label="Catalog pages"><ul class="side-list">']
    parts.append(f'<li>{anchor("Home", "index")}</li>')

    for d in PAGE_DIRS:
        groups = index_groups(d)
        if not groups:
            continue
        inside = current_n.startswith(d + os.sep)
        # Small sections start open; the 225-cell matrix only when we're in it.
        open_attr = " open" if inside or d != "data-product-types" else ""
        parts.append(f'<li><details class="side-section"{open_attr}>')
        parts.append(f'<summary>{esc(section_h1(d))}</summary><ul class="side-list">')
        parts.append(anchor("Index", f"{d}/"))
        for heading, items in groups:
            if heading is None or len(items) <= 1:
                parts.extend(f'<li>{anchor(label, target)}</li>' for label, target in items)
                continue
            g_open = " open" if any(os.path.normpath(site_file(t)) == current_n
                                    for _, t in items) else ""
            parts.append(f'<li><details class="side-sub"{g_open}>')
            parts.append(f'<summary>{esc(heading)}</summary><ul class="side-list">')
            parts.extend(f'<li>{anchor(label, target)}</li>' for label, target in items)
            parts.append("</ul></details></li>")
        parts.append("</ul></details></li>")

    parts.append(f'<li>{anchor("Log", "log")}</li>')
    parts.append(f'<li>{anchor("README", "README")}</li>')
    parts.append("</ul></nav>")
    return "\n".join(parts)


# --------------------------------------------------------------------------- #
# HTML template (shared layout: sidebar page tree + global search bar)
# --------------------------------------------------------------------------- #
TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="stylesheet" href="{base}site.css">
<script>window.SITE_BASE = "{base}";</script>
<script src="{base}navigation.js" defer></script>
<script src="{base}search.js" defer></script>
</head>
<body>
<header class="site-header">
  <button class="nav-toggle" id="nav-toggle" aria-expanded="false" aria-controls="sidebar">
    <span aria-hidden="true">&#8801;</span><span class="nav-toggle-label">Pages</span>
  </button>
  <a class="brand" href="{base}index.html">{site_title}</a>
  <div class="search" id="search">
    <input id="search-input" type="search" placeholder="Search the catalog&hellip;"
           autocomplete="off" spellcheck="false" aria-label="Search the catalog">
    <ul id="search-results" class="search-results" hidden></ul>
  </div>
</header>
<div class="layout">
<aside class="sidebar" id="sidebar">
{sidebar}
</aside>
<main class="page">
{content}
</main>
</div>
<footer class="site-footer">
  <span class="muted">OKF v0.1 knowledge catalog</span>
  <a href="{base}README.html">README</a>
  <a href="{source_url}" target="_blank" rel="noopener">Source on GitHub</a>
</footer>
</body>
</html>
"""


def esc(s: str) -> str:
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
             .replace('"', "&quot;"))


def render_page(rel: str, text: str) -> str:
    source_dir = os.path.dirname(rel)
    depth = len(source_dir.split(os.sep)) if source_dir else 0
    base = "../" * depth

    fm, body = split_frontmatter(text)
    body = rewrite_links(body, source_dir)
    html_body = markdown.markdown(body, extensions=MD_EXTENSIONS)
    title = esc(pick_title(fm, body, rel))
    # The SKOS `definition` is the one-line summary of each concept; `description`
    # is kept as a legacy fallback only (OKF does not require it and this bundle
    # no longer uses the key).
    description = esc(fm.get("definition") or fm.get("description") or SITE_DESC)
    return TEMPLATE.format(
        base=base, title=title, description=description,
        site_title=esc(SITE_TITLE), source_url=SOURCE_URL, content=html_body,
        sidebar=render_sidebar(rel),
    )


# --------------------------------------------------------------------------- #
# Build
# --------------------------------------------------------------------------- #
def build():
    global OUT
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)

    # 1. Static assets.
    asset_src = os.path.join(ROOT, ASSET_DIR)
    if os.path.isdir(asset_src):
        shutil.copytree(asset_src, os.path.join(OUT, ASSET_DIR))
    # Root-level static files (the README's License section links to LICENSE).
    for static in ("LICENSE",):
        src = os.path.join(ROOT, static)
        if os.path.isfile(src):
            shutil.copyfile(src, os.path.join(OUT, static))

    # 2. Render every page.
    index = []
    pages = sorted(set(iter_pages()))
    for rel in pages:
        text = open(os.path.join(ROOT, rel), encoding="utf-8").read()
        html = render_page(rel, text)
        dest = os.path.join(OUT, os.path.splitext(rel)[0] + ".html")
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        open(dest, "w", encoding="utf-8").write(html)

        url = os.path.splitext(rel)[0] + ".html"
        fm, body = split_frontmatter(text)
        index.append({
            "title": pick_title(fm, body, rel),
            "url": url,
            "content": strip_markdown(text)[:1200],
        })

    # 3. Shared assets.
    open(os.path.join(OUT, "site.css"), "w", encoding="utf-8").write(write_css())
    open(os.path.join(OUT, "navigation.js"), "w", encoding="utf-8").write(write_navigation_js())
    open(os.path.join(OUT, "search.js"), "w", encoding="utf-8").write(write_search_js())
    with open(os.path.join(OUT, "search_index.json"), "w", encoding="utf-8") as fh:
        json.dump(index, fh, ensure_ascii=False, indent=0)

    validate_site()
    print(f"build_site: wrote {len(pages)} pages + {len(index)} search entries -> {OUT}")
    return 0


def write_css() -> str:
    return """
:root{--bg:#fff;--fg:#1b1f24;--muted:#57606a;--accent:#0969da;--border:#d0d7de;--code:#f6f8fa}
*{box-sizing:border-box}
body{margin:0;font:16px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif;color:var(--fg);background:var(--bg)}
a{color:var(--accent);text-decoration:none}a:hover{text-decoration:underline}
.site-header{position:sticky;top:0;z-index:10;display:flex;align-items:center;gap:16px;flex-wrap:wrap;padding:10px 20px;background:#fff;border-bottom:1px solid var(--border)}
.brand{font-weight:600;color:var(--fg);font-size:15px;white-space:nowrap}
.nav-toggle{display:none;margin-left:-4px;padding:5px 10px;font-size:14px;border:1px solid var(--border);border-radius:6px;background:#fff;color:var(--fg);cursor:pointer;white-space:nowrap}
.search{position:relative;display:flex}
.search input{width:min(340px,60vw);padding:6px 10px;border:1px solid var(--border);border-radius:6px;font-size:14px;background:#fff}
.search-results{position:absolute;top:100%;left:0;right:0;margin:4px 0 0;padding:4px;list-style:none;background:#fff;border:1px solid var(--border);border-radius:8px;box-shadow:0 8px 24px rgba(140,149,159,.25);max-height:60vh;overflow:auto;z-index:20}
.search-results li a{display:block;padding:8px 10px;border-radius:6px;color:var(--fg);text-decoration:none}
.search-results li a:hover{background:#f6f8fa}
.search-results li a strong{font-weight:600}
.search-results li a span{color:var(--muted);font-size:13px}
.search-results li.none{color:var(--muted);padding:8px 10px}
.layout{display:flex;align-items:flex-start;max-width:1320px;margin:0 auto}
.sidebar{flex:0 0 290px;width:290px;position:sticky;top:56px;max-height:calc(100vh - 70px);overflow-y:auto;padding:16px 14px 60px 18px;font-size:14px;border-right:1px solid var(--border)}
.sidebar ul{list-style:none;margin:0;padding:0}
.sidebar ul ul{margin:2px 0 8px 10px;padding-left:8px;border-left:1px solid var(--border)}
.sidebar a{display:block;padding:4px 8px;border-radius:6px;color:var(--muted);text-decoration:none}
.sidebar a:hover{background:#f1f3f5;color:var(--fg);text-decoration:none}
.sidebar a.side-current{background:#ddf4ff;color:var(--accent);font-weight:600}
.sidebar summary{list-style:none;cursor:pointer;font-weight:600;display:flex;align-items:center;gap:8px;padding:6px 8px;border-radius:6px;margin:2px 0}
.sidebar summary:hover{background:#f1f3f5}
.sidebar summary::-webkit-details-marker{display:none}
.sidebar summary::before{content:"\\25B8";font-size:9px;color:var(--muted);transform-origin:50% 50%}
.sidebar details[open]>summary::before{transform:rotate(90deg)}
.page{flex:1 1 auto;min-width:0;max-width:1040px;padding:26px 32px 60px}
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
@media (max-width:960px){
.nav-toggle{display:inline-block}
.layout{display:block}
.sidebar{position:fixed;top:0;left:0;bottom:0;width:min(330px,86vw);max-height:none;z-index:60;background:#fff;transform:translateX(-102%);transition:transform .16s ease;padding:18px 12px 60px;box-shadow:8px 0 24px rgba(140,149,159,.25)}
body.sidebar-open .sidebar{transform:translateX(0)}
body.sidebar-open::after{content:"";position:fixed;inset:0;z-index:55;background:rgba(27,31,36,.35)}
.page{padding:22px 16px 60px}
}
@media (max-width:640px){.search{flex:1}.search input{width:100%}}
"""


def write_navigation_js() -> str:
    return """(function () {
  var body = document.body;
  var toggle = document.getElementById("nav-toggle");

  function setOpen(open) {
    body.classList.toggle("sidebar-open", !!open);
    if (toggle) toggle.setAttribute("aria-expanded", open ? "true" : "false");
  }
  if (toggle) {
    toggle.addEventListener("click", function () {
      setOpen(!body.classList.contains("sidebar-open"));
    });
  }
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") setOpen(false);
  });
  // On small screens, choosing a page closes the sliding panel (the navigation
  // reloads the page, which restores the default closed state).
  document.querySelectorAll(".sidebar a").forEach(function (a) {
    a.addEventListener("click", function () {
      if (window.matchMedia("(max-width:960px)").matches) setOpen(false);
    });
  });
})();
"""


def write_search_js() -> str:
    return """(function () {
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


def validate_site() -> None:
    """Every href/src in the finished site must resolve to a real file."""
    errors = []
    for dp, dns, fns in os.walk(OUT):
        dns[:] = [d for d in dns if d not in {".git", "__pycache__", ".github"}]
        for fn in fns:
            if not fn.endswith(".html"):
                continue
            p = os.path.join(dp, fn)
            base = dp
            refs = re.findall(r'(?:href|src)="([^"]+)"', open(p, encoding="utf-8").read())
            for ref in refs:
                if ref.startswith(("http://", "https://", "mailto:", "#", "data:", "javascript:")):
                    continue
                if not os.path.exists(os.path.normpath(os.path.join(base, ref))):
                    errors.append(f"{os.path.relpath(p, OUT)} -> {ref}")
    # search index sanity
    data = json.load(open(os.path.join(OUT, "search_index.json"), encoding="utf-8"))
    if not data:
        errors.append("search index is empty")
    for e in data:
        if not os.path.exists(os.path.join(OUT, e["url"])):
            errors.append(f"search url missing: {e['url']}")
    if errors:
        for e in errors:
            print("VALIDATION ERROR:", e, file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    sys.exit(build())
