---
title: "Architectural Constraints"
session: 13
week: 4
weekTheme: "Constraining the Agent Makes It Perform Better, Not Worse"
duration: "60 min"
order: 13
status: "planned"
objectives:
  - "Distinguish between rules that are stated and rules that are enforced"
  - "Apply the four ACI design principles from SWE-agent research to their own tooling"
  - "Identify at least one architectural rule in their project that is currently only documented"
  - "Make that rule mechanical before the next session"
coreTeachingMoment: >
  "What architectural rules in your project exist only as documentation?"
  Everything in that category is a harness gap. The testable rules from
  session 6 can become automated checks. Pillar 2 audit.
takeaway: "At least one architectural rule now enforced by the build, not by hope."
isRetro: false
---

## Stated Rules vs. Enforced Rules

There are two kinds of rules in a software project:

1. **Stated rules** — documented conventions that developers and agents are expected to follow
2. **Enforced rules** — constraints that the build system, linter, or test suite actively verify

Stated rules rely on the reader to comply. Enforced rules don't care about intent — they fail the build if violated.

**The gap between stated and enforced is a harness gap.** Every architectural rule that exists only as documentation is a rule that can be violated without detection.

This matters especially for agents. An agent won't be embarrassed about violating a convention. It won't feel the social pressure to comply. If the rule isn't enforced, the rule is optional.

## The Four ACI Design Principles

Research on agent-computer interfaces (ACI) from SWE-agent identified four principles for tools and environments that improve agent reliability:

### 1. Actions Should Be Simple

Purpose-built tools outperform complex general-purpose commands. An agent given a `run_tests` tool that returns structured pass/fail output will use it more reliably than an agent told to run `pytest --tb=short -q` and parse the output.

**Apply this:** Build simple, purpose-built checks for your architectural rules. A script that verifies "all routes go through the service layer" is more reliable than a prompt that asks the agent to check this.

### 2. Actions Should Be Compact

Consolidate multi-step operations. If enforcing a rule requires four separate commands, the agent has four chances to make a mistake. A single command that does all four reduces error surface.

**Apply this:** Combine related checks into single scripts. `make lint` that runs formatting, type checking, and architectural validation in one command.

### 3. Feedback Should Be Informative But Concise

The agent needs to know what changed and what the problem is — immediately, without parsing noise. A 200-line stack trace for a simple import error is not useful feedback. "ImportError: `repositories.expenses` imported directly from router — use service layer" is.

**Apply this:** Write custom error messages for your architectural checks. The message should tell the agent what violated the rule, not just that something failed.

### 4. Guardrails Mitigate Error Propagation

Errors compound. A constraint violation in step 2 of a 10-step task can cascade into 8 more violations before the agent surfaces a problem. Early detection gates prevent this.

**Apply this:** Check architectural constraints before and after changes, not just at the end of a task. A pre-commit hook that catches violations immediately is more effective than a CI check that runs after the PR is open.

## The Pillar 2 Audit: What's Enforced?

For each architectural rule in your project, categorize it:

| Rule | Status |
|------|--------|
| "No business logic in routers" | Stated / Enforced |
| "All queries use the repository pattern" | Stated / Enforced |
| "Response envelope on all endpoints" | Stated / Enforced |
| "Type hints on all functions" | Stated / Enforced |

Every "Stated" row is a harness gap.

## From Stated to Enforced: Practical Approaches

| Rule Type | Enforcement Mechanism |
|-----------|----------------------|
| Import constraints | `flake8-import-order`, custom AST check |
| Response format | pytest fixture that validates envelope structure |
| Type coverage | `mypy --strict` in CI |
| Test coverage | `pytest --cov` with minimum threshold |
| Naming conventions | Custom flake8 plugin or pre-commit hook |
| File structure | Shell script in Makefile |

The goal for this session: identify the one rule with the highest error rate in your project and make it mechanical before session 14.

## The Compound Effect

A rule that's enforced mechanically is a rule that never needs to be in a prompt. As more rules become enforced, the agent's job gets simpler — it has fewer decisions to make about whether it's following conventions, because the build will tell it immediately if it isn't.

This is what "constraints make agents better" looks like in practice.
