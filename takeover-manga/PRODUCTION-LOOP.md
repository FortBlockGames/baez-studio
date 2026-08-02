# TAKEOVER Manga — Production Loop Specification

*A build spec for tooling the comic pipeline. Written from what actually happened producing
Chapter 1 (10 plates) and Chapter 2 (20 plates) by hand, including every defect that reached
the founder's eye and what fixed it.*

**Audience:** whoever builds the production tool.
**Governing docs:** `VISUAL-CONSISTENCY-STANDARD.md` (Prime Law) → `ASSETS.md` (registry) →
`CANON-ADDITIONS.md` (approved inventions) → `SERIES-PLAN.md` (format) → `QA-GATE.md`.
Where this spec and the Standard disagree, the Standard wins.

---

## 0. The one-paragraph summary

A page is **not** "a good image." A page is a *contract*: correct characters from locked
Elements, correct faction colours to the hex, correct marks composited from real files,
zero generated text, zero blank boxes, dialogue in narrative order, and no fact that the
game build could later contradict. The generator satisfies roughly 70% of that contract on
the first try. **The entire value of the tool is mechanising the other 30%** — which is
detection, compositing, lettering and verification, not image generation.

---

## 1. Definition of done (a page is shippable when all pass)

| # | Gate | Automatable? |
|---|---|---|
| 1 | Every recurring character came from its registered Element token | ✅ enforce at prompt build |
| 2 | No text anywhere in the art except deliberately art-baked in-world signage | ✅ OCR |
| 3 | No element-token leak (`@Name` printed into the image) | ✅ OCR |
| 4 | No blank/empty white boxes, panels or screens | ✅ CV |
| 5 | Faction colours match the locked hex; **no colour on skin/faces/hair** | ✅ CV |
| 6 | Every faction mark is composited from the official file, never drawn | ✅ pipeline-enforced |
| 7 | Marks are centred on their surface and correctly occluded | ✅ CV + bake |
| 8 | No numerals printed anywhere (art or lettering) | ✅ OCR |
| 9 | Balloons in narrative reading order, ≤ caps, covering no face | ⚠️ semi — layout check + eyeball |
| 10 | Beat matches the approved script; no lore violation | ❌ human / lore-guard agent |
| 11 | Founder eyeball | ❌ never automate |

Gates 1–8 are hard-fail and should block the pipeline. 9 warns. 10–11 are review.

---

## 2. Invariant laws (hard-code these; they are earned, not stylistic)

### L1 — Identity is anchored, never described
Recurring characters **must** be embedded as `<<<element_uuid>>>` tokens. Never re-describe a
character's identity in prose. Describe only what changes: pose, camera, setting, lighting.
*Why:* prose descriptions drift page to page; Elements don't.

### L2 — Exact marks are composited, never generated
Every faction logo, the TAKEOVER wordmark, every brand emblem is a **transparent PNG baked in
post**. The prompt must instead request a **blank plate**: "a plain flat red disc with no
design, no emblem, no letters," or "banner valance completely blank."
*Why:* the generator hallucinates plausible-but-wrong marks 100% of the time. We shipped a
fake "V" for Vital Vibe before catching it.
**Corollary:** never put a `<<<*-logo>>>` Element token in a prompt — it prints the literal
string `@dh-logo` into the artwork.

### L3 — Separated lettering
Dialogue is **never** generated into art. Pages are textless plates; balloons are an HTML
overlay authored by a human.
*Why:* generated balloon text garbles at scale, can't be edited, and can't be localised.

### L4 — Never reserve space (counterintuitive; costly to learn)
Do **not** write "leave open space for captions." That instruction is what *causes* empty
white boxes to appear in the artwork. Always demand **"FULLY DETAILED edge to edge, NO blank
boxes, NO empty panels, NO reserved space."**
*Why:* overlay balloons are opaque and sit on top of finished art. Reserved space is never
needed and always backfires. This single line eliminated an entire defect class.

