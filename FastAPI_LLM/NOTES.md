# 1️⃣ FastAPI

### 🔹 What is FastAPI?
    -   A modern Python web framework
    -   Used to build REST APIs
    -   Very fast (built on Starlette + Pydantic)
    -   Automatic Swagger documentation

### 🔹 Why we use FastAPI in LLM projects?
    -   To create an API endpoint
    -   To expose LLM functionality over HTTP
    -   To connect frontend (Angular/React) with backend AI logic

### 🔹 Basic Example
```
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}
```

If you run:
```
uvicorn main:app --reload
```

You get:
```
http://localhost:8000
```

Swagger docs:
```
http://localhost:8000/docs
```

### 🔹 In LLM Architecture

FastAPI acts as:
```
User → FastAPI → LangChain → Ollama → Response → FastAPI → User
```

It is the API layer.

# 2️⃣ Postman
### 🔹 What is Postman?
    -   API testing tool
    -   Used to send HTTP requests
    -   Used to test backend endpoints

### 🔹 Why use Postman?
    -   To test your FastAPI endpoints
    -   To send POST requests with prompts
    -   To debug JSON request/response

### 🔹 Example

If your FastAPI has:
```
@app.post("/ask")
def ask_question(prompt: str):
    return {"response": prompt}
```

In Postman:
    -   Method → POST
    -   URL → http://localhost:8000/ask
    -   Body → raw → JSON
```
{
  "prompt": "Tell me about Kolkata cuisine"
}
```

### 🔹 Role in Architecture

Postman is: Testing Client

    -   It simulates:
    -   Frontend
    -   Mobile app
    -   Browser
    -   Any external client


# 3️⃣ LangChain
### 🔹 What is LangChain?

    -   Python framework for building LLM applications
    -   Helps connect LLM with:
        -   Prompts
        -   Memory
        -   Tools
        -   RAG
        -   Vector DB

### 🔹 Why use LangChain?

Instead of directly calling LLM:
```
response = ollama.generate("Tell me about AI")
```

LangChain gives:
    -   Prompt templates
    -   Chains
    -   Agents
    -   RAG pipelines
    -   Structured output

### 🔹 Example with Ollama
```
from langchain_community.llms import Ollama

llm = Ollama(model="llama2")

response = llm.invoke("Tell me about Kolkata cuisine")
print(response)
```

### 🔹 Important Components
| Component      | Purpose              |
| -------------- | -------------------- |
| PromptTemplate | Format prompt        |
| LLM            | Connect to model     |
| Chain          | Combine prompt + LLM |
| Memory         | Conversation history |
| Retriever      | Used in RAG          |
| Agent          | Tool-calling logic   |

### 🔹 In Architecture

LangChain is: AI Orchestration Layer

It manages:
    -   Prompt engineering
    -   RAG
    -   Tool usage
    -   Memory

# 4️⃣ Ollama
### 🔹 What is Ollama?
    -   Tool to run LLMs locally
    -   Runs models like:
        -   Llama2
        -   Mistral
        -   Gemma
        -   DeepSeek

### 🔹 Why Ollama?
    -   No API cost
    -   Runs locally
    -   No internet required
    -   Data privacy

### 🔹 Install (Windows)
```
ollama pull llama2
ollama run llama2
```

### 🔹 How it works internally
```
Prompt → Model → Tokenization → Transformer → Output tokens → Text
```

### 🔹 Ollama API (Local)

Runs at:
```
http://localhost:11434
```

You can call it directly via REST API OR via LangChain.

