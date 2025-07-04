# docker/Dockerfile
FROM ubuntu:22.04

# Set non-interactive frontend for clean installs
ENV DEBIAN_FRONTEND=noninteractive

# Update system and install dependencies
RUN apt-get update && apt-get install -y \
    python3 python3-pip python3-venv \
    curl gnupg unzip git iproute2 iptables \
    apt-transport-https ca-certificates lsb-release \
    docker.io ansible \
    && curl -fsSL https://apt.releases.hashicorp.com/gpg | gpg --dearmor -o /usr/share/keyrings/hashicorp.gpg \
    && echo "deb [signed-by=/usr/share/keyrings/hashicorp.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" > /etc/apt/sources.list.d/hashicorp.list \
    && apt-get update && apt-get install -y terraform \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install kubectl via official release (safer than relying on K3s)
RUN curl -LO "https://dl.k8s.io/release/$(curl -sL https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl" \
    && install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl \
    && rm kubectl

# Copy code and entrypoint
WORKDIR /app
COPY . /app
COPY docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Install Python dependencies (FastAPI, Uvicorn, etc.)
RUN pip3 install --upgrade pip && pip3 install -r requirements.txt

# Expose MCP API port
EXPOSE 8000

# Use custom entrypoint
ENTRYPOINT ["/entrypoint.sh"]
