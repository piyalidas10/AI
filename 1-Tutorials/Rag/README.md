# ✅ RAG (Retrieval-Augmented Generation)

**RAG Demo Codes** : https://github.com/whyashthakker/RAG/tree/main

**Retrieval-Augmented Generation (RAG) is an AI architecture that combines:**
- Retrieval – Fetching relevant information from external knowledge sources.
- Augmentation – Adding the retrieved information to the user's prompt as additional context.
- Generation – Using an LLM to generate an accurate answer based on both the user's question and the retrieved context.

Instead of relying only on what the LLM learned during training, RAG allows it to use up-to-date, private, and domain-specific knowledge.

<img src="./img/Retrieval-augmented generation.png" width="100%" />

**👉 RAG = Retriever (search relevant data) + Generator (LLM creates answer)**     
So instead of guessing, the model uses real data at runtime.

**RAG exists because:**
- LLMs hallucinate
- Knowledge is outdated
- Enterprises need grounded, factual answers

RAG (Retrieval-Augmented Generation) is primarily a form of Generative AI that uses external data to enhance accuracy. It acts as a specialized search-and-generation tool, retrieving relevant information to inform LLMs. While standard RAG is a static retrieval method, it can evolve into Agentic AI (Agentic RAG).

<img src="https://github.com/piyalidas10/AI/blob/3f48d0a94bd2fb9b9b4227611974dbdf2ac676e0/Rag/img/RAG.png" width="600px" />

```
Data Sources  →  Vector DB  →  LLM
     (You own)      (RAG)       (Reasoning)
```

**“RAG retrieves relevant knowledge from a vector database and injects it into the LLM prompt so the model generates grounded, context-aware answers instead of hallucinating.”**

**🔷LLM does NOT read your documents directly. It retrieves relevant chunks from a vector DB and augments the prompt with them before generating an answer.**

> Retrieval-Augmented Generation (RAG) is an AI architecture that enhances Large Language Models by combining information retrieval with text generation. Instead of relying only on the model's training data, RAG retrieves relevant information from external sources such as PDFs, databases, Confluence, SharePoint, APIs, or knowledge bases. The retrieved content is added to the user's prompt, and the LLM generates an answer grounded in that context.
> RAG addresses several key challenges of LLMs: it reduces hallucinations, enables access to private and organisation-specific data, keeps responses current without retraining the model, and is significantly more cost-effective than frequent fine-tuning. A typical RAG pipeline involves document ingestion, chunking, embedding generation, storage in a vector database, similarity search, prompt augmentation, and response generation using an LLM.

Common use cases include enterprise knowledge assistants, customer support chatbots, banking and healthcare assistants, legal document search, AI resume coaches, and educational question-answering systems.

## Why do we need RAG?

**Large Language Models (LLMs) like GPT, Claude, Gemini, or Llama are trained on massive datasets.**

**However, they have several limitations:**
- They cannot access your company's private documents.
- They don't automatically know newly created information.
- They may generate incorrect answers (hallucinations).
- Retraining or fine-tuning for every new document is expensive and time-consuming.

RAG solves these problems by retrieving relevant information at inference time.

## Typical RAG Pipeline
```
Documents
(PDFs, Word, Excel)
        │
        ▼
Document Loader
        │
        ▼
Text Chunking
        │
        ▼
Embedding Model
        │
        ▼
Vector Database
(Qdrant, Pinecone, Chroma)
        │
        ▼
User Query
        │
        ▼
Query Embedding
        │
        ▼
Similarity Search
        │
        ▼
Top-K Chunks Retrieved
        │
        ▼
Prompt Augmentation
        │
        ▼
Large Language Model
        │
        ▼
Final Answer
```

## Understanding the Three Components
### 1. Retrieval

Retrieve the most relevant information from external sources.

These sources may include:
```
PDFs
Word documents
Excel files
Databases
SharePoint
Confluence
Websites
APIs
Emails
Knowledge bases
```
Example:

User asks:
> Why is my Vodafone bill £2,500 this month?

Instead of guessing, the system retrieves:
- Customer billing history
- Current month's bill
- International call records
- Roaming usage
- Customer account details

