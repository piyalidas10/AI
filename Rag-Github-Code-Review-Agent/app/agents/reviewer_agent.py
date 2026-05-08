from loguru import logger

from langchain_ollama import ChatOllama
from langchain.prompts import ChatPromptTemplate


class CodeReviewerAgent:

    def __init__(self):

        logger.info("Initializing Code Reviewer Agent")

        # Ollama model
        self.llm = ChatOllama(
            model="phi3",
            temperature=0,
            base_url="http://ollama:11434"
        )

        # Prompt Template
        self.prompt = ChatPromptTemplate.from_template(
            """
            You are a senior software engineer performing a professional code review.

            STRICT RULES:
            - Use ONLY the provided context
            - Do NOT hallucinate
            - If context is insufficient, say so
            - Focus on practical engineering issues
            - Be concise but technically accurate

            Review for:
            1. Bugs
            2. Security vulnerabilities
            3. Performance issues
            4. Readability problems
            5. Best practices
            6. Maintainability

            For each issue provide:

            File:
            Language:
            Issue Type:
            Severity:
            Explanation:
            Suggested Fix:

            ========================
            CONTEXT
            ========================

            {context}

            ========================
            QUESTION
            ========================

            {question}

            ========================
            REVIEW
            ========================
            """
        )

    # =====================================================
    # Build Context
    # =====================================================

    def build_context(self, documents):

        context_parts = []

        for doc in documents:

            metadata = doc.metadata

            source = metadata.get("source", "unknown")

            language = metadata.get("language", "unknown")

            chunk_type = metadata.get("type", "unknown")

            header = f"""
            FILE: {source}
            LANGUAGE: {language}
            CHUNK_TYPE: {chunk_type}
            """

            context_parts.append(
                header + "\n" + doc.page_content
            )

        return "\n\n".join(context_parts)

    # =====================================================
    # Review Code
    # =====================================================

    def review_code(self, question, documents):

        logger.info(
            f"Starting code review with {len(documents)} documents"
        )

        # Build structured context
        context = self.build_context(documents)

        # Create chain
        chain = self.prompt | self.llm

        # Invoke model
        response = chain.invoke({
            "context": context,
            "question": question
        })

        logger.info("Code review completed")

        return response.content