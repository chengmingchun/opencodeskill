---
name: skill-creator
description: Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, edit or optimize an existing skill, run evals to test a skill, benchmark skill performance with variance analysis, or optimize a skill's description for better triggering accuracy.
---

# Skill Creator

A skill for creating new skills and iteratively improving them.

## Overview

The process of creating a skill:
1. Decide what you want the skill to do and how it should work
2. Write a draft of the skill
3. Create test prompts and run the skill on them
4. Iterate and improve based on results

## Creating a Skill

### Step 1: Capture Intent

Understand the user's needs:
1. What should this skill enable Claude to do?
2. When should this skill trigger? (what user phrases/contexts)
3. What's the expected output format?
4. Should we set up test cases to verify the skill works?

### Step 2: Write the SKILL.md

Required components:
- **name**: Skill identifier (kebab-case)
- **description**: When to trigger, what it does. Include both what the skill does AND specific contexts for when to use it.
- **compatibility**: Required tools, dependencies (optional)
- **instructions**: The skill body with detailed instructions

### Anatomy of a Skill

```
skill-name/
├── SKILL.md (required)
│   ├── YAML frontmatter (name, description required)
│   └── Markdown instructions
└── Bundled Resources (optional)
    ├── scripts/    - Executable code for deterministic/repetitive tasks
    ├── references/ - Docs loaded into context as needed
    └── assets/     - Templates, fonts, icons
```

## Skill Structure

### Three-Level Loading System

1. **Metadata** (name + description) - Always in context (~100 words)
2. **SKILL.md body** - In context whenever skill triggers (<500 lines ideal)
3. **Referenced files** - Loaded on demand

### Best Practices

- Keep SKILL.md under 500 lines
- Reference files clearly from SKILL.md with guidance on when to read them
- Use examples to illustrate expected behavior
- Include edge case handling

## Eval Creation

### What Makes Good Evals

1. **Representative prompts** - Test real use cases
2. **Clear assertions** - Verifiable pass/fail criteria
3. **Sufficient coverage** - Cover edge cases and common scenarios

### Eval Format

```json
{
  "eval_id": 1,
  "eval_name": "example-eval",
  "should_trigger": true,
  "prompt": "Your test prompt here",
  "expected": {
    "behavior": "What the skill should do"
  }
}
```

## Improvement Process

1. Run eval on current skill description
2. Analyze failures and patterns
3. Improve skill description based on results
4. Re-run eval to verify improvements
5. Repeat until satisfactory

## Scripts

The skill-creator includes several scripts in the `scripts/` directory:
- `run_eval.py` - Run evaluation for a skill
- `run_loop.py` - Run eval + improve loop
- `improve_description.py` - Improve skill description using AI
- `aggregate_benchmark.py` - Aggregate benchmark results
- `package_skill.py` - Package skill as .skill file

## Agents

### Grader Agent
Evaluates expectations against execution transcript and outputs.

### Blind Comparator Agent
Compares two outputs WITHOUT knowing which skill produced them.

### Post-hoc Analyzer Agent
Analyzes comparison results to understand why the winner won.

## References

See `references/` directory for:
- Schema definitions
- Best practices
- Example skills
