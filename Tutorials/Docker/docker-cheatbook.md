# Docker Cheatbook — Complete Command Reference

A comprehensive reference for every Docker command with clear explanations, real-world examples, and common use cases. From beginner basics to advanced production patterns.

---

## Table of Contents

1. [Docker Version & System Info](#1-docker-version--system-info)
2. [Images](#2-images)
3. [Containers — Lifecycle](#3-containers--lifecycle)
4. [Containers — Inspect & Debug](#4-containers--inspect--debug)
5. [Containers — Exec & Logs](#5-containers--exec--logs)
6. [Networking](#6-networking)
7. [Volumes & Storage](#7-volumes--storage)
8. [Docker Compose](#8-docker-compose)
9. [Dockerfile Instructions](#9-dockerfile-instructions)
10. [Registry & Hub](#10-registry--hub)
11. [Build — Advanced](#11-build--advanced)
12. [Docker System Cleanup](#12-docker-system-cleanup)
13. [Docker Stats & Monitoring](#13-docker-stats--monitoring)
14. [Docker Swarm](#14-docker-swarm)
15. [Security & Permissions](#15-security--permissions)
16. [Real-World Recipes](#16-real-world-recipes)

---

## 1. Docker Version & System Info

```bash
# Check Docker client and server version
docker version

# Show system-wide information (containers, images, resources)
docker info

# Show only the Docker version number
docker --version

# Check if Docker daemon is running
docker system info
```

| Command | What it tells you |
|---|---|
| `docker version` | Client version, server version, API version, OS/Arch |
| `docker info` | # containers running/stopped, images, storage driver, memory, CPUs |
| `docker system df` | Disk space used by images, containers, volumes, build cache |

---

## 2. Images

### Pulling Images

```bash
# Pull the latest version of an image from Docker Hub
docker pull nginx

# Pull a specific version (tag)
docker pull nginx:1.25

# Pull from a specific registry (not Docker Hub)
docker pull gcr.io/google-containers/pause:3.1

# Pull and suppress verbose output
docker pull ubuntu:22.04 --quiet
```

### Listing Images

```bash
# List all locally available images
docker images

# Same as above (long form)
docker image ls

# List images with full image ID (no truncation)
docker images --no-trunc

# Show only image IDs
docker images -q

# Filter images by name
docker images nginx

# Filter dangling images (untagged images left after builds)
docker images --filter "dangling=true"

# Show image size, creation date, and tags in table format
docker images --format "table {{.Repository}}\t{{.Tag}}\t{{.Size}}\t{{.CreatedAt}}"
```

### Inspecting Images

```bash
# Show detailed metadata about an image (JSON)
docker inspect nginx

# Get a specific field using Go template
docker inspect --format='{{.Os}}/{{.Architecture}}' nginx

# Show image layer history (how the image was built)
docker history nginx

# Show history without truncating commands
docker history --no-trunc nginx
```

### Tagging & Renaming Images

```bash
# Tag an image with a new name (useful before pushing to a registry)
docker tag nginx:latest myregistry.com/myapp/nginx:v1.0

# Tag with multiple aliases
docker tag myapp:latest myapp:1.2.3
docker tag myapp:latest myapp:stable
```

### Removing Images

```bash
# Remove a specific image
docker rmi nginx

# Remove by image ID
docker rmi abc123def456

# Force remove (even if containers use it)
docker rmi -f nginx

# Remove multiple images at once
docker rmi nginx ubuntu redis

# Remove all dangling (untagged) images
docker image prune

# Remove ALL unused images (not just dangling)
docker image prune -a

# Remove all images (use carefully!)
docker rmi $(docker images -q)
```

### Saving & Loading Images

```bash
# Save an image to a .tar file (useful for air-gapped environments)
docker save nginx:latest -o nginx.tar
docker save nginx:latest > nginx.tar

# Load an image from a .tar file
docker load -i nginx.tar
docker load < nginx.tar

# Export a running container's filesystem (not the image layers)
docker export mycontainer > mycontainer.tar

# Import an exported container as a new image
docker import mycontainer.tar myapp:restored
```

---

## 3. Containers — Lifecycle

### Running Containers

```bash
# Run a container (pulls image if not available locally)
docker run nginx

# Run in detached mode (background)
docker run -d nginx

# Run with a custom name
docker run -d --name my-nginx nginx

# Run and immediately remove when it exits (great for one-off tasks)
docker run --rm ubuntu echo "Hello Docker"

# Run interactively with a terminal (for exploration)
docker run -it ubuntu bash

# Run interactively and remove on exit
docker run --rm -it ubuntu bash

# Map host port 8080 to container port 80
docker run -d -p 8080:80 nginx

# Map multiple ports
docker run -d -p 8080:80 -p 8443:443 nginx

# Map all exposed ports to random host ports
docker run -d -P nginx

# Set environment variables
docker run -d -e MYSQL_ROOT_PASSWORD=secret mysql

# Set multiple environment variables
docker run -d \
  -e MYSQL_ROOT_PASSWORD=secret \
  -e MYSQL_DATABASE=mydb \
  -e MYSQL_USER=myuser \
  mysql

# Load env variables from a file
docker run -d --env-file .env myapp

# Set memory limit (container OOM-killed if exceeded)
docker run -d --memory="512m" nginx

# Set CPU limit (1.5 = 1.5 cores)
docker run -d --cpus="1.5" nginx

# Restart policy: always restart unless manually stopped
docker run -d --restart unless-stopped nginx

# Restart policies:
#   no            → never restart (default)
#   always        → always restart
#   on-failure    → restart only on non-zero exit code
#   unless-stopped → restart always except when manually stopped
docker run -d --restart on-failure:5 myapp   # max 5 retries

# Run with a volume mount
docker run -d -v /host/path:/container/path nginx

# Run with a named volume
docker run -d -v mydata:/var/lib/mysql mysql

# Run with read-only filesystem (security hardening)
docker run -d --read-only nginx

# Set the working directory inside the container
docker run -w /app myapp

# Override the default CMD
docker run ubuntu echo "Override CMD"

# Override the entrypoint
docker run --entrypoint bash ubuntu

# Set hostname inside container
docker run --hostname myserver ubuntu

# Connect to a specific network
docker run -d --network mynetwork nginx

# Add a host entry to /etc/hosts inside the container
docker run --add-host db:192.168.1.10 myapp

# Set user (run as non-root for security)
docker run --user 1001 myapp

# Run with privileged access (dangerous — grants all Linux capabilities)
docker run --privileged myapp

# Add specific Linux capabilities
docker run --cap-add NET_ADMIN myapp

# Drop Linux capabilities
docker run --cap-drop ALL --cap-add NET_BIND_SERVICE myapp
```

### Starting, Stopping, Restarting

```bash
# Start a stopped container
docker start mycontainer

# Stop a running container (sends SIGTERM, waits 10s, then SIGKILL)
docker stop mycontainer

# Stop with custom timeout (seconds before SIGKILL)
docker stop -t 30 mycontainer

# Kill immediately (sends SIGKILL — no graceful shutdown)
docker kill mycontainer

# Send a specific signal
docker kill --signal SIGINT mycontainer

# Restart a container
docker restart mycontainer

# Restart with a custom timeout
docker restart -t 5 mycontainer

# Pause a container (freezes all processes — useful for snapshots)
docker pause mycontainer

# Unpause a paused container
docker unpause mycontainer
```

### Listing Containers

```bash
# List running containers
docker ps

# List ALL containers (running + stopped)
docker ps -a

# Show only container IDs
docker ps -q

# Show last N created containers
docker ps -n 5

# Show container sizes
docker ps -s

# Custom format output
docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"

# Filter by status
docker ps --filter "status=exited"
docker ps --filter "status=running"

# Filter by name
docker ps --filter "name=nginx"

# Filter by image
docker ps --filter "ancestor=nginx"
```

### Removing Containers

```bash
# Remove a stopped container
docker rm mycontainer

# Force remove a running container
docker rm -f mycontainer

# Remove and delete its anonymous volumes too
docker rm -v mycontainer

# Remove all stopped containers
docker container prune

# Remove all stopped containers without confirmation prompt
docker container prune -f

# Remove all containers (running + stopped) — DESTRUCTIVE
docker rm -f $(docker ps -aq)
```

---

## 4. Containers — Inspect & Debug

```bash
# Show detailed JSON metadata about a container
docker inspect mycontainer

# Get the container's IP address
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' mycontainer

# Get the container's mounts
docker inspect -f '{{json .Mounts}}' mycontainer | python -m json.tool

# Get the restart count
docker inspect -f '{{.RestartCount}}' mycontainer

# Show port mappings
docker port mycontainer

# Show port mapping for a specific port
docker port mycontainer 80

# Show real-time events from the Docker daemon
docker events

# Filter events by container
docker events --filter container=mycontainer

# Filter events by event type
docker events --filter event=start
docker events --filter event=die

# Show differences in container filesystem since it started
docker diff mycontainer
# A = Added, C = Changed, D = Deleted
```

---

## 5. Containers — Exec & Logs

### Exec into Running Containers

```bash
# Open an interactive bash shell inside a running container
docker exec -it mycontainer bash

# Use sh if bash is not available (Alpine-based images)
docker exec -it mycontainer sh

# Run a single command inside a container without interactive mode
docker exec mycontainer ls /app

# Run as a specific user inside the container
docker exec -it --user root mycontainer bash

# Set environment variable for the exec session
docker exec -e DEBUG=true mycontainer env

# Run in a specific directory
docker exec -w /tmp mycontainer ls
```

### Logs

```bash
# View all logs from a container
docker logs mycontainer

# Follow (tail) logs in real time (like tail -f)
docker logs -f mycontainer

# Show last 100 lines
docker logs --tail 100 mycontainer

# Show logs with timestamps
docker logs -t mycontainer

# Combine: last 50 lines, follow, with timestamps
docker logs --tail 50 -f -t mycontainer

# Show logs since a specific time (ISO 8601 or relative)
docker logs --since "2025-01-01T10:00:00" mycontainer
docker logs --since 30m mycontainer   # last 30 minutes
docker logs --until 1h mycontainer    # up until 1 hour ago

# Redirect logs to a file
docker logs mycontainer > app.log 2>&1
```

### Copying Files

```bash
# Copy a file from the host into a running container
docker cp ./config.json mycontainer:/app/config.json

# Copy a directory into a container
docker cp ./dist/ mycontainer:/usr/share/nginx/html/

# Copy a file from a container to the host
docker cp mycontainer:/var/log/app.log ./app.log

# Copy a directory from a container to the host
docker cp mycontainer:/app/logs ./logs
```

---

## 6. Networking

### Network Management

```bash
# List all Docker networks
docker network ls

# Create a custom bridge network
docker network create mynetwork

# Create with a specific subnet and gateway
docker network create \
  --subnet 172.20.0.0/16 \
  --gateway 172.20.0.1 \
  mynetwork

# Create an overlay network (for Docker Swarm / multi-host)
docker network create --driver overlay myoverlay

# Inspect a network (see connected containers, subnet, etc.)
docker network inspect mynetwork

# Connect a running container to a network
docker network connect mynetwork mycontainer

# Connect and assign a specific IP
docker network connect --ip 172.20.0.10 mynetwork mycontainer

# Disconnect a container from a network
docker network disconnect mynetwork mycontainer

# Remove a network
docker network rm mynetwork

# Remove all unused networks
docker network prune
```

### Network Drivers

| Driver | Use case |
|---|---|
| `bridge` | Default. Isolated network on a single host |
| `host` | Container shares the host's network stack (no isolation) |
| `none` | No networking at all (fully isolated) |
| `overlay` | Multi-host networking (Docker Swarm / Kubernetes) |
| `macvlan` | Container gets its own MAC address (acts like a physical device) |

```bash
# Run container on host network (port 80 is directly the host's port 80)
docker run -d --network host nginx

# Run with no network
docker run --network none myapp
```

---

## 7. Volumes & Storage

### Volume Management

```bash
# Create a named volume
docker volume create mydata

# List all volumes
docker volume ls

# Inspect a volume (see mountpoint on host)
docker volume inspect mydata

# Remove a specific volume
docker volume rm mydata

# Remove all unused volumes
docker volume prune

# Remove all unused volumes without confirmation
docker volume prune -f
```

### Mount Types

```bash
# Named volume (managed by Docker — persists across container restarts)
docker run -d -v mydata:/var/lib/mysql mysql

# Bind mount (maps a host path directly into the container)
docker run -d -v /home/user/app:/app myapp

# Bind mount using --mount syntax (more explicit and readable)
docker run -d \
  --mount type=bind,source=/home/user/app,target=/app \
  myapp

# Read-only bind mount (container cannot write to the path)
docker run -d \
  --mount type=bind,source=/etc/config,target=/config,readonly \
  myapp

# tmpfs mount (in-memory only — data lost when container stops)
docker run -d \
  --mount type=tmpfs,destination=/tmp \
  myapp

# Named volume using --mount syntax
docker run -d \
  --mount type=volume,source=mydata,target=/data \
  myapp
```

### Volume vs Bind Mount

| Feature | Named Volume | Bind Mount |
|---|---|---|
| **Managed by** | Docker | Host OS |
| **Portability** | High | Low (host path must exist) |
| **Performance** | Better on Linux | Slightly slower on macOS/Windows |
| **Use case** | Databases, persistent app data | Dev hot-reload, config injection |
| **Backup** | `docker run --volumes-from` | Direct host filesystem access |

```bash
# Backup a named volume to a tar archive
docker run --rm \
  -v mydata:/data \
  -v $(pwd):/backup \
  ubuntu \
  tar cvf /backup/mydata-backup.tar /data

# Restore a volume from a tar archive
docker run --rm \
  -v mydata:/data \
  -v $(pwd):/backup \
  ubuntu \
  bash -c "cd /data && tar xvf /backup/mydata-backup.tar --strip 1"
```

---

## 8. Docker Compose

### Basic Commands

```bash
# Start all services defined in docker-compose.yml (detached)
docker compose up -d

# Start and rebuild images before starting
docker compose up -d --build

# Start a specific service only
docker compose up -d nginx

# Stop all services (containers remain, just stopped)
docker compose stop

# Stop and remove containers, networks (volumes preserved)
docker compose down

# Stop and remove everything including volumes (DESTRUCTIVE)
docker compose down -v

# Stop and remove everything including images
docker compose down --rmi all

# View logs for all services
docker compose logs

# Follow logs in real time
docker compose logs -f

# View logs for a specific service
docker compose logs -f api

# Restart a specific service
docker compose restart api

# Rebuild a specific service image
docker compose build api

# Pull latest images for all services
docker compose pull

# List running compose services
docker compose ps

# Run a one-off command in a service container
docker compose run --rm api python manage.py migrate

# Execute a command in a running service container
docker compose exec api bash

# Scale a service to N instances
docker compose up -d --scale worker=5

# Show resource usage
docker compose top

# Validate and view the effective compose config
docker compose config

# Show service dependencies
docker compose config --services
```

### docker-compose.yml — Annotated Example

```yaml
version: "3.9"

services:
  # ── Web Application ──────────────────────────────
  api:
    build:
      context: .           # Build from current directory
      dockerfile: Dockerfile.prod
    image: myapp:latest
    container_name: myapp-api
    restart: unless-stopped
    ports:
      - "8000:8000"        # host:container
    environment:
      - DATABASE_URL=postgresql://user:pass@db:5432/mydb
      - REDIS_URL=redis://cache:6379
    env_file:
      - .env               # Load additional env vars from file
    depends_on:
      db:
        condition: service_healthy   # Wait until DB passes health check
      cache:
        condition: service_started
    volumes:
      - ./app:/app         # Bind mount for hot-reload in dev
      - media:/app/media   # Named volume for uploads
    networks:
      - backend
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s
    deploy:
      resources:
        limits:
          cpus: "1.0"
          memory: 512M

  # ── PostgreSQL Database ───────────────────────────
  db:
    image: postgres:16-alpine
    container_name: myapp-db
    restart: unless-stopped
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: pass
      POSTGRES_DB: mydb
    volumes:
      - pgdata:/var/lib/postgresql/data   # Persist DB data
    networks:
      - backend
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U user -d mydb"]
      interval: 10s
      timeout: 5s
      retries: 5

  # ── Redis Cache ────────────────────────────────────
  cache:
    image: redis:7-alpine
    container_name: myapp-cache
    restart: unless-stopped
    command: redis-server --maxmemory 256mb --maxmemory-policy allkeys-lru
    ports:
      - "6379:6379"
    networks:
      - backend

  # ── Nginx Reverse Proxy ────────────────────────────
  nginx:
    image: nginx:alpine
    container_name: myapp-nginx
    restart: unless-stopped
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/nginx.conf:ro
      - ./certbot/conf:/etc/letsencrypt:ro
    depends_on:
      - api
    networks:
      - backend
      - frontend

# ── Named Volumes ─────────────────────────────────────
volumes:
  pgdata:
  media:

# ── Networks ──────────────────────────────────────────
networks:
  backend:
    driver: bridge
  frontend:
    driver: bridge
```

---

## 9. Dockerfile Instructions

### Complete Dockerfile Reference

```dockerfile
# ── FROM — Base image (must be first instruction) ──────────────────────
FROM node:20-alpine

# Multi-stage build: name the first stage "builder"
FROM node:20-alpine AS builder


# ── ARG — Build-time variables (not available at runtime) ──────────────
ARG NODE_ENV=production
ARG APP_VERSION=1.0.0

# Use an ARG value
RUN echo "Building version $APP_VERSION"


# ── ENV — Runtime environment variables ─────────────────────────────────
ENV PORT=3000
ENV NODE_ENV=production
ENV APP_HOME=/app


# ── WORKDIR — Set working directory (creates it if not exists) ──────────
WORKDIR /app


# ── COPY — Copy files from build context into image ─────────────────────
# Copy a single file
COPY package.json .

# Copy multiple files
COPY package.json package-lock.json ./

# Copy everything from current directory
COPY . .

# Copy from a named build stage (multi-stage builds)
COPY --from=builder /app/dist ./dist

# Copy with specific ownership
COPY --chown=node:node . .


# ── ADD — Like COPY but also handles URLs and .tar auto-extraction ───────
ADD https://example.com/file.tar.gz /tmp/
# Prefer COPY over ADD unless you need these extra features


# ── RUN — Execute a command during the image build ───────────────────────
RUN npm install

# Chain commands to reduce layers
RUN apt-get update && \
    apt-get install -y curl vim && \
    rm -rf /var/lib/apt/lists/*

# Run as a specific user
RUN --mount=type=cache,target=/root/.npm \
    npm ci --only=production


# ── EXPOSE — Document which port the container listens on ───────────────
# This is metadata only — it does NOT actually publish the port
EXPOSE 3000
EXPOSE 3000/tcp
EXPOSE 53/udp


# ── USER — Switch to a non-root user ────────────────────────────────────
# Create the user first
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser

# Use numeric UID (more portable)
USER 1001


# ── VOLUME — Declare a mount point ──────────────────────────────────────
VOLUME ["/data"]
VOLUME /logs /uploads


# ── CMD — Default command to run when the container starts ───────────────
# Exec form (preferred — no shell, process gets signals directly)
CMD ["node", "server.js"]

# Shell form (runs via /bin/sh -c)
CMD node server.js

# Only ONE CMD allowed — last one wins


# ── ENTRYPOINT — Makes the container behave like an executable ──────────
ENTRYPOINT ["node", "server.js"]

# ENTRYPOINT + CMD pattern:
# ENTRYPOINT sets the fixed executable
# CMD provides default arguments (can be overridden at runtime)
ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["nginx", "-g", "daemon off;"]


# ── HEALTHCHECK — How Docker checks if the container is healthy ──────────
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:3000/health || exit 1

# Disable health check inherited from base image
HEALTHCHECK NONE


# ── LABEL — Add metadata to the image ────────────────────────────────────
LABEL maintainer="piyalidas.it@gmail.com"
LABEL version="1.0.0"
LABEL description="My production app"
LABEL org.opencontainers.image.source="https://github.com/org/repo"


# ── SHELL — Change the default shell used for RUN commands ───────────────
SHELL ["/bin/bash", "-c"]
# Now RUN commands use bash instead of sh


# ── STOPSIGNAL — Signal sent to stop the container ───────────────────────
STOPSIGNAL SIGTERM


# ── ONBUILD — Triggers when this image is used as a base image ──────────
ONBUILD COPY . /app
ONBUILD RUN npm install
```

### Multi-Stage Build Example (Node.js)

```dockerfile
# Stage 1: Build
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build          # outputs to /app/dist

# Stage 2: Production image (much smaller — no dev deps, no source)
FROM node:20-alpine AS production
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
COPY package.json .
USER node
EXPOSE 3000
CMD ["node", "dist/server.js"]
```

---

## 10. Registry & Hub

```bash
# Login to Docker Hub
docker login

# Login to a private registry
docker login registry.mycompany.com

# Login with username and password (non-interactive)
docker login -u myuser -p mypassword registry.mycompany.com

# Logout
docker logout
docker logout registry.mycompany.com

# Push an image to Docker Hub
docker push myusername/myapp:latest

# Push to a private registry
docker push registry.mycompany.com/myapp:1.0.0

# Search Docker Hub for an image
docker search nginx

# Search with filter (official images only)
docker search --filter is-official=true nginx

# Search and limit results
docker search --limit 5 nginx
```

---

## 11. Build — Advanced

```bash
# Basic build (from current directory)
docker build .

# Build and tag
docker build -t myapp:latest .

# Build from a specific Dockerfile
docker build -f Dockerfile.prod -t myapp:prod .

# Pass build arguments
docker build --build-arg NODE_ENV=production -t myapp .

# No cache (always rebuilds from scratch)
docker build --no-cache -t myapp .

# Set memory limit during build
docker build --memory 2g -t myapp .

# Multi-platform build (requires BuildKit)
docker buildx build --platform linux/amd64,linux/arm64 -t myapp:multi .

# Build and push in one step
docker buildx build --platform linux/amd64 -t myapp:latest --push .

# Build a specific stage only (multi-stage)
docker build --target builder -t myapp:builder .

# Build with secrets (securely pass sensitive data without baking into image)
docker build --secret id=mysecret,src=./secret.txt -t myapp .

# Enable BuildKit (faster builds, better caching)
DOCKER_BUILDKIT=1 docker build -t myapp .

# Squash all layers into one (reduces image size)
docker build --squash -t myapp .

# Show build output verbosely
docker build --progress=plain -t myapp .
```

---

## 12. Docker System Cleanup

```bash
# Show disk usage breakdown
docker system df

# Show detailed disk usage
docker system df -v

# Remove ALL unused data (containers, images, networks, volumes)
# ⚠ This is destructive — use carefully in production
docker system prune

# Remove ALL unused data including volumes
docker system prune -a --volumes

# Prune without confirmation prompt
docker system prune -f

# Remove only stopped containers
docker container prune

# Remove only unused images
docker image prune        # dangling only
docker image prune -a     # all unused

# Remove only unused volumes
docker volume prune

# Remove only unused networks
docker network prune

# Remove specific old containers (older than 24 hours)
docker container prune --filter "until=24h"

# Remove images older than a week
docker image prune -a --filter "until=168h"
```

---

## 13. Docker Stats & Monitoring

```bash
# Live resource usage stats for all running containers
docker stats

# Stats for a specific container
docker stats mycontainer

# One-time snapshot (no live refresh)
docker stats --no-stream

# Custom format output
docker stats --format "table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}\t{{.NetIO}}"

# Show running processes inside a container (like top)
docker top mycontainer

# Show processes with custom ps options
docker top mycontainer aux

# Get container PID on host
docker inspect --format '{{.State.Pid}}' mycontainer
```

---

## 14. Docker Swarm

Docker Swarm is Docker's native container orchestration tool (lighter than Kubernetes).

```bash
# Initialise a Swarm on the current node (becomes manager)
docker swarm init

# Initialise with a specific advertised IP
docker swarm init --advertise-addr 192.168.1.10

# Get the join token for worker nodes
docker swarm join-token worker

# Get the join token for manager nodes
docker swarm join-token manager

# Join a Swarm as a worker
docker swarm join --token <SWMTKN-...> 192.168.1.10:2377

# Leave the Swarm (on a worker node)
docker swarm leave

# Force leave (on a manager node)
docker swarm leave --force

# List all nodes in the Swarm
docker node ls

# Inspect a node
docker node inspect mynode

# Promote a worker to manager
docker node promote myworker

# Demote a manager to worker
docker node demote mymanager

# Deploy a stack (compose file) to the Swarm
docker stack deploy -c docker-compose.yml mystack

# List running stacks
docker stack ls

# List services in a stack
docker stack services mystack

# List tasks (containers) in a stack
docker stack ps mystack

# Remove a stack
docker stack rm mystack

# Create a service
docker service create --name web --replicas 3 -p 80:80 nginx

# List services
docker service ls

# Inspect a service
docker service inspect web

# Scale a service
docker service scale web=5

# Update a service (rolling update)
docker service update --image nginx:1.25 web

# View service logs
docker service logs web
docker service logs -f web

# Remove a service
docker service rm web
```

---

## 15. Security & Permissions

```bash
# Run as a non-root user
docker run --user 1001:1001 myapp

# Run with read-only root filesystem
docker run --read-only myapp

# Drop ALL Linux capabilities, then add only what's needed
docker run --cap-drop ALL --cap-add NET_BIND_SERVICE myapp

# Prevent privilege escalation (container cannot gain more privileges than its user)
docker run --security-opt no-new-privileges myapp

# Use a custom seccomp profile to restrict syscalls
docker run --security-opt seccomp=/path/to/seccomp.json myapp

# Use AppArmor profile
docker run --security-opt apparmor=docker-default myapp

# Scan an image for vulnerabilities (requires Docker Scout)
docker scout cves nginx:latest

# Check image SBOM (Software Bill of Materials)
docker scout sbom nginx:latest

# Scan with Trivy (popular open-source scanner)
# trivy image nginx:latest

# Run container with limited PIDs (prevents fork bombs)
docker run --pids-limit 100 myapp

# Limit /dev/shm size
docker run --shm-size 128m myapp

# Set ulimits
docker run --ulimit nofile=1024:1024 myapp
```

---

## 16. Real-World Recipes

### Run a PostgreSQL database locally

```bash
docker run -d \
  --name postgres \
  -e POSTGRES_USER=admin \
  -e POSTGRES_PASSWORD=secret \
  -e POSTGRES_DB=mydb \
  -p 5432:5432 \
  -v pgdata:/var/lib/postgresql/data \
  --restart unless-stopped \
  postgres:16-alpine
```

### Run Redis with persistence

```bash
docker run -d \
  --name redis \
  -p 6379:6379 \
  -v redis-data:/data \
  --restart unless-stopped \
  redis:7-alpine \
  redis-server --appendonly yes --requirepass mysecretpassword
```

### Run Nginx as a reverse proxy

```bash
docker run -d \
  --name nginx \
  -p 80:80 \
  -p 443:443 \
  -v $(pwd)/nginx.conf:/etc/nginx/nginx.conf:ro \
  -v $(pwd)/certs:/etc/ssl/certs:ro \
  --restart unless-stopped \
  nginx:alpine
```

### Run a Node.js app in development with hot reload

```bash
docker run -it --rm \
  -v $(pwd):/app \
  -w /app \
  -p 3000:3000 \
  -e NODE_ENV=development \
  node:20-alpine \
  sh -c "npm install && npm run dev"
```

### Run a one-off database migration

```bash
docker run --rm \
  --network myapp_backend \
  -e DATABASE_URL=postgresql://user:pass@db:5432/mydb \
  myapp:latest \
  python manage.py migrate
```

### Copy a database dump into a container and restore

```bash
# Copy dump to container
docker cp backup.sql mypostgres:/tmp/backup.sql

# Restore inside the container
docker exec -it mypostgres \
  psql -U admin -d mydb -f /tmp/backup.sql
```

### Check what's eating disk space

```bash
docker system df -v
docker images --format "{{.Size}}\t{{.Repository}}:{{.Tag}}" | sort -hr | head -20
```

### Get a shell in a crashed container (start with different entrypoint)

```bash
docker run --rm -it --entrypoint sh myapp:latest
```

### Debug a container using a sidecar

```bash
# Attach a debug container that shares the same network namespace
docker run -it --rm \
  --network container:myapp \
  nicolaka/netshoot \
  bash
# Now you can run curl, nmap, tcpdump etc. against myapp's network
```

### Watch Docker events in real time (useful for CI debugging)

```bash
docker events --format '{{.Time}} {{.Type}} {{.Action}} {{.Actor.Attributes.name}}'
```

---

## Quick Reference Card

```
Image Commands                Container Commands           Network & Volume
─────────────────────         ────────────────────         ─────────────────────────
docker pull <img>             docker run <img>             docker network ls
docker images                 docker ps                    docker network create
docker build -t <tag> .       docker ps -a                 docker network inspect
docker push <img>             docker start <ctr>           docker volume ls
docker rmi <img>              docker stop <ctr>            docker volume create
docker tag <img> <new>        docker restart <ctr>         docker volume inspect
docker history <img>          docker rm <ctr>              docker volume rm
docker inspect <img>          docker exec -it <ctr> bash   docker volume prune
docker save <img> > f.tar     docker logs -f <ctr>
docker load < f.tar           docker inspect <ctr>         Compose Commands
docker image prune -a         docker cp src <ctr>:dst      ─────────────────────────
                              docker stats                 docker compose up -d
System                        docker top <ctr>             docker compose down
─────────────────────         docker diff <ctr>            docker compose logs -f
docker version                docker port <ctr>            docker compose ps
docker info                   docker kill <ctr>            docker compose exec svc sh
docker system df              docker pause <ctr>           docker compose build
docker system prune -a        docker unpause <ctr>         docker compose pull
docker events                                              docker compose restart svc
```

---

*Related: Dockerfile best practices, Docker Compose, Kubernetes, Container Security, CI/CD Pipelines*
