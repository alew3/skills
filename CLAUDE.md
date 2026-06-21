# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A **local-first marketplace of modular AI skill plugins**. There is no application runtime — plugins are folders of Markdown "skills" (prompt instructions with YAML frontmatter), plus templates and examples. Validation and scaffolding are the only executable code, written in Python (stdlib only, no dependencies).

## Commands

```bash
# Validate the entire marketplace (run after any structural change; CI runs this on push/PR to main)
python scripts/validate_marketplace.py

# Scaffold a new plugin from plugins/_template and auto-register it in marketplace.json
python scripts/create_plugin.py my-plugin-id \
  --name "My Plugin" --description "What it does" --category general --author "Name"
# add --no-register to create files without touching marketplace.json
```

There is no build, lint, or test suite. `validate_marketplace.py` is the de facto correctness check. (The docs write `python`, but invoke with `python3` if `python` is not on PATH.)

## Two manifest systems (important)

This repo carries **two parallel manifest formats** — keep both in sync when adding/renaming plugins:

1. **Claude Code native** — `.claude-plugin/marketplace.json` (repo root) + `.claude-plugin/plugin.json` (per plugin). This is what Claude Code's `/plugin marketplace add alew3/skills` and `/plugin install <plugin>@alew3-skills` actually read. Schema: top-level `$schema`, `name`, `version`, `description`, `owner{name,email}`, `plugins[]`; each plugin needs `name`/`description`/`source`/`category` (+ optional `version`/`author`). Marketplace `name` must be alphanumeric/hyphens (`alew3-skills`, no spaces).
2. **Custom registry** — root `marketplace.json` + per-plugin `plugin.json`, validated by `scripts/validate_marketplace.py`. Richer metadata (skills[], templates[], examples[], tags) and the repo's own docs/tooling depend on it. Claude Code ignores this file.

Skills live at `plugins/<plugin-id>/skills/<skill-id>/SKILL.md` and are auto-discovered by Claude Code once the plugin is installed — this path serves both systems.

**Keep the plugin `version` in sync across all four places** when you change a plugin: the custom `marketplace.json` entry, the custom `plugin.json`, the native `.claude-plugin/plugin.json`, and the native `.claude-plugin/marketplace.json` entry. `validate_marketplace.py` now fails on any mismatch. Bump the version (semver) whenever a plugin's behavior or content changes.

## Architecture

Three nesting levels: **Marketplace → Plugin → Skill**.

- `marketplace.json` — top-level registry. Each entry summarizes a plugin (`id`, `path`, `entry_skill`, `skill_count`, tags). This is an index only; the authoritative skill list lives in each plugin's `plugin.json`.
- `plugins/<plugin-id>/plugin.json` — the plugin manifest. Its `skills[]` array (each with `name` + `path`) is what the validator actually checks against disk. Keep this in sync with the files on disk and with the marketplace summary.
- `plugins/<plugin-id>/skills/<skill-id>/SKILL.md` — one skill = one responsibility. Must begin with YAML frontmatter containing at least `name:` and `description:`.
- `plugins/_template/` — source copied by `create_plugin.py`; placeholders (`{{PLUGIN_ID}}`, `{{PLUGIN_NAME}}`, `{{PLUGIN_DESCRIPTION}}`, `{{PLUGIN_CATEGORY}}`, `{{AUTHOR}}`, and `template-orchestrator`) are find-and-replaced.

### Orchestrator vs specialist skills

Within a plugin, one skill is usually the **orchestrator** (named `<plugin-id>-orchestrator`, referenced as `entry_skill`). It coordinates the workflow by calling specialist skills by responsibility — it must **not** duplicate their instructions. Every specialist skill is also independently callable. See `plugins/higgsfield-seedance-video-suite/` for the reference implementation (7 skills: `video-workflow-orchestrator` + 6 specialists).

### Passthrough discipline

When a skill produces a prompt meant to be sent to a downstream tool unchanged, it must be isolated in a `SEND VERBATIM:` block. Everything outside that block is commentary/metadata. Approval gates are required whenever an intermediate output (character/environment reference, storyboard, final prompt) affects downstream generation.

## Conventions enforced by the validator

- All plugin ids and skill names must be **lowercase kebab-case** (`^[a-z0-9]+(?:-[a-z0-9]+)*$`).
- `plugin.json`'s `id` must equal the marketplace entry's `id` and match the folder name.
- Each plugin needs `plugin.json` + `README.md` and at least one skill.
- Each `SKILL.md` needs frontmatter with `name` and `description`.
- Skill names must be unique within a plugin; plugin ids unique across the marketplace.

When adding a plugin manually (not via the generator), update **both** `plugin.json` (full `skills[]`) and `marketplace.json` (summary + `skill_count`), then run the validator. Reference docs live in `docs/` (`PLUGIN_SPEC.md`, `MARKETPLACE_SPEC.md`, `WORKFLOW.md`, `ADDING_A_PLUGIN.md`, `GOVERNANCE.md`).
