# Dockerfile

Complete Dockerfile

For the example in your transcript, it would look like:
```
FROM node

WORKDIR /app

COPY . /app

RUN npm install

EXPOSE 80

CMD ["node", "server.js"]
```

## 1. FROM — choose a base image
```
FROM node
```
Your custom image starts from the existing node image.

Think of it as:
```
Node.js image → your custom image
```
You could also specify a version, which is generally better for reproducibility:
```
FROM node:20
```

## 2. WORKDIR — define the application directory
```
WORKDIR /app
```
This tells Docker:

From this point onward, treat /app as the working directory.

So commands such as npm install and node server.js execute inside /app.

## 3. COPY — copy your application into the image
```
COPY . /app
```
This means:
```
Local machine
    │
    │ COPY
    ▼
Docker image
    /app
       ├── package.json
       ├── package-lock.json
       ├── server.js
       └── ...
```
The first . means the current build context.

The /app is the destination inside the image.

## 4. RUN — execute something while building the image
```
RUN npm install
```
This happens during image creation.

So:
```
docker build
      │
      ├── FROM node
      ├── WORKDIR /app
      ├── COPY . /app
      ├── RUN npm install   ← happens now
      │
      ▼
   Docker Image
```
The dependencies become part of the image.

## 5. EXPOSE — document the application's port

For example, if your Node.js application listens on port 80:
```
EXPOSE 80
```
Important: EXPOSE does not actually publish the port to your host machine. It documents which port the containerized application expects to use.

You still need port mapping when running the container:
```
docker run -p 8080:80 my-node-app
```
Meaning:
```
Your Windows machine          Docker container
       │                              │
       │  localhost:8080              │
       └─────────────────────────────►│ port 80
                                      │
                                  Node.js
```

## 6. CMD — what happens when the container starts
```
CMD ["node", "server.js"]
```
This is different from RUN.

RUN:
```
RUN npm install
```
→ executes when the image is built

CMD:
```
CMD ["node", "server.js"]
```
→ executes when a container is started

This distinction is extremely important.

## The overall mental model
```
                  docker build
                       │
                       ▼
              ┌─────────────────┐
              │   Dockerfile    │
              └────────┬────────┘
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
     FROM           COPY/RUN        EXPOSE
        │              │              │
        └──────────────┼──────────────┘
                       ▼
               ┌───────────────┐
               │ Docker Image  │
               │ my-node-app   │
               └───────┬───────┘
                       │
                  docker run
                       │
                       ▼
               ┌───────────────┐
               │   Container   │
               │               │
               │ node server.js│
               │     :80       │
               └───────┬───────┘
                       │
                 -p 8080:80
                       │
                       ▼
                 localhost:8080
```
One correction to the transcript: COPY does not become relative to WORKDIR in the way described there. WORKDIR affects subsequent RUN, CMD, and ENTRYPOINT instructions; 
for clarity and correctness, COPY . /app is the better form when you explicitly want to copy into /app.

Also, in a real project, I would usually add a .dockerignore so things such as node_modules, .git, logs, 
and build artifacts aren't unnecessarily copied into the Docker build context.

-------------------------

# Docker workflow: Dockerfile → Image → Container → Port Mapping

The most important thing to understand is that EXPOSE and -p are different.

For run the Docker file, open terminal or cmd inside the path where Dockerfile is kept.
```
# Build image
docker build -t my-node-app .

# See images
docker images

# Run container
docker run -p 3000:80 my-node-app

# See running containers
docker ps

# See all containers
docker ps -a

# Stop container
docker stop <container-name-or-id>
```

## 1. Build the image

**From the folder containing your Dockerfile:**
```
docker build .
```
Docker reads the Dockerfile and creates an image.

**A better practice is to give the image a name:**
```
docker build -t my-node-app .
```

Here:
- docker build → create an image
- -t my-node-app → give the image a name/tag
- . → Docker build context is the current directory

**You can verify it:**
```
docker images
```

## 2. Run a container from the image
```
docker run my-node-app
```
This creates a new container from my-node-app.

**If your Dockerfile contains:**
```
CMD ["node", "server.js"]
```

**then Docker executes:**
```
node server.js
```
inside the container.

Because the Node server keeps running, the container also keeps running.

## 3. Why EXPOSE 80 doesn't make localhost work

Suppose your application listens on:
```
Container
    │
    └── Node.js → port 80
```
And your Dockerfile contains:
```
EXPOSE 80
```
That doesn't mean:
```
Your PC → localhost:80 → Container:80
```
EXPOSE is primarily metadata/documentation saying:

This containerized application expects to use port 80.

## 4. Use -p to publish the port

You need:
```
docker run -p 3000:80 my-node-app
```
The syntax is:
```
-p HOST_PORT:CONTAINER_PORT
```
So:
```
-p 3000:80
   │    │
   │    └── port inside container
   │
   └─────── port on your machine
```
The resulting flow is:
```
Browser
   │
   │ http://localhost:3000
   ▼
Windows machine
   │
   │ port 3000
   ▼
Docker
   │
   │ port mapping
   ▼
Container
   │
   │ port 80
   ▼
Node.js server
```
This is why you can access:
```
http://localhost:3000
```
even though Node is listening on port 80 inside the container.

## 5. Check running containers
```
docker ps
```
This shows only running containers.

**For example:**
```
CONTAINER ID   IMAGE          PORTS
abc123         my-node-app    0.0.0.0:3000->80/tcp
```

**The important part is:**
```
3000->80
```

**It means:**
```
Host 3000 → Container 80
```

## 6. Stop the container

Find the container:
```
docker ps
```
Then:
```
docker stop abc123
```
You can use either the container ID or container name.

## 7. See stopped containers

After stopping it:
```
docker ps
```
may show nothing.

That's because docker ps only shows running containers.

Use:
```
docker ps -a
```
Now you'll see both running and stopped containers.


| Docker concept | Purpose                                          |
| -------------- | ------------------------------------------------ |
| `Dockerfile`   | Instructions for creating an image               |
| `docker build` | Creates an image                                 |
| Image          | Template/blueprint                               |
| `docker run`   | Creates and starts a container                   |
| Container      | Running instance of an image                     |
| `EXPOSE 80`    | Documents intended container port                |
| `-p 3000:80`   | Actually maps host port 3000 → container port 80 |
| `docker stop`  | Stops a running container                        |
| `docker ps`    | Shows running containers                         |
| `docker ps -a` | Shows all containers                             |

The key mental model is:
> **Dockerfile → Image → Container**

And port publishing happens when you run the container, not when you build the image.