### L5 — No numerals, ever
No CP value, price, ratio, count or date appears in art or lettering. Quantities are drawn
as **wordless notch-ladders, ring segments, chevrons, lit/unlit cells**.
*Why:* the game's economy tuning is live product canon. A printed number in a shipped comic
becomes a contradiction the moment the build changes. This also produced the best page in
Chapter 2 (P2's two ladders, one running off the edge).

### L6 — Treatment lock
B&W ink + halftone screentone. Faction **spot colour only** on uniforms, gear, bot paint,
emblems, banners, holographic glows. **Faces, skin and hair are always pure monochrome.**
State the treatment *and* the specific hex in every prompt.

### L7 — Colour is law, not vibe
Pass exact hex values. Faction locks live in `ASSETS.md`. Watch adjacency collisions:
Vital Vibe accent `#FF7849` vs Legion of Ghosts `#FF7A1A` are near-identical — a page mixing
them must be hex-checked or it reads as the wrong faction.

### L8 — Narrator containment
McClaine is the series narrator/host. He appears **in person only on narrator/title plates**.
His voice may carry a flavoured caption elsewhere. Putting him in a scene is a lore break —
we shipped one and had to regenerate the page.

---

## 3. Pipeline stages

```
 (1) OUTLINE ──▶ (2) SCRIPT ──▶ (3) ANCHOR ──▶ (4) GENERATE ──▶ (5) AUTO-QA
                     │                                              │
                     │                                    fail ─────┘
                     ▼                                    (regenerate w/ hardened negatives)
              (6) COMPOSITE MARKS ──▶ (7) LETTER ──▶ (8) VERIFY ──▶ (9) SHIP
```

### (1) Outline
**In:** `SERIES-PLAN.md` arc requirements + `lore-master.txt` + previous chapter's open threads.
**Out:** `chapters/chNN/OUTLINE.md` — page-by-page beats with panel counts, a canon-anchor
table, an invented-items queue, and explicit founder decision points.
**Tool role:** template + a lore-grep helper that surfaces relevant bible sections for the
chapter's subject. Founder approves before scripting.

### (2) Script
**In:** approved outline, full lore bible, previous chapter's voice guide.
**Out:** `chapters/chNN/script.md` containing, per plate:
- panel-by-panel **art direction** (concrete enough to compile into a prompt)
- **final lettering** table: item #, type, speaker, exact line
- flags: which surfaces are blank plates awaiting composite; which lines need a special style

Plus: voice-guide delta, **canon audit table** (every proper noun → bible citation), and the
invented-but-benign log.
**Tool role:** enforce lettering caps (captions ≤12 words, balloons ≤14, 3–6 items/page),
run the lore-guard and text-guard agents, and refuse to advance if the canon audit has gaps.

### (3) Anchor
Any new recurring character/prop needs an Element **cut and founder-approved before** it
appears on a page. Generate 3–4 concept variants → founder picks → register via Elements API
→ append invariants to `ASSETS.md`.
**Tool role:** the concept→pick→register→document flow as one command. Block generation of
any page whose script references an unregistered character.

### (4) Generate
One prompt per plate, compiled from the script (see §4). 1–2 variants for ordinary pages,
3–4 for hero pages (covers, splashes, reveals) and anything with a hard countable
requirement.
**Tool role:** prompt compiler + batch submit + poll + fetch.

### (5) Auto-QA
See §5. Hard-fail gates re-enter generation with **hardened negatives specific to the defect
found** — not a blind retry.

### (6) Composite marks
CV-detect the target surface → bake the official PNG with correct scale, rotation and
occlusion. See §6.

### (7) Letter
Emit the reader HTML with the overlay balloon layer. See §7.

### (8) Verify
Headless render each page at reading width, screenshot, assemble contact sheets for founder
eyeball. See §8.

### (9) Ship
Commit plates + script + reader; push; produce a **commit-pinned** githack URL so the review
link can never drift.

---

## 4. Prompt construction spec

A page prompt is assembled from six blocks, always in this order. This structure was arrived
at empirically; deviating from it reintroduces defects.

```
[1 FORMAT]   Vertical manga page, N panels, black-and-white ink with halftone
             screentone, <spot colour summary>.

[2 SCENE]    <one clause of setting>

[3 PANELS]   PANEL 1: <camera> — <staging>. PANEL 2: ...
             • Element tokens inline exactly where the character appears
             • Describe only pose/camera/lighting for anchored characters
             • Every surface destined for a composited mark is declared BLANK

[4 TREATMENT] TREATMENT: black-and-white manga; spot colour ONLY on <explicit list>;
              faces, skin and hair pure monochrome.

[5 NEGATIVES] FULLY DETAILED edge to edge — NO blank white boxes, NO empty panels,
              NO empty screens, NO speech balloons, NO caption boxes, ZERO letters,
              words or numerals anywhere.

[6 CAMERA]    <optional> Cinematic low angle. / Explosive. / Contemplative.
```

**Generation params (current):** model `nano_banana_2`, `aspect_ratio` `2:3`, `resolution`
`2k`, `count` 1–4. Character sheets use `3:4`.

**Hardened-negative variants** — apply the one matching the observed defect, not all of them:

| Defect seen | Add to block [5] |
|---|---|
| Stray words on signage | `CRITICAL: this image must contain ZERO WRITING. Every sign, rail, placard, label and screen is COMPLETELY BLANK — no letters, no words, no numbers, no logos, no symbols.` |
| Blank boxes | `FULLY DETAILED finished art — every screen shows detailed UI; there are NO blank panels, NO empty boxes, NO reserved space.` |
| Wrong count (e.g. 7 banners not 8) | `there must be EXACTLY EIGHT — count them one-two-three-four-five-six-seven-eight, NOT seven and NOT nine` |
| Colour drift | `the cores must be ORANGE, never red. NO red anywhere.` |
| Colour on skin | `PURE MONOCHROME on all people — absolutely no colour on skin, faces, hair or plating.` |
| Off-lore character present | `and NO cowboy-hat businessman robot in the scene.` |

---

## 5. Defect taxonomy — every failure that reached review, with its automated check

| ID | Defect | Detection | Action |
|---|---|---|---|
| D1 | **Stray in-art text** ("VICTORY", "PRICE", "DEAD ARCADE") | OCR the plate; allow-list approved in-world signage per page from the script | Regenerate with zero-writing negative |
| D2 | **Element-token leak** (`@Rae-Manga` printed in art) | OCR for `@` + any registered Element name | Always regenerate — unfixable in post |
| D3 | **Blank boxes** | CV: find large near-uniform white regions with hard rectangular borders not adjacent to a panel gutter | Regenerate with L4 negative |
| D4 | **Colour on skin/face/hair** | Detect face/skin regions; assert saturation below threshold | Regenerate; usually recoverable by restating treatment |
| D5 | **Wrong faction hex** | Cluster saturated pixels; nearest-match against the lock table; flag if distance > tolerance or if a faction is present that shouldn't be on this page | Regenerate with explicit colour negative |
| D6 | **Hallucinated mark** | Any logo-like glyph inside a region the script declared a blank plate | Regenerate as blank plate, then composite |
| D7 | **Wrong element count** | Count via the domain detector (see §6.1) and compare to script | Regenerate; use `count:3` and select |
| D8 | **Mark off-centre** | Post-bake: recompute surface centre, assert mark centroid within tolerance | Re-bake (cheap — no regeneration) |
| D9 | **Occlusion error** (mark floating over a finger that should be in front) | Manual/visual; mitigated by always running the occlusion-restore path | Re-bake |
| D10 | **Lore violation** (narrator in-scene, wrong doctrine) | lore-guard agent on the script *before* generation | Rewrite beat, regenerate |
| D11 | **Reading order scrambled** | Layout lint: item order in the reader array vs. narrative order in the script | Re-letter (free) |
| D12 | **Dropped story beat** on regeneration | Diff regenerated page's art direction against script beat function | Regenerate to the script |
| D13 | **Printed numeral** | OCR for digits | Regenerate with L5 negative |

**Observed base rates** (Ch.1–2, ~45 generations): D1 ≈ 1 in 6 plates · D3 ≈ 1 in 8 (before
L4 was adopted; ~0 after) · D5 ≈ 1 in 10 · D2 ≈ 1 in 20 · D7 on any page with a hard count.
**Budget 1.4–1.6 generations per shipped plate.**

---

## 6. Mark compositing — the algorithms that actually worked

This is the highest-value part to automate; it took the most iterations to get right and it
is fully deterministic once correct.

### 6.1 Surface detection (pick by surface type)

**Banner/ribbon rows — use the background-gap method.**
Naive approaches failed repeatedly. What works: sample a horizontal band at the mark's
intended height, classify columns as background (page cream, brightness > threshold) vs.
not, take runs of non-background wider than ~4% of image width — those runs are the banners.
Centre each mark on its run's midpoint.
*Failure modes this fixes:* whole-object centroids drift on leaning/tapering banners; dark
banners defeat brightness thresholds; page margins pull the outermost banners outward. The
gap method solved the outer-banner drift that survived two earlier attempts.

**Tilted cards/passports:** threshold to the bright card face → `cv2.minAreaRect` → gives
centre, size **and angle**; rotate the mark to match.

**Glowing screens/wrist displays:** bright-region detection inside a tight ROI, with a
smoothness filter to reject line-shaded background.

**Round stamps/discs:** connected components on the colour mask, filtered by aspect ratio
0.7–1.4 and minimum area; take the largest.

### 6.2 Mark preparation
**Always auto-trim the PNG to its alpha bounding box before scaling.** Source logo files have
asymmetric transparent padding; centring the *file* instead of the *artwork* produces marks
that look off-centre even when the maths is right. This was a real shipped defect.

### 6.3 Placement
Scale to fit a box (min of width/height ratio, never stretch), rotate to the detected angle,
composite onto a full-size transparent layer, then `alpha_composite` onto the plate.

### 6.4 Occlusion — the "always do it properly" rule
When something in the scene should sit *in front* of the mark (a finger over a card):

1. Snapshot the plate before compositing.
2. Composite the mark.
3. Rebuild a mask of the true target surface (e.g. clean bright card face, largest connected
   component in the bbox, dilated).
4. **Restore original pixels everywhere in the bbox that is not the target surface.**

Masking the mark to a colour range alone is insufficient — a light-skinned finger and a white
card are both bright. The restore-from-snapshot approach is the correct general solution and
should be the only path the tool implements. No shortcuts.

---

## 7. Lettering system spec

Overlay balloons on finished art, positioned in **percentages** so they scale with the image.

### Data model
```js
{ lbl:'PAGE 15 · WHO HOLDS THE PAPER', img:'pages/p15.png', items:[
  { k:'bub'|'cap'|'sfx'|'name',
    t:'LINE TEXT',
    cx:74, cy:26,        // % of width/height, centre-anchored
    mw:26,               // max-width %
    tail:'dl'|'dr'|'ul'|'ur',   // omit for tailless
    cls:'brand'|'teal'|'sys'|'log' }  // voice style
]}
```

### Voice styles (each must be visually distinguishable at a glance)
| Class | Voice | Treatment |
|---|---|---|
| *(default)* `bub` | human speech | white oval, black stroke, tail |
| `cap` | narration | white rectangle, no tail |
| `cap.sys` | machine/institutional | dark hairline box, cool grey text, **never prints a number** |
| `bub.brand` | corporate advertising | scalloped, tailless, brand-tinted, ~8% larger than the human balloon beside it |
| `bub.teal` | a different corp's brand voice | same shape, that faction's hex |
| `cap.log` | pirate/resistance broadcast | dark box, dashed faction-orange border |
| `sfx` | sound | outlined display type, rotated, no container |

*Why tailless for brand voice:* it's a broadcast, not a person speaking. Readers parse it as
ambient corporate noise instantly.

### Rules the linter should enforce
- Captions ≤ 12 words; balloons ≤ 14; 3–6 items per page.
- Item array order **must** equal narrative reading order (this is what fixes D11).
- Tail direction must point toward the speaker's side of the frame.
- No item's box may overlap a detected face region.
- All-caps display.

---

## 8. Verification

Headless Chromium (`/opt/pw-browsers/chromium`, `playwright` from the global node modules)
loads the reader, scrolls each `.stage` into view, screenshots it, and the tool assembles
**contact sheets of 3–4 pages** for founder review.

Reviewing pages individually is a waste of the founder's attention; reviewing them as a
sequence is also how reading-order and pacing problems become visible. Always present as a
run of pages.

---

## 9. Repo data model

```
takeover-manga/
├── lore-master.txt              # source of truth (owner-owned; tool reads, never writes)
├── ASSETS.md                    # Element registry + colour locks + identity sheets
├── CANON-ADDITIONS.md           # manga-invented canon + founder status
├── SERIES-PLAN.md               # arc architecture + format law
├── VISUAL-CONSISTENCY-STANDARD.md
├── QA-GATE.md
├── PRODUCTION-LOOP.md           # this file
├── tools/                       # detect/composite scripts
└── chapters/chNN/
    ├── OUTLINE.md
    ├── script.md                # art direction + lettering + canon audit
    ├── index.html               # reader (art + overlay lettering)
    ├── PLATES.md                # plate manifest w/ job IDs
    └── pages/*.png
```

**Asset access note:** the generation CDN is blocked by network policy in the build
environment. Rendered images are retrieved through a locked-down relay (allow-listed to the
one CDN host and a strict filename pattern) that returns base64. Any tool must budget for
this hop; direct CDN fetches fail with a proxy 403.

---

## 10. Proposed tool surface

```
manga outline   chNN                 # scaffold + lore-grep helper
manga script    chNN                 # lint caps, run lore/text guards, canon-audit check
manga anchor    "Name" --concepts 4  # generate → pick → register Element → write ASSETS.md
manga gen       chNN --pages 1-10 [--variants 2]
manga qa        chNN [--fix]         # D1-D13; --fix re-generates with matched negatives
manga bake      chNN                 # detect surfaces → composite marks → verify centring
manga letter    chNN                 # emit reader from script lettering tables
manga verify    chNN                 # headless render → contact sheets
manga ship      chNN                 # commit, push, print commit-pinned review URL
manga run       chNN                 # the whole loop, halting at founder gates
```

**Config:** `manga.config.json` holding model/aspect/resolution, the colour lock table,
Element ID map, lettering caps, and per-page allow-listed in-world signage.

### Automation boundary — do not cross
Automate: prompt assembly, batching, fetching, OCR/CV QA, mark detection and baking,
lettering emission, rendering, contact sheets, committing, link generation.

**Never automate:** the founder eyeball gate, approval of a new character Element, approval
of a new canon mechanic, or the decision that a page "reads." Every serious defect this
project shipped was caught by a human looking at the page — 7 banners instead of 8, a
hallucinated logo, a lore-broken narrator, a dropped story beat. The tool's job is to make
that review *fast and rare*, not to replace it.

---

## 11. Cost & throughput (measured)

- ~1.4–1.6 generations per shipped plate including QA regenerations.
- A 20-plate chapter ≈ 30–35 generations end-to-end.
- Dominant human time is **not** generation — it is reviewing and re-prompting. Automating
  §5 and §6 is where the tool pays for itself.
- Hero plates (cover, splash, reveal) deserve 3–4 variants; ordinary pages 1–2.

## 12. Adoption order (highest ROI first)

1. **Prompt compiler + negative library** (§4) — removes most defects at the source.
2. **Auto-QA D1/D2/D13 via OCR** (§5) — catches the embarrassing, shippable-looking bugs.
3. **Mark compositing** (§6) — deterministic, fiddly, and the single biggest source of
   founder-visible rework.
4. **Lettering emitter + order linter** (§7).
5. **Render + contact sheets** (§8).
6. Outline/script scaffolding and the guard agents.