### 2. Augmentation

The retrieved information is added to the prompt.

Example prompt sent to the LLM:
```
User Question:
Why is my bill £2,500?

Retrieved Context:

Customer Name: John

Previous Bills:
£120
£140
£135

Current Usage:
27 International Calls
350 International SMS
Roaming Charges £1,950

Answer the question using only this information.
```
Now the LLM has factual evidence.

### 3. Generation

Finally, the LLM generates an answer using the retrieved context.

Example:
```
Your bill increased because you made 27 international calls while roaming abroad, resulting in £1,950 in roaming charges. Your previous bills were around £120–£140, making this month's bill significantly higher.
```

## RAG Architecture
```
                User Question
                      │
                      ▼
             Query Processing
                      │
                      ▼
             Embedding Model
                      │
                      ▼
          Vector Database Search
      (Qdrant, Pinecone, Weaviate)
                      │
          Top-K Relevant Documents
                      │
                      ▼
           Prompt Augmentation
                      │
                      ▼
             Large Language Model
          (GPT / Claude / Llama)
                      │
                      ▼
             Generated Response
```

## Real-Life Vodafone Example

**Without RAG**

User:
```
Why is my Vodafone bill £2,500?
```
ChatGPT:
```
It might be because of roaming, taxes, late payment or international calls.
```
This is only a generic guess.

**With RAG**

The system retrieves:
```
Customer Database
Current Bill
Call Logs
Usage Details
International Charges
Roaming Charges
```
LLM Response:
```
Your bill is higher because you travelled to Germany from 5th–12th July and incurred £1,950 in roaming charges along with 27 international calls and 350 SMS.
```
This answer is accurate because it uses actual customer data. Without RAG, LLM guesses. With RAG, LLM answers using retrieved evidence.

## 👉 Most real-world systems use:

**Hybrid Retrieval**
+ Reranking
+ Context Compression
+ Guardrails
+ Evaluation

That’s the default production stack.

## Architecture Diagram of all 20 types of RAGs
<img src="img/rag_architechture.png" width="100%" />

### 🧱 RAG has TWO clear phases
```
1️⃣ Indexing Phase (Offline / One-time)
2️⃣ Query Phase (Runtime / Every question)
```

### Here is a breakdown of how RAG fits into these categories:
- **Generative AI (Primary Type)**: RAG enhances generative models by grounding them in factual, external data, reducing hallucinations. It is fundamentally a technique to improve generation, making it a subset of generative AI.
- **Agentic AI (Advanced Form)**: Agentic RAG combines RAG with autonomous agents that can reason, plan, use multiple tools, and break down complex queries into multiple steps. Unlike standard RAG, Agentic RAG acts as a proactive researcher rather than just a lookup tool.
- **Predictive AI**: RAG is not typically classified as predictive AI, which is used for forecasting numerical trends rather than generating content or retrieving information.

### RAG (Retrieval-Augmented Generation) Evaluation Metrics
<img src="./img/RAG%20(Retrieval-Augmented%20Generation)%20evaluation%20metrics.png" width="100%" />


<details>

<summary><strong>What is RAG ?</strong></summary>

## What is RAG ?
> chatGPT or Deepseek are good for generaic answers but if you ask a specific question related to your datatbase, it will fail. Because it has not seen that data. So along with the question we also provide the additional data and instructions how to access the data. Example "what are the table names and column names are present in the database?" These instructions must be very precise that is why data scientists and prompt engineers come into pictures. Which is why it is known as prompt engineering. When now you are asking a question you are supplimenting it or augmenting it with your database and additional instructions to formulate these answers. So the LLM goes and generate a response by retrieving the data from your database. The whole setup is known as Retrieval-Augmented Generation (RAG)

Retrieval-Augmented Generation (RAG) is a technique where an LLM retrieves relevant external data at query time and uses it, along with precise instructions, to generate accurate and context-aware responses without retraining the model.

<img src="https://github.com/piyalidas10/AI/blob/fcc09341ef2c5a7309d03d57af14ed8bf402fc70/Rag/img/RAG1.png" width="600px" />

