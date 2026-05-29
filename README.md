<p align="center">
  <img src="./banner.svg" alt="AI-Era SEO and Marketing Skill for Claude Code" width="100%">
</p>

<p align="center">
  <sub>A Claude Code skill &middot; authored by <b>[your name]</b> &middot; MIT License</sub>
</p>

Point this skill at any web page (or a keyword) and it runs a **live competitive SEO assessment**: it searches Google in real time, scrapes the top-ranking competitors, finds the content gaps they leave open, and hands you a concrete plan — page title, URL slug, headline, and opening line — to outrank them. **No API key required** — it uses Claude Code's built-in web tools.

---

## Install in 3 steps

### Step 1 · Download
Download this folder as a ZIP and unzip it. You should have a folder named `ai-era-seo-marketing` containing `SKILL.md` and a `scripts/` folder.

### Step 2 · Drag it into your Claude skills folder
Move the whole `ai-era-seo-marketing` folder into `.claude/skills/` (this project only) or `~/.claude/skills/` (all your projects). Put it *directly* inside that folder — not in a sub-folder — or Claude won't recognize it by name.

### Step 3 · Ask Claude Code to wire it in
Open Claude Code in your project and paste this prompt:

```
I just added a skill folder called "ai-era-seo-marketing" to my Claude skills directory. Wire it in so you use it automatically for any SEO, landing-page, or marketing work on this project, and adapt it to my actual stack. Specifically:

- Confirm the skill is discoverable in .claude/skills/ (move it up one level if it's nested so the /name resolves), then add a one-line pointer to it in my CLAUDE.md / AGENTS.md / project instructions so it's the default skill for SEO and page work.
- Read the skill, then scan my repo to learn where my pages and content live and how my site outputs page metadata (title, meta description, canonical URL, and structured data / JSON-LD) — and record that mapping so the skill's steps match my setup.
- Fill in the skill's keyword-bank and differentiators placeholders with terms and advantages specific to my product.

Then confirm it's working by running its Live SEO Assessment Loop on one of my real pages and showing me the assessment.
```

> **No setup, no API key.** This skill uses Claude Code's built-in web search and fetch — nothing to enable or configure. The first time it runs, Claude may ask permission to use **WebSearch** / **WebFetch** — just approve it.

---

That's it. From now on, just tell Claude **"run the SEO skill on /my-page"** and it searches live, studies your competitors, and tells you exactly what to change to win the top spot.



# Sources

This skill is grounded in official Google Search Central documentation
(verified 2026-05-28).

| Source | URL |
|---|---|
| Optimizing for generative AI search | https://developers.google.com/search/docs/fundamentals/ai-optimization-guide |
| SEO Starter Guide | https://developers.google.com/search/docs/fundamentals/seo-starter-guide |
| Guide to Google Search ranking systems | https://developers.google.com/search/docs/appearance/ranking-systems-guide |
| Structured data (all features) | https://developers.google.com/search/docs/appearance/structured-data/search-gallery |
| FAQ structured data (deprecation notice) | https://developers.google.com/search/docs/appearance/structured-data/faqpage |
| Spam policies | https://developers.google.com/search/docs/essentials/spam-policies |

**Note:** Any cited statistics (e.g. "58% click reduction," Ahrefs studies) are
third-party estimates, not Google guidance.
