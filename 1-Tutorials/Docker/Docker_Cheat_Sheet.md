
# 🐳 Docker Cheat Sheet (Real-World)

### 🔨 1. Build Image
```
docker build -t <Docker image name> .
```

👉 Tag with version:
```
docker build -t <Docker image name>:v1 .
```

### 📦 2. Create Container (no start)
```
docker create --name <Container name> <Docker image name>
```
👉 With port:
```
docker create -p 3000:3000 --name <Container name> <Docker image name>
```

### 🚀 3. Run Container (create + start)
```
docker run <Docker image name>
```

👉 Detached + port + name:
```
docker run -d -p 3000:3000 --name <Container name> <Docker image name>
```

👉 With env:
```
docker run -d -e NODE_ENV=prod <Docker image name>
```

### ▶️ 4. Start / Stop
```
docker start <Container name>
docker stop <Container name>
```

### 🔁 5. Restart
```
docker restart <Container name>
```

### 🗑️ 6. Remove
```
docker rm <Container name>
docker rmi <Docker image name>
```

### 📜 7. Logs
```
docker logs <Container name>
docker logs -f <Container name>
```

### 🐚 8. Exec (enter container)
```
docker exec -it <Container name> sh
```

👉 Run command:
```
docker exec -it <Container name> ls
```

### 📊 9. Status / Listing
```
docker ps          # running
docker ps -a       # all
docker images
```

### 🔌 10. Port Mapping

👉 Run with port:
```
docker run -p 4000:3000 <Docker image name>
```
👉 Check port:
```
docker port <Container name>
```
⚠️ Cannot change port of running container → must recreate

### 🌐 11. Networking
```
docker network ls
docker network create <Network name>
```
👉 Run in network:
```
docker run -d --network <Network name> <Docker image name>
```

### 💾 12. Volumes (Data persistence)
```
docker volume create <Data name>
```
👉 Use volume:
```
docker run -v <Data name>:/app/data <Docker image name>
```

### 🧹 13. Cleanup
```
docker system prune
docker system prune -a
```

### 📦 14. Docker Compose
```
docker-compose up
docker-compose up -d
docker-compose down
```

### 🔍 15. Inspect (deep debug)
```
docker inspect <Container name>
```

### 🚀 16. Copy Files
```
docker cp file.txt <Container name>:/app/
```

### 🧠 1. Run Ollama in Docker
```
docker run -d \
  --name ollama \
  -p 11434:11434 \
  ollama/ollama
```
👉 This starts Ollama API at:
http://localhost:11434

### 📦 2. Check Running Container
```
docker ps
```

### 📥 3. Pull Models (inside container)
```
docker exec -it ollama ollama pull <model name>
```
-it → interactive terminal (so you can see output properly)

```
docker exec -it ollama ollama pull llama3
docker exec -it ollama ollama pull phi3
docker exec -it ollama ollama pull mistral
```

### 📜 4. List Downloaded Models (Go inside the ollama container and list all installed models)
```
docker exec -it ollama ollama list
```
+ docker exec → runs a command inside an existing container
+ -it → interactive terminal (so you can see output properly)
+ ollama → container name
+ ollama list → command inside the container (from Ollama)

### 🚀 5. Run Model (interactive)
```
docker exec -it ollama ollama run <model name>
```

```
docker exec -it ollama ollama run llama3
```

### 🔍 6. Check Logs
```
docker logs -f ollama
```

### 🐚 7. Enter Container Shell
```
docker exec -it ollama sh
```
Then:
```
ollama list
```

### 🌐 8. Call Ollama via API (VERY IMPORTANT)
List models
```
curl http://localhost:11434/api/tags
```

Generate response
```
curl http://localhost:11434/api/generate -d '{
  "model": "llama3",
  "prompt": "Explain RAG architecture"
}'
```

### 💾 9. Persist Models (Volume)

⚠️ Without this, models will be lost if container is removed.
```
docker run -d \
  --name ollama \
  -p 11434:11434 \
  -v ollama-data:/root/.ollama \
  ollama/ollama
```

### ⚡ 10. GPU Support (for faster inference)
```
docker run -d \
  --gpus all \
  -p 11434:11434 \
  -v ollama-data:/root/.ollama \
  --name ollama \
  ollama/ollama
```

### 🔁 11. Restart / Stop
```
docker restart ollama
docker stop ollama
```

### 🗑️ 12. Remove Container
```
docker rm -f ollama
```

### 📊 13. Inspect Container
```
docker inspect ollama
```

### 🔄 14. Update Ollama Image
```
docker pull ollama/ollama
docker stop ollama
docker rm ollama

docker run -d -p 11434:11434 --name ollama ollama/ollama
```

### Restart your containers
```
docker compose restart
```

### Stop all containers
```
docker stop $(docker ps -q)
```

### Remove all containers
```
docker rm $(docker ps -aq)
```

### Reset and Rebuild your Docker Compose environment
```
docker compose down -v
docker compose build --no-cache
docker compose up
```

**1. Stop and remove everything**
```
docker compose down -v
```
Removes:
- Running containers
- Networks
- Volumes (-v)
- Anonymous data

Useful when:
- Database got corrupted
- Cache issues
- Old dependencies remain
- Fresh environment needed

**2. Rebuild images from scratch**
```
docker compose build --no-cache
```
Forces Docker to:
- Ignore previous cached layers
- Reinstall packages
- Re-run all Dockerfile steps

Useful when:
- package.json changed
- requirements.txt changed
- Docker cache causing issues
- ENV variables updated

**3. Start services**
```
docker compose up
```
Starts all services defined in docker-compose.yml.

For background mode:
```
docker compose up -d
```
For live logs:
```
docker compose logs -f
```

