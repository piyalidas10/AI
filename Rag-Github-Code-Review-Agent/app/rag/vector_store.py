from langchain_community.vectorstores import Qdrant
from qdrant_client import QdrantClient


class VectorStore:

    def __init__(self, embeddings):

        self.client = QdrantClient(
            host="localhost",
            port=6333
        )

        self.embeddings = embeddings
        self.collection_name = "github_code"

    def create_vector_store(self, documents):

        vector_store = Qdrant.from_documents(
            documents,
            self.embeddings,
            url="http://localhost:6333",
            collection_name=self.collection_name
        )

        return vector_store

    def load_vector_store(self):

        return Qdrant(
            client=self.client,
            collection_name=self.collection_name,
            embeddings=self.embeddings
        )