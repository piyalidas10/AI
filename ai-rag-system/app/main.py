# app/main.py

from fastapi import FastAPI, Request, status, Response
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from app.core.metrics import REQUEST_COUNT, REQUEST_LATENCY
from contextlib import asynccontextmanager
import time

from app.routes import upload, chat, monitoring
from app.services.embedding_service import EmbeddingService


# =====================================================
# Application Lifespan (Startup / Shutdown)
# =====================================================

embedding_service = EmbeddingService()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Initialize resources on startup.
    """
    print("🚀 Starting Enterprise RAG API...")
    embedding_service.connect()  # Connect Qdrant on startup
    print("✅ Application startup complete")
    yield
    print("🛑 Shutting down application...")


# =====================================================
# FastAPI App Initialization
# =====================================================

app = FastAPI(
    title="Enterprise RAG API",
    description="Production-grade RAG system using FastAPI + Ollama + Qdrant",
    version="1.0.0",
    lifespan=lifespan
)


# =====================================================
# CORS Configuration (Frontend Ready)
# =====================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# =====================================================
# Templates
# =====================================================

templates = Jinja2Templates(directory="app/templates")


# =====================================================
# Include Routers
# =====================================================

app.include_router(upload.router)
app.include_router(chat.router)
app.include_router(monitoring.router)


# =====================================================
# UI Route
# =====================================================

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "upload.html",
        {"request": request}
    )


# =====================================================
# Basic Liveness Check
# =====================================================

@app.get("/health", tags=["System"])
async def health():
    return {
        "status": "ok",
        "service": "Enterprise RAG API",
        "timestamp": time.time()
    }


# =====================================================
# Readiness Check (Qdrant + Dependencies)
# =====================================================

@app.get("/ready", tags=["System"])
async def readiness():
    """
    Readiness probe for Kubernetes / Docker.
    """
    try:
        result = embedding_service.health_check()
        if result["status"] != "healthy":
            return JSONResponse(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                content={"status": "not_ready", "details": result}
            )

        return {"status": "ready"}

    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            content={"status": "not_ready", "error": str(e)}
        )


# =====================================================
# Global Exception Handler
# =====================================================

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "message": "Internal server error",
            "detail": str(exc)
        },
    )