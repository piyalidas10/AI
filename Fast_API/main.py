from fastapi import FastAPI, Request, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel
from typing import Optional, Any
from datetime import datetime

app = FastAPI(title="Enterprise API Example")


# ===============================
# Response Models
# ===============================

class SuccessResponse(BaseModel):
    success: bool = True
    data: Any
    timestamp: datetime


class ErrorDetail(BaseModel):
    code: str
    message: str
    details: Optional[Any] = None


class ErrorResponse(BaseModel):
    success: bool = False
    error: ErrorDetail
    timestamp: datetime
    path: str


# ===============================
# Request Model
# ===============================

class PostRequest(BaseModel):
    title: str
    body: str
    userId: int


# ===============================
# Custom Business Exception
# ===============================

class BusinessException(Exception):
    def __init__(self, code: str, message: str, status_code: int = 400):
        self.code = code
        self.message = message
        self.status_code = status_code


# ===============================
# Global Exception Handlers
# ===============================

@app.exception_handler(BusinessException)
async def business_exception_handler(request: Request, exc: BusinessException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "error": {
                "code": exc.code,
                "message": exc.message,
                "details": None,
            },
            "timestamp": datetime.utcnow().isoformat(),
            "path": request.url.path,
        },
    )


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "error": {
                "code": "HTTP_ERROR",
                "message": exc.detail,
                "details": None,
            },
            "timestamp": datetime.utcnow().isoformat(),
            "path": request.url.path,
        },
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "success": False,
            "error": {
                "code": "VALIDATION_ERROR",
                "message": "Invalid request payload",
                "details": exc.errors(),
            },
            "timestamp": datetime.utcnow().isoformat(),
            "path": request.url.path,
        },
    )


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "error": {
                "code": "INTERNAL_SERVER_ERROR",
                "message": "Something went wrong",
                "details": str(exc),
            },
            "timestamp": datetime.utcnow().isoformat(),
            "path": request.url.path,
        },
    )


# ===============================
# Routes
# ===============================

@app.get("/")
def health_check():
    return {
        "success": True,
        "message": "API is running",
        "timestamp": datetime.utcnow().isoformat()
    }


@app.post(
    "/posts",
    status_code=status.HTTP_201_CREATED,
    responses={
        400: {"model": ErrorResponse},
        422: {"model": ErrorResponse},
        500: {"model": ErrorResponse},
    },
)
def create_post(request: PostRequest):

    # Business validation example
    if request.userId <= 0:
        raise BusinessException(
            code="INVALID_USER_ID",
            message="User ID must be greater than 0",
            status_code=400
        )

    # Simulate success response
    return {
        "success": True,
        "data": {
            "title": request.title,
            "body": request.body,
            "userId": request.userId,
            "id": 101
        },
        "timestamp": datetime.utcnow().isoformat()
    }


