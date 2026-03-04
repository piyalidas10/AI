from pydantic import BaseModel, Field
from typing import Optional


# ============================
# Chat / Ask Request
# ============================

class ChatRequest(BaseModel):
    question: str = Field(
        ...,
        min_length=3,
        example="What is Prompt Engineering?"
    )

    category: Optional[str] = Field(
        default="general",
        example="finance"
    )


# ============================
# Upload Metadata Request
# (Used if you convert to JSON upload API later)
# ============================

class UploadMetadata(BaseModel):
    category: Optional[str] = Field(
        default="general",
        example="legal"
    )