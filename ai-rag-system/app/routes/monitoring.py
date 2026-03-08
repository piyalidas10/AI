from fastapi import APIRouter
from app.services.embedding_service import EmbeddingService

router = APIRouter(prefix="/monitor", tags=["Monitoring"])

embedding_service = EmbeddingService()
embedding_service.connect()


@router.get("/health")
def qdrant_health():
    """
    Check Qdrant health.
    """
    return embedding_service.health_check()


@router.get("/metrics")
def qdrant_metrics():
    """
    Get Qdrant collection metrics.
    """
    return embedding_service.get_collection_metrics()