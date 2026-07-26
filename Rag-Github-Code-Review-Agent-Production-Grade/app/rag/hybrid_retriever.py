# vector + BM25 retrieval
from rank_bm25 import BM25Okapi

from langchain.schema import Document


class HybridRetriever:

    def __init__(
        self,
        vector_store,
        documents
    ):

        self.vector_store = vector_store
        self.documents = documents

        # BM25 Corpus
        self.corpus = [
            doc.page_content.split()
            for doc in documents
        ]

        self.bm25 = BM25Okapi(self.corpus)

    # ==========================================
    # Hybrid Retrieval
    # ==========================================

    def retrieve(
        self,
        query,
        vector_k=10,
        bm25_k=10
    ):

        # ======================================
        # Vector Search
        # ======================================

        vector_results = (
            self.vector_store.similarity_search(
                query,
                k=vector_k
            )
        )

        # ======================================
        # BM25 Search
        # ======================================

        tokenized_query = query.split()

        bm25_scores = self.bm25.get_scores(
            tokenized_query
        )

        ranked_indices = sorted(
            range(len(bm25_scores)),
            key=lambda i: bm25_scores[i],
            reverse=True
        )[:bm25_k]

        bm25_results = [
            self.documents[i]
            for i in ranked_indices
        ]

        # ======================================
        # Merge Results
        # ======================================

        merged = []

        seen = set()

        for doc in vector_results + bm25_results:

            content_hash = hash(doc.page_content)

            if content_hash not in seen:

                merged.append(doc)

                seen.add(content_hash)

        return merged