from loguru import logger


class Retriever:

    def __init__(self, vector_store):

        self.vector_store = vector_store

    # =====================================================
    # Optimized Retriever for Local Ollama + Qdrant Setup
    # =====================================================

    def get_retriever(self, k: int = 2):

        logger.info(
            f"Creating retriever with k={k}"
        )

        return self.vector_store.as_retriever(
            search_type="mmr",
            search_kwargs={
                "k": k
            }
        )

    # =====================================================
    # Retrieve Relevant Documents
    # =====================================================

    def retrieve(self, query: str, k: int = 2):

        logger.info(
            f"Retrieving documents for query: {query}"
        )

        retriever = self.get_retriever(k)

        docs = retriever.invoke(query)

        logger.info(
            f"Retrieved {len(docs)} documents"
        )

        # Optional debug logging
        for index, doc in enumerate(docs):

            source = doc.metadata.get(
                "source",
                "unknown"
            )

            logger.info(
                f"Document {index + 1}: {source}"
            )

        return docs