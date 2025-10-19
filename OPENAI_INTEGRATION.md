# OpenAI ChatGPT Integration Guide

This guide explains how to use the Humanitarian Negotiation MCP Server as a Custom GPT action in ChatGPT.

## Overview

The Humanitarian Negotiation MCP can be integrated with ChatGPT as a custom action, allowing you to:
- Access all 5 humanitarian negotiation analysis tools
- Receive AI-enhanced responses combining ChatGPT and specialized analysis
- Use natural language to trigger complex negotiations frameworks
- Get insights tailored to your specific context

## Files Included

Two OpenAPI schema files are provided:

1. **`OPENAI_COMPLETE_SCHEMA.json`** - Full schema with all 5 tools
   - Complete implementation with all endpoints
   - Ready for custom GPT integration
   - Includes all optional parameters

2. **`OPENAI_SCHEMA_FIXED.json`** - Compact schema (optimized version)
   - Streamlined for performance
   - Recommended for most use cases
   - Faster response times

## Setup Instructions

### Prerequisites

1. ChatGPT Plus subscription (required for Custom GPTs)
2. OpenAI API access
3. Server deployed and accessible via HTTPS
4. OpenAPI schema file (see files above)

### Deployment Options

#### Option 1: Google Cloud Run (Recommended)

The schema files reference a default GCP Cloud Run endpoint. To use your own:

1. **Deploy the HTTP server to Cloud Run:**
```bash
# Build and deploy
gcloud run deploy humanitarian-mcp \
  --source . \
  --platform managed \
  --region us-central1 \
  --timeout 900 \
  --memory 256Mi \
  --allow-unauthenticated
```

2. **Get your endpoint:**
```bash
gcloud run services describe humanitarian-mcp --region us-central1 --format='value(status.url)'
```

3. **Update the schema file:**
   - Edit `OPENAI_COMPLETE_SCHEMA.json` or `OPENAI_SCHEMA_FIXED.json`
   - Replace the `servers.url` field with your endpoint
   - Example: `"url": "https://your-service-xxxxx.run.app"`

#### Option 2: Self-Hosted HTTPS Server

1. **Start the HTTP server locally:**
```bash
python http_server.py
```

2. **Set up HTTPS tunnel (using ngrok):**
```bash
ngrok http 8000
```

3. **Update schema with your ngrok URL:**
   - Replace `servers.url` with your ngrok HTTPS URL

#### Option 3: AWS Lambda / Azure Container

Deploy using your preferred cloud provider, ensuring:
- HTTPS is enabled
- CORS is configured
- All required dependencies are installed

### Creating a Custom GPT

1. **Go to ChatGPT Custom GPTs:**
   - Navigate to https://chatgpt.com/gpts/mine
   - Click "Create a GPT"
   - Select "Create new"

2. **Configure the GPT:**
   - Name: "Humanitarian Negotiation Analyzer"
   - Description: "Analyzes complex humanitarian negotiations using proven methodologies"
   - Instructions: (See below)

3. **Add Your Schema:**
   - Go to "Actions" section
   - Click "Create new action"
   - Choose "Import from URL" or "Paste JSON"
   - Paste the content of `OPENAI_COMPLETE_SCHEMA.json`
   - Save and publish

### GPT Instructions Template

```
You are an expert humanitarian negotiation analyst with deep knowledge of
conflict resolution, mediation, and stakeholder engagement.

When users describe negotiation scenarios, use these specialized tools:

1. Island of Agreement (IoA) - Start here for new negotiations
   - Maps contested vs. agreed facts
   - Identifies convergent vs. divergent norms
   - Best for finding common ground

2. Iceberg & Common Shared Space - Understand deeper motivations
   - Reveals positions, reasoning, and motives
   - Identifies compromise opportunities
   - Use after IoA analysis

3. Stakeholder Analysis - Map all relevant actors
   - Assess power, urgency, legitimacy, position
   - Prioritize engagement strategies
   - Identify influence pathways

4. Leverage Influence - Tactical execution
   - Develop specific influence tactics
   - Build coalitions
   - Mitigate risks

5. Negotiation Guide - Comprehensive methodology reference

Always:
- Ask clarifying questions to gather complete context
- Provide structured, actionable recommendations
- Consider cultural context and local realities
- Frame advice in terms of shared benefits
- Follow humanitarian principles and international norms
```

## API Endpoints

All endpoints follow the OpenAPI 3.1.0 specification:

### 1. Island of Agreement
```
POST /api/v1/island-of-agreement

Request:
{
  "situation_description": "string (min 50 chars)",
  "organization_name": "string",
  "counterpart_name": "string",
  "additional_context": "string (optional)",
  "response_format": "markdown" | "json",
  "detail_level": "concise" | "detailed"
}

Response:
{
  "analysis": "Island of Agreement analysis",
  "contested_facts": [...],
  "agreed_facts": [...],
  "convergent_norms": [...],
  "divergent_norms": [...],
  "strategic_recommendations": [...]
}
```

