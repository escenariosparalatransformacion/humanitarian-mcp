# Deploying as a Universal MCP Server

## 📌 Current Status

Tu MCP **ya es agnóstico a LLMs** porque usa `FastMCP`, que es parte del ecosistema MCP estándar de Anthropic. Sin embargo, aquí hay varias formas de hacerlo verdaderamente universal y accesible desde cualquier aplicación.

---

## 🎯 Opciones de Deployment

### Opción 1: MCP Server Estándar (Recomendado - Ya lo tienes)

Tu servidor actual ya es universal. Puede usarse con:

- ✅ **Claude Desktop** (ya configurado)
- ✅ **Claude Web** (próximamente)
- ✅ **Cline** (VSCode extension)
- ✅ **Continue** (IDE extension)
- ✅ **Cursor IDE**
- ✅ Cualquier cliente MCP compatible

**Configuración en otros clientes:**

```json
// Ejemplo para Cursor IDE, Continue, o Cline
{
  "mcpServers": {
    "humanitarian-negotiation": {
      "command": "python",
      "args": ["/ruta/absoluta/a/humanitarian_negotiation_mcp.py"]
    }
  }
}
```

---

### Opción 2: Servidor HTTP (Más Universal)

Expone el MCP como API REST para que cualquier aplicación lo use.

#### Pasos:

**1. Crear un wrapper HTTP:**

```python
# http_mcp_server.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import asyncio
import json
from humanitarian_negotiation_mcp import (
    create_island_of_agreement,
    analyze_icebergs,
    analyze_stakeholders,
    leverage_stakeholder_influence,
    get_negotiation_guide
)

app = FastAPI(
    title="Humanitarian Negotiation MCP API",
    description="Universal REST API for humanitarian negotiation analysis",
    version="1.0.0"
)

# Enable CORS for universal access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check
@app.get("/health")
async def health():
    return {"status": "ok", "service": "humanitarian-negotiation-mcp"}

# Tool endpoints
@app.post("/tools/island-of-agreement")
async def api_island_of_agreement(request: dict):
    try:
        result = create_island_of_agreement(
            situation_description=request.get("situation_description"),
            organization_name=request.get("organization_name"),
            counterpart_name=request.get("counterpart_name"),
            additional_context=request.get("additional_context"),
            response_format=request.get("response_format", "markdown"),
            detail_level=request.get("detail_level", "detailed")
        )
        return {"success": True, "data": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/tools/analyze-icebergs")
async def api_analyze_icebergs(request: dict):
    try:
        result = analyze_icebergs(
            organization_positions=request.get("organization_positions", []),
            organization_reasoning=request.get("organization_reasoning", []),
            organization_motives=request.get("organization_motives", []),
            counterpart_positions=request.get("counterpart_positions", []),
            counterpart_reasoning=request.get("counterpart_reasoning", []),
            counterpart_motives=request.get("counterpart_motives", []),
            response_format=request.get("response_format", "markdown"),
            detail_level=request.get("detail_level", "detailed")
        )
        return {"success": True, "data": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/tools/analyze-stakeholders")
async def api_analyze_stakeholders(request: dict):
    try:
        result = analyze_stakeholders(
            context=request.get("context"),
            stakeholders=request.get("stakeholders", []),
            response_format=request.get("response_format", "markdown"),
            detail_level=request.get("detail_level", "detailed")
        )
        return {"success": True, "data": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/tools/leverage-influence")
async def api_leverage_influence(request: dict):
    try:
        result = leverage_stakeholder_influence(
            target_stakeholder_name=request.get("target_stakeholder_name"),
            stakeholders_analysis_json=request.get("stakeholders_analysis_json"),
            response_format=request.get("response_format", "markdown")
        )
        return {"success": True, "data": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/tools/guide")
async def api_guide():
    try:
        result = get_negotiation_guide()
        return {"success": True, "data": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Tool discovery endpoint
@app.get("/tools")
async def list_tools():
    return {
        "tools": [
            {
                "name": "humanitarian_create_island_of_agreement",
                "description": "Creates IoA table with contested/agreed facts and convergent/divergent norms",
                "endpoint": "/tools/island-of-agreement"
            },
            {
                "name": "humanitarian_analyze_icebergs",
                "description": "Compares parties' positions, reasoning, and motives",
                "endpoint": "/tools/analyze-icebergs"
            },
            {
                "name": "humanitarian_analyze_stakeholders",
                "description": "Characterizes and prioritizes stakeholders",
                "endpoint": "/tools/analyze-stakeholders"
            },
            {
                "name": "humanitarian_leverage_stakeholder_influence",
                "description": "Develops tactics to influence target stakeholders",
                "endpoint": "/tools/leverage-influence"
            },
            {
                "name": "humanitarian_negotiation_guide",
                "description": "Comprehensive guide to all methodologies",
                "endpoint": "/tools/guide"
            }
        ]
    }

if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        log_level="info"
    )
```

