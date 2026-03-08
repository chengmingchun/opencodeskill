# Skill Authoring Best Practices

## Overview

This guide covers best practices for creating effective skills that work well with Claude and other AI coding agents.

## Key Principles

### 1. Clear Trigger Conditions

The `description` field in your skill's frontmatter should clearly explain:
- What the skill does
- When to trigger (specific phrases, contexts, use cases)
- What the user is trying to accomplish

**Good example:**
```
description: Create and manage GitHub issues. Use when user wants to create, list, update, or close GitHub issues.
```

**Avoid:**
```
description: GitHub integration.
```

### 2. Progressive Disclosure

Keep the SKILL.md file under 500 lines. Use referenced files for:
- Detailed documentation
- API schemas
- Complex examples
- Background information

### 3. Concrete Examples

Include specific examples of:
- What the user might say to trigger the skill
- Expected input/output formats
- Edge cases and how to handle them

### 4. Tool Declarations

Clearly state required tools:
- MCP servers
- CLI tools
- External APIs

### 5. Test with Real Use Cases

Create eval prompts that represent:
- Common user scenarios
- Edge cases
- Error handling situations

## Skill Structure

```
skill-name/
├── SKILL.md           # Required
├── scripts/           # Optional - executable code
├── references/        # Optional - documentation
└── assets/           # Optional - templates, etc
```

## Frontmatter Format

```yaml
---
name: skill-name
description: When to use this skill and what it does.
---
```

## Common Mistakes

1. **Vague descriptions** - Be specific about trigger conditions
2. **Too long** - Keep SKILL.md under 500 lines
3. **Missing examples** - Show, don't just tell
4. **No error handling** - Include edge cases
5. **Assuming context** - Don't rely on conversation history

## Testing Your Skill

1. Write 3-5 representative eval prompts
2. Run Claude with your skill on each prompt
3. Verify the outputs meet expectations
4. Iterate based on results

## Resources

- [Anthropic Skills Documentation](https://docs.anthropic.com/en/docs/agents-and-tools/skill)
- [Agent Skills Specification](https://agentskills.io)
