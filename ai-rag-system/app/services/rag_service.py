from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain

from app.core.config import OLLAMA_BASE_URL

class RAGService:

    def __init__(self, vector_store):
        self.llm = OllamaLLM(
            model="phi3",
            base_url=OLLAMA_BASE_URL
        )

        retriever = vector_store.as_retriever(search_kwargs={"k": 4})

        prompt = ChatPromptTemplate.from_template(
            """Use the context to answer strictly from provided documents.

Context:
{context}

Question:
{input}

Answer:"""
        )

        document_chain = create_stuff_documents_chain(self.llm, prompt)
        self.retrieval_chain = create_retrieval_chain(retriever, document_chain)

    def ask(self, question: str):
        response = self.retrieval_chain.invoke({"input": question})
        return response["answer"]