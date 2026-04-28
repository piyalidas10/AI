# Docker
Docker is an OS‑level virtualization (or containerization) platform, which allows applications to share the host OS kernel instead of running a separate guest OS like in traditional virtualization. This design makes Docker containers lightweight, fast, and portable, while keeping them isolated from one another.

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
