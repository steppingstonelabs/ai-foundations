---
title: "Modes & the System Prompt"
session: 3
week: 1
weekTheme: "How LLMs Actually Work"
duration: "30 min"
order: 3
status: "planned"
objectives:
  - "Explain what a system prompt is and how it differs from a user prompt"
  - "Describe how the system prompt shapes every subsequent interaction in a session"
  - "Identify what makes a system prompt weak or ineffective"
  - "Write a system prompt that produces consistent, reliable behavior from a code writing assistant"
coreTeachingMoment: >
  The same user message run against three system prompts — none, vague, and
  learner-written. The contrast between versions 1 and 3 is the lesson.
takeaway: "Replace the model's defaults with something that works for you."
isRetro: false
---

## What Is a System Prompt?

The system prompt is a set of instructions loaded into the context window **before** any user message. It defines the model's role, behavior, constraints, and defaults for the entire session.

The user prompt is what you type in the message box. The system prompt is what tells the model how to interpret and respond to every user message it receives.

**The key difference:**
- User prompt: "What's wrong with this function?"
- System prompt: "You are a code reviewer for a Python API project. Focus on correctness, simplicity, and adherence to the project's existing patterns. Do not rewrite unless asked — diagnose and explain."

Without the system prompt, the model uses its own defaults. With it, you control the defaults.

## How the System Prompt Shapes Everything

The system prompt persists for the entire session. Every user message is interpreted through its lens. This means:

- A system prompt that establishes "you are a senior Python engineer" will bias responses toward Python idioms and patterns
- A system prompt that says "be concise" will shorten every response
- A system prompt that says "do not modify files outside the `/src` directory" creates a constraint that applies to every action

The system prompt is the most powerful lever you have for consistent, predictable model behavior.

## What Makes a System Prompt Weak?

**Too generic:**
> "You are a helpful coding assistant."

This adds almost nothing. The model was already helpful and already knows about coding.

**Too abstract:**
> "Always write good code."

What is good code? This is meaningless without specifics.

**Missing the key constraints:**
A system prompt that doesn't specify what the model should *not* do is incomplete. The most important lines in a system prompt are often the "refuse these" lines.

**No context about the environment:**
The model doesn't know what language you're using, what frameworks are in play, what patterns matter, or what the architectural goals are. A weak system prompt leaves all of that to inference.

## Anatomy of a Strong System Prompt

A strong system prompt for a code writing assistant covers:

| Section | What to include |
|---------|----------------|
| Identity | Role, expertise level, primary task |
| Stack | Language, frameworks, key libraries |
| Architecture rules | What patterns to follow, what to avoid |
| Code quality rules | Style, naming, structure expectations |
| Output rules | Format, verbosity, what to include/omit |
| What to refuse | Operations outside scope, destructive actions |

## The Three-Version Comparison

Run the same user message — "Add a search endpoint to the expenses API" — against:

1. **No system prompt** — observe the model's defaults
2. **Vague system prompt** ("You are a helpful coding assistant") — observe marginal difference
3. **Your written system prompt** — observe the contrast

The gap between version 1 and version 3 is the value of the system prompt. Everything else in this workshop builds on that foundation.
