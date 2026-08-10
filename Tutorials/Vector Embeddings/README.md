# 🔹 What Are Vector Embeddings?

> **Vectors → Embeddings → Vector Database → Similarity Search**, which is one of the most important parts of a RAG system.

An embedding is not a random number representation. An embedding model learns to map semantically related data to nearby points in a high-dimensional vector space.

Vector embeddings are numerical representations of unstructured data such as:
  -  Text (documents, PDFs, queries)
  -  Images
  -  Audio
  -  Code

Examples of LLM Models:
  -  **nomic-embed-text** → converts text → vector
  -  **CLIP** → converts image + text → vectors
  -  **wav2vec** → converts audio → vectors

Ollama Embedding : https://ollama.com/search?c=embedding

Example:
```
"I love Kolkata cuisine"
→ [0.021, -0.994, 0.332, ... 768 dimensions]
```

These vectors:
  -  Capture semantic meaning
  -  Allow similarity search
  -  Are used in vector databases (like Qdrant, Weaviate)

## What exactly is a vector?

A vector is simply a list of numbers.

**For example:**
```
Apple
 ↓
[0.12, 0.81, -0.23, 0.44, 0.91]
```
**Another:**
```
Banana
 ↓
[0.15, 0.78, -0.20, 0.48, 0.88]
```
**And:**
```
Car
 ↓
[-0.72, 0.13, 0.91, -0.54, 0.11]
```
The embedding model places semantically related things closer together.

**Conceptually:**
```
                 Fruits

          Apple ●
                \
                 ● Banana
                   \
                    ● Mango


                                      Vehicles

                              ● Car
                                   \
                                    ● Bus
```
In reality, embeddings usually have hundreds or thousands of dimensions, not just 2 or 3.

## Why do we need embeddings?

Consider this traditional search:
```
User:
"How can I change my password?"
```
Traditional SQL search might do:
```
SELECT *
FROM documents
WHERE text LIKE '%change%'
   OR text LIKE '%password%';
```
But imagine the document contains:
```
"Users can reset their credentials from the account settings page."
```
There is no exact "change password" match.

Yet the meaning is very similar.

**Semantic search solves this.**
```
"How can I change my password?"
              ↓
         Embedding
              ↓
     [0.21, -0.42, ...]
              ↓
        Vector Search
              ↓
"Users can reset their credentials
 from the account settings page."
```
Even though the words are different, the meaning is similar.

## Why Convert to Numbers?

Computers don’t understand meaning directly.  
They understand numbers and math.  

When text is converted into vectors:
  -  Similar meanings → vectors close together
  -  Different meanings → vectors far apart

This allows:
  -  Semantic search
  -  Similarity matching
  -  Clustering
  -  RAG retrieval
  -  Recommendation systems

## 🔹 What are Embedding Models ?
Embedding models take text, images, or other data and transform them into numerical representations. These numbers capture the essential meaning of the data, allowing machines to understand it better.

<img src="imgs/Correct vs incorrect embedding approach for similarity search.png" width="100%" />

> In a RAG (Retrieval-Augmented Generation) system, the document embeddings and the user query embeddings should generally be created using the same embedding model. This is one of the most important requirements for obtaining accurate similarity search results.

Think of it like this: Imagine a dictionary that translates words into unique codes. Embedding models do something similar, but instead of single words, they code complex ideas and relationships.

**Benefits of Embeddings:**  
  -  Semantic Search: Find similar data based on meaning, not just keywords.
  -  Machine Learning: Improve model performance by feeding it meaningful numerical data.
  -  Dimensionality Reduction: Simplify complex data for faster processing.

**Available Embedding Models Online:**  
There are many options available, here are a few resources to get you started:  
  -  Hugging Face: [Hugging Face Embeddings] offers pre-trained models for text and code.
  -  OpenAI API: [OpenAI Embeddings] provides text embedding models with adjustable size for performance optimization.

## Traditional Search vs Semantic Search

**Traditional keyword search**
```
Query:
"How do I change my password?"

             ↓

      Match exact words

             ↓

     "change"
     "password"

             ↓

       Search Results
```
It primarily focuses on words.

**Semantic search**
```
Query:
"How do I change my password?"

             ↓

       Embedding Model

             ↓

       Query Vector

             ↓

   Similarity Calculation

             ↓

┌─────────────────────────────┐
│ "reset my credentials"      │
│ "forgot my login password"  │
│ "update account password"   │
└─────────────────────────────┘
```
It focuses on meaning.

## What is stored in a vector database?

A common misconception is that the database stores only vectors.

**Usually you store:**
```
┌───────────────────────────────────────┐
│ Vector Database                       │
├───────────────────────────────────────┤
│                                       │
│ ID: 101                               │
│ Vector: [0.12, -0.43, 0.77, ...]     │
│ Text: "Employees receive 25 days..."  │
│ Metadata: {source: "handbook.pdf"}    │
│                                       │
│ ID: 102                               │
│ Vector: [0.21, -0.15, 0.82, ...]     │
│ Text: "Employees can work remotely..."│
│ Metadata: {source: "handbook.pdf"}    │
│                                       │
└───────────────────────────────────────┘
```
The metadata is extremely useful for filtering.

**For example:**
```
department = "HR"
document = "handbook.pdf"
page = 15
```

## Where does ANN come in?

**Your transcript mentions:**
```
Approximate Nearest Neighbor — ANN
```

**Imagine a vector database containing:**
```
10 vectors
```
Easy.

