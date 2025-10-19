# Quick Start Guide - Humanitarian Negotiation MCP Server

## Installation (3 Minutes)

### Step 1: Install Dependencies
```bash
pip install -r requirements_mcp.txt
```

### Step 2: Run Setup Script
```bash
python setup.py
```

This will automatically:
- Check your Python version
- Verify dependencies
- Locate your Claude Desktop config
- Add the server configuration
- Provide next steps

### Step 3: Restart Claude Desktop

Close and reopen Claude Desktop. Look for the 🔌 icon to verify the MCP server is connected.

---

## First Use (5 Minutes)

### 1. Get the Guide
```
Use the humanitarian_negotiation_guide tool
```

This shows you all methodologies and how to use them.

### 2. Try Island of Agreement

Start a conversation with Claude:

```
I need to analyze a humanitarian negotiation using the Island of Agreement methodology.

Situation: [Describe your situation in 2-3 paragraphs]
My Organization: [Your org name]
Counterpart: [Their name]
```

Claude will use the `humanitarian_create_island_of_agreement` tool automatically.

### 3. Proceed to Iceberg Analysis

After reviewing your IoA results:

```
Now conduct an Iceberg and Common Shared Space analysis comparing us with [counterpart name].

Our positions: [List 3-5 demands]
Our reasoning: [Why these demands]
Our motives: [Deep values driving you]

Their positions: [What you know]
Their reasoning: [If known]
Their motives: [If known]
```

### 4. Map Stakeholders

```
Analyze the stakeholders in this negotiation:

[List each stakeholder with:
- Name and role
- Power (0-1): [estimate]
- Urgency (0-1): [estimate]  
- Legitimacy (0-1): [estimate]
- Position (-1 to 1): [estimate]
- Who they influence: [list names]
]
```

### 5. Target Influence

```
Develop influence tactics for [target stakeholder name] using the previous stakeholder analysis.
```

---

## Common Use Cases

### Emergency Response Coordination
```
I'm coordinating a rapid response to [disaster type] affecting [number] people. 
Multiple agencies are involved: [list]. We need to establish [coordination mechanism].
Analyze the stakeholders and recommend engagement strategies.
```

### Access Negotiation
```
We're negotiating access to [location] for [purpose]. The government is requiring
[restrictions]. Create an Island of Agreement showing what we can build on vs. 
what needs negotiation.
```

### Inter-Agency Disputes
```
There's a dispute between [agency 1] and [agency 2] over [issue]. Conduct an 
Iceberg analysis to understand underlying motivations and find compromise opportunities.
```

---

## Tips for Best Results

### Provide Rich Context
✓ Include numbers, locations, timeframes
✓ Describe constraints and challenges  
✓ Mention relevant history or precedents
✗ Don't be vague or generic

### Be Specific About Stakeholders
✓ Use real names or clear titles
✓ Estimate attributes thoughtfully
✓ Map influence connections
✗ Don't guess wildly at values

### Use Sequential Analysis
1. Start with Island of Agreement (foundation)
2. Then Iceberg Analysis (depth)
3. Then Stakeholder Analysis (engagement)
4. Then Influence Tactics (execution)

### Update Regularly
- Re-run analyses when situations change
- Update stakeholder positions as they shift
- Refine strategies based on outcomes

---

## Troubleshooting

### "Server not found" or "Connection error"
- Verify server is in Claude Desktop config
- Check the file path is correct
- Restart Claude Desktop
- Run `python humanitarian_negotiation_mcp.py` to check for errors

### "Invalid input" errors
- Check that all required fields are provided
- Verify numeric values are in correct ranges (0-1 for Power/Urgency/Legitimacy, -1 to 1 for Position)
- Ensure stakeholder names match exactly when using influence tool

### Poor quality outputs
- Provide more detailed context (200-500 words ideal)
- Be specific about positions, reasoning, motives
- Include relevant background and constraints
- Use concrete examples vs. generalities

### Server not appearing in Claude
- Run setup.py again to verify configuration
- Check Claude Desktop config file manually
- Ensure Python and dependencies are installed
- Look at Claude Desktop logs for errors

---

## Getting Help

1. **Read the documentation**
   - README.md - Full overview
   - EXAMPLES.md - Practical examples
   - This file - Quick start

2. **Use the guide tool**
   ```
   Use humanitarian_negotiation_guide
   ```

3. **Check examples**
   - EXAMPLES.md has complete, ready-to-use examples
   - Copy and adapt for your situation

4. **Verify setup**
   ```bash
   python setup.py
   ```

---

## What Each Tool Does

| Tool | Purpose | When to Use |
|------|---------|-------------|
| `humanitarian_negotiation_guide` | Get comprehensive methodology guide | Starting out, need refresher |
| `humanitarian_create_island_of_agreement` | Map facts and norms | Beginning of negotiation |
| `humanitarian_analyze_icebergs` | Understand deep motivations | After IoA, seeking compromise |
| `humanitarian_analyze_stakeholders` | Map and prioritize actors | Complex multi-party situations |
| `humanitarian_leverage_stakeholder_influence` | Develop influence tactics | Targeting specific stakeholder |

---

## Example Session Flow

```
User: I need help with a negotiation. We're trying to get access to IDP camps.

Claude: I can help you analyze this using humanitarian negotiation methodologies. 
Let me start by creating an Island of Agreement. Could you provide:
- Detailed situation description
- Your organization name
- Counterpart organization name

User: [Provides details]

Claude: [Uses humanitarian_create_island_of_agreement tool]
Here's your Island of Agreement analysis... [results]

Based on this, I recommend [strategic guidance]. Would you like me to:
1. Conduct an Iceberg analysis to understand deeper motivations?
2. Analyze stakeholders to map influence?
3. Both?

User: Let's do the Iceberg analysis

Claude: I'll need your positions, reasoning, and motives, plus what you know 
about the counterpart's...

[And so on...]
```

---

## Key Principles

1. **Evidence-Based**: Support claims with data
2. **Sequential**: Build from foundation to tactics
3. **Adaptive**: Update as situations evolve
4. **Relationship-Focused**: Build trust incrementally
5. **Principle-Driven**: Stay grounded in humanitarian values

---

## Next Steps After Setup

1. ✓ Install and configure (you're done!)
2. → Read EXAMPLES.md for practical scenarios
3. → Try your first analysis with real situation
4. → Share with team members
5. → Iterate and refine based on outcomes

---

**You're ready to go! Start by asking Claude to use the humanitarian negotiation tools for your situation.**
