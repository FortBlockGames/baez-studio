# TAKEOVER: THE MANGA — Series Plan

*The master plan for the manga series. Built from (a) the internal Takeover Lore
Bible and (b) a 5-analyst research study of top manga — art styles, serialization
economics, first-chapter hooks, game tie-in comics, and distribution (full
findings: `research/playbook.md`). Business goal: convert readers into Takeover
Conquest players.*

---

## The pitch
Year 2577. Five megacorps legally wage war over every commercial district on the
planet, and civilians are the scenery they fight in front of. But any citizen can
enlist a bot and pilot it into the war from their own room. **Rae Marlo — the best
arcade hands in District 12 — just lost everything to "acceptable collateral."
Now the war gets to meet the scenery.**

The manga's transformation scene IS the game ad: **piloting is the verb.**
"Even you, from your room, could fight back" is the pitch — every arc dramatizes
bot sorties, the exact thing players do in-game.

## Format (research-locked)
| Parameter | Decision | Basis |
| --- | --- | --- |
| Chapter 1 | **55 pages**, self-contained mini-movie | One Piece 54 / Demon Slayer ~55 / CSM ~54 / JJK 47 |
| Ongoing chapters | **18–22 pages, weekly** | WSJ standard; weekly feeds platform algorithms |
| Panels per page | 5–6 avg; 2–4 action; 6–8 dialogue; never 9+ | Jump page grammar |
| Master format | **B&W + faction spot color** (see treatment lock), paged, then vertical-scroll re-cut (~60 panels/ep) | Dark Horse × WEBTOON model + the lore's paint-scheme warfare |
| Splash pages | **One per chapter**, rationed | Jump rhythm: small setups → huge payoff |
| Buffer | Bank 6–8 chapters before public launch | cadence misses killed Halo: Uprising |
| Price | **Free, everywhere, always** | every paywalled web3 comic died |

## Art style bible (condensed — full prompt strings in `research/playbook.md` §1)
- **TREATMENT LOCK (owner-approved): B&W manga + faction SPOT COLOR — color appears
  ONLY on uniforms, gear, bot paint, faction emblems/banners/logos, and holographic
  glows. Faces, skin, and hair are ALWAYS pure monochrome ink + screentone.
  Backgrounds monochrome. Rationale: the Combat Standardization Mandate makes paint
  the only battlefield identity — spot color makes the war legible.**
- One line register forever: clean modern-Jump inking; rough line only inside impact panels; Berserk-density hatching reserved for megacorp dread moments.
- All gray is **screentone** (3 fixed tiers + solid spot blacks); standing negative prompt bans full-color/gradients/3D/painterly on every generation (spot color is whitelisted per the treatment lock).
- **Silhouette test is law**: every recurring pilot and faction bot reads as a filled black shape at 1cm — one value assignment + one signature prop each.
- Faction coding without color: corps = hard geometric silhouettes + heavy blacks; resistance = rounder improvised shapes + white space. One 1cm-survivable emblem per faction — reused as the game's faction icons.
- SFX hand-drawn, katakana-stroke styled; dialogue lettered in a separate pass (never trust generation for balloon text at scale).
- Chapter title pages are in-universe real estate: faction propaganda posters, bot spec sheets.

## Series architecture — ~150 chapters, 3 seasons
Factions enter **arc-by-arc through conflict, never exposition** — mirroring how
players meet them in-game. Each arc is a self-contained on-ramp (Riot
champion-comic model).

### SEASON 1 — "One District" (ch. 1–40, 4 volumes)
- **Arc 1 (ch. 1–9) — The Chickows Boot.** One protagonist (Rae), one district
  (Merica City D12), ONE corp **foregrounded** — **Chickows** (the most satirically
  legible boot: burger empire, "comfort food with teeth," General Chickow).
  Dollar Holler is unavoidably on-screen (Merica City is canonically Dollar Holler
  vs. Chickows, district by district) but stays antagonist-of-circumstance. Premise engine
  fully assembled by ch. 3; complete emotional mini-arc by ch. 9; ends with the
  District 12 takeover battle. Volume 1 = the playable-fantasy demo.
- **Arc 2 (ch. 10–24) — Water & The Gavel.** **Aquafeelya** (subscription
  rainfall, Captain "W") + first resistance faction fully onboarded: **PUF**
  (Joe Paradise, Commander Shen — reform vs. rage tension with Rae). Introduce
  the visible progression ladder: Basic/Prime editions and Soldier/Captain tiers
  are world canon; "pilot ranks" is product-layer progression (game UI canon, not
  world lore) shown as territory-map/rank infographics (Solo Leveling
  numbers-go-up engine, mapped 1:1 to game mechanics).
- **Arc 3 (ch. 25–40) — Edge.** **Vital Vibe** (Captain Dodge) + a rival
  citizen-pilot antagonist (corp-sponsored, chemically boosted). Season finale:
  a territory falls — mirrored by a live in-game event the same week.
  Board state at season end: 3/5 corps, 2/3 resistance (PUF + LoG teased via
  Skullface since ch. 1).

### SEASON 2 — "The Faction War" (ch. 41–95)
- **Digi-U arc** (Cyborgia, Cybersoldiers, the Digital Servitude Agreement),
  **Dollar Holler arc** (Dollar Bot 9000, the fall of Zone K-9 / Chrome Patty
  District), **Sentioids arc** (Captain PAT, electronic warfare, AI personhood).
  Full 5v3 board assembled entirely through battles.
