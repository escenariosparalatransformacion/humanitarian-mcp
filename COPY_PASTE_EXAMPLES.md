# Copy-Paste Examples - Ready to Use

Quick, copy-paste solutions for common tasks.

---

## 🌐 HTTP API Usage

### Example 1: Start the HTTP Server

```bash
pip install fastapi uvicorn
python http_server.py
```

Then visit: `http://localhost:8000/docs`

---

### Example 2: Test with cURL

```bash
# Health check
curl http://localhost:8000/health

# Get all tools
curl http://localhost:8000/tools

# Create Island of Agreement
curl -X POST http://localhost:8000/api/v1/island-of-agreement \
  -H "Content-Type: application/json" \
  -d '{
    "situation_description": "UN agency negotiating with regional government for access to IDP camps where 50,000 displaced persons need immediate food assistance. Government demands all operations be coordinated through Ministry of Interior. Security situation is volatile with recent armed clashes in the area.",
    "organization_name": "World Food Programme",
    "counterpart_name": "Ministry of Interior",
    "response_format": "markdown",
    "detail_level": "detailed"
  }'
```

---

### Example 3: Python Client

```python
import requests
import json

API_BASE = "http://localhost:8000/api/v1"

def create_island_of_agreement():
    response = requests.post(
        f"{API_BASE}/island-of-agreement",
        json={
            "situation_description": "UN agency negotiating with regional government for access to IDP camps where 50,000 displaced persons need immediate food assistance. Government demands all operations be coordinated through Ministry of Interior.",
            "organization_name": "World Food Programme",
            "counterpart_name": "Ministry of Interior",
            "response_format": "markdown",
            "detail_level": "detailed"
        }
    )

    if response.status_code == 200:
        result = response.json()
        print(result["data"])
    else:
        print(f"Error: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    create_island_of_agreement()
```

---

### Example 4: JavaScript Client

```javascript
const API_BASE = "http://localhost:8000/api/v1";

async function createIslandOfAgreement() {
  try {
    const response = await fetch(`${API_BASE}/island-of-agreement`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        situation_description: "UN agency negotiating with regional government for access to IDP camps where 50,000 displaced persons need immediate food assistance.",
        organization_name: "World Food Programme",
        counterpart_name: "Ministry of Interior",
        response_format: "markdown",
        detail_level: "detailed"
      })
    });

    const result = await response.json();
    console.log(result.data);
  } catch (error) {
    console.error('Error:', error);
  }
}

createIslandOfAgreement();
```

---

## 🐳 Docker Usage

### Example 5: Run with Docker Compose

```bash
# Start services
docker-compose up -d

# View logs
docker-compose logs -f humanitarian-mcp-http

# Stop services
docker-compose down

# Access at http://localhost:8000
```

---

### Example 6: Build Docker Image Manually

```bash
# Build image
docker build -t humanitarian-mcp:1.0 .

# Run container
docker run -p 8000:8000 humanitarian-mcp:1.0

# Run with environment variables
docker run -p 8000:8000 -e PYTHONUNBUFFERED=1 humanitarian-mcp:1.0

# Run with volume mount (for development)
docker run -p 8000:8000 -v $(pwd):/app humanitarian-mcp:1.0
```

---

## 📦 Python Package Usage

### Example 7: Build Python Package

```bash
# Install build tools
pip install --upgrade build twine

# Build package
python -m build

# Check what was built
ls -la dist/

# Upload to test PyPI (first time)
twine upload --repository testpypi dist/*

# Upload to PyPI (production)
twine upload dist/*
```

---

### Example 8: Install from PyPI

```bash
# After publishing to PyPI
pip install humanitarian-negotiation-mcp

# With HTTP support
pip install humanitarian-negotiation-mcp[http]

# With development dependencies
pip install humanitarian-negotiation-mcp[dev]

# Everything
pip install humanitarian-negotiation-mcp[all]
```

---

## 🔧 Integration Examples

### Example 9: Postman/Insomnia

1. Open Postman/Insomnia
2. Create new POST request to: `http://localhost:8000/api/v1/island-of-agreement`
3. Set headers:
```
Content-Type: application/json
```
4. Set body (JSON):
```json
{
  "situation_description": "UN agency negotiating with regional government for access to IDP camps where 50,000 displaced persons need immediate food assistance.",
  "organization_name": "World Food Programme",
  "counterpart_name": "Ministry of Interior",
  "response_format": "markdown",
  "detail_level": "detailed"
}
```
5. Click Send

---

### Example 10: Excel/Google Sheets (Zapier)

