"""
serp_intel.py
Competitive SERP & content-gap analyzer, aligned with the v2.0
Google-grounded playbook.

WHAT IT DOES
  - Pulls SERP top-N for up to 10 keywords (via a SERP API, NOT by scraping Google).
  - Fetches + extracts main content from each ranking page (robots-aware, rate-limited).
  - Profiles each page on the dimensions that actually move rankings:
      * page type / intent signals
      * content depth & heading structure (query fan-out: the sub-questions it answers)
      * structured-data types present (via extruct)
  - Builds a CONTENT-GAP report per keyword: what the leaders cover, what's thin
    or commodity, and where your first-hand differentiators can win.

WHAT IT DELIBERATELY DOES NOT DO
  - Score "exact keyword-match density" to out-stuff competitors. Current Google
    guidance is explicit: AI understands synonyms; you don't write for the machine.
    This tool measures SEMANTIC / INTENT coverage instead.

SETUP
  Homebrew / system Python is PEP-668 "externally managed" — install into a venv,
  and use `python3 -m pip` (bare `pip` is often absent):
      python3 -m venv .venv && source .venv/bin/activate
      python3 -m pip install -r requirements.txt
  A SERP API key is REQUIRED (free tier at https://serpapi.com). Without it the
  tool cannot fetch SERPs and exits non-zero — it will NOT emit an empty report:
      export SERPAPI_KEY="your_key"

RUN
  python3 serp_intel.py "your high-intent keyword" "your second keyword"
  python3 serp_intel.py --file keywords.txt --top 3 --out report.md
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import urllib.robotparser as robotparser
from collections import Counter
from dataclasses import dataclass, field, asdict
from urllib.parse import urlparse

import httpx
import trafilatura
import extruct
from bs4 import BeautifulSoup

# ----------------------------------------------------------------------------- 
# Config
# -----------------------------------------------------------------------------

SERPAPI_KEY = os.environ.get("SERPAPI_KEY", "")
USER_AGENT = "SEOResearchBot/1.0 (+set-your-contact-url; competitive research)"
REQUEST_TIMEOUT = 20.0
POLITE_DELAY_SEC = 1.5          # between page fetches, per host courtesy
MAX_KEYWORDS = 10

# Customize: your product's hard-to-copy differentiators. Map each label to the
# terms a competitor would use if they covered it; the report flags whether
# leaders mention these — when none do, that absence is your whitespace wedge.
YOUR_DIFFERENTIATORS = {
    "a capability only you offer": ["replace-with-your", "unique-capability", "terms"],
    "a proprietary dataset or first-hand source": ["benchmark", "dataset", "original data", "proprietary"],
    "an integration competitors lack": ["portable", "export", "integration", "no lock-in"],
}

# Cheap intent classifier from page signals (extend as you learn your niche).
INTENT_SIGNALS = {
    "transactional": ["pricing", "buy", "start free", "sign up", "get started", "try", "book a demo", "free trial"],
    "comparison":    ["vs", "versus", "alternative", "comparison", "compare", "best ", "top "],
    "informational": ["what is", "how to", "guide", "tutorial", "explained", "introduction to"],
}

# Optional embedding model (loaded lazily; tool still runs without it).
_EMBEDDER = None


def _get_embedder():
    global _EMBEDDER
    if _EMBEDDER is not None:
        return _EMBEDDER
    try:
        from sentence_transformers import SentenceTransformer
        _EMBEDDER = SentenceTransformer("all-MiniLM-L6-v2")
    except Exception:
        _EMBEDDER = False  # signal "unavailable"
    return _EMBEDDER


# ----------------------------------------------------------------------------- 
# Data models
# -----------------------------------------------------------------------------

@dataclass
class PageProfile:
    url: str
    rank: int
    fetched: bool = False
    title: str = ""
    meta_description: str = ""
    h1: str = ""
    headings: list[str] = field(default_factory=list)      # H2/H3 — the page's "answer outline"
    word_count: int = 0
    schema_types: list[str] = field(default_factory=list)
    page_type: str = "unknown"
    top_phrases: list[str] = field(default_factory=list)   # candidate sub-topics / fan-out
    differentiators_mentioned: list[str] = field(default_factory=list)
    semantic_coverage: float | None = None                 # vs the keyword, 0..1, if embeddings available
    error: str = ""


@dataclass
class KeywordReport:
    keyword: str
    pages: list[PageProfile] = field(default_factory=list)
    dominant_intent: str = "unknown"
    common_subtopics: list[str] = field(default_factory=list)   # what ALL leaders cover -> table stakes
    gap_subtopics: list[str] = field(default_factory=list)      # covered by some, not all -> easy wins
    differentiator_whitespace: list[str] = field(default_factory=list)  # what NO leader covers -> the wedge


# ----------------------------------------------------------------------------- 
# Polite fetching
# -----------------------------------------------------------------------------

_robots_cache: dict[str, robotparser.RobotFileParser] = {}


def allowed_by_robots(url: str) -> bool:
    parsed = urlparse(url)
    base = f"{parsed.scheme}://{parsed.netloc}"
    rp = _robots_cache.get(base)
    if rp is None:
        rp = robotparser.RobotFileParser()
        rp.set_url(f"{base}/robots.txt")
        try:
            rp.read()
        except Exception:
            rp = None  # if robots is unreachable, default to allowed but cautious
        _robots_cache[base] = rp
    return True if rp is None else rp.can_fetch(USER_AGENT, url)


def fetch_html(url: str) -> str | None:
    if not allowed_by_robots(url):
        return None
    try:
        r = httpx.get(
            url,
            headers={"User-Agent": USER_AGENT, "Accept-Language": "en-US,en;q=0.9"},
            timeout=REQUEST_TIMEOUT,
            follow_redirects=True,
        )
        if r.status_code == 200 and "text/html" in r.headers.get("content-type", ""):
            return r.text
    except Exception:
        return None
    return None


# ----------------------------------------------------------------------------- 
# Page analysis
# -----------------------------------------------------------------------------

STOPWORDS = set("""a an and are as at be by for from has have in is it its of on or that the
this to was were will with your you we our they their what how why when can use using into out
about more most page site web are not but if then than so do does done get just like make made
one two three top best vs versus tool tools data sql""".split())


def extract_candidate_phrases(text: str, k: int = 12) -> list[str]:
    """Lightweight fan-out extraction: frequent 2-3 word phrases minus boilerplate.
    Not exact-match scoring — used to see what *sub-topics* a page covers."""
    words = re.findall(r"[a-zA-Z][a-zA-Z\-']+", text.lower())
    grams: Counter = Counter()
    for n in (2, 3):
        for i in range(len(words) - n + 1):
            gram = words[i:i + n]
            if gram[0] in STOPWORDS or gram[-1] in STOPWORDS:
                continue
            if any(w in STOPWORDS for w in gram[1:-1]) and n == 3:
                continue
            grams[" ".join(gram)] += 1
    return [p for p, c in grams.most_common(k) if c > 1]


def classify_page_type(text: str, title: str) -> str:
    blob = (title + " " + text[:2000]).lower()
    scores = {k: sum(blob.count(sig) for sig in sigs) for k, sigs in INTENT_SIGNALS.items()}
    best = max(scores, key=scores.get)
    return best if scores[best] > 0 else "unknown"


def find_differentiators(text: str) -> list[str]:
    blob = text.lower()
    found = []
    for label, terms in YOUR_DIFFERENTIATORS.items():
        if any(t in blob for t in terms):
            found.append(label)
    return found


def schema_types_from_html(html: str, url: str) -> list[str]:
    try:
        data = extruct.extract(html, base_url=url, syntaxes=["json-ld", "microdata"])
    except Exception:
        return []
    types: set[str] = set()
    for item in data.get("json-ld", []):
        t = item.get("@type")
        if isinstance(t, list):
            types.update(t)
        elif isinstance(t, str):
            types.add(t)
        for g in item.get("@graph", []) if isinstance(item, dict) else []:
            gt = g.get("@type")
            if isinstance(gt, str):
                types.add(gt)
    for item in data.get("microdata", []):
        t = item.get("type")
        if isinstance(t, str):
            types.add(t.rsplit("/", 1)[-1])
    return sorted(types)


def semantic_coverage(keyword: str, text: str) -> float | None:
    embedder = _get_embedder()
    if not embedder:
        return None
    from sentence_transformers import util
    # Compare keyword intent against the page's strongest passages, not exact strings.
    passages = [p.strip() for p in re.split(r"\n+", text) if len(p.strip()) > 60][:30]
    if not passages:
        return 0.0
    kw_emb = embedder.encode(keyword, convert_to_tensor=True)
    p_emb = embedder.encode(passages, convert_to_tensor=True)
    sims = util.cos_sim(kw_emb, p_emb)[0]
    return round(float(sims.max()), 3)


def profile_page(url: str, rank: int, keyword: str) -> PageProfile:
    prof = PageProfile(url=url, rank=rank)
    html = fetch_html(url)
    if not html:
        prof.error = "blocked by robots, non-200, or fetch failed"
        return prof

    soup = BeautifulSoup(html, "lxml")
    prof.title = (soup.title.string or "").strip() if soup.title else ""
    md = soup.find("meta", attrs={"name": "description"})
    prof.meta_description = (md.get("content", "").strip() if md else "")
    h1 = soup.find("h1")
    prof.h1 = h1.get_text(strip=True) if h1 else ""
    prof.headings = [h.get_text(strip=True) for h in soup.find_all(["h2", "h3"])][:25]
    prof.schema_types = schema_types_from_html(html, url)

    text = trafilatura.extract(html) or soup.get_text(" ", strip=True)
    prof.word_count = len(text.split())
    prof.page_type = classify_page_type(text, prof.title)
    prof.top_phrases = extract_candidate_phrases(text)
    prof.differentiators_mentioned = find_differentiators(text)
    prof.semantic_coverage = semantic_coverage(keyword, text)
    prof.fetched = True
    return prof


# ----------------------------------------------------------------------------- 
# SERP source
# -----------------------------------------------------------------------------

def fetch_serp(keyword: str, top: int) -> list[str]:
    """Return top-N organic URLs via SerpAPI. Swap this one function for
    DataForSEO/Serpstack if you prefer — keep the rest of the tool unchanged."""
    if not SERPAPI_KEY:
        print(f"  [!] SERPAPI_KEY not set — skipping live SERP for '{keyword}'.", file=sys.stderr)
        return []
    try:
        from serpapi import GoogleSearch
        search = GoogleSearch({
            "q": keyword,
            "engine": "google",
            "num": max(top + 2, 10),
            "hl": "en",
            "gl": "us",
            "api_key": SERPAPI_KEY,
        })
        results = search.get_dict()
        urls = [r["link"] for r in results.get("organic_results", []) if "link" in r]
        return urls[:top]
    except Exception as e:
        print(f"  [!] SERP fetch failed for '{keyword}': {e}", file=sys.stderr)
        return []


# ----------------------------------------------------------------------------- 
# Keyword-level synthesis (the part that matters)
# -----------------------------------------------------------------------------

def analyze_keyword(keyword: str, top: int) -> KeywordReport:
    report = KeywordReport(keyword=keyword)
    urls = fetch_serp(keyword, top)
    for i, url in enumerate(urls, start=1):
        report.pages.append(profile_page(url, i, keyword))
        time.sleep(POLITE_DELAY_SEC)

    fetched = [p for p in report.pages if p.fetched]
    if not fetched:
        return report

    # Dominant intent across the leaders -> tells you the page TYPE to build.
    report.dominant_intent = Counter(p.page_type for p in fetched).most_common(1)[0][0]

    # Subtopic coverage = query fan-out. What everyone covers is table stakes;
    # what only some cover is a quick win; what no one covers is whitespace.
    phrase_doc_freq: Counter = Counter()
    for p in fetched:
        for phrase in set(p.top_phrases):
            phrase_doc_freq[phrase] += 1
    n = len(fetched)
    report.common_subtopics = [ph for ph, c in phrase_doc_freq.items() if c == n][:12]
    report.gap_subtopics = [ph for ph, c in phrase_doc_freq.items() if 1 <= c < n][:12]

    # The wedge: which of your differentiators NO leader mentions.
    mentioned = set()
    for p in fetched:
        mentioned.update(p.differentiators_mentioned)
    report.differentiator_whitespace = [d for d in YOUR_DIFFERENTIATORS if d not in mentioned]
    return report


# ----------------------------------------------------------------------------- 
# Reporting
# -----------------------------------------------------------------------------

def render_markdown(reports: list[KeywordReport]) -> str:
    out = ["# SERP & content-gap report\n"]
    for r in reports:
        out.append(f"## `{r.keyword}`\n")
        out.append(f"**Dominant intent of ranking pages:** {r.dominant_intent}  "
                   f"→ build a *{r.dominant_intent}*-type page, not a generic explainer.\n")

        out.append("### Ranking pages\n")
        out.append("| # | Page type | Words | Schema | Coverage | Differentiators they mention |")
        out.append("|---|-----------|-------|--------|----------|------------------------------|")
        for p in r.pages:
            if not p.fetched:
                out.append(f"| {p.rank} | — | — | — | — | _{p.error}_ |")
                continue
            cov = "n/a" if p.semantic_coverage is None else f"{p.semantic_coverage:.2f}"
            schema = ", ".join(p.schema_types) or "none"
            diffs = ", ".join(p.differentiators_mentioned) or "—"
            out.append(f"| {p.rank} | {p.page_type} | {p.word_count} | {schema} | {cov} | {diffs} |")
        out.append("")

        if r.common_subtopics:
            out.append("### Table stakes (every leader covers these — you must too)")
            out.append(", ".join(f"`{s}`" for s in r.common_subtopics) + "\n")
        if r.gap_subtopics:
            out.append("### Quick wins (only some leaders cover these — cover them better)")
            out.append(", ".join(f"`{s}`" for s in r.gap_subtopics) + "\n")
        if r.differentiator_whitespace:
            out.append("### Whitespace — your wedge (NO leader covers these)")
            for d in r.differentiator_whitespace:
                out.append(f"- **{d}** — none of the top pages address this. This is the non-commodity, "
                           f"first-hand angle you can own (build log, benchmark, or worked example).")
            out.append("")
        out.append("---\n")
    return "\n".join(out)


# ----------------------------------------------------------------------------- 
# CLI
# -----------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description="Competitive SERP & content-gap analyzer.")
    ap.add_argument("keywords", nargs="*", help="Keywords (up to 10).")
    ap.add_argument("--file", help="Path to a file with one keyword per line.")
    ap.add_argument("--top", type=int, default=3, help="Top-N ranking pages to analyze per keyword.")
    ap.add_argument("--out", default="serp_report.md", help="Markdown report output path.")
    ap.add_argument("--json", help="Optional JSON output path.")
    args = ap.parse_args()

    keywords = list(args.keywords)
    if args.file:
        with open(args.file) as f:
            keywords += [ln.strip() for ln in f if ln.strip()]
    keywords = keywords[:MAX_KEYWORDS]
    if not keywords:
        ap.error("Provide keywords as args or via --file.")

    if not SERPAPI_KEY:
        print(
            "ERROR: SERPAPI_KEY is not set. This tool requires a SERP API key "
            "(free tier at https://serpapi.com) — it does not scrape Google directly.\n"
            "  export SERPAPI_KEY=\"your_key\"   then re-run.",
            file=sys.stderr,
        )
        sys.exit(2)

    reports = []
    for kw in keywords:
        print(f"Analyzing: {kw}", file=sys.stderr)
        reports.append(analyze_keyword(kw, args.top))

    total_fetched = sum(len([p for p in r.pages if p.fetched]) for r in reports)
    if total_fetched == 0:
        print(
            "ERROR: no SERP pages could be fetched for any keyword (SERP API returned "
            "nothing, or every ranking page was blocked/unreachable). No report written — "
            "rerun with a valid key, fewer keywords, or check network/robots access.",
            file=sys.stderr,
        )
        sys.exit(1)

    md = render_markdown(reports)
    with open(args.out, "w") as f:
        f.write(md)
    print(f"\nReport written to {args.out}", file=sys.stderr)

    if args.json:
        with open(args.json, "w") as f:
            json.dump([asdict(r) for r in reports], f, indent=2)
        print(f"JSON written to {args.json}", file=sys.stderr)


if __name__ == "__main__":
    main()
