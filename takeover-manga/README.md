# TAKEOVER — Manga

Comic-style manga adaptations of the **FBG Universe "Takeover"** lore
(world year 2577 PE), produced with BAEZ Studio's AI generation pipeline.

## Pipeline
1. **Lore** → source of truth is the internal Takeover Lore Bible (kept out of git —
   see `lore-master.txt`, gitignored; do not publish).
2. **Script** → per-chapter page/panel breakdown (`chapters/chNN/script.md`).
3. **Character design** → reusable model sheets in `characters/` used as visual
   references so the cast stays consistent panel-to-panel.
4. **Panels** → generated with **Takeover Studio** (`studio/`) — our own
   character-consistency panel generator (see below) — or directly via Higgsfield
   (Nano Banana Pro). Authentic B&W manga (ink + screentone).
5. **Assembly** → the storyboard in Takeover Studio collects and exports panels.

## Takeover Studio (`studio/index.html`)
Our own character-consistency generator, purpose-built for the manga. A
self-contained, client-side web tool — no server, no build step — built on three
ideas: **identity from references** + **layout from composition** + a
**resemblance ↔ adaptation** dial.

- **Characters** — lock each character from reference art; "Load Takeover cast"
  seeds the canonical 8-faction roster + Rae.
- **Compose** — cast the panel, pick composition/mood/style, dial resemblance,
  and generate a B&W manga panel. The tool assembles a structured prompt from the
  character refs + shot + style.
- **Storyboard** — collect kept panels, export/download.
- **Backends** — ships with an offline **Demo** renderer (always works), plus
  pluggable **Google Gemini (Nano Banana)** and **custom-endpoint** adapters.
  API keys live in the browser only (localStorage) and go straight to the
  provider — nothing routes through BAEZ servers. Project data
  import/exports as JSON.
- Verified end-to-end in headless Chromium (`noindex`, not served in sitemap).

## Structure
```
takeover-manga/
  README.md            this file
  lore-master.txt      internal lore bible (GITIGNORED — not served publicly)
  characters/          reusable character design sheets
  chapters/
    ch01/
      script.md        Chapter 1 page/panel script
      panels/          generated panel art for Chapter 1
```

## Status
- **Ch01 "Collateral"** — script drafted; protagonist design sheet generated
  (Rae Marlo, 19, citizen bot-pilot). Panels pending art-direction sign-off.
