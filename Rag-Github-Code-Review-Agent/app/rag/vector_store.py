from loguru import logger

from qdrant_client import QdrantClient
from qdrant_client.http.models import (
    Distance,
    VectorParams
)

from langchain_qdrant import QdrantVectorStore


class VectorStore:

    def __init__(self, embeddings):

        self.embeddings = embeddings

        self.collection_name = "github_code"

        # Qdrant Docker service
        self.qdrant_host = "qdrant"
        self.qdrant_port = 6333

        # Qdrant Client
        self.client = QdrantClient(
            host=self.qdrant_host,
            port=self.qdrant_port
        )

    # =====================================================
    # Create Collection If Not Exists
    # =====================================================

    def ensure_collection(self):

        logger.info("Checking Qdrant collections")

        collections = self.client.get_collections().collections

        collection_names = [
            collection.name
            for collection in collections
        ]

        if self.collection_name not in collection_names:

            logger.info(
                f"Creating collection: {self.collection_name}"
            )

            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config=VectorParams(
                    size=768,
                    distance=Distance.COSINE
                )
            )

            logger.info(
                f"Collection created: {self.collection_name}"
            )

        else:

            logger.info(
                f"Collection already exists: {self.collection_name}"
            )

    # =====================================================
    # Store Documents In Qdrant
    # =====================================================

    def create_vector_store(self, documents):

        logger.info(
            f"Storing {len(documents)} documents in Qdrant"
        )

        # Ensure collection exists
        self.ensure_collection()

        # Create vector store
        vector_store = QdrantVectorStore.from_documents(
            documents=documents,
            embedding=self.embeddings,
            url=f"http://{self.qdrant_host}:{self.qdrant_port}",
            collection_name=self.collection_name
        )

        logger.info(
            "Documents stored successfully in Qdrant"
        )

        return vector_store

    # =====================================================
    # Load Existing Vector Store
    # =====================================================

    def load_vector_store(self):

        logger.info(
            f"Loading collection: {self.collection_name}"
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
    # Delete Collection
    # =====================================================

    def delete_collection(self):

        logger.warning(
            f"Deleting collection: {self.collection_name}"
        )

        self.client.delete_collection(
            collection_name=self.collection_name
        )

        logger.info("Collection deleted")

    # =====================================================
    # Get Collection Info
    # =====================================================

    def get_collection_info(self):

        info = self.client.get_collection(
            collection_name=self.collection_name
        )

        logger.info(
            f"Collection info: {info}"
        )

        return info