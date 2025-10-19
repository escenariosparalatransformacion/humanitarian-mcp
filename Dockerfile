# Multi-stage build for Humanitarian Negotiation MCP

# Stage 1: Builder
FROM python:3.10-slim as builder

WORKDIR /build

# Copy requirements
COPY requirements_mcp.txt .

# Install dependencies to a specific directory
RUN pip install --user --no-cache-dir -r requirements_mcp.txt && \
    pip install --user --no-cache-dir fastapi uvicorn[standard]

# Stage 2: Runtime
FROM python:3.10-slim

WORKDIR /app

# Copy Python packages from builder
COPY --from=builder /root/.local /root/.local

# Make sure scripts in .local are usable
ENV PATH=/root/.local/bin:$PATH
ENV PYTHONUNBUFFERED=1

# Copy application files
COPY humanitarian_negotiation_mcp.py .
COPY http_server.py .
COPY requirements_mcp.txt .

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Default to HTTP server (recommended)
# For MCP server only, change to: CMD ["python", "-u", "humanitarian_negotiation_mcp.py"]
CMD ["python", "-u", "http_server.py"]

# Metadata
LABEL maintainer="Humanitarian Negotiation MCP"
LABEL description="Universal REST API for humanitarian negotiation analysis"
LABEL version="1.0.0"
