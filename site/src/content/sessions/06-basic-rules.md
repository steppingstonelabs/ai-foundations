---
title: "Basic Rules"
session: 6
week: 2
weekTheme: "Tell the Model What It Can and Can't Do"
duration: "60 min"
order: 6
status: "planned"
objectives:
  - "Distinguish between rules that actually change model behavior and rules that only sound correct"
  - "Identify the three properties of a well-written rule: specific, consequential, and testable"
  - "Write rules that directly address the failure modes identified in session 5"
  - "Assemble a working set of basic rules ready to use immediately"
coreTeachingMoment: >
  Part 1 — sort 10 pre-built rules into good and bad, building the judgment
  for what makes a rule effective. Part 2 — return to the session 5 output
  and write the rules that would have prevented each of the three strikes.
takeaway: "A working rulebook built from real failure modes."
isRetro: false
---

## What Makes a Rule Effective?

A rule is a constraint you encode in your system prompt or AGENTS.md that changes how the model behaves. Not all rules are equal. Most rules that developers write are ineffective — they sound correct but don't change anything.

The test of a rule is simple: **does the model behave differently with it than without it?**

## The Three Properties of a Well-Written Rule

### 1. Specific

A specific rule names a concrete behavior, not an aspiration.

**Not specific:**
> "Write clean code."

**Specific:**
> "Each function must do exactly one thing. If a function validates input *and* persists data, split it."

The specific version gives the model something it can check against while generating.

### 2. Consequential

A consequential rule applies to something that actually matters in practice. Rules about things the model rarely does wrong are wasted tokens.

Focus your rules on the failure modes you've actually observed — the patterns from session 5's output, the issues that come up repeatedly in your codebase.

### 3. Testable

A testable rule is one you can verify. You should be able to look at the output and determine whether the rule was followed.

**Not testable:**
> "Be thoughtful about error handling."

**Testable:**
> "Every endpoint must return errors in the format `{'data': null, 'error': {'code': str, 'message': str}}`."

You can check whether a given output follows the second rule. You cannot check whether it followed the first.

## The Rule Sorting Exercise

Ten pre-built rules, each labeled A through J. Sort each into **effective** or **ineffective**:

| Category | Examples |
|----------|---------|
| Too vague | "Write good code", "Be helpful" |
| Not testable | "Handle edge cases", "Think carefully" |
| Not consequential | Rules for patterns the model gets right anyway |
| Well-written | Specific, consequential, verifiable constraints |

The sorting exercise builds the judgment before you start writing rules of your own.

## Connecting Rules to Failure Modes

The most reliable source of rules is your own observed failures. Return to the session 5 output — the purpose-built FastAPI endpoint with three strikes.

For each strike, write the rule that would have prevented it:

1. **SID violation** → What rule would have constrained the structure?
2. **Pattern deviation** → What rule would have enforced the project's conventions?
3. **Over-engineering** → What rule would have required simplicity?

Rules written from real failures are almost always better than rules written from first principles. You know exactly what they're guarding against.

## A Starter Rulebook Structure

```markdown
## Code Structure
- [SID rules here]

## Project Patterns
- [Pattern conformance rules here]

## Simplicity
- [Anti-over-engineering rules here]

## Output Format
- [Response format, naming, structure rules here]

## What to Refuse
- [Out-of-scope operations, destructive actions]
```

By the end of this session, every line in your rulebook should be specific, consequential, and testable — and traceable to a failure mode you've actually seen.
