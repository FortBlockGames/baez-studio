# Per-Page QA Gate — mandatory pipeline
*No page is generated, and no render ships, without passing these gates in order.
Agents live in `.claude/agents/` (`lore-guard`, `consistency-guard`) — spawn them
per page or per batch; a FAIL verdict blocks the step it guards.*

```
 script/captions ──► [GATE 1: lore-guard] ──► generation prompt
                                                  │
                              [GATE 2: consistency-guard (prompt audit)]
                                                  │ PASS
                                              generate
                                                  │
                              [GATE 3: consistency-guard emits the
                               FOUNDER EYEBALL CHECKLIST for the render]
                                                  │
                     [GATE 4: founder eyeball in browser/Higgsfield panel
                      — Standard §10; sandbox cannot see the CDN]
                                                  │ PASS
                                         page enters the reader
```

## Gate rules
1. **Gate 1 — Lore.** `lore-guard` audits the page's script, captions, and dialogue
   against `lore-master.txt`. Any VIOLATION = rewrite before prompting.
2. **Gate 2 — Prompt.** `consistency-guard` audits the assembled generation prompt
   against the Standard + registry: anchored Elements (right per-style IDs), McClaine
   face-rule guardrail, hero marks as blank plates (composite in post — never
   generated), exact faction color locks, treatment lock, negatives. FAIL = fix the
   prompt, never "generate and hope."
3. **Gate 3 — Checklist.** The same agent outputs the founder eyeball checklist
   specific to that page (which invariants, which marks, which colors to verify).
4. **Gate 4 — Founder eyeball.** The only gate a human must click through — by
   design (Standard §1.4/§10). A render that fails is re-anchored or re-generated;
   its replacement re-enters at Gate 2.

## Batch mode
For a chapter batch, run Gate 1 once over the whole script, Gate 2 per prompt
(agents may be spawned in parallel, one per page), and deliver a single merged
eyeball checklist ordered by page.

## Non-negotiables the gates enforce
- Logos/wordmarks: pixel-exact = composited masters only (`ASSETS.md` title-logo +
  faction tables). Element-embeds are ambient-grade.
- Faction colors: exact locked values on every banner/bot/emblem, consistent across
  pages within a chapter.
- Lore: the Bible wins every conflict; Shelved stays shelved, Contested stays contested.
- Identity: registry Elements only, per style; drift is fixed by re-anchoring, never
  by adjectives.