## What is RAG vs LLM?
An LLM (Large Language Model) is the core AI that understands and generates text, while RAG (Retrieval-Augmented Generation) is an architecture that enhances LLMs by connecting them to external data sources (like documents or databases) to provide more current, factual, and domain-specific answers, preventing "hallucinations" and allowing source citations. Think of a base LLM as having general knowledge, while a RAG system gives that LLM a real-time "library card" to look up specific, up-to-date facts before responding. 

#### 1️⃣ Why ChatGPT / DeepSeek fail for database-specific questions

  -  Models like ChatGPT or DeepSeek are trained on public, generic data
  -  They do not have access to:
       -  Your internal databases
       -  Company sales data
       -  Private tables or schemas

📌 Example: “What were my sales last quarter?”

❌ The LLM cannot answer this on its own because:
  -  It has never seen your database
  -  It cannot directly query your systems

#### 2️⃣ The need for supplying external data

To answer specific business questions, we must provide the data explicitly.

This means:
  -  Fetching data from:
       -  Databases (Sales, Inventory, Finance)
       -  CSV / Excel files
       -  APIs or internal systems
  -  Supplying that data along with the user’s question

📌 This is where retrieval comes into the picture.

#### 3️⃣ Adding precise instructions (System Prompt)

Along with data, we also provide very precise instructions, such as:
  -  What tables exist
  -  What columns exist
  -  How the data should be interpreted

📌 Example system instructions:
```
You are an intelligent assistant.
The database contains two tables:
1. sales
2. inventory
Use this data to answer the user query accurately.
```
✔️ These instructions guide the LLM  
✔️ Prevent hallucinations  
✔️ Ensure correct interpretation of data  

#### 4️⃣ Role of Data Scientists & Prompt Engineers

This is where Data Scientists and Prompt Engineers come into the picture.

Their responsibilities:
  -  Designing clear and unambiguous prompts
  -  Structuring retrieved data properly
  -  Ensuring:
       -  Correct context
       -  Minimal noise
       -  Accurate responses

📌 This discipline is called Prompt Engineering.
> Poor prompt → Wrong answer
> Well-engineered prompt → Accurate, grounded answer

#### 5️⃣ Augmenting the question with data (Core idea of RAG)

When a user asks a question:
  -  We augment (supplement) the question with:
      -  Retrieved data from the database
      -  System instructions

📌 Final prompt sent to the LLM looks like:
```
Question + Retrieved Data + Instructions
```
This is the augmentation part.

#### 6️⃣ Retrieval + Generation flow

The LLM does not directly access the database.

Instead:
  -  Relevant data is retrieved first
  -  Data is injected into the prompt
  -  The LLM generates an answer using only that context

> 📌 Example output: “Sales in the last quarter was $2.3M”

✔️ Factual  
✔️ Based on your data  
✔️ No guessing  

#### 7️⃣ Why this setup is called Retrieval-Augmented Generation (RAG)
| Term       | Meaning                                       |
| ---------- | --------------------------------------------- |
| Retrieval  | Fetching relevant data from your database     |
| Augmented  | Adding that data + instructions to the prompt |
| Generation | LLM generates a natural language response     |
📌 Entire setup = RAG

</details>

<details>

<summary><strong>Proper RAG Diagram (Clean & Correct)</strong></summary>

## 📊 Proper RAG Diagram (Clean & Correct)
```
┌───────────────────────────────┐
 │        DATA SOURCES            │
 │  • PDFs  • Docs  • CSVs        │
 │  • DB rows • APIs              │
 └───────────────┬───────────────┘
                 │
                 ▼
 ┌───────────────────────────────┐
 │   Document Loader & Parser     │
 │ (PDF → text, CSV → rows, etc.) │
 └───────────────┬───────────────┘
                 │
                 ▼
 ┌───────────────────────────────┐
 │        Chunking                │
 │  (300–1000 tokens per chunk)   │
 │  + overlap (e.g. 50 tokens)    │
 └───────────────┬───────────────┘
                 │
                 ▼
 ┌───────────────────────────────┐
 │     Embedding Model            │
 │  "Text → Vector (numbers)"     │
 └───────────────┬───────────────┘
                 │
                 ▼
 ┌───────────────────────────────┐
 │        Vector Database         │
 │  (Pinecone / FAISS / Chroma)   │
 │  Stores:                       │
 │  • vector                      │
 │  • original text chunk         │
 │  • metadata                    │
 └───────────────────────────────┘
```
##### 🔹 1. Read the Document (Indexing Phase)
**What happens**  
  -  PDFs → text
  -  CSV → rows
  -  Docs → paragraphs

