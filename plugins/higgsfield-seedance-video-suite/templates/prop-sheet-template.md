# Prop / Object Design Sheet Template

Produces a single, polished landscape **prop / object design sheet**: header, hero render, multi-angle views, detail & material callouts, scale reference, variants/states, and color palette — one cohesive image that locks the object's identity for downstream shots.

**TEXT-HEAVY** (title, labels, hex, callouts) → use **GPT Image 2** (project standard); aspect **16:9**. See `docs/MODEL_PROMPTING.md`. For consistency, lock the hero render first and reference it; if a view drifts, derive it separately (master→derive) and recomposite.

PROP: prop:<name> · CATEGORY: [weapon | tool | vehicle | trophy | device | accessory | signage | …] · HERO (identity lock): [media_id if available]

LAYOUT (describe every section in the prompt):
- HEADER: "<PROP NAME>" + category.
- HERO RENDER: the object, clean background, even product lighting.
- MULTI-ANGLE VIEWS: front / side / back / 3-4 (+ top if layout-critical) — identical object, labeled.
- DETAIL CALLOUTS: close-ups of materials, mechanisms, textures, markings, wear — labeled.
- SCALE REFERENCE: the prop next to a hand / human silhouette / measured marker.
- VARIANTS / STATES: e.g. clean vs worn, open vs closed, color variants — labeled.
- MATERIAL BREAKDOWN: labeled material samples.
- COLOR PALETTE: labeled swatches with hex.
- USAGE NOTES: short caption.
- STYLE: clean editorial infographic layout, thin rule lines, sans-serif labels.

SEND VERBATIM (example filled):
```
A professional prop / object design sheet, landscape, clean editorial infographic layout with thin rule lines and sans-serif labels. HEADER: "DUNK CONTEST TROPHY" + "category: trophy". HERO RENDER: a gold championship basketball trophy with an engraved plaque, on a clean neutral background with even product lighting. MULTI-ANGLE VIEWS: the SAME trophy shown front, side, back, and 3/4, labeled "FRONT / SIDE / BACK / 3-4". DETAIL CALLOUTS: close-ups of the gold finish, the engraved plaque text, and the base — labeled. SCALE REFERENCE: the trophy beside a human hand for size. VARIANTS: a polished gold variant and a matte bronze variant, labeled. MATERIAL BREAKDOWN: labeled samples of polished gold, brushed metal base. COLOR PALETTE strip with labeled hex swatches: "TROPHY GOLD #D4AF37, BASE BLACK #0D0D0F, PLAQUE #C9A24B". USAGE NOTES caption. Identical object identity across every view, legible labels, no warped text.
```

NEGATIVE: shape or material change between views, extra objects, background clutter, unreadable labels, text outside labels.