**2. Instalar dependencias adicionales:**

```bash
pip install fastapi uvicorn
```

**3. Ejecutar el servidor:**

```bash
python http_mcp_server.py
```

**4. El servidor estará disponible en:**
- Local: `http://localhost:8000`
- Documentación interactiva: `http://localhost:8000/docs`

---

### Opción 3: Docker Container (Máxima Portabilidad)

Para que cualquiera pueda ejecutar tu MCP en cualquier sistema.

**1. Crear Dockerfile:**

```dockerfile
FROM python:3.10-slim

WORKDIR /app

# Copy requirements
COPY requirements_mcp.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements_mcp.txt

# Copy MCP server
COPY humanitarian_negotiation_mcp.py .

# Expose port for HTTP server
EXPOSE 8000

# Run the MCP server
CMD ["python", "humanitarian_negotiation_mcp.py"]

# Alternative: Run HTTP wrapper
# CMD ["python", "http_mcp_server.py"]
```

**2. Crear .dockerignore:**

```
__pycache__
*.pyc
*.pyo
.pytest_cache
.git
.gitignore
*.md
.env
```

**3. Construir la imagen:**

```bash
docker build -t humanitarian-negotiation-mcp:1.0 .
```

**4. Ejecutar el contenedor:**

```bash
# Opción 1: MCP directo (con stdout)
docker run -it humanitarian-negotiation-mcp:1.0

# Opción 2: HTTP server
docker run -p 8000:8000 humanitarian-negotiation-mcp:1.0
```

---

### Opción 4: Publicar en Package Repository

Para máxima distribución: PyPI, conda, etc.

**1. Estructura del proyecto:**

```
humanitarian-negotiation-mcp/
├── src/
│   └── humanitarian_negotiation_mcp/
│       ├── __init__.py
│       ├── server.py
│       └── http_wrapper.py
├── setup.py
├── pyproject.toml
├── requirements.txt
└── README.md
```

**2. setup.py:**

```python
from setuptools import setup, find_packages

setup(
    name="humanitarian-negotiation-mcp",
    version="1.0.0",
    description="MCP server for humanitarian negotiation analysis",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/humanitarian-negotiation-mcp",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.10",
    install_requires=[
        "anthropic>=0.18.0",
        "mcp>=0.9.0",
        "pydantic>=2.0.0",
        "httpx>=0.24.0",
        "python-dateutil>=2.8.0",
    ],
    entry_points={
        "console_scripts": [
            "humanitarian-mcp=humanitarian_negotiation_mcp.server:main",
            "humanitarian-mcp-http=humanitarian_negotiation_mcp.http_wrapper:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
    ],
)
```

**3. Publicar en PyPI:**

```bash
pip install build twine
python -m build
twine upload dist/*
```

**Uso después de publicar:**

```bash
pip install humanitarian-negotiation-mcp
humanitarian-mcp  # Ejecuta el servidor directamente
```

