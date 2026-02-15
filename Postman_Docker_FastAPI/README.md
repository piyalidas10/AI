# Postman  →  Docker  →  FastAPI
Let’s build it properly using your existing FastAPI application and run it inside Docker.

Existing FastAPI application : https://github.com/piyalidas10/AI/tree/main/Fast_API

**How does Postman interact with FastAPI inside Docker?**
Postman sends an HTTP request to the host machine’s exposed port. Docker maps that host port to the container’s internal port, where Uvicorn runs the FastAPI application, processes the request, and returns a response back through Docker to Postman.

## ✅ Run DOCKER image in my Local

I already have docker image in my local which was created from https://github.com/piyalidas10/AI/tree/main/Fast_API.
<img src="docker_desktop.png" width="600px">

I have to create docker new container from existing docker image.

**1️⃣ Option 1** 
```
docker run -p 8000:8000 fastapi-enterprise
```
What this means:
```
Host Machine Port 8000  →  Container Port 8000
```
So Postman must call host port, not container internal port.   
Now Docker is running your FastAPI inside container.  

**2️⃣ Option 2** 
Open Docker Desktop
<img src="docker_desktop.png" width="600px">
<img src="run_docker.png" width="600px">
<img src="run_docker_1.png" width="600px">
<img src="run_docker_2.png" width="600px">
<img src="run_docker_3.png" width="600px">

Open Browser to check Fast API is running with post 8000
```
http://localhost:8000/docs
```
<img src="docs_browser.png" width="600px">

Open Postman.
```
POST http://localhost:8000/posts
```
Body → raw → JSON
```
{
  "title": "Test",
  "body": "Docker Integration",
  "userId": 1
}
```
Click Send.    
<img src="Run_Postman.png" width="600px">
<img src="Run_Postman_check_docker_container.png" width="600px">

If you want to stop Docker Container
<img src="Stop_Docker_Container.png" width="600px">


**🧠 What Actually Happens**

When Postman hits:
```
http://localhost:8000/posts
```
Flow:
```
Postman
   ↓
Your Machine Port 8000
   ↓
Docker Engine
   ↓
Container Port 8000
   ↓
Uvicorn Server
   ↓
FastAPI App
   ↓
Business Logic / Validation
   ↓
JSON Response
   ↓
Back to Postman
```

**If Postman fails:**

Run:
```
docker ps
```
Make sure container is running.

If not:
```
docker logs <container_id>
```


# 🐳 Dockerized Architecture Diagram

(FastAPI Enterprise API in Container)
```
                    ┌──────────────────────┐
                    │       Postman        │
                    │   (Client Machine)   │
                    └──────────┬───────────┘
                               │
                               │ HTTP Request
                               │ POST /posts
                               ▼
        ┌────────────────────────────────────────────┐
        │                 Docker Host                │
        │        (Your Windows / Linux Machine)      │
        │                                            │
        │   ┌────────────────────────────────────┐   │
        │   │          Docker Container          │   │
        │   │                                    │   │
        │   │  ┌──────────────────────────────┐  │   │
        │   │  │       Uvicorn Server         │  │   │
        │   │  │   (ASGI Runtime Process)     │  │   │
        │   │  └──────────────┬───────────────┘  │   │
        │   │                 │                  │   │
        │   │                 ▼                  │   │
        │   │       FastAPI Application          │   │
        │   │                                    │   │
        │   │   ┌────────────────────────────┐   │   │
        │   │   │   Pydantic Validation      │   │   │
        │   │   ├────────────────────────────┤   │   │
        │   │   │   Business Logic Layer     │   │   │
        │   │   ├────────────────────────────┤   │   │
        │   │   │   Global Exception Layer   │   │   │
        │   │   └────────────────────────────┘   │   │
        │   └────────────────────────────────────┘   │
        │                                            │
        └────────────────────────────────────────────┘
```

## 🧠 Internal Flow Inside Container
```
Postman
   ↓
Docker Network Layer
   ↓
Container (Port 8000)
   ↓
Uvicorn
   ↓
FastAPI Router
   ↓
Pydantic Validation
   ↓
Business Logic
   ↓
Exception Handler (if needed)
   ↓
JSON Response
   ↓
Postman
```
<img src="Postman_Docker_FastAPI.png" width="600px">

## 🏗 If You Add Database (Production Style)
```
                  ┌──────────────┐
                  │   Postman    │
                  └──────┬───────┘
                         │
                         ▼
                ┌────────────────┐
                │  FastAPI App   │  (Docker Container)
                └──────┬─────────┘
                       │
                       ▼
                ┌────────────────┐
                │ PostgreSQL DB  │  (Another Container)
                └────────────────┘
```
In production, we use:
    -   Docker Compose
    -   Multiple containers
    -   Separate network
    -   Environment variables

## 🐳 Production-Ready Docker Architecture
```
                ┌─────────────────────┐
                │      Postman        │
                └─────────┬───────────┘
                          │
                          ▼
               ┌──────────────────────┐
               │   Nginx (Optional)   │
               │ Reverse Proxy Layer  │
               └─────────┬────────────┘
                         │
                         ▼
               ┌──────────────────────┐
               │   FastAPI Container  │
               │   (Uvicorn + App)    │
               └─────────┬────────────┘
                         │
                         ▼
               ┌──────────────────────┐
               │  PostgreSQL Container│
               └──────────────────────┘
```

📦 What Docker Actually Does Here

Docker:

✔ Packages your FastAPI code   
✔ Installs dependencies (fastapi, uvicorn, pydantic)   
✔ Exposes port 8000    
✔ Runs Uvicorn automatically   
✔ Makes your app portable  