import json
import uuid
from datetime import datetime

from loguru import logger


TRACE_FILE = "app/logs/rag_traces.jsonl"


class RAGTracer:

    @staticmethod
    def create_trace(
        query,
        retrieved_docs,
        response,
        latency_ms
    ):

        trace = {
            "trace_id": str(uuid.uuid4()),
            "timestamp": datetime.utcnow().isoformat(),
            "query": query,
            "retrieved_documents": [
                {
                    "source": doc.metadata.get("source"),
                    "language": doc.metadata.get("language"),
                    "chunk_type": doc.metadata.get("type")
                }
                for doc in retrieved_docs
            ],
            "retrieved_count": len(retrieved_docs),
            "response_preview": response[:500],
            "latency_ms": latency_ms
        }

        with open(TRACE_FILE, "a") as f:
            f.write(json.dumps(trace) + "\n")

        logger.info(
            f"RAG trace stored: {trace['trace_id']}"
        )