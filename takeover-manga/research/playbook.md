# TAKEOVER: THE MANGA — SHOWRUNNER'S PLAYBOOK
*B&W manga series, year 2577, five megacorps vs. three resistance factions. Business goal: convert readers into Takeover Conquest players.*

---

## 1. ART STYLE BIBLE
Prompt-ready rules. Rules 1–13 govern every generated page; append the baseline style string and negative prompt to every generation.

1. **One line register, forever.** Clean modern-Jump inking (JJK/Naruto register): bold character outlines, finer interior lines, backgrounds finer still so figures pop. The ONLY sanctioned break: Fujimoto-rough sketchy line inside impact panels. Never Berserk-density hatching except megacorp villain reveals, where its oppressiveness is the point.
2. **All gray is screentone, never gradient.** Fixed 3-tier vocabulary: 10–30% dots (skin/light shadow), 40–60% (clothing/bot metal), 60–70%+ (skies/heavy shadow), plus solid spot blacks. Standing negative prompt on every generation: `color, photorealistic, 3D render, soft gradients, airbrushed shading, painterly, western comic style, gray digital painting`.
3. **Baseline positive string on every panel:** `black and white manga panel, Weekly Shonen Jump style, clean confident ink linework, bold character outlines with fine interior lines, screentone shading, halftone dot patterns, solid black spot fills, high contrast, white background`.
4. **Page grammar:** 5–6 panels average, 2–4 on action pages, 6–8 on dialogue pages, never 9+. Right-to-left, top-to-bottom, flow starts top-right; motion vectors lead left/down. Tall B5 ratio (~1:1.41). Horizontal gutters ~2x wider than vertical.
5. **Panel shapes are a code:** rectangles = neutral; tilted/diagonal = action; borderless = dream; wavy borders or black gutters = flashback; tachikiri full-bleed on the page's biggest panel = awe/scale (first bot reveal, corp tower looming).
6. **Ration splashes to one per chapter** (opener, first bot reveal, or climax hit). Build pages on the Jump rhythm: 2–3 small setup panels → one huge payoff panel at bottom-left or across the page turn.
7. **Action effects kit, used verbatim:** background deleted and replaced with speed lines for movement; radial focus lines for shock; white-burst or black-silhouette impact frames at the hit; ink spatter for force; then a crisp fully-rendered still for the finisher pose. Modifier string: `dynamic action panel, radial speed lines, impact frame, background replaced with speed lines, foreshortened pose, ink spatter, diagonal composition`.
8. **Silhouette test is law.** Every recurring pilot and every faction bot must be identifiable as a filled black shape at thumbnail size (the Oda rule). Each principal gets ONE value assignment (solid black / white / one fixed tone hair) and ONE signature prop readable at 1cm — the Takeover equivalents of Luffy's straw hat and Gojo's blindfold.
9. **Faction coding without color:** megacorps = hard geometric silhouettes, heavy solid blacks, dense mechanical hatching, angular logos; resistance = rounder improvised shapes, cloth textures, more white space. One simple emblem per faction (all 8), survivable at 1cm, reused on bots, covers, spines — these emblems are also the game's faction icons.
10. **Two characters in one panel must differ in value distribution** — black/white/tone masses never merge.
11. **SFX are hand-drawn art, not typeset:** English letters styled like katakana strokes ("GOOOM", "KRAK", "VRRRN"), size = volume, allowed to break panel borders. Keep the mimetic class (silence, dread) — it's the most manga-distinctive tool. Dialogue in tall elliptical balloons, typeset in a separate lettering pass — never trust AI to render balloon text.
12. **Consistency machinery:** per-character LoRA/image-reference conditioning; a fixed value sheet appended to every prompt; reading direction stated explicitly on multi-panel generations.
13. **Covers are the only color:** rotating character spotlight, fixed logo lockup in the top third, uniform trade dress, connecting spine art across volumes — each spine reveals another faction emblem/bot (collect-them-all = play-them-all).
14. **Chapter title pages are in-universe real estate:** faction propaganda posters, bot spec sheets, pilot pin-ups — B&W game-lore ads inside the book.
15. **Horror/corp-dread modifier:** `heavy crosshatching, dense black shadows, dark gradient screentone, oppressive atmosphere, low-angle shot` (Isayama register) — reserved for megacorp power moments so the visual language itself takes sides.

## 2. FORMAT

