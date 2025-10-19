# Humanitarian Negotiation MCP Server

A Model Context Protocol (MCP) server providing specialized tools for analyzing and conducting humanitarian negotiations in high-stakes, complex environments.

**Developed by**: Jhozman Camacho
**License**: MIT
**Repository**: Available for public use and contribution

## Overview

This MCP server implements three proven methodologies used by humanitarian negotiators, mediators, and aid workers:

1. **Island of Agreement (IoA)** - Establishes common ground by categorizing negotiation elements into contested/agreed facts and convergent/divergent norms
2. **Iceberg & Common Shared Space (CSS)** - Reveals the hidden structure of positions by examining what parties say (positions), how they think (reasoning), and why they act (motives/values)
3. **Stakeholder Analysis** - Systematically maps, prioritizes, and develops engagement strategies for all relevant actors based on their power, urgency, legitimacy, and position

## Features

- **Structured Analysis**: Transform complex negotiation contexts into actionable frameworks
- **Evidence-Based Recommendations**: Receive prioritized strategies based on proven methodologies
- **Flexible Output Formats**: Get results in Markdown (human-readable) or JSON (machine-readable)
- **Relationship Mapping**: Visualize influence pathways and identify key intermediaries
- **Coalition Building**: Discover opportunities to build alliances and neutralize opposition
- **Risk Mitigation**: Identify potential pitfalls and receive specific mitigation strategies

## Tools Available

### Core Analysis Tools

1. **`humanitarian_create_island_of_agreement`**
   - Creates IoA table with contested/agreed facts and convergent/divergent norms
   - Provides strategic recommendations on what to prioritize and avoid
   - Best used at the start of negotiation planning

2. **`humanitarian_analyze_icebergs`**
   - Compares both parties' positions, reasoning, and motives
   - Identifies Common Shared Space for compromise
   - Suggests specific opportunities for mutual gain

3. **`humanitarian_analyze_stakeholders`**
   - Characterizes stakeholders by Power, Urgency, Legitimacy, and Position
   - Prioritizes stakeholders into First/Second/Third priority levels
   - Maps relationships and influence pathways
   - Develops engagement strategies for each priority level

4. **`humanitarian_leverage_stakeholder_influence`**
   - Develops specific tactics to influence a target stakeholder
   - Identifies direct and indirect influence pathways
   - Recommends coalition opportunities and risk mitigation

### Utility Tools

5. **`humanitarian_negotiation_guide`**
   - Comprehensive guide to all methodologies
   - Best practices and workflow recommendations
   - Tool selection guidance

## Installation

### Quick Start (Automated)

**Windows Users:**
```bash
INSTALL_MCP_CLAUDE_DESKTOP.bat
```
This script will automatically:
- Verify Python installation
- Install all dependencies
- Configure Claude Desktop
- Validate the setup

Then restart Claude Desktop and you're ready to go!

### Prerequisites

- Python 3.10 or higher
- pip package manager
- Claude Desktop application

### Manual Installation

1. **Install dependencies:**
```bash
pip install -r requirements_mcp.txt
```

2. **Locate your Claude Desktop config:**
   - **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - **Windows**: `%APPDATA%/Claude/claude_desktop_config.json`
   - **Linux**: `~/.config/Claude/claude_desktop_config.json`

3. **Add the server configuration:**
```json
{
  "mcpServers": {
    "humanitarian-negotiation": {
      "command": "python",
      "args": ["/absolute/path/to/humanitarian_negotiation_mcp.py"]
    }
  }
}
```

4. **Restart Claude Desktop**

### Verification

After installation, you should see these 5 tools available in Claude Desktop:
- `humanitarian_create_island_of_agreement`
- `humanitarian_analyze_icebergs`
- `humanitarian_analyze_stakeholders`
- `humanitarian_leverage_stakeholder_influence`
- `humanitarian_negotiation_guide`

## Usage Examples

### Example 1: Starting a New Negotiation

```
Use the humanitarian_create_island_of_agreement tool to analyze my situation:

Situation: UN agency negotiating with regional government for access to IDP camps 
where 50,000 displaced persons need immediate food assistance. Government demands 
all operations be coordinated through Ministry of Interior. Security situation is 
volatile with recent armed clashes in the area.

Organization: World Food Programme
Counterpart: Ministry of Interior, Regional Government
```

**Result**: You'll receive an IoA table showing which facts are agreed upon (e.g., 50,000 people need assistance) vs. contested (e.g., exact locations, security assessment), and which norms are shared (humanitarian imperative) vs. divergent (sovereignty concerns).

### Example 2: Understanding Deeper Motivations

```
Use humanitarian_analyze_icebergs to compare positions:

Organization: International Medical Corps
Positions: 
- Unrestricted access to all affected areas
- Guarantee of staff safety and freedom of movement
- Direct communication with beneficiary communities

Reasoning:
- Need to assess medical needs accurately
- Staff safety essential for sustained operations
- Direct contact ensures aid reaches intended recipients

Motives:
- Humanitarian imperative to prevent deaths
- Medical neutrality and impartiality
- Accountability to donors and beneficiaries

Counterpart: National Security Council
Positions:
- All access must be pre-approved
- Military escort required in contested zones
- No direct contact with certain population groups
```

**Result**: Iceberg analysis revealing that both parties share concern about reputational risk, suggesting a compromise around transparent reporting mechanisms and joint monitoring.

### Example 3: Stakeholder Mapping

