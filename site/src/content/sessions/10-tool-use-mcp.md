---
title: "Tool Use / MCP & Function Calling"
session: 10
week: 3
weekTheme: "Making Behavior Persistent"
duration: "60 min"
order: 10
status: "planned"
objectives:
  - "Explain what MCP is and how tool definitions load into the context window"
  - "Describe the tool call loop — how a model decides to call a tool, what it sends, and how the result feeds back into context"
  - "Design a multi-tool chain connecting GitHub and Slack"
  - "Identify the failure points in a tool chain and reason about how to handle them"
  - "Understand the token cost of tool definitions"
coreTeachingMoment: >
  Design the chain before running it, run it and narrate every tool call,
  then deliberately break it by misconfiguring Slack. Partial failure surfaces
  the hardest design constraint in agentic tool use.
takeaway: "The design principles for tool chains that are safe to run in production."
isRetro: false
---

## What Is MCP?

MCP (Model Context Protocol) is a standard for connecting language models to external tools. It defines how tools are described, how the model requests tool calls, and how results are returned.

When you connect an MCP server to an agent, the tool definitions load into the context window alongside your system prompt and user messages. The model reads them and can invoke them when relevant.

**The hidden cost:** Tool definitions are tokens. A fully loaded MCP configuration with dozens of tools can consume thousands of tokens before you've typed a single message. This matters for budgeting and for performance.

## The Tool Call Loop

Understanding this loop is essential for reasoning about what can go wrong.

```
1. Model reads the prompt and decides a tool call is needed
      ↓
2. Model outputs a structured tool call request
      ↓
3. The tool executes OUTSIDE the model (in your environment)
      ↓
4. The result is injected back into the context window
      ↓
5. Model reads the result and decides what to do next
      ↓
6. Repeat until the task is complete
```

**Critical insight:** The model doesn't execute tools. It *requests* tool calls. Your environment executes them. The model only sees the results after they've been injected back into the context.

This distinction matters for error handling. If a tool fails silently, the model may not know it failed. If a tool returns a misleading success response, the model will proceed as if the operation succeeded.

## Designing a Multi-Tool Chain

The example chain: code review → PR comments → Slack notification

**Tools needed:**
- `github.list_pull_requests` — find open PRs
- `github.get_pull_request_diff` — read the code
- `github.create_review_comment` — post the review
- `slack.post_message` — notify the team

**Designing before running:**

Before executing, map the chain:
1. What does each tool need as input?
2. What does each tool return?
3. Which outputs feed into subsequent inputs?
4. What happens if any step fails?

A chain designed on paper is easier to debug than one designed by trial and error.

## Failure Points in Tool Chains

Every step in a tool chain is a potential failure point. The design challenge is deciding how the agent should behave when a step fails.

**Failure modes:**

| Type | Example | Risk |
|------|---------|------|
| Tool unavailable | MCP server not running | Chain stops; model may not detect |
| Auth failure | Expired token | Silent failure or misleading error |
| Wrong input | Malformed PR number | Tool rejects call; model may retry incorrectly |
| Partial success | Review posted, Slack fails | Half-done state; inconsistent reality |
| Silent success | Tool claims success but didn't execute | Model proceeds on false assumption |

**The partial failure problem is the hardest.** The chain ran. GitHub got the review. Slack didn't get the notification. The model reported success. The team never saw it.

## The Deliberate Break Exercise

Run the chain successfully. Then misconfigure Slack — wrong channel, expired token, or wrong payload format. Run it again.

Observe:
- Does the model detect the failure?
- Does it report partial success or total failure?
- Does it attempt recovery?
- What state is the system in after the failed run?

The answers reveal the design constraints that matter in production: explicit failure handling, idempotent operations, and confirmation requirements before irreversible steps.

## Design Principles for Production Tool Chains

1. **Require confirmation before irreversible operations** — posting a review, sending a notification, merging a PR
2. **Treat partial failure as total failure** — if any step fails, surface it clearly
3. **Make operations idempotent where possible** — running the chain twice should produce the same result
4. **Log tool inputs and outputs** — the context window is your audit trail
5. **Cap retry depth** — a model that retries a failing tool indefinitely is a runaway agent
