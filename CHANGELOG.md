# Changelog

## 0.2.0

- Renamed marketplace to **alew3 skills** (`alew3-skills`).
- Added native Claude Code marketplace manifests (`.claude-plugin/marketplace.json` + per-plugin `.claude-plugin/plugin.json`) so the repo is installable via `/plugin marketplace add alew3/skills`; documented install in the README.
- Overhauled `higgsfield-seedance-video-suite` (0.1.0 → 0.2.0):
  - **Dual-mode** every skill: drive the Higgsfield MCP **or** emit paste-ready prompts.
  - **Clarify-before-generate** protocol (asks for format/aspect/duration/model/references first).
  - **Two orchestrators**: `image-workflow-orchestrator` and `video-workflow-orchestrator`.
  - Split image generation into per-deliverable skills: `image-generator`, `character-designer`, `character-sheet-builder`, `environment-sheet-builder`, `style-board-builder`, `storyboard-builder`; added `audio-generator`; renamed `video-brief-grill`→`creative-brief-grill` and `seedance-video-prompt-architect`→`video-prompt-architect` (7 → 14 skills).
  - Support for **multiple characters and multiple environments**; named/array asset map and workflow-state.
  - New backbone docs (`HIGGSFIELD_MCP_REFERENCE`, `DUAL_MODE`, `IMAGE_PROMPT_CONVENTIONS`, `VIDEO_PROMPT_CONVENTIONS`, `GETTING_STARTED`), new templates and worked examples.

## 0.1.0

- Initial marketplace structure.
- Added `higgsfield-seedance-video-suite` as the first plugin.
- Added plugin template.
- Added marketplace validator.
- Added plugin creation script.
