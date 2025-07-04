from pydantic import BaseModel

class TerraformPlanResponse(BaseModel):
    success: bool
    stdout: str
    stderr: str | None = None

class AnsiblePingResponse(BaseModel):
    success: bool
    stdout: str
    stderr: str | None = None
