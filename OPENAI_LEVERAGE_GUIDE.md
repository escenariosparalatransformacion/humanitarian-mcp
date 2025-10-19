# How to Use Leverage Influence Tool (Tool 4) in OpenAI

## The Problem

OpenAI doesn't automatically pass the output from one tool to another. After running **Analyze Stakeholders** (Tool 3), you need to **manually provide that data** to the **Leverage Influence** tool (Tool 4).

## Solution: Copy and Paste Pattern

### Step 1: Run Stakeholder Analysis (Tool 3)

Ask Claude to analyze your stakeholders:

```
Analyze these stakeholders:

Context: Complex humanitarian crisis requiring coordination between multiple parties...

Stakeholders:
1. Riverland Government - Power: 0.9, Urgency: 0.8, Legitimacy: 0.95, Position: 0.6
2. GRN (Rebel Group) - Power: 0.7, Urgency: 0.9, Legitimacy: 0.3, Position: -0.8
3. Local NGOs - Power: 0.5, Urgency: 0.8, Legitimacy: 0.7, Position: 0.7
4. Donors - Power: 0.6, Urgency: 0.7, Legitimacy: 0.8, Position: 0.8
5. Media - Power: 0.4, Urgency: 0.6, Legitimacy: 0.6, Position: 0.5
```

### Step 2: Get the Output

Claude will return something like:

```json
{
  "analysis_context": "Complex humanitarian crisis...",
  "total_stakeholders": 5,
  "stakeholders": [
    {
      "name": "Riverland Government",
      "power": 0.9,
      "urgency": 0.8,
      "legitimacy": 0.95,
      "position": 0.6,
      "salience_score": 2.65,
      "priority_level": "First",
      "influenced_by": [],
      "engagement_strategy": "Supportive"
    },
    ...more stakeholders...
  ],
  "priority_summary": {...}
}
```

### Step 3: Copy the ENTIRE Response

**Important**: You need to copy the COMPLETE JSON response from Tool 3, including:
- `analysis_context`
- `total_stakeholders`
- `stakeholders` (with all fields)
- `priority_summary`

### Step 4: Use Leverage Influence Tool

Ask Claude to develop tactics for a specific stakeholder, providing the full analysis:

```
Based on the stakeholder analysis I just received, develop influence tactics for the Riverland Government.

Here's the complete analysis:

[PASTE THE ENTIRE JSON FROM STEP 3 HERE]

Target stakeholder: Riverland Government
```

## Example: Complete Flow

### Input 1 - Analyze Stakeholders:
```
Analyze these 5 stakeholders:
Context: Multi-party humanitarian crisis in Riverland requiring coordination.

Stakeholders:
1. Riverland Government - Power: 0.9, Urgency: 0.8, Legitimacy: 0.95, Position: 0.6
2. GRN (Armed Group) - Power: 0.7, Urgency: 0.9, Legitimacy: 0.3, Position: -0.8
3. Local NGOs - Power: 0.5, Urgency: 0.8, Legitimacy: 0.7, Position: 0.7
4. International Donors - Power: 0.6, Urgency: 0.7, Legitimacy: 0.8, Position: 0.8
5. Media Networks - Power: 0.4, Urgency: 0.6, Legitimacy: 0.6, Position: 0.5
```

### Output 1 - Claude returns stakeholder analysis
```json
{
  "analysis_context": "Multi-party humanitarian crisis in Riverland...",
  "total_stakeholders": 5,
  "stakeholders": [
    {
      "name": "Riverland Government",
      "power": 0.9,
      "urgency": 0.8,
      "legitimacy": 0.95,
      "position": 0.6,
      "salience_score": 2.65,
      "priority_level": "First",
      "influenced_by": [],
      "engagement_strategy": "Supportive"
    },
    {
      "name": "GRN (Armed Group)",
      "power": 0.7,
      "urgency": 0.9,
      "legitimacy": 0.3,
      "position": -0.8,
      "salience_score": 1.9,
      "priority_level": "Second",
      "influenced_by": ["Media Networks"],
      "engagement_strategy": "Adversarial"
    },
    ...
  ],
  "priority_summary": {...}
}
```

### Input 2 - Leverage Influence (with copied data):
```
Now develop influence tactics for Riverland Government using this stakeholder analysis:

[PASTE THE COMPLETE JSON HERE]

Target: Riverland Government
```

### Output 2 - Claude develops tactics
```json
{
  "target_stakeholder": "Riverland Government",
  "target_profile": {
    "power": 0.9,
    "urgency": 0.8,
    "legitimacy": 0.95,
    "position": 0.6,
    "priority_level": "First"
  },
  "influence_strategy": {
    "primary_approach": "Coalition building",
    "target_psychology": "Leverage shared interests",
    "communication_tone": "Collaborative"
  },
  "tactical_options": [
    {
      "tactic": "Coalition Building",
      "description": "Unite with supportive stakeholders...",
      "allies": ["Local NGOs", "International Donors"]
    },
    ...
  ]
}
```

## Important Notes

1. **Don't manually edit** the JSON - copy it exactly as Claude returns it
2. **Include all fields** - the stakeholders array must have all properties
3. **One stakeholder at a time** - repeat the process for each stakeholder you want to influence
4. **Keep the structure** - the API expects the exact same structure that Tool 3 returns

## Troubleshooting

**Error: "Stakeholder 'X' not found in analysis"**
- Make sure the stakeholder name matches exactly (case-sensitive)
- Copy the complete JSON response, not a partial one

**Error: "Field required" for stakeholders_analysis_json**
- You must provide the complete JSON object
- Don't just provide the name and target

**It says the tool is trying to call but then fails**
- Make sure the JSON is valid (use https://jsonlint.com/ to verify)
- Check that all required fields are present
