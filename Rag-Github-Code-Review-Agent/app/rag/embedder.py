from langchain_ollama import OllamaEmbeddings

# Since you're running inside Docker Compose, you should explicitly specify the Ollama container URL.
class Embedder:

    def __init__(self):

        self.embedding = OllamaEmbeddings(
            model="nomic-embed-text",
            base_url="http://ollama:11434"
        )

    def get_embeddings(self):
        return self.embedding