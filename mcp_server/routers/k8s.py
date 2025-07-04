from fastapi import APIRouter, Depends, Query
from mcp_server.auth.apikey import get_api_key
import subprocess
import os

router = APIRouter()


@router.get("/k8s_apply")
def k8s_apply(
    file: str = Query(..., description="Path to Kubernetes YAML manifest"),
    api_key: str = Depends(get_api_key),
):
    try:
        full_path = os.path.abspath(f"/app/{file}")
        if not os.path.exists(full_path):
            return {"success": False, "error": f"File not found: {full_path}"}

        cmd = ["kubectl", "apply", "-f", full_path]
        result = subprocess.run(cmd, capture_output=True, text=True)
        return {
            "success": result.returncode == 0,
            "stdout": result.stdout,
            "stderr": result.stderr,
        }
    except Exception as e:
        return {"success": False, "error": str(e)}
