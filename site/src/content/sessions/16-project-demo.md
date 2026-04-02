---
title: "Project Demo"
session: 16
week: 5
weekTheme: "The Capstone Skill"
duration: "60 min"
order: 16
status: "planned"
objectives:
  - "Demonstrate the expense tracker app with the agent infrastructure built throughout the workshop"
  - "Articulate how the skills from each week connect and compound in real work"
  - "Identify what changed in how they approach AI-assisted development"
coreTeachingMoment: >
  Each learner demos their app — not just the features, but the AGENTS.md,
  scoped rules, skills, and at least one agent-executed spec. The demo is a
  proof of the harness, not just the product.
takeaway: "A clear picture of how the skills you've built connect and compound in real work."
isRetro: false
---

## What You're Demonstrating

This is not a product demo. You're not here to show that your expense tracker has a working search endpoint.

You're here to show **the harness** — the full infrastructure you built over five weeks that enables reliable, repeatable agent-assisted development.

The app is evidence that the harness works. The harness is the achievement.

## The Demo Structure

### 1. The Repository Tour (10 min)

Walk through the repository structure:

- **AGENTS.md** — show the routing table, the global rules, the identity section. Explain one rule you wrote and what failure mode it prevents.
- **`docs/rules/`** — show at least one scoped rule file. Explain when it loads and why it's scoped rather than global.
- **`docs/skills/`** — show at least one skill file. Explain the task it encodes and why a skill was needed rather than a rule.
- **`docs/architecture/`** — show the architecture documentation you externalized. Explain what knowledge it captures that used to live only in your head.

### 2. The Harness in Action (15 min)

Live demonstration of the harness working:

- Show a task being executed by the agent with the harness in place
- Show the agent loading the correct scoped rules for the task
- Show at least one mechanical constraint catching a violation (or preventing one)
- Show the response format being enforced across endpoints

### 3. Spec Execution (15 min)

Run the spec you wrote in session 15 live:

- Show the spec
- Walk through the acceptance criteria
- Run the agent against the spec
- Show the proof of work: tests passing, HTTP records, type checking clean

This is the capstone demonstration. A spec written by a human, executed by an agent, verified against explicit criteria.

### 4. The Reflection (20 min)

Each participant answers:

1. **Week 1 you vs. Week 5 you** — what would week 1 you have done when the agent produced wrong output? What do you do now?

2. **The most valuable change** — of everything you built (rules, scoped rules, skills, architecture docs, enforcement), which single change had the most impact on the quality of agent output?

3. **The gap you'd close first** — what's the highest-leverage harness improvement you'd make in the next two weeks?

4. **Where this goes next** — what kind of work would you tackle with this infrastructure in place that you wouldn't have attempted before?

## What "Done" Looks Like

The expense tracker, at the end of week 5, should have:

- All required endpoints working and tested
- A complete AGENTS.md with routing table
- At least three scoped rule files covering the major contexts
- At least two skill files
- Architecture documentation for the key components
- At least one automated architectural constraint
- At least one agent-executed spec with proof of work

Not because those are the arbitrary requirements of a workshop. Because that's what a harness-engineered codebase looks like — and you've built one.

## The Connection Across Five Weeks

| Week | What you built | How it connects |
|------|---------------|-----------------|
| 1 | Mental models, system prompts | The foundation for everything that follows |
| 2 | Rules, scoped rules, skills | The behavioral constraints in the harness |
| 3 | AGENTS.md, tool chains | Persistent behavior, external capabilities |
| 4 | Context engineering, enforcement, auditing | The harness architecture |
| 5 | Specs, proof of work | The workflow that uses the harness |

The skills compound. A spec executed without a harness is fragile. A harness without specs is incomplete. Together, they're the basis for reliable AI-assisted development at scale.
