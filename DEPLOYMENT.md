# Deployment Guide - Humanitarian Negotiation MCP

This guide covers deployment options beyond Claude Desktop for teams and organizations.

## Table of Contents

1. [Local Deployment (Claude Desktop)](#local-deployment)
2. [Team Deployment](#team-deployment)
3. [Docker Deployment](#docker-deployment)
4. [HTTP Server Mode](#http-server-mode)
5. [Cloud Deployment](#cloud-deployment)

## Local Deployment

### Individual Installation

For single-user installation on Windows:

```bash
INSTALL_MCP_CLAUDE_DESKTOP.bat
```

For macOS/Linux manual installation:

```bash
# 1. Install dependencies
pip install -r requirements_mcp.txt

# 2. Edit Claude Desktop config
# macOS: ~/Library/Application\ Support/Claude/claude_desktop_config.json
# Linux: ~/.config/Claude/claude_desktop_config.json

# 3. Add server configuration
# Replace /absolute/path/to/humanitarian_negotiation_mcp.py with actual path

# 4. Restart Claude Desktop
```

## Team Deployment

### Sharing with Team Members

1. **Distribute the entire directory** to your team
2. **Each member runs** the installation script or manual setup
3. **Share examples** using the EXAMPLES.md file
4. **Document customizations** for your organization

### Shared Network Location

For organizations using shared network drives:

```json
{
  "mcpServers": {
    "humanitarian-negotiation": {
      "command": "python",
      "args": ["\\\\network-drive\\path\\to\\humanitarian_negotiation_mcp.py"]
    }
  }
}
```

## Docker Deployment

### Using Docker Compose

```bash
docker-compose up -d
```

This uses the included `docker-compose.yml` configuration.

### Manual Docker Build

```bash
# Build the image
docker build -t humanitarian-mcp:latest .

# Run the container
docker run -p 8000:8000 humanitarian-mcp:latest
```

### Kubernetes Deployment

For Kubernetes environments, adapt the Docker image to your cluster configuration.

## HTTP Server Mode

### Running as HTTP Server

```bash
python http_server.py
```

The server will be available at:
```
http://localhost:8000
```

### API Endpoints

- `POST /api/v1/island-of-agreement`
- `POST /api/v1/analyze-icebergs`
- `POST /api/v1/analyze-stakeholders`
- `POST /api/v1/leverage-influence`
- `GET /api/v1/guide`

### Example API Call

```bash
curl -X POST http://localhost:8000/api/v1/island-of-agreement \
  -H "Content-Type: application/json" \
  -d '{
    "situation_description": "Negotiating humanitarian access...",
    "organization_name": "WFP",
    "counterpart_name": "Government Ministry",
    "response_format": "json"
  }'
```

## Cloud Deployment

### Google Cloud Run

Environment requirements:
- Python 3.10+
- 256MB RAM minimum
- 15 minute timeout

Deploy using:
```bash
gcloud run deploy humanitarian-mcp \
  --source . \
  --platform managed \
  --region us-central1 \
  --timeout 900 \
  --memory 256Mi
```

### AWS Lambda

For Lambda deployment, package the application with all dependencies:

```bash
pip install -t lambda_layer/python -r requirements_mcp.txt
```

### Azure Container Instances

```bash
az container create \
  --resource-group my-group \
  --name humanitarian-mcp \
  --image humanitarian-mcp:latest \
  --cpu 1 --memory 1
```

## Configuration Options

### Environment Variables

```bash
# Set Python path
export PYTHONPATH=/path/to/project:$PYTHONPATH

# Set MCP debug mode (optional)
export MCP_DEBUG=1
```

### Performance Tuning

Modify in `humanitarian_negotiation_mcp.py`:

```python
# Maximum stakeholders per analysis
MAX_STAKEHOLDERS = 50

# Character limit per response
CHARACTER_LIMIT = 25000

# Response detail level
DEFAULT_DETAIL_LEVEL = "detailed"
```

## Troubleshooting

### Common Issues

**Issue**: "Python not found"
- **Solution**: Ensure Python 3.10+ is installed and in PATH

**Issue**: "Module not found"
- **Solution**: Run `pip install -r requirements_mcp.txt`

**Issue**: "Connection refused"
- **Solution**: Verify correct path in Claude Desktop config

**Issue**: "Permission denied"
- **Solution**: Check file permissions: `chmod +x humanitarian_negotiation_mcp.py`

### Verification

Test the installation:

```bash
# Check Python version
python --version

# Verify imports
python -c "from humanitarian_negotiation_mcp import mcp"

# Test MCP connection
python humanitarian_negotiation_mcp.py
```

## Security Considerations

### Data Privacy

- All analyses run locally (no external API calls)
- No data is stored or transmitted
- All input remains on your system

### Authentication

For cloud deployments, implement:
- API key authentication
- OAuth 2.0
- SSL/TLS encryption

### Rate Limiting

For HTTP server mode, implement:
- Request throttling
- API key-based rate limits
- Timeout policies

## Monitoring and Logging

### Enable Logging

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Track Usage

For HTTP server, add:
- Request/response logging
- Error tracking
- Performance monitoring

## Backup and Recovery

### Regular Backups

- Back up `requirements_mcp.txt`
- Back up `humanitarian_negotiation_mcp.py`
- Back up `setup.py`

### Version Control

Recommended Git setup:

```bash
git init
git add .
git commit -m "Initial deployment"
git tag v1.0.0
```

## Updates and Maintenance

### Checking for Updates

1. Monitor the official repository
2. Test updates in a staging environment
3. Deploy to production
4. Maintain version history

### Updating Dependencies

```bash
pip install -r requirements_mcp.txt --upgrade
```

## Support

For deployment issues:
1. Check the troubleshooting section
2. Review logs and error messages
3. Verify configuration files
4. Test with example prompts from EXAMPLES.md

---

**Last Updated**: 2025
**Version**: 1.0.0
**License**: MIT
