# What is LangChain?

LangChain is a framework for building applications using LLMs. It acts as a middle layer between User/Application and the LLM. It simplifies development of advanced LLM-based applications.    
LangChain is used to build scalable, flexible, and advanced LLM applications with easy model switching and feature integration.

## LangChain Architecture
Modern LangChain is built around Runnables (LCEL), and Chains and Agents are two major application patterns built on top of them.

```
                    LangChain
                        │
        ┌───────────────┴───────────────┐
        │                               │
     Chains                         Agents
        │                               │
   Fixed Workflow               Dynamic Workflow
        │                               │
        └───────────────┬───────────────┘
                        │
                  Runnables (LCEL)
```

1. Chains

A Chain is a predefined sequence of steps.

The execution path is fixed.

Example:
```
User Question
      │
      ▼
PromptTemplate
      │
      ▼
 Gemini
      │
      ▼
Output Parser
      │
      ▼
 Final Answer
```
Example code:
```
const chain = PromptTemplate
    .fromTemplate("Explain {topic}")
    .pipe(model)
    .pipe(new StringOutputParser());

const answer = await chain.invoke({
    topic: "LangChain"
});
```
The model always follows the same pipeline.

2. Agents

An Agent can reason, decide, and choose which tools to use.

Instead of following a fixed path, it decides the next action based on the user's request.

Example:
```
User:
What's the weather in London?
        │
        ▼
      Agent
        │
        ▼
Should I answer directly?
        │
       No
        │
        ▼
Call Weather Tool
        │
        ▼
Receive Result
        │
        ▼
Generate Final Answer
```
Another example:
```
User asks:

"Search the web, summarise the article and email it."

Agent decides:

Search Tool
      │
      ▼
Summariser
      │
      ▼
Email Tool
      │
      ▼
Done
```
The workflow is dynamic, not hard-coded.

**Chains vs Agents**

| Feature         | Chain                           | Agent                            |
| --------------- | ------------------------------- | -------------------------------- |
| Workflow        | Fixed                           | Dynamic                          |
| Tool usage      | Optional                        | Core feature                     |
| Decision making | No                              | Yes                              |
| Reasoning       | No                              | Yes                              |
| Predictable     | Yes                             | Less predictable                 |
| Speed           | Faster                          | Usually slower                   |
| Best for        | RAG, summarisation, translation | Assistants, copilots, automation |

## Real-World Examples

**Chain**
```
PDF
 │
 ▼
Text Splitter
 │
 ▼
Embedding Model
 │
 ▼
Vector Database
 │
 ▼
Retriever
 │
 ▼
LLM
 │
 ▼
Answer
```
Everything is predetermined.

**Agent**
```
User:
"Analyse this sales CSV and create a PowerPoint."

          Agent
             │
     ┌───────┼────────┐
     ▼       ▼        ▼
 Read CSV  Python   PowerPoint Tool
     │       │        │
     └───────┴────────┘
             ▼
      Final Response
```
The agent decides which tools to invoke and in what order.

## Modern LangChain Layers
```
                 LangChain
                      │
        ┌─────────────┴─────────────┐
        │                           │
     Runnables (LCEL)           LangGraph
        │                           │
   PromptTemplate              Agent Workflows
   RunnableSequence            Multi-Agent Systems
   RunnableParallel            Memory
   RunnableLambda              State Management
```

- LCEL (LangChain Expression Language) is used to compose chains with runnables such as pipe(), RunnableSequence, and RunnableParallel.
- LangGraph is the recommended framework for building advanced, stateful agent workflows.


## 🔥 Real Enterprise Example (Bank Use Case)

In Kolkata branch (since you’re in India 🇮🇳):

Bank employee asks:

> “What is the interest rate for senior citizen fixed deposit?”

Flow:
```
User → LangChain → Agent → Search PDF DB → LLM → Response → Store memory
```

Result:    
⚡ Faster search    
💰 Reduced manual effort    
📄 Works across 1000+ documents    

## Basic LLM Setup (Without LangChain)

<img src="imgs/Langchain.png" width="600px">

```
User → Prompt → LLM (Ollama / OpenAI / Google AI) → Response
```

    -   Direct communication with LLM
    -   Works fine for simple prompt-response systems
    -   Not scalable for advanced features

## Setup With LangChain
```
User → LangChain → LLM → LangChain → User
```
LangChain sits in the middle

It can:
    -   Modify prompt
    -   Process output
    -   Add additional logic
    -   Connect external tools

