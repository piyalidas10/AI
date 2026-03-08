# app/routes/chat.py

from fastapi import APIRouter, HTTPException, status, Depends
from app.models.request_models import ChatRequest
from app.models.response_models import ChatResponse
from app.services.embedding_service import EmbeddingService
from app.services.rag_service import RAGService
from app.security import get_current_user  # 👈 Added

router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
    dependencies=[Depends(get_current_user)]  # 👈 Protect entire router
)

# Initialize services (singleton-style)
embedding_service = EmbeddingService()
embedding_service.connect()

rag_service = RAGService(
    embedding_service.get_vector_store()
)


@router.post("/ask", response_model=ChatResponse)
async def ask_question(
    payload: ChatRequest,
    user: str = Depends(get_current_user)  # 👈 Optional: access user if needed
):
    """
    Ask question using RAG system with:
    - Metadata filtering (category)
    - Boundary control
    - Source tracking
    - Confidence scoring
    """

    try:
        # 🚀 Call RAG Service (now returns structured result)
        result = rag_service.ask(
            question=payload.question,
            category=payload.category, # ✅ 1. Category-aware search
            user_id=payload.user_id # ✅ 2. Multi-tenant ready. You can use this later in Qdrant filter.
        )

        return ChatResponse(
            success=True,
            message="Answer generated successfully",
            answer=result.get("answer"),
            category=payload.category,
            sources=result.get("sources"),
            confidence_score=result.get("confidence_score")
        )

    except ValueError as ve:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(ve)
        )

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Chat processing failed: {str(e)}"
        )