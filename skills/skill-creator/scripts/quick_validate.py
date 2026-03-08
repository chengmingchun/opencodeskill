#!/usr/bin/env python3
"""Basic validation of a skill."""

import re
import sys
from pathlib import Path


def validate_skill(skill_path):
    """Basic validation of a skill"""
    skill_path = Path(skill_path)

    # Check SKILL.md exists
    skill_md = skill_path / 'SKILL.md'
    if not skill_md.exists():
        return False, "SKILL.md not found"

    # Read and validate frontmatter
    content = skill_md.read_text()
    if not content.startswith('---'):
        return False, "No YAML frontmatter found"

    # Extract frontmatter
    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return False, "Invalid frontmatter format"

    frontmatter_text = match.group(1)

    # Check required fields
    required_fields = ['name:', 'description:']
    for field in required_fields:
        if field not in frontmatter_text:
            return False, f"Missing required field: {field.replace(':', '')}"

    # Check name format
    name_match = re.search(r'^name:\s*(.+)$', frontmatter_text, re.MULTILINE)
    if name_match:
        name = name_match.group(1).strip()
        if ' ' in name:
            return False, "Name should be kebab-case (no spaces)"

    return True, "Valid skill"


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python quick_validate.py <skill-path>")
        sys.exit(1)

    valid, message = validate_skill(sys.argv[1])
    if valid:
        print(f"✓ {message}")
    else:
        print(f"✗ {message}")
        sys.exit(1)
