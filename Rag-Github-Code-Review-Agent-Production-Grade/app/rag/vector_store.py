# app/rag/vector_store.py

from uuid import uuid4

from loguru import logger

from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    VectorParams
)

from langchain_qdrant import QdrantVectorStore


class VectorStore:

    def __init__(
        self,
        embeddings,
        collection_name: str = "github_code"
    ):

        self.embeddings = embeddings

        self.collection_name = collection_name

        # =====================================
        # Qdrant Docker Service
        # =====================================

        self.qdrant_host = "qdrant"
        self.qdrant_port = 6333

        # =====================================
        # Qdrant Client
        # =====================================

        self.client = QdrantClient(
            host=self.qdrant_host,
            port=self.qdrant_port
        )

        # =====================================
        # Detect Embedding Dimension Dynamically
        # =====================================

        sample_embedding = (
            self.embeddings.embed_query("dimension_check")
        )

        self.embedding_size = len(sample_embedding)

        logger.info(
            f"Embedding dimension detected: "
            f"{self.embedding_size}"
        )

    # =====================================================
    # Create Collection If Not Exists
    # =====================================================

    def ensure_collection(self):

        logger.info(
            f"Checking collection: "
            f"{self.collection_name}"
        )

        collections = (
            self.client.get_collections().collections
        )

        collection_names = [
            collection.name
            for collection in collections
        ]

        # =====================================
        # Create Collection
        # =====================================

        if self.collection_name not in collection_names:

            logger.info(
                f"Creating collection: "
                f"{self.collection_name}"
            )

            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config=VectorParams(
                    size=self.embedding_size,
                    distance=Distance.COSINE
                )
            )

            logger.info(
                f"Collection created: "
                f"{self.collection_name}"
            )

        else:

            logger.info(
                f"Collection already exists: "
                f"{self.collection_name}"
            )

    # =====================================================
    # Load Vector Store
    # =====================================================

    def load_vector_store(self):

        self.ensure_collection()

        logger.info(
            f"Loading vector store: "
            f"{self.collection_name}"
        )

        vector_store = QdrantVectorStore(
            client=self.client,
            collection_name=self.collection_name,
            embedding=self.embeddings
        )

        logger.info(
            "Vector store loaded successfully"
        )

        return vector_store

    # =====================================================
    # Store Documents
    # =====================================================

    def add_documents(
        self,
        documents,
        repo_name: str = "default_repo"
    ):

        logger.info(
            f"Adding {len(documents)} documents "
            f"to collection"
        )

        self.ensure_collection()

        vector_store = self.load_vector_store()

        # =====================================
        # Add Repository Metadata
        # =====================================

        for doc in documents:

            doc.metadata["repository"] = repo_name

        # =====================================
        # Generate Stable IDs
        # =====================================

        ids = []

        for doc in documents:

            source = doc.metadata.get(
                "source",
                ""
            )

            content_hash = hash(
                doc.page_content + source
            )

            ids.append(str(content_hash))

        # =====================================
        # Insert Documents
        # =====================================

        vector_store.add_documents(
            documents=documents,
            ids=ids
        )

        logger.info(
            "Documents added successfully"
        )

        return vector_store

    # =====================================================
    # Similarity Search
    # =====================================================

    def similarity_search(
        self,
        query,
        k=5,
        repository=None,
        language=None
    ):

        vector_store = self.load_vector_store()

        # =====================================
        # Metadata Filters
        # =====================================

        filter_conditions = []

        if repository:

            filter_conditions.append({
                "key": "repository",
                "match": {
                    "value": repository
                }
            })

        if language:

            filter_conditions.append({
                "key": "language",
                "match": {
                    "value": language
                }
            })

        search_kwargs = {
            "k": k
        }

        if filter_conditions:

            search_kwargs["filter"] = {
                "must": filter_conditions
            }

        logger.info(
            f"Running similarity search "
            f"for query: {query}"
        )

        results = (
            vector_store.similarity_search(
                query=query,
                **search_kwargs
            )
        )

        logger.info(
            f"Retrieved {len(results)} documents"
        )

        return results

    # =====================================================
    # Delete Collection
    # =====================================================

    def delete_collection(self):

        logger.warning(
            f"Deleting collection: "
            f"{self.collection_name}"
        )

        self.client.delete_collection(
            collection_name=self.collection_name
        )

        logger.info(
            "Collection deleted successfully"
        )

    # =====================================================
    # Collection Information
    # =====================================================

    def get_collection_info(self):

        info = self.client.get_collection(
            collection_name=self.collection_name
        )

        logger.info(
            f"Collection info: {info}"
        )

        return info

    # =====================================================
    # Count Documents
    # =====================================================

    def count_documents(self):

        info = self.client.get_collection(
            collection_name=self.collection_name
        )

        count = info.points_count

        logger.info(
            f"Total documents in collection: "
            f"{count}"
        )

        return count