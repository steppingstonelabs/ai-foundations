---
title: "Writing Specs for Agents"
session: 15
week: 5
weekTheme: "The Capstone Skill"
duration: "60 min"
order: 15
status: "planned"
objectives:
  - "Explain why a spec written for an agent is fundamentally different from a task description written for a human"
  - "Identify gaps in a spec — places where an agent would fill in arbitrarily"
  - "Write exhaustive Given → When → Then acceptance criteria that leave no room for agent inference"
  - "Specify proof of work requirements through HTTP records and Playwright scripts"
  - "Produce a complete, executable agent spec for a real task in their own project"
coreTeachingMoment: >
  A deliberately gapped spec for a password reset endpoint. Learner hunts for
  gaps before the spec is run, rewrites the acceptance criteria as proper
  Given → When → Then scenarios, then writes their own spec for a real task
  in their project.
takeaway: "The mindset shift that changes how you work with AI permanently."
isRetro: false
---

## Specs for Agents vs. Tasks for Humans

When you hand a task to a human developer, they bring implicit context:
- They've seen how the project works
- They'll ask questions when something is ambiguous
- They'll apply judgment when the spec doesn't cover a case
- They'll recognize when a decision feels wrong and flag it

When you hand a task to an agent, none of that happens. The agent has only what's in the context window. It will fill every gap with inference. It will not ask clarifying questions unless explicitly told to. It will not flag decisions that feel wrong — it will make them and move on.

**A spec for an agent must be exhaustive. A task description for a human can rely on judgment.**

## What a Complete Agent Spec Contains

### Objective

What the agent is being asked to accomplish, stated with precision.

Not: "Add password reset to the API."

Instead: "Implement a two-step password reset flow. Step 1: `POST /auth/reset-request` accepts an email and sends a reset token to that address. Step 2: `POST /auth/reset-confirm` accepts the token and a new password and updates the user's password hash."

### Scope

What is explicitly in bounds and what is explicitly out of bounds.

```
In scope:
- The two endpoints described above
- Token generation and storage
- Token expiry (24 hours)
- Password validation (min 8 chars, 1 uppercase, 1 number)

Out of scope:
- Email delivery (stub with a logged message)
- Rate limiting (documented as future work)
- Existing auth endpoints
```

### Relevant Modules

The exact files, classes, and functions to reference or modify.

```
Reference:
- src/models/user.py — User model (add reset_token, reset_token_expiry fields)
- src/repositories/user.py — UserRepository (add get_by_reset_token method)
- src/services/auth.py — AuthService (add request_reset, confirm_reset methods)

Create:
- src/routers/auth_reset.py — new router
- tests/test_auth_reset.py — test file
```

### Constraints

What the agent must not do.

```
- Do not modify the existing login or registration endpoints
- Do not use a third-party library for token generation — use secrets.token_urlsafe(32)
- Do not store plaintext tokens — hash with SHA-256 before persisting
```

### Acceptance Criteria

Exhaustive Given → When → Then scenarios that leave no room for inference.

```gherkin
Given a valid email address for an existing user
When POST /auth/reset-request is called with that email
Then the response is 200 with body {"data": {"message": "Reset email sent"}, "error": null}
And a reset token is stored in the user's record (hashed)
And the token has an expiry 24 hours from the request time

Given an email address that does not correspond to any user
When POST /auth/reset-request is called with that email
Then the response is 200 with body {"data": {"message": "Reset email sent"}, "error": null}
And no token is stored (security: do not reveal whether email exists)

Given a valid, unexpired reset token and a valid new password
When POST /auth/reset-confirm is called
Then the response is 200 with body {"data": {"message": "Password updated"}, "error": null}
And the user's password hash is updated
And the reset token is cleared from the user's record
```

### Proof of Work

The evidence the agent must produce to demonstrate the implementation is complete.

```
1. HTTP request/response records for each acceptance scenario (captured with httpx)
2. All tests in tests/test_auth_reset.py pass
3. mypy reports no type errors in modified files
```

## The Gap-Hunting Exercise

Before running a spec, read it as if you're the agent. For every decision the spec requires, ask: is the answer in the spec, or would you have to infer it?

Common gap locations:
- Error cases not covered by acceptance criteria
- Ambiguous field naming ("token" vs. "reset_token" vs. "password_reset_token")
- Unspecified behavior for edge cases (expired token, already-used token)
- Missing constraints on what not to touch

Every gap is a place where the agent will make a decision you didn't make. That decision may be reasonable. It may not be. A complete spec eliminates the variance.

## Writing Your Own Spec

For the session exercise: identify a real, bounded task in your expense tracker — a new endpoint, a data validation change, a new filter parameter — and write a complete spec for it.

The test: could you hand this spec to someone who has never seen your project and have them implement it correctly? If the answer is no, find the gaps and fill them.
