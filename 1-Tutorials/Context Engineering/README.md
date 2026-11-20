# From Prompts to Environments: Understanding Production-Grade Context Engineering

This article builds directly on what we've just discussed about Agent Harnesses, RAG, memory management and token budgets.

Mastering Context Engineering: Retrieval, Hard Filters, and Multi-Turn Memory : https://www.youtube.com/watch?v=r7ZnrKCjVj4

> **My assessment:** The article presents a good production architecture, but some technical claims need qualification. Its central message is correct: production AI systems need to manage the entire information environment around an LLM, not just write better prompts.

Let's review it from a software architect's perspective, connecting it to your FastAPI + Ollama + Qdrant + Angular architecture.

---

## 1. The big shift: Prompt Engineering vs Context Engineering

These concepts are related, but they solve different problems.

| Prompt Engineering | Context Engineering |
| :--- | :--- |
| How should I instruct the LLM? | What information should the LLM receive? |
| Focuses on instructions | Focuses on the complete information environment |
| Defines behavior and output format | Manages prompts, history, memory, RAG and tools |
| Often static | Dynamically changes according to the task |

### Example

**User asks:**
> *"Why was my payment declined?"*

**Prompt engineering might define:**
> *"You are a banking assistant. Explain payment failures clearly."*

**Context engineering additionally determines:**
- Which transaction details should be retrieved?
- Which banking policies are relevant?
- Which previous conversation details matter?
- Which tools should be available?
- How many tokens can be allocated?
- Which information is verified and trustworthy?

> **The distinction is important:** A beautifully written prompt cannot compensate for missing or incorrect information.

---

## 2. Understanding the four-layer Context Engine

The article proposes four layers. These are useful architectural responsibilities, although a real implementation may combine or separate them differently.

### Layer 1: Retrieval Layer – The Librarian
*Core production capability*

The retrieval layer finds the knowledge needed to answer the user's question.

Suppose your banking application has 50,000 documents.

**The user asks:**
> *"Explain international payment failure codes."*

**The retrieval layer:**
1. Converts the question into an embedding.
2. Searches Qdrant for semantically similar content.
3. Performs keyword matching for exact failure codes.
4. Combines search results.
5. Reranks the results.
6. Returns the most relevant document chunks.

**Two important techniques:**
- **Semantic search:** Finds information based on meaning.
- **Hybrid search:** Combines semantic search with keyword search.

For example, a user searches for `ERR-4021`.  
A semantic search might find documents discussing payment failures but miss an exact error-code match. Keyword search helps find that exact code.

![Hybrid Retrieval Pipeline](Hybrid%20Retrieval%20Pipeline.jpg)

#### What is Semantic Chunking?

Traditional chunking might split documents every 500 characters. This can accidentally separate a heading from its explanation.

Semantic chunking tries to split documents at meaningful boundaries, such as:
- Paragraph boundaries.
- Topic changes.
- Section headings.
- Related concepts.

For your Qdrant project, I would start with heading-aware chunking and token-based chunk sizes, then evaluate semantic chunking against it.

---

### Layer 2: Memory Layer – The Secretary
*Core production capability*

This layer manages information from previous interactions.

The article correctly separates memory into two categories:

#### Short-term memory
**Recent conversation context:**
- **User:** Explain RAG.
- **Assistant:** RAG retrieves external knowledge.
- **User:** How does Qdrant work?

*Usually maintained as recent messages in the conversation.*

#### Long-term memory
**Important information retained across conversations:**
- Preferred programming language: Python
- Current project: Enterprise RAG Platform
- LLM preference: Local Ollama models
- Frontend preference: Angular

*Stored as structured records or searchable memories.*

#### A useful implementation:

| Component | Suggested technology |
| :--- | :--- |
| Recent conversation | PostgreSQL or Redis |
| Conversation summaries | PostgreSQL |
| Semantic memory retrieval | Qdrant |
| Memory extraction | LLM |
| Memory retrieval | Embedding + metadata filters |

> **One important architectural improvement:** Don't automatically turn every user statement into permanent memory.

For example, distinguish between:
- Verified facts.
- User preferences.
- Temporary instructions.
- Unverified claims.
- Sensitive information.

Memory should have provenance, timestamps and appropriate retention policies.

---

### Layer 3: Pruning and Compression – The Editor
*Important for scalability*

This is where the harness decides what information to remove, summarize or retain.

**Imagine:**
- 30 previous messages.
- 20 retrieved document chunks.
- 5 memory records.
- 15 available tools.

The combined context might exceed your token budget. The pruning layer reduces unnecessary information.

- **Technique 1: Summarization** — Instead of sending 30 old messages, summarize their important decisions and retain recent messages in full.
- **Technique 2: Deduplication** — If three retrieved documents repeat the same payment policy, avoid sending all three copies unless they provide distinct evidence.
- **Technique 3: Reranking** — Rank retrieved documents based on their usefulness for the current question.
- **Technique 4: Compression** — Compress verbose information while preserving important facts, numbers, constraints and references.

