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

Tokenization is **not arbitrary**—it's optimized for efficiency and handling unknown words. For example:
- Models use **Byte-Pair Encoding (BPE)** or **WordPiece** to split text into common subword units.
- **Foreign languages** (e.g., German compound words) often require **more tokens** per word than English.
- **Code** (e.g., `def calculate_sum(a, b):`) is **highly dense**—it uses fewer tokens per word because of predictable patterns and minimal natural language.
- **Numbers, symbols, and emojis** are treated as distinct tokens (e.g., `€` = 1 token, `123` = 3 tokens).

**The 750 Words / 1,000 Tokens Rule (and Why It's Not Fixed)**

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
- **Quality**: Overloading the context window with dense content (e.g., code) *reduces* the available tokens for the model's response, degrading output quality.
- **Debugging**: If a model "forgets" your instructions, check if your prompt exceeded the context window—**it's not a memory issue; it's a token overflow**.

## The Context Window: Your Session's Finite Memory

### The Core Concept

The **context window** is the **maximum amount of text** (in tokens) a model can process *simultaneously* during a single session. It's **not a memory bank**—it's a **sliding buffer** that fills as you interact. Everything included in the window is **literally the only information the model has access to**:

| **Content Included**               | **Example**                                  |
|------------------------------------|----------------------------------------------|
| **System prompt**                  | "You are a helpful coding assistant."          |
| **User messages**                  | "Write a Python function to sort a list."     |
| **Model responses**                | "Here's a bubble sort implementation:..."     |
| **Tool inputs/outputs**            | `File: data.csv (100 tokens)`                 |
| **Pasted content**                 | "Paste of a 500-word research paper"          |

### Key Mechanics

- **Finite Size**: Most models have fixed limits (e.g., GPT-4: 128,000 tokens; Claude 3: 200,000 tokens).
- **No Persistence**: If you start a new chat session, **all prior context is erased**—the model has *zero* memory of past conversations.
- **Filling the Window**:
  - *Example*: A 10,000-token system prompt + 10 user messages (500 tokens each) = **60,000 tokens**. If your model's window is 64,000 tokens, you have **4,000 tokens left** for the model's response.
  - *Consequence*: If you paste a 10,000-token file, **your prompt might get truncated** to fit the window.

**Why "No Memory" is Critical**
> *"The model has no memory outside the context window. If you started a conversation three days ago and start a new session today, the model knows nothing from that prior session unless you include it."*
This is **not a limitation**—it's a **design principle** for privacy, cost control, and avoiding hallucinations. Models **cannot** "remember" past sessions; they only process what's in the current window.

## Auto-Compaction: The "Save Space" Feature (With Hidden Costs)

### How It Works

When the context window nears capacity, **some models/engines automatically summarize older content** to make room for new input. This is **auto-compaction** (e.g., OpenAI's "context compression" in GPT-4).

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


Tokens are the **currency of the model's understanding**, and the context window is its **only working memory**. Misunderstanding these concepts leads to **unexpected costs, poor quality, and wasted effort**. By treating tokens as *numbers* (not words) and the context window as a *strict physical limit*, you transform from a casual user into a **strategic prompt engineer**.

> *"The model doesn't 'read' your text—it processes a sequence of numbers. Your job is to optimize that sequence for cost, clarity, and completeness."*

## Action Items: Prompts to Observe Token Behavior

Pick one or more of these prompts and run them in an LLM interface with a **token counter visible** (e.g., Claude's usage panel, OpenAI's API dashboard). For each, **observe the gap between what you expect the cost to be and what it actually costs**.

### 1. The "Invisible Overhead" Hook

**Prompt**: What's 2+2?

**Why this works**: Seems trivial (3 tokens expected), but the counter will show 1,000+ tokens once system prompt, project context, and tool definitions are included. The hook: Reality vs. expectation gap.

---

### 2. Prose vs. Code Comparison

**Prompt A (Prose)**:
```
Write me a function that takes a list of numbers and returns the sum of all the numbers in that list. The function should be written in Python and should work with both positive and negative numbers.
```

**Prompt B (Code)**:
```
def sum_list(nums):
  return sum(nums)
```

**Why**: Prompt A uses ~40 tokens; Prompt B (pasted code to explain) uses ~12 tokens. Learners see the 3–4× token difference for the same semantic content.

---

### 3. Repetition Penalty

**Prompt**: Write a function to sort a list. Write a function to sort a list. Write a function to sort a list.

**Why**: Demonstrates that repeating the same phrase doesn't triple the cost—compression kicks in. Compare the token count to a single-request version.

---

### 4. Dense Content (Technical Jargon)

**Prompt**: Explain quantum entanglement, superposition, decoherence, and the no-cloning theorem in the context of quantum error correction codes and topological quantum computing.

**Why**: Uses uncommon words that fragment into many subword tokens. Compare token count to a simpler explanation of the same concepts.

---

### 5. Multilingual Comparison

**Prompt A (English)**:
```
Hello, how are you today?
```

**Prompt B (Mixed Language)**:
```
Bonjour, comment allez-vous aujourd'hui? Können Sie mir bitte helfen?
```

**Why**: Non-English text uses 40–60% more tokens per word. Learners see the cost of language diversity.

---

### 6. The File Paste Reality Check

**Prompt**: [Paste a large file here—e.g., 10KB JSON or a code repository]

Now, summarize this in 2 sentences.

**Why**: Shows that adding a 5,000-token file means 5,000+ tokens are consumed before the model even starts answering. Reveals why "quick questions" on big projects aren't quick.

---

### 7. The Auto-Compaction Trigger

**Prompt**: Start a long conversation with repeated questions:

- Question 1: What is machine learning?
- [Then ask 10–15 follow-up questions in sequence, each adding ~500 tokens]

**Why**: Learners watch the counter approach the context window limit and observe when auto-compaction kicks in (if the platform supports it).

---

### 8. System Prompt + Minimal Query

**Setup**: Activate a system prompt like "You are a legal expert. Provide all responses in formal legalese."

**Prompt**: Is this contract valid?

**Why**: The 3-token question balloons to 200+ tokens once the system prompt is included. Perfect for demonstrating the "invisible baseline" cost.

---

### 9. Instruction Bloat

**Prompt A (Minimal)**:
```
Write a Python function to reverse a string.
```

**Prompt B (Verbose)**:
```
I need you to write a Python function that takes a string as input and returns a new string with the characters in reverse order. The function should handle edge cases like empty strings and strings with special characters. Please include comments explaining each step. Also, write unit tests for the function. Make sure the code is PEP 8 compliant and follows Python best practices. The function should be efficient and readable.
```

**Why**: Learners see that Prompt B uses 3–5× more tokens to ask for the same thing. Demonstrates the cost of verbosity.

---

### 10. The Context Window Limit (Advanced)

**Prompt**: Ask a complex question, then paste incrementally larger documents/code snippets until the model's response quality degrades or cuts off.

**Why**: Shows the finite nature of the context window and when quality degrades due to token overflow.

---

## Observation Framework

For each prompt, track these metrics:

| **Metric** | **What to observe** |
|---|---|
| **Token count before my input** | Baseline overhead (system prompt + context) |
| **Token count after my input** | Your question's actual cost |
| **Expected vs. actual** | Did it match your intuition? |
| **Response quality** | Did you get a full answer, or was it cut off? |

**Reflection**: For each prompt, ask yourself: *Did the actual token cost match my expectation? If not, why?* This is the core insight of the session.
