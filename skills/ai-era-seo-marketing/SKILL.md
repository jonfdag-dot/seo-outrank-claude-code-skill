---
name: ai-era-seo-marketing
description: >
  ALWAYS load and apply this skill whenever the task touches SEO, content
  strategy, landing pages, keyword research, marketing copy, brand messaging,
  competitor positioning, blog/page creation, sitemap/SEO file edits, or any
  go-to-market work for your product. This is the canonical playbook for how to
  do search and AI-citation marketing. Treat its rules as defaults, not
  suggestions. If a request would violate a rule here (e.g. "write a how-to blog
  post to rank"), surface the conflict and propose the conversion-page
  alternative instead. WHEN INVOKED ON A PAGE OR KEYWORD, run the Live SEO
  Assessment Loop (Addendum A) end-to-end — live `WebSearch` for the SERP +
  robots-aware `WebFetch` to scrape the top-3 competitors, then a content-gap
  assessment — and return the SEO Assessment. No API key required; this is the
  default behavior, not an optional step.
triggers:
  - "editing files under /marketing, /content, /seo, /public, /pages, /blog"
  - "editing sitemap.xml, robots.txt, prerender config, JSON-LD, meta tags"
  - "any prompt containing SEO, keyword, ranking, landing page, comparison page, vs page, alternative page, backlink, press release, HARO, content strategy, AI overview, GEO (generative engine optimization), brand messaging"
  - "drafting copy that will be publicly indexed"
version: 2.0
owner: (your organization)
---

# AI-Era SEO & Marketing — Operating Playbook

## 0. How to use this skill

This is both a **way of working** and a **knowledge base**. When invoked:

> **DEFAULT ACTION — run the Live SEO Assessment Loop (Addendum A).** Whenever the operator points this skill at a page or a keyword ("run the SEO skill on X", "optimize X", "where can X rank"), the *first thing you do* is execute the six-phase live loop in Addendum A — keyless `WebSearch` for the real SERP, robots-aware `WebFetch` to scrape the top-3 competitors, content-gap analysis, then return the **SEO Assessment**. Do not substitute playbook recitation or the static keyword bank for live data. If live web tools are genuinely unavailable in the session, say so explicitly and fall back to Tier-2 (the script) or labeled hand-analysis — never present static analysis as a live assessment.

1. Run the **Live SEO Assessment Loop** (Addendum A) — this produces the assessment.
2. Apply the **Hard Rules** (Section 9) without exception unless explicitly overridden by the operator.
3. When generating/updating a page, run the **Page Build Checklist** (Section 10).
4. When the operator asks for something that contradicts a Hard Rule, do not silently comply — name the conflict and offer the playbook-aligned alternative.

**Boundary — where this skill stops (run order: strategy → format → technical gate → audits).** This skill owns *strategy*: keyword/intent targeting, page-type selection, positioning, SERP/citation, and your per-route schema *assignment* (Section 13). It does **not** own technical-SEO depth. Defer to **your technical-SEO reference** for crawl/render/index rules, tag reference, and **schema validity** (which types are worth it + the visible-content rule); defer to **your page-format/design conventions** for page skeleton/tokens. Run this skill *first* to set the target, then those gates before ship.

The single mental model behind everything below:

> **Old SEO answered questions so people would visit. New SEO captures people who already know what they want but not which brand gives it to them — and plants citations that LLMs repeat back as fact.**

Two structural facts this playbook is built around:
- AI overviews have measurably cut clicks to informational pages (~58% reduction in cited studies). Ranking #1 on an informational query no longer guarantees traffic.
- LLMs (ChatGPT, Claude, Gemini, Perplexity) get most real-time answers from web search. They surface and paraphrase whatever ranks — they do not independently verify. Whoever controls the indexed content controls the AI answer.

---

## 1. STRATEGY GROUP A — Intent & Keyword Targeting

The foundation. Everything else amplifies the keywords you choose here.

### A1. Hunt high-intent, not high-volume
- **Target keywords where the searcher wants to *act*, not *learn*.** Signals: `generator`, `[task] for [profession]`, `[service] near me`, `24 hour [x]`, `[outcome] tool`, `book`, `buy`, `[competitor] alternative`.
- High intent → fewer searchers → **lower volume → ignored by incumbents.** That gap is the opportunity. Big players chase head terms; they leave high-intent long-tail untargeted.
- Anti-pattern: chasing `what is`, `how to`, `when`, `why` informational terms. These are now answered inside the AI overview and rarely earn a click.

### A1.1 Keyword shape — the targeting rule (apply on EVERY target, no exceptions)

The single most common failure is drifting to a phrase that's too long and too generic (e.g. searching a full sentence describing the job, or swapping a named tool/entity for a vague category). Every target keyword must pass ALL five:

1. **Length: 2–3 words minimum, 5–6 words MAXIMUM.** Never longer. If a phrase runs long, distill to its core — drop `how to / my / into / files / a / for`. Count the words before you search.
2. **Most common surface form.** Phrase it the way a practitioner *actually types it into Google* — the common search, not a clever internal/brand name.
3. **Common but unique.** Common enough that people search it; specific enough that few strong pages own it. The sweet spot = a familiar phrase + **one** specific anchor that narrows the slot.
4. **Anchor on a concrete named entity — never a generic category.** Prefer the named tool/file/format/platform your audience actually types. Ban the generic dilutants that lose the slot (broad categories like `AI`, `platform`, `software`, `automation`, `solution`). A specific named anchor beats a vague category every time. **"for [named tool]" beats "for the category"; the exact filename beats "the file".**
5. **One target per page.**

**Self-check before any `WebSearch`:** word count 2–6? · names a specific tool/entity (not a generic category)? · would a real practitioner type these exact words? · do only a handful of strong pages own it?

| Too long / too generic | Tightened target |
|---|---|
| `<full sentence describing the job> for AI agents` (too long, generic category) | `<core task> + <named tool>` (5w) · `<entity> to <named format>` (4w) |
| `how to <verb> <thing> into <format> files for <platform>` (9w) | `<verb> <thing> to <format>` (4w) · `<thing> to <platform> skill` (5w) |
| `<generic connector> for AI agents` ("AI agents") | `<connector type> for <named tool>` (5w) · `read-only <db> connector` (4w) |
| `how to give <team> their own AI analyst` (9w) | `<role> agent for <task>` (5w) · `<role> skill file` (4w) |

### A2. Semantic similarity is the #1 ranking factor for AI citation
Per large-scale prompt studies (Ahrefs, ~1.4M AI prompts), the strongest predictor of being cited by an LLM is **semantic similarity between your page and the language the AI uses when searching** — *similarity*, not string identity. Modern search and LLMs resolve synonyms; you write for the human, and the machine follows.

Make the page's primary subject unmistakable — in the searcher's natural language, synonyms welcome — in all four anchor placements (see the reframed Four-Slot Rule, Section 7):
1. **Page `<title>`**
2. **URL slug** (descriptive, like `/postgres-to-skill-converter`, not `/features/converter-v2`)
3. **`<h1>`**
4. **The opening line of body copy**

Do **not** engineer exact-match repetition to "beat" a competitor's keyword density — that v1.0 mechanic is retired (see Section 6 F2 and the companion script's stated non-goal). Cover the *intent*; let the words read like a human wrote them.