The article mentions using a smaller model such as Gemini Flash to summarize documents. That's one possible implementation, but it is not mandatory. You could use a local model through Ollama, a deterministic extraction process, or a cloud model depending on your latency, quality, privacy and cost requirements.

![Pruning and Compression – The Editor](Pruning%20and%20Compression%20–%20The%20Editor.jpg)

> **Important distinction:**
> Pruning and compression are not identical.
> - **Pruning** removes information.
> - **Compression** represents information more compactly.
> 
> Both can introduce information loss, so critical facts must be preserved and summaries should be traceable to their source.

---

### Layer 4: Controller – The Brain
*Orchestration and validation*

This layer assembles the final context and controls what happens next.

**For example:**
1. The retrieval layer returns three banking documents.
2. The memory layer returns two relevant preferences.
3. The conversation manager provides the last five messages.
4. The pruning layer removes redundant content.
5. The controller then constructs the final LLM request.

**It can also:**
- Attach source references.
- Check permissions.
- Validate retrieved information.
- Apply security policies.
- Decide whether more retrieval is needed.
- Manage the tool execution loop.

> **One clarification:** The controller is not necessarily another AI model. It can be ordinary application code, with optional LLM-based components for tasks such as summarization or classification.
> 
> The LLM remains responsible for reasoning and generating its response.

---

## 3. Understanding the pruning scoring formula

The article proposes:

$$Score = w_1R + w_2T + w_3D$$

**Where:**

| Variable | Meaning |
| :--- | :--- |
| $R$ | Semantic relevance |
| $T$ | Recency |
| $D$ | Information density |
| $w_1, w_2, w_3$ | Importance weights |

This is a useful conceptual model for deciding which information to retain.

### Example Scenario:

**User asks:**
> *"How does our payment retry mechanism work?"*

Suppose the context engine has these candidates:

| Information | Relevance | Recency | Density |
| :--- | :--- | :--- | :--- |
| Payment retry policy | 0.98 | 0.90 | 0.95 |
| Circuit breaker design | 0.93 | 0.85 | 0.90 |
| Database indexing | 0.30 | 0.95 | 0.60 |
| Old Angular styling discussion | 0.05 | 0.20 | 0.40 |

**Using illustrative weights:**
$$w_1 = 0.6, \quad w_2 = 0.2, \quad w_3 = 0.2$$

**The first candidate gets:**
$$Score = (0.6 \times 0.98) + (0.2 \times 0.90) + (0.2 \times 0.95)$$
$$Score = 0.958$$

This helps rank candidate information.

**However, there are three important improvements I would make before implementing this in production:**
1. **Recency should not automatically make newer information more important.** A current system policy may be more important than a recent conversation.
2. **Information density needs a measurable definition.** It should not simply reward shorter text.
3. **Relevance scoring must be combined with mandatory constraints** such as security, permissions and factual provenance.

For example, a highly relevant customer record must still be excluded if the current user is not authorized to access it.

### What about Surprise-Based Pruning?

The article mentions removing predictable, low-information tokens. This relates to information theory, where surprising or unexpected information can carry more information than predictable content.

However, it is not a standard universal production pruning algorithm.

I would not implement token-level surprise pruning as a first step. It could remove seemingly predictable but essential details, such as a negation, transaction status or security restriction.

Start with document-level relevance, redundancy removal and token budgeting instead.

---

## 4. Context Caching – Improving performance and reducing costs

This is another important concept the article introduces.

Imagine every user request sends the same 1,000 tokens of system instructions to the LLM. For 10,000 requests, that creates substantial repeated processing. Context caching can help.

### Without caching
- `Request 1` → Process system instructions
- `Request 2` → Process system instructions again
- `Request 3` → Process system instructions again

### With provider-supported prompt caching
*(Reusable prefix cached: System instructions and stable context)*
- `Request 1` → Reuse cached prefix + new question
- `Request 2` → Reuse cached prefix + new question
- `Request 3` → Reuse cached prefix + new question

### There are two different caching concepts worth distinguishing:

| Cache type | Purpose |
| :--- | :--- |
| Application-level cache | Stores reusable retrieval results, summaries or configuration |
| LLM prompt/KV cache | Reuses previously processed prompt prefixes where supported |

For example, an LLM serving engine may reuse attention key/value states from a previously processed prefix. This can reduce repeated prefill computation and improve latency.

> **Important correction to the article:** The claim that caching can reduce latency by up to 80% is not a universal guarantee. Actual improvements depend on model, provider, cache hit rate, prompt length and workload. Also, Ollama and other inference servers have their own caching behavior; provider-specific prompt caching features are not automatically available everywhere.

---

## 5. Technical fact-check: Which claims need qualification?

Here is how I would evaluate the article before using it as an architectural reference:

