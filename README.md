# Artificial Intelligent

## Foundational explanation of how Modern AI Systems evolved from Rule-based Systems to Agentic AI
The Reality of AI Nobody Tells You | AI Agents, LLMs & Generative AI : https://www.youtube.com/watch?v=gqRWi9X_TD0

1. Conventional AI (Rule-Based AI) : The system follows predefined rules. It refers to systems designed to analyze specific data, recognize patterns, and make decisions or predictions within predefined parameters.
   Examples are :
    - Spam Filters: AI algorithms in email providers (like Gmail) analyze incoming messages for patterns, flagging potential junk or phishing before it hits the inbox.
    - Predictive Text: Smartphone keyboards and word processors use AI to analyze the words being typed and suggest the next logical word or correct typos.
    - Recommendation Systems: Streaming platforms (like Netflix) and online retailers (like Amazon) use machine learning to analyze past purchases and viewing history, then suggest relevant items.
    - Dynamic Pricing: Ride-sharing apps (like Uber) use conventional AI models to instantly analyze traffic, time of day, and rider demand to calculate fares.
    - Fraud Detection: Banking institutions use AI to instantly analyze transaction histories in real-time, identifying unusual activity that deviates from a customer's standard behavior.
    - Credit Scoring: Loan applications are frequently evaluated by AI models that quickly assess financial risk based on thousands of historical data points.
    - Route Optimization: Mapping apps (like Google Maps) utilize AI algorithms to evaluate travel speed, distance, and real-time traffic data to find the fastest route.
    - Voice Assistants: Digital assistants (like Apple Siri) rely on speech recognition and natural language processing to process audio commands and execute specific tasks.
    - Medical Diagnostics: In healthcare, AI models are trained on thousands of medical images (like X-rays or MRIs) to identify early signs of abnormalities or diseases.
    - Autonomous Driving: Self-driving cars (like Tesla) rely on computer vision and obstacle detection AI to continuously process environmental data and make real-time navigational decisions.

   Fails when new unseen patterns appear.
3. Deep Learning : Instead of manually writing rules, the system learns patterns from data. Examples are Netflix recommendations, Instagram reels feed, YouTube recommendations, Face recognition. The model learns from user behavior, preferences, timing, engagement patterns etc, but cannot generate truly new content independently.
4. Generative AI : This is where modern LLMs come in. Examples are OpenAI's ChatGPT, Google's Gemini, Anthropic's Claude etc. It creates text, code, images, music, summaries, emails, UI code, documentation etc. Limitation of Generative AI is that it can search hotels, flights but can't book for you.
   - LLM works : LLMs are trained on trillions of tokens. A token can be word, subword, punctuation.
       Example: "My name is Ajay"
        Tokens:
          - My
          - name
          - is
          - Ajay
         These tokens become vectors (embeddings).
    - Embeddings & Vector Databases : Text → converted into numbers (vectors).
       Those vectors are stored in:
        - Qdrant
        - Pinecone
        - Weaviate
        - Chroma
       This enables:
        - semantic search
        - similarity matching
        - contextual retrieval
     - RAG (Retrieval-Augmented Generation) : LLMs do not know your company’s private data.
        - External knowledge sources
           - Unstructured Text: Internal wikis, policy manuals, corporate reports, emails, legal contracts, and knowledge bases.
           - Media & Files: PDFs, research papers, slide decks, and whitepapers.
           - Structured Data: SQL or NoSQL databases, product catalogs, employee directories, and CRM platforms.
           - Live Web Data: Real-time search engines, news feeds, and live APIs (e.g., fetching weather or stock prices).
           - Version Control & Code: Code repositories (like GitHub) and technical API documentation.
6. Agentic AI : AI Agent is created by three components LLM (Brain), Memory (Short-Term Memory, Long-Term Memory, External Memory) and Tools.
   Tools : Agents become powerful when connected to tools.
         - APIs
         - databases
         - email systems
         - payment gateways
         - search engines
         - CRMs   
   Agent Workflow : Observe → Plan → Act → Reflect
   Multi-Agent Systems :
      
   | Agent          | Responsibility     |
   | -------------- | ------------------ |
   | Order Agent    | Order handling     |
   | Payment Agent  | Payment processing |
   | Delivery Agent | Rider coordination |
   | Support Agent  | Customer issues    |

   Popular Agentic AI Frameworks
    - For Simple Workflows
      - LangChain
    - For Complex Multi-Agent Systems
     - LangGraph
     - Enterprise Managed Platforms
     - Amazon Web Services Bedrock
     - Microsoft AutoGen
     - Google Vertex AI

So the correct hierarchy is:
```
AI
 └── Machine Learning
      └── Deep Learning
           └── Generative AI
                └── Agentic AI Systems
```
That’s the technically accurate structure.

<img src="imgs/ai_system_layers.gif" width="70%"/>

## 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗶𝘃𝗲 𝗔𝗜 vs 𝗔𝗴𝗲𝗻𝘁𝗶𝗰 𝗔𝗜 vs 𝗟𝗟𝗠𝘀
<img src="imgs/genai_agenticai_llm.gif" width="70%" />
1. 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗶𝘃𝗲 𝗔𝗜
Using AI to create content across text, images, audio, and video.