### A3. Reverse-engineer what the AI actually searched
When auditing why a competitor gets cited, inspect the real query the LLM issued:
- In ChatGPT, copy the conversation ID from the URL (the part after `/c/`).
- Right-click → Inspect → Network tab → paste the ID → refresh → open the matching request → Response → search for `"queries"`. That array is the literal search string the model ran.
- Then run those exact strings in Google yourself to see what's ranking — that's your competition for the citation slot.

### A4. Your focal-point keyword bank

Mine high-intent terms around the job-to-be-done, not the category. The set below is the **focal set**: ultra-specific, low-competition phrases where ranking #1 is realistic *because almost nobody targets them yet.* Each is grouped by intent, which dictates the **page type** to build (Section 2). Target **one** phrase per page — the more specific, the more winnable.

> **Replace this bank with 10–20 terms for YOUR product's jobs-to-be-done.** The phrases below are *illustrative examples* showing the shape and grouping — substitute your own named entities (your tools, files, formats, integrations, roles). Keep the structure: group by intent → page type, distill each to its 2–6 word core per the A1.1 shape rule, keep the named anchor, drop the filler.

These are written as full jobs for clarity; the **target you actually optimize for is the 2–6 word core** per the A1.1 shape rule — keep the named anchor (your tool/file/format/platform name), drop the filler. E.g. `How to give [tool] access to my [data source]` → target `[tool] [data source] access` (4w).

