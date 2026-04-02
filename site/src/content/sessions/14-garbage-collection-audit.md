---
title: "Garbage Collection & Full Audit"
session: 14
week: 4
weekTheme: "Constraining the Agent Makes It Perform Better, Not Worse"
duration: "60 min"
order: 14
status: "planned"
objectives:
  - "Explain why agent-generated code accumulates drift differently than human-written code"
  - "Design a basic garbage collection strategy for their repository"
  - "Complete a full three-pillar harness audit"
  - "Identify the single highest-leverage gap to close before session 15"
coreTeachingMoment: >
  Full three-pillar audit across context engineering, architectural constraints,
  and garbage collection. For each gap: "What's the highest-leverage fix —
  what single change would prevent the most future failures?"
takeaway: "A harness that stays accurate — and a clear list of what to fix next."
isRetro: false
---

## Why Agent-Generated Code Drifts Differently

Human developers accumulate technical debt incrementally. They understand what they built, remember why they made certain decisions, and can recognize when something has diverged from the original intent.

Agents don't have memory across sessions. Each session starts fresh. An agent that built a component two weeks ago has no recollection of the design decisions made at the time. It reads the current state of the repository and infers what was intended.

**This creates a specific failure mode:** as the codebase evolves, architectural decisions documented in the past may no longer reflect the current reality. The agent reads stale documentation and makes decisions based on it. The gap between documentation and implementation grows — silently.

This is **documentation drift**, and it's more common and more dangerous with agents than with human teams.

## Garbage Collection Strategies

Garbage collection in a harness-engineered repository is the practice of keeping documentation, rules, and architectural specs current with the actual codebase.

### Strategy 1: Periodic Agent Review

Schedule a recurring task where the agent reviews `docs/` against the actual codebase:

```
Task: Review docs/architecture/data-model.md against the current SQLAlchemy models.
For each discrepancy, open a PR with the corrected documentation.
```

The agent becomes its own documentation maintainer.

### Strategy 2: CI Validation for AGENTS.md Links

AGENTS.md contains a routing table with file paths. Those paths can be validated automatically:

```bash
# Check that every file referenced in AGENTS.md exists
grep -oP '`docs/[^`]+`' AGENTS.md | xargs -I{} test -f {} || exit 1
```

A broken link in AGENTS.md means the agent is routing to a file that doesn't exist — silently skipping rules.

### Strategy 3: Weekly Quality Document Review

A standing agenda item: compare `docs/quality/checklist.md` against recent PRs. Are the criteria still the right ones? Are they catching the right things? Has the codebase evolved in ways that make some criteria obsolete?

This is a human review, not an automated one — but it should be scheduled and tracked.

## The Full Three-Pillar Audit

Weeks 3 and 4 have covered three pillars of harness engineering. This session is the comprehensive audit.

### Pillar 1: Context Engineering

*Can the agent understand your project without asking you?*

- [ ] Architecture docs exist and are current
- [ ] Data model documented with rationale
- [ ] Key design decisions recorded
- [ ] AGENTS.md is a lean table of contents, not an encyclopedia
- [ ] Scoped rule files cover all major contexts

### Pillar 2: Architectural Constraints

*Are your rules enforced by the build, not by documentation?*

- [ ] High-priority rules have automated enforcement
- [ ] CI checks catch architectural violations before merge
- [ ] Error messages are informative and actionable
- [ ] Pre-commit hooks prevent most violations from entering the repo

### Pillar 3: Garbage Collection

*Does your harness stay accurate as the project evolves?*

- [ ] Process for detecting documentation drift
- [ ] AGENTS.md link validation in CI
- [ ] Scheduled review cycle for quality documents
- [ ] Clear ownership for documentation updates

## The Highest-Leverage Gap

For each gap identified in the audit, ask: *What single change would prevent the most future failures?*

Not every gap is equal. A missing architecture doc for a stable, low-touch component is a low-priority gap. A missing enforcement mechanism for a rule that's been violated three times in the last month is the highest-leverage fix.

Prioritize by failure rate, not by completeness. The harness doesn't have to be perfect — it has to prevent the most expensive mistakes.

## Before Session 15

Leave this session with:
1. A prioritized list of harness gaps
2. The single highest-leverage gap identified
3. A plan to close it before the spec-writing session

The spec-writing session works best when the harness is solid enough that the agent can execute against a spec reliably. Gaps in the harness become failures in spec execution.
