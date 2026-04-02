# AI/LLM Skills Coaching Workshop — Plan Summary
**Stepping Stone Labs**

---

## Overview

A progressive, hands-on curriculum for software developers to build real fluency with AI and LLM tools — from foundational concepts to spec-driven agent development.

**Format:** Small cohorts (8–10 people), live delivery
**Audience:** Software developers
**Duration:** 5 weeks
**Price:** $899 per person
**Cohorts per year:** ~8
**Goal:** Bring participants to the point where they adopt a spec-driven development mindset with AI agents

## Tech Stack

Use the Astro framework to build a modular, static site that has a left-hand navigation with a link for each session. When clicked the session's content will load in the main content area.

---

## The Throughline App

After Week 1, each learner builds a **Personal Expense Tracker API** using the skills from sessions 1–4. This app becomes the sandbox for all evaluation, rule-writing, agent configuration, and spec exercises in weeks 2–5.

**Required baseline features:**
- User model with basic auth
- Expense model (amount, category, date, description)
- Create an expense — `POST /expenses`
- List expenses — `GET /expenses`
- Filter by category — `GET /expenses?category=food`
- Totals with filters — `GET /expenses/total`
- Standard response envelope — `{"data": ..., "error": null}`
- Basic test suite (happy path per endpoint)

**Stack:** Python 3.11+, FastAPI, SQLAlchemy 2.0, Pydantic v2, PostgreSQL, pytest

Learners may extend the app however they like. The build is introduced at the end of session 4 and due before session 5.

---

## Curriculum Map

| Week | # | Session | Duration |
|------|---|---------|----------|
| 1 | 1 | Tokens → Context Window | 30 min |
| 1 | 2 | Prompt Engineering | 30 min |
| 1 | 3 | Modes / System Prompt | 30 min |
| 1 | 4 | Model Selection + Assignment Brief | 30 min |
| 2 | 5 | Output Evaluation | 30 min |
| 2 | 6 | Basic Rules | 60 min |
| 2 | 7 | Scoped Rules | 60 min |
| 2 | 8 | Skills | 60 min |
| 3 | 9 | AGENTS.md / CLAUDE.md | 60 min |
| 3 | 10 | Tool Use / MCP + Function Calling | 60 min |
| 4 | 11 | The Paradigm Shift | 60 min |
| 4 | 12 | Context Engineering | 60 min |
| 4 | 13 | Architectural Constraints | 60 min |
| 4 | 14 | Garbage Collection & Full Audit | 60 min |
| 5 | 15 | Writing Specs for Agents | 60 min |
| 5 | 16 | Project Demo | 60 min |
| 5 | — | Retrospective & Next Steps | 60 min |

**Total instruction time:** ~14.5 hours across 5 weeks

---

## Week 1 — Foundations
**Theme:** How LLMs Actually Work

### Session 1: Tokens → Context Window
**Duration:** 30 minutes

**Learning objectives:**
- Explain what a token is and how LLMs consume them
- Understand that every interaction has a real dollar cost they can observe
- Describe the context window as a finite shared resource that fills from the first message
- Recognize what auto-compaction is, what triggers it, and what it costs

**Core teaching moment:** Learner asks one simple question inside a project and watches the token counter and dollar cost appear. The gap between what they expected it to cost and what it actually cost is the hook.

**Takeaway:** The mental model everything else builds on.

---

### Session 2: Prompt Engineering
**Duration:** 30 minutes

**Learning objectives:**
- Identify the four core failure modes in a poorly written prompt
- Diagnose why a prompt failed before reaching for a fix
- Apply targeted corrections that address the specific failure
- Develop the instinct to read a prompt the way a model reads it

**The four failure modes:**
1. Too vague — the model fills the gap with assumptions
2. Missing context — the model doesn't have what it needs
3. No output format specified — right content, wrong shape
4. Assuming knowledge the model doesn't have

**Core teaching moment:** Four purpose-built broken prompts, each failing in a different way. Learner and coach diagnose each failure together before applying the fix.

**Takeaway:** A diagnostic framework you'll apply to every prompt you write.

---

### Session 3: Modes / System Prompt
**Duration:** 30 minutes

