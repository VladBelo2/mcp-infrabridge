#!/bin/bash
set -e

COMPOSE_FILE="docker/docker-compose.yml"
PROJECT_NAME="mcp"

echo "[🧹] Stopping and cleaning old containers..."
docker compose -f "$COMPOSE_FILE" -p "$PROJECT_NAME" down --volumes --remove-orphans

echo "[🔧] Rebuilding and launching MCP server..."
docker compose -f "$COMPOSE_FILE" -p "$PROJECT_NAME" up --build --force-recreate
