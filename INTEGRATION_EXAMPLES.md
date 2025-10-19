# Integration Examples: Using the MCP with Different Clients

## 🎯 Overview

This document shows how to integrate the Humanitarian Negotiation MCP with various LLM clients and applications.

---

## 1. Claude Desktop (Claude)

**Status**: ✅ Already configured

**Configuration**: `claude_desktop_config.json`

```json
{
  "mcpServers": {
    "humanitarian-negotiation": {
      "command": "python",
      "args": ["C:\\Users\\Jhozman Camacho\\Downloads\\FACT Negotiator MCP\\humanitarian_negotiation_mcp.py"]
    }
  }
}
```

**Usage**: Simply chat with Claude - tools appear automatically in tool list.

---

## 2. Cline (VSCode Extension)

**Installation**: Install from VSCode marketplace

**Configuration**: Add to VSCode settings or `.cline/mcp-config.json`

```json
{
  "mcpServers": {
    "humanitarian-negotiation": {
      "command": "python",
      "args": ["C:\\path\\to\\humanitarian_negotiation_mcp.py"]
    }
  }
}
```

**Usage**: Use Cline chat - tools appear in suggestions.

---

## 3. Continue IDE (VSCode/JetBrains)

**Installation**: Install from VS Code marketplace or JetBrains plugins

**Configuration**: `.continuerc.json`

```json
{
  "models": [
    {
      "title": "Claude 3 Opus",
      "provider": "claude",
      "model": "claude-3-5-sonnet-20241022"
    }
  ],
  "contextProviders": [
    {
      "name": "codebase"
    },
    {
      "name": "mcp",
      "params": {
        "humanitarian-negotiation": {
          "command": "python",
          "args": ["C:\\path\\to\\humanitarian_negotiation_mcp.py"]
        }
      }
    }
  ]
}
```

**Usage**: Reference `@humanitarian-negotiation` in Continue chat.

---

## 4. Cursor IDE

**How it works**: Cursor uses Claude Desktop config automatically

**Configuration**: `%APPDATA%/Claude/claude_desktop_config.json`

Your existing configuration already works!

**Usage**: Same as Claude Desktop.

---

## 5. HTTP API (REST)

**Perfect for**: Web apps, mobile apps, custom integrations, or any HTTP client

### 5.1 Starting the HTTP Server

```bash
pip install fastapi uvicorn
python http_server.py
```

Server starts at `http://localhost:8000`

### 5.2 Using with cURL

```bash
# Get available tools
curl http://localhost:8000/tools

# Create Island of Agreement analysis
curl -X POST http://localhost:8000/api/v1/island-of-agreement \
  -H "Content-Type: application/json" \
  -d '{
    "situation_description": "UN agency negotiating with regional government for access to IDP camps...",
    "organization_name": "World Food Programme",
    "counterpart_name": "Ministry of Interior",
    "response_format": "markdown",
    "detail_level": "detailed"
  }'

# Analyze stakeholders
curl -X POST http://localhost:8000/api/v1/analyze-stakeholders \
  -H "Content-Type: application/json" \
  -d '{
    "context": "Negotiating ceasefire agreement for humanitarian corridor",
    "stakeholders": [
      {
        "name": "Chief Military Commander",
        "power": 1.0,
        "urgency": 0.7,
        "legitimacy": 0.8,
        "position": -0.5,
        "influenced_by": ["UN Secretary General Envoy"]
      },
      {
        "name": "UN Secretary General Envoy",
        "power": 0.8,
        "urgency": 1.0,
        "legitimacy": 1.0,
        "position": 1.0,
        "influenced_by": []
      }
    ],
    "response_format": "json",
    "detail_level": "detailed"
  }'

# Get methodology guide
curl http://localhost:8000/api/v1/guide
```

### 5.3 Python Client

```python
import requests
import json

API_BASE = "http://localhost:8000/api/v1"

def create_island_of_agreement(situation, org_name, counterpart):
    """Create Island of Agreement analysis via HTTP"""
    response = requests.post(
        f"{API_BASE}/island-of-agreement",
        json={
            "situation_description": situation,
            "organization_name": org_name,
            "counterpart_name": counterpart,
            "response_format": "markdown",
            "detail_level": "detailed"
        }
    )

    if response.status_code == 200:
        result = response.json()
        return result["data"]
    else:
        raise Exception(f"Error: {response.status_code} - {response.text}")

# Usage
analysis = create_island_of_agreement(
    "UN agency negotiating with regional government for access to IDP camps where 50,000 displaced persons need immediate food assistance...",
    "World Food Programme",
    "Ministry of Interior"
)
print(analysis)
```