**Learning objectives:**
- Explain what a system prompt is and how it differs from a user prompt
- Describe how the system prompt shapes every subsequent interaction in a session
- Identify what makes a system prompt weak or ineffective
- Write a system prompt that produces consistent, reliable behavior from a code writing assistant

**Core teaching moment:** The same user message run against three system prompts — none, vague, and learner-written. The contrast between versions 1 and 3 is the lesson.

**Takeaway:** Replace the model's defaults with something that works for you.

---

### Session 4: Model Selection + Assignment Brief
**Duration:** 30 minutes

**Learning objectives:**
- Describe the tradeoffs between Claude Haiku, Sonnet, and Opus across capability, cost, and latency
- Explain what extended thinking is and when it's worth the cost
- Match a task type to the right model based on complexity, latency, and budget
- Develop the judgment to stop defaulting to the most capable model for every task

**The four configurations:**
- Claude Haiku — fast, cheap, high volume
- Claude Sonnet — balanced, strong capability at reasonable cost
- Claude Opus — maximum capability, highest cost
- Claude Opus + Extended Thinking — deliberate reasoning mode

**Core teaching moment:** The same architectural analysis prompt run across all four configurations. Learner compares output quality, response time, and cost side by side.

**Takeaway:** The judgment to pick the right model — not just the most capable one.

**End of session:** Introduction of the Week 1 assignment — build the Personal Expense Tracker API using the skills from sessions 1–4. Due before session 5.

---

## Week 2 — Evaluation & Guidance
**Theme:** Tell the Model What It Can and Can't Do

### Session 5: Output Evaluation
**Duration:** 30 minutes

**Learning objectives:**
- Apply a three-point review protocol to any LLM-generated output
- Identify SID violations, pattern deviations, and over-engineering in realistic code output
- Develop the instinct to read LLM output critically before acting on it

**The review protocol:**
1. **SID** — Are Single Responsibility, Interface Segregation, and Dependency Inversion applied?
2. **Patterns** — Did the model adhere to the architectural and code style patterns of the project?
3. **Simplicity** — Did the model reach for complexity where a simpler solution would have worked?

**Core teaching moment:** A purpose-built FastAPI endpoint output that contains all three failure types simultaneously. Learner reads it independently for 7 minutes, then the three-strike debrief reveals what they found and what they missed.

**Takeaway:** A structured protocol for catching what you'd normally skim and ship.

---

### Session 6: Basic Rules
**Duration:** 60 minutes

**Learning objectives:**
- Distinguish between rules that actually change model behavior and rules that only sound correct
- Identify the three properties of a well-written rule: specific, consequential, and testable
- Write rules that directly address the failure modes identified in session 5
- Assemble a working set of basic rules ready to use immediately

**Core teaching moment:** Part 1 — sort 10 pre-built rules into good and bad, building the judgment for what makes a rule effective. Part 2 — return to the session 5 output and write the rules that would have prevented each of the three strikes.

**Takeaway:** A working rulebook built from real failure modes.

---

### Session 7: Scoped Rules
**Duration:** 60 minutes

**Learning objectives:**
- Distinguish between rules that belong globally and rules that only apply in a specific context
- Structure a rule file with a description, scope glob, and rule content
- Build a routing table in AGENTS.md that points the agent to the right rule files
- Produce a complete scoped rule system from existing rules

**The pattern:**
- AGENTS.md acts as a router with a routing table
- Scoped rule files (e.g. `docs/rules/orm.md`) are self-describing with a `description` and `scope` glob
- The agent loads only the rule files relevant to the current task

**Core teaching moment:** Take the learner's rules from session 6 and sort every one — is it truly global or context-specific? Convert buckets into scoped rule files, then rebuild AGENTS.md as a lean router. Verify the routing works live.

**Takeaway:** A leaner AGENTS.md, scoped rule files, and a token budget that thanks you.

---

### Session 8: Skills
**Duration:** 60 minutes

**Learning objectives:**
- Explain the difference between a rule and a skill
- Understand when a skill is needed versus a rule
- Structure a skill file with a description, scope, and step-by-step procedure
- Add at least two skills to `docs/skills/` and wire them into the AGENTS.md routing table

