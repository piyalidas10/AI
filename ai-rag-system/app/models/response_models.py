from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


# ============================
# Base API Response
# ============================

class BaseResponse(BaseModel):
    success: bool = Field(
        ...,
        description="Indicates if the request was successful"
    )

    message: str = Field(
        ...,
        description="Human-readable status message"
    )

    timestamp: datetime = Field(
        default_factory=datetime.utcnow,
        description="Response generation timestamp (UTC)"
    )


# ============================
# Chat / Ask Response
# ============================

class ChatResponse(BaseResponse):
    answer: Optional[str] = Field(
        default=None,
        description="LLM generated answer"
    )

    category: Optional[str] = Field(
        default=None,
        description="Category used for metadata filtering"
    )

    sources: Optional[List[str]] = Field(
        default=None,
        description="List of document sources used to generate answer"
    )

    confidence_score: Optional[float] = Field(
        default=None,
        description="Average similarity score from retrieved chunks"
    )


# ============================
# Upload Response
# ============================

class UploadResponse(BaseResponse):
    filename: Optional[str] = Field(
        default=None,
        description="Uploaded file name"
    )

    category: Optional[str] = Field(
        default=None,
        description="Category assigned to document"
    )

    chunks_stored: Optional[int] = Field(
        default=None,
        description="Number of vector chunks stored in Qdrant"
    )