# Docker
Docker is an OS‑level virtualization (or containerization) platform, which allows applications to share the host OS kernel instead of running a separate guest OS like in traditional virtualization. This design makes Docker containers lightweight, fast, and portable, while keeping them isolated from one another.

[Docker Docs](https://docs.docker.com/reference/cli/docker/)

## How Docker Containers Differ from Virtual Machines
Before Docker, deploying applications across different environments was a nightmare. Differences in dependencies, library versions, and OS configurations led to the infamous “works on my machine” problem.
<img width="80%" alt="image" src="https://media.geeksforgeeks.org/wp-content/uploads/20260409180847988992/420047160.webp" />

## Docker solutions
Docker solves this by standardizing the runtime environment. By bundling the application code with its specific dependencies into a single unit, it ensures the software runs identically whether it’s on a developer's laptop, a test server, or a cloud cluster.
+ Portability: Runs anywhere in local machine, cloud, on‑prem servers.
+ Consistency: Same behavior in development, testing, and production.
+ Lightweight: No full OS per app; containers share the host kernel.
+ Scalability: Ideal for microservices and orchestrators like Kubernetes and Docker Swarm.
+ Efficiency: Starts in seconds, uses fewer system resources.

## 🧠 What the Docker daemon actually is

The Docker daemon is the core service that:
- Builds images
- Runs containers
- Manages networks & volumes
- Handles container lifecycle
👉 When you run any Docker command, you’re really talking to the daemon.

**1. 🚀 Running a container**
```
docker run nginx
```
👉 CLI → Docker daemon → creates & starts container

**2. 🏗️ Building an image**
```
docker build -t my-app .
```
👉 Daemon reads Dockerfile and builds the image

**3. 📦 Managing containers**
```
docker ps
docker stop container_id
docker rm container_id
```
👉 All handled by the daemon

**4. 🌐 Networking & volumes**
```
docker network create my-net
docker volume create my-vol
```
👉 Daemon manages infrastructure behind the scenes  

If the Docker daemon is NOT running, nothing works:
```
docker ps
```
You’ll get: "Cannot connect to the Docker daemon"

## 🔄 Docker Architecture (simple)
```
Docker CLI  --->  Docker Daemon (dockerd)  --->  containerd  ---> containers
```
- CLI = what you type
- Daemon = brain
- containerd = low-level runtime

- Docker CLI = remote control
- Docker daemon = TV
- Containers = channels
👉 Without the TV (daemon), the remote does nothing.

## 🧠 Docker High-level architecture
```
Docker CLI  --->  REST API  --->  dockerd  --->  containerd  --->  runc  --->  Linux Kernel
```
Components:
- Docker CLI → your commands (docker run)
- dockerd (daemon) → orchestration brain
- containerd → container lifecycle manager
- runc → actually creates containers
- Linux kernel → isolation (namespaces + cgroups)

## Dockerfile
<img src="https://media.geeksforgeeks.org/wp-content/uploads/20260409110311942089/419253548.webp" width="80%" />
The Dockerfile uses DSL (Domain Specific Language) and contains instructions for generating a Docker image.
```
Docker Image → Blueprint (static, read only).
Docker Container → Running instance of that image (dynamic, executable)
```
- Docker image : A Docker Image is a file made up of multiple layers that contains the instructions to build and run a Docker container. It acts as an executable package that includes everything needed to run an application code, runtime, libraries, environment variables, and configurations.
- Docker container : A Docker Container is a lightweight, runnable instance of a Docker Image. It packages the application code together with all its dependencies and runs it in an isolated environment. Containers allow applications to run quickly and consistently across different environments — whether on a developer’s laptop, test servers, or production.

<img src="https://media.geeksforgeeks.org/wp-content/uploads/20260409110312041527/419253549.webp" width="80%" />
- Docker Hub : Docker Hub is a repository service and it is a cloud based service where people push their Docker Container Images and also pull the Docker Container Images from the Docker Hub anytime or anywhere via the internet.

## Why need to delete Docker Container before removing Docker Image?
You must delete a Docker container before its image because the container relies on that image as its base filesystem; as long as a container (even a stopped one) exists, it maintains a reference to the image layers, preventing their removal to avoid breaking the container's environment.

## FAQs
1. How do I delete all stopped containers in Docker?
To delete all stopped containers in Docker, use the following command:
```
docker compose down
```
This command will stop and remove all containers defined in your docker-compose.yml file and does not affect any other stopped containers. If you want to remove every stopped container, use:
```
docker container prune
```
2. What happens when I run docker system prune?
When you run **docker system prune**, Docker will remove all stopped containers and all networks not used by at least one container. Additionally, if you use the -a flag, Docker will also remove all unused images. This command is useful for freeing up disk space and cleaning up your Docker environment.

3. Can I remove a running Docker container?
Yes, you can remove a running Docker container using the **-f** flag with the **docker rm** command. This will force the removal of the container without stopping it first. Here’s an example:
```
docker rm -f <container_id>
```

4. How do I free up disk space used by Docker?
To free up disk space used by Docker, you can use the following commands:
- docker system prune -a to remove all unused images.
- docker system prune -a -v to remove all unused images and volumes.
- docker volume prune -a to remove all unused volumes.
- docker network prune -a to remove all unused networks.

5. What is the difference between docker rm and docker rmi?
**docker rm** is used to remove a container, while **docker rmi** is used to remove an image. **docker rm** will delete a container and its associated resources, but it will not delete the image that the container was based on. **docker rmi**, on the other hand, will delete an image, but it will not delete any containers that are based on that image.

6. How do I completely remove Docker images?
To completely remove a Docker image, use the following command:
```
docker rmi <image-id>
```
Replace <image-id> with the ID or name of the image. If the image is in use by a container, you must first remove the container before removing the image.

7. How do I remove unused Docker images?
Unused images (dangling and untagged) can be removed using the following command:
```
docker image prune
```
To remove all unused images, use the --all flag:
```
docker image prune --all
```

8. How do I clear all Docker images and cache?
To remove all Docker images, containers, volumes, and networks, use this command:
```
docker system prune --all --volumes
```
Note: This command will delete everything related to Docker, including all stopped containers and volumes.

9. How do I remove files from a Docker image?
You cannot directly modify a Docker image. Instead, create a new image without the unwanted files. Here’s how:

Start and login inside the container from the image:
```
docker run -it <image-id> /bin/bash
```
Now, remove files within the container as needed.

Next, commit the changes to a new image:
```
docker commit <container-id> <new-image-name>
```
Note: Using docker commit is generally discouraged for production workflows. The recommended approach is to update the Dockerfile to exclude unwanted files and rebuild the image. docker commit should be used only for quick experiments or debugging.

10. How do I remove old Docker containers?
To remove containers that have been inactive for a specified time, use the following:
```
docker ps -a --filter "status=exited" --filter "status=created"
docker rm $(docker ps -a -q --filter "status=exited" --filter "status=created")
```
This removes containers with **exited** or **created** status. Adjust the filter based on your needs.

11. Where are Docker images stored?
Docker keeps its images and container data in different places depending on the operating system and backend in use.

 - Linux:
    On Linux systems, Docker stores all image layers, containers, and related metadata under a single directory by default:
    ```
      /var/lib/docker
    ```
    The internal layout of this directory varies based on the storage driver configured on the host, such as overlay2 or containerd.

- macOS:
  When using Docker Desktop on macOS, Linux containers and images are stored inside a virtual disk file rather than directly on the host filesystem. This file is   typically found at:
  ```
    ~/Library/Containers/com.docker.docker/Data/vms/0/Docker.raw
    You can inspect or change where this disk image is stored from the Docker Desktop interface by navigating to: Settings -> Resources -> Advanced -> Disk image location
  ```

- Windows:

On Windows, Docker’s storage path depends on the container mode and backend:

Linux containers with WSL 2: Data is stored within the user profile at:
```
%USERPROFILE%\AppData\Local\Docker\wsl\data
```
Windows containers (windowsfilter driver): Image and container data reside under:
```
C:\ProgramData\docker\image
C:\ProgramData\docker\windowsfilter
```
Hyper-V backend (legacy): The storage directory is configurable during installation using the --hyper-v-default-data-root installer option.

You can verify the storage driver and path using:
```
docker info | grep "Docker Root Dir"
```

12. How do I remove a container when Docker is finished?
To automatically remove a container after it exits, use the --rm flag when starting the container:
```
docker run --rm <image-id>
```
This ensures the container is removed as soon as it stops.



