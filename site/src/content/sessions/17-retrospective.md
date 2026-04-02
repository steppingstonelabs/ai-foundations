---
title: "Retrospective & Next Steps"
week: 5
weekTheme: "The Capstone Skill"
duration: "60 min"
order: 17
status: "planned"
objectives:
  - "Reflect on the full arc of the workshop — from tokens to specs"
  - "Identify the highest-leverage next steps for your own practice"
  - "Map a path to the advanced workshop topics"
coreTeachingMoment: >
  Look back at the full arc — from tokens to specs — and take stock of what's
  changed. Surface the highest-leverage next steps for each participant and
  map a path to the advanced workshop.
takeaway: "A clear picture of where you are and what to build next."
isRetro: true
---

## Looking Back at the Arc

Five weeks ago, you watched a token counter and discovered that AI interactions have a real cost you can observe. That was the hook — the gap between what you expected and what it actually cost.

Every session since has been about closing gaps. The gap between a vague prompt and an effective one. The gap between rules that sound right and rules that change behavior. The gap between documentation and enforcement. The gap between a task description and a spec an agent can execute.

**The arc:** tokens → prompts → rules → persistence → harness → specs.

Each layer depends on the one before it. A spec executed against a weak harness is fragile. A harness without rules is guidance without constraint. Rules without understanding context are cargo-culting. It all starts with understanding what you're actually working with.

## What Changed

Take stock honestly. The goal isn't to feel good about what you built — it's to understand what actually shifted.

### The debugging instinct

When the agent produces wrong output now, what's your first move?

Before: fix the prompt, rerun.

After (ideally): find the harness gap that allowed this class of mistake and close it.

### The documentation instinct

When you make an architectural decision now, where does it go?

Before: in your head, maybe in a Slack message.

After (ideally): in `docs/architecture/`, version-controlled, machine-readable.

### The spec instinct

When you want the agent to implement something non-trivial, how do you approach it?

Before: describe it conversationally and iterate.

After (ideally): write the spec first — objective, scope, constraints, acceptance criteria, proof of work — then run it.

## Highest-Leverage Next Steps

For each participant, identify the single change that would have the most impact on the quality of your AI-assisted development practice over the next 30 days.

Common candidates:
- Completing the context engineering work (architecture docs, decision records)
- Closing the highest-priority enforcement gap identified in the session 14 audit
- Building the spec habit — writing one complete spec per week for real tasks
- Running the garbage collection process for the first time
- Extending the harness to a second project or codebase

**The principle:** don't try to do everything. Identify the highest-leverage gap and close it first. The compound effect is real — each improvement makes the next one easier.

## The Path to the Advanced Workshop

This workshop brought you to functional fluency. The advanced workshop goes further:

### Quantitative Evals

Evals-as-code: building a test suite for agent output quality. Scoring functions, regression testing, automated evaluation pipelines. Moving from "does this look right" to "does this score above the threshold."

### Memory and State Management

Short-term vs. long-term memory. Summarization vs. truncation. Building agents that maintain coherent state across long-horizon tasks without losing context fidelity.

### Multi-Agent Orchestration

Designing systems where multiple specialized agents coordinate to complete complex tasks. Orchestrator patterns, handoff protocols, consistency across agent boundaries.

### Autonomous Agents

Production-grade autonomous operation. Monitoring, kill switches, escalation patterns, audit trails. Building agent workflows you can actually trust to run unsupervised.

### Building the Production Environment

The full infrastructure for agent workflows at scale: tooling, environment design, CI integration, observability. Moving from individual developer productivity to team-scale harness engineering.

---

## The Thing That Doesn't Change

The technical details will evolve. Models will get better. Tools will change. Protocols will be updated.

The underlying skill — designing environments that produce reliable outcomes from probabilistic systems — doesn't change. That's what you've been building.

Bring it to real work. Find the gaps. Close them one at a time.

The harness is never done. It just gets better.
