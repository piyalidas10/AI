# Docker

## 🐳 Docker & Docker Compose Command Reference
| Command                                               | What It Does                                         | When To Use                 | Risk Level   |
| ----------------------------------------------------- | ---------------------------------------------------- | --------------------------- | ------------ |
| `docker compose up`                                   | Starts services defined in docker-compose.yml        | Normal startup              | Safe         |
| `docker compose up -d`                                | Starts services in background (detached mode)        | Production / background run | Safe         |
| `docker compose down`                                 | Stops and removes containers                         | When stopping project       | Safe         |
| `docker compose down -v`                              | Stops containers **and deletes volumes (data lost)** | Full reset / clean DB       | ⚠️ Dangerous |
| `docker compose build`                                | Builds images from Dockerfile                        | After code change           | Safe         |
| `docker compose build --no-cache`                     | Rebuilds from scratch (ignores cache)                | Fix weird build issue       | Medium       |
| `docker compose restart`                              | Restarts running containers                          | Quick refresh               | Safe         |
| `docker compose logs`                                 | Shows logs of all services                           | Debugging                   | Safe         |
| `docker compose logs -f`                              | Shows live logs                                      | Real-time debugging         | Safe         |
| `docker ps`                                           | Shows running containers                             | Check status                | Safe         |
| `docker ps -a`                                        | Shows all containers (even stopped)                  | Debugging                   | Safe         |
| `docker images`                                       | Lists all built images                               | Check image size            | Safe         |
| `docker exec -it <container> bash`                    | Enter container terminal                             | Debug inside container      | Safe         |
| `docker exec -it ollama ollama pull phi3`             | Pull model inside Ollama container                   | First-time model setup      | Safe         |
| `docker exec -it ollama ollama pull nomic-embed-text` | Pull embedding model                                 | First-time embedding setup  | Safe         |
| `docker volume ls`                                    | List volumes                                         | Check persistent storage    | Safe         |
| `docker volume rm <volume>`                           | Remove specific volume                               | Clean specific DB           | ⚠️ Careful   |
| `docker system prune`                                 | Remove unused containers/images                      | Clean disk                  | ⚠️ Careful   |
| `docker system prune -a`                              | Remove ALL unused images                             | Full cleanup                | 🚨 Risky     |

## 🧠 For Your AI Project (Best Practice)
**✅ Normal Daily Run**
```
docker compose up -d
```

**✅ After Code Change**
```
docker compose build
docker compose up -d
```

**❌ Only When Resetting Everything**
```
docker compose down -v
docker compose build --no-cache
docker compose up
```

### 💡 Important for You
Since you're working with:
- FastAPI
- LangChain
- Qdrant
- Ollama (phi3 + nomic-embed-text)

👉 If containers are already running, you DO NOT need to pull models again.
Models stay inside Ollama volume unless you delete it.

## 🐳 Docker Ecosystem
Your diagram contains:
    -   Docker Client
    -   Docker Server
    -   Docker Machine
    -   Docker Images
    -   Docker Hub
    -   Docker Compose


**1️⃣ Docker Client**

👉 This is what you use.

Examples:
    -   docker build
    -   docker run
    -   docker compose up
    -   docker scout cves

When you type a command in:
    -   Terminal
    -   VS Code
    -   PowerShell

It talks to Docker Server.

**2️⃣ Docker Server (Docker Daemon)**

👉 This is the engine that does the real work.

It:
    -   Builds images
    -   Runs containers
    -   Pulls images
    -   Manages networks & volumes

Client → sends command → Server executes.

**3️⃣ Docker Images**

👉 Read-only templates used to create containers.

Example:
```
docker build -t fastapi-app .
```

Image contains:
    -   Python
    -   FastAPI
    -   Your code
    -   Dependencies

Then you run:
```
docker run fastapi-app
```
That creates a container from image.

**4️⃣ Docker Hub**

👉 Public image registry (like GitHub for Docker images).

Examples:
    -   python:3.12-slim
    -   nginx
    -   redis
    -   postgres

When you do:
```
docker pull python:3.12-slim
```

It downloads from Docker Hub.

You can also push your own image:
```
docker push myusername/fastapi-app
```

**5️⃣ Docker Compose**

👉 Used to manage multi-container applications.

Example:

Instead of running:
```
docker run fastapi
docker run qdrant
docker run redis
```
You define:
```
services:
  app:
  qdrant:
  redis:
```
And run:
```
docker compose up
```
It manages everything together.

**6️⃣ Docker Machine (Older Concept)**

👉 Used to create Docker hosts on:
    -   VirtualBox
    -   AWS
    -   Azure

⚠️ Mostly replaced now by:
    -   Docker Desktop
    -   Kubernetes
    -   Cloud container services

## 🔥 How Everything Connects (Real Flow)

Let’s map it practically:
```
You (Docker Client)
        ↓
Docker Daemon (Server)
        ↓
Build Image
        ↓
Store locally or push to Docker Hub
        ↓
Run container
        ↓
Manage multiple services with Docker Compose
        ↓
Scan image with Docker Scout
        ↓
Fix CVEs
```

## 🔎 Where Docker Scout Fits

Docker Scout checks:

Docker Image → for CVEs → shows in:

    -   CLI
    -   Docker Desktop → Images → Security tab

## 🧠 Enterprise Architecture View

If you’re building:

**FastAPI + LangChain + Qdrant + Ollama**