| Article claim | Assessment |
| :--- | :--- |
| **Lost-in-the-Middle Effect** | **Valid:** Long-context models can miss relevant information depending on its position. The effect varies by model and task. |
| **Hallucination Poisoning** | **Needs clarification:** Unverified information can contaminate context, but retrieval and validation do not guarantee truth. |
| **Hybrid Search** | **Valid:** Combining keyword and semantic retrieval is useful. |
| **Semantic Chunking** | **Valid:** Useful technique, but should be evaluated against other chunking methods. |
| **80% summarization trigger** | **Heuristic:** Not a universal industry standard. |
| **Surprise-Based Pruning** | **Experimental concept:** Not a standard requirement for context engines. |
| **Context caching reduces latency by 80%** | **Not guaranteed:** Depends on implementation and workload. |
| **4,000 tokens always outperform 100,000** | **Overstated:** Quality depends on task, evidence coverage and model capabilities. |

I particularly want you to remember the last point. A 4,000-token context containing incomplete evidence cannot reliably outperform a 100,000-token context containing all the necessary evidence.

> **The goal is not simply to minimize tokens.**  
> **The goal is to maximize useful information within the available budget.**

---

## 6. How I would implement this in your Enterprise RAG Platform

You already have a foundation with FastAPI, Ollama, Qdrant, LangChain and Docker.

I would extend that architecture as follows:

```
┌────────────────────────────────────────────────────────┐
│               Enterprise Context Engine                │
├────────────────────────────────────────────────────────┤
│  Angular 19                                            │
│  Chat interface                                        │
├────────────────────────────────────────────────────────┤
│  FastAPI Agent Harness                                 │
│  Request orchestration and authorization               │
├────────────────────────────────────────────────────────┤
│  Context Engine                                        │
│  1. Retrieval Service: Qdrant + keyword search + rerank │
│  2. Memory Service: PostgreSQL + Qdrant                │
│  3. Pruning Service: Deduplication + summary + compress│
│  4. Context Controller: Budget + validation + sources  │
├────────────────────────────────────────────────────────┤
│  Ollama + Phi-3                                        │
│  LLM inference                                         │
├────────────────────────────────────────────────────────┤
│  Tool Execution                                        │
│  Python functions · PostgreSQL · Internal APIs         │
└────────────────────────────────────────────────────────┘
```
*Tool results update the context for the next model call.*

### Suggested project modules

| Module | Responsibility |
| :--- | :--- |
| `retrieval_service.py` | Hybrid search and reranking |
| `memory_service.py` | Short-term and long-term memory |
| `conversation_service.py` | History and conversation summaries |
| `context_pruner.py` | Deduplication and compression |
| `token_budget.py` | Token counting and allocation |
| `context_builder.py` | Assemble final LLM messages |
| `context_validator.py` | Validate provenance, permissions and input structure |
| `agent_executor.py` | Tool execution and agent loop |

### Suggested implementation order
1. Build a token budget manager.
2. Add conversation history summarization.
3. Implement Qdrant retrieval with metadata filters.
4. Add hybrid search and reranking.
5. Implement short-term and long-term memory.
6. Add context pruning and compression.
7. Add context caching.
8. Add observability and evaluation.

> **Don't start by implementing all four layers simultaneously.** Build and measure each component independently.

---

## 7. Practical exercise: Think like a Context Engineer

Imagine your local LLM supports an **8,192-token** context window.

**User asks:**
> *"Explain why my international payment failed."*

Your harness has collected the following information. Select the information you would send to the LLM:

*For this exercise, reserve 1,500 tokens for the model response. Input budget = 6,692 tokens.*

- [x] **System instructions** — Essential priority (800 tokens)
- [x] **Current question** — Essential priority (200 tokens)
- [x] **Last 5 conversation messages** — High priority (1,400 tokens)
- [ ] **Old unrelated conversations** — Low priority (2,500 tokens)
- [x] **International payment policy documents** — High priority (2,200 tokens)
- [ ] **Domestic ATM policy documents** — Low priority (1,800 tokens)
- [x] **Customer transaction details** — High priority (700 tokens)
- [x] **Available tool definitions** — Medium priority (900 tokens)

**Selected token count:** `6,200 tokens`  
**Remaining input budget:** `492 tokens`  

> **Evaluation:** Budget satisfied! Good selection. You retained the essential instructions, question, relevant policy and transaction details. Consider whether the history and tool definitions are actually needed for this particular request.
> 
> *Note: This exercise uses simplified fixed token estimates. A real context manager must also account for tool schemas, message formatting and actual model tokenization.*

---

## 8. Final takeaway

There is a progression worth remembering:

1. **Prompt Engineering** → *Tell the LLM what to do.*
2. **Context Engineering** → *Give the LLM the right information to do it.*
3. **Agent Harness** → *Manage context, tools, memory and execution.*
4. **Production AI Architecture** → *Make the entire system reliable, secure, observable and scalable.*

> **Next Step:** The recommended next deep-dive is **RAG Retrieval Engineering: Chunking, Embeddings, Hybrid Search, Reranking and Context Selection**. This is the natural next step because your context engine needs to retrieve the right evidence before it can decide what deserves space in the LLM's context window.
