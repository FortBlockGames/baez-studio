# Official Asset Registry — Manga Pipeline
*Subordinate to `VISUAL-CONSISTENCY-STANDARD.md` (v1.3 mirror; AI-OS device copy is
source of truth). Where this file and the Standard disagree, the Standard wins.*

**Prime Law (from the Standard): identity is anchored (Elements), never prompted;
the look is a preset, never a paragraph; EXACT MARKS ARE COMPOSITED, NEVER GENERATED.**

## Title logo (official)
| Asset | Element name | Element ID | Use |
| --- | --- | --- | --- |
| TAKEOVER logo (blue, transparent) | `takeover-logo-blue` | `3a882097-1113-45df-8bab-38e2fcd6aa56` | transparent master — **composite** on covers/title pages |
| TAKEOVER logo (white, transparent) | `takeover-logo-white` | `c135d080-623f-4900-a601-bc5693a78771` | transparent master — **composite** on dark pages |

Source files: Drive folder `1K468n1HJTz5aFqMFUUwlkP1jK32Xh15R` (+ banner variants).
**Never hand-letter or model-generate the title. Hero placement = composite the PNG
in post over a blank plate (Standard §2). Element-embedding is ambient-grade only.**

## Faction logos (official)
Ambient use (weathered crest, background banner): embed `<<<element_id>>>`, accept drift.
**Hero use (readable banner, cover, anything a fan would screenshot): blank plate +
composite the source PNG (Standard §2).**

| Faction | Element name | Element ID |
| --- | --- | --- |
| Chickows | `chickow-logo` | `7b092aff-20e8-441e-a507-7b6db379763e` |
| Aquafeelya | `aqua-logo` | `d23d76cb-d454-4818-ad83-11e0a6046f5c` |
| Vital Vibe | `vital-vibe-logo` | `8913605f-23bd-4c0b-b197-d9f07c4739d3` |
| Digi-U | `digi-logo` | `e64b09c9-843b-40d8-ad49-871329ee6d18` |
| Dollar Holler | `dh-logo` | `8b219e28-296f-474d-be76-4f0c545c363a` |
| PUF | `puf-logo` | `609a0749-ac76-488f-bd9f-294b9483f420` |
| PUF (alt — canonical pick pending, Standard registry note) | `puf2-logo` | `a332662a-4096-4e25-9c08-c9370372705c` |
| Legion of Ghosts | `log-logo` | `23fec6b8-0076-436a-ae6d-6188cd94f687` |
| Sentioids | `sentioid-logo` | `1c0c0a7d-b3f2-4f08-ac17-0ce5dbc9af4b` |

## Characters & bots (Elements)
| Asset | Element name | Element ID | Notes |
| --- | --- | --- | --- |
| **Bots McClaine — realistic PFP** | `bots-mclaine` | `0e3f46dd-1df1-4ff1-83e3-a29fae9fbbdb` | cowboy-hat 3D render register |
| **Bots McClaine — anime** | `Bots-McClaine-Anime` | `076d353a-eec9-475a-a985-5190e88d2df6` | per Standard registry; *not visible in this workspace's element list — confirm workspace before use* |
| **Bots McClaine — manga** | *(to cut — pending founder approval of anchor)* | — | candidate anchor: model-sheet job `647d2808-e6d3-4c35-9e68-113f81c19464` (Standard §4A re-anchor flow) |
| BOT-Captain (generic archetype) | `BOT-Captain` | `998d1657-ce6a-4298-8b09-6a9c50101d79` | use for any Captain-grade unit in panels |
| BOT-SOLDIER (generic archetype) | `BOT-SOLDIER` | `bfd9815d-109c-486c-b950-f2e30bc88ae7` | use for any Soldier unit in panels; faction = color lock + composited logo |
| Rae Marlo — manga (original cast) | *(to cut — pending founder approval of anchor)* | — | candidate anchor: model-sheet job `4d19fbe2-e263-4a3a-b218-f041a1c27161`; until cut, pass the job ID as image reference |
| Rose / Patch / ELI / Papa / ma | per Standard registry | `698bdfa5…` / `58594ee9…` / `db34eda0…` / `389ed70f…` / `f9fd9298…` | team cast |
| red-soldier-01 / red-1 / big-boi / soldier2100PE | legacy | see Standard registry | reconcile vs Armory roster or retire |

### McClaine identity sheet (invariants — QA every render against these, any style)
- Silhouette: humanoid robot in a **fitted business suit + broad-brim cowboy hat**
- Signature: cowboy hat, ornate belt buckle, bolo/string tie, boots
- **HARD FACE RULE: sealed mouthplate — NO mouth, NO teeth, ever; glowing eyes**
- Color signature: tan/mustard suit, yellow tie (exact values pending)
- Emotion goes in body/camera, never the face. Restate the face rule in every prompt.
- **Narrator role (owner-locked):** all narration/host/recap/title-page appearances are
  McClaine, from the correct per-style Element (manga register once `McClaine-Manga` is cut).

## Environments (Elements)
| Environment | Element ID |
| --- | --- |
| main-st-town | `fe9373a8-24d4-4bb2-8123-9b7c56e71408` |
| Mall-EXT | `a2b82b82-9749-4cbb-a326-2c19b5534883` |
| plaza-01 | `7fecb8ac-fe7c-4c14-b8ee-817a18f64f94` |

## Treatment lock (owner-approved)
B&W manga + faction **spot color on uniforms/gear/bot paint/emblems/glows ONLY**.
Faces, skin, and hair are always pure monochrome. State the treatment in every prompt.
Faction colors are **locked exact values** (Standard: pull from `atlas/zones.js`) —
⚠ open canon question: zones.js values (e.g. Digi-U green `#16A34A`) differ from the
lore-bible brand palettes (Digi-U blue/chrome). Needs a founder canon pass; until then
the manga follows the lore-bible palettes it shipped with.

## Pipeline rules (Standard-conformant)
1. Recurring character ⇒ its per-style Element token in every prompt; describe only
   what changes (pose/setting/camera). Never re-describe identity.
2. New style for a hero asset ⇒ §4A re-anchor: seed candidate → identity-sheet check →
   founder approval → cut style Element (e.g. `McClaine-Manga`). Never mass-produce
   off an unapproved anchor.
3. Hero marks ⇒ blank plate + post composite of the transparent master. Ambient marks
   may use Element embeds. Speech/caption lettering: Nano Banana Pro + anti-garble
   negatives, or composite for guaranteed copy.
4. Fold the Standard's negative blocks (B1 base / B2 lettering / B3 portrait / mark-plate)
   into generations where the API allows; otherwise express as in-prompt prohibitions.
5. **Founder eyeball gate before anything ships** — the sandbox cannot see the CDN, so
   acceptance (Standard §10) happens in your browser/Higgsfield panel. No exceptions.