```
Trigger: Manual or on schedule
Action: Make HTTP request to:
  URL: http://localhost:8000/api/v1/island-of-agreement
  Method: POST
  Headers: Content-Type: application/json
  Body:
  {
    "situation_description": "[Zapier variable]",
    "organization_name": "[Zapier variable]",
    "counterpart_name": "[Zapier variable]"
  }
```

---

### Example 11: OpenAI Integration

```python
from openai import OpenAI
import requests
import json

client = OpenAI(api_key="your-api-key")

# Define tools
tools = [
    {
        "type": "function",
        "function": {
            "name": "humanitarian_island_of_agreement",
            "description": "Create Island of Agreement analysis",
            "parameters": {
                "type": "object",
                "properties": {
                    "situation_description": {"type": "string"},
                    "organization_name": {"type": "string"},
                    "counterpart_name": {"type": "string"}
                },
                "required": ["situation_description", "organization_name", "counterpart_name"]
            }
        }
    }
]

# Make request to OpenAI
response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "user", "content": "Analyze this humanitarian negotiation..."}
    ],
    tools=tools,
    tool_choice="auto"
)

# Handle tool calls
if response.tool_calls:
    for tool_call in response.tool_calls:
        if tool_call.function.name == "humanitarian_island_of_agreement":
            args = json.loads(tool_call.function.arguments)

            # Call our API
            api_response = requests.post(
                "http://localhost:8000/api/v1/island-of-agreement",
                json=args
            ).json()

            print(api_response["data"])
```

---

### Example 12: Claude API Integration

```python
import anthropic
import requests
import json

client = anthropic.Anthropic(api_key="your-api-key")

# Define tools
tools = [
    {
        "name": "humanitarian_island_of_agreement",
        "description": "Create Island of Agreement analysis",
        "input_schema": {
            "type": "object",
            "properties": {
                "situation_description": {"type": "string"},
                "organization_name": {"type": "string"},
                "counterpart_name": {"type": "string"}
            },
            "required": ["situation_description", "organization_name", "counterpart_name"]
        }
    }
]

# Make request to Claude
response = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=4096,
    tools=tools,
    messages=[
        {"role": "user", "content": "Analyze this negotiation..."}
    ]
)

# Handle tool calls
for content_block in response.content:
    if content_block.type == "tool_use":
        # Call our API
        api_response = requests.post(
            "http://localhost:8000/api/v1/island-of-agreement",
            json=content_block.input
        ).json()

        print(api_response["data"])
```

---

### Example 13: Shell Script

```bash
#!/bin/bash

# Configuration
API_BASE="http://localhost:8000/api/v1"

# Function: Create Island of Agreement
create_ioa() {
    local situation="$1"
    local org="$2"
    local counterpart="$3"

    curl -X POST "$API_BASE/island-of-agreement" \
        -H "Content-Type: application/json" \
        -d "{
            \"situation_description\": \"$situation\",
            \"organization_name\": \"$org\",
            \"counterpart_name\": \"$counterpart\",
            \"response_format\": \"markdown\",
            \"detail_level\": \"detailed\"
        }" | jq .
}

# Function: Analyze Stakeholders
analyze_stakeholders() {
    local context="$1"
    local stakeholders_json="$2"

    curl -X POST "$API_BASE/analyze-stakeholders" \
        -H "Content-Type: application/json" \
        -d "{
            \"context\": \"$context\",
            \"stakeholders\": $stakeholders_json,
            \"response_format\": \"markdown\",
            \"detail_level\": \"detailed\"
        }" | jq .
}

# Example usage
create_ioa \
    "UN agency negotiating with regional government..." \
    "World Food Programme" \
    "Ministry of Interior"
```

---

### Example 14: Node.js Express Server

```javascript
const express = require('express');
const axios = require('axios');

const app = express();
app.use(express.json());

const API_BASE = 'http://localhost:8000/api/v1';

// Route: Create Island of Agreement
app.post('/api/island-of-agreement', async (req, res) => {
    try {
        const response = await axios.post(
            `${API_BASE}/island-of-agreement`,
            req.body
        );

        res.json(response.data);
    } catch (error) {
        res.status(400).json({ error: error.message });
    }
});

// Route: Get Tools List
app.get('/api/tools', async (req, res) => {
    try {
        const response = await axios.get(`${API_BASE}/../tools`);
        res.json(response.data);
    } catch (error) {
        res.status(400).json({ error: error.message });
    }
});

app.listen(3000, () => {
    console.log('Server running on http://localhost:3000');
});
```

---

### Example 15: React Component

