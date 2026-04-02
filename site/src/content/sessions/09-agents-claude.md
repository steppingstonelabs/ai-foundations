---
title: "AGENTS.md / CLAUDE.md"
session: 9
week: 3
weekTheme: "Making Behavior Persistent"
duration: "60 min"
order: 9
status: "planned"
objectives:
  - "Explain what AGENTS.md is and why it exists"
  - "Identify the key sections of a well-structured AGENTS.md and what each one does"
  - "Adapt an existing AGENTS.md to their own project context"
  - "Extend their AGENTS.md beyond the example with rules specific to their stack and workflow"
  - "Understand where CLAUDE.md fits as a Claude-specific implementation of the same concept"
coreTeachingMoment: >
  Walkthrough of a complete example AGENTS.md, section by section. Then
  adapt-then-extend — learner adapts it to their own project and writes at
  least two sections that aren't in the example.
takeaway: "Your rules live in the project — not in a prompt you have to remember to paste."
isRetro: false
---

## The Problem AGENTS.md Solves

Everything you've built so far — system prompts, rules, scoped rule files, skills — has one fragile dependency: you have to remember to include it.

A system prompt you wrote in week 1 helps you only if you paste it every time you start a session. Rules you wrote in week 2 only load if you're in an environment that loads them. The moment you start a new chat window, forget to include the context, or hand the project to someone else, all of that knowledge disappears.

**AGENTS.md is a convention that solves this by embedding your rules in the repository itself.**

When an agent opens your project, it reads AGENTS.md first. The rules are there. The routing table is there. The context is there. You don't have to remember to paste anything.

## The Key Sections of a Well-Structured AGENTS.md

### Identity and Role

Who is the agent in this project? What is its primary function?

```markdown
## Identity and Role

You are a backend engineer working on the Personal Expense Tracker API.
Your primary responsibility is implementing, testing, and maintaining
FastAPI endpoints, SQLAlchemy models, and the repository layer.
```

### Stack

What is the technical context? This prevents the model from defaulting to patterns from other stacks.

```markdown
## Stack

- Python 3.11+
- FastAPI with async handlers
- SQLAlchemy 2.0 (async, declarative base)
- Pydantic v2
- PostgreSQL
- pytest with pytest-asyncio
```

### Architecture Rules

The structural constraints that shape every decision.

```markdown
## Architecture Rules

- Follow the repository pattern. Routers call services. Services call repositories.
  Repositories call the database. No layer skips another.
- Never put business logic in a router or model.
- All database access is async.
```

### Code Quality Rules

The standards that apply to all code.

```markdown
## Code Quality Rules

- Functions do exactly one thing.
- No function longer than 30 lines without a documented reason.
- Type hints on every function signature.
```

### Simplicity Rules

The anti-complexity constraints.

```markdown
## Simplicity Rules

- Default to the simplest solution that works.
- No abstract base classes unless there are at least two concrete implementations.
- No factory patterns for objects with a single variant.
```

### Output Rules

How the agent should format and present its work.

```markdown
## Output Rules

- All API responses use the envelope: `{"data": ..., "error": null}`
- Errors use: `{"data": null, "error": {"code": str, "message": str}}`
- Do not explain what you did unless asked.
```

### What to Refuse

The hard limits.

```markdown
## What to Refuse

- Do not modify files outside of `src/`, `tests/`, and `alembic/`
- Do not drop or truncate tables
- Do not modify authentication logic without explicit instruction
```

## The Routing Table (from Week 2)

After the global sections, AGENTS.md includes the routing table from session 7:

```markdown
## Rule Files

| Scope | File | Description |
|-------|------|-------------|
| `src/models/**` | `docs/rules/orm.md` | ORM patterns |
| `src/routers/**` | `docs/rules/api.md` | Endpoint conventions |
| `tests/**` | `docs/rules/testing.md` | Test patterns |
```

## CLAUDE.md — The Same Concept, Claude-Specific

CLAUDE.md is Claude Code's implementation of the same idea. When you open a project in Claude Code, it reads CLAUDE.md automatically. The structure is identical — identity, stack, rules, routing table.

The concept is the same regardless of the tool: **rules that live in the repository are persistent. Rules that live in your head are not.**

## The Adapt-Then-Extend Exercise

1. Start with the example AGENTS.md
2. Adapt every section to your expense tracker — replace the generic content with content that's true of your project
3. Add at least two sections that aren't in the example — rules specific to your stack choices, your error handling approach, your testing philosophy

The sections you add are where the real value is. The example gives you the structure. Your extensions give it meaning.