**The distinction:**
- Rules govern behavior — what the agent must and must not do
- Skills govern execution — how the agent performs a specific type of task
- Both live in `docs/` and are routed through AGENTS.md

**Skill file structure:**
```markdown
description: <one line describing what this skill covers>
scope: <glob pattern for when to load this skill>
---
## Steps
1. Step one
2. Step two
...
```

**Core teaching moment:** TBD — session design in progress.

**Takeaway:** TBD

---

## Week 3 — Thinking in Agents
**Theme:** Making Behavior Persistent

### Session 9: AGENTS.md / CLAUDE.md
**Duration:** 60 minutes

**Learning objectives:**
- Explain what AGENTS.md is and why it exists
- Identify the key sections of a well-structured AGENTS.md and what each one does
- Adapt an existing AGENTS.md to their own project context
- Extend their AGENTS.md beyond the example with rules specific to their stack and workflow
- Understand where CLAUDE.md fits as a Claude-specific implementation of the same concept

**Key sections of a well-structured AGENTS.md:**
- Identity and Role
- Stack
- Architecture Rules
- Code Quality Rules
- Simplicity Rules
- Output Rules
- What to Refuse

**Core teaching moment:** Walkthrough of a complete example AGENTS.md, section by section. Then adapt-then-extend — learner adapts it to their own project and writes at least two sections that aren't in the example.

**Takeaway:** Your rules live in the project — not in a prompt you have to remember to paste.

---

### Session 10: Tool Use / MCP + Function Calling
**Duration:** 60 minutes

**Learning objectives:**
- Explain what MCP is and how tool definitions load into the context window
- Describe the tool call loop — how a model decides to call a tool, what it sends, and how the result feeds back into context
- Design a multi-tool chain connecting GitHub and Slack
- Identify the failure points in a tool chain and reason about how to handle them
- Understand the token cost of tool definitions

**The tool call loop:**
1. Model reads the prompt and decides a tool call is needed
2. Model outputs a structured tool call request
3. The tool executes outside the model
4. The result is injected back into the context window
5. Model reads the result and decides what to do next
6. Repeat until complete

**The tool chain:** Code review → PR comments → Slack notification using GitHub MCP and Slack MCP.

**Core teaching moment:** Design the chain before running it, run it and narrate every tool call, then deliberately break it by misconfiguring Slack. Partial failure surfaces the hardest design constraint in agentic tool use.

**Takeaway:** The design principles for tool chains that are safe to run in production.

---

## Week 4 — Harness Engineering
**Theme:** Constraining the Agent Makes It Perform Better, Not Worse

### Session 11: The Paradigm Shift
**Duration:** 60 minutes

**Learning objectives:**
- Define harness engineering in their own words
- Internalize the three foundational principles
- Explain why every agent mistake is an engineering problem, not a prompting problem
- Reframe their own role from code writer to environment designer

**The three principles:**
1. The agent sees only the repository — knowledge in Slack, Docs, or people's heads doesn't exist
2. The human's job changes — from writing code to designing environments, specifying intent, and building feedback loops
3. Constraints make agents better, not worse — a model given precise constraints produces reliable output

**Core teaching moment:** "In every session so far, when something went wrong, what did you do?" The answer — fix the prompt, adjust the rules, rerun — is the instinct to replace. Harness engineering means fixing the class of mistake, not the instance.

**Takeaway:** A fundamentally different orientation toward AI-assisted development.

---

### Session 12: Context Engineering
**Duration:** 60 minutes

**Learning objectives:**
- Explain why a monolithic AGENTS.md fails at scale
- Describe what a fully harness-engineered repository looks like
- Identify what knowledge in their project currently lives only in people's heads
- Begin externalizing that knowledge into version-controlled, machine-readable artifacts

**The pattern:** AGENTS.md as table of contents, not encyclopedia. A structured `docs/` directory containing design documentation, architecture maps, quality documents, and execution plans — all versioned alongside the code.

**Core teaching moment:** "If an agent opened your repository with no other context, what could it learn about how your project works?" The gap between the answer and reality is the harness work. Pillar 1 audit.

**Takeaway:** A repository the agent can navigate without asking you for context.

---

### Session 13: Architectural Constraints
**Duration:** 60 minutes

