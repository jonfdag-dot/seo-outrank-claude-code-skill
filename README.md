<div align="center">

# AI-Era SEO & Marketing Skill

### Outrank the page above you.

A Claude Code skill that runs a **live competitive SEO assessment** — no API key.

<sub>Authored by <b>Jonathan Dag</b></sub>

</div>

---

Point this skill at any web page (or a keyword) and it runs a **live competitive SEO assessment**: it searches Google in real time, scrapes the top-ranking competitors, finds the content gaps they leave open, and hands you a concrete plan — page title, URL slug, headline, and opening line — to outrank them. **No API key required** — it uses Claude Code's built-in web tools.

---

## Install in 3 steps

### Step 1 · Download the repo
Download the repo as a ZIP and unzip it — inside you'll find the `ai-era-seo-marketing` skill folder.

### Step 2 · Drag the skill folder into your Claude skills folder
Drag the `ai-era-seo-marketing` folder into `.claude/skills/` (this project only) or `~/.claude/skills/` (all your projects). Put it *directly* inside that folder — not in a sub-folder — or Claude won't recognize it by name.

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
