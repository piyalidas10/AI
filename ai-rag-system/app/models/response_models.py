from pydantic import BaseModel
from typing import Optional, List, Any


# ============================
# Standard API Response
# ============================

class BaseResponse(BaseModel):
    success: bool
    message: str


# ============================
# Upload Response
# ============================

class UploadResponse(BaseResponse):
    chunks: Optional[int] = None
    file_name: Optional[str] = None


# ============================
# Chat Response
# ============================

class ChatResponse(BaseResponse):
    answer: Optional[str] = None
    sources: Optional[List[Any]] = None


# ============================
# Health Response
# ============================

class HealthResponse(BaseModel):
    status: str