**Learning objectives:**
- Distinguish between rules that are stated and rules that are enforced
- Apply the four ACI design principles from SWE-agent research to their own tooling
- Identify at least one architectural rule in their project that is currently only documented
- Make that rule mechanical before the next session

**The ACI design principles:**
1. Actions should be simple — purpose-built tools, not complex commands
2. Actions should be compact — consolidate multi-step operations
3. Feedback should be informative but concise — show the agent what changed immediately
4. Guardrails mitigate error propagation — syntax checkers, linters, CI gates

**Core teaching moment:** "What architectural rules in your project exist only as documentation?" Everything in that category is a harness gap. The testable rules from session 6 can become automated checks. Pillar 2 audit.

**Takeaway:** At least one architectural rule now enforced by the build, not by hope.

---

### Session 14: Garbage Collection & Full Audit
**Duration:** 60 minutes

**Learning objectives:**
- Explain why agent-generated code accumulates drift differently than human-written code
- Design a basic garbage collection strategy for their repository
- Complete a full three-pillar harness audit
- Identify the single highest-leverage gap to close before session 15

**Garbage collection approaches:**
- Periodic agent task to review `docs/` and open PRs for stale content
- CI check that validates AGENTS.md links resolve to real files
- Weekly quality document review

**Core teaching moment:** Full three-pillar audit across context engineering, architectural constraints, and garbage collection. For each gap: "What's the highest-leverage fix — what single change would prevent the most future failures?"

**Takeaway:** A harness that stays accurate — and a clear list of what to fix next.

---

## Week 5 — Spec-Driven Development
**Theme:** The Capstone Skill

### Session 15: Writing Specs for Agents
**Duration:** 60 minutes

**Learning objectives:**
- Explain why a spec written for an agent is fundamentally different from a task description written for a human
- Identify gaps in a spec — places where an agent would fill in arbitrarily
- Write exhaustive Given → When → Then acceptance criteria that leave no room for agent inference
- Specify proof of work requirements through HTTP records and Playwright scripts
- Produce a complete, executable agent spec for a real task in their own project

**A complete spec contains:**
- Objective — what the agent is being asked to accomplish, stated precisely
- Scope — what is explicitly in and out of bounds
- Relevant modules — exact files, classes, and functions to reference or modify
- Constraints — what the agent must not do
- Acceptance criteria — exhaustive Given → When → Then scenarios
- Proof of work — HTTP request/response records and Playwright scripts

**Core teaching moment:** A deliberately gapped spec for a password reset endpoint. Learner hunts for gaps before the spec is run, rewrites the acceptance criteria as proper Given → When → Then scenarios, then writes their own spec for a real task in their project.

**Takeaway:** The mindset shift that changes how you work with AI permanently.

---

### Session 16: Project Demo
**Duration:** 60 minutes

**Learning objectives:**
- Demonstrate the expense tracker app with the agent infrastructure built throughout the workshop
- Articulate how the skills from each week connect and compound in real work
- Identify what changed in how they approach AI-assisted development

**Format:** Each learner demos their app — not just the features, but the AGENTS.md, scoped rules, skills, and at least one agent-executed spec. The demo is a proof of the harness, not just the product.

**Takeaway:** A clear picture of how the skills you've built connect and compound in real work.

---

### Retrospective & Next Steps
**Duration:** 60 minutes

**Format:** Look back at the full arc — from tokens to specs — and take stock of what's changed. Surface the highest-leverage next steps for each participant and map a path to the advanced workshop.

**Takeaway:** A clear picture of where you are and what to build next.

---

## Still To Be Built

The following sessions have been scoped but not yet fully designed:

- **Session 8: Skills** — experience design and full session plan
- **Sessions 11–14: Harness Engineering** — decomposed from the existing single session into four separate session plans
- **Session 16: Project Demo** — facilitation structure

---

## Advanced Workshop (Planned)

Topics flagged for the advanced workshop:
- Quantitative evals (evals-as-code, scoring, regression testing)
- Memory and state management (short-term vs. long-term, summarization vs. truncation)
- Multi-agent orchestration
- Autonomous agents
- Building the environment and tooling for production-grade agent workflows