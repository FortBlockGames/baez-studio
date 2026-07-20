# TAKEOVER — Manga

Comic-style manga adaptations of the **FBG Universe / Makooor** "Takeover" lore
(world year 2577 PE), produced with BAEZ Studio's AI generation pipeline.

## Pipeline
1. **Lore** → source of truth is the internal Takeover Lore Bible (kept out of git —
   see `lore-master.txt`, gitignored; do not publish).
2. **Script** → per-chapter page/panel breakdown (`chapters/chNN/script.md`).
3. **Character design** → reusable model sheets in `characters/` used as visual
   references so the cast stays consistent panel-to-panel.
4. **Panels** → generated via Higgsfield (Nano Banana Pro), authentic B&W manga
   (ink + screentone).
5. **Assembly** → a lightweight comic-reader page renders the chapter.

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
