import subprocess
import os
from fastapi import APIRouter, Depends
from mcp_server.auth.apikey import get_api_key
from mcp_server.schemas.tool_schemas import TerraformPlanResponse

router = APIRouter()

EXAMPLES_DIR = "/app/examples/terraform_sample"


@router.get("/terraform_plan", response_model=TerraformPlanResponse)
def run_terraform_plan(api_key: str = Depends(get_api_key)):
    try:
        if not os.path.exists(f"{EXAMPLES_DIR}/main.tf"):
            return {
                "success": False,
                "error": "No Terraform config found in sample directory",
            }

        subprocess.run(
            ["terraform", "init"], cwd=EXAMPLES_DIR, check=True, capture_output=True
        )
        result = subprocess.run(
            ["terraform", "plan"], cwd=EXAMPLES_DIR, capture_output=True, text=True
        )

        return {
            "success": result.returncode == 0,
            "stdout": result.stdout,
            "stderr": result.stderr,
        }

    except subprocess.CalledProcessError as e:
        return {
            "success": False,
            "error": str(e),
            "stderr": e.stderr,
            "stdout": e.stdout,
        }
    except Exception as e:
        return {"success": False, "error": str(e)}
