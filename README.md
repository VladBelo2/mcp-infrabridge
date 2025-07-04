# 🧠 MCP InfraBridge Server

![CI](https://github.com/vladbelo2/mcp-infrabridge/actions/workflows/ci.yml/badge.svg)

A lightweight, containerized **Model Context Protocol (MCP) Server** that acts as a secure DevOps gateway between LLMs and real-world infrastructure tools like Terraform, Ansible, Docker, and Kubernetes.

---

## 🌐 What It Does

This project enables external agents (like LLMs or scripts) to trigger infrastructure actions through a simple HTTP API.

> 🧠 "Run terraform plan" → `GET /tools/terraform_plan`  
> 🧠 "Ping with Ansible" → `GET /tools/ansible_ping`  
> 🧠 "Apply this K8s YAML" → `GET /tools/k8s_apply?file=...`  
> 🧠 "Build image from this Dockerfile" → `GET /tools/docker_build?...`

It securely exposes powerful DevOps tooling behind an API layer, making it easy to integrate into any automated or AI-powered workflow.

---

## 🚀 Features

- ✅ FastAPI-based HTTP API with OpenAPI docs (`/docs`)
- 🔐 API key-based auth via `X-API-Key` header
- ⚙️ Built-in support for:
  - Terraform
  - Ansible
  - Docker
  - Kubernetes
- 🐳 Runs fully inside Docker with optional K3s/Kubectl
- 📦 Modular architecture for easy extension
- 🧪 CI workflow: lint, test, build, curl-check

---

## 📦 Getting Started

```bash
git clone https://github.com/vladbelo2/mcp-server
cd mcp-server
./scripts/dev_rebuild.sh
```

Then open: http://localhost:8000/docs

Use any key from `.env` under `VALID_API_KEYS` to authenticate.

---

## 🔧 API Endpoints

| Method  |  Endpoint  |  Description |
|---------|------------|--------------|
| GET	  | /health    | Health check |
| GET	  | /tools/terraform_plan | Run terraform plan inside sample |
| GET	  | /tools/ansible_ping | Ping localhost with Ansible |
| GET	  | /tools/docker_build | Build Dockerfile from given path |
| GET	  | /tools/k8s_apply	| Apply K8s YAML using kubectl |

> ℹ️ Swagger UI available at /docs

---

## 🔐 Authentication

Set your valid keys in .env:
```bash
VALID_API_KEYS=supersecret123,another-key
```
Pass them via header:
```bash
-H "X-API-Key: supersecret123"
```

---

## 🧪 CI/CD Workflow

CI is handled via GitHub Actions:

- 🔍 Lint Python (Black + Ruff)
- 🐍 Check Python type safety (mypy)
- 🐳 Docker build test
- ✅ API test: curl /health, /tools/... via key

> See `.github/workflows/ci.yml`

---

## 📁 Project Structure

```text
mcp_server/
  ├── main.py             # FastAPI app entrypoint
  ├── routers/            # Terraform, Ansible, Docker, K8s routers
  ├── schemas/            # Typed response models
  └── auth/               # API key logic

docker/
  ├── Dockerfile          # Ubuntu-based production image
  └── entrypoint.sh       # Boot sequence for MCP

examples/
  ├── terraform_sample/   # main.tf example
  ├── k8s_sample/         # simple deployment.yaml
  └── docker_sample/      # alpine Dockerfile

scripts/
  └── dev_rebuild.sh      # One-click dev rebuild
```

---

## 🧠 Roadmap

- ✅ GET-only secured DevOps API
- 🔁 Add /run_tool unified endpoint
- 🧠 Add mcp_client.py to simulate agents calling the API
- 🔧 Add more tools: Git, Helm, systemd, AWS CLI, GCloud CLI
- 🧪 Add support for POST operations and payload validation
- 📊 Build frontend dashboard (optional)
- 🌍 Add external auth: OAuth2, JWT, user accounts

---

## 🤝 Contributions

This project is open to community contributions!
Feel free to fork, improve, and PR — or suggest features and integrations.

---

## 📜 License

MIT License © 2025 Vlad Belo