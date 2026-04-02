---
title: "Model Selection & Assignment Brief"
session: 4
week: 1
weekTheme: "How LLMs Actually Work"
duration: "30 min"
order: 4
status: "planned"
objectives:
  - "Describe the tradeoffs between Claude Haiku, Sonnet, and Opus across capability, cost, and latency"
  - "Explain what extended thinking is and when it's worth the cost"
  - "Match a task type to the right model based on complexity, latency, and budget"
  - "Develop the judgment to stop defaulting to the most capable model for every task"
coreTeachingMoment: >
  The same architectural analysis prompt run across all four configurations.
  Learner compares output quality, response time, and cost side by side.
takeaway: "The judgment to pick the right model — not just the most capable one."
isRetro: false
---

## The Four Configurations

Claude comes in configurations with different tradeoffs. Choosing correctly is a skill worth developing early.

### Claude Haiku — Fast, Cheap, High Volume

Best for: classification, extraction, summarization, simple Q&A, routing decisions, repetitive batch tasks.

- Lowest cost per token
- Lowest latency (often sub-second)
- Strong enough for well-constrained, bounded tasks
- Not the right tool for complex reasoning or multi-step planning

**Rule of thumb:** If the task has a clearly correct answer and doesn't require synthesis or judgment, Haiku is usually sufficient.

### Claude Sonnet — Balanced Capability

Best for: most coding tasks, code review, test writing, documentation, multi-step reasoning, the bulk of daily work.

- Significantly more capable than Haiku
- Reasonable cost at reasonable latency
- The default for most development workflows

**Rule of thumb:** When in doubt, start here. Most professional coding tasks don't require more.

### Claude Opus — Maximum Capability

Best for: complex architectural reasoning, nuanced judgment calls, long-horizon planning, tasks where quality matters more than cost or speed.

- Highest capability
- Highest cost, higher latency
- Overkill for routine tasks

**Rule of thumb:** Reserve for genuinely complex problems where the quality difference justifies the cost.

### Claude Opus + Extended Thinking — Deliberate Reasoning

Extended thinking gives the model time to reason step-by-step before producing an answer. It's not magic — it's structured deliberation.

Best for: hard design problems, architectural tradeoffs, situations where the model needs to reason through competing constraints before committing.

- Most expensive configuration
- Slowest (by design — it's thinking)
- Produces more reliable results on genuinely difficult problems

**Rule of thumb:** When you'd want a senior engineer to "take 20 minutes to think before answering," extended thinking is worth it.

## The Tradeoff Matrix

| Configuration | Capability | Cost | Latency | Best Use |
|--------------|------------|------|---------|----------|
| Haiku | ★★☆☆☆ | $ | Fast | Volume, simple tasks |
| Sonnet | ★★★★☆ | $$ | Medium | Most development work |
| Opus | ★★★★★ | $$$$ | Slow | Complex reasoning |
| Opus + Extended Thinking | ★★★★★+ | $$$$$ | Very Slow | Hard design problems |

## The Judgment to Develop

The goal is not to know the spec sheet. It's to build the instinct that says:

> "This is a classification task — Haiku. This is a multi-file refactor — Sonnet. This is an architectural decision with long-term consequences — Opus."

Defaulting to the most capable model for every task is like using a sledgehammer for every nail. It works, but it's wasteful, and it teaches you nothing about the tools.

## Week 1 Assignment: Personal Expense Tracker API

This is the project you'll build before session 5. It becomes the sandbox for everything in weeks 2–5.

**Stack:** Python 3.11+, FastAPI, SQLAlchemy 2.0, Pydantic v2, PostgreSQL, pytest

**Required features:**
- User model with basic auth
- Expense model (amount, category, date, description)
- `POST /expenses` — create an expense
- `GET /expenses` — list expenses
- `GET /expenses?category=food` — filter by category
- `GET /expenses/total` — totals with filters
- Standard response envelope: `{"data": ..., "error": null}`
- Basic test suite (happy path per endpoint)

**The point:** Build this using the skills from sessions 1–4. Pay attention to token costs, apply what you've learned about prompting, and write at least a basic system prompt for your coding assistant. The app doesn't need to be perfect — it needs to exist and run. You'll be iterating on it for the next four weeks.
