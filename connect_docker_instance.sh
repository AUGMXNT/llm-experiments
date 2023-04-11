#!/bin/bash

# Check if the Docker container is running
container_id=$(docker ps --filter "name=llm-experiments" --format "{{.ID}}")
if [ -z "$container_id" ]; then
  echo "Starting Docker container..."
  docker-compose up -d
  container_id=$(docker ps --filter "name=llm-experiments" --format "{{.ID}}")
fi

# Display the container name
container_name=$(docker ps --filter "id=$container_id" --format "{{.Names}}")
echo "Container name: $container_name"

# Shell into the Docker instance with bash
docker exec -it $container_id bash
