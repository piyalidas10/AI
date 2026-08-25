
# Docker
https://docs.docker.com/reference/cli/docker/

## Find out what is using the space:
The docker system df command displays information regarding the amount of disk space used by the Docker daemon.
```
docker system df
```
https://docs.docker.com/reference/cli/docker/system/df/

TYPE                TOTAL               ACTIVE              SIZE                RECLAIMABLE
Images              5                   2                   16.43 MB            11.63 MB (70%)
Containers          2                   0                   212 B               212 B (100%)
Local Volumes       2                   1                   36 B                0 B (0%)

## Remove build cache
Remove build cache
```
docker builder prune
```
https://docs.docker.com/reference/cli/docker/builder/prune/

## How to remove old and unused Docker images
```
docker image prune -a
```
(more precise than docker system prune)

It will remove dangling and unused images. Warning: 'unused' means "images not referenced by any container": be careful before using -a.

Then check if the disk space for images has shrunk accordingly.
