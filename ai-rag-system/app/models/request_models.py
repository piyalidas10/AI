from pydantic import BaseModel, Field, field_validator
from typing import Optional
from datetime import datetime


# ============================
# Chat / Ask Request
# ============================

class ChatRequest(BaseModel):
    question: str = Field(
        ...,
        min_length=3,
        max_length=2000,
        example="What is Prompt Engineering?"
    )

    category: str = Field(
        default="general",
        min_length=2,
        max_length=50,
        example="finance",
        description="Document category used for metadata filtering"
    )

    user_id: Optional[str] = Field(
        default=None,
        example="user_123",
        description="Optional user identifier for multi-tenant filtering"
    )

    @field_validator("question")
    @classmethod
    def validate_question(cls, value: str):
        if not value.strip():
            raise ValueError("Question cannot be empty.")
        return value.strip()

    @field_validator("category")
    @classmethod
    def normalize_category(cls, value: str):
        if not value.strip():
            raise ValueError("Category cannot be empty.")
        return value.strip().lower()


# ============================
# Upload Metadata Request
# (For future JSON-based upload APIs)
# ============================

class UploadMetadata(BaseModel):
    category: str = Field(
        default="general",
        min_length=2,
        max_length=50,
        example="legal",
        description="Category used for semantic boundary filtering"
    )

    uploaded_by: Optional[str] = Field(
        default="admin",
        example="admin",
        description="User who uploaded the document"
    )

    tags: Optional[list[str]] = Field(
        default=None,
        example=["contract", "nda", "compliance"],
        description="Optional list of searchable tags"
    )

    timestamp: Optional[datetime] = Field(
        default_factory=datetime.utcnow,
        description="Auto-generated upload timestamp"
    )

    @field_validator("category")
    @classmethod
    def normalize_category(cls, value: str):
        return value.strip().lower()