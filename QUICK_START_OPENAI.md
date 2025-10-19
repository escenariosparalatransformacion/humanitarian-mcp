# Quick Start: Using All 5 Tools in OpenAI

## 1. Update Your Schema in ChatGPT

1. Go to your Custom GPT settings
2. Click **"Actions"** section
3. Paste the contents of `OPENAI_COMPLETE_SCHEMA.json`
4. Server URL should be: `https://humanitarian-mcp-904769523449.us-central1.run.app`

## 2. Test Each Tool

### Tool 1: Island of Agreement ✅
```
Analyze using Island of Agreement:
- Situation: Complex humanitarian crisis in a country with disputed access to beneficiaries
- Organization: UN Relief Agency
- Counterpart: Government Ministry
- Description: The UN needs full access to deliver aid, the government wants to control all operations and reporting
```

### Tool 2: Icebergs ✅
```
Analyze the icebergs between UN and Government:

UN positions: Full access, international staff, transparent reporting
UN reasoning: Security needs, donor requirements, accountability
UN motives: Help people, maintain credibility, ensure safety

Government positions: Limited access, only local staff, restricted reports
Government reasoning: Sovereignty protection, security concerns
Government motives: Maintain control, protect reputation
```

### Tool 3: Stakeholders ✅
```
Analyze these stakeholders for the crisis:
Context: Multi-agency humanitarian response requiring coordination

Stakeholders:
1. Riverland Government - Power: 0.9, Urgency: 0.8, Legitimacy: 0.95, Position: 0.6
2. GRN (Armed Group) - Power: 0.7, Urgency: 0.9, Legitimacy: 0.3, Position: -0.8
3. Local NGOs - Power: 0.5, Urgency: 0.8, Legitimacy: 0.7, Position: 0.7
4. Donors - Power: 0.6, Urgency: 0.7, Legitimacy: 0.8, Position: 0.8
5. Media - Power: 0.4, Urgency: 0.6, Legitimacy: 0.6, Position: 0.5
```

### Tool 4: Leverage Influence ⚠️ REQUIRES MANUAL DATA PASSING

**Important**: This tool needs the complete output from Tool 3.

After running Tool 3, ask Claude:
```
Based on the stakeholder analysis you just provided, develop influence tactics for Riverland Government.

Please include the complete analysis data (the full JSON output with all stakeholders).
```

**OR** copy the Tool 3 output and paste it directly:
```
Develop influence tactics for Riverland Government using this stakeholder analysis:

[PASTE THE COMPLETE TOOL 3 OUTPUT HERE]
```

### Tool 5: Guide ✅
```
Show me the comprehensive guide to all negotiation methodologies available.
```

## Complete Workflow Example

### Step 1: Gather Data
Provide all information about your negotiation

### Step 2: Island of Agreement
Understand the common ground

### Step 3: Icebergs
Dig deeper into interests and values

### Step 4: Stakeholders
Map all relevant actors and their influence

### Step 5: Leverage Influence
Develop specific tactics for key stakeholders (requires passing data from Step 4)

### Step 6: Guide
Reference the methodologies as needed

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Tool not appearing | Reload ChatGPT, check schema JSON validity |
| "Validation error" | Ensure situation_description is at least 50 characters |
| Tool 4 fails to run | Make sure you're providing the complete stakeholder analysis JSON |
| API timeout | The server is responding slowly; try again in a moment |

## Schema File Location

The file `OPENAI_COMPLETE_SCHEMA.json` in this repo contains the complete OpenAPI specification. Update it in ChatGPT whenever you see changes.

## Production Server

```
URL: https://humanitarian-mcp-904769523449.us-central1.run.app
Status: Always online
Health check: https://humanitarian-mcp-904769523449.us-central1.run.app/health
```

## All Tools Summary

| # | Tool | Input | Output | Notes |
|---|------|-------|--------|-------|
| 1 | Island of Agreement | Situation + parties | Contested/agreed facts & norms | ✅ Standalone |
| 2 | Icebergs | Positions, reasoning, motives | Common shared space analysis | ✅ Standalone |
| 3 | Stakeholders | List of actors + ratings | Prioritized stakeholders | ✅ Standalone |
| 4 | Leverage Influence | Target + Tool 3 output | Influence tactics | ⚠️ Needs Tool 3 data |
| 5 | Guide | (none) | Complete methodology guide | ✅ Reference |
