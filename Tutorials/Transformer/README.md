## Transformers in RAG System : FastAPI + Ollama + Qdrant + RAG + Upload UI (Dockerized)

Your architecture has two different Transformer usages:
  -  Embedding Model (Transformer Encoder)
  -  LLM Generator Model (Transformer Decoder or Encoder-Decoder)

```
                ┌──────────────────────┐
                │      FastAPI         │
                └──────────┬───────────┘
                           │
           ┌───────────────┴────────────────┐
           │                                 │
   Document Upload                     User Query
           │                                 │
           ▼                                 ▼
   Transformer Encoder               Transformer Encoder
   (nomic-embed-text)                (nomic-embed-text)
           │                                 │
           ▼                                 ▼
        Vector                             Vector
           │                                 │
           └──────────►  Qdrant  ◄───────────┘
                          │
                    Top-K Chunks
                          │
                          ▼
               Transformer LLM (phi3)
                          │
                    Final Answer
```

**1️⃣ Document Upload (PDF / Text)**  
User uploads document → FastAPI processes it → splits into chunks.  
👉 No Transformer yet.

**2️⃣ Convert Text to Vector (Embedding Phase)**

Here you use: nomic-embed-text (via Ollama). This is a Transformer Encoder model.

Transformer does: Text → Tokenization → Self-Attention → Hidden Layers → Vector Embedding

Output: "Loan interest rate is 8%" → [0.023, -0.91, 0.44, ... 768 dimensions]

These vectors are stored in: 📦 Qdrant

So: Document → Transformer → Vector → Qdrant

⚡ Here Transformer is used for semantic understanding, not text generation.

**3️⃣ User Query**

User asks:
```
“What is the loan interest rate?”
```
Same embedding Transformer runs again:
```
Query → Transformer → Query Vector
```
Then:

Qdrant performs vector similarity search  
(cosine similarity / dot product)  

Returns top-k relevant document chunks.

**4️⃣ Grounded Answer Generation (LLM Phase)**

Now retrieved chunks + user query go to:
  -  phi3 (running inside Ollama)

This is a Transformer-based LLM.

Internally:
```
[User Question]
+
[Retrieved Context from Qdrant]
        ↓
Transformer (Self-Attention)
        ↓
Generates Final Answer
```
So here Transformer is doing:
  -  Context understanding
  -  Reasoning
  -  Token-by-token generation

**🎯 Why Transformers Are Perfect for RAG**  
✅ For Embeddings
  -  Self-attention captures semantic meaning
  -  Similar meaning → similar vectors
  -  Better than traditional NLP

✅ For Generation
  -  Understands long context
  -  Uses retrieved chunks
  -  Reduces hallucination
  -  Produces grounded answers


