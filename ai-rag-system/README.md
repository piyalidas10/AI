

✅ Browser
    -   → /documents/upload → Qdrant
    -   → /chat/ask → RAG → phi3 → Answer   

✅ FOLDER STRUCTURE
```
ai-rag-system/
│
├── app/
│   ├── main.py
│
│   ├── routes/
│   │     ├── chat.py
│   │     ├── upload.py
│
│   ├── services/
│   │     ├── rag_service.py
│   │     ├── embedding_service.py
│
│   ├── core/
│   │     ├── config.py
│   │     ├── security.py
│
│   ├── models/
│   │     ├── request_models.py
│   │     ├── response_models.py
│
│   └── __init__.py
│
├── data/
│   └── uploads/
│
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .env
├── .dockerignore
├── .gitignore
└── README.md
```

**2️⃣ services/embedding_service.py**

Handles:
    -   Qdrant connection
    -   Collection creation
    -   Embeddings
    -   Vector store

**3️⃣ services/rag_service.py**

Handles:
    -   LLM
    -   Retrieval chain
    -   Ask logic

