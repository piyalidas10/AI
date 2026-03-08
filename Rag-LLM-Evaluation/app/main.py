import os
import shutil
import time
import uuid
import pandas as pd
import json
import plotly.express as px

from typing import List
from datetime import datetime

from fastapi import FastAPI, UploadFile, File, Form, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from langchain_ollama import OllamaLLM, OllamaEmbeddings
from langchain_community.vectorstores import Qdrant
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain

from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams

from pypdf import PdfReader
from docx import Document as DocxDocument

# RAG Evaluation
from ragas import evaluate
# from ragas.metrics import faithfulness, answer_relevancy, context_precision
from ragas.metrics import faithfulness, answer_relevancy, context_utilization
from datasets import Dataset

# Ragas internally tries to use OpenAI models via LangChain if you don't explicitly configure an LLM.
# This app uses Ollama (llama3), but RAGAS by default expects OpenAI API for evaluation.
# I must explicitly tell RAGAS to use your Ollama LLM instead of OpenAI.
from ragas.llms import LangchainLLMWrapper
from ragas.embeddings import LangchainEmbeddingsWrapper


# =====================================================
# CONFIG
# =====================================================

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://ollama:11434")
QDRANT_URL = os.getenv("QDRANT_URL", "http://qdrant:6333")

COLLECTION_NAME = "rag_collection"
UPLOAD_FOLDER = "uploaded_docs"
RAG_LOG_FILE = "rag_logs.jsonl"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# =====================================================
# RAG SAFETY THRESHOLDS
# =====================================================

FAITHFULNESS_THRESHOLD = 0.65
SIMILARITY_THRESHOLD = 0.35


# =====================================================
# FastAPI App
# =====================================================

app = FastAPI(title="Enterprise RAG API")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))


# =====================================================
# LLM & EMBEDDINGS
# =====================================================

llm = OllamaLLM(
    model="llama3",
    base_url=OLLAMA_BASE_URL,
    temperature=0,
)

embeddings = OllamaEmbeddings(
    model="nomic-embed-text",
    base_url=OLLAMA_BASE_URL
)

# Because nomic-embed-text embeddings are always 768 dimensions.
VECTOR_SIZE = 768

qdrant_client: QdrantClient = None
vector_store: Qdrant = None
retrieval_chain = None


# =====================================================
# COLLECTION ENSURE
# =====================================================

def ensure_collection_and_store():

    global vector_store

    collections = qdrant_client.get_collections().collections
    names = [c.name for c in collections]

    if COLLECTION_NAME not in names:

        print("📦 Creating rag_collection...")

        qdrant_client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(
                size=VECTOR_SIZE,
                distance=Distance.COSINE,
            ),
        )

        print("✅ rag_collection created")

    vector_store = Qdrant(
        client=qdrant_client,
        collection_name=COLLECTION_NAME,
        embeddings=embeddings,
    )


# =====================================================
# STARTUP
# =====================================================

@app.on_event("startup")
async def startup_event():

    global qdrant_client, retrieval_chain

    print("🔄 Connecting to Qdrant...")

    for i in range(10):

        try:
            qdrant_client = QdrantClient(url=QDRANT_URL)
            qdrant_client.get_collections()
            break

        except Exception:
            print(f"⏳ Retry {i+1}/10...")
            time.sleep(3)

    else:
        raise Exception("❌ Qdrant not reachable")

    ensure_collection_and_store()

    # retriever = vector_store.as_retriever(
    #    search_type="similarity",
    #    search_kwargs={"k": 4}
    #)

    # In LangChain, the method vector_store.as_retriever() converts a vector database (like Qdrant, Pinecone, FAISS, etc.) into a Retriever object used in RAG pipelines.
    retriever = vector_store.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": 4, # return top 4 results to the user
            "fetch_k": 12, # fetch more candidates for MMR to rerank and improve relevance/diversity
            "score_threshold":0.6 # only consider results with similarity score above 0.6 (tune this based on your data and embedding behavior)
        }
    )

    prompt = ChatPromptTemplate.from_template(
    """
    You are a company policy assistant.

    Answer the question using ONLY the provided context.

    If the answer exists in the context, extract it directly.

    Context:
    {context}

    Question:
    {input}

    Answer:
    """
    )

    document_chain = create_stuff_documents_chain(llm, prompt)

    retrieval_chain = create_retrieval_chain(
        retriever,
        document_chain
    )

    print("🚀 Startup complete")


