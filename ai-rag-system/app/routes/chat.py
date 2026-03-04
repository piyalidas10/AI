from fastapi import APIRouter, HTTPException
from app.models.request_models import ChatRequest
from app.models.response_models import ChatResponse
from app.services.embedding_service import EmbeddingService
from app.services.rag_service import RAGService

router = APIRouter(prefix="/chat", tags=["Chat"])

# Initialize services (singleton-style for simplicity)
embedding_service = EmbeddingService()
embedding_service.connect()

rag_service = RAGService(
    embedding_service.get_vector_store()
)


@router.post("/ask", response_model=ChatResponse)
async def ask_question(payload: ChatRequest):
    """
    Ask question using RAG system.
    """

    try:
        answer = rag_service.ask(payload.question)

        return ChatResponse(
            success=True,
            message="Answer generated successfully",
            answer=answer
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Chat error: {str(e)}"
        )