- 𝗘𝗻𝗰𝗼𝗱𝗶𝗻𝗴-𝗗𝗲𝗰𝗼𝗱𝗶𝗻𝗴 + 𝗟𝗮𝘁𝗲𝗻𝘁 𝗦𝗽𝗮𝗰𝗲: Learn patterns and creativity.
- 𝗧𝗿𝗮𝗻𝘀𝗳𝗼𝗿𝗺𝗲𝗿 𝗦𝘁𝗿𝘂𝗰𝘁𝘂𝗿𝗲: Same foundation as LLMs.
- 𝗦𝘆𝗻𝘁𝗵𝗲𝘁𝗶𝗰 𝗗𝗮𝘁𝗮: Generate new training data.
- 𝗗𝗶𝗳𝗳𝘂𝘀𝗶𝗼𝗻 + 𝗚𝗔𝗡𝘀: Power image and video generation.
- 𝗭𝗲𝗿𝗼 / 𝗙𝗲𝘄-𝘀𝗵𝗼𝘁 + 𝗥𝗟𝗛𝗙: Improve output quality.
- 𝗙𝗶𝗻𝗲-𝘁𝘂𝗻𝗶𝗻𝗴 + 𝗦𝘁𝘆𝗹𝗲 𝗧𝗿𝗮𝗻𝘀𝗳𝗲𝗿: Customize for brands and styles.
- 𝗠𝘂𝗹𝘁𝗶𝗺𝗼𝗱𝗮𝗹 𝗔𝗜: Works with text, image, audio, video.
- 𝗧𝗲𝘅𝘁-𝘁𝗼-𝗜𝗺𝗮𝗴𝗲 / 𝗩𝗶𝗱𝗲𝗼: Create media from prompts.
- 𝗣𝗿𝗼𝗺𝗽𝘁 𝗘𝗻𝗴𝗶𝗻𝗲𝗲𝗿𝗶𝗻𝗴: Better prompts = better content.

Generative AI mainly 𝗰𝗿𝗲𝗮𝘁𝗲𝘀 𝗰𝗼𝗻𝘁𝗲𝗻𝘁 𝘄𝗵𝗲𝗻 𝗮𝘀𝗸𝗲𝗱.  
Generative AI is the **creative application layer built on top of those models (text, images, code, video)**.

2. 𝗔𝗴𝗲𝗻𝘁𝗶𝗰 𝗔𝗜
AI systems that plan, decide, and execute tasks independently.

- 𝗜𝗻𝗱𝗲𝗽𝗲𝗻𝗱𝗲𝗻𝘁 𝗚𝗼𝗮𝗹𝘀 + 𝗔𝗱𝗮𝗽𝘁𝗶𝘃𝗲 𝗣𝗹𝗮𝗻𝗻𝗶𝗻𝗴: Break big goals into tasks.
- 𝗛𝗶𝗲𝗿𝗮𝗿𝗰𝗵𝗶𝗰𝗮𝗹 𝗔𝗴𝗲𝗻𝘁𝘀: Multiple decision-making layers.
- 𝗧𝗼𝗼𝗹 𝗨𝘀𝗲 + 𝗧𝗮𝘀𝗸 𝗘𝘅𝗲𝗰𝘂𝘁𝗶𝗼𝗻: Can browse, code, email, automate.
- 𝗟𝗼𝗻𝗴-𝘁𝗲𝗿𝗺 𝗠𝗲𝗺𝗼𝗿𝘆: Remembers past work and context.
- 𝗦𝗲𝗹𝗳-𝗥𝗲𝘃𝗶𝗲𝘄 + 𝗣𝗲𝗿𝗳𝗼𝗿𝗺𝗮𝗻𝗰𝗲 𝗠𝗲𝘁𝗿𝗶𝗰𝘀: Improves automatically.
- 𝗖𝗼𝗧 𝗥𝗲𝗮𝘀𝗼𝗻𝗶𝗻𝗴: Thinks step-by-step before acting.
- 𝗠𝘂𝗹𝘁𝗶-𝗔𝗴𝗲𝗻𝘁 𝗖𝗼𝗹𝗹𝗮𝗯: AI agents work as a team.
- 𝗠𝗼𝗻𝗶𝘁𝗼𝗿𝗶𝗻𝗴 + 𝗢𝗿𝗰𝗵𝗲𝘀𝘁𝗿𝗮𝘁𝗶𝗼𝗻: Tracks progress and manages workflows.
- 𝗛𝘂𝗺𝗮𝗻-𝗶𝗻-𝘁𝗵𝗲-𝗟𝗼𝗼𝗽: Humans supervise key decisions.
- 𝗖𝗼𝗴𝗻𝗶𝘁𝗶𝘃𝗲 𝗖𝘆𝗰𝗹𝗲: Plan → Act → Observe → Improve.

Agentic AI mainly 𝗽𝗹𝗮𝗻𝘀 𝗮𝗻𝗱 𝗰𝗼𝗺𝗽𝗹𝗲𝘁𝗲𝘀 𝘄𝗼𝗿𝗸 𝗮𝘂𝘁𝗼𝗻𝗼𝗺𝗼𝘂𝘀𝗹𝘆.  
Agentic AI is the **execution architecture that wraps models with memory, tools, planning, and control loops**.

3. 𝗟𝗟𝗠𝘀
The core models that understand language and generate responses.