## LangChain, LangGraph, LangFlow, and LangSmith
| Tool      | Main Role       | Used For                   |
| --------- | --------------- | -------------------------- |
| LangChain | Framework       | Build LLM apps             |
| LangGraph | Workflow Engine | Complex agents & loops     |
| LangFlow  | Visual Builder  | Drag-and-drop pipelines    |
| LangSmith | Debug & Monitor | Observability & evaluation |

1️⃣ LangChain
-----------------------------------------------
🔹 What it is : A framework for building applications powered by LLMs.

🔹 Purpose     
Helps you connect:    
- LLMs (OpenAI, Ollama, etc.)
- Vector databases (Qdrant, Pinecone, etc.)
- Tools
- APIs
- Memory
- Agents

🔹 When to Use    
- Building RAG apps
- Creating AI chatbots
- Connecting LLMs to databases
- Tool-using agents

🔹 Example Flow    
User → Prompt → LLM → Vector DB → Response

🔹 Think of it as: 🧱 The core building blocks for LLM apps.

2️⃣ LangGraph
-----------------------------------------------
🔹 What it is : A graph-based orchestration layer built on top of LangChain.

🔹 Purpose
- Helps create:
- Multi-step workflows
- Stateful agents
- Decision-based routing
- Cyclic flows (loops)

🔹 Why Needed?
- Normal LangChain chains are mostly linear:
- Input → Step1 → Step2 → Output

LangGraph allows:
```
Input
  ↓
Decision Node
 ↙       ↘
Tool A   Tool B
  ↓        ↓
   ← Loop Back →
```

🔹 Best For
- Complex AI agents
- Multi-agent systems
- Stateful conversations
- Human-in-the-loop systems

🔹 Think of it as: 🧠 Advanced workflow engine for AI reasoning.

3️⃣ LangFlow
-----------------------------------------------
🔹 What it is : A visual drag-and-drop UI tool for building LangChain apps.

🔹 Purpose    
Lets you build:    
- Chains
- RAG pipelines
- Agents
- Without writing much code.

🔹 Who Uses It?    
- Beginners
- Rapid prototyping teams
- Non-developers

🔹 Think of it as: 🎨 Visual designer for LangChain pipelines.

4️⃣ LangSmith
-----------------------------------------------
🔹 What it is : An observability, monitoring, and debugging platform.

🔹 Purpose    
Tracks:    
- Prompts
- Responses
- Token usage
- Latency
- Errors
- Agent reasoning steps

🔹 Why Important?    
LLM apps are hard to debug.    
LangSmith shows:    
- Why the model gave that answer
- Which step failed
- How much tokens were used

🔹 Think of it as: 🔍 Debugger + monitoring dashboard for LLM apps.

**🎯Suppose you're building a Bank RAG System (like you discussed earlier):**    
1. LangChain → Connect LLM + Qdrant + embeddings
2. LangGraph → Handle approval workflow & decision routing
3. LangFlow → Prototype quickly before coding
4. LangSmith → Monitor production errors & token usage

## 🧠 Easy Memory Trick
🧱 LangChain = Build    
🔄 LangGraph = Orchestrate    
🎨 LangFlow = Visualize    
🔍 LangSmith = Debug    

## ⭐ Why We Use LangChain (Main Reasons)
**✅ 1. Easy Model Switching (Very Important)**

LangChain makes it easy to switch models with minimal code change.

Example:
    -   From OpenAI GPT → Local Ollama (LLaMA 3.1)
    -   From OpenAI → Google Generative AI
    -   From Cloud model → Local model

👉 Usually requires just one line change    
👉 No need to rewrite full application  

This makes applications flexible and scalable.

**✅ 2. Easy Integration of Advanced Features**

LangChain simplifies adding:

🔹 Chat Memory
    -   Maintains conversation history
    -   Enables chatbot behavior

🔹 Knowledge Integration (RAG)
    -   Retrieval-Augmented Generation
    -   Connects LLM to:
        -   PDFs
        -   Databases
        -   Company documents
        -   Vector databases

🔹 Agents
    -   LLM can call tools
    -   Tools return results
    -   LLM decides next action

Example:
    -   Call weather API
    -   Query database
    -   Run calculator
    -   Execute search

🔹 API Creation
    -   Easy integration with FastAPI / backend systems


**🎯 Two Advanced Features Covered**

The instructor focuses on:
1. RAG (Retrieval-Augmented Generation)
    -   Adds external knowledge
    -   Solves LLM knowledge limitation
2. Agents
    -   LLM uses tools
    -   Tool output influences final response

These are the most common real-world LLM applications.

**🛠 Install required packages:**
```
pip install langchain
pip install langchain-core
pip install langchain-ollama
pip install langchain-community
```

After installing, you can start building:
    -   Simple prompt apps
    -   RAG systems
    -   Agent-based systems

