from loguru import logger

from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams

from langchain_community.vectorstores import Qdrant


class VectorStore:

    def __init__(self, embeddings):

        self.embeddings = embeddings

        self.collection_name = "github_code"

        # Docker internal hostname
        self.qdrant_url = "http://qdrant:6333"

        self.client = QdrantClient(
            host="qdrant",
            port=6333
        )

    # =====================================================
    # Create Collection If Not Exists
    # =====================================================

    def ensure_collection(self):

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

    # =====================================================
    # Create / Store Documents
    # =====================================================

    def create_vector_store(self, documents):

        logger.info(
            f"Storing {len(documents)} documents in Qdrant"
        )

        self.ensure_collection()

        vector_store = Qdrant.from_documents(
            documents=documents,
            embedding=self.embeddings,
            url=self.qdrant_url,
            collection_name=self.collection_name
        )

        logger.info("Documents stored successfully")

        return vector_store

    # =====================================================
    # Load Existing Collection
    # =====================================================

    def load_vector_store(self):

        logger.info(
            f"Loading collection: {self.collection_name}"
        )

        return Qdrant(
            client=self.client,
            collection_name=self.collection_name,
            embeddings=self.embeddings
        )