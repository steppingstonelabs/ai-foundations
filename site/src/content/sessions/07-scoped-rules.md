---
title: "Scoped Rules"
session: 7
week: 2
weekTheme: "Tell the Model What It Can and Can't Do"
duration: "60 min"
order: 7
status: "planned"
objectives:
  - "Distinguish between rules that belong globally and rules that only apply in a specific context"
  - "Structure a rule file with a description, scope glob, and rule content"
  - "Build a routing table in AGENTS.md that points the agent to the right rule files"
  - "Produce a complete scoped rule system from existing rules"
coreTeachingMoment: >
  Take the learner's rules from session 6 and sort every one — is it truly
  global or context-specific? Convert buckets into scoped rule files, then
  rebuild AGENTS.md as a lean router. Verify the routing works live.
takeaway: "A leaner AGENTS.md, scoped rule files, and a token budget that thanks you."
isRetro: false
---

## The Problem with One Big Rule File

In session 6, you built a rulebook. In session 7, you're going to break it apart.

The single-file approach has a hidden cost: **every rule loads for every task.** ORM rules load when you're writing documentation. Test rules load when you're writing migration scripts. None of those tokens are doing useful work.

The solution is scoped rules — rule files that load only when they're relevant.

## Global vs. Scoped Rules

The distinction is simple: **does this rule apply everywhere, or only in specific contexts?**

**Global rules** (stay in AGENTS.md):
- Core identity and role
- Language and stack defaults
- Output format conventions
- What to refuse unconditionally

**Scoped rules** (move to separate files):
- ORM-specific patterns (`models/`, `repositories/`)
- Test conventions (`tests/`)
- API endpoint patterns (`routers/`, `endpoints/`)
- Migration rules (`alembic/`)
- Documentation standards (`docs/`)

If a rule only applies when the agent is touching a specific part of the codebase, it belongs in a scoped rule file.

## Scoped Rule File Structure

A scoped rule file has three parts:

```markdown
description: <one line — what these rules cover>
scope: <glob pattern — when to load this file>
---

## Rules

- Rule one
- Rule two
```

**Example — ORM rules:**

```markdown
description: SQLAlchemy ORM patterns for the expense tracker API
scope: src/models/**,src/repositories/**
---

## Rules

- Use the repository pattern. Never access the session directly from a router.
- All queries must use the async session. Never use synchronous SQLAlchemy calls.
- Relationships must be explicitly declared with `lazy="selectin"` or `lazy="raise"`.
```

The `scope` field is a glob. The agent loads this file only when working on files that match the pattern.

## AGENTS.md as a Router

Once you have scoped rule files, AGENTS.md changes role. It stops being an encyclopedia and becomes a **routing table** — a lean document that tells the agent where to find the rules relevant to the current task.

**Example routing table:**

```markdown
## Rule Files

| Scope | File | Description |
|-------|------|-------------|
| `src/models/**,src/repositories/**` | `docs/rules/orm.md` | ORM and database patterns |
| `src/routers/**,src/endpoints/**` | `docs/rules/api.md` | FastAPI endpoint conventions |
| `tests/**` | `docs/rules/testing.md` | pytest patterns and test structure |
| `alembic/**` | `docs/rules/migrations.md` | Migration conventions |
```

The agent reads the routing table, identifies which rule files apply to the current task, and loads only those files. Global rules stay in AGENTS.md. Scoped rules live in `docs/rules/`.

## The Sorting Exercise

Take every rule from your session 6 rulebook. For each one:

1. Ask: "Does this apply everywhere, or only in specific contexts?"
2. If everywhere → keep in AGENTS.md
3. If context-specific → identify the scope, create or append to the right rule file

After sorting, rebuild AGENTS.md with:
- Global rules only
- A routing table pointing to every scoped rule file

Then verify it live: run a task that touches ORM code and confirm the ORM rule file loads. Run a task that touches tests and confirm the test rule file loads.

## The Token Budget Payoff

A monolithic AGENTS.md for a mid-sized project might be 2,000–4,000 tokens. Loading it for every task — including ones that never touch the database — wastes most of those tokens.

A scoped system loads 200–400 tokens of global context plus 200–600 tokens of relevant scoped rules. The math is straightforward. The model that reads fewer irrelevant rules is more focused on the ones that matter.
