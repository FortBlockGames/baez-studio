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
- **Backends** — **Higgsfield (BAEZ)** is the default engine: the studio POSTs to
  a serverless proxy at **`/api/generate`** (`../../api/generate.js`) that holds the
  Higgsfield key server-side and submits/polls the Higgsfield Cloud API. Also ships
  an offline **Demo** renderer (always works; auto-fallback when `/api/generate`
  isn't reachable, e.g. opening the local file) and a **custom-endpoint** adapter.
  Project data import/exports as JSON.
- Verified end-to-end in headless Chromium (`noindex`, not served in sitemap).

### Deploy config (Higgsfield backend)
The `/api/generate` proxy needs, in Vercel → Project → Settings → Environment Variables:

| Var | Required | Notes |
| --- | --- | --- |
| `HIGGSFIELD_API_KEY` | yes | `KEY_ID:KEY_SECRET` — create at https://platform.higgsfield.ai |
| `HIGGSFIELD_MODEL` | no | Cloud API model path (default `nano-banana/text-to-image`) |
| `HIGGSFIELD_BASE` | no | API base (default `https://platform.higgsfield.ai`) |
| `STUDIO_ACCESS_CODE` | no | if set, clients must supply it (Settings → Access code) — keeps the tool semi-private |
| `ALLOWED_ORIGINS` | no | extra allowed origins (comma-separated); same-origin is always allowed |

The key is read only server-side and never shipped to the browser. Until it's set,
the deployed studio returns a clear error on Generate; the local file falls back to Demo.

### Abuse protection (public-facing endpoint)
`/api/generate` is built to serve Takeover Conquest users generating promo lore,
so it ships locked down:
- **Same-origin only** — requests must come from the site itself (plus `ALLOWED_ORIGINS`).
- **Optional access code** via `STUDIO_ACCESS_CODE` for a semi-private launch.
- **Strict rate limits** — per IP: 4/min, 20/hour, 40/day, 2 concurrent; per server
  instance: 12/min, 300/day, 4 concurrent. 429 responses carry `Retry-After`,
  which the studio surfaces to the user.
- **Input validation** — prompt length cap, no inline data, aspect-ratio allowlist,
  one image per request.
- Limits are in-memory per warm serverless instance (best-effort). If traffic
  grows, swap in Vercel KV/Upstash for hard global caps — the check is isolated
  in `checkLimits()` so it's a one-function change.

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
- **Series plan** — `SERIES-PLAN.md`: 3 seasons / ~150 chapters, arc-per-faction,
  research-backed format + acquisition loop (research: `research/playbook.md`).
- **Ch01 "Collateral" v1** — SHIPPED: cover + 8 pages generated, reader at
  `chapters/ch01/`. v2 milestone: expand to the 55-page hook formula.
