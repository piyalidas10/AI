from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from loguru import logger

from app.loaders.github_loader import GithubLoader
from app.rag.embedder import Embedder
from app.rag.vector_store import VectorStore
from app.rag.retriever import Retriever
from app.agents.reviewer_agent import CodeReviewerAgent


app = FastAPI(
    title="AI GitHub Code Review Agent",
    version="1.0.0"
)


# =========================
# Request Models
# =========================

class RepoRequest(BaseModel):
    repo_url: str


class ReviewRequest(BaseModel):
    question: str


# =========================
# Health Check
# =========================

@app.get("/")
def health_check():
    return {
        "status": "running",
        "service": "AI Code Review Agent"
    }


# =========================
# Index GitHub Repository
# =========================

@app.post("/index_repo")
def index_repo(request: RepoRequest):

    try:

        logger.info(f"Cloning repo: {request.repo_url}")

        # Load GitHub repository
        loader = GithubLoader(request.repo_url)

        loader.clone_repo()

        # Load source code files
        documents = loader.load_code_files()

        if not documents:
            raise HTTPException(
                status_code=400,
                detail="No supported code files found"
            )

        logger.info(f"Loaded {len(documents)} files")

        # Split documents into chunks
        chunks = loader.split_documents(documents)

        logger.info(f"Created {len(chunks)} chunks")

        # Create embeddings
        embedder = Embedder()

        embeddings = embedder.get_embeddings()

        # Store in Qdrant
        vector_store = VectorStore(embeddings)

        vector_store.create_vector_store(chunks)

        logger.info("Vector store created successfully")

        return {
            "message": "Repository indexed successfully",
            "files_loaded": len(documents),
            "chunks_created": len(chunks)
        }

    except Exception as e:

        logger.exception("Indexing failed")

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# =========================
# Review Code
# =========================

@app.post("/review")
def review_code(request: ReviewRequest):

    try:

        logger.info(f"Review question: {request.question}")

        # Embeddings
        embedder = Embedder()

        embeddings = embedder.get_embeddings()

        # Load vector store
        vector_store = VectorStore(embeddings).load_vector_store()

        # Retrieve relevant chunks
        retriever = Retriever(vector_store)

        docs = retriever.retrieve(request.question)

        if not docs:
            raise HTTPException(
                status_code=404,
                detail="No relevant code found"
            )

        logger.info(f"Retrieved {len(docs)} relevant chunks")

        # AI Reviewer Agent
        agent = CodeReviewerAgent()

        review = agent.review_code(
            request.question,
            docs
        )

        return {
            "question": request.question,
            "review": review,
            "chunks_used": len(docs)
        }

    except Exception as e:

        logger.exception("Review failed")

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )