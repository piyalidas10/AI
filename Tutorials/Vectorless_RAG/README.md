# Vectorless RAG

**Read the bellow Tutorial**
[Tutorials/Vectorless_RAG/Vectorless RAG.pdf](https://github.com/piyalidas10/AI/blob/bd593d17d100d9cdf0de640118ca5c3d209b6634/Tutorials/Vectorless_RAG/Vectorless%20RAG.pdf)

## Tutorials
1. https://www.youtube.com/watch?v=f3zHina9MTo
2. https://medium.com/@visrow/what-is-pageindex-how-to-build-a-vectorless-rag-system-no-embeddings-no-vector-db-dc097fae3071


PageIndex is a vectorless RAG architecture that retrieves information by reasoning over document structure instead of performing semantic search. Rather than treating a document as a flat pile of text, it treats it as a structured hierarchy — like a textbook with a table of contents.

PageIndex is a vectorless, reasoning-based Retrieval-Augmented Generation (RAG) approach that retrieves answers from long documents without using embeddings, chunking, or a vector database.

Instead of relying on semantic similarity search, PageIndex builds a hierarchical Table of Contents (TOC) tree from a document and uses a Large Language Model (LLM) to reason over that structure. The model first identifies the most relevant section using the document’s hierarchy, then navigates to that section to generate a precise, cited answer.

> Traditional RAG retrieves by similarity.
> PageIndex retrieves by reasoning over structure.

This makes it particularly effective for structured, long-form content such as financial reports, legal contracts, regulatory filings, policy documents, and academic papers.

**Why PageIndex Works?**  

PageIndex works because it separates two cognitive tasks:
1.	Navigation — Determine where the answer should exist.
2.	Extraction — Read only that section and generate the answer.

**This mirrors how humans read:**

When you want to know why something happened in a novel, you don’t skim every page randomly.
You go to the chapter where the relevant event occurred.
PageIndex forces the LLM to behave the same way.
```
Vector RAG:
Query → Find similar chunks

Vectorless RAG:
Query → Traverse tree → Reason → Select path
```