**Why**
  -  LLM cannot read raw files
  -  Everything must become plain text

##### 🔹 2. Create Chunks
**Why chunking is mandatory**  
  -  LLM context window is limited
  -  Retrieval works better on smaller text units

**Typical values**
```
Chunk size: 300–1000 tokens
Overlap:    50–200 tokens
```
**Example**
```
Chunk 1: "RAG is a technique that..."
Chunk 2: "The indexing phase converts..."
```

##### 🔹 3. Contextual Embedding
**Key concept**
```
Embedding = semantic meaning → numbers
```
Example:
```
"This is an invoice" → [0.021, -0.33, 0.89, ...]
```
  -  ✔ Same meaning → vectors close together
  -  ✔ Different meaning → vectors far apart

⚠️ Your slide’s ##### is showing vectors

##### 🔹 4. Store in Vector DB
Each record contains:
```
{
  vector: [0.021, -0.33, ...],
  text: "Original chunk text",
  metadata: {
    source: "invoice.pdf",
    page: 12
  }
}
```
**Popular Vector DBs**  
  -  Pinecone
  -  Chroma
  -  FAISS
  -  Weaviate

</details>

<details>

<summary><strong>What EXACTLY Happens When User Enters a Prompt</strong></summary>

## 🔁 What EXACTLY Happens When User Enters a Prompt (Step-by-Step)
“When a user enters a prompt, RAG converts it into an embedding, retrieves semantically similar document chunks from a vector database, injects them into the prompt, and then lets the LLM generate a grounded response.”
```
════════════════ QUERY TIME ════════════════


 ┌───────────────────────────────┐
 │         User Question          │
 │   "How does RAG work?"         │
 └───────────────┬───────────────┘
                 │
                 ▼
 ┌───────────────────────────────┐
 │   Question Embedding           │
 │  Same embedding model used     │
 └───────────────┬───────────────┘
                 │
                 ▼
 ┌───────────────────────────────┐
 │ Similarity Search (Top-K)      │
 │ Cosine / Dot / Euclidean       │
 └───────────────┬───────────────┘
                 │
                 ▼
 ┌───────────────────────────────┐
 │  Retrieved Relevant Chunks     │
 └───────────────┬───────────────┘
                 │
                 ▼
 ┌───────────────────────────────┐
 │ Prompt Augmentation            │
 │ System Prompt + Context + Q    │
 └───────────────┬───────────────┘
                 │
                 ▼
 ┌───────────────────────────────┐
 │           LLM                  │
 │  GPT / LLaMA / Mistral         │
 └───────────────────────────────┘
                 │
                 ▼
        ✅ Grounded Answer
```
**Let’s assume the user types: “How does RAG work?”**

> User Prompt is NOT sent directly to LLM
> 🚫 Important misconception : The LLM does not answer immediately.

**Why?**
  -  LLM has no knowledge of your private documents.
  -  It must retrieve context first

**🔹 1. User Query (Prompt) → Embedding**  
The question is converted into a vector:
```
User: "How does RAG work?"
→ [0.12, -0.44, 0.88, ...]
```

> Converted to vector using SAME embedding model
> ⚠️ Same embedding model must be used (e.g., text-embedding-3-large, nomic-embed-text, etc.)
> ⚠️ This is critical for correct similarity search

**🔹 2. Similarity Search**  
Vector DB compares:
```
Query Vector
   ↕ cosine similarity
Stored Chunk Vectors
```