- **Chapter 1: 55 pages.** The proven debut weight class (One Piece 54, Demon Slayer ~55, Chainsaw Man ~54, JJK 47). Non-negotiable.
- **Ongoing chapters: 18–22 pages, weekly.** Pick weekly first — it dictates everything downstream, it's what WEBTOON's algorithm rewards (bi-weekly halves discovery surface), and an AI-assisted pipeline removes the human bottleneck that forces monthly.
- **Panels per page:** 5–6 average; 2–4 on action pages; 6–8 on dialogue; hard ceiling 9.
- **Master paged, ship both.** Master as B&W paged manga (print/PDF/MANGA Plus-ready, page-turn shock mechanics intact), then produce a vertical-scroll re-cut per the Dark Horse × WEBTOON 2025 model: ~60 panels per episode (up to 80 for action), one beat per screen, panels rebuilt for phone width — not stacked pages — every episode ending on a cliffhanger. Solo Leveling proved grayscale vertical-scroll converts.
- **Cadence is sacred.** Publishing delays killed Halo: Uprising's launch tie; team reboots killed the Assassin's Creed comics. Bank a 6–8 chapter buffer before launch and never miss a week.

## 3. SERIES ARCHITECTURE

Total plan: **~150 chapters across 3 seasons** — the modern sweet spot (Chainsaw Man Pt.1 = 97, AoT = 139, Demon Slayer = 205), not a 700-chapter legacy serial. Factions are introduced arc-by-arc through conflict, never exposition — mirroring how players meet them in-game. Each arc is a self-contained faction entry point (Riot champion-comic model) so any viral chapter is a clean on-ramp.

**SEASON 1 — "One District" (~40 chapters, 4 volumes)**
- **Arc 1 (ch. 1–9):** One protagonist, one district, ONE megacorp (recommend the fast-food corp — the most satirically legible boot). Premise engine fully assembled by ch. 3 (MHA speed). Complete emotional mini-arc lands inside the 10-chapter survival window; volume 1 (~190 pages) is the playable-fantasy demo. Ends with the district takeover battle — win a battle, reveal the war.
- **Arc 2 (ch. 10–24):** The water corp + first resistance faction fully onboarded. Introduce the visible progression ladder (pilot ranks, bot tiers, territory map).
- **Arc 3 (ch. 25–40):** Energy-drink corp; a rival citizen-pilot antagonist; season finale = a territory falls, mirrored by a live in-game event. Season 1 ends with 3 of 5 corps and 2 of 3 resistance factions on the board.

**SEASON 2 — "The Faction War" (~55 chapters, ch. 41–95)**
- Three arcs of 15–20 chapters: tech corp arc, big-box retail corp arc, third resistance faction arc (each arc = a spotlight designed to steer game faction population — the Dota Davion effect). Full 5v3 map assembled by end of season 2, entirely through battles.
- Mid-season: rotate a co-protagonist from a corp-loyalist POV (satirical dual-perspective; also an entry point for players who main megacorps).