Your ecosystem becomes:
```
Docker Client
    ↓
Docker Compose
    ↓
---------------------------------
| FastAPI Container            |
| Qdrant Container             |
| Ollama Container             |
---------------------------------
    ↓
Docker Images
    ↓
Docker Hub
    ↓
Docker Scout (Security Scan)
```

## Draw a modern enterprise-grade Docker architecture diagram
Here is a production-ready architecture (example: FastAPI + Qdrant + Redis + CI/CD):
```
                        ┌─────────────────────────┐
                        │        Developer        │
                        │  (VS Code / Terminal)   │
                        └─────────────┬───────────┘
                                      │ docker build
                                      ▼
                        ┌─────────────────────────┐
                        │     Docker Client       │
                        └─────────────┬───────────┘
                                      │
                                      ▼
                        ┌─────────────────────────┐
                        │   Docker Daemon         │
                        │   (Docker Engine)       │
                        └─────────────┬───────────┘
                                      │
                                      ▼
                        ┌─────────────────────────┐
                        │     Docker Image        │
                        └─────────────┬───────────┘
                                      │
                     ┌────────────────┴────────────────┐
                     ▼                                 ▼
         ┌─────────────────────┐            ┌────────────────────┐
         │   Docker Scout      │            │   Docker Registry  │
         │  (CVE Scan)         │            │ (Docker Hub / ECR) │
         └──────────┬──────────┘            └──────────┬─────────┘
                    │                                   │
                    ▼                                   ▼
              Fix Vulnerabilities               Push Clean Image
                    │                                   │
                    └──────────────┬────────────────────┘
                                   ▼
                         ┌───────────────────────┐
                         │   Production Server   │
                         │ (VM / Cloud / K8s)    │
                         └───────────┬───────────┘
                                     ▼
                      ┌────────────────────────────┐
                      │ Docker Compose / K8s Pods  │
                      │  - FastAPI                 │
                      │  - Qdrant                  │
                      │  - Redis                   │
                      └────────────────────────────┘
```
This is enterprise-grade because it includes:
    -   Image scanning
    -   Registry push
    -   Controlled deployment
    -   Multi-container orchestration

## ✅ Where CVE Scanning Fits in DevOps Pipeline

CVE scanning happens before deployment.

Modern DevSecOps Pipeline:
```
Code → Build → Scan → Fix → Push → Deploy
```
Expanded version:
```
Developer pushes code to GitHub
            │
            ▼
      CI Pipeline starts
            │
      Build Docker Image
            │
            ▼
     🔎 Docker Scout Scan
            │
   ┌────────┴─────────┐
   │                  │
No Critical        Critical Found
   │                  │
Push to Registry    Fail Pipeline
   │                  │
Deploy              Developer Fix
```

⚠️ In enterprise, deployment is blocked if:
    -   Critical CVEs > 0
    -   High CVEs > allowed threshold

This is called Shift-Left Security.

## ✅ CI/CD Flow with Docker Scout

Example using GitHub Actions:
```
GitHub Repo
    │
    ▼
GitHub Actions Workflow
    │
    ├── Step 1: Checkout Code
    ├── Step 2: Build Docker Image
    ├── Step 3: docker scout cves
    ├── Step 4: Fail if Critical > 0
    ├── Step 5: Push to Docker Hub
    └── Step 6: Deploy to Server
```
Real command in CI:
```
docker build -t myapp .
docker scout cves myapp --exit-code
```
If vulnerabilities found → CI fails automatically.

This is enterprise DevSecOps automation.

**✅ Docker Networking (Visual Explanation)**

Docker creates isolated networks.

**🔹 Default Bridge Network**
```
Container A  ←→  Container B
       │
       ▼
  Docker Bridge Network
       │
       ▼
 Host Machine
```
Containers communicate internally using:
```
http://service_name:port
```
Example in docker-compose:
```
services:
  app:
  redis:
```
App connects to Redis using:
```
redis:6379
```

**🔹 Types of Docker Networks** 
| Type    | Use Case                  |
| ------- | ------------------------- |
| bridge  | Default local containers  |
| host    | Use host network directly |
| overlay | Multi-host (Swarm/K8s)    |
| macvlan | Assign real IP            |

## ✅ Docker vs Kubernetes (Enterprise View)
| Feature           | Docker            | Kubernetes               |
| ----------------- | ----------------- | ------------------------ |
| Purpose           | Container runtime | Container orchestration  |
| Scaling           | Manual            | Auto-scaling             |
| Self-healing      | No                | Yes                      |
| Load balancing    | Basic             | Advanced                 |
| Production ready? | Small-medium apps | Large enterprise systems |

**🔹 Visual Comparison**
Docker Compose
```
1 Server
 ├── App
 ├── Redis
 └── Qdrant
```
Simple.

**Kubernetes**
```
Cluster
 ├── Node 1
 │    ├── Pod (App)
 │    └── Pod (Redis)
 ├── Node 2
 │    └── Pod (Qdrant)
 └── Load Balancer
```
Features:
    -   Auto restart pods
    -   Horizontal scaling
    -   Rolling updates
    -   Secrets management

Use Docker Compose if:
    -   Learning
    -   Small production app
    -   Single server deployment

Use Kubernetes if:
    -   High traffic
    -   Auto scaling needed
    -   Multiple microservices
    -   Enterprise infrastructure