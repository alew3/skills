# Governance

This marketplace is intentionally lightweight.

## Recommended review rules

Before adding or updating a plugin, check:

- Is the plugin purpose clear?
- Are skill responsibilities separated?
- Does the README explain usage?
- Does the plugin include examples?
- Does the plugin avoid unnecessary overlap with existing plugins?
- Does validation pass?

## Versioning

Use semantic versioning where practical:

```text
0.1.0 = initial draft
0.2.0 = new capabilities, still experimental
1.0.0 = stable public release
```

## Deprecation

If a plugin becomes obsolete, keep it in the marketplace but mark it as deprecated in `plugin.json`:

```json
"deprecated": true,
"deprecated_reason": "Replaced by newer plugin-id"
```
