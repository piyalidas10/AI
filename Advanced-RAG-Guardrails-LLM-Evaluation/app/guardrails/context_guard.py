# =====================================================
# 👉 Prevents garbage retrieval → garbage answer
# =====================================================

from typing import List
from langchain_core.documents import Document

def validate_context(docs: List[Document]):

    if not docs:
        raise ValueError("❌ No relevant documents found")

    # Remove low-content chunks
    filtered = [d for d in docs if len(d.page_content.strip()) > 50]

    if len(filtered) == 0:
        raise ValueError("❌ Context too weak")

    return filtered