Returns:
```
Top-K most relevant chunks (K = 3–10)
Top 3–5 most relevant chunks
```

Example:
  -  Chunk from “RAG architecture.pdf”
  -  Chunk from “LLM retrieval notes.txt”

**🔹 3. Prompt Augmentation**  
Now the system builds the final prompt. LLM prompt becomes:
```
SYSTEM:
You are a helpful assistant.

CONTEXT:
Chunk 1: RAG has two phases...
Chunk 2: Embeddings represent semantic meaning...
Chunk 3: Vector databases enable similarity search...

USER QUESTION:
How does RAG work?
```

> 👉 This is why it’s called Retrieval-Augmented Generation (RAG)

**🔹 4. LLM Generates Answer**  
Now the LLM:
  -  Reads only the provided context
  -  Generates a grounded, accurate answer using your private data
  -  Avoids hallucination

> ✅ Output is based on your documents, not training data

</details>

<details>

<summary><strong>RAG Questions & Answers</strong></summary>

### 🎯 Why RAG Is Powerful
| Problem            | Without RAG | With RAG |
| ------------------ | ----------- | -------- |
| Hallucination      | High        | Low      |
| Private data       | ❌         | ✅       |
| Up-to-date info    | ❌         | ✅       |
| Fine-tuning needed | Yes         | No       |
| Cost               | High        | Lower    |

### 1️⃣ Where does RAG get its data from?
ANs. RAG data sources are external systems. RAG does not invent data. You explicitly ingest data into the vector database during the indexing phase.

> “RAG gets its data from external knowledge sources such as documents, databases, or APIs that are ingested, embedded, and stored in a vector database. At query time, it retrieves relevant chunks from this indexed data to augment the LLM’s response.”

Common real-world data sources 👇
##### 📁 Files & Documents (most common)
 - PDFs (manuals, policies, invoices)
 - Word / Text files
 - PowerPoint decks
 - CSV / Excel files

**✅ Example:**
 - Company HR policy PDFs
 - Product documentation

##### 🗄️ Databases
 - PostgreSQL / MySQL
 - MongoDB
 - Data warehouse tables

**✅ Example:**
 - Orders table
 - Customer support tickets
👉 Rows → text → chunks → embeddings

##### 🌐 APIs & Services
 - Internal microservices
 - REST / GraphQL APIs
 - SaaS tools (Jira, Confluence, Notion)

**✅ Example:**
 - Jira issues
 - Confluence wiki pages

##### ☁️ Cloud Storage
 - AWS S3
 - Azure Blob
 - Google Cloud Storage

**✅ Example:**
 - Logs
 - Uploaded customer documents

##### 📡 Streaming / Event Data (advanced)
 - Kafka topics
 - Event logs
 - IoT feeds (snapshotted)

⚠️ Usually summarized before embedding

### 2️⃣ How does data reach RAG? (Important)
Ans. RAG never pulls data live at answer time (usually).

**✅ Correct flow**
```
External Data Source
      ↓
Ingestion Pipeline
      ↓
Parsing + Cleaning
      ↓
Chunking
      ↓
Embedding
      ↓
Vector Database
```
👉 At query time, RAG only talks to the vector DB, not the raw source.

### 3️⃣ Example: Enterprise RAG Data Sources
**🏢 Company Chatbot**
| Source     | Purpose          |
| ---------- | ---------------- |
| PDFs       | HR policies      |
| DB tables  | Employee info    |
| Confluence | Engineering docs |
| Jira       | Incident history |

**🧪 Local Ollama RAG**
| Source       | Purpose        |
| ------------ | -------------- |
| Local folder | Markdown docs  |
| CSV files    | Knowledge base |
| SQLite       | App data       |

### 4️⃣ What RAG does NOT use as a data source ❌

❌ LLM training data  
❌ Internet (unless you build a crawler)  
❌ User prompt history (unless you store it)  

LLM = reasoning engine, not knowledge store.

### 5️⃣ Who decides the data source?

👉 You do. RAG is just a pattern, not a product.

You decide:
 - What data to ingest
 - How often to update it
 - How fresh it should be

</details>


