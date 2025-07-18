#!/bin/bash
set -eu

./install.sh

if docker ps | grep -q fastapi-products-api; then
  echo "FastAPI Products API is running at http://localhost:8000"
else
  echo "Error: FastAPI Products API is not running." >&2
  exit 1
fi
