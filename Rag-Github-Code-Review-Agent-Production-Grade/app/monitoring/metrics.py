from prometheus_client import Counter
from prometheus_client import Histogram
from prometheus_client import Gauge


TOTAL_QUERIES = Counter(
    "rag_total_queries",
    "Total RAG Queries"
)

FAILED_QUERIES = Counter(
    "rag_failed_queries",
    "Failed RAG Queries"
)

QUERY_LATENCY = Histogram(
    "rag_query_latency_seconds",
    "RAG Query Latency"
)

ACTIVE_REQUESTS = Gauge(
    "rag_active_requests",
    "Active Requests"
)

RETRIEVED_DOCS = Histogram(
    "rag_retrieved_docs",
    "Retrieved Documents Count"
)