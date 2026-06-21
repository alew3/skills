# Marketplace Spec

The marketplace is a repository-level registry for AI skill plugins.

## Required root files

```text
marketplace.json
README.md
LICENSE
```

## Required root directories

```text
plugins/
docs/
scripts/
```

## `marketplace.json`

The root `marketplace.json` file is the index of all published plugins.

Required fields:

```json
{
  "schema_version": "0.1.0",
  "id": "alew3-skills",
  "name": "alew3 skills",
  "description": "...",
  "plugin_root": "plugins",
  "plugins": []
}
```

Each plugin entry should include:

```json
{
  "id": "plugin-id",
  "name": "Plugin Name",
  "version": "0.1.0",
  "description": "...",
  "path": "plugins/plugin-id",
  "category": "video-generation",
  "tags": ["tag-1", "tag-2"],
  "entry_skill": "plugin-orchestrator",
  "skill_count": 3
}
```

## Plugin directory convention

```text
plugins/<plugin-id>/
├── plugin.json
├── README.md
├── skills/
│   └── <skill-id>/
│       └── SKILL.md
├── templates/
└── examples/
```

## ID rules

Plugin IDs and skill IDs should use lowercase kebab-case:

```text
good-plugin-id
bad_plugin_id
BadPluginId
```

## Validation

Run:

```bash
python scripts/validate_marketplace.py
```

The validator checks:

- root marketplace file exists;
- plugin entries are unique;
- plugin directories exist;
- plugin manifests are valid JSON;
- skill paths exist;
- skill files include frontmatter with `name` and `description`.