- Mid-season: rotate a **corp-loyalist co-protagonist** POV (satirical dual
  perspective; an entry point for players who main megacorps).
- Arc spotlights double as **faction-population steering** for the game
  (underpopulated faction → next spotlight; the Dota "Davion effect").

### SEASON 3 — "The Takeover" (ch. 96–150)
- One earned mega-arc (Infinity Castle / Culling Game scale): the all-map war —
  **the Battle for Mount Profitmore** escalating into **Aethelburg's Grid**
  (Digi-U's MegaCity; Urthora has no capital in canon).
- **Pay off the two series-long mysteries WITHOUT arbitrating them** (lore bible
  Canon Governance: Contested Archive items are never resolved by studio voice —
  dramatize the competing versions, expand only the open hooks). End on emotional
  debt **the game repays**: the war explicitly unresolved, continued in-game
  (Edgerunners principle).

### The two long mysteries (question ledger)
- **M1 — The Eye of Novia:** what became of the first awakened AI, and what did
  she leave in the network? **Novia's fate is an official open hook** (expandable);
  the Great Spark's *cause* (awakening vs. "Network Integrity Failure") is
  Contested Archive and is dramatized both ways, never arbitrated.
- **M2 — The masked broadcaster:** a **distinct third figure** — never confirmed
  as Jinx (shelved canon) and never confirmed as The Wraith (Contested Archive).
  Both fan-theories stay live for the entire series; the broadcaster's identity
  ends the series still contested. That IS the ending, per Canon Governance.
- Plus: answer **one small question per chapter** (a bot spec, an emblem decoded,
  a rank explained) — each doubling as game-content marketing.

## Chapter 1 — status & upgrade path
- **v1 (SHIPPED):** 8-page pilot "Collateral" + cover — generated, in
  `chapters/ch01/` with reader page. Perfect weight for social distribution and
  as the proof-of-concept vertical slice. Honest gap vs. research: hit formula
  wants 55 pages.
- **v2 (NEXT MILESTONE):** expand to the research-locked 55-page beat sheet
  (`research/playbook.md` §4): misery-in-exact-numbers cold open (Rae's debt in
  corp scrip, to the credit) → want spoken aloud by p.5 → despair cycle →
  **witness beat** (a veteran pilot sees Rae's hands — the Shanks/All Might beat,
  currently missing from v1) → irreversible loss → first pilot run as the
  transformation climax (the chapter's one splash) → public vow → open door +
  faction emblem + "The takeover has begun. Pick your side."
  v1's 8 pages map to v2 beats nearly 1:1 — they become the skeleton, not waste.

## User-acquisition loop (per chapter)
1. **In-art CTA final panel** every chapter: faction emblem + "This district
   falls in-game this week. Pick your side." + link/QR.
2. **Landing pad rule:** every arc finale ships with a same-week in-game event
   (the manga's district contested in-game). Media heat without a landing pad
   churns (Arcane); with one, it converts (Edgerunners).
3. **Bidirectional payoffs:** manga pilots/bots become acquirable in-game
   (Collei effect); manga districts appear on playable maps (Afterlife-bar
   effect); chapter-embedded redemption codes reward readers in-game.
4. **Distribution stack (ranked in `research/playbook.md` §5):** WEBTOON Canvas +
   Tapas weekly (vertical re-cut) → panel-crop cliffhangers on X/Bluesky 3–5×/wk
   → game Discord/client drops → TikTok faction-propaganda edits → MANGA Plus
   Creators mirror → Reddit at arc milestones → Patreon early-access only after
   ~20 banked chapters.
5. **Expectation setting:** comics are slow-burn (Genshin seeded 2 yrs
   pre-launch; Solo Leveling ran ~6 yrs before ARISE harvested 15M
   pre-registrations). Pair arc finales with a video beat for spikes.

## Production pipeline (per chapter)
1. Beat sheet from this plan → panel script (`chapters/chNN/script.md`)
2. Character/bot refs locked from the OFFICIAL asset registry (`ASSETS.md`) —
   faction logos and established designs (e.g. McClaine) are embedded as
   Higgsfield reference elements, NEVER re-invented — plus Takeover Studio
   identity-from-references for the manga-original cast
3. Pages generated (Higgsfield, Nano Banana Pro, 2:3, ref-conditioned)
4. Lettering pass (balloon text typeset, never generated) — *pipeline TODO*
5. Paged master → vertical re-cut → reader page + platform exports
6. Job IDs logged in `generations.md`; art-direction QA against the style bible

## Top 10 commandments (from the research — full text in playbook §6)
1. Ch. 1 = 55-page self-contained mini-movie with the witness beat.
2. The transformation scene IS the game ad — sell the play fantasy, never the encyclopedia.
3. One line register + fixed screentone vocabulary, forever.
4. Everything passes the 1cm silhouette test.
5. Weekly, free, everywhere, never late.
6. Premise by ch. 3, complete arc by ch. 9, one faction per arc.
7. Cut one panel after the reveal; two giant mysteries run for years.
8. Every arc finale gets a same-week in-game landing pad + reader reward code.
9. Reading and playing pay each other (characters, maps, codes).
10. Platforms are the destination, socials are the engine.
