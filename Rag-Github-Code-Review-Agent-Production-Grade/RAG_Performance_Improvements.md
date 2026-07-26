# Improve Retrieval of Documents From VectorDB using Maximum Marginal Relevance(MMR) for Balancing relevance and diversity (Langchain and Qdrant DB)

## Similarity Search vs MMR (Maximal Marginal Relevance)

| Method                    | Accuracy           | Complexity | Recommendation     |
| ------------------------- | ------------------ | ---------- | ------------------ |
| Similarity                | Medium             | Low        | Small datasets     |
| MMR                       | High               | Low        | ✅ Best default    |
| Similarity + MMR pipeline | Slight improvement | Medium     | Rarely needed      |
| Hybrid (BM25 + Vector)    | **Highest**        | Higher     | Production systems |


Both retrievers work, but they behave very differently.

```
retriever = vector_store.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 4}
)
```
and
```
retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={"k":3, "fetch_k":10}
)
```
Let’s compare them clearly.

✅ fetch_k = candidate pool 
✅ k = final results    

**1️⃣ Similarity Search (Basic Retrieval)**

search_type="similarity"

This retrieves the top-k most similar chunks based purely on embedding distance.

Example:

Query:
"What are the company office working hours?"

Vector DB may return:

| Rank | Document Chunk                              | Similarity |
| ---- | ------------------------------------------- | ---------- |
| 1    | company handbook – office hours             | 0.73       |
| 2    | company handbook – office hours paragraph 2 | 0.71       |
| 3    | company handbook – intro                    | 0.69       |
| 4    | handbook overview                           | 0.68       |

Problem:

⚠️ All chunks may come from the same document section, giving redundant context.

This is common in **LangChain RAG systems.

Pros

- ✔ Fast
- ✔ Simple
- ✔ Works well for small datasets

Cons

- ❌ Often returns duplicate context
- ❌ Less diverse information
- ❌ Can miss useful chunks

**2️⃣ MMR Retrieval (Recommended for RAG)**

search_type="mmr"

MMR = Maximal Marginal Relevance.

It balances:
- Similarity to the query
- Diversity between retrieved chunks

So instead of retrieving 4 similar chunks from the same document, it spreads them.

Example:

| Rank | Document Chunk                 | Reason              |
| ---- | ------------------------------ | ------------------- |
| 1    | handbook – office hours        | most relevant       |
| 2    | HR policy – work schedule      | different source    |
| 3    | company handbook – remote work | related but diverse |

MMR uses:

score = relevance - redundancy
Role of fetch_k
search_kwargs={"k":3, "fetch_k":10}

Meaning:

1. Fetch 10 candidate chunks
2. Choose 3 diverse chunks

So the model sees better context variety.

**🧠 Why MMR Improves RAG**

In RAG, LLMs perform best when context is:

✔ relevant 
✔ non-repetitive   
✔ diverse  

MMR gives exactly that.

This is why most production RAG systems use it.

| Feature             | Similarity    | MMR                |
| ------------------- | ------------- | ------------------ |
| Speed               | Fast          | Slightly slower    |
| Context diversity   | Low           | High               |
| Duplicate chunks    | Common        | Rare               |
| RAG answer accuracy | Medium        | Higher             |
| Best for            | simple search | **RAG QA systems** |

**✅ Best Choice for Your System**

Use MMR:
```
retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 4,
        "fetch_k": 12
    }
)
```
This usually gives the best RAG performance.

**🚀 One More Important Improvement (Most People Miss)**

Your similarity scores show:
```
0.72
0.55
0.46
```
The last one (insurance policy) should not be retrieved.

Add a score threshold filter:
```
search_kwargs={
    "k":4,
    "fetch_k":12,
    "score_threshold":0.6
}
```
This dramatically improves answer accuracy.

### For performance optimization, focus on these:
```
k
fetch_k
lambda_mult
score_threshold
filter
search_params
```