# ✅ RAG (Retrieval-Augmented Generation)

**“RAG retrieves relevant knowledge from a vector database and injects it into the LLM prompt so the model generates grounded, context-aware answers instead of hallucinating.”**

**🔷LLM does NOT read your documents directly. It retrieves relevant chunks from a vector DB and augments the prompt with them before generating an answer.**

### 🧱 RAG has TWO clear phases
```
1️⃣ Indexing Phase (Offline / One-time)
2️⃣ Query Phase (Runtime / Every question)
```

### 📊 Proper RAG Diagram (Clean & Correct)
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

### 🔁 What EXACTLY Happens When User Enters a Prompt (Step-by-Step)
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

**🔹 6. Similarity Search**  
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

**🔹 7. Prompt Augmentation**  
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

**🔹 8. LLM Generates Answer**  
Now the LLM:
  -  Reads only the provided context
  -  Generates a grounded, accurate answer using your private data
  -  Avoids hallucination

> ✅ Output is based on your documents, not training data

### 🎯 Why RAG Is Powerful
| Problem            | Without RAG | With RAG |
| ------------------ | ----------- | -------- |
| Hallucination      | High        | Low      |
| Private data       | ❌         | ✅       |
| Up-to-date info    | ❌         | ✅       |
| Fine-tuning needed | Yes         | No       |
| Cost               | High        | Lower    |