---

### Opción 5: Integración con LLMs Específicos

Para usar directamente con APIs de LLMs (OpenAI, Anthropic, etc.)

**1. Cliente OpenAI con MCP:**

```python
from openai import OpenAI
import json

client = OpenAI(api_key="your-api-key")

# Define las herramientas MCP para OpenAI
tools = [
    {
        "type": "function",
        "function": {
            "name": "humanitarian_create_island_of_agreement",
            "description": "Creates IoA analysis with contested/agreed facts and convergent/divergent norms",
            "parameters": {
                "type": "object",
                "properties": {
                    "situation_description": {"type": "string"},
                    "organization_name": {"type": "string"},
                    "counterpart_name": {"type": "string"},
                    "additional_context": {"type": "string"},
                    "response_format": {"type": "string", "enum": ["markdown", "json"]},
                    "detail_level": {"type": "string", "enum": ["concise", "detailed"]}
                },
                "required": ["situation_description", "organization_name", "counterpart_name"]
            }
        }
    }
]

messages = [
    {
        "role": "user",
        "content": "Analyze this negotiation: UN agency negotiating with regional government..."
    }
]

response = client.chat.completions.create(
    model="gpt-4",
    messages=messages,
    tools=tools,
    tool_choice="auto"
)
```

---

## 🚀 Recomendación: Camino a Universal

Para maximizar alcance y compatibilidad, recomiendo esta secuencia:

### 1️⃣ Corto Plazo (Ya hecho)
- ✅ MCP estándar funcional
- ✅ Compatible con Claude Desktop
- ✅ Documentación clara

### 2️⃣ Mediano Plazo
- 📝 Crear versión HTTP con FastAPI
- 📝 Documentación Swagger/OpenAPI
- 📝 Ejemplos para múltiples clientes

### 3️⃣ Largo Plazo
- 📦 Publicar en PyPI
- 🐳 Docker container
- 🌐 Hosting en nube (AWS Lambda, Google Cloud Run, etc.)

---

## 🔗 Cómo Usar en Diferentes Plataformas

### Claude Desktop ✅ (Ya configurado)
```json
{
  "mcpServers": {
    "humanitarian-negotiation": {
      "command": "python",
      "args": ["/ruta/a/humanitarian_negotiation_mcp.py"]
    }
  }
}
```

### Cline (VSCode)
Añade la misma configuración a `.cline/mcp-config.json`

### Continue IDE
```json
{
  "contextProviders": [
    {
      "name": "mcp",
      "params": {
        "mcpServers": {
          "humanitarian-negotiation": {
            "command": "python",
            "args": ["/ruta/a/humanitarian_negotiation_mcp.py"]
          }
        }
      }
    }
  ]
}
```

### Cursor IDE
Stalkear la configuración de Claude Desktop (usa el mismo archivo)

### API REST (Tu propia app)
```bash
curl -X POST http://localhost:8000/tools/island-of-agreement \
  -H "Content-Type: application/json" \
  -d '{
    "situation_description": "...",
    "organization_name": "...",
    "counterpart_name": "..."
  }'
```

---

## 📊 Comparativa de Opciones

| Opción | Facilidad | Universalidad | Escalabilidad | Complejidad |
|--------|-----------|--------------|---------------|------------|
| MCP Estándar | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | Baja |
| HTTP API | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | Media |
| Docker | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | Media |
| PyPI | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | Alta |
| LLM Integration | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | Alta |

---

## 💡 Conclusión

Tu MCP **ya es agnóstico** y puede usarse con cualquier cliente compatible. Para hacerlo "verdaderamente universal":

1. **Inmediato**: Usa con Cline, Continue, Cursor
2. **Próxima semana**: Crea wrapper HTTP
3. **Este mes**: Publica en PyPI y crea Docker image
4. **Largo plazo**: Hospédalo en nube como servicio

¿Quieres que implemente alguna de estas opciones?