**Tool / transactional ("I want to do this now")** → conversion landing pages (B1):
- `[verb] [your input] into [your output format]` (e.g. an export/convert action)
- `[your core action] for [named platform]`
- `[your tool] for [specific job]`

**Integration / setup how-to** → integration pages:
- `how to connect [named tool] to [your product]`
- `[integration type] for [named platform]`
- `[your product] [named platform] setup`

**Team / role / org ("for my team / my department")** → buyer-framed conversion pages (B1):
- `[your product] for my team`
- `build a [role] [your output] from [data source]`
- `per-department [your product] setup`

**Comparison / objection** → comparison & alternative pages (B2/B3):
- `[your category] alternative to [competitor]`
- `[your differentiator] vs [the common objection]`

**Note on the `How to…` phrasings:** these are **transactional in disguise** — the searcher wants to *accomplish the task*, not read theory. They are **not** the dead informational pattern F1 warns against. Answer each with a conversion or integration page that *demonstrates the how* (worked example, real connector steps, copy-paste artifact) with a CTA above the fold — never a blog explainer.

Avoid head terms your product will lose on (broad category terms incumbents own) — incumbents own those.

---

## 2. STRATEGY GROUP B — Page Types That Win

In the AI era, **conversion-oriented landing pages and structured comparison pages** are the highest-ROI assets. They convert well in Google *and* are disproportionately cited by LLMs because they're concrete and structured.

### B1. Conversion SEO landing pages (replace blog posts)
- One page per high-intent job. The page **is** the conversion surface, not a stop on the way to one.
- Above-the-fold CTA before any scrolling: start the product, run the demo, book a call.
- Lead with the outcome the searcher typed, in their words (A2).
- These pages get referenced by AI far more than blog posts and convert at far higher rates.

### B2. Comparison pages — `[You] vs [Competitor]`
- A direct, honest comparison page lets you **control the narrative** that both Google and AI overviews repeat.
- AI overviews literally lift comparison **tables**. Include a clean, structured table — it's the most extractable format.
- Make a page for each major competitor. Reference real, defensible differentiators.

### B3. Alternative pages — `[Competitor] alternative`
- Page title: `[Competitor] Alternative`. H2: `[Competitor] vs [Your Product]: Comparison`.
- Keep the pitch tight and concise; CTA visible before scroll.
- Embed a comparison table (reuse B2 structure).
- **Bonus mechanic:** if a competitor under-invests in SEO, your alternative page can rank for *their own brand name* and get cited when people research them.

### B4. Reviews page — `[Your Product] reviews`
- A dedicated page consolidating every review/testimonial you want surfaced.
- During due diligence, LLMs search `[brand] reviews` → Google → this page → they paraphrase what they find.
- **Critical:** link to it from your main site so Google indexes it. An unlinked review page is invisible to crawlers and therefore to AI.

### B5. Your comparison/alternative targets
Build the full matrix against **your top 2–4 competitors**, and any product positioning to capture the same demand you serve. Your narrative wedge in every table is **your product's unique, hard-to-copy differentiators — the things competitors structurally can't claim (fill these in for your product).** For example:
- **A capability only you offer** (something a competitor's architecture can't match)
- **A proprietary dataset or first-hand source** competitors don't have
- **An integration or portability competitors lack** (e.g. runs outside the platform, not locked to one vendor)

---

## 3. STRATEGY GROUP C — Off-Site Authority & Digital PR

Backlinks and third-party mentions build the trust that makes Google rank you and makes LLMs treat you as a real entity.

### C1. Journalist sourcing (HARO successors)
- Sign up free as an expert on **Source of Sources** (sourceofsources.com) and **Featured.com** — the successors to the now-defunct HARO.
- Journalists from major outlets (NYT, Washington Post, etc.) email queries daily looking for expert quotes.
- Reply fast with a genuinely useful, specific answer. Good answers get cited → the article ranks → you earn a high-authority backlink → AI cites the article (and you).

### C2. Distribution & directory launches
For any new product or feature page, run the launch sequence:
- SaaS directories
- Product Hunt
- BetaList
- Relevant subreddits / communities (value-first, not spam)
- Podcast appearances (use AI podcast-matching services to find shows)

### C3. The flywheel
Backlinks → Google trust → ranking for your target high-intent terms → LLMs pull from Google during web search → they recommend you in answers. Authority compounds; start the loop early.