# =====================================================
# TEXT EXTRACTION
# =====================================================

def extract_text(file_path: str, filename: str, category: str) -> List[Document]:

    documents = []
    uploaded_time = datetime.utcnow().isoformat()

    if filename.lower().endswith(".pdf"):

        reader = PdfReader(file_path)

        for page_no, page in enumerate(reader.pages, start=1):

            text = page.extract_text()

            if text:
                documents.append(
                    Document(
                        page_content=text,
                        metadata={
                            "file_name": filename,
                            "page": page_no,
                            "category": category,
                            "uploaded_at": uploaded_time,
                        },
                    )
                )

    elif filename.lower().endswith(".docx"):

        doc = DocxDocument(file_path)
        text = "\n".join(p.text for p in doc.paragraphs)

        documents.append(
            Document(
                page_content=text,
                metadata={
                    "file_name": filename,
                    "category": category,
                    "uploaded_at": uploaded_time,
                },
            )
        )

    elif filename.lower().endswith(".csv"):

        df = pd.read_csv(file_path)

        documents.append(
            Document(
                page_content=df.to_string(),
                metadata={
                    "file_name": filename,
                    "category": category,
                    "uploaded_at": uploaded_time,
                },
            )
        )

    else:
        raise HTTPException(status_code=400, detail="Unsupported file type")

    return documents


# =====================================================
# DOCUMENT SPLITTING
# =====================================================

def split_documents(documents: List[Document]) -> List[Document]:

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    return splitter.split_documents(documents)


# =====================================================
# RAG EVALUATION
# =====================================================

def evaluate_rag(question, answer, contexts, grounded):

    try:

        if not contexts:
            contexts = ["No context retrieved"]

        if not answer:
            answer = "No answer generated"

        # ----------------------------
        # Prepare dataset for RAGAS
        # ----------------------------
        dataset = Dataset.from_dict({
            "question": [question],
            "answer": [answer],
            "contexts": [contexts]
        })

        print("\nDEBUG DATASET:")
        print(dataset)

        # Wrap Ollama models for RAGAS
        # explicitly tell RAGAS to use your Ollama LLM instead of OpenAI because RAGAS by default expects OpenAI API for evaluation.
        ragas_llm = LangchainLLMWrapper(llm)
        ragas_embeddings = LangchainEmbeddingsWrapper(embeddings)

        # result = evaluate(dataset, metrics=[faithfulness, answer_relevancy, context_precision])
        result = evaluate(
            dataset,
            metrics=[
                faithfulness,
                answer_relevancy,
                context_utilization
            ],
            llm=ragas_llm,
            embeddings=ragas_embeddings,
            raise_exceptions=False
        )

        result_dict = dict(result)

    except Exception as e:

        print("⚠️ RAGAS evaluation crashed:", str(e))

        result_dict = {
            "faithfulness": 0.0,
            "answer_relevancy": 0.0,
            "context_utilization": 0.0
        }

    # Safely extract scores
    faithfulness_score = float(result_dict.get("faithfulness", 0.0) or 0.0)
    relevancy_score = float(result_dict.get("answer_relevancy", 0.0) or 0.0)
    context_util_score = float(result_dict.get("context_utilization", 0.0) or 0.0)

    # ---------------------------------------------
    # Save RAG logs
    
    # Every question will generate a log entry like:
    #    {
    #    "timestamp": "2026-03-07T15:22:01",
    #    "question": "What are company office hours?",
    #    "answer": "Office hours are 9AM to 6PM.",
    #    "contexts": [
    #        "Office hours are 9AM to 6PM Monday-Friday",
    #        "Employees must log in before 9AM"
    #        ]
    #    }
    # ----------------------------------------------
    log_data = {
        "timestamp": datetime.utcnow().isoformat(),
        "question": question,
        "answer": answer,
        "contexts": contexts,
        "faithfulness": faithfulness_score,
        "answer_relevancy": relevancy_score,
        "context_utilization": context_util_score,
        "grounded": grounded
    }

    try:
        with open(RAG_LOG_FILE, "a") as f:
            f.write(json.dumps(log_data) + "\n")
    except Exception as log_error:
        print("Log write failed:", log_error)

    return {
        "faithfulness": faithfulness_score,
        "answer_relevancy": relevancy_score,
        "context_utilization": context_util_score
    }


