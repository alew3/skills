# Environment Sheet Template

Establish the EMPTY location authoritatively first, then derive angles holding geometry + light direction fixed. See `docs/IMAGE_PROMPT_CONVENTIONS.md` §6.

ENVIRONMENT: `environment:<name>`
ASPECT RATIO: [16:9 or 21:9]

LOCATION BIBLE (lock these):
- Architectural anchors (never move): [windows, doors, key furniture/landmarks]
- Materials: [walls, floor, surfaces]
- Lighting logic: [sources + direction + color temp]
- Palette: [3–5 colors]
- Forbidden drift: [what must not change between shots]

MASTER (establishing) SEND VERBATIM:
[Wide establishing prompt naming the anchors, materials, time of day, lighting direction, camera eye-level wide; "keep anchors, layout, light direction fixed across future shots."]

ANGLE SET (derived from master, geometry-locked):
- Reverse wide — camera 180°, same materials/light/anchors.
- Medium working shot — at [anchor], eye-level, same room + lighting.
- Detail insert — close-up of [key prop], same materials + palette.

TIME-OF-DAY VARIANTS (same geometry, change only light): [dawn | midday | golden hour | night]
