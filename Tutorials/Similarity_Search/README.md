# Similarity Search


## What is similarity search?
Suppose a user asks:
```
"How can I reset my password?"
```
A traditional keyword search might look for:
```
reset
password
```
But similarity search converts the query into a vector/embedding:
```
"How can I reset my password?"
              ↓
        Embedding Model
              ↓
[0.12, -0.83, 0.41, 0.67, ...]
```
Documents are also converted into vectors.
```
Document A:
"Steps to change your account password"
              ↓
[0.15, -0.79, 0.43, 0.64, ...]

Document B:
"How to update billing information"
              ↓
[-0.62, 0.21, 0.87, -0.12, ...]
```
The search engine calculates distance/similarity between the query vector and document vectors.

The closest vectors are returned.
```
                 Query
                   ●
                  / \
                 /   \
                ●     ●
          Doc A       Doc C
           
                      ●
                    Doc B
```
So:
```
Query
  ↓
Embedding
  ↓
Vector Search
  ↓
Top-K Similar Vectors
  ↓
Relevant Documents
```
**Common similarity/distance measures include:**
- Cosine similarity
- Euclidean distance
- Dot product

For many text-embedding systems, cosine similarity is a very common concept.

## Why keyword search is not enough

Consider these documents:
```
D1 = "You can change your password from account settings."

D2 = "Our application supports payment through credit cards."

D3 = "Users can update their login credentials."
```
Query:
```
"How do I modify my login password?"
```
Keyword search may struggle because:
```
modify ≠ change
login ≈ account
password ≈ credentials
```
Semantic similarity understands that:
```
"modify password"
        ≈
"change login credentials"
```
because their embeddings are close in vector space.

## Similarity vs distance

There are two common ways of determining similarity.

**Similarity**

Higher score = more similar.
```
Similarity(Query, Document)
```
Example:
```
D1 → 0.92
D2 → 0.71
D3 → 0.34
```
Therefore:
```
D1 > D2 > D3
```

**Distance**

Lower score = more similar.
```
Distance(Query, Document)
```
Example:
```
D1 → 0.08
D2 → 0.29
D3 → 0.81
```
Therefore:
```
D1 > D2 > D3
```

## Similarity Search vs Full-Text Search

This distinction is very important in system design interviews.

| Feature                | Keyword Search      | Similarity Search |
| ---------------------- | ------------------- | ----------------- |
| Matching               | Words               | Meaning           |
| Data                   | Text                | Vectors           |
| Synonyms               | Limited             | Strong            |
| Semantic understanding | ❌                   | ✅                 |
| Exact IDs              | Excellent           | Poor              |
| Typo handling          | Good with analyzers | Variable          |
| RAG                    | Limited             | Core technology   |
| Typical index          | Inverted index      | HNSW/ANN          |
| Example                | Elasticsearch       | Qdrant            |

## Similarity Search inside RAG

A production RAG pipeline typically looks like:
```
             DOCUMENT INGESTION
                     │
                     ▼
                Documents
                     │
                     ▼
                  Chunking
                     │
                     ▼
                Embeddings
                     │
                     ▼
             ┌───────────────┐
             │ Vector DB     │
             │               │
             │ HNSW Index    │
             └───────────────┘
                     ▲
                     │
                     │
User Query ──► Embedding
                     │
                     ▼
              Similarity Search
                     │
                     ▼
                  Top-K
                     │
                     ▼
               Re-ranking
                     │
                     ▼
             Relevant Context
                     │
                     ▼
                    LLM
                     │
                     ▼
                  Answer
```

## Hybrid Search

Production systems often combine:
```
Keyword Search
       +
Vector Search
       ↓
Hybrid Retrieval
```

Why?

Because semantic search is not always good at exact matches.

Example:
```
Query:
"INC-45892"
```
You want exact matching.

Vector search may not be ideal.

But for:
```
"Why does authentication fail after the session expires?"
```
semantic search is excellent.

So:
```
                Query
                  │
          ┌───────┴────────┐
          ▼                ▼
   Keyword Search    Vector Search
          │                │
          └───────┬────────┘
                  ▼
             Fusion/RRF
                  │
                  ▼
              Re-ranking
                  │
                  ▼
             Top Results
```
