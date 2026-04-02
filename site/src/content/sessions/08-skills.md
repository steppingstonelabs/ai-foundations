---
title: "Skills"
session: 8
week: 2
weekTheme: "Tell the Model What It Can and Can't Do"
duration: "60 min"
order: 8
status: "planned"
objectives:
  - "Explain the difference between a rule and a skill"
  - "Understand when a skill is needed versus a rule"
  - "Structure a skill file with a description, scope, and step-by-step procedure"
  - "Add at least two skills to docs/skills/ and wire them into the AGENTS.md routing table"
coreTeachingMoment: "Session design in progress — core experience TBD."
takeaway: "Procedural knowledge encoded where the agent can use it."
isRetro: false
---

## Rules vs. Skills: The Core Distinction

By now you have rules. Rules govern **behavior** — what the agent must and must not do. But some tasks aren't just about behavior. They're about *how* to perform a specific type of work.

That's where skills come in.

**A rule:** "Never modify files outside `src/`."

**A skill:** "Here is the exact sequence of steps to add a new API endpoint to this project."

Rules constrain. Skills instruct. Both are necessary. Neither replaces the other.

## When a Rule Isn't Enough

A rule can tell the agent *what* to produce. It can't reliably encode *how* to produce it when the process matters.

Consider adding a new FastAPI endpoint to the expense tracker. The agent needs to:
1. Create the router file in the right location
2. Register the route in the main app
3. Add the Pydantic request/response schemas
4. Implement the service layer
5. Wire up the repository
6. Write the corresponding test

You could write rules for each of these. But the *sequence* and the *interdependencies* — "don't create the service before you have the schema" — are procedural knowledge that a step-by-step skill encodes better than a set of independent rules.

## Skill File Structure

```markdown
description: <one line describing what this skill covers>
scope: <glob pattern for when to load this skill>
---

## Steps

1. Step one — precise, actionable
2. Step two — what to do after step one
3. Step three — continue...
```

The `description` and `scope` fields work exactly like scoped rule files. The content is a numbered procedure.

**Example — adding an endpoint:**

```markdown
description: Procedure for adding a new API endpoint to the expense tracker
scope: src/routers/**,src/endpoints/**
---

## Steps

1. Create the Pydantic schema in `src/schemas/<resource>.py`
2. Add the repository method in `src/repositories/<resource>.py`
3. Add the service method in `src/services/<resource>.py`
4. Create the router in `src/routers/<resource>.py` using the service
5. Register the router in `src/main.py` with the correct prefix and tags
6. Add a happy-path test in `tests/test_<resource>.py`
```

## Integrating Skills into AGENTS.md

Skills live in `docs/skills/` and are routed the same way as scoped rule files — through a routing table in AGENTS.md.

**Extended routing table:**

```markdown
## Rule Files

| Scope | File | Description |
|-------|------|-------------|
| `src/models/**` | `docs/rules/orm.md` | ORM patterns |
| `tests/**` | `docs/rules/testing.md` | Test conventions |

## Skill Files

| Scope | File | Description |
|-------|------|-------------|
| `src/routers/**` | `docs/skills/add-endpoint.md` | Adding a new endpoint |
| `alembic/**` | `docs/skills/add-migration.md` | Creating a database migration |
```

## The Assignment

Add at least two skills to `docs/skills/`:

1. A skill for a task you do repeatedly in the expense tracker (adding an endpoint, creating a migration, writing a test)
2. A skill for a type of task where you've noticed the agent makes consistent mistakes

Wire both into the AGENTS.md routing table and verify they load correctly.

The goal is a `docs/` directory that contains not just constraints, but procedural knowledge — a repository the agent can navigate to understand not just the rules, but how work gets done here.
