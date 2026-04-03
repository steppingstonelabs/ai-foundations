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

## Tokens: The Fundamental Building Blocks of Model Processing

### Beyond Words: The True Unit of Understanding**

A token is **not a word, a character, or a sentence**—it is the **smallest unit of text a language model processes and generates**. Think of tokens as the "atoms" of language that the model *actually* interprets. Crucially, tokenization is **subword-based**, meaning models break text into predictable fragments (e.g., prefixes, suffixes, common word parts) rather than treating whole words as single units. This is why:

- **"unbelievable"** often splits into **2 tokens**: `un` + `believable` (or similar subword units).
- **"a"** is **1 token** (a very common subword).
- **"Hello!"** might be **3 tokens**: `Hello` + `!` (punctuation is often a separate token).
- **Spaces** are typically **part of the token** (e.g., the space before "world" in "hello world" is included in the "hello" token, not a separate token).

### Why Tokenization Matters

Tokenization is **not arbitrary**—it’s optimized for efficiency and handling unknown words. For example:
- Models use **Byte-Pair Encoding (BPE)** or **WordPiece** to split text into common subword units.
- **Foreign languages** (e.g., German compound words) often require **more tokens** per word than English.
- **Code** (e.g., `def calculate_sum(a, b):`) is **highly dense**—it uses fewer tokens per word because of predictable patterns and minimal natural language.
- **Numbers, symbols, and emojis** are treated as distinct tokens (e.g., `€` = 1 token, `123` = 3 tokens).

**The 750 Words / 1,000 Tokens Rule (and Why It’s Not Fixed)**

The common ratio of **~750 words per 1,000 tokens** is a *rough average* for **English prose**. However, the actual token density **varies significantly**:
| **Content Type**       | **Tokens per Word** | **Reason**                                  |
|------------------------|---------------------|---------------------------------------------|
| English Prose          | ~1.3 tokens         | Standard word-based tokenization            |
| Code (Python/JS)       | **~0.7 tokens**     | High predictability, minimal punctuation    |
| Technical Jargon       | ~1.5 tokens         | Uncommon words split into subwords          |
| Multilingual Text      | ~1.6 tokens         | Non-English words often require more tokens |
| Long Repeated Phrases  | **↓↓↓ (compressed)**| Models recognize patterns (e.g., "the the the" = 1 token for repetition) |

**Practical Implications**
- **Cost**: If you pay per token (e.g., $0.0001 per token), a 500-word report might cost **650 tokens** (not 500), while a 500-line code snippet could cost **350 tokens**.
- **Quality**: Overloading the context window with dense content (e.g., code) *reduces* the available tokens for the model’s response, degrading output quality.
- **Debugging**: If a model "forgets" your instructions, check if your prompt exceeded the context window—**it’s not a memory issue; it’s a token overflow**.

## The Context Window: Your Session's Finite Memory

### The Core Concept

The **context window** is the **maximum amount of text** (in tokens) a model can process *simultaneously* during a single session. It’s **not a memory bank**—it’s a **sliding buffer** that fills as you interact. Everything included in the window is **literally the only information the model has access to**:

| **Content Included**               | **Example**                                  |
|------------------------------------|----------------------------------------------|
| **System prompt**                  | "You are a helpful coding assistant."          |
| **User messages**                  | "Write a Python function to sort a list."     |
| **Model responses**                | "Here’s a bubble sort implementation:..."     |
| **Tool inputs/outputs**            | `File: data.csv (100 tokens)`                 |
| **Pasted content**                 | "Paste of a 500-word research paper"          |

### Key Mechanics

- **Finite Size**: Most models have fixed limits (e.g., GPT-4: 128,000 tokens; Claude 3: 200,000 tokens).
- **No Persistence**: If you start a new chat session, **all prior context is erased**—the model has *zero* memory of past conversations.
- **Filling the Window**:
  - *Example*: A 10,000-token system prompt + 10 user messages (500 tokens each) = **60,000 tokens**. If your model’s window is 64,000 tokens, you have **4,000 tokens left** for the model’s response.
  - *Consequence*: If you paste a 10,000-token file, **your prompt might get truncated** to fit the window.

**Why "No Memory" is Critical**
> *"The model has no memory outside the context window. If you started a conversation three days ago and start a new session today, the model knows nothing from that prior session unless you include it."*
This is **not a limitation**—it’s a **design principle** for privacy, cost control, and avoiding hallucinations. Models **cannot** "remember" past sessions; they only process what’s in the current window.

## Auto-Compaction: The "Save Space" Feature (With Hidden Costs)

### How It Works

When the context window nears capacity, **some models/engines automatically summarize older content** to make room for new input. This is **auto-compaction** (e.g., OpenAI’s "context compression" in GPT-4).

**The Hidden Costs**
1. **Token Cost**:
   - Summarizing 10,000 tokens costs **~500–1,000 tokens** (the cost of the summary itself).
   - *Example*: A 10,000-token chat history might be summarized to 500 tokens, but the *summarization step* uses 700 tokens.
2. **Information Loss**:
   - The model **sees the summary, not the original**. Key details (e.g., "Use Python 3.10+ for async") might become "Use modern Python."
3. **Quality Degradation**:
   - Poor summaries lead to **inaccurate responses**. *Example*: A summary missing "use TLS 1.3" might cause the model to suggest insecure protocols.

### The "Hook" Explained

> *"Ask one question inside an active project. Watch the token counter. The number is almost always higher than people expect."*
- **Why?** The counter includes:
  - **System prompt** (e.g., 50 tokens for "You are a legal expert").
  - **Project context** (e.g., 1,000 tokens from a past document).
  - **Tool definitions** (e.g., 200 tokens for "Use the `fetch_data()` API").
  - *Your question* (e.g., 50 tokens).
- **Total**: **1,300+ tokens** before you type a single word. A "simple" question might consume **10% of a 128k window**.

## Why This Knowledge is Transformative

1. **Cost Optimization**:
   - **Code** = cheaper to process than text. *Strategy*: Paste code snippets instead of describing them.
   - **Avoid repetition**: Trim verbose instructions (e.g., "Write a function that sorts a list" → "Sort list function").
2. **Quality Control**:
   - **Never assume** the model "remembers" past context—restate key details in *every* prompt.
   - **Monitor token counters** before pasting large files.
3. **System Design**:
   - For apps, **pre-summarize long contexts** (e.g., "Summarize last 500 messages") *before* sending to the model, to avoid auto-compaction losses.
4. **Debugging**:
   - If responses are incoherent, **check if the context window was exceeded**—not a model "glitch."

## Key Takeaways

| Concept | What to remember |
|---------|-----------------|
| Token ≠ word | Roughly 4 chars per token for English prose |
| Context window | Finite, fills from message 1, doesn't reset |
| Dollar cost | Every session has a real cost you can observe |
| Auto-compaction | Triggered near the limit; costs tokens and loses fidelity |


Tokens are the **currency of the model’s understanding**, and the context window is its **only working memory**. Misunderstanding these concepts leads to **unexpected costs, poor quality, and wasted effort**. By treating tokens as *numbers* (not words) and the context window as a *strict physical limit*, you transform from a casual user into a **strategic prompt engineer**.

> *"The model doesn’t ‘read’ your text—it processes a sequence of numbers. Your job is to optimize that sequence for cost, clarity, and completeness."*



