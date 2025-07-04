from fastapi import APIRouter, Depends, Query
from mcp_server.auth.apikey import get_api_key
import subprocess
import os

router = APIRouter()


@router.get("/docker_build")
def docker_build(
    path: str = Query(..., description="Relative path to Docker build context"),
    tag: str = Query("mcp/test-image:latest", description="Docker image tag to apply"),
    api_key: str = Depends(get_api_key),
):
    try:
        full_path = os.path.abspath(f"/app/{path}")
        if not os.path.exists(full_path):
            return {"success": False, "error": f"Path not found: {full_path}"}

        cmd = ["docker", "build", "-t", tag, full_path]
        result = subprocess.run(cmd, capture_output=True, text=True)
        return {
            "success": result.returncode == 0,
            "stdout": result.stdout,
            "stderr": result.stderr,
        }
    except Exception as e:
        return {"success": False, "error": str(e)}
