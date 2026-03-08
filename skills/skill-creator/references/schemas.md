# Skill Schema Reference

## SKILL.md Frontmatter

```yaml
---
name: skill-name
description: Description of when to trigger and what the skill does.
version: 1.0.0
author: Your Name
---
```

## Required Fields

| Field | Type | Description |
|-------|------|-------------|
| name | string | Skill identifier (kebab-case) |
| description | string | When to trigger + what it does |

## Optional Fields

| Field | Type | Description |
|-------|------|-------------|
| version | string | Semantic version |
| author | string | Skill author |
| compatibility | object | Required tools/dependencies |

## Eval Format

```json
{
  "eval_id": 1,
  "eval_name": "example-eval",
  "should_trigger": true,
  "prompt": "Your test prompt here",
  "expected": {
    "behavior": "What the skill should do",
    "output_format": "Optional output format"
  },
  "assertions": [
    {
      "type": "contains",
      "value": "expected string"
    },
    {
      "type": "regex",
      "pattern": ".*pattern.*"
    }
  ]
}
```

## Assertion Types

| Type | Description |
|------|-------------|
| contains | Output contains specific string |
| regex | Output matches regex pattern |
| file_exists | Specific file was created |
| file_contains | File contains specific content |
| no_error | No error messages in output |

## Skill Directory Structure

```
skill-name/
├── SKILL.md              # Required
├── scripts/              # Optional
│   └── *.py, *.sh
├── references/           # Optional
│   └── *.md, *.json
├── assets/               # Optional
│   └── templates/*
└── examples/             # Optional
    └── *.json
```
