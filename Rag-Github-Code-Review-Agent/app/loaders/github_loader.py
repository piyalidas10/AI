import os
import ast

from git import Repo

from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter

from tree_sitter_languages import get_parser


class GithubLoader:

    def __init__(self, repo_url: str, local_path: str = "repo"):

        self.repo_url = repo_url
        self.local_path = local_path

        # Tree-sitter parsers
        self.ts_parser = get_parser("typescript")
        self.js_parser = get_parser("javascript")

    # =====================================================
    # Clone Repository
    # =====================================================

    def clone_repo(self):

        if os.path.exists(self.local_path):
            return self.local_path

        Repo.clone_from(self.repo_url, self.local_path)

        return self.local_path

    # =====================================================
    # Load Files
    # =====================================================

    def load_code_files(self):

        documents = []

        for root, dirs, files in os.walk(self.local_path):

            # Ignore unnecessary folders
            dirs[:] = [
                d for d in dirs
                if d not in [
                    ".git",
                    "node_modules",
                    "__pycache__",
                    "dist",
                    "build",
                    ".next",
                    "venv",
                    "docs",
                    "tests",
                    "examples",
                    ".github",
                    "site-packages"
                ]
            ]

            for file in files:

                path = os.path.join(root, file)

                try:

                    # ======================================
                    # Python AST Chunking
                    # ======================================

                    if file.endswith(".py"):

                        python_docs = self.parse_python_file(path)

                        documents.extend(python_docs)

                    # ======================================
                    # TypeScript AST Chunking
                    # ======================================

                    elif file.endswith(".ts"):

                        ts_docs = self.parse_typescript_file(path)

                        documents.extend(ts_docs)

                    # ======================================
                    # JavaScript AST Chunking
                    # ======================================

                    elif file.endswith(".js"):

                        js_docs = self.parse_javascript_file(path)

                        documents.extend(js_docs)

                    # ======================================
                    # Other Languages Fallback
                    # ======================================

                    elif file.endswith((
                        ".java",
                        ".go",
                        ".cpp"
                    )):

                        with open(path, "r", encoding="utf-8") as f:

                            code = f.read()

                            documents.append(
                                Document(
                                    page_content=code,
                                    metadata={
                                        "source": path,
                                        "type": "full_file"
                                    }
                                )
                            )

                except Exception as e:

                    print(f"Error processing {path}: {e}")

        return documents

    # =====================================================
    # Python AST Parser
    # =====================================================

    def parse_python_file(self, file_path):

        documents = []

        with open(file_path, "r", encoding="utf-8") as f:

            source_code = f.read()

        tree = ast.parse(source_code)

        for node in ast.walk(tree):

            # Function
            if isinstance(node, ast.FunctionDef):

                function_code = ast.get_source_segment(
                    source_code,
                    node
                )

                documents.append(
                    Document(
                        page_content=function_code,
                        metadata={
                            "source": file_path,
                            "language": "python",
                            "type": "function",
                            "name": node.name,
                            "line": node.lineno
                        }
                    )
                )

            # Class
            elif isinstance(node, ast.ClassDef):

                class_code = ast.get_source_segment(
                    source_code,
                    node
                )

                documents.append(
                    Document(
                        page_content=class_code,
                        metadata={
                            "source": file_path,
                            "language": "python",
                            "type": "class",
                            "name": node.name,
                            "line": node.lineno
                        }
                    )
                )

        return documents

    # =====================================================
    # TypeScript Parser
    # =====================================================

    def parse_typescript_file(self, file_path):

        return self.parse_tree_sitter_file(
            file_path,
            self.ts_parser,
            "typescript"
        )

    # =====================================================
    # JavaScript Parser
    # =====================================================

    def parse_javascript_file(self, file_path):

        return self.parse_tree_sitter_file(
            file_path,
            self.js_parser,
            "javascript"
        )

    # =====================================================
    # Generic Tree-sitter Parser
    # =====================================================

    def parse_tree_sitter_file(
        self,
        file_path,
        parser,
        language
    ):

        documents = []

        with open(file_path, "r", encoding="utf-8") as f:

            source_code = f.read()

        tree = parser.parse(bytes(source_code, "utf8"))

        root_node = tree.root_node

        self.extract_nodes(
            root_node,
            source_code,
            file_path,
            language,
            documents
        )

        return documents

    # =====================================================
    # Extract Semantic Nodes
    # =====================================================

    def extract_nodes(
        self,
        node,
        source_code,
        file_path,
        language,
        documents
    ):

        important_types = [
            "function_declaration",
            "method_definition",
            "class_declaration",
            "lexical_declaration"
        ]

        if node.type in important_types:

            chunk = source_code[
                node.start_byte:node.end_byte
            ]

            documents.append(
                Document(
                    page_content=chunk,
                    metadata={
                        "source": file_path,
                        "language": language,
                        "type": node.type,
                        "start_line": node.start_point[0] + 1,
                        "end_line": node.end_point[0] + 1
                    }
                )
            )

        for child in node.children:

            self.extract_nodes(
                child,
                source_code,
                file_path,
                language,
                documents
            )

    # =====================================================
    # Secondary Chunking
    # =====================================================

    def split_documents(self, documents):

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1500,
            chunk_overlap=200
        )

        final_docs = []

        for doc in documents:

            # Split only large chunks
            if len(doc.page_content) > 2500:

                split_docs = splitter.split_documents([doc])

                final_docs.extend(split_docs)

            else:
                final_docs.append(doc)

        return final_docs