**SEASON 3 — "The Takeover" (~50–60 chapters, ch. 96–150)**
- One earned mega-arc of 40–50 chapters (Infinity Castle = 47, Culling Game = 63 scale): the全-map war for the capital grid. Answer the two series-long mysteries. End on emotional debt the game repays — the war explicitly unresolved, continued in-game (Edgerunners' tragedy-the-game-answers principle).

## 4. CHAPTER 1 HOOK FORMULA
55 pages, self-contained mini-movie that happens to continue. State-change every 4–6 pages; three despair↓/hope↑ cycles; transformation in the final 20%.

- **Pages 1–4 — Cold open, CSM-style misery-in-exact-numbers.** One citizen in 2577 crushed by ONE megacorp: rent auto-debited in corp scrip, oxygen/compute rations, a debt figure to the yen (Chainsaw Man's 38,040,000¥ move). Entire world premise legible in ≤4 pages, through the protagonist's day, zero narration dumps. The other 7 factions do not appear.
- **Pages 5–8 — Want stated aloud.** The protagonist says what they want (spoken, ≤ page 5 territory — "Pirate King" rule). Wound dramatized in a scene, never narrated. The want-wound gap is the series promise.
- **Pages 9–20 — Despair cycle 1 + world texture.** Corp enforcement bots in the streets; citizens glued to pilot-feeds; the tantalizing fact planted: *any citizen can remotely pilot a standardized combat bot.* Plant the unexplained mystery image (AoT "To You, 2,000 Years From Now" move) for a 100-chapter payoff.
- **Pages 21–30 — Hope: the witness beat.** A veteran resistance pilot sees something in the nobody — the Shanks/Iruka/All Might/Pochita beat, the most-cited emotional payoff in every great ch. 1. This is also the reader's permission slip: "even you could pilot."
- **Pages 31–38 — Despair cycle 2: the corp takes something irreversible.** Home, sibling, district — page-1 status quo destroyed AoT-style (mother-under-the-rubble weight class).
- **Pages 39–48 — TRANSFORMATION: first bot-piloting run.** Piloting is the game's core verb, so this scene IS the ad. Stage it as the CSM revenge-transformation: full effects kit, the chapter's one splash page on the bot reveal. Show the power's EFFECT and COST (neural strain, traceable signal, a defenseless body left in a rented room) — never its rules (mystery box + Sanderson's First Law).
- **Pages 49–53 — Payoff still + vow.** Crisp finisher pose. Public vow (One Piece "I'll be King of the Pirates" move) against the corp.
- **Pages 54–55 — Open door.** The resistance's hand extended + a doom/mystery final page. Cut one panel AFTER the reveal, never after the resolution. Last panel: faction emblem + "The takeover has begun. Pick your side." → game link.

## 5. USER-ACQUISITION MECHANICS

**Per-chapter conversion loop:**
- **End-of-chapter CTA on every episode:** in-art final panel + QR/link — "This district falls in-game this week. Choose your faction." The CTA replaces the paywall in the Jump funnel: everything free, everywhere, always (every gated web3 comic — Punks Comic, Jenkins the Valet, Azuki — died; Azuki's only win was its *free* anime short).
- **Question ledger:** answer one small question per chapter (a new bot spec, a faction emblem decoded, a rank explained); keep 2 giant mysteries open for years. Each faction reveal doubles as game-content marketing.
- **Visible progression system** on the page: pilot ranks, bot tiers, territory-control maps as recurring in-art infographics — Solo Leveling's numbers-go-up engine, mapping 1:1 onto game mechanics.
- **Sell the play fantasy, not the encyclopedia.** Every arc dramatizes bot sorties — what players actually DO. Dragon's Blood S1 flopped for UA because watching it resembled nothing about playing Dota.
- **Bidirectional payoffs (Collei effect):** manga pilots and bots become acquirable in-game; manga locations appear on playable maps (Edgerunners' Afterlife-bar effect); chapter-embedded redemption codes reward readers in-game (WEBTOON × PlayStation reciprocal model).
- **Landing pad rule:** every arc finale ships with a same-week in-game event (the manga's district contested in-game). Arcane proved media heat with no landing pad — and a hostile first hour — just churns; the comic fills the funnel, the game's first hour converts it.
- **Steering, not just acquiring:** spotlight whichever faction is underpopulated in-game — featured units reliably see pick-rate boosts (Dota's Davion).

**Distribution tactics, ranked (effort vs. impact):**
1. Free weekly serialization on WEBTOON Canvas + Tapas simultaneously (vertical re-cut), same files both platforms.
2. Native 1–4 panel cliffhanger crops on X AND Bluesky (where the comics community migrated), 3–5×/week; read-link in the reply, never the post.
3. End-of-chapter game CTA + chapter drops in the game's Discord/client/patch notes — the pre-seeded audience is free.
4. TikTok/Reels/Shorts 2–3×/week: panel-motion edits with VO, timelapses, 60s+ faction-propaganda lore edits (#comictok, #manga) — the premise is natively short-video-shaped ("which faction are you").
5. Discord 24h-early drops, faction reaction channels, manga events synced to in-game takeovers.
6. Reddit (r/manga OC, r/webtoons) at arc milestones only, best pages only.
7. Mirror on MANGA Plus Creators — B&W-paged-native audience, Jump+ editorial visibility, near-zero extra effort.
8. Seed manga-rec TikTok/YouTube accounts once 10+ chapters exist.
9. Patreon rolling early-access after ~20 banked chapters (revenue, not reach — never gate early).
10. Print vol. 1 Kickstarter only after digital traction.

**Expectation setting:** comics are a slow-burn audience builder (Genshin seeded its manga 2 years pre-launch; Solo Leveling serialized ~6 years before ARISE harvested 15M pre-registrations). Pair arc finales with an anime/video beat for Edgerunners-style spikes (+300% concurrents).

## 6. TOP 10 COMMANDMENTS

1. Chapter 1 is a 55-page self-contained mini-movie — misery in exact numbers, want spoken aloud, witness beat, first pilot run as climax, status quo irreversibly destroyed (One Piece/CSM/AoT formula).
2. The manga's transformation scene IS the game ad: piloting is the verb, "even you, from your room, could fight back" is the pitch — sell the play fantasy, never the encyclopedia (Dragon's Blood's fatal error).
3. One clean-Jump line register and a fixed 3-tier screentone vocabulary forever; rough line only inside impact panels; negative-prompt gradients and color on every generation.
4. Every character and bot passes the silhouette test at 1cm — one value, one prop, one faction emblem (the Oda rule).
5. Weekly, free, everywhere, never late — cadence misses (Halo: Uprising) and paywalls (every web3 comic) kill the funnel dead.
6. Premise engine by ch. 3, complete emotional arc by ch. 9, one faction per arc thereafter — never tour all eight factions in exposition.
7. Cut every chapter one panel after the reveal, put shocks after the page turn, and answer one small question per chapter while two giant mysteries run for years.
8. Every arc finale gets a same-week in-game landing pad and a reader reward code — or you're making Arcane, not Edgerunners.
9. Make reading and playing pay each other: manga characters acquirable in-game (Collei), manga districts on playable maps (Afterlife bar), spotlight underpopulated factions (Davion).
10. Platforms are the destination, socials are the engine: master in pages, re-cut vertical, and let daily panel crops and faction-propaganda TikToks do the acquiring.