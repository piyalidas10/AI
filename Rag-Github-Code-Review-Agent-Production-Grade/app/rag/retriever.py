from app.rag.hybrid_retriever import (
    HybridRetriever
)

from app.rag.reranker import Reranker


class Retriever:

    def __init__(
        self,
        vector_store,
        documents
    ):

        self.hybrid = HybridRetriever(
            vector_store,
            documents
        )

        self.reranker = Reranker()

    # ==========================================
    # Retrieve Relevant Documents
    # ==========================================

    def retrieve(
        self,
        query,
        top_k=5
    ):

        # --------------------------------------
        # Hybrid Retrieval
        # --------------------------------------

        docs = self.hybrid.retrieve(
            query=query,
            vector_k=10,
            bm25_k=10
        )

        # --------------------------------------
        # Reranking
        # --------------------------------------

        reranked_docs = self.reranker.rerank(
            query=query,
            documents=docs,
            top_k=top_k
        )

        return reranked_docs