# Docker Compose
Docker Compose is a powerful tool designed to define and run multi-container applications using a single YAML configuration file. Instead of manually running multiple docker run commands for each part of your app (like a web server and a database), Compose orchestrates them as a unified "stack".

Compose simplifies the control of your entire application stack, making it easy to manage services, networks, and volumes in a single YAML configuration file. Then, with a single command, you create and start all the services from your configuration file.

Compose works in all environments - production, staging, development, testing, as well as CI workflows. 

**It also has commands for managing the whole lifecycle of your application:**
- Start, stop, and rebuild services
- View the status of running services
- Stream the log output of running services
- Run a one-off command on a service

**Key benefits of Docker Compose**
- Single Configuration: All services (containers), networks, and volumes are defined in one file, typically named docker-compose.yml or compose.yaml.
- Service Communication: Compose automatically creates a shared network. Containers can talk to each other using their service names (e.g., a backend can reach a database at db:5432).
- Dependency Management: You can use the depends_on tag to ensure services start in a specific order (e.g., the database starts before the application).
- One-Command Operations: Use docker compose up to build and start everything at once, and docker compose down to stop and remove all related resources

## Key commands
1. To start all the services defined in your compose.yaml file:
```
docker compose up
```
The docker compose up command starts the frontend and backend services, creates the necessary networks and volumes, and injects the configuration and secret into the frontend service.

2. To stop and remove the running services:
```
docker compose down
```

3. If you want to monitor the output of your running containers and debug issues, you can view the logs with:
```
docker compose logs
```

4. To list all the services along with their current status:
```
docker compose ps
```



