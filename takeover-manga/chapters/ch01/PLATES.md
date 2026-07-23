# Chapter 1 "Collateral" — Final Textless Plate Manifest

Canonical textless art plates (2K, 2:3, `nano_banana_2`), each verified via the asset
relay against the Visual Consistency Standard + ASSETS.md locks before lettering.
Dialogue is a typeset HTML overlay in `index.html` (SEPARATED-LETTERING LAW) — no text
is generated into the art.

| Page | Job ID | Reference anchors | Verify verdict |
| --- | --- | --- | --- |
| Cover | `5e28db52-0ef2-401a-9d03-c74ab9d98fcf` | Rae-Manga + BOT-SOLDIER | PASS — LoG bot black `#23232B`/orange `#FF7A1A`, Rae monochrome, title band reserved |
| Narrator (McClaine) | `3b98fbfc-0ad8-418e-83e1-ab0bc4494d8f` | McClaine-Manga + McClaine-Color-Master | PASS — canonical colors (tan suit, cyan-teal eyes), sealed mouthplate, textless |
| P1 (v3) | `32c2530e-6786-49a3-a767-09f9da3e304a` | Rae-Manga + BOT-SOLDIER | PASS — Chickows `#E02418` / Dollar Holler `#FFD534` bots, all signage blank |
| P2 | `3fc5a7ad-a976-48ee-9e57-77ce0ac94a76` | Rae-Manga | PASS — Vital Vibe teal `#17C3B2`/orange `#FF7849` recruitment holo is the only color |
| P3 (v3) | `9fdc6fad-5691-4bad-9d6a-0ff41318ce1f` | Rae-Manga + BOT-SOLDIER | PASS — Dollar Holler gold bots, blank SFX burst, cabinets/storefronts blank |
| P4 | `e5e6e1fc-182b-4f3d-a06e-584d6f7a9a91` | Rae-Manga | PASS — orange `#FF7A1A` pirate broadcast only color, eight blank banners |
| P5 | `7d9bd776-18ca-4077-8863-637e4121da10` | Rae-Manga | PASS — eight-banner money shot, all 8 faction hexes correct, banners blank |
| P6 | `4fb59ba9-a0b9-4a35-a766-53fea8a6e5bb` | Rae-Manga + BOT-SOLDIER | PASS — grey bot resolves to LoG black/orange paint bloom |
| P7 (v3) | `c4f8f4ee-2bfd-4a20-9b8a-edb97991521e` | Rae-Manga + BOT-SOLDIER | PASS — wordless orange HUD, blank impact burst, LoG bot black/orange |
| P8 | `860b3ce6-7cd3-4147-812e-890bea019b99` | Rae-Manga + BOT-Captain | PASS — LoG bots on-model, orange rebel (Skullface) hologram, textless |

## Reroll log (why P1/P3/P7 have a v3)
The first clean-regen batch produced Iron-Man-style armor wherever a bot was framed as
"full combat armor in faction paint" (P1 shipped with an EMPTY anchor list; P3 drifted
despite the BOT-Captain anchor), plus the model hallucinated environmental signage/SFX
text ("DOLLAR HOLLER" sign, "STARFIGHTER" cabinet, "EMPTY!!" / "SKOOM" SFX, katakana).

Fixes applied (guard-audited before each reroll):
1. **Every bot anchored to `BOT-SOLDIER`** (`bfd9815d…`) with hard anti-Iron-Man negatives
   ("NOT sleek superhero armor / faceplate / marvel"). P6/P8 proved the bare token renders
   the real design; the drift was caused by full-armor prose + gold color reading as Iron-Man.
2. **No positive re-description of locked designs** — identity rides the Element token only
   (consistency-guard finding; Prime Law).
3. **Hardened textless clause** — every cabinet/screen/store/sign/HUD/SFX declared BLANK,
   "ZERO letters/numbers/words in ANY language," with per-surface negatives. This cleared
   the residual signage and forced blank SFX bursts (SFX are added in the letter overlay).
4. **Rae anchored in P1 Panel 3** (was described as "teenage eyes" — a guard-flagged
   identity breach).

## Known-benign residuals (accepted)
- P2 arcade screen shows tiny diegetic game-HUD icons (not words) — accepted as first-batch.
- P7 HUD carries small wordless targeting icons — accepted (no letters/numbers).

## Lettering + logo compositing (reader)
Two overlay layers sit on top of every textless plate in `index.html`, so the art
files stay pristine and every mark is pixel-exact:
1. **Dialogue** — typeset HTML text placed *inside the art's own drawn bubbles*
   (transparent, no added balloons), per the founder note. Story pages letter into the
   generated bubbles; the cover + narrator (open-space plates) use styled caption boxes.
2. **Official logos** — the real transparent PNG masters, composited (never generated):
   - `assets/logos/takeover-white.png` on the cover (Drive master, 2048×512).
   - all eight `assets/logos/<faction>.png` crests on the Page-5 banner ring.
   - `log.png` on Rae's gauntlet at the Legion-of-Ghosts assignment (Page 5), replacing
     the hallucinated sigil (founder note #3).
   - `vital-vibe.png` on the Page-2 recruitment hologram, replacing the invented drone
     glyph (founder note #4).
   Logo masters pulled from the owner's Drive faction-logo set + title-logo folder and
   committed to `takeover-manga/assets/logos/` for stable, version-controlled hosting.

## Durable follow-up (logged, not blocking)
Per consistency-guard §4A, cut a founder-approved `BOT-SOLDIER-Manga` style Element so the
manga register never has to fight the generic archetype. The BOT-SOLDIER token is the
current working anchor and now renders on-model, but a cut manga Element is the permanent fix.
