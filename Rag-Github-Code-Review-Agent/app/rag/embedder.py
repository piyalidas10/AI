from langchain_ollama import OllamaEmbeddings


class Embedder:

    def __init__(self):
        self.embedding = OllamaEmbeddings(model="nomic-embed-text")

    def get_embeddings(self):
        return self.embedding