### 2. Analyze Icebergs
```
POST /api/v1/analyze-icebergs

Request:
{
  "organization_name": "string",
  "counterpart_name": "string",
  "organization_positions": ["string"],
  "organization_reasoning": ["string"],
  "organization_motives": ["string"],
  "counterpart_positions": ["string"],
  "counterpart_reasoning": ["string"],
  "counterpart_motives": ["string"],
  "response_format": "markdown" | "json",
  "detail_level": "concise" | "detailed"
}

Response:
{
  "organization_iceberg": {...},
  "counterpart_iceberg": {...},
  "common_shared_space": {...},
  "compromise_opportunities": [...]
}
```

### 3. Analyze Stakeholders
```
POST /api/v1/analyze-stakeholders

Request:
{
  "context": "string (min 50 chars)",
  "stakeholders": [
    {
      "name": "string",
      "power": 0.0-1.0,
      "urgency": 0.0-1.0,
      "legitimacy": 0.0-1.0,
      "position": -1.0 to 1.0,
      "influenced_by": ["string"]
    }
  ],
  "response_format": "markdown" | "json",
  "detail_level": "concise" | "detailed"
}

Response:
{
  "stakeholders": [...],
  "priority_levels": {...},
  "relationship_mapping": {...},
  "engagement_strategies": [...]
}
```

### 4. Leverage Influence
```
POST /api/v1/leverage-influence-latest

Request:
{
  "target_stakeholder_name": "string",
  "response_format": "markdown" | "json"
}

Response:
{
  "target_stakeholder": {...},
  "influence_tactics": [...],
  "coalition_opportunities": [...],
  "risk_mitigation": [...]
}
```

### 5. Negotiation Guide
```
GET /api/v1/guide

Response:
{
  "guide": "Comprehensive methodology guide"
}
```

## Example Usage in ChatGPT

### Example Prompt

```
I'm a UN agency negotiating with the regional government for access to
IDP camps where 50,000 displaced persons need assistance. The government
wants all operations coordinated through their Ministry of Interior, and
the security situation is volatile.

Our organization needs unrestricted access and direct community contact.
The government prioritizes sovereignty and security control.

What should we do?
```

### ChatGPT Will:

1. **Recognize the negotiation context**
2. **Call the Island of Agreement tool** to identify common ground
3. **Call the Iceberg tool** to understand deeper motivations
4. **Map stakeholders** (UN agencies, local authorities, security forces, affected communities)
5. **Suggest influence tactics** for key stakeholders
6. **Provide actionable recommendations**

## Authentication & Security

### Current Implementation
- No authentication required (suitable for internal/trusted use)
- HTTPS recommended for all production deployments

### Adding Authentication

For production deployments, add:

```json
{
  "servers": [
    {
      "url": "https://your-api.example.com",
      "variables": {
        "basePath": {
          "default": "/api/v1"
        }
      }
    }
  ],
  "components": {
    "securitySchemes": {
      "BearerAuth": {
        "type": "http",
        "scheme": "bearer"
      }
    }
  },
  "security": [
    { "BearerAuth": [] }
  ]
}
```

## Troubleshooting

### Issue: "Connection refused"
- Verify server is running and accessible
- Check HTTPS is enabled
- Verify firewall allows external connections

### Issue: "Invalid schema"
- Ensure OpenAPI 3.1.0 format
- Validate JSON syntax
- Check all required fields are present

### Issue: "Timeout errors"
- Increase timeout in Cloud Run (current: 900 seconds)
- Optimize API performance
- Consider caching results

### Issue: "CORS errors"
- Verify CORS is enabled on the server
- Check origin header configuration
- Ensure HTTP headers are correct

## Performance Tips

1. **Request optimization:**
   - Keep descriptions concise but complete
   - Use "concise" detail level for quick analysis
   - Batch similar requests

2. **Server optimization:**
   - Use Cloud Run for auto-scaling
   - Enable caching for repeated analyses
   - Monitor response times

3. **ChatGPT optimization:**
   - Provide clear, structured context
   - Use the GPT instructions to guide queries
   - Build on previous analyses

## Support

For issues or questions:

1. Check DEPLOYMENT.md for server setup
2. Review README.md for methodology documentation
3. Test API directly using curl or Postman
4. Enable debug logging for troubleshooting

## Examples for Different Contexts

### Humanitarian Access Negotiation
```
Use Island of Agreement first
→ Map contested access points vs. agreed principles
→ Analyze stakeholder positions
→ Develop influence tactics
```

### Ceasefire Agreement
```
Use Stakeholder Analysis first
→ Identify military decision-makers
→ Analyze their positions and motivations
→ Develop engagement strategies
→ Identify coalition opportunities
```

### Inter-Agency Coordination
```
Use Iceberg analysis for each agency
→ Understand their positions and motivations
→ Find common shared space
→ Resolve conflicts
```

## API Rate Limits

Current implementation: No rate limiting (configure as needed)

For production:
- Recommended: 100 requests/minute per API key
- Burst limit: 10 requests/second
- Implement token bucket or sliding window algorithms

## Version Information

- **Schema Version**: 1.0.0
- **OpenAPI Version**: 3.1.0
- **MCP Server**: 1.0.0
- **Last Updated**: 2025

---

**Developed by**: Jhozman Camacho
**License**: MIT
**Documentation**: See README.md and DEPLOYMENT.md for additional information