### C4. Your application
- Position **your founder / subject-matter expert** as the credible source: name, title, and credentials (relevant prior roles, domain expertise, the specific problem they're known for solving). Lead with what makes them an authority in your category.
- Pitch angles for journalist queries: frame the structural problem your product solves, the contrarian take your differentiators support, and the trend your category sits inside.

---

## 4. STRATEGY GROUP D — AI Citation Mechanics (GEO)

How to get *named* inside an LLM answer, not just ranked.

### D1. LLMs repeat what's indexed
LLMs parrot web-search results as fact without verifying. This is a blue-ocean lever:
- A well-optimized **press release**, **Reddit post/comment**, or **YouTube description** can rank within hours and get repeated by LLMs.
- For reputation/branded queries, content titled `[Brand] review — is it legit?` is eaten up by both LLMs and humans doing due diligence.

### D2. Platforms that get cited well
Beyond your own site, these surfaces are frequently pulled into AI answers: **YouTube, TikTok, Instagram, X, Facebook, LinkedIn.** If your domain already has SEO authority, branded content on it ranks fast.

### D3. Make content genuinely cite-worthy
LLMs preferentially cite **original, specific, sourced** material:
- Original data, benchmarks, and stats *with sources*.
- Concrete numbers beat vague claims. "Does [the core job] in under N seconds across M tools" outperforms "fast and flexible."

### D4. Verify your own AI answers
When using AI for research, always open the cited sources — confirm where the claim actually came from before trusting it. (Also how you spot competitors planting content.)

### D5. Your application
- Publish original benchmarks tied to your differentiators: the metrics only you can measure first-hand (latency, accuracy, success rate, throughput — whatever your product uniquely produces).
- Maintain a branded `[Your Product] review / is it legit` surface (own site + one video) so due-diligence queries surface *your* framing.

---

## 5. STRATEGY GROUP E — The Unbundling Thesis (Product + GTM)

The strategic frame for where pages even come from.

- Large SaaS suites are bundles of features. Any one feature can now be rebuilt solo with modern tooling (Replit, Cursor, Claude Code).
- Find the high-intent keywords a major platform *ranks for but doesn't actively target*, rebuild that feature as a focused standalone, and capture the demand.
- **The only remaining barrier to entry is marketing** — which is exactly what this skill operationalizes.
- For your product: frame each capability as a sharp, searchable standalone (the "unbundled feature" extracted from the monolithic suite experience) rather than burying it inside a platform pitch.

---

## 6. STRATEGY GROUP F — What's Dead / Anti-Patterns

Do **not** spend effort here. Flag it if asked to.

### F1. Informational blog posts for traffic
- `how/what/when/why` blog content now feeds the AI overview and earns the click ~58% less often. Writing blog posts hoping to rank-and-convert is old SEO. Redirect that effort into conversion landing pages (B1).
- *Exception:* original-data / benchmark content (D3) is still worth publishing — but as a cite-magnet, not a traffic play.

### F2. Schema for types whose visible content isn't on the page (v2.0 — supersedes the old "minimal schema only" stance)
The v1.0 rule said "minimal Organization/Product only; schema barely moves AI visibility." That stance is **retired.** When your site emits a range of schema types and a build-time check enforces a per-route floor, structured data is infrastructure, not a side bet. The canonical positive rule now lives in **Section 13 (Structured Data — Per-Route Schema)**.

What stays dead is the *misuse*, not the schema:
- **Emitting a type whose required visible content isn't on the page.** `aggregateRating` with no visible reviews, `HowTo` with no real steps, `FAQPage` with no real Q&A on-page → spam signal, and Google may strip the rich result or penalize. Emit a type only when the page visibly contains what the type claims.
- **Relying on deprecated rich-result types.** Google deprecated `HowTo` rich results and restricted `FAQPage` rich results to authoritative gov/health sites; further types were retired (per Google Search Central — re-verify per Rule D4 before citing externally). You may still emit these for entity understanding, but **never plan a page's traffic around their rich-result appearance.**
- **Runtime-injecting JSON-LD.** Injecting `application/ld+json` via `document.createElement('script')` at runtime is unreliable — LLM crawlers and the prerender/raw pass don't run JS. Emit through your prerendered head/metadata mechanism only (Section 13).

### F3. Chasing volume over intent
- High-volume head terms are owned by incumbents and increasingly answered without a click. Lower-volume high-intent terms convert and get cited. Choose intent.

---

## 7. The Four-Slot Rule (v2.0 — descriptive subject, written for humans)

For every page, the **primary subject** — the job the searcher is trying to do, in their natural language — must be unmistakable in all four placements. **Synonyms are fine; write for a human, not for the crawler. Do not engineer exact-match repetition.** Matching the searcher's intent beats matching their exact string.

| Slot | Example |
|------|---------|
| `<title>` | `Export [Your Input] to [Named Tool] — [Your Product]` |
| URL slug | `/[your-input]-to-[named-tool]` |
| `<h1>` | `Turn [your input] into a portable [named-tool] artifact` |
| Opening line | `[Your Product] converts [your input] into a portable artifact you can run in [Tool A], [Tool B], or [Tool C].` |

The four placements may phrase the subject differently (the title, h1, and opening line above all vary the wording) — that is *correct*, not a defect. The test is: a reader landing on any one of the four instantly knows what the page is for. If the page's subject is ambiguous in any slot, it's not optimized. If you're counting keyword occurrences to "win," stop — that's the retired v1.0 trap (Section 6 F2, A2).

---

## 8. Asset Priority (where to spend the next hour)

Ranked by ROI in the AI era:

1. **Conversion landing pages** for high-intent jobs (B1)
2. **Comparison / alternative pages** with tables (B2, B3)
3. **Reviews page**, linked from main site (B4)
4. **Journalist-sourced backlinks** (C1)
5. **Original-data / benchmark posts** as cite-magnets (D3)
6. **Branded social/video** on cite-friendly platforms (D2)
7. ~~Informational blog posts~~ (F1 — deprioritize)
8. **Per-route structured data** via your head/metadata mechanism, content-backed (Section 13) — infrastructure, not optional; but never a *substitute* for the conversion/comparison content above it.

---

## 9. HARD RULES (enforce on every output)

1. **Never** propose an informational blog post as a primary traffic/conversion play. Default to a conversion landing page (B1).
2. **Always** apply the Four-Slot Rule (Section 7): the page's primary subject is unmistakable in title, slug, h1, and opening line — in natural human language, synonyms fine, never exact-match-engineered.
3. **Always** include a structured comparison **table** on any vs/alternative page.
4. **Always** place a CTA above the fold on conversion pages.
5. **Always** emit the per-route structured-data set via your head/metadata mechanism (Section 13), and **only** types whose required visible content is present on that page. Never runtime-inject JSON-LD; never plan traffic around deprecated `FAQPage`/`HowTo` rich results.
6. **Always** match the exact searcher/AI phrasing over clever marketing phrasing when they conflict.
7. **Always** link new authority pages (reviews, comparisons) from the main site so they're indexed.
8. **Prefer** concrete, sourced numbers over adjectives (D3).
9. When a request conflicts with these rules, **state the conflict and offer the compliant alternative** before proceeding.
10. Keep your product's unique, hard-to-copy differentiators present in competitive content — the things competitors structurally can't claim (fill these in for your product).

---

## 10. Page Build Checklist (run before shipping any page)

```
[ ] Ran the Live SEO Assessment Loop (Addendum A) first — live WebSearch SERP + WebFetch top-3 scrape — and targeting a single high-intent keyword/job (A1)?
[ ] Primary subject unmistakable in title, slug, h1, opening line — human language, synonyms fine, NOT exact-match-engineered (Four-Slot Rule)?
[ ] Page type matches the dominant intent of the ranking pages: conversion / comparison / alternative / reviews?
[ ] Covers the table-stakes subtopics the leaders all cover, AND lands at least one whitespace differentiator no leader covers?
[ ] CTA visible before scroll?
[ ] Comparison table present (if vs/alternative)?
[ ] At least one concrete, sourced number or benchmark?
[ ] Internal link from main site (for authority pages)?
[ ] Your differentiators referenced where relevant?
[ ] Per-route structured data emitted via your head/metadata mechanism, and every emitted type's required visible content is actually on the page (Section 13)?
[ ] NOT an informational blog post masquerading as a traffic play?
```

---

## 11. Reusable Templates

### 11.1 Comparison page skeleton (`/[your-product]-vs-[competitor]`)
```
Title:  [Your Product] vs [Competitor]: <your one-line wedge>
H1:     [Your Product] vs [Competitor]
Intro:  One sentence with the exact comparison phrase + the wedge.
CTA:    [Try [Your Product] free] (above fold)

H2: [Your Product] vs [Competitor]: Comparison
| Capability                   | [Your Product] | [Competitor] |
| <differentiator 1>           | ✓              | ?            |
| <differentiator 2>           | ✓              | ✗            |
| <differentiator 3>           | ✓              | ✗            |
| <capability competitor lacks>| ✓              | ✗            |

H2: When [Competitor] is the right call
(honest, concise — credibility = citation)

H2: Why teams choose [Your Product]
CTA again.
```

### 11.2 Alternative page skeleton (`/[competitor]-alternative`)
```
Title:  [Competitor] Alternative — [Your Product]
H1:     A [Competitor] alternative built on <your differentiators>
CTA:    above fold
H2:     [Competitor] vs [Your Product]: Comparison  (reuse table from 11.1)
Body:   tight, concise reasons to switch
```

### 11.3 Journalist response template (Source of Sources / Featured.com)
```
Hook (1 line, quotable):
Credential (your founder / SME — name, title, credentials; built [Your Product]):
Specific, original insight (numbers if possible):
Optional link to a relevant [Your Product] data/benchmark page:
```

---

## 12. Source provenance

This playbook distills a set of AI-era SEO/marketing talks. Cleaned references:
`Replit/Cursor` (vibe-coding tools), `Deel` (vs Rippling example), `Source of Sources`
+ `Featured.com` (HARO successors), `Ahrefs` (the cited studies). Figures (58% click
reduction; 1,885-page schema study; 1.4M-prompt semantic-similarity study) are reported
as stated in the source material — re-verify before citing externally per Rule D4.

---

## 13. Structured Data — Per-Route Schema (the metadata "form")

**Schema-validity source of truth:** your technical-SEO reference owns *which types are worth it*, the visible-content rule, and deprecations. This section owns your *per-route assignment* of those types and how they emit. The two cross-reference; defer to your technical-SEO reference for schema-validity depth.

**Rule (supersedes the old F2 "minimal schema" stance):** every public route emits the structured-data type(s) appropriate to *that page type*, and **only** types whose required visible content is actually on the page. Emit through your prerendered head/metadata mechanism (the thing that ships `<title>`, meta description, canonical, and JSON-LD into the static HTML) — **never** runtime-injected, since LLM crawlers and the raw prerender pass don't run JS. If you have a build-time SEO/prerender check, point it at the per-route schema floor below: a route missing its declared `@type` set should fail the build.

### 13.1 The emit surface (single source of truth)

All metadata should ship through **your site's head/metadata component** — whatever single mechanism emits `<title>`, meta description, canonical, and JSON-LD into the prerendered HTML. Map each field below to the prop/mechanism your site uses, and keep that mechanism the *single* source of truth (never reintroduce a competing head store). Authoritative Google references for these fields — re-verify per Rule D4 before citing externally:
- Search Central docs — `developers.google.com/search/docs`
- AI-optimization guide — `developers.google.com/search/docs/fundamentals/ai-optimization-guide`
- Rich Results Test — `search.google.com/test/rich-results`
- Schema.org type reference — `schema.org`
- Core Web Vitals / page experience — `web.dev`

### 13.2 Metadata form — Google field → your head/metadata mechanism → when to set

Fill this for every page; map each field to the prop/mechanism your site uses. Every emitted item must be backed by visible page content.

| Google / crawler field | Maps to (your mechanism) | Default if omitted | Set it when |
|---|---|---|---|
| `<title>` | title (required) | — | Always. 30–60 chars (homepage ≤75). Primary subject, human language. |
| meta description | description (required) | — | Always. 120–160 chars. |
| canonical URL | canonical | none (no canonical emitted) | Always on indexable pages. Path only (`/your-slug`); your site base is prepended. Drives `og:url` + auto-BreadcrumbList. |
| robots | robots | `index, follow` | Only to *restrict* (`noindex` on thin/utility pages). Public sitemap URLs must stay indexable. |
| meta keywords | keywords | none | Optional; Google ignores it. Low priority. |
| `og:title` / `og:description` | ogTitle / ogDescription | fall back to title / description | Only when social framing should differ from the SEO title. |
| `og:image` / alt | ogImage / ogImageAlt | your default OG image | Per-page share image. Must be ≥1200×630. |
| `og:type` | ogType | `website` | `article` on posts. |
| `twitter:card` | (automatic) | `summary_large_image` | — always emitted. |
| `article:published_time` | articlePublishedTime | none | On posts/articles (ISO 8601). |
| **BreadcrumbList** JSON-LD | breadcrumb items (multi-level) or breadcrumb name (2-level) | none on homepage; else nothing | On every non-homepage deep route. Auto-prepends Home. |
| **FAQPage** JSON-LD | faq schema / faq items | suppressed unless an FAQ page / feature flag | Only when real Q&A is visible on-page. **Do not plan traffic around its rich result** (deprecated for most sites). |
| **HowTo** JSON-LD | howTo schema | none | Only when real, numbered steps are visible on-page. Rich result deprecated — emit for entity understanding only. |
| **SoftwareApplication** (+Offer) JSON-LD | product schema | none | Product / pricing / tool pages. `aggregateRating` **only** with real visible reviews. |
| Organization / Person / WebSite / Article / Dataset / VideoObject / WebPage etc. | structured-data list (built from a shared schema helper) | none | Per the per-route floor in 13.3. |

### 13.3 Per-route schema floor (mirror this in your build verifier, if you have one)

If you have a build-time SEO/prerender check, keep this table and its per-route expectations in sync:

| Page type | Required `@type`(s) | Visible content the type requires |
|---|---|---|
| Home (`/`) | Organization, Person, WebSite, SoftwareApplication | real org/founder identity; app description + offer |
| Product / tool page | SoftwareApplication (+ HowTo only if real steps shown) | product description, real offer; HowTo only with visible numbered steps |
| Pricing | SoftwareApplication (Offer per plan) | visible plan + price for each Offer |
| Comparison / "vs" page | WebPage, ItemList | the visible comparison table rows |
| Blog post / resource | BlogPosting (+ BreadcrumbList) | real author, dates, body |
| Benchmark / original-data page | **Dataset** (+ Article) | the visible benchmark table/numbers with sources (D3/D5) |
| Demo / video | VideoObject, BreadcrumbList (ItemList on a demos index) | the embedded video + real metadata |
| Docs / guide | TechArticle (+ BreadcrumbList) | the visible guide body, real author/dates |
| About / founder | Person | real bio, credentials |
| FAQ | FAQPage | real Q&A visible on-page |
| Sitewide (every indexable page) | Organization + WebSite (via shared layout) | — |

**Audit-and-prune discipline:** before relying on `HowTo` or `FAQPage` on any route, audit it: if the required visible content (numbered steps, on-page Q&A) isn't present, remove that type from both the page's metadata call and your build verifier's expectation in the same change.

---

## Addendum A — The Live SEO Assessment Loop (run this EVERY time the skill is invoked)

**This is the skill's default operating procedure.** Goal: given a page and/or a keyword, *summarize the concept in focus → find the real competitors by live search → scrape their pages → find the gap → produce a concrete plan to beat them.* Output is always the **SEO Assessment** (template at the bottom). It needs **no API key** — it runs on the agent's own `WebSearch` + `WebFetch`.

### Two tiers — pick by scale

| Tier | Tools | When | Key? |
|---|---|---|---|
| **Tier 1 — in-session (DEFAULT)** | agent's `WebSearch` + `WebFetch` | "run the skill on this page", 1–10 keywords interactively | **No key** |
| **Tier 2 — batch / headless** | `scripts/serp_intel.py` (SerpAPI) | 10+ keywords, CI, or no-agent automation | `SERPAPI_KEY` required |

**Never scrape google.com directly** (ToS + CAPTCHA). `WebSearch` is the sanctioned SERP source; `WebFetch` is robots-aware and respects each site's rules. That is exactly why Tier-1 is keyless and safe.

### The six phases (Tier-1 — do all six, in order)

**Phase 0 — Summarize & prep (the concept in focus).** Read the page you're optimizing — its source files for a draft, or `WebFetch` the live URL. State in **one sentence** the page's job. List your differentiators relevant for *this* page (Rule 10: your product's unique, hard-to-copy differentiators). That sentence + those differentiators are the "concept in focus" you'll defend.

**Phase 1 — Target.** Pick **one** keyword and run it through the **A1.1 shape rule** (2–6 words · most common surface form · common-but-unique · anchored on a concrete named entity, never a generic category). Distill A4 bank entries to their 2–6 word core; keep the named anchor. State the target and confirm it passes all five A1.1 checks *before* searching. If it doesn't match the page's job, you need a *different* page, not a forced fit. **At scale:** repeat Phases 1–5 once per target (loop the A4 bank, ≤10 per session for Tier-1; hand 10+ to Tier-2).

**Phase 2 — Live SERP (`WebSearch`).** Search the **specific, named** target first — `WebSearch("<target with the named anchor>")`, not a generic category term. Record the top organic results (title + URL). Only widen with a *second* query if the first is thin — and widen with a **close synonym that keeps the named anchor**, never by genericizing to a category term. These results are the pages you must beat for the slot.

**Phase 3 — Scrape the top 3 (`WebFetch`, robots-aware).** For each of the top 3 URLs, call `WebFetch(url, <CANONICAL EXTRACTION PROMPT below>)` so every competitor returns the **same fields**. This is the "scrape their sites and understand how they rank" step. If a fetch is blocked/redirected, note it and move to the next result.

**Phase 4 — Compare & find the gap.** Across the three extractions, derive:
- **Dominant intent** (transactional / comparison / informational) → the page **type** to build or keep.
- **Table stakes** = subtopics **all three** cover → you must cover them too, or you're not credible.
- **Whitespace = the WEDGE** = your differentiators (Phase 0) that **none** of them cover → where you win, because they structurally can't copy it.
- **Four-slot diff** = how the leaders phrase their title/H1/slug vs. the differentiated job you can own.

**Phase 5 — Plot (how to beat them).** Write the plan: *target phrase · page type · the 1–2 whitespace wedges this page owns · the four-slot rewrite (title/slug/h1/opening line, human language, synonyms fine, NO exact-match stuffing) · per-route schema (Section 13).*

**Phase 6 — Update the page.** Apply via the **Section 10 checklist** + **Section 13 schema floor**, then hand to the gates in run order: your technical-SEO validation (crawl/render/index, tag + schema validity) + your page-format/design conventions. Cover every table-stakes subtopic, lead with the wedge, CTA above the fold.

### Canonical `WebFetch` extraction prompt (use verbatim, once per competitor)
```
Extract this page's SEO/positioning, factually and concisely:
1. the <title> and <h1>
2. primary keyword / search intent (transactional / comparison / informational)
3. main headings / subtopics it covers (the content fan-out)
4. does it mention any of — [your differentiator 1]; [your differentiator 2];
   [your differentiator 3]?  (yes/no for each — list YOUR product's
   hard-to-copy differentiators here)
5. its CTA and what it is selling
```

### The SEO Assessment — return this structure EVERY run
```
# SEO Assessment — <route or page> · target: "<keyword>"

Concept in focus: <one-sentence page job>            [Phase 0]
Your differentiators in play: <…>

Live SERP — top results:                             [Phase 2 · WebSearch]
  1. <title> — <url>
  2. <title> — <url>
  3. <title> — <url>

Top-3 competitors scraped:                           [Phase 3 · WebFetch, robots-aware]
  | # | title / h1 | intent | covers our wedge? | CTA / selling |

Dominant intent → page type: <…>                     [Phase 4]
Table stakes (must cover): <…>
WHITESPACE / our wedge (no leader covers): <…>

Plot to win:                                         [Phase 5]
  target phrase: <…> · page type: <…> · wedge: <…>
  four-slot rewrite —
    title  → <…>
    slug   → <…>
    h1     → <…>
    opening line → <…>
  schema (§13): <…>

Hard-Rules check (§9): <one line per rule, pass/fail>
Next gates: technical-SEO validation → page-format/design conventions
```

### Tier-2 — batch script (only for scale / headless)
For 10+ keywords or CI, `scripts/serp_intel.py` automates the same buckets via SerpAPI. Setup (Homebrew/system Python is PEP-668 externally-managed — use a venv, and `python3 -m pip`):
```
python3 -m venv .venv && source .venv/bin/activate
python3 -m pip install -r scripts/requirements.txt
export SERPAPI_KEY="…"   # REQUIRED for Tier-2 only; never scrapes google.com directly
python3 scripts/serp_intel.py --file keywords.txt --top 3 --out report.md
```
Without the key the script **exits non-zero** — it will not emit an empty report. The script's page-fetch is also robots-aware and rate-limited.

**Stated non-goal (both tiers):** do **not** score exact-keyword-match density to out-stuff competitors. Measure semantic/intent coverage and content gaps. If any coverage number pushes you toward rewriting for the metric, ignore it — that's the retired v1.0 trap (Section 6 F2, A2). You beat competitors by **covering the intent + owning the whitespace wedge**, not by repeating their keywords.
