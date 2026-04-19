from fastapi import FastAPI
from pydantic import BaseModel

from app.loaders.github_loader import GithubLoader
from app.rag.embedder import Embedder
from app.rag.vector_store import VectorStore
from app.rag.retriever import Retriever
from app.agents.reviewer_agent import CodeReviewerAgent


app = FastAPI()

class RepoRequest(BaseModel):
    repo_url: str


class ReviewRequest(BaseModel):
    question: str


vector_store_instance = None


@app.post("/index_repo")
def index_repo(request: RepoRequest):

    loader = GithubLoader(request.repo_url)

    loader.clone_repo()

    documents = loader.load_code_files()

    chunks = loader.split_documents(documents)

    embedder = Embedder()

    embeddings = embedder.get_embeddings()

    vector_store = VectorStore(embeddings)

    vector_store_instance = vector_store.create_vector_store(chunks)

    return {"message": "Repository indexed successfully"}


@app.post("/review")
def review_code(request: ReviewRequest):

    embedder = Embedder()

    embeddings = embedder.get_embeddings()

    vector_store = VectorStore(embeddings).load_vector_store()

    retriever = Retriever(vector_store)

    docs = retriever.retrieve(request.question)

    agent = CodeReviewerAgent()

    review = agent.review_code(request.question, docs)

    return {"review": review}