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

1. **Claude Code native** — `.claude-plugin/marketplace.json` (repo root) + `.claude-plugin/plugin.json` (per plugin). This is what Claude Code's `/plugin marketplace add alew3/skills` and `/plugin install <plugin>@alew3-skills` actually read, per the official schemas ([marketplace](https://json.schemastore.org/claude-code-marketplace.json), [plugin manifest](https://json.schemastore.org/claude-code-plugin-manifest.json)). Marketplace requires `name`, `owner{name}`, `plugins[]` (each plugin entry requires only `name` + `source`). Plugin manifest requires only `name`. **Follow market standard — populate the recommended metadata on both**: `$schema`, `displayName`, `description`, `version`, `author{name,email}`, `homepage`, `repository`, `license` (SPDX), `keywords[]`, `category`. `source` for a local plugin is a `./`-relative path from the repo root (git-based marketplaces only). Marketplace `name` must be lowercase kebab-case (`alew3-skills`, no spaces) and must avoid Anthropic's reserved names.
2. **Custom registry** — root `marketplace.json` + per-plugin `plugin.json`, validated by `scripts/validate_marketplace.py`. Richer metadata (skills[], templates[], examples[], tags) and the repo's own docs/tooling depend on it. Claude Code ignores this file.

Skills live at `plugins/<plugin-id>/skills/<skill-id>/SKILL.md` and are auto-discovered by Claude Code once the plugin is installed — this path serves both systems.

**Two version levels — keep both in sync:**

- **Plugin version** — the per-plugin `version`, which must match across **all four places**: the custom `marketplace.json` entry, the custom `plugin.json`, the native `.claude-plugin/plugin.json`, and the native `.claude-plugin/marketplace.json` entry. `validate_marketplace.py` fails on any mismatch. Bump it (semver) whenever a plugin's behavior or content changes.
- **Marketplace (registry) version** — the top-level `version` on the registry itself: native `.claude-plugin/marketplace.json` `version` and custom `marketplace.json` `version` (distinct from `schema_version`, which tracks the manifest *format*, not its content). Bump this whenever the registry contents change (e.g. a plugin bump or a new plugin) — it's the signal clients like Claude for Desktop use to detect the marketplace changed and re-fetch instead of serving a cached catalog. Keep the two registry `version` fields equal.

Note both manifest systems cache aggressively: the Claude Code CLI clones the marketplace under `~/.claude/plugins/marketplaces/<name>/` and caches a catalog in `~/.claude/plugins/plugin-catalog-cache.json`; Claude for Desktop keeps its own copy in the app's IndexedDB (`~/Library/Application Support/Claude`). Reinstalling a *plugin* does not refresh the *marketplace* — run `/plugin marketplace update <name>` (CLI) or remove + re-add the marketplace (Desktop) after pushing version changes.

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
