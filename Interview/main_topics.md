# 🚀 AI Engineer / GenAI / RAG interview discussions

## 🎯 Real Skills Checklist (Senior GenAI Engineer)

Companies expect knowledge of:
+ ✔ RAG pipelines
+ ✔ Vector databases
+ ✔ Prompt engineering
+ ✔ Multi-agent orchestration
+ ✔ LLM observability
+ ✔ RAG evaluation
+ ✔ Hallucination mitigation
+ ✔ Production architecture
+ ✔ LLM APIs
+ ✔ Semantic search

## Multi-Agent Systems

**Agents collaborating together using frameworks like:**
- AutoGen
- CrewAI
- LangGraph

**Example agents:**
```
Planner Agent
⬇
Research Agent
⬇
Code Agent
⬇
Reviewer Agent
```

## 1️⃣ Agent Orchestration
Agent orchestration is the coordination of multiple AI agents and tools to complete a complex task.

Instead of one LLM doing everything, multiple specialized agents collaborate.

**Example Workflow**
```
User Request
⬇
Planner Agent → breaks task into steps
⬇
Research Agent → searches information
⬇
Code Agent → writes code
⬇
Reviewer Agent → validates output
```

**Popular Tools**
+ LangChain
+ LangGraph
+ AutoGen
+ CrewAI

**Real Use Cases**
+ AI research assistants
+ Autonomous software development
+ Business workflow automation
+ AI customer support agents

## 2️⃣ AutoGen
AutoGen is a framework developed by Microsoft for creating multi-agent AI systems where agents talk to each other.

Key Concept : Multiple agents communicate in a conversation loop until the task is solved.

**Example:**
```
User → Assistant Agent
⬇
Assistant → Code Agent
⬇
Code Agent → Debug Agent
⬇
Final Response to User
```

**Agents in AutoGen**  

Typical agents include:
- Assistant Agent
- User Proxy Agent
- Code Executor Agent
- Tool Agent

#### Example Use Case

Autonomous coding assistant:

User:
```
Build a REST API
```
Agent Flow:
```
Assistant Agent → writes code
⬇
Executor Agent → runs code
⬇
Debug Agent → fixes errors
⬇
Final working API returned
```

## 3️⃣ Semantic Query
Semantic query means searching based on meaning instead of keywords.

Instead of exact word matching, the system understands context and intent.

**Example**  

Keyword Search
```
query: "car insurance"
```
Semantic Search
```
query: "vehicle coverage policy"
```
Both return same relevant documents.

**Technology Behind It**
- 1️⃣ Text Embeddings
- 2️⃣ Vector Database
- 3️⃣ Similarity Search

**Popular Embedding Models**
- OpenAI Embeddings
- Nomic Embed
- BGE Embeddings
- Vector Databases
- Qdrant
- Pinecone
- Weaviate

**Where It Is Used**
- RAG systems
- ChatGPT document assistants
- Enterprise knowledge search
- AI recommendation systems

## MCP (Model Context Protocol)
MCP is a standard protocol that allows LLMs to interact with external tools, databases, and APIs.

It was introduced by Anthropic to make AI systems connect to real tools safely.

**What MCP Solves**

LLMs normally cannot directly access:
- databases
- APIs
- files
- external systems

MCP acts as a standard bridge.

**MCP Architecture**
```
LLM
⬇
MCP Client
⬇
MCP Server
⬇
External Tools
```

**Example tools:**
- Google Drive
- Slack
- GitHub
- Databases


## LLM APIs
Using API endpoints of large language models inside applications.

**Popular LLM Providers**
- OpenAI
- Anthropic
- Example Models

**OpenAI:**
- GPT-4
- GPT-4o

**Anthropic:**
- Claude

**Example API Call (Python)**
```
from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role":"user","content":"Explain RAG"}]
)

print(response.choices[0].message.content)
```

**Real Use Cases**
- AI chatbots
- Document summarization
- AI coding assistants
- AI customer support

## LangChain
LangChain is a framework for building applications powered by LLMs.

It connects:
```
LLM + Tools + Memory + Data
```

**Core Components**
```
1️⃣ Prompts
2️⃣ Chains
3️⃣ Agents
4️⃣ Tools
5️⃣ Memory
6️⃣ Vector stores
```

**Example RAG Pipeline**
```
User Question
⬇
Embedding Model
⬇
Vector Database
⬇
Retriever
⬇
LLM Answer
```

**Example Code**
```
from langchain.chains import RetrievalQA
```

## Prompt Engineering

Prompt engineering is the **technique of designing prompts to get better outputs from LLMs**.

**Techniques**

**1️⃣ Role prompting**
```
You are an expert AI architect.
Explain RAG architecture.
```

**2️⃣ Few-shot prompting**
```
Example 1
Example 2
Now answer:
```

**3️⃣ Chain-of-thought prompting**
```
Explain step-by-step reasoning
```

**4️⃣ Structured prompting**
```
Return response in JSON format
```

