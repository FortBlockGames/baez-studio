# Official Asset Registry — USE THESE, DO NOT INVENT

**Rule: never invent a logo, emblem, or established character design. Every
generation that shows faction branding or an existing character MUST reference
the official assets below** (Higgsfield reference elements — embed as
`<<<element_id>>>` inside the prompt; works with Nano Banana Pro/2, GPT Image 2,
Seedream, Kling, Cinema Studio).

## Title logo (official — MANDATORY on covers/title pages)
| Asset | Element name | Element ID |
| --- | --- | --- |
| TAKEOVER logo (blue, transparent) | `takeover-logo-blue` | `3a882097-1113-45df-8bab-38e2fcd6aa56` |
| TAKEOVER logo (white, transparent) | `takeover-logo-white` | `c135d080-623f-4900-a601-bc5693a78771` |

Source of truth: Drive folder `1K468n1HJTz5aFqMFUUwlkP1jK32Xh15R` (also holds blue/white
banner variants). Never hand-letter the title — embed one of these elements with the
"reproduce exactly, do not re-letter" rule.

## Faction logos (official)
| Faction | Element name | Element ID |
| --- | --- | --- |
| Chickows | `chickow-logo` | `7b092aff-20e8-441e-a507-7b6db379763e` |
| Aquafeelya | `aqua-logo` | `d23d76cb-d454-4818-ad83-11e0a6046f5c` |
| Vital Vibe | `vital-vibe-logo` | `8913605f-23bd-4c0b-b197-d9f07c4739d3` |
| Digi-U | `digi-logo` | `e64b09c9-843b-40d8-ad49-871329ee6d18` |
| Dollar Holler | `dh-logo` | `8b219e28-296f-474d-be76-4f0c545c363a` |
| PUF | `puf-logo` | `609a0749-ac76-488f-bd9f-294b9483f420` |
| PUF (alt) | `puf2-logo` | `a332662a-4096-4e25-9c08-c9370372705c` |
| Legion of Ghosts | `log-logo` | `23fec6b8-0076-436a-ae6d-6188cd94f687` |
| Sentioids | `sentioid-logo` | `1c0c0a7d-b3f2-4f08-ac17-0ce5dbc9af4b` |

## Established characters & bots (official designs)
| Asset | Element name | Element ID |
| --- | --- | --- |
| **McClaine (the bot — official design)** | `bots-mclaine` | `0e3f46dd-1df1-4ff1-83e3-a29fae9fbbdb` |
| Red Soldier bot | `red-soldier-01` | `2af746db-9899-4e1c-b11e-e70ca2ee7a88` |
| Red bot (alt) | `red-1` | `193dcbd6-6e22-4ef3-ae0f-3a4686aa2dc5` |
| Big Boi (bot) | `big-boi` | `c8407545-56d0-44bb-8b23-e8514df6c7f3` |
| Soldier 2100 PE (era design) | `soldier2100PE` | `e1908f76-44f6-413c-8f34-673df804fa3e` |
| Rose | `Rose` | `698bdfa5-decb-4923-a5ef-a040e693f4bc` |
| Patch | `Patch` | `58594ee9-23d4-44d1-acf5-9fe1ff197f56` |
| Papa | `Papa` | `389ed70f-586c-4a6b-b633-a83661ebc7e7` |
| ma | `ma` | `f9fd9298-930c-4a3b-b924-dea555d014a7` |
| ELI | `ELI` | `db34eda0-7d00-41f5-beae-18963bbc772f` |

## Environments (official)
| Asset | Element name | Element ID |
| --- | --- | --- |
| Main St. town | `main-st-town` | `fe9373a8-24d4-4bb2-8123-9b7c56e71408` |
| Mall exterior | `Mall-EXT` | `a2b82b82-9749-4cbb-a326-2c19b5534883` |
| Plaza | `plaza-01` | `7fecb8ac-fe7c-4c14-b8ee-817a18f64f94` |

## Manga-original references (generated, reusable as job-ID refs)
| Asset | Type | Job ID |
| --- | --- | --- |
| Rae Marlo — design model sheet | image job | `4d19fbe2-e263-4a3a-b218-f041a1c27161` |

## Usage rules
1. Faction banners/emblems/paint: embed the faction's `<<<element_id>>>` in the prompt.
2. McClaine appearances: ALWAYS embed `<<<0e3f46dd-1df1-4ff1-83e3-a29fae9fbbdb>>>` — never re-invent the design.
   **McClaine is the series' recurring NARRATOR/HOST (owner-locked):** every narration
   role — chapter openers/recaps, title pages, fourth-wall host panels, "previously on"
   frames, promo voiceover visuals — is fronted by McClaine rendered from this element,
   with "reproduce the design exactly, do not redesign" stated in the prompt.
3. Rae appearances: pass the model-sheet job ID as an image reference.
4. New recurring characters: generate a model sheet once, save it as a reference
   element in Higgsfield, add it to this table, then reference it everywhere.
5. When both an element and a text description conflict, the element (official art) wins.

## Treatment lock (owner-approved)
B&W manga + faction **spot color on uniforms/gear/bot paint/emblems/glows ONLY**.
Faces, skin, and hair are always pure monochrome. Every generation prompt must
state this treatment explicitly.
