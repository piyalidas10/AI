# Postman  → FastAPI (Docker) -> Ollama

Now we build the clean working pipeline using phi3 (lightweight model).
```
Postman → FastAPI (Docker) → Ollama → Response

Postman
   ↓
Docker (FastAPI :8000)
   ↓
Ollama (Host :11434)
   ↓
Response

```

## Run FAST API using Docker

1. Open Docker desktop. Then Download Ollama from:
```
👉 https://ollama.com
```
Then pull a model:
```
ollama pull llama3
```
2. Open cmd inside "Postman_FastAPI_Ollama" folder   
3. Run the docker command in cmd to Build Docker Image
```
"docker build -t fastapi-ollama ."
```
<img src="imgs/docker_img_create.png" width="600px">
This creates an image named fastapi-ollama.
<img src="imgs/docker_image.png" width="600px">

4. Now you must run a Docker container from the already build Docker Image (fastapi-ollama).
Run the container (this actually starts FastAPI) using CMD
```
docker run -p 8000:8000 fastapi-ollama
```
OR  
Inside Docker Desktop, Click the ▶️ Run button next to fastapi-ollama. Click Optional settings.  

| Setting        | Value |
| -------------- | ----- |
| Host Port      | 8000  |
| Container Port | 8000  |

<img src="imgs/docker_image.png" width="600px">

It will open a popup.

<img src="imgs/run_docker_2.png" width="600px">

**If Verify It Is Running**     
Run this command:
```
docker ps
```
You should see something like:
```
CONTAINER ID   IMAGE                PORTS
xxxxx          fastapi-enterprise   0.0.0.0:8000->8000/tcp
```
**Now FastAPI is running inside Docker.**    
<img src="imgs/docker_running.png" width="600px">

```
Your Code (main.py)
        ↓
Docker Build → Image
        ↓
Docker Run → Container
        ↓
FastAPI running on :8000
```
5. Open:
```
http://localhost:8000/docs
```
<img src="imgs/fast_api_docs.png" width="600px">

6. Make sure Ollama is running
```
ollama run phi3
```
<img src="imgs/ollama_model_run_testing.png" width="600px">

7. Trigger from Postman
```
POST
http://localhost:8000/generate
```
Body → raw → JSON
```
{
  "prompt": "Explain Docker in simple words"
}
```
Response
```
{
    "success": true,
    "model": "phi3",
    "response": "Docker is like a special tool that helps you create and run applications inside containers, which are like lightweight virtual machines. It makes it easier to set up the environment needed for an application by packaging everything into one easy-to-distribute unit called a \"container.\" With Docker, software developers can package their code with all its dependencies in this container so that they only need install and run on any machine without worrying about configuration differences. This way of working allows people to develop faster because it eliminates the issues caused by inconsistent environments between different systems or locations (like homes, offices, etc.). It also makes sharing projects across teams much simpler! Lastly, Docker provides a built-in system for running and distributing applications as containers in production smoothly too.",
    "timestamp": "2026-02-16T15:34:54.448505"
}
```
<img src="imgs/Postman_Test.png" width="600px">

**✅ Expected Flow**

   -  Postman sends request to /generate
   -  FastAPI receives prompt
   -  FastAPI calls Ollama (phi3)
   -  Ollama generates answer
   -  FastAPI returns JSON response
   -  Postman displays answer



## 🧠 Real-Time Architecture (With LangChain & Ollama Example)
If you extend this to AI:
```
Postman
   │
   ▼
FastAPI Endpoint
   │
   ▼
LangChain
   │
   ▼
Ollama Model
   │
   ▼
Response → Postman
```
This is what happens when you do: 
```
Postman → FastAPI → LangChain → Ollama
```

1️⃣ API backend (FastAPI) 
2️⃣ Testing layer (Postman)   
3️⃣ AI model layer (Ollama)   
4️⃣ Possibly Docker containerization

## 🧠 What Happened Internally

1️⃣ Postman sends prompt  
2️⃣ FastAPI receives JSON 
3️⃣ FastAPI calls Ollama API  
4️⃣ Ollama generates response 
5️⃣ FastAPI returns response  
6️⃣ Postman displays it   


