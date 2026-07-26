# =========================
# get_relevant_documents() is becoming deprecated in newer LangChain versions.
# We should also improve:
# 1) logging
# 2) configurable k
# 3) better retrieval settings
# 4) cleaner production structure
# =========================

from loguru import logger


class Retriever:

    def __init__(self, vector_store):

        self.vector_store = vector_store

    # def get_retriever(self, k: int = 4):

    #     return self.vector_store.as_retriever(
    #         search_type="similarity",
    #         search_kwargs={
    #             "k": k
    #         }
    #     )

    # def retrieve(self, query: str, k: int = 4):

    #     logger.info(f"Retrieving documents for query: {query}")

    #     retriever = self.get_retriever(k)

    #     # This aligns with:
    #     # Runnable interfaces
    #     # Chains
    #     # LangGraph
    #     # Agent workflows

    #     docs = retriever.invoke(query)

    #     logger.info(f"Retrieved {len(docs)} documents")

    #     return docs
    
    # ============================================
    # Best Retrieval Settings for Code RAG
    # Recommended:

    # search_type="mmr"
    # k=6
    # fetch_k=30

    # Especially useful for:
    # large repos
    # repeated utility functions
    # similar files
    # duplicated code
    # ============================================

    def get_retriever(self, k: int = 6):

        return self.vector_store.as_retriever(
            search_type="mmr", # MMR = Max Marginal Relevance. It reduces duplicate chunks and improves context diversity.
            search_kwargs={
                "k": k,
                "fetch_k": 30
            }
        )

    def retrieve(self, query: str, k: int = 6):

        logger.info(f"Retrieving documents for query: {query}")

        retriever = self.get_retriever(k)

        docs = retriever.invoke(query)

        logger.info(f"Retrieved {len(docs)} documents")

        return docs