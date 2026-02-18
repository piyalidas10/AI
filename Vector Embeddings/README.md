# 🔹 What Are Embeddings?

Ollama Embedding : https://ollama.com/search?c=embedding

> Embeddings convert text → numerical vectors.

Example:
```
"I love Kolkata cuisine"
→ [0.021, -0.994, 0.332, ... 768 dimensions]
```

These vectors:
  -  Capture semantic meaning
  -  Allow similarity search
  -  Are used in vector databases (like Qdrant, Weaviate)

## 🔹 What are Embedding Models ?
Embedding models take text, images, or other data and transform them into numerical representations. These numbers capture the essential meaning of the data, allowing machines to understand it better.

Think of it like this: Imagine a dictionary that translates words into unique codes. Embedding models do something similar, but instead of single words, they code complex ideas and relationships.

**Benefits of Embeddings:**  
  -  Semantic Search: Find similar data based on meaning, not just keywords.
  -  Machine Learning: Improve model performance by feeding it meaningful numerical data.
  -  Dimensionality Reduction: Simplify complex data for faster processing.

**Available Embedding Models Online:**  
There are many options available, here are a few resources to get you started:  
  -  Hugging Face: [Hugging Face Embeddings] offers pre-trained models for text and code.
  -  OpenAI API: [OpenAI Embeddings] provides text embedding models with adjustable size for performance optimization.

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
