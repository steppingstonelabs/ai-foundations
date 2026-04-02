---
title: "Context Engineering"
session: 12
week: 4
weekTheme: "Constraining the Agent Makes It Perform Better, Not Worse"
duration: "60 min"
order: 12
status: "planned"
objectives:
  - "Explain why a monolithic AGENTS.md fails at scale"
  - "Describe what a fully harness-engineered repository looks like"
  - "Identify what knowledge in their project currently lives only in people's heads"
  - "Begin externalizing that knowledge into version-controlled, machine-readable artifacts"
coreTeachingMoment: >
  "If an agent opened your repository with no other context, what could it
  learn about how your project works?" The gap between the answer and reality
  is the harness work. Pillar 1 audit.
takeaway: "A repository the agent can navigate without asking you for context."
isRetro: false
---

## Why Monolithic AGENTS.md Fails at Scale

In week 2, you built a scoped rule system to reduce token waste. Context engineering is the same principle applied to the entire repository structure.

A monolithic AGENTS.md — even a well-written one — has limits:

- It grows as the project grows, eventually becoming too long to be useful
- It can't capture the depth of context that architectural decisions deserve
- It conflates routing instructions with substantive content
- It becomes a bottleneck: every important decision gets pushed into one file

The solution is a structured `docs/` directory that distributes knowledge across purpose-built artifacts.

## The Harness-Engineered Repository

A fully harness-engineered repository separates knowledge into distinct categories:

```
docs/
├── architecture/
│   ├── overview.md          # System design and key decisions
│   ├── data-model.md        # Entity relationships and schema rationale
│   └── api-design.md        # Endpoint conventions and patterns
├── rules/
│   ├── orm.md               # SQLAlchemy patterns
│   ├── api.md               # FastAPI conventions
│   └── testing.md           # Test structure
├── skills/
│   ├── add-endpoint.md      # How to add a new endpoint
│   └── add-migration.md     # How to run a migration
└── quality/
    ├── checklist.md         # Pre-commit quality gates
    └── review-criteria.md   # What good looks like
AGENTS.md                    # Table of contents + routing table
```

**AGENTS.md is the table of contents, not the encyclopedia.**

## What Goes in Architecture Docs

Architecture docs are not README files. They're not setup guides. They're decision records — documents that explain *why* the system is structured the way it is.

A good architecture doc answers:
- What does this component do?
- Why was this approach chosen over alternatives?
- What are the key constraints and invariants?
- What should an agent preserve when modifying this component?

An agent reading your architecture docs should be able to make new decisions that are consistent with past decisions — without asking you.

## The Pillar 1 Audit: What Does the Agent Know?

The core question: *If an agent opened your repository with no other context, what could it learn about how your project works?*

Work through these categories:

| Category | Question | Status |
|----------|---------|--------|
| Architecture | Can the agent understand the system design? | Gap / Covered |
| Data model | Can the agent understand the entity relationships? | Gap / Covered |
| Patterns | Can the agent understand what "following the patterns" means? | Gap / Covered |
| Decisions | Can the agent understand why key decisions were made? | Gap / Covered |
| Constraints | Can the agent understand what it must not do? | Gap / Covered |

Every gap is a place where the agent is currently filling in with inference.

## Externalizing Knowledge

The practical work of context engineering is **identifying knowledge that currently lives only in human heads and writing it down in machine-readable form.**

This includes:
- Architecture decisions that were made in conversations and never documented
- Conventions that "everyone knows" but aren't written anywhere
- The reasoning behind architectural choices that look arbitrary without context
- Constraints that are enforced socially, not mechanically

Start with the highest-impact gaps — the knowledge whose absence would cause the most agent errors — and externalize one at a time.

## Version Control Is Not Optional

Every artifact in `docs/` must be version-controlled alongside the code. When the architecture changes, the architecture doc changes in the same commit. When a rule is added, the rule file is committed with the feature it governs.

A `docs/` directory that drifts from the codebase is worse than no `docs/` directory — it teaches the agent the wrong things.