- 𝗣𝗿𝗲-𝘁𝗿𝗮𝗶𝗻𝗶𝗻𝗴 & 𝗙𝗶𝗻𝗲-𝘁𝘂𝗻𝗶𝗻𝗴: Learn from massive datasets and get refined.
- 𝗧𝗼𝗸𝗲𝗻𝗶𝘇𝗮𝘁𝗶𝗼𝗻 + 𝗔𝘁𝘁𝗲𝗻𝘁𝗶𝗼𝗻: Break text into tokens and focus on important words.
- 𝗧𝗿𝗮𝗻𝘀𝗳𝗼𝗿𝗺𝗲𝗿𝘀 + 𝗩𝗲𝗰𝘁𝗼𝗿𝘀: Convert language into numbers and patterns.
- 𝗣𝗼𝘀𝗶𝘁𝗶𝗼𝗻 𝗘𝗻𝗰𝗼𝗱𝗶𝗻𝗴: Understand word order and context.
- 𝗭𝗲𝗿𝗼 / 𝗙𝗲𝘄-𝘀𝗵𝗼𝘁: Perform new tasks with little training.
- 𝗥𝗔𝗚 + 𝗥𝗟𝗛𝗙: Use external knowledge and human feedback.
- 𝗛𝗮𝗹𝗹𝘂𝗰𝗶𝗻𝗮𝘁𝗶𝗼𝗻 𝗥𝗲𝗱𝘂𝗰𝘁𝗶𝗼𝗻: Improve reliability and accuracy.
- 𝗠𝗼𝗱𝗲𝗹 𝗢𝗽𝘁𝗶𝗺𝗶𝘇𝗮𝘁𝗶𝗼𝗻: Size reduction, evaluation, and context limits.
- 𝗣𝗿𝗼𝗺𝗽𝘁 𝗘𝗻𝗴𝗶𝗻𝗲𝗲𝗿𝗶𝗻𝗴: Communicating effectively with models.

LLMs mainly 𝘂𝗻𝗱𝗲𝗿𝘀𝘁𝗮𝗻𝗱 𝗮𝗻𝗱 𝗴𝗲𝗻𝗲𝗿𝗮𝘁𝗲 𝘁𝗲𝘅𝘁 𝘄𝗵𝗲𝗻 𝗽𝗿𝗼𝗺𝗽𝘁𝗲𝗱.  
LLMs **(like those from OpenAI or Anthropic) are the reasoning engine**. Generative AI is the creative application layer built on top of those models (text, images, code, video).

✅ 𝗜𝗻 𝘀𝗵𝗼𝗿𝘁:
- 𝗟𝗟𝗠𝘀 → The brain that understands & writes
- 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗶𝘃𝗲 𝗔𝗜 → Creates content
- 𝗔𝗴𝗲𝗻𝘁𝗶𝗰 𝗔𝗜 → Plans & executes work

## Optimization & improving AI Model's performance using the following methods
1. Fine-tuning
2. Prompt Engineering
3. Retrieval augmented generation (RAG)

## 📌 Features
- Document Upload (PDF, CSV, DOCX)
- Vector Embeddings (nomic-embed-text)
- Qdrant Vector DB
- Ollama LLM
- Dockerized Setup
- Swagger API

## Two Types of AI
**🔹 1️⃣ Query-Based AI (Direct Prompt AI)**

Example: OpenAI's ChatGPT
  -  Pre-trained on internet data
  -  No access to your private documents
  -  Answers based on training knowledge
  -  Cannot read your bank’s internal PDFs

👉 This is General AI

**🔹 2️⃣ Knowledge-Based AI (Document Storage AI)**  
  -  Stores company documents (PDFs, policies, manuals)
  -  Converts documents into vector embeddings
  -  Stores them in a Vector Database
  -  Retrieves relevant content when queried

👉 This is Enterprise AI

## Combination = SMART AI (RAG)

When we combine:
```
✔ Pre-trained LLM (like ChatGPT)
✔ Vector Database (company documents)
```

We get:
```
🔥 AI that answers using your company’s real data.
```
This is called Retrieval Augmented Generation (RAG).

## Prompts : https://prompts.chat/prompts

```
Data → ML → DL → Transformers → LLMs
                     ↓
            GenAI + RAG + Agents
                     ↓
              Real Applications
```

## 🏦 Real-Time Banking Use Case (Enterprise Knowledge Assistant)

**Scenario:**

A bank employee needs to search:
  -  Loan policy PDF
  -  Insurance document
  -  Compliance rules
  -  RBI circulars
  -  1000+ documents

Instead of manually searching, They ask:
```
"What is the eligibility criteria for home loan for salaried employees?"
```

**🔍 What Happens Internally:**  
1. Query converted into vector
2. Vector DB finds similar documents
3. Relevant chunks retrieved
4. Sent to LLM
5. LLM generates accurate answer using retrieved data

**🎯 Result:**  
✔ Faster document search  
✔ Reduced working cost  
✔ Accurate answers  
✔ Better customer experience  

**Angular + Spring Boot + Vector DB + LLM Flow**  
Now let’s explain your architecture clearly 👇  
```
┌──────────────────────────────────────────────┐
│                👨‍💼 Bank Employee              │
└──────────────────────────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────┐
│ 🟦 Angular Frontend (Chat UI)               │
│ - Question Input                            │
│ - Chat History                              │
│ - Document Upload                           │
└──────────────────────────────────────────────┘
                         │ REST API
                         ▼
┌──────────────────────────────────────────────┐
│ 🟩 Spring Boot Backend                      │
│----------------------------------------------│
│ 1️⃣ Authentication (JWT/OAuth2)             │
│ 2️⃣ Query Validation                         │
│ 3️⃣ Embedding Generation                     │
│ 4️⃣ Vector Search                            │
│ 5️⃣ LLM Prompt Construction                  │
│ 6️⃣ Response Formatting                      │
└──────────────────────────────────────────────┘
            │                         │
            │                         │
            ▼                         ▼
┌───────────────────────┐     ┌───────────────────────┐
│ 🟣 Vector Database     │     │ 🟠 LLM Server          │
│ (Semantic Search)      │     │ (Answer Generator)     │
│                        │     │                        │
│ - Document Embeddings  │     │ - GPT / Llama / etc   │
│ - Metadata Filtering   │     │ - Context Aware       │
└───────────────────────┘     └───────────────────────┘
            │                         │
            └───────────┬─────────────┘
                        ▼
              ┌────────────────────┐
              │ Final AI Response  │
              └────────────────────┘
                        │
                        ▼
                 Back to Angular UI
```

