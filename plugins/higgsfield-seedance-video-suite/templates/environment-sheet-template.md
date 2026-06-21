# Environment Design Sheet Template

Produces a single, polished landscape **environment design sheet**: header/meta, hero environment with numbered callouts, environment views A–F, prop breakdown, material/detail callouts, color palette with hex, world notes, and design-notes + top-down map — one cohesive image.

**TEXT-HEAVY** (title, meta row, lettered callouts, captions, hex) → use **GPT Image 2** (project standard); aspect **16:9**. See `docs/MODEL_PROMPTING.md`. For consistency, lock the empty-location master first (master→derive) and keep geometry + light direction identical across every view.

LOCATION: environment:<name> · LOCATION BIBLE (verbatim): [anchors + lighting logic] · MASTER (for geometry lock): [media_id if available]

LAYOUT (describe every section in the prompt):
- HEADER: "<LOCATION> — ENVIRONMENT DESIGN SHEET" + meta row (PROJECT | LOCATION | SETTING | DATE).
- 1. MAIN SCENERY / HERO ENVIRONMENT: a large hero render with numbered leader lines to labeled features.
- 2. ENVIRONMENT VIEWS: ~6 labeled thumbnails A–F (different angles of the SAME location).
- 3. PROP BREAKDOWN: ~8 props A–H, each a product-style shot + short caption.
- 4. MATERIAL / DETAIL CALLOUTS: ~5 material close-ups A–E with labels.
- 5. COLOR PALETTE: labeled swatches with hex.
- 6. WORLD NOTES: a short paragraph.
- 7. DESIGN NOTES / CALLOUTS: lettered notes + a top-down schematic map.
- STYLE: clean editorial infographic layout; identical geometry + lighting across all views.

SEND VERBATIM (example filled):
```
A professional environment design sheet, landscape, editorial infographic layout with thin rule lines and sans-serif labels. HEADER: "INDOOR ARENA — ENVIRONMENT DESIGN SHEET", meta row "PROJECT: ALE BBALL | LOCATION: INDOOR ARENA | SETTING: DUNK CONTEST FINALS". Section 1 MAIN SCENERY: a large hero render of a modern indoor basketball arena — polished hardwood floor, a center-hung jumbotron reading "DUNK FINALS", dramatic overhead spotlights, dense crowd — with numbered leader lines labeling jumbotron, overhead lighting, player tunnel, polished court, and judges table. Section 2 ENVIRONMENT VIEWS: six labeled thumbnails of the SAME arena (A center-court wide, B basket / rim zone, C judges & scorer table, D player tunnel entrance, E crowd seating bowl, F trophy presentation area). Section 3 PROP BREAKDOWN: eight labeled props with short captions (basketball, hoop & backboard, scoreboard/jumbotron, judges score cards, trophy, courtside chair, announcer mic, floor markings). Section 4 MATERIAL / DETAIL CALLOUTS: five close-ups (hardwood floor, matte black accents, LED scoreboard, rim & net, lighting rig). Section 5 COLOR PALETTE: labeled hex swatches. Consistent geometry and lighting across all views, legible labels, no warped text.
```

NEGATIVE: inconsistent geometry or lighting between views, unreadable labels, characters in the empty environment.
