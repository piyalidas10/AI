from langchain_ollama import OllamaEmbeddings

# Since you're running inside Docker Compose, you should explicitly specify the Ollama container URL.
class Embedder:

    _instance = None

    def __new__(cls):

        if cls._instance is None:

            cls._instance = super().__new__(cls)

            cls._instance.embedding = OllamaEmbeddings(
                model="nomic-embed-text",
                base_url="http://ollama:11434"
            )

        return cls._instance

    def get_embeddings(self):
        return self.embedding