**1️⃣ Angular Frontend (UI)**  
  -  User types question
  -  Sends REST API call to Spring Boot

**2️⃣ Spring Boot Backend (API layer)**  
Before employees ask questions:
  -  Upload 1000+ PDFs
  -  Split into chunks
  -  Convert chunks into embeddings
  -  Store in vector database like Qdrant, Pinecone, Weaviate

Each chunk stored like:
```
{
  text: "Home loan eligibility criteria...",
  embedding: [0.234, 0.875, ...],
  metadata: {
      department: "loan",
      version: "2025",
      confidential: false
  }
}
```

After employees ask questions:
  -  Convert User query → embedding
  -  Search vector database
  -  Retrieve top similar documents or top 5 chunks
  -  Construct prompt:
    ```
    Answer based on below documents:
    
    [chunk1]
    [chunk2]
    [chunk3]
    
    Question: What is home loan eligibility?
    ```  
  -  Send to LLM (OpenAI models or Ollama for local deployment)
  -  Return structured answer

**3️⃣ Vector Database (Document intelligence)**    
Examples:
  -  Qdrant
  -  Pinecone
  -  Weaviate

It returns:
```
Top 3 matching document chunks
```

**4️⃣ LLM (Answer generation)**  
Examples:
  -  OpenAI models
  -  Ollama (for local models)
LLM generates:
✔ Final human-readable answer  
✔ Based only on retrieved documents

**5️⃣ Response Flow Back**
```
LLM → Spring Boot → Angular → UI rendered to employee
```

**6️⃣ Why This is Powerful for Enterprises**  
| Traditional Search | RAG AI             |
| ------------------ | ------------------ |
| Keyword matching   | Semantic search    |
| Manual reading     | Auto summarization |
| Slow               | Instant            |
| High cost          | Reduced cost       |

**7️⃣ Angular Enterprise Use Case**  
🔵 Frontend (Angular)
  -  Chat UI
  -  File upload UI
  -  Search interface
  -  Document preview

🟢 Backend (Spring Boot)
  -  REST APIs
  -  Embedding generation
  -  Vector search
  -  LLM communication
  -  Security (JWT, OAuth)
  -  Role-based access (Admin, Loan Officer, Manager)
    -  Example:
       -  Loan officer can access only:
           -  Loan documents
           -  Not insurance documents
  -  Rate limiting
  -  Audit logging

**This is exactly how:**  
  -  Banking AI assistants
  -  Insurance AI systems
  -  Legal document AI
  -  HR policy bots

are built in real-world enterprise systems.

## 🧠 What is Ollama?
Ollama is a tool that lets you run Large Language Models (LLMs) locally on your own machine.  

> Think of it as: “Docker for AI models”

> Instead of calling OpenAI / Gemini / Claude over the internet, Ollama runs models offline, locally, and securely.

> Ollama is designed to run large language models locally on your machine. That’s why we install it in the system — it provides the runtime environment, model management, and API endpoints that your code can connect to.

## Tools running local LLMs
**Ollama (CLI)**, **LM Studio (GUI)**, and **Hugging Face (model repository)** are top tools for running local LLMs, with LM Studio being most beginner-friendly and Ollama best for developers and automation. LM Studio offers a visual interface to explore Hugging Face models, while Ollama provides fast inference, API integration, and lightweight management. 

🧠 1. LM Studio – Local AI with a Friendly Desktop UI
-----------------------------------------------------------------------------------
**What it is**: A desktop application that lets you run large language models locally with a graphical interface — think of it like “ChatGPT locally” with easy model discovery and controls.

**Key traits**
  -  🖥️ GUI-first — very visual, easy for beginners to pick up and experiment without coding.
  -  📚 Hugging Face model access built in — you can browse and download GGUF/MLX models directly inside the app.
  -  🛠️ Local API support — it can expose a local server compatible with OpenAI-style APIs.
  -  📊 Controls and visualization — model stats, quantization choices, memory usage sliders.

**Who it’s good for**
  -  Beginners, creators, researchers who want a desktop app for local chatting and experimenting.
  -  People who want Hugging Face model breadth without manually handling downloads.
  -  Trade-offs
  -  Slightly heavier on memory/CPU compared to minimal CLI tools.
  -  Only supports Hugging Face GGUF/MLX formats — custom models outside that need conversion.

🛠️ 2. Ollama – Minimal Local Server & CLI for Devs
-----------------------------------------------------------------------------------
**What it is**: A command-line local model runner that works as a lightweight language model server (daemon/API).

**Key traits**
  -  🐧 CLI-driven — install with a single binary and pull models via terminal.
  -  🚀 Lightweight, efficient runtime — optimized for speed and low resource overhead in many setups.
  -  📦 Curated model registry — you can pull optimized, ready-to-run models (e.g., Llama, Mistral).
  -  🔒 Local only by default — no cloud dependencies and good for privacy-first use cases.
  -  🧩 REST/ API support — run it as a local endpoint that other software (LangChain, scripts) can call.

**Who it’s good for**
  -  Developers and engineers who want scriptable, automatable local inference.
  -  Projects that need a local API server to embed in apps or workflows.

**Trade-offs**
  -  Command-line only — steeper learning curve for non-technical users.
  -  Smaller built-in model catalogue than Hugging Face, though you can point to GGUF models from HF too with the right commands.

🌐 3. Hugging Face – Broad Model Ecosystem + Cloud/Local Frameworks
-----------------------------------------------------------------------------------
**What it is**: A platform and ecosystem (model/dataset hub, libraries, cloud inference) — not just a local runner.

