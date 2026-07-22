# Consistency-Guard Audit — Chapter 1 (first live run)
*Agent: consistency-guard · against Visual Consistency Standard v1.3 + ASSETS.md*

## Verdicts
| Prompt | Verdict | Core defect |
|---|---|---|
| Narrator page v2 (assembly template) | **PASS** (3 risks) | conforms on identity/face/treatment; tighten banner plates, lettering routing, complete B1 negatives |
| Cover | **FAIL** (6 violations) | hero marks generated not composited; Rae + Soldier bot not Element-anchored; no negative blocks; hero text generated |
| Page 5 ritual | **FAIL** (3 violations + blocking risk) | readable banners = hero marks generated; 6 of 8 faction color locks missing; PUF canonical pick pending; inherits cover's anchoring/negative gaps |

**Ruling:** every page built on the cover/ritual pattern is presumed nonconforming on
marks, Rae anchoring, and negatives → queued for regeneration through Gates 2–4 once
the blocking registry items clear. The narrator-v2 pattern is the template to converge on.

## Blocking registry actions (founder)
1. **Faction color canon pass** — fill all 8 exact hex locks (zones.js vs lore-bible
   conflict; only Digi-U/DH hexes on file and both disputed vs lore palettes).
2. **Canonical PUF logo pick** — `puf-logo` vs `puf2-logo`; annotate the loser as retired.
3. **FBG wordmark master** — registry has none; needed before any "A FORT BLOCK GAMES
   MANGA" strip can be composited.

## Template upgrades adopted from this audit (apply to every future prompt)
- Blank-plate language for ALL readable marks + mark-plate negative add-on; composite
  masters in post (§2 is absolute — "reproduce exactly" phrasing is a wish, not a lock).
- `<<<Rae-Manga>>>` (2bd84b66…) and `<<<BOT-SOLDIER>>>` (bfd9815d…) anchors — never
  job-ID references, never prose bot descriptions.
- Full negative block: B1 base (incl. real-world brand/trademark ban) + B2 lettering
  + B3 portrait + mark-plate, folded in-prompt.
- Register the style string as a named preset + prepend the §7 canon-constants line.
- Neutral phrasing for style shorthands (no real-world publication names).

Full agent report retained in session log 2026-07-22.


## Gate-4 founder eyeball results (2026-07-22, narrator v3)
**FAIL — two founder-caught defects, both now codified as guard rules:**
1. Off-profile color: orange visor glow/accents on McClaine (canonical = cyan-teal
   glow, tan/gold palette; no faction colors ever). → COLOR LAW added to registry +
   guard rule 2b; `McClaine-Color-Master` element cut (e8f2c3e5…).
2. Stray hallucinated words in-frame beyond the scripted captions. → STRAY-TEXT LAW
   added to registry + guard rule 2c; v4 prompt enumerates allowed text and blanks
   all other surfaces. Composite lettering pass remains the exact-text end state.
Narrator v4 regenerated under both laws (job 3f50eba7…).
