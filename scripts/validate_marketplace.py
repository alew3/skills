#!/usr/bin/env python3
"""Validate the alew3 skills marketplace structure."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise ValueError(f"Invalid JSON: {path}: {exc}") from exc


def has_frontmatter_required_fields(skill_path: Path) -> tuple[bool, list[str]]:
    text = skill_path.read_text(encoding="utf-8")
    missing = []
    if not text.startswith("---"):
        return False, ["frontmatter"]
    parts = text.split("---", 2)
    if len(parts) < 3:
        return False, ["frontmatter"]
    fm = parts[1]
    for field in ("name:", "description:"):
        if field not in fm:
            missing.append(field.rstrip(":"))
    return not missing, missing


def validate() -> int:
    errors: list[str] = []
    marketplace_path = ROOT / "marketplace.json"
    if not marketplace_path.exists():
        errors.append("Missing marketplace.json")
        print_errors(errors)
        return 1

    marketplace = load_json(marketplace_path)
    plugins = marketplace.get("plugins", [])
    if not isinstance(plugins, list):
        errors.append("marketplace.json: plugins must be a list")
        print_errors(errors)
        return 1

    seen_plugin_ids: set[str] = set()
    seen_skill_names: set[str] = set()

    for entry in plugins:
        plugin_id = entry.get("id")
        if not plugin_id:
            errors.append("Marketplace plugin entry missing id")
            continue
        if not SLUG_RE.match(plugin_id):
            errors.append(f"Plugin id must be lowercase kebab-case: {plugin_id}")
        if plugin_id in seen_plugin_ids:
            errors.append(f"Duplicate plugin id: {plugin_id}")
        seen_plugin_ids.add(plugin_id)

        rel_path = entry.get("path")
        if not rel_path:
            errors.append(f"Plugin {plugin_id} missing path")
            continue
        plugin_dir = ROOT / rel_path
        if not plugin_dir.exists():
            errors.append(f"Plugin directory not found: {rel_path}")
            continue

        manifest_path = plugin_dir / "plugin.json"
        readme_path = plugin_dir / "README.md"
        if not manifest_path.exists():
            errors.append(f"Plugin {plugin_id} missing plugin.json")
            continue
        if not readme_path.exists():
            errors.append(f"Plugin {plugin_id} missing README.md")

        manifest = load_json(manifest_path)
        if manifest.get("id") != plugin_id:
            errors.append(f"Plugin id mismatch: marketplace={plugin_id}, plugin.json={manifest.get('id')}")

        skills = manifest.get("skills", [])
        if not isinstance(skills, list) or not skills:
            errors.append(f"Plugin {plugin_id} must contain at least one skill")
            continue

        for skill in skills:
            skill_name = skill.get("name")
            skill_path_rel = skill.get("path")
            if not skill_name:
                errors.append(f"Plugin {plugin_id} has skill missing name")
                continue
            if not SLUG_RE.match(skill_name):
                errors.append(f"Skill name must be lowercase kebab-case: {skill_name}")
            unique_skill_key = f"{plugin_id}:{skill_name}"
            if unique_skill_key in seen_skill_names:
                errors.append(f"Duplicate skill in plugin: {unique_skill_key}")
            seen_skill_names.add(unique_skill_key)
            if not skill_path_rel:
                errors.append(f"Skill {skill_name} missing path")
                continue
            skill_path = plugin_dir / skill_path_rel
            if not skill_path.exists():
                errors.append(f"Skill file not found: {plugin_id}/{skill_path_rel}")
                continue
            ok, missing = has_frontmatter_required_fields(skill_path)
            if not ok:
                errors.append(f"Skill {plugin_id}/{skill_name} missing frontmatter fields: {', '.join(missing)}")

    if errors:
        print_errors(errors)
        return 1

    print(f"Marketplace OK: {len(plugins)} plugin(s) validated.")
    return 0


def print_errors(errors: list[str]) -> None:
    print("Marketplace validation failed:\n")
    for error in errors:
        print(f"- {error}")


if __name__ == "__main__":
    sys.exit(validate())
