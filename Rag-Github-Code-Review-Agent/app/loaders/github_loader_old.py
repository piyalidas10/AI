import os
from git import Repo
from langchain.schema import Document
from langchain_text_splitters import Language
from langchain.text_splitter import RecursiveCharacterTextSplitter


class GithubLoader:

    def __init__(self, repo_url: str, local_path: str = "repo"):
        self.repo_url = repo_url
        self.local_path = local_path

    def clone_repo(self):

        if os.path.exists(self.local_path):
            return self.local_path

        Repo.clone_from(self.repo_url, self.local_path)
        return self.local_path

    def load_code_files(self):

        documents = []

        for root, dirs, files in os.walk(self.local_path):

            for file in files:

                if file.endswith((".py", ".js", ".ts", ".java", ".go", ".cpp")):

                    path = os.path.join(root, file)

                    try:
                        with open(path, "r", encoding="utf-8") as f:

                            code = f.read()

                            documents.append(
                                Document(
                                    page_content=code,
                                    metadata={"source": path}
                                )
                            )

                    except Exception:
                        pass

        return documents

    def split_documents(self, documents):

        # RecursiveCharacterTextSplitter is fundamentally a character-based splitter. Right now you chunk by characters.
        # It tries to split text recursively using separators like:
        # 
        # \n\n
        # \n
        # space
        # character
        # 
        # but ultimately the chunk size is measured in characters/tokens, not code structure.
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1200,
            chunk_overlap=200
        )

        # This is MUCH better for code. It tries to split around: classes, functions, methods instead of raw characters.
        splitter = RecursiveCharacterTextSplitter.from_language(
            language= Language.PYTHON,
            chunk_size=1200,
            chunk_overlap=200
        )

        return splitter.split_documents(documents)