class Retriever:

    def __init__(self, vector_store):
        self.vector_store = vector_store

    def get_retriever(self):

        return self.vector_store.as_retriever(
            search_type="similarity",
            search_kwargs={"k": 4}
        )

    def retrieve(self, query):

        retriever = self.get_retriever()

        docs = retriever.get_relevant_documents(query)

        return docs