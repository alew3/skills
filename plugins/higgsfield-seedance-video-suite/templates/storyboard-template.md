# Storyboard / Shot List Template

A planning document, not a poster. One row per shot. Each shot binds the approved character(s) and environment it uses. See `docs/VIDEO_PROMPT_CONVENTIONS.md`.

GLOBALS (apply to all shots): aspect ratio · palette · grade · lens/film look · time of day

Per-shot rows:

| shot_id | dur(s) | shot_size | camera_move | subjects | action (one beat) | location | dialogue/SFX | refs_used | continuity | purpose |
|---------|--------|-----------|-------------|----------|-------------------|----------|--------------|-----------|-----------|---------|
| S01-01  | 5      | WS        | static      | maya     | enters, scans room | lab     | (none)       | character:maya, environment:lab, style-board | maya enters frame-left | establish |
| S01-02  | 5      | MCU       | slow push-in| maya     | her eyes narrow    | lab     | SFX: hum     | character:maya, environment:lab | match S01-01 light | reveal |

Rules: ONE motion + ONE action beat per shot; `purpose` blank ⇒ decorative ⇒ cut it; `refs_used` binds the shot to locked assets for continuity. Each storyboard keyframe (one still per shot) is generated from the bound character/environment/style refs and becomes the i2v start frame.