**But a production system might contain:**
```
100 million vectors
```
You don't want to compare the query against every single vector.
```
Query
  │
  ├── compare → Vector 1
  ├── compare → Vector 2
  ├── compare → Vector 3
  ├── compare → Vector 4
  ├── ...
  └── compare → Vector 100,000,000
```
That can be expensive.

ANN indexing algorithms make the search dramatically more efficient by navigating an index designed to find very close candidates without exhaustively checking everything.

**Conceptually:**
```
             Query
               │
               ▼
        ANN Index
        /       \
       /         \
   Candidate    Candidate
      │             │
      ▼             ▼
   Vector A       Vector B
      │
      ▼
   Top-K Results
```
This is why vector databases can perform similarity search efficiently at scale.

## 🔹 What is Nomic Embedding?

Nomic AI created a popular open-source embedding model.    
Nomic embeddings which are heavily used in RAG systems, vector search, semantic search, and retrieval pipelines.    
Nomic embeddings (nomic-embed-text) are a specific, high-performance, open-source model designed for long-context text encoding, often outperforming proprietary models like OpenAI's text-embedding-ada-002.

  -  **Performance**: Specifically, nomic-embed-text is noted for superior performance on both short and long context tasks compared to older OpenAI models.
  -  **Key Features**: It is a 137M parameter, open-source model designed for high-performance RAG (Retrieval-Augmented Generation).
  -  **Context Window**: Supports a very large context length (up to 8192 tokens).
  -  **Usage**: Nomic provides specific task types (e.g., search_query, search_document, classification, clustering) to optimize for different NLP tasks.

One common model:
  -  nomic-embed-text
  -  768 dimensions
  -  Very good semantic performance
  -  Works great with RAG

You can use it via:
  -  Ollama
  -  HuggingFace
  -  Direct API

## Text embeddings vs Nomic embeddings

Nomic embeddings (nomic-embed-text) are a specific, high-performance, open-source model designed for long-context text encoding, often outperforming proprietary models like OpenAI's text-embedding-ada-002.     
Text embeddings are the broader category of converting text into numerical vectors, while Nomic specializes in better, faster, and open-source alternatives for retrieval and semantic search.

**Nomic Embeddings**  
  -  Performance: Specifically, **nomic-embed-text** is noted for superior performance on both short and long context tasks compared to older OpenAI models.
        - nomic-embed-text-v1 with Qdrant : https://qdrant.tech/documentation/embeddings/nomic/
        - ollama : https://ollama.com/library/nomic-embed-text
  -  Key Features: It is a 137M parameter, open-source model designed for high-performance RAG (Retrieval-Augmented Generation).
  -  Context Window: Supports a very large context length (up to 8192 tokens).
  -  Usage: Nomic provides specific task types (e.g., search_query, search_document, classification, clustering) to optimize for different NLP tasks. 

**Text Embeddings (General Concept)**  
  -  Definition: Numerical representations of text (words, sentences, documents) as vectors of real-valued numbers.
  -  Purpose: They map text into a high-dimensional space where vectors that are close together have similar meanings.
  -  Use Cases: Semantic search, classification, clustering, sentiment analysis, and recommendation systems.
  -  Examples: OpenAI text-embedding-3, BERT-based models, nomic-embed-text, OpenAI text-embedding-ada-002. 

Key Differences
  -  Performance: Nomic aims to outperform standard, often proprietary, text embeddings.
  -  Accessibility: Nomic is open-source and often more cost-effective compared to closed, API-driven text embeddings.
  -  Focus: Nomic is tailored heavily towards Retrieval-Augmented Generation (RAG) and handling large documents.


## 🔹 Can You Use Different LLMs with Same Embedding?

YES ✅

Example:
  - Embedding: nomic-embed-text
  - LLM:
    - Llama 3
    - Mistral
    - Phi-3

Embedding model and LLM are independent. That’s a very important architecture principle.

## Why use Same Embedding Model for Converting your Documents into Vectors and Convert the Query into a Vector??????????
When we say:
```
“Query vector generated by the same embedding model”
```
It means:

> 👉 The model used to convert your documents into vectors must be the exact same model used to convert the query into a vector.

**🔎 Why is this important?**  
Because embeddings create a vector space.

If you use different embedding models:
  -  The vector meanings change
  -  Dimensions may change (768 vs 1536 etc.)
  -  The coordinate system changes
  -  Similarity comparison becomes invalid ❌

It’s like:
  -  Storing locations in GPS coordinates
  -  But searching using a different map system

They won’t align.

**Step 1: Store Documents**

Using embedding model Model A  

Document:
```
"Fast car"
```
Converted to:
```
[0.12, -0.89, 0.44, ...]
```
Stored in vector DB.

**Step 2: User Query**

User asks:
```
"Sports vehicle"
```
Now if you use:

**✅ Same Model A**
  -  It converts to a vector in the SAME mathematical space.
  -  Distance calculation works correctly.

**❌ Different Model B**

It produces:
  -  Different dimension size
  -  Different scaling
  -  Different semantic mapping
Now similarity math becomes meaningless.

**🔬 Technical Reason**

Embedding model defines:
  -  Vector dimension size
  -  Meaning encoding logic
  -  Tokenization strategy
  -  Vector distribution pattern

Changing model = changing geometry of space.

Similarity search only works if:
```
All vectors live in same vector space.
```

**📊 Real Production Rule**

When building RAG system:  
✔ Pick embedding model  
✔ Use it for:  
  -  Document indexing
  -  Query embedding

❌ Never mix embedding models inside same vector collection.





