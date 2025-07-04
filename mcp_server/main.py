from fastapi import FastAPI
from mcp_server.routers import terraform, ansible, docker, k8s

app = FastAPI(
    title="MCP InfraBridge 🧠🔧",
    description="A secure MCP server to bridge LLMs to DevOps tools",
    version="0.1.0",
)


@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok"}


# Register tool routers
app.include_router(terraform.router, prefix="/tools", tags=["Terraform"])
app.include_router(ansible.router, prefix="/tools", tags=["Ansible"])
app.include_router(docker.router, prefix="/tools", tags=["Docker"])
app.include_router(k8s.router, prefix="/tools", tags=["Kubernetes"])