**Key traits**
  -  📦 Huge model repository — tens of thousands of open models across NLP, vision, audio, multimodal tasks.
  -  🧰 Frameworks & libraries — Transformers, Datasets, Evaluate for training, fine-tuning, evaluation.
  -  ☁️ Cloud + hosted inference — can serve models at scale (paid services) or experiment with them locally.
  -  🤝 Integration with tools like LM Studio & Ollama — Hugging Face models often serve as the backend for local runners.

**Who it’s good for**
  -  Researchers and ML engineers who need fine-tuning, training, evaluation, and deployment capabilities.
  -  Projects that go beyond just running a model — e.g., building apps, RAG systems, multi-modal workflows.

**Trade-offs**
  -  Not a standalone local runner by itself — you use libraries or services.
  -  Cloud services have pricing layers; local usage requires setup (Python, frameworks).

| Feature / Use Case        | **LM Studio**     | **Ollama**     | **Hugging Face** |
| ------------------------- | ----------------- | -------------- | ---------------- |
| Local GUI app             | ✅                 | ❌              | ❌ (via tools)    |
| Command-line / scriptable | ❌ (mostly)        | ✅              | ⚙️ (via HF CLI)  |
| Local LLM serving         | ✅ (desktop + API) | ✅ (daemon/API) | ✅ (with infra)   |
| Model diversity           | ⭐⭐⭐⭐              | ⭐⭐⭐            | ⭐⭐⭐⭐⭐            |
| Starter-friendly          | ⭐⭐⭐⭐              | ⭐⭐             | ⭐⭐               |
| Production / scaling      | ⭐⭐                | ⭐⭐⭐            | ⭐⭐⭐⭐⭐            |
| Fine-tuning / training    | ❌                 | ❌              | ⭐⭐⭐⭐             |

**🧠 Which Should You Pick?**
-----------------------------------------------------------------------------------
🟦 Beginners & Desktop Users:
→ LM Studio — easiest way to explore local AI with minimal setup.

🟩 Developers & API Workflows:
→ Ollama — minimal, fast, scriptable local server.

🟨 Research & Full ML Lifecycle:
→ Hugging Face — unparalleled model choices + training/inference frameworks.


## Transformers
The Transformer is the backbone of an LLM, enabling it to understand long-range context, learn deep semantic relationships using self-attention, and scale efficiently to massive datasets.
Think of the Transformer as the engine, and the LLM as a very large, very well-trained version of that engine 🚀

## Pre-trained LLM vs RAG

**Pre-trained LLM**  =====================================================  
“A pre-trained LLM is a closed-knowledge system. It can only answer based on what it learned during training, which makes it unsuitable for dynamic or enterprise-specific data without augmentation like RAG.”

  -  It creates responses based on user input or a query
  -  The LLM was trained once on a fixed dataset (internet text, books, code, etc.)
  -  It predicts the next token based on patterns learned during training. Training happened in the past.
  -  After training:
      -  ❌ It cannot learn new facts
      -  ❌ It cannot see your private data
      -  ❌ It cannot query databases or APIs
  -  Key problems one its knowledge is limited to what it was trained on and is not up to date
  -  It doesn't provide reliable sources. It does not think, search, verify facts, access live systems
  -  User sends a Query. LLM generates a Response. Communication is stateless:
        -  No memory
        -  No awareness of past interactions
        -  No access to external sources
        -  This is a closed-book exam model.
  -  LLMs fail when questions depend on information that was NOT part of training

Examples:
  -  ❌ “What tables are in my PostgreSQL database?”
  -  ❌ “What’s today’s production error log?”
  -  ❌ “What policy did my company publish last week?”

The model will either:
  -  Hallucinate
  -  Give a generic answer
  -  Say it doesn’t know


**RAG**  ======================================================================  
Modern production systems add:
  -  🔍 Retrieval (Vector DB)
  -  📄 External data (PDFs, DBs, APIs)
  -  🧠 Grounding (context injection)

That upgraded version is called **RAG (Retrieval-Augmented Generation)**.

  -  RG uses the latest data stored in a vector database
  -  The data is converted into Vector embeddings, mathematical representations of text and saved in the database
  -  When a query is made relevant data is retrieved and passed to the LLM (large language model)
  -  LLM (large language model) which then generates a contextual and accurate response


<details>
<summary><strong>🧩 What problems does Ollama solve?</strong></summary>

**Without Ollama:**  
  -  You depend on cloud APIs 🌐
  -  You pay per request 💰
  -  Your data leaves your system 🔓

**With Ollama:**  
✅ Runs fully local  
✅ No internet needed after download  
✅ Your data never leaves your laptop  
✅ Free & open-source  
✅ Simple CLI + REST API

**🤖 What models can Ollama run?**  
Ollama supports many popular open-source LLMs:  
| Model         | Best For                |
| ------------- | ----------------------- |
| **Llama 3**   | General chat, reasoning |
| **Mistral**   | Fast & lightweight      |
| **CodeLlama** | Coding assistant        |
| **Phi**       | Small, fast, low RAM    |
| **Gemma**     | Google’s open LLM       |

**🏗 How Ollama works (simple architecture)**  
```
You (CLI / Angular / API)
        |
        v
Ollama Server (localhost:11434)
        |
        v
LLM Model (Llama, Mistral, etc.)
        |
        v
Response (Text / Stream)
```
  -  Ollama runs a local AI server
  -  Your app talks to it via HTTP API
  -  Model runs on CPU or GPU

</details>

