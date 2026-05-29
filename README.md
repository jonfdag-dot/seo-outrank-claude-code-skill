# AI-Era SEO & Marketing Skill for Claude Code

Point this skill at any web page (or a keyword) and it runs a **live competitive SEO assessment**: it searches Google in real time, scrapes the top-ranking competitors, finds the content gaps they leave open, and hands you a concrete plan — page title, URL slug, headline, and opening line — to outrank them. **No API key required** — it uses Claude Code's built-in web tools.

## Install — 3 steps

### 1. Download
Download this folder as a ZIP and unzip it. You should have a folder named `ai-era-seo-marketing` containing `SKILL.md` and a `scripts/` folder.

### 2. Drag it into your Claude skills folder
Move the whole `ai-era-seo-marketing` folder into your Claude skills directory:
- **This project only:** `.claude/skills/`
- **All your projects:** `~/.claude/skills/`

> Put it *directly* inside `.claude/skills/` — not in a sub-folder — or Claude won't recognize it by name.

### 3. Ask Claude Code to wire it in
Open Claude Code in your project and paste this prompt:

```
I just added a skill folder called "ai-era-seo-marketing" to my Claude skills directory. Wire it in so you use it automatically for any SEO, landing-page, or marketing work on this project, and adapt it to my actual stack. Specifically:

- Confirm the skill is discoverable in .claude/skills/ (move it up one level if it's nested so the /name resolves), then add a one-line pointer to it in my CLAUDE.md / AGENTS.md / project instructions so it's the default skill for SEO and page work.
- Read the skill, then scan my repo to learn where my pages and content live and how my site outputs page metadata (title, meta description, canonical URL, and structured data / JSON-LD) — and record that mapping so the skill's steps match my setup.
- Fill in the skill's keyword-bank and differentiators placeholders with terms and advantages specific to my product.

Then confirm it's working by running its Live SEO Assessment Loop on one of my real pages and showing me the assessment.
```

That's it. From now on, just tell Claude **"run the SEO skill on /my-page"** and it searches live, studies your competitors, and tells you exactly what to change to win the top spot.