# =====================================================
# ROUTES
# =====================================================

@app.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    category: str = Form("general")
):

    try:

        ensure_collection_and_store()

        file_path = os.path.join(UPLOAD_FOLDER, file.filename)

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        documents = extract_text(file_path, file.filename, category)

        chunks = split_documents(documents)

        for chunk in chunks:
            chunk.metadata["doc_id"] = str(uuid.uuid4())

        vector_store.add_documents(chunks)

        return {
            "message": "File uploaded successfully",
            "chunks": len(chunks)
        }

    except Exception as e:

        print("❌ Upload Error:", str(e))

        raise HTTPException(status_code=500, detail=str(e))


# =====================================================
# ASK QUESTION
# =====================================================

@app.post("/ask-ui", response_class=HTMLResponse)
async def ask_ui(request: Request, question: str = Form(...)):

    try:

        docs_with_scores = vector_store.similarity_search_with_score(question, k=4)

        # (Lower score = better match in cosine distance)
        best_similarity = min([score for _, score in docs_with_scores])

        retrieval_debug = []
        heatmap_data = []

        print("\n🔎 Vector Similarity Scores:")
        for doc, score in docs_with_scores:
            retrieval_debug.append({
                "file": doc.metadata.get("file_name"),
                "page": doc.metadata.get("page"),
                "score": round(score, 3),
                "preview": doc.page_content[:300]
            })
            # This heatmap_data is used to visualize which documents/pages were most relevant to the question based on similarity scores.
            heatmap_data.append({
                "document": doc.metadata.get("file_name"),
                "page": doc.metadata.get("page"),
                "score": float(score)
            })
            print(score, doc.metadata.get("file_name"))

        response = retrieval_chain.invoke({"input": question})

        answer = response["answer"]

        # Context Captured for Evaluation
        # Without this RAG evaluation does not work.
        # response["context"] comes from LangChain retriever.

        # Example retrieved documents:
        # response["context"] = [
        #    Document(page_content="Office hours 9AM-6PM"),
        #    Document(page_content="Company works Monday-Friday"),
        #    Document(page_content="Employees must login before 9AM")
        #]

        contexts = [doc.page_content for doc in response["context"]]

        # contexts = [
        # "Office hours 9AM-6PM",
        # "Company works Monday-Friday",
        # "Employees must login before 9AM"
        # ]

        # Debug retrieved documents and their metadata to ensure they are correctly passed to RAGAS for evaluation.

        print("\n📄 Retrieved Documents:")
        for doc in response["context"]:
            print(doc.metadata)
            print("Preview:", doc.page_content[:150])

        evaluation = evaluate_rag(
            question,
            answer,
            contexts,
            True
        )

        faithfulness_score = evaluation.get("faithfulness", 0.0)
        
        grounded = True

        if faithfulness_score == 0:
            print("⚠️ RAGAS evaluation unavailable — skipping faithfulness check")
        else:
            if faithfulness_score < FAITHFULNESS_THRESHOLD:
                grounded = False

        if best_similarity < SIMILARITY_THRESHOLD:
            grounded = False

        if grounded:

            hallucination_warning = "✅ Answer grounded in retrieved documents"

        else:

            hallucination_warning = "⚠️ Low grounding confidence. Answer may be unreliable."

            answer = """
        I could not confidently answer this question using the available documents.

        Please try:
        • Rephrasing the question
        • Uploading more relevant documents
        • Asking about existing document content
        """        

        sources = [
            {
                "file_name": doc.metadata.get("file_name"),
                "page": doc.metadata.get("page"),
                "category": doc.metadata.get("category")
            }
            for doc in response["context"]
        ]

        return templates.TemplateResponse(
            "upload.html",
            {
                "request": request,
                "answer": answer,
                "evaluation": evaluation,
                "hallucination": hallucination_warning,
                "sources": sources,
                "retrieval_heatmap": heatmap_data,
                "retrieval_debug": retrieval_debug
            }
        )

    except Exception as e:

        return templates.TemplateResponse(
            "upload.html",
            {
                "request": request,
                "answer": f"Error: {str(e)}"
            }
        )


