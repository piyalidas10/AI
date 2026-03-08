# app/services/embedding_service.py

import time
from typing import Optional

from qdrant_client import QdrantClient
from qdrant_client.http.models import (
    Distance,
    VectorParams,
    OptimizersConfigDiff,
    PayloadSchemaType
)

from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import Qdrant

from app.core.config import (
    OLLAMA_BASE_URL,
    QDRANT_URL,
    COLLECTION_NAME,
    VECTOR_SIZE,
)


class EmbeddingService:
    """
    Embedding Service Layer
    ------------------------
    Responsible for:
    - Connecting to Qdrant
    - Ensuring collection exists
    - Creating payload indexes
    - Providing vector store instance

    ✅ Clean separation of responsibilities
    """

    def __init__(self):
        self.qdrant_client: Optional[QdrantClient] = None
        self.vector_store: Optional[Qdrant] = None

        # Embedding model configuration
        self.embeddings = OllamaEmbeddings(
            model="nomic-embed-text",
            base_url=OLLAMA_BASE_URL
        )

    # ====================================================
    # Connect to Qdrant (with retry logic)
    # ====================================================
    def connect(self):

        # ✅ Proper retry with logging clarity
        for attempt in range(10):
            try:
                self.qdrant_client = QdrantClient(url=QDRANT_URL)
                self.qdrant_client.get_collections()
                print("✅ Connected to Qdrant")
                break
            except Exception:
                print(f"⏳ Waiting for Qdrant... Attempt {attempt + 1}")
                time.sleep(3)
        else:
            raise Exception("❌ Qdrant not reachable after multiple attempts")

        self.ensure_collection()

    # ====================================================
    # Ensure Collection Exists
    # ====================================================
    def ensure_collection(self):

        collections = self.qdrant_client.get_collections().collections
        collection_names = [c.name for c in collections]

        if COLLECTION_NAME not in collection_names:

            print(f"🚀 Creating collection: {COLLECTION_NAME}")

            # ✅ Collection creation with payload indexing support
            self.qdrant_client.create_collection(
                collection_name=COLLECTION_NAME,
                vectors_config=VectorParams(
                    size=VECTOR_SIZE,  # ✅ Vector size auto-validation
                    distance=Distance.COSINE,
                ),
                optimizers_config=OptimizersConfigDiff(
                    indexing_threshold=20000
                ), # Better performance for larger datasets.
            )

            # Create metadata indexes
            self._create_payload_indexes()

        else:
            print(f"ℹ️ Collection '{COLLECTION_NAME}' already exists")

        # Initialize LangChain VectorStore wrapper
        self.vector_store = Qdrant(
            client=self.qdrant_client,
            collection_name=COLLECTION_NAME,
            embeddings=self.embeddings,
        )

    # ====================================================
    # Create Payload Indexes for Metadata Filtering
    # ====================================================
    def _create_payload_indexes(self):

        print("🔎 Creating payload indexes...")

        # ✅ Multi-tenant ready payload index (category filter)
        # Category index allows us to filter documents by category during retrieval, improving relevance.
        self.qdrant_client.create_payload_index(
            collection_name=COLLECTION_NAME,
            field_name="category",
            field_schema=PayloadSchemaType.KEYWORD,
        )

        # ✅ Multi-tenant ready payload index (uploaded_by filter)
        # Uploaded_by index allows us to track who uploaded the document, 
        # enabling user-specific filtering and access control in the future.
        self.qdrant_client.create_payload_index(
            collection_name=COLLECTION_NAME,
            field_name="uploaded_by",
            field_schema=PayloadSchemaType.KEYWORD,
        )

        # ✅ Multi-tenant ready payload index (user isolation)
        # User_id index (future multi-tenant support) allows us to isolate documents by user, 
        # enabling true multi-tenancy where each user's data is separated and secure.
        self.qdrant_client.create_payload_index(
            collection_name=COLLECTION_NAME,
            field_name="user_id",
            field_schema=PayloadSchemaType.KEYWORD,
        )

        # ✅ Metadata source tracking
        # Source file index allows us to track the origin of each document chunk, 
        # enabling source attribution in responses and better traceability.
        self.qdrant_client.create_payload_index(
            collection_name=COLLECTION_NAME,
            field_name="source",
            field_schema=PayloadSchemaType.KEYWORD,
        )

        print("✅ Payload indexes created successfully")

    # ====================================================
    # Get Vector Store
    # ====================================================
    def get_vector_store(self) -> Qdrant:

        # ✅ Better structure for production (safe guard). Prevents silent runtime failure.
        if not self.vector_store:
            raise Exception("Vector store not initialized. Call connect() first.")

        return self.vector_store