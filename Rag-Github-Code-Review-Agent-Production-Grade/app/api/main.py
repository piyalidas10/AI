import time

from fastapi import FastAPI
from fastapi import HTTPException
from prometheus_client import generate_latest
from prometheus_client import CONTENT_TYPE_LATEST
from fastapi.responses import Response

from app.guardrails.input_guard import InputGuard
from app.guardrails.output_guard import OutputGuard
from app.monitoring.metrics import (
    TOTAL_QUERIES,
    FAILED_QUERIES,
    QUERY_LATENCY,
    ACTIVE_REQUESTS,
    RETRIEVED_DOCS
)
from app.monitoring.tracing import RAGTracer


app = FastAPI()


@app.get("/metrics")
def metrics():

    return Response(
        generate_latest(),
        media_type=CONTENT_TYPE_LATEST
    )


@app.post("/review")
def review(payload: dict):

    ACTIVE_REQUESTS.inc()

    start_time = time.time()

    TOTAL_QUERIES.inc()

    try:

        query = payload["question"]

        # =====================================
        # Guardrails
        # =====================================

        validation = InputGuard.validate_input(query)

        if not validation["allowed"]:

            FAILED_QUERIES.inc()

            raise HTTPException(
                status_code=400,
                detail=validation["reason"]
            )

        # =====================================
        # Retrieve Documents
        # =====================================

        docs = retriever.retrieve(query)

        RETRIEVED_DOCS.observe(len(docs))

        # =====================================
        # Generate Review
        # =====================================

        response = reviewer.review_code(
            query,
            docs
        )

        # =====================================
        # Output Guard
        # =====================================

        cleaned_response = OutputGuard.validate_output(
            response
        )

        # =====================================
        # Tracing
        # =====================================

        RAGTracer.trace({
            "query": query,
            "retrieved_docs": len(docs),
            "response_length": len(cleaned_response)
        })

        return {
            "answer": cleaned_response
        }

    except Exception as e:

        FAILED_QUERIES.inc()

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

    finally:

        # =====================================
        # Request Duration
        # =====================================

        latency = time.time() - start_time

        QUERY_LATENCY.observe(latency)

        # =====================================
        # Active Requests Cleanup
        # =====================================

        ACTIVE_REQUESTS.dec()