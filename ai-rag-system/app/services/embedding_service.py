import time
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import Qdrant

from app.core.config import (
    OLLAMA_BASE_URL,
    QDRANT_URL,
    COLLECTION_NAME,
    VECTOR_SIZE,
)

class EmbeddingService:

    def __init__(self):
        self.qdrant_client = None
        self.vector_store = None
        self.embeddings = OllamaEmbeddings(
            model="nomic-embed-text",
            base_url=OLLAMA_BASE_URL
        )

    def connect(self):
        for _ in range(10):
            try:
                self.qdrant_client = QdrantClient(url=QDRANT_URL)
                self.qdrant_client.get_collections()
                break
            except Exception:
                time.sleep(3)
        else:
            raise Exception("Qdrant not reachable")

        self.ensure_collection()

    def ensure_collection(self):
        collections = self.qdrant_client.get_collections().collections
        names = [c.name for c in collections]

        if COLLECTION_NAME not in names:
            self.qdrant_client.create_collection(
                collection_name=COLLECTION_NAME,
                vectors_config=VectorParams(
                    size=VECTOR_SIZE,
                    distance=Distance.COSINE,
                ),
            )

        self.vector_store = Qdrant(
            client=self.qdrant_client,
            collection_name=COLLECTION_NAME,
            embeddings=self.embeddings,
        )

    def get_vector_store(self):
        return self.vector_store