```
Use humanitarian_analyze_stakeholders for:

Context: Negotiating ceasefire agreement for humanitarian corridor

Stakeholders:
1. Chief Military Commander (Power: 1.0, Urgency: 0.7, Legitimacy: 0.8, Position: -0.5)
2. UN Secretary General's Special Envoy (Power: 0.8, Urgency: 1.0, Legitimacy: 1.0, Position: 1.0)
3. International Committee of the Red Cross (Power: 0.7, Urgency: 0.9, Legitimacy: 1.0, Position: 1.0)
4. Regional Governor (Power: 0.9, Urgency: 0.6, Legitimacy: 0.7, Position: 0.0)
5. Local Community Leaders (Power: 0.4, Urgency: 1.0, Legitimacy: 0.9, Position: 0.5)
```

**Result**: Priority rankings showing which stakeholders need active engagement (First Priority: Military Commander, UN Envoy, ICRC) and specific engagement strategies for each.

### Example 4: Influencing a Key Stakeholder

```
After stakeholder analysis, use humanitarian_leverage_stakeholder_influence:

Target: Chief Military Commander
[Provide previous stakeholder analysis JSON]
```

**Result**: Specific tactics showing which supportive stakeholders can advocate to the Commander, how to neutralize opposed influencers, and coalition-building opportunities.

## Methodology Overview

### Island of Agreement

**Purpose**: Establish negotiation foundation by separating facts from norms, and agreed elements from contested ones.

**When to Use**: 
- Beginning of negotiation
- When parties are polarized
- Need to find common ground

**Key Output**: 4-column table (Contested Facts | Agreed Facts | Convergent Norms | Divergent Norms)

### Iceberg & Common Shared Space

**Purpose**: Understand the three-level structure of negotiation:
- **What** (Visible positions)
- **How** (Tactical reasoning)  
- **Why** (Core motives and values)

**When to Use**:
- After IoA analysis
- Positions seem incompatible
- Need creative solutions

**Key Output**: Side-by-side iceberg comparison with Common Shared Space and compromise opportunities

### Stakeholder Analysis

**Purpose**: Systematically identify, assess, prioritize, and engage stakeholders.

**Assessment Criteria**:
- **Power**: Ability to influence decisions (0.0-1.0)
- **Urgency**: Time-sensitivity of issue (0.0-1.0)
- **Legitimacy**: Relevance to contribute meaningfully (0.0-1.0)
- **Position**: Stance on issue (-1.0 to +1.0: Opposed to Supportive)

**Priority Levels**:
- **First Priority**: High Power AND Urgency AND Legitimacy → Active engagement
- **Second Priority**: Any two high attributes → Selective engagement
- **Third Priority**: One or fewer high attributes → Minimal engagement

**Key Output**: Characterization table, priority rankings, relationship mapping, engagement strategies

## Best Practices

### 1. Sequential Approach
Use tools in sequence for comprehensive analysis:
1. Island of Agreement (foundation)
2. Iceberg/CSS (deeper understanding)
3. Stakeholder Analysis (engagement planning)
4. Influence Leverage (tactical execution)

### 2. Regular Updates
- Negotiations are dynamic - update analyses as situations evolve
- Re-run stakeholder analysis if positions change significantly
- Adjust strategies based on outcomes

### 3. Evidence-Based Decisions
- Support contested facts with credible data
- Use joint fact-finding to resolve disagreements
- Document all agreements and understandings

### 4. Communication Style
- Maintain formal, professional tone
- Focus on shared interests and mutual benefits
- Avoid inflammatory or judgmental language
- Frame in terms of risk mitigation for all parties

### 5. Relationship Building
- Start with agreed facts and convergent norms
- Build trust incrementally through small wins
- Demonstrate understanding of all perspectives
- Seek solutions that allow all parties to "save face"

## Limitations

- **Analysis Quality**: Output quality depends on input quality. Provide comprehensive, accurate context.
- **Dynamic Situations**: Analyses represent snapshots in time. Update regularly as situations evolve.
- **Cultural Context**: Tools provide general frameworks. Adapt recommendations to specific cultural contexts.
- **Human Judgment**: Tools support decision-making but don't replace experienced negotiator judgment.

## Use Cases

### Humanitarian Access Negotiations
- Negotiating with governments or armed groups for access to affected populations
- Establishing humanitarian corridors or ceasefires
- Coordinating multi-agency responses

### Inter-Organizational Coordination
- Resolving conflicts between UN agencies
- Coordinating with military forces on civil-military cooperation
- Aligning donor priorities with operational needs

### Community Engagement
- Negotiating with local authorities and leaders
- Managing community expectations and participation
- Resolving disputes over aid distribution

### Crisis Response Planning
- Multi-stakeholder coordination for emergency response
- Negotiating resource allocation among agencies
- Establishing coordination mechanisms under pressure

## Support and Feedback

This MCP server implements established humanitarian negotiation frameworks used in:
- UN humanitarian operations
- International Committee of the Red Cross (ICRC) negotiations
- NGO coordination in complex emergencies

For questions about specific use cases or to report issues, provide detailed context including:
- Negotiation type and stage
- Parties involved
- Specific challenges faced
- Tool outputs received

## License

This project is licensed under the MIT License - see below for details.

```
MIT License

Copyright (c) 2025 Jhozman Camacho

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Author

**Jhozman Camacho** - Initial development and architecture

## Acknowledgments

This MCP server implements established humanitarian negotiation practices and frameworks:
- Island of Agreement (IoA) methodology used in UN humanitarian operations
- Iceberg and Common Shared Space (CSS) analysis from ICRC negotiation practices
- Stakeholder Analysis framework adapted from Mitchell-Agle-Wood model for humanitarian contexts

Special thanks to:
- Anthropic for the Model Context Protocol (MCP)
- The humanitarian negotiation community for validated methodologies
- All contributors and users providing feedback and improvements
