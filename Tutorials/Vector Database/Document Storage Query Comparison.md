# 🟢 FULL FLOW: Document Storage + Query Comparison

> 📄 Document → Vector → Store in DB → Query → Compare → Return Results

**We’ll divide into 2 parts:**

1️⃣ Document Ingestion (Storing Phase)
2️⃣ Query Search (Retrieval Phase)

## 🟦 PART 1: Document → Vector → Store in Vector DB
**🔹 Step 1: Raw Document**

Example document:
```
"FastAPI is a modern Python web framework."
```
This is plain text (unstructured data).

**🔹 Step 2: Convert Text → Embedding**

Using embedding model (for example from Ollama or OpenAI)

It converts text into a numeric vector:
```
[0.21, -0.84, 0.55, 0.10, 0.73, ...]
```

Think of this as:  
👉 A coordinate in 768-dimensional space  
👉 A compressed meaning of the sentence  

**🔹 Step 3: Store in Vector Database**

Example vector database:
  -  Qdrant
  -  Pinecone
  -  Weaviate

The database stores:
```
{
  id: 101,
  vector: [0.21, -0.84, 0.55, 0.10, 0.73...],
  payload: {
      text: "FastAPI is a modern Python web framework",
      source: "blog1"
  }
}
```

Important:
  -  The actual searchable part = VECTOR
  -  The text is stored as metadata (payload)

**🔹 Step 4: Index Creation (Very Important)**

The DB builds a special structure:

👉 HNSW graph (not simple B-tree like SQL)

This makes nearest neighbor search very fast.

Now documents are ready to search.

## 🟢 PART 2: Query → Compare → Return Top-K
🔹 Step 5: User Sends Query

User asks:
```
"FastAPI tutorial"
```

**🔹 Step 6: Query → Embedding**

Same embedding model converts query into vector:
```
Query Vector (Q)
[0.20, -0.80, 0.50, 0.08, 0.70...]
```

⚠ Important:  
Query must use SAME embedding model as documents.

**🔹 Step 7: Similarity Comparison**

Now database compares:
```
Query Vector (Q)
vs
All Document Vectors
```

It calculates similarity score using:
  -  Cosine similarity (most common)
  -  Dot product
  -  Euclidean distance

In simple terms:  
👉 Which vectors are closest to Q in multi-dimensional space?

**🔹 Step 8: Ranking**

Example similarity scores:
```
Doc A → 0.95
Doc B → 0.92
Doc C → 0.30
```

If K = 2

Return:
```
Doc A
Doc B
```

This is called:  
🎯 Top-K Retrieval

## 🔥 COMPLETE VISUAL FLOW

DOCUMENT INGESTION FLOW
-----------------------------------------------------------------
```
Raw Text
   ↓
Embedding Model
   ↓
Vector (Numbers)
   ↓
Store in Vector DB
   ↓
Build HNSW Index
```

QUERY SEARCH FLOW
-----------------------------------------------------------------
```
User Query
   ↓
Embedding Model
   ↓
Query Vector
   ↓
Vector DB
   ↓
Similarity Calculation
   ↓
Find Nearest Neighbors
   ↓
Return Top-K Results
```

## 🧠 What Actually Gets Compared?

NOT:
```
"FastAPI tutorial" == "FastAPI guide"
```

BUT:
```
[0.20, -0.80, 0.50...] 
compared with
[0.21, -0.84, 0.55...]
```
Pure numeric comparison.
