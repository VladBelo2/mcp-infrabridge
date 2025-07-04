from fastapi import APIRouter, Depends
from mcp_server.auth.apikey import get_api_key
from mcp_server.schemas.tool_schemas import AnsiblePingResponse
import subprocess

router = APIRouter()

@router.get("/ansible_ping", response_model=AnsiblePingResponse)
def ansible_ping(api_key: str = Depends(get_api_key)):
    try:
        cmd = ["ansible", "localhost", "-m", "ping", "-i", "localhost,", "--connection", "local"]
        result = subprocess.run(cmd, capture_output=True, text=True)
        return {
            "success": result.returncode == 0,
            "stdout": result.stdout,
            "stderr": result.stderr
        }
    except Exception as e:
        return {"success": False, "error": str(e)}
