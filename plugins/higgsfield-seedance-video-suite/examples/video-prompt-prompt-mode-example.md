# Example: Single video prompt, prompt mode (no MCP)

User: *"Give me a Seedance prompt — a lone red-roofed lighthouse on a misty cliff, slow aerial pull-back, 10s, 21:9. I'll run it myself."*

`video-prompt-architect` confirms the few open params (model target = Seedance 2.0; 10s is an allowed step; no start frame = text-to-video; no audio), then outputs:

RATIONALE: Establishing landscape → wide aerial pull-back, overcast soft light, one camera move; 21:9 cinematic.

```
SEND VERBATIM:
A lone red-roofed lighthouse on a misty cliff above a grey sea, gulls drifting, slow aerial pull-back revealing the rugged coastline, soft overcast diffused light, muted desaturated film tone with subtle grain, serene and lonely mood, 10 seconds, 21:9, avoid temporal flicker
```

SUGGESTED PARAMETERS: model `seedance_2_0` · aspect `21:9` · duration `10` · text-to-video · no audio

MCP CALL (optional — same prompt string, if you do have the MCP):
```json
{ "params": { "model": "seedance_2_0", "prompt": "A lone red-roofed lighthouse on a misty cliff above a grey sea, gulls drifting, slow aerial pull-back revealing the rugged coastline, soft overcast diffused light, muted desaturated film tone with subtle grain, serene and lonely mood, 10 seconds, 21:9, avoid temporal flicker", "aspect_ratio": "21:9", "duration": 10 } }
```

The user copies the `SEND VERBATIM` block into Dreamina / any Seedance host. Nothing but the prompt is inside the block.