```jsx
import React, { useState } from 'react';
import axios from 'axios';

const IslandOfAgreementAnalyzer = () => {
    const [loading, setLoading] = useState(false);
    const [result, setResult] = useState(null);
    const [error, setError] = useState(null);

    const handleAnalyze = async (e) => {
        e.preventDefault();
        setLoading(true);
        setError(null);

        try {
            const response = await axios.post(
                'http://localhost:8000/api/v1/island-of-agreement',
                {
                    situation_description: e.target.situation.value,
                    organization_name: e.target.org.value,
                    counterpart_name: e.target.counterpart.value,
                    response_format: 'markdown',
                    detail_level: 'detailed'
                }
            );

            setResult(response.data.data);
        } catch (err) {
            setError(err.message);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div>
            <form onSubmit={handleAnalyze}>
                <textarea name="situation" required />
                <input name="org" required />
                <input name="counterpart" required />
                <button type="submit" disabled={loading}>
                    {loading ? 'Analyzing...' : 'Analyze'}
                </button>
            </form>

            {error && <div className="error">{error}</div>}
            {result && <div className="result">{JSON.stringify(result, null, 2)}</div>}
        </div>
    );
};

export default IslandOfAgreementAnalyzer;
```

---

## 🚀 Deployment Scripts

### Example 16: Deploy to AWS Lambda

```python
# lambda_handler.py
import json
import requests

API_BASE = "http://localhost:8000/api/v1"

def lambda_handler(event, context):
    try:
        # Parse incoming event
        body = json.loads(event.get('body', '{}'))

        # Call our MCP API
        response = requests.post(
            f"{API_BASE}/island-of-agreement",
            json=body
        )

        return {
            'statusCode': 200,
            'body': json.dumps(response.json())
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
```

---

### Example 17: Deploy to Google Cloud Run

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements_mcp.txt .
RUN pip install --no-cache-dir -r requirements_mcp.txt fastapi uvicorn

COPY humanitarian_negotiation_mcp.py .
COPY http_server.py .

ENV PORT=8080
EXPOSE 8080

CMD ["python", "-m", "uvicorn", "http_server:app", "--host", "0.0.0.0", "--port", "8080"]
```

Deploy:
```bash
gcloud run deploy humanitarian-mcp \
    --source . \
    --platform managed \
    --region us-central1
```

---

### Example 18: GitHub Actions CI/CD

```yaml
# .github/workflows/deploy.yml
name: Deploy MCP

on:
  push:
    branches: [ main ]

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.10'

    - name: Install dependencies
      run: |
        pip install -r requirements_mcp.txt
        pip install pytest pytest-asyncio

    - name: Run tests
      run: pytest

    - name: Build Docker image
      run: docker build -t humanitarian-mcp:${{ github.sha }} .

    - name: Push to Docker Hub
      run: |
        echo ${{ secrets.DOCKER_PASSWORD }} | docker login -u ${{ secrets.DOCKER_USERNAME }} --password-stdin
        docker push humanitarian-mcp:${{ github.sha }}
```

---

## 📋 Checklist Scripts

### Example 19: Pre-Deployment Checklist

```bash
#!/bin/bash

echo "Pre-Deployment Checklist"
echo "========================"

# Check Python version
python_version=$(python --version 2>&1 | awk '{print $2}')
echo "✓ Python version: $python_version (requires 3.10+)"

# Check dependencies
pip show anthropic > /dev/null && echo "✓ anthropic installed" || echo "✗ anthropic missing"
pip show mcp > /dev/null && echo "✓ mcp installed" || echo "✗ mcp missing"
pip show pydantic > /dev/null && echo "✓ pydantic installed" || echo "✗ pydantic missing"

# Check files
[ -f humanitarian_negotiation_mcp.py ] && echo "✓ MCP server found" || echo "✗ MCP server missing"
[ -f http_server.py ] && echo "✓ HTTP wrapper found" || echo "✗ HTTP wrapper missing"
[ -f Dockerfile ] && echo "✓ Dockerfile found" || echo "✗ Dockerfile missing"

# Check Docker
docker --version > /dev/null 2>&1 && echo "✓ Docker installed" || echo "✗ Docker not installed"

echo ""
echo "✅ Pre-deployment check complete!"
```

---

## 💡 Tips & Tricks

### Example 20: Monitoring & Health Checks

```bash
#!/bin/bash

# Continuous health monitor
while true; do
    status=$(curl -s http://localhost:8000/health | jq .status)
    timestamp=$(date '+%Y-%m-%d %H:%M:%S')

    if [ "$status" = '"operational"' ]; then
        echo "[$timestamp] ✓ MCP is healthy"
    else
        echo "[$timestamp] ✗ MCP is down!"
        # Alert or restart
    fi

    sleep 60
done
```

---

All examples are ready to copy-paste! Adjust as needed for your use case.