### Knowledge Integration (RAG)

Now we want to do knowledge integration where we will give text files, PDF files or CSV files, or we may want to put all the relevant files in a folder. And then based on our input, we want to send a query and fetch only relevant documents or relevant part of the documents from this knowledge and give it back as part of prompt to the LLM. So instead of sending the whole PDF file or the entire text
or the entire data, we want to identify only relevant parts from this knowledge and send only that relevant part to the LLM so that it can answer the user query.

<img src="imgs/Knowledge_integration.png" width="600px">

**Why are we not sending the entire PDF file?**

There are two reasons for that.

    -   One is most models have a context window. That is you can only send certain amount of tokens in one prompt. So if you have a big PDF file, that will not be allowed in the prompt. You will not be able to send the entire PDF file.
    -   Second reason is that if you send a lot of information in the prompt, it becomes difficult for the LLM model to pick out relevant parts from it. It might give importance to non-important parts of the document, and you may not get the desired response from LLM. 

For this reason, in a rag system, we first fetch the relevant parts from our knowledge source and send that relevant part only to the LLM.

## 🚀 Why Do We Need LangSmith When We Already Have LangChain?

https://docs.langchain.com/langsmith/home

🔹 First Understand the Difference
    -   LangChain → Framework to build LLM applications
    -   LangSmith → Platform to debug, monitor, and evaluate LLM applications

👉 Simple analogy:
    -   LangChain = Builder
    -   LangSmith = Inspector + Monitor + Evaluator

1️⃣ Debugging Complex Chains
-----------------------------------------------------------
When you build:
```
User → PromptTemplate → LLM → Retriever → Tool → Final Output
```

If output is wrong:
    -   Is prompt wrong?
    -   Retriever failed?
    -   LLM hallucinated?
    -   Tool returned bad data?

👉 LangChain alone does NOT give deep tracing.

✅ LangSmith provides:
    -   Step-by-step execution trace
    -   Input/output at every node
    -   Token usage
    -   Latency tracking

2️⃣ Observability (Production Monitoring)
-----------------------------------------------------------
In production (e.g., your FastAPI API):

You need:
    -   How many users?
    -   Token consumption?
    -   Response time?
    -   Failure rate?
    -   Which prompts are underperforming?

LangChain ❌ does not provide monitoring dashboard  
LangSmith ✅ provides production observability dashboard    

3️⃣ Evaluation & Testing (Very Important for RAG)
-----------------------------------------------------------
You’re working with RAG concepts. Now imagine:

You changed:
    -   Chunk size
    -   Embedding model
    -   Retriever strategy
    -   Prompt template

How do you know which version is better?

LangSmith allows:
    -   Dataset-based evaluation
    -   Run experiments
    -   Compare chain versions
    -   Score outputs (accuracy, relevance, faithfulness)

Without LangSmith → Manual testing  
With LangSmith → Scientific evaluation  

4️⃣ Prompt Versioning
-----------------------------------------------------------
In real projects:
    -   Prompt v1
    -   Prompt v2
    -   Prompt with system message
    -   Few-shot prompt

LangSmith helps:
    -   Track prompt versions
    -   Compare outputs
    -   Rollback bad versions
    -   LangChain alone cannot manage prompt experiments.

5️⃣ Team Collaboration (Enterprise Need)
-----------------------------------------------------------
If 5 developers work on same LLM system:

You need:
    -   Shared logs
    -   Shared traces
    -   Dataset management
    -   Experiment history

LangSmith supports team-level collaboration.

| Feature              | LangChain | LangSmith    |
| -------------------- | --------- | ------------ |
| Build chains         | ✅        | ❌          |
| Prompt templates     | ✅        | ❌          |
| RAG pipelines        | ✅        | ❌          |
| Execution tracing    | Limited   | ✅ Advanced  |
| Monitoring dashboard | ❌        | ✅          |
| Evaluation framework | ❌        | ✅          |
| Production analytics | ❌        | ✅          |

#### 🔥 Real-World Example (Your FastAPI Setup)

Your flow:
```
Postman → FastAPI → LangChain → Ollama
```

Without LangSmith:
    -   If response wrong → you print() debug
    -   Hard to track token usage
    -   No experiment comparison

With LangSmith:
    -   Full trace of each request
    -   Token cost per request
    -   Prompt comparison
    -   Performance monitoring

You don’t need it if:
    -   Just learning LangChain
    -   Small personal project
    -   No production deployment
    -   No evaluation requirement

You MUST Use LangSmith
    -   Production LLM app
    -   RAG system
    -   Enterprise AI system
    -   Multi-user API
    -   Cost monitoring needed
    -   A/B prompt testing
