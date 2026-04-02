---
title: "Tokens & the Context Window"
session: 1
week: 1
weekTheme: "How LLMs Actually Work"
duration: "30 min"
order: 1
status: "planned"
objectives:
  - "Explain what a token is and how LLMs consume them"
  - "Understand that every interaction has a real dollar cost they can observe"
  - "Describe the context window as a finite shared resource that fills from the first message"
  - "Recognize what auto-compaction is, what triggers it, and what it costs"
coreTeachingMoment: >
  Learner asks one simple question inside a project and watches the token
  counter and dollar cost appear. The gap between what they expected it to
  cost and what it actually cost is the hook.
takeaway: "The mental model everything else builds on."
isRetro: false
---

## What Is a Token?

A token is not a word. It's the unit a language model actually sees. The word "unbelievable" might be two tokens. The word "a" is one. A newline is a token. A space before a word is often part of the token.

Most models process roughly **750 words per 1,000 tokens** — but that ratio shifts depending on the content. Code is denser. Repeated patterns compress. Foreign-language text often tokenizes less efficiently than English.

**Why this matters:** The model never sees your prose. It sees a sequence of numbers. Understanding that helps you reason about why some prompts cost more than others, and why response quality can degrade near the context limit.

## The Context Window

Think of the context window as a **finite scroll of paper** that begins the moment you start a session. Everything goes on the scroll:

- Your system prompt
- Every user message
- Every model response
- Tool call inputs and outputs
- File contents you paste in

The scroll fills up. When it's full, the model can't see the beginning anymore.

**Key fact:** The model has no memory outside the context window. If you started a conversation three days ago and start a new session today, the model knows nothing from that prior session unless you include it.

## Auto-Compaction

When the context window approaches its limit, some tools automatically compress older content to make room. This is called **auto-compaction**.

Auto-compaction is not free:
- It costs tokens to run the summarization
- Information is lost — the model sees a summary, not the original
- The quality of the summary affects everything that follows

**The hook:** Ask one question inside an active project. Watch the token counter. The number is almost always higher than people expect — because the system prompt, project context, and tool definitions are already loaded before you typed a single word.

## Practical Takeaways

| Concept | What to remember |
|---------|-----------------|
| Token ≠ word | Roughly 4 chars per token for English prose |
| Context window | Finite, fills from message 1, doesn't reset |
| Dollar cost | Every session has a real cost you can observe |
| Auto-compaction | Triggered near the limit; costs tokens and loses fidelity |
