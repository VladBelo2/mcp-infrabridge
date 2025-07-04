#!/usr/bin/env bash
set -e

# Verify kubectl is functional
if kubectl version --client &>/dev/null; then
  echo "[INFO] 🧭 kubectl available: $(kubectl version --client=true --output=yaml | grep gitVersion)"
else
  echo "[ERROR] ❌ kubectl not found or not working"
fi

# Launch MCP server
echo "[INFO] 🚀 Starting MCP API server..."
exec uvicorn mcp_server.main:app --host 0.0.0.0 --port 8000
