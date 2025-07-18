#!/bin/bash
set -eu

# Build Docker image
echo "Building Docker image..."
docker build -t fastapi-products .

# Stop and remove running container if exists
if docker ps -a --format '{{.Names}}' | grep -Eq '^fastapi-products-api$'; then
  echo "Removing existing container..."
  docker rm -f fastapi-products-api
fi

# Start new container
echo "Starting FastAPI products API container..."
docker run -d --name fastapi-products-api -p 8000:8000 fastapi-products
sleep 2

# Check status
docker ps | grep fastapi-products-api && echo "Container started successfully."
