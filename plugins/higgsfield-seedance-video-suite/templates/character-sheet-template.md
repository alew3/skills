# Character Design Sheet Template

Produces a single, polished landscape **character design / model sheet** (studio style): header, full turnaround, expression row, outfit & equipment breakdown with callouts, color palette with hex, and a small world-setting panel — one cohesive image.

**TEXT-HEAVY** (title, labels, hex, bullet callouts) → prefer **GPT Image 2** or **Nano Banana Pro**; aspect **16:9**. See `docs/MODEL_PROMPTING.md`. For maximum identity fidelity, lock the character master first (`character-designer`) and reference it; if a panel drifts, derive it separately (master→derive) and recomposite.

CHARACTER: character:<name> · IDENTITY BLOCK (verbatim from character-designer): [...] · MASTER (for identity lock): [media_id if available]

LAYOUT (describe every section in the prompt):
- HEADER: "<NAME>" large + "<height> | <role/position>".
- TURNAROUND: full-body FRONT, SIDE (profile), BACK — identical identity, wardrobe, proportions; neutral standing pose; clean white seamless background; even studio light; labeled FRONT / SIDE / BACK.
- FACIAL EXPRESSIONS: a row of ~5 head-and-shoulders portraits, same face, labeled (e.g. NEUTRAL, FOCUSED, DETERMINED, SLIGHT SMILE, INTENSE).
- OUTFIT & EQUIPMENT BREAKDOWN: flat product-style shots of each garment/item (e.g. top front+back, bottoms front+back, footwear, accessories, key prop), each with 2–3 bullet callouts.
- DETAIL CALLOUTS: close-ups of trims / materials with short labels.
- COLOR PALETTE: labeled swatches with hex codes.
- WORLD SETTING: one small environment thumbnail + a 2–3 line caption.
- STYLE: clean editorial infographic layout, thin rule lines between sections, sans-serif labels, white background.

SEND VERBATIM (assemble the above; example filled):
```
A professional character design / model sheet on a clean white background, editorial infographic layout with thin rule lines and sans-serif labels. HEADER top-left: "ALE BBALL" large, beside it "6'4\" | SHOOTING GUARD". TURNAROUND row — the same man, [identity block: ~50s athletic man, short grey curly hair, lined face] — shown full-body FRONT, SIDE profile, and BACK in a black basketball jersey number 24 with grey/white trim and matching shorts, neutral standing pose, even studio lighting, labeled "FRONT / SIDE / BACK". FACIAL EXPRESSIONS row: five head-and-shoulders portraits of the SAME face labeled "NEUTRAL, FOCUSED, DETERMINED, SLIGHT SMILE, INTENSE GAME FACE". OUTFIT & EQUIPMENT BREAKDOWN: clean flat shots of the jersey (front and back, number 24), shorts (front and back), black basketball shoes, white crew socks, and a basketball, each with small bullet callouts. COLOR PALETTE strip with labeled swatches: "JERSEY BLACK #1A1A1A, TRIM GRAY #D9D9D9, WHITE #FFFFFF, SKIN TONE #E0B08C, HAIR GRAY #6B6F73". WORLD SETTING: a small thumbnail of a modern indoor basketball arena with a 2-line caption. Identical identity across every panel, legible labels, no warped text.
```

NEGATIVE: inconsistent face between panels, unreadable labels, cluttered layout, extra people.