# =====================================================
# HOME
# =====================================================

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        "upload.html",
        {"request": request}
    )

# =====================================================
# RAG DASHBOARD

# This lets you track:
# Total queries
# Questions asked
# Answers generated
# Contexts used
# =====================================================

# =====================================================
# RAG DASHBOARD
# =====================================================

@app.get("/rag-dashboard", response_class=HTMLResponse)
async def rag_dashboard(request: Request):

    records = []

    if not os.path.exists(RAG_LOG_FILE):
        return templates.TemplateResponse(
            "dashboard.html",
            {
                "request": request,
                "faithfulness_chart": None,
                "relevancy_chart": None,
                "context_chart": None
            }
        )

    with open(RAG_LOG_FILE) as f:
        for line in f:
            try:
                records.append(json.loads(line))
            except:
                pass

    if len(records) == 0:
        return templates.TemplateResponse(
            "dashboard.html",
            {
                "request": request,
                "faithfulness_chart": None,
                "relevancy_chart": None,
                "context_chart": None
            }
        )

    df = pd.DataFrame(records)

    # If evaluation metrics exist in logs
    if "faithfulness" in df.columns:

        fig1 = px.line(
            df,
            x="timestamp",
            y="faithfulness",
            title="Faithfulness Over Time"
        )

        faithfulness_chart = fig1.to_html(full_html=False)

    else:
        faithfulness_chart = None

    if "answer_relevancy" in df.columns:

        fig2 = px.histogram(
            df,
            x="answer_relevancy",
            title="Answer Relevancy Distribution"
        )

        relevancy_chart = fig2.to_html(full_html=False)

    else:
        relevancy_chart = None

    if "context_utilization" in df.columns:

        fig3 = px.line(
            df,
            x="timestamp",
            y="context_utilization",
            title="Context Utilization Trend"
        )

        context_chart = fig3.to_html(full_html=False)

    else:
        context_chart = None

    total_queries = len(df)
    avg_faithfulness = round(df["faithfulness"].mean(),2)
    avg_relevancy = round(df["answer_relevancy"].mean(),2)

    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request,
            "faithfulness_chart": faithfulness_chart,
            "relevancy_chart": relevancy_chart,
            "context_chart": context_chart,
            "total_queries": total_queries,
            "avg_faithfulness": avg_faithfulness,
            "avg_relevancy": avg_relevancy
        }
    )

# =====================================================
# QUERY TRACES
# =====================================================

@app.get("/query-traces", response_class=HTMLResponse)
async def query_traces(request: Request):

    records = []

    if os.path.exists(RAG_LOG_FILE):
        with open(RAG_LOG_FILE) as f:
            for line in f:
                records.append(json.loads(line))

    records = records[-20:]  # latest 20

    return templates.TemplateResponse(
        "traces.html",
        {
            "request": request,
            "records": records
        }
    )


# =====================================================
# HEALTH
# =====================================================

@app.get("/health")
async def health():

    return {"status": "ok"}