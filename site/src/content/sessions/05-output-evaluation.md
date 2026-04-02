---
title: "Output Evaluation"
session: 5
week: 2
weekTheme: "Tell the Model What It Can and Can't Do"
duration: "30 min"
order: 5
status: "planned"
objectives:
  - "Apply a three-point review protocol to any LLM-generated output"
  - "Identify SID violations, pattern deviations, and over-engineering in realistic code output"
  - "Develop the instinct to read LLM output critically before acting on it"
coreTeachingMoment: >
  A purpose-built FastAPI endpoint output that contains all three failure types
  simultaneously. Learner reads it independently for 7 minutes, then the
  three-strike debrief reveals what they found and what they missed.
takeaway: "A structured protocol for catching what you'd normally skim and ship."
isRetro: false
---

## The Problem with Shipping LLM Output Unchecked

LLM-generated code is fluent. It compiles. It might even pass a basic test. That fluency is the danger — it creates the illusion of correctness.

The three most common failure categories in LLM output are not syntax errors. They're architectural errors that look like reasonable code until you know what to look for.

## The Three-Point Review Protocol

### Point 1: SID — Structural Integrity Check

Check for violations of three foundational principles:

**Single Responsibility Principle**
Does each function, class, and module do exactly one thing? LLMs frequently produce functions that validate input, transform data, persist to the database, and format a response — all in one block.

**Interface Segregation**
Are interfaces narrow and purpose-specific? LLMs tend to pass large objects when only a few fields are needed, coupling components unnecessarily.

**Dependency Inversion**
Does the code depend on abstractions rather than concrete implementations? LLMs often hardcode dependencies directly instead of injecting them, making the code difficult to test and modify.

### Point 2: Patterns — Architectural Conformance

Did the model follow the patterns of *your* project, or did it invent its own?

This is the failure mode that's hardest to catch without context. The code may be well-structured in isolation while violating every convention your codebase has established.

Check:
- Does it use the same response envelope pattern as existing endpoints?
- Does it follow the same error handling approach?
- Does it use the same ORM patterns (repository pattern, direct session usage, etc.)?
- Does naming match existing conventions?

LLMs default to their training data patterns, not yours.

### Point 3: Simplicity — Over-Engineering Check

Did the model reach for complexity where a simpler solution would have worked?

Common over-engineering signals:
- Abstract base classes for something that will have one implementation
- Factory patterns for objects with no variation
- Custom exception hierarchies for standard error cases
- Generic type parameters on non-generic code
- Design patterns applied where plain functions would suffice

**The test:** Can you explain why the complexity is needed? If not, it probably isn't.

## The Seven-Minute Read

Before any debrief or discussion, read the output independently. The exercise:

1. Set a 7-minute timer
2. Read the output as if you're reviewing a colleague's pull request
3. Mark every issue you find with the protocol category: SID, Pattern, or Simplicity
4. Note what you *almost* missed

The debrief compares notes. The gaps between what you found and what you missed are the skill gaps to close.

## Building the Instinct

The protocol is a scaffold, not a permanent checklist. The goal is to internalize it until critical reading becomes automatic — until you notice the God function, the pattern deviation, and the unnecessary abstraction before you consciously check for them.

That instinct is built by running the protocol deliberately, repeatedly, until it runs on its own.