### 5.4 JavaScript/Node.js Client

```javascript
const API_BASE = "http://localhost:8000/api/v1";

async function createIslandOfAgreement(situation, orgName, counterpartName) {
  try {
    const response = await fetch(`${API_BASE}/island-of-agreement`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        situation_description: situation,
        organization_name: orgName,
        counterpart_name: counterpartName,
        response_format: 'markdown',
        detail_level: 'detailed'
      })
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const result = await response.json();
    return result.data;
  } catch (error) {
    console.error('Error:', error);
    throw error;
  }
}

// Usage
createIslandOfAgreement(
  "UN agency negotiating with regional government...",
  "World Food Programme",
  "Ministry of Interior"
).then(analysis => console.log(analysis));
```

### 5.5 Interactive API Docs

Visit `http://localhost:8000/docs` for interactive Swagger UI where you can:
- See all endpoints
- Read parameter descriptions
- Test requests directly
- See response schemas

---

## 6. Docker Container

### 6.1 Build Image

```bash
docker build -t humanitarian-mcp:1.0 .
```

### 6.2 Run Container

```bash
# Run HTTP server
docker run -p 8000:8000 humanitarian-mcp:1.0

# Access at: http://localhost:8000
```

### 6.3 Docker Compose

```bash
# Start services
docker-compose up -d

# View logs
docker-compose logs -f humanitarian-mcp-http

# Stop services
docker-compose down
```

---

## 7. OpenAI Client

Use the HTTP wrapper with OpenAI's API:

```python
from openai import OpenAI
import requests
import json

client = OpenAI(api_key="your-api-key")

# First, get the list of tools from our HTTP server
http_response = requests.get("http://localhost:8000/tools").json()

tools = []
for tool in http_response["tools"]:
    # Create tool definitions for OpenAI
    if tool["name"] == "humanitarian_create_island_of_agreement":
        tools.append({
            "type": "function",
            "function": {
                "name": tool["name"],
                "description": tool["description"],
                "parameters": {
                    "type": "object",
                    "properties": {
                        "situation_description": {"type": "string"},
                        "organization_name": {"type": "string"},
                        "counterpart_name": {"type": "string"},
                        "response_format": {"type": "string", "enum": ["markdown", "json"]},
                        "detail_level": {"type": "string", "enum": ["concise", "detailed"]}
                    },
                    "required": ["situation_description", "organization_name", "counterpart_name"]
                }
            }
        })

messages = [
    {
        "role": "user",
        "content": "Analyze this negotiation: UN agency negotiating with regional government for access..."
    }
]

response = client.chat.completions.create(
    model="gpt-4",
    messages=messages,
    tools=tools,
    tool_choice="auto"
)

# When tool_calls appear in response, forward to our HTTP server
if response.tool_calls:
    for tool_call in response.tool_calls:
        if tool_call.function.name == "humanitarian_create_island_of_agreement":
            tool_response = requests.post(
                "http://localhost:8000/api/v1/island-of-agreement",
                json=json.loads(tool_call.function.arguments)
            ).json()
            print(tool_response)
```

---

## 8. Anthropic SDK

Direct integration with Anthropic SDK:

```python
import anthropic
import requests
import json

client = anthropic.Anthropic(api_key="your-api-key")

# Define tools for Anthropic
tools = [
    {
        "name": "humanitarian_create_island_of_agreement",
        "description": "Creates IoA analysis with contested/agreed facts",
        "input_schema": {
            "type": "object",
            "properties": {
                "situation_description": {
                    "type": "string",
                    "description": "Description of negotiation situation"
                },
                "organization_name": {
                    "type": "string",
                    "description": "Name of organization"
                },
                "counterpart_name": {
                    "type": "string",
                    "description": "Name of counterpart"
                },
                "response_format": {
                    "type": "string",
                    "enum": ["markdown", "json"],
                    "default": "markdown"
                },
                "detail_level": {
                    "type": "string",
                    "enum": ["concise", "detailed"],
                    "default": "detailed"
                }
            },
            "required": ["situation_description", "organization_name", "counterpart_name"]
        }
    }
]

messages = [
    {
        "role": "user",
        "content": "Help me analyze a humanitarian negotiation..."
    }
]

response = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=4096,
    tools=tools,
    messages=messages
)

# Process tool calls
for content_block in response.content:
    if content_block.type == "tool_use":
        tool_input = content_block.input

        # Call HTTP server
        http_response = requests.post(
            "http://localhost:8000/api/v1/island-of-agreement",
            json=tool_input
        ).json()

        print(http_response)
```

