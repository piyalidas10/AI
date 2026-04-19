from langchain_ollama import ChatOllama
from langchain.prompts import ChatPromptTemplate


class CodeReviewerAgent:

    def __init__(self):

        # Using Ollama local model
        self.llm = ChatOllama(
            model="phi3",
            temperature=0
        )

        self.prompt = ChatPromptTemplate.from_template(
            """
            You are a senior software engineer performing a professional code review.

            Use ONLY the provided context.

            Check for:
            - bugs
            - security issues
            - performance improvements
            - code readability
            - best practices

            Return the answer in the following structured format:

            File:
            Issue:
            Explanation:
            Suggested Fix:

            Context:
            {context}

            Question:
            {question}

            Provide the review now.
            """
        )

    def review_code(self, question, documents):

        # Combine retrieved code chunks
        context = "\n\n".join([doc.page_content for doc in documents])

        # Build chain
        chain = self.prompt | self.llm

        # Invoke LLM
        response = chain.invoke({
            "context": context,
            "question": question
        })

        return response.content