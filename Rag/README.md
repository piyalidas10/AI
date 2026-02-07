# ✅ RAG (Retrieval-Augmented Generation)

<img src="https://github.com/piyalidas10/AI/blob/3f48d0a94bd2fb9b9b4227611974dbdf2ac676e0/Rag/img/RAG.png" width="600px" />

```
Data Sources  →  Vector DB  →  LLM
     (You own)      (RAG)       (Reasoning)
```

**“RAG retrieves relevant knowledge from a vector database and injects it into the LLM prompt so the model generates grounded, context-aware answers instead of hallucinating.”**

**🔷LLM does NOT read your documents directly. It retrieves relevant chunks from a vector DB and augments the prompt with them before generating an answer.**

### 🧱 RAG has TWO clear phases
```
1️⃣ Indexing Phase (Offline / One-time)
2️⃣ Query Phase (Runtime / Every question)
```

<details>

<summary><strong>What is RAG ?</strong></summary>

## What is RAG ?
> chatGPT or Deepseek are good for generaic answers but if you ask a specific question related to your datatbase, it will fail. Because it has not seen that data. So along with the question we also provide the additional data and instructions how to access the data. Example "what are the table names and column names are present in the database?" These instructions must be very precise that is why data scientists and prompt engineers come into pictures. Which is why it is known as prompt engineering. When now you are asking a question you are supplimenting it or augmenting it with your database and additional instructions to formulate these answers. So the LLM goes and generate a response by retrieving the data from your database. The whole setup is known as Retrieval-Augmented Generation (RAG)

#### 1️⃣ Why ChatGPT / DeepSeek fail for database-specific questions

  -  Models like ChatGPT or DeepSeek are trained on public, generic data
  -  They do not have access to:
       -  Your internal databases
       -  Company sales data
       -  Private tables or schemas

📌 Example: “What were my sales last quarter?”

❌ The LLM cannot answer this on its own because:
     It has never seen your database
     It cannot directly query your systems


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