## AI
<details>
<summary><strong>AI Youtube Videos</strong></summary>
  
  -  [![20 AI Concepts Explained in 40 Minutes]](https://www.youtube.com/watch?v=OYvlznJ4IZQ)
  -  [![RAG Explained For Beginners]](https://www.youtube.com/watch?v=_HQ2H_0Ayy0)
  -  [![AI Complete OneShot Course for Beginners - HINDI]](https://www.youtube.com/watch?v=D1eL1EnxXXQ)
  -  [![AI full Course for Beginners | Learn N8N, Web Dev, AI Content & AI Agents - HINDI]](https://www.youtube.com/watch?v=DaUxBGfYSVQ)

</details>

<details>
<summary><strong>RAG (Retrieval-Augmented Generation)</strong></summary>

<img src="https://github.com/piyalidas10/AI/blob/a9da8107a506f6bb6e0d714051e58382f0f6f038/imgs/rag.png" width="600px"/>

RAG Solution
```
User Question
 ↓
Search company data (DB, PDFs, APIs)
 ↓
Inject relevant context into prompt
 ↓
LLM generates grounded answer
```

> 🔷LLM does NOT read your documents directly. It retrieves relevant chunks from a vector DB and augments the prompt with them before generating an answer.
> “RAG retrieves relevant knowledge from a vector database and injects it into the LLM prompt so the model generates grounded, context-aware answers instead of hallucinating.”

</details>

<details>
<summary><strong>🧑‍💻 Copilots (Human-in-the-loop AI)</strong></summary>

<img src="https://github.com/piyalidas10/AI/blob/0fc8fc42ba1c00aed48a74525636cc4f333e613d/imgs/modern_ai_system.jpg" width="500px" />

Copilot ≠ Agent
  -  Agent: autonomous
  -  Copilot: assists a human

```
User working
 ↓
Context capture (code, doc, email)
 ↓
LLM suggestion
 ↓
Human approves/edits
```
Real products
  -  GitHub Copilot
  -  Microsoft 365 Copilot
  -  Cursor / Codeium

</details>

<details>
<summary><strong>Enterprise Support AI - Putting EVERYTHING Together (One Real System)</strong></summary>

```
Chat UI
 ↓
Copilot UX
 ↓
RAG (company KB, tickets)
 ↓
Agent (can create Jira tickets)
 ↓
LLM (GenAI)
 ↓
Safe Response
```
This system uses:
  -  AI (rules)
  -  ML (ticket classification)
  -  Deep Learning (language understanding)
  -  GenAI (response generation)
  -  RAG (company data)
  -  Agents (task execution)
  -  Copilot (human approval)

</details>

<details>
<summary><strong>ChatGPT</strong></summary>

**ChatGPT = Generative AI system built on Deep Learning (Transformers) with system layers around it**  
In real systems, it’s combined with RAG for grounding, agents for autonomy, and copilots for human-assisted workflows.
```
User
 ↓
Frontend (Chat UI / API Client)
 ↓
Prompt Orchestrator
  - System prompt
  - User prompt
  - Context
 ↓
LLM (GPT-4/5, etc.)
 ↓
Optional:
 - Tools / Functions
 - Browsing
 - Code execution
 ↓
Response Formatter
 ↓
User
```
👉 ChatGPT itself is NOT just a model. It’s a full AI product wrapping a GenAI model.

</details>

<details>
<summary><strong>What is AI ? How many types of AI ?</strong></summary>
AI is a computer program that can do things that normally require a human mind. This includes things like learning, recognizing patterns, understanding language, and making decisions.

<img src="https://github.com/piyalidas10/AI/blob/88c87d782663baaca78aef01e7df91fbb8712541/imgs/ai_img.png" width="400px" />

This is the classic way to think about AI's "level of intelligence."

1️⃣ Types of AI based on Capability
----------------------------------------------------------------------------
**🔹 1. Narrow AI (Weak AI)**  
👉 Built to do one specific task really well.

Examples
  -  Chatbots likes ChatGPT
  -  Voice Assistants: Siri, Alexa, Google Assistant understanding your speech.
  -  Face recognition : Facebook recognizing faces in your photos.
  -  Recommendation systems (Netflix, Amazon): Netflix suggesting shows, Spotify creating Discover Weekly.
  -  Voice assistants (Alexa, Siri)
  -  Spam Filters: Your email client learning to detect junk mail.
  -  Navigation: Google Maps predicting traffic and optimizing your route.

**🔹 2. General AI (Strong AI)**   
👉 Can understand, learn, and apply knowledge across any intellectual task a human can.

Abilities
  -  Understand context
  -  Transfer knowledge between tasks
  -  Learn autonomously
  -  Theoretical Example: A robot that can cook breakfast, have a philosophical conversation, then learn to fix a car—all with common sense.

> 🚫 Does not exist yet (still theoretical)

**🔹 3. Super AI**  
👉 Intelligence that surpasses humans in every aspect. Self-improving, potentially incomprehensible to humans.

Examples (fictional)
  -  Skynet
  -  Jarvis (Iron Man)
  -  ⚠️ Purely hypothetical & sci-fi for now
  -  Theoretical Example: An AI that solves climate change, cures all diseases, and invents physics beyond our understanding.

2️⃣ Types of AI based on Functionality
----------------------------------------------------------------------------
**🔹 1. Reactive Machines**  
👉 No memory, no learning from past  
Example : IBM's Deep Blue (chess computer), basic spam filters.

**🔹 2. Limited Memory AI**  
👉 Uses past data to make decisions  
Examples : Self-driving cars, Chatbots, Recommendation engines  
✅ Most modern AI falls here

**🔹 3. Theory of Mind AI**  
👉 Understands emotions, beliefs, intentions  
🧠 Still in research phase

**🔹 4. Self-Aware AI**  
👉 Conscious, self-reflective  
🚫 Doesn’t exist. This would be a form of AGI/ASI.  
Example: A robot that knows it's a robot and has desires.

3️⃣ Types of AI based on Technology / Approach
----------------------------------------------------------------------------
**🔹 1. Machine Learning (ML) - AI that learns from data.**  
  -  Supervised Learning: Learns from labeled data (cat/not cat photos)
  -  Unsupervised Learning: Finds patterns in unlabeled data (customer segmentation)
  -  Reinforcement Learning: Learns by trial and error with rewards (AlphaGo)
  -  Semi-supervised Learning: Mix of labeled and unlabeled data

**🔹 2. Deep Learning (DL) - ML using neural networks**
  -  Image recognition
  -  Speech recognition
  -  LLMs
  -  Convolutional Neural Networks (CNNs): For images/video
  -  Recurrent Neural Networks (RNNs): For sequential data (time series, text)
  -  Transformers: The architecture behind ChatGPT (processes all data at once)
  -  Generative Adversarial Networks (GANs): Generate realistic fake data

**🔹 3. Natural Language Processing (NLP) - Understands human language**
  -  Translation
  -  Chatbots
  -  Sentiment analysis

**🔹 4. Computer Vision - Interprets images & videos**
  -  Face detection
  -  OCR
  -  Medical imaging

**🔹 5. Generative AI 🔥 - Creates new content**
  -  Text (ChatGPT)
  -  Images (DALL·E)
  -  Code (Copilot)

**🔹 6. Robotics: AI in physical machines** 
  -  Boston Dynamics robots

**🔹 7. Discriminative AI - Classifies or distinguishes between things**  
  -  Spam filters
  -  facial recognition
  -  medical diagnosis AI

**🔹 8. Predictive AI - Forecasts future outcomes**
  -  Stock prediction
  -  weather forecasting
  -  demand planning

</details>

<details>
<summary><strong>AI Subdomains</strong></summary>

```
              Artificial Intelligence
                     │
     ┌───────────────┼────────────────┐
     │               │                │
Machine Learning   Symbolic AI     Search/Planning
     │
Deep Learning
     │
 ┌───┼────┐
NLP  CV  Speech
     │
Generative AI
     │
Multimodal + Agents
```
  
**1️⃣ Machine Learning (ML)**  
Learns patterns from historical data   
Products
  -  Netflix / Amazon → Recommendation engines
  -  Stripe / PayPal → Fraud detection
  -  Google Ads → Click-through prediction
  -  Uber → Demand & pricing prediction
  -  Credit scoring systems
  -  Fraud detection
  -  Search ranking

Used heavily in:
  -  FinTech
  -  E-commerce
  -  Marketing analytics

**2️⃣ Deep Learning (DL)**  
Understands complex data (image, speech, text)    
Products
  -  Google Photos → Image recognition
  -  Tesla Autopilot → Perception systems
  -  YouTube → Video classification
  -  Spotify → Audio understanding
  -  Face ID
  -  Speech-to-text (Alexa, Siri)
  -  Autonomous driving vision

Used heavily in:
  -  Computer Vision
  -  Speech recognition
  -  NLP (pre-GenAI era)

**3️⃣ Natural Language Processing (NLP)**
Understanding & generating text  
Products
  -  Gmail → Smart Reply
  -  Google Search → Query understanding
  -  Zendesk / Intercom → Support automation
  -  Grammarly → Writing assistance

📌 Text → meaning → action

**4️⃣ Computer Vision (CV)**  
Understanding images & videos  
Products
  -  Face ID (Apple) → Face recognition
  -  Google Lens → Image search
  -  Amazon Go → Checkout-free stores
  -  Medical imaging tools → Tumor detection

📌 Cameras + CNNs + DL

**5️⃣ Speech & Audio AI**  
Voice & sound processing  
Products
  -  Alexa / Siri / Google Assistant → Voice assistants
  -  Zoom → Live captions
  -  Call center IVR systems → Speech recognition
  -  Descript → Audio editing with text

📌 ASR + TTS pipelines

**6️⃣ Generative AI 🔥**  
Creates new content  
Products
  -  ChatGPT / Claude / Gemini → Text generation
  -  DALL·E / Midjourney → Image generation
  -  GitHub Copilot → Code generation
  -  Notion AI → Content creation
  -  Adobe Firefly → design

📌 LLMs + Diffusion models

**7️⃣ Reinforcement Learning (RL)**  
Decision-making via rewards  
Products
  -  AlphaGo → Game strategy
  -  Robotics systems → Motion control
  -  Ad bidding systems → Budget optimization
  -  Warehouse robots (Amazon) → Navigation

📌 Trial → reward → optimize

**8️⃣ Knowledge Representation & Reasoning (KRR)**   
Rules, logic, symbolic reasoning  
Products
  -  Tax software → Rule-based compliance
  -  Medical expert systems → Diagnosis support
  -  Policy engines → Access control decisions

📌 Often combined with ML today

**9️⃣ Search, Planning & Optimization**  
Finding best paths & schedules  
Products
  -  Google Maps → Route planning
  -  Airline scheduling systems
  -  Delivery optimization (UPS, FedEx)

📌 Classical AI still very relevant

**🔟 Multimodal AI**  
Multiple input types together  
Products
  -  ChatGPT (Vision) → Image + text
  -  Google Gemini → Text + image + code
  -  Microsoft Copilot → Docs + charts + text

📌 Next-gen assistants

**1️⃣1️⃣ AI Agents & Autonomous Systems 🔥**  
Plan → decide → act  
Products
  -  AutoGPT / LangGraph agents → Task automation
  -  Trading bots → Market actions
  -  Research agents → Report generation
  -  Customer support agents → End-to-end resolution

📌 LLM + tools + memory

**1️⃣2️⃣ Explainable AI (XAI)**  
Transparency & trust  
Products
  -  Credit scoring systems → Decision explanations
  -  Healthcare AI tools → Diagnosis justification
  -  Regulated finance tools → Auditability

📌 Mandatory in regulated industries

**1️⃣3️⃣ Responsible & Ethical AI**  
Safety, fairness, governance  
Products
  -  OpenAI / Google AI guardrails
  -  Content moderation systems
  -  Bias detection platforms

📌 Invisible but critical

</details>

<details>
<summary><strong>Imagine you're using a Financial Research Agent. You ask: "Analyze Tesla's Q4 2024 prospects and recommend if we should invest.". Let’s walk through exactly what happens</strong></summary>

> “A financial research agent decomposes the investment query, retrieves real-time market data via tools, performs financial and qualitative reasoning, evaluates risks through scenarios, applies compliance guardrails, and generates a probabilistic recommendation.”

🟢 STEP 1: Query Understanding (Intent Parsing)
----------------------------------------------------------------------------------
The agent first understands what you want, not just the words.  
It extracts:
  -  Company → Tesla (TSLA)
  -  Timeframe → Q4 2024
  -  Task → Analysis + Recommendation
  -  Domain → Financial / Investment
  -  Decision Type → Buy / Hold / Sell
  -  Risk → High-stakes financial advice ⚠️

📌 Internally:
```
Intent: Investment decision
Assets involved: Public equity
Constraints: Needs up-to-date financial data
```

🟢 STEP 2: Task Decomposition (Agent Planning)
----------------------------------------------------------------------------------
The agent breaks the problem into subtasks.  
Typical plan:
  -  Collect Tesla Q4 2024 data
  -  Analyze financial performance
  -  Analyze business & market factors
  -  Analyze risks
  -  Compare with peers
  -  Generate investment recommendation
  -  Add disclaimer & confidence level

📌 This is called agent planning.

🟢 STEP 3: Data Collection (Tool Use 🔧)
----------------------------------------------------------------------------------
The agent now calls tools, not its memory.  
Data Sources:
  -  Earnings reports (Q4 2024)
  -  Revenue, margins, EPS
  -  Vehicle delivery numbers
  -  Energy business performance
  -  Market news (price cuts, competition)
  -  Macroeconomic data (interest rates)
  -  Analyst consensus

📌 Internally:
```
Tool: Financial API
Tool: Market News API
Tool: SEC filings
```
**👉 This is where RAG (Retrieval-Augmented Generation) happens.**

🟢 STEP 4: Data Validation & Freshness Check
----------------------------------------------------------------------------------
The agent checks:
  -  Is the data latest?
  -  Any conflicting numbers?
  -  Missing info?

If something is outdated:
  -  ➡️ It re-queries sources
  -  ➡️ Or marks uncertainty explicitly

🟢 STEP 5: Financial Analysis
----------------------------------------------------------------------------------
Now the reasoning kicks in.  
The agent analyzes:
  -  Revenue growth / decline
  -  Gross margin trends
  -  EPS vs expectations
  -  Cash flow
  -  CapEx & R&D
  -  Price-cut impact on margins

> 📌 Example reasoning: “Margins declined due to aggressive pricing, but delivery volume grew.”

🟢 STEP 6: Business & Strategic Analysis
----------------------------------------------------------------------------------
The agent evaluates qualitative factors:
  -  EV market competition (BYD, legacy auto)
  -  FSD progress & regulation
  -  Energy storage growth
  -  AI / robotics optionality
  -  CEO influence (Elon factor)
  -  This is non-numeric reasoning.

🟢 STEP 7: Risk Assessment ⚠️
----------------------------------------------------------------------------------
Critical step for financial agents.  
Risks Identified:
  -  Margin compression
  -  Regulatory scrutiny
  -  Demand volatility
  -  China market risk
  -  Interest rate sensitivity
  -  Each risk is weighted.

🟢 STEP 8: Scenario Modeling
----------------------------------------------------------------------------------
The agent often simulates multiple futures:  
| Scenario  | Outcome                   |
| --------- | ------------------------- |
| Bull Case | Strong AI + Energy growth |
| Base Case | Stable but slow growth    |
| Bear Case | Margin erosion continues  |

🟢 STEP 9: Recommendation Logic
----------------------------------------------------------------------------------
Now comes the decision engine.  

The agent:
  -  Matches analysis to investor profile
  -  Applies investment heuristics
  -  Considers valuation vs growth

📌 Example logic:
```
If risk > reward → HOLD
If upside >> downside → BUY
```

🟢 STEP 10: Safety & Compliance Layer 🛡️
----------------------------------------------------------------------------------
Because this is financial advice, the agent:
  -  Avoids guarantees
  -  Uses probabilistic language
  -  Adds disclaimers
  -  Encourages independent judgment
  -  This is Responsible AI enforcement.

🟢 STEP 11: Response Generation
----------------------------------------------------------------------------------
Finally, the agent writes the answer:

Typical structure:
  -  Executive summary
  -  Financial performance
  -  Growth drivers
  -  Risks
  -  Final recommendation
  -  Confidence level

🟢 STEP 12: Output to User 📤
----------------------------------------------------------------------------------
You receive a clear, structured, decision-oriented answer like:
```
Recommendation: HOLD (Moderate Risk)
Tesla shows innovation strength, but near-term margin pressure limits upside in Q4 2024.
```

</details>

<details>
<summary><strong>AI Questions & Answers</strong></summary>

Q: What happens if RAG returns irrelevant docs?  
👉 “We add confidence scoring and allow the model to say ‘I don’t know’.”

Q: Can RAG be attacked?  
👉 “Yes, via indirect prompt injection embedded in documents.”

Q: Why not let Angular call OpenAI directly?  
👉 “Security, cost control, prompt safety, and auditability.”

</details>

