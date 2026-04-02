---
title: "Prompt Engineering"
session: 2
week: 1
weekTheme: "How LLMs Actually Work"
duration: "30 min"
order: 2
status: "planned"
objectives:
  - "Identify the four core failure modes in a poorly written prompt"
  - "Diagnose why a prompt failed before reaching for a fix"
  - "Apply targeted corrections that address the specific failure"
  - "Develop the instinct to read a prompt the way a model reads it"
coreTeachingMoment: >
  Four purpose-built broken prompts, each failing in a different way. Learner
  and coach diagnose each failure together before applying the fix.
takeaway: "A diagnostic framework you'll apply to every prompt you write."
isRetro: false
---

## The Four Failure Modes

Most prompt failures fall into exactly four categories. Once you can name the failure, the fix becomes obvious.

### Failure Mode 1: Too Vague

The model fills gaps with assumptions. If your prompt doesn't specify what you want, the model will decide for you — and its defaults may not match yours.

**Example of a vague prompt:**
> "Write a function to handle the data."

Which data? What kind of handling? What language? What should it return? The model will guess, and its guess might be plausible while being completely wrong for your context.

**The fix:** Be specific about what you want, in what format, with what constraints.

### Failure Mode 2: Missing Context

The model doesn't have what it needs to do the job. This is different from vagueness — you may have been very specific about *what* you want, but neglected to give the model the information it needs to produce it.

**Example:**
> "Refactor this function to follow our project patterns."

What patterns? The model can't follow conventions it hasn't seen.

**The fix:** Include the relevant context — existing code, architectural decisions, examples of the pattern you want.

### Failure Mode 3: No Output Format Specified

Right content, wrong shape. The model produces something correct but in a form you can't use.

**Example:**
> "List the edge cases for this function."

Did you want a bullet list? A numbered list with explanations? A table with severity ratings? A paragraph? The model will pick one, and it might not be what you need.

**The fix:** Specify the output format explicitly. "Return a markdown table with columns for edge case, expected behavior, and severity."

### Failure Mode 4: Assuming Knowledge the Model Doesn't Have

The model knows what it was trained on. It doesn't know your team's conventions, your codebase's history, your internal libraries, or decisions made after its training cutoff.

**Example:**
> "Use the standard approach we discussed."

What discussion? What standard? Even within a session, if you didn't include the prior context, the model may not have it.

**The fix:** Never assume shared context. State what you mean explicitly.

## The Diagnostic Protocol

Before you rewrite a prompt, ask:

1. **Was it too vague?** Did I leave gaps the model had to fill?
2. **Was context missing?** Did the model have everything it needed?
3. **Did I specify output format?** Did I tell it what shape to return?
4. **Did I assume knowledge?** Did I expect it to know something I didn't include?

One of those four is almost always the culprit. Fix the root cause — don't just add more words and hope.

## Reading a Prompt Like the Model Does

The model reads your prompt literally and sequentially. It doesn't infer intent. It doesn't know what you were thinking when you wrote it.

A useful exercise: read your prompt as if you've never seen the codebase, never met the person who wrote it, and have no idea what the goal is. What would you produce? If the answer is "I'd have to guess," the prompt needs work.