---

## 9. LangChain Integration

```python
from langchain.tools import tool
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
import requests
import json

# Define tool for LangChain
@tool
def humanitarian_island_of_agreement(
    situation_description: str,
    organization_name: str,
    counterpart_name: str,
    response_format: str = "markdown"
) -> str:
    """
    Create an Island of Agreement analysis for humanitarian negotiation.

    Args:
        situation_description: Description of the negotiation situation
        organization_name: Name of your organization
        counterpart_name: Name of the counterpart
        response_format: Output format (markdown or json)
    """
    response = requests.post(
        "http://localhost:8000/api/v1/island-of-agreement",
        json={
            "situation_description": situation_description,
            "organization_name": organization_name,
            "counterpart_name": counterpart_name,
            "response_format": response_format
        }
    ).json()

    return json.dumps(response.get("data", response))

# Use with LangChain agent
tools = [humanitarian_island_of_agreement]
llm = ChatOpenAI(model="gpt-4", temperature=0)
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.OPENAI_FUNCTIONS,
    verbose=True
)

result = agent.run(
    "Analyze this humanitarian negotiation: UN agency with regional government..."
)
print(result)
```

---

## 10. Command Line / Shell

Add to your shell scripts:

```bash
#!/bin/bash

# Function to call MCP HTTP API
call_mcp() {
    local endpoint=$1
    local data=$2

    curl -X POST "http://localhost:8000/api/v1/${endpoint}" \
      -H "Content-Type: application/json" \
      -d "$data" \
      --silent | jq .
}

# Example: Create Island of Agreement
call_mcp "island-of-agreement" '{
  "situation_description": "UN agency negotiating with regional government for access...",
  "organization_name": "World Food Programme",
  "counterpart_name": "Ministry of Interior"
}'

# Example: Get list of tools
curl http://localhost:8000/tools --silent | jq .
```

---

## 📊 Comparison Table

| Client | Type | Status | Configuration | Complexity |
|--------|------|--------|---------------|-----------|
| Claude Desktop | Native MCP | ✅ Ready | `claude_desktop_config.json` | Low |
| Cline | VSCode Ext | ✅ Ready | `.cline/mcp-config.json` | Low |
| Continue | IDE Ext | ✅ Ready | `.continuerc.json` | Low |
| Cursor | IDE | ✅ Ready | Uses Claude config | Low |
| HTTP API | REST | ✅ Ready | `http_server.py` | Medium |
| Docker | Container | ✅ Ready | `Dockerfile` | Medium |
| PyPI | Package | 📦 Soon | `pip install` | Low |
| OpenAI | SDK | ✅ Working | Custom integration | Medium |
| Anthropic | SDK | ✅ Working | Custom integration | Medium |
| LangChain | Framework | ✅ Working | Custom tools | High |

---

## 🚀 Quick Start for Each Platform

### VSCode Users
1. Install Cline or Continue extension
2. Add MCP config to settings
3. Use `@humanitarian-negotiation` in chat

### Web App Developers
1. Start HTTP server: `python http_server.py`
2. Make requests to `http://localhost:8000/api/v1/*`
3. Check docs at `http://localhost:8000/docs`

### Python Developers
```bash
pip install humanitarian-negotiation-mcp[http]
# Or just import and use HTTP client shown above
```

### Docker Users
```bash
docker-compose up -d
# Access at http://localhost:8000
```

### Anyone Else
Use the REST API endpoints - compatible with any platform that can make HTTP requests.

---

## ❓ FAQ

**Q: Can I use this with multiple LLMs?**
A: Yes! The HTTP API works with OpenAI, Anthropic, Mistral, or any LLM supporting tool calling.

**Q: Do I need to run multiple servers?**
A: No, the HTTP server handles all requests from multiple clients simultaneously.

**Q: Can I self-host?**
A: Yes! Use Docker or run `http_server.py` on any server. Deploy to AWS Lambda, Google Cloud Run, etc.

**Q: What if I want custom modifications?**
A: Edit `humanitarian_negotiation_mcp.py` directly or extend the HTTP wrapper.
