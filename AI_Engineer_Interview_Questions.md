# AI Engineer Interview Questions

## In a RAG system with similarity search, how do you make sure that when someone searches for an exact ID like “Order #1766”, it doesn’t return a similar one like “Order #1767” just because they look alike? How can the system correctly find the exact match while still using smart (semantic) search for normal queries?

Root Cause: Semantic search is great for meaning, but terrible for exact identifiers like IDs, order numbers, or codes. It treats "Order #3766" and "Order #3767" as basically the same thing.

**✅ Solutions:**
+ Use Hybrid Search — Combine semantic search (for meaning) with keyword/BM25 search (for exact matches). This way, exact IDs are matched precisely.
+ Add Metadata Filtering — Store order numbers as structured metadata, not just embedded text. Then filter by exact order ID before doing any semantic search.
+ Pre-processing / Chunking Strategy — Make sure order numbers are treated as unique tokens. Avoid burying them inside large text chunks where they lose their identity.
+ Use a dedicated lookup layer — For structured data like order IDs, skip embeddings entirely. Use a direct database or key-value lookup for exact match retrieval.

> **💡 Simple Rule of Thumb:** If the user is searching for something exact (IDs, names, codes) → use keyword/exact match. If they're searching by meaning (concepts, intent) → use semantic search. Best systems use both together.

## Our client is a bank. They want to run this AI on their private servers with ZERO internet access. How do you build an AI that doesn't need the Cloud?

To solve this, you need to shift from Cloud LLMs to Local LLMs.
Here is how you Decode the “No Internet” problem:

1️⃣ Pick an Open-Source Model: Instead of OpenAI, use models like Llama 3 (Meta), Mistral, or Gemma (Google). These are weights you can actually download and own.  
2️⃣ Quantization is Key: A massive model won’t fit on standard office servers. Use Quantization (4-bit or 8-bit) to compress the model so it runs fast on local hardware without losing much “intelligence.”  
3️⃣ Local Serving Tools: Use frameworks like Ollama, vLLM, or LocalAI. These tools create a local API that works exactly like ChatGPT but stays 100% inside the company’s firewall.  
4️⃣ Offline Vector Database: For the RAG pipeline, use local databases like ChromaDB or FAISS. This ensures that even the “search” part of your AI never hits the public web.  

Privacy isn’t a feature; it’s a requirement. 
