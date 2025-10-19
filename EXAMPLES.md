# Humanitarian Negotiation MCP Server - Practical Examples

This document provides complete, ready-to-use examples for each tool in the humanitarian negotiation MCP server.

## Table of Contents
1. [Island of Agreement Examples](#island-of-agreement-examples)
2. [Iceberg & CSS Examples](#iceberg--css-examples)
3. [Stakeholder Analysis Examples](#stakeholder-analysis-examples)
4. [Influence Leverage Examples](#influence-leverage-examples)

---

## Island of Agreement Examples

### Example 1: Food Aid Access Negotiation

**Scenario**: WFP negotiating with government for access to drought-affected areas

**Prompt to Claude**:
```
Use humanitarian_create_island_of_agreement with:

situation_description: "World Food Programme is negotiating with the Ministry of Agriculture 
to deliver emergency food assistance to 75,000 people affected by severe drought in the 
northern provinces. The government insists all food distribution must go through government 
channels and local authorities. WFP is concerned about targeting accuracy and timely delivery. 
The drought has created food insecurity affecting multiple provinces, with children particularly 
vulnerable to malnutrition. Government has limited capacity to reach all affected areas. 
International donors have pledged funds but require direct WFP oversight. Security situation 
is generally stable but some areas have limited road access during rainy season."

organization_name: "World Food Programme (WFP)"

counterpart_name: "Ministry of Agriculture, National Government"

additional_context: "This is the first major emergency response in this country. Government 
is sensitive about sovereignty and international presence. Previous small-scale programs 
worked well with joint implementation."

response_format: "markdown"

detail_level: "detailed"
```

**Expected Output**: IoA table with:
- Contested Facts: Exact targeting criteria, delivery timelines, capacity assessment
- Agreed Facts: 75,000 people need assistance, drought severity, government-WFP partnership
- Convergent Norms: Right to food, accountability to beneficiaries, efficient use of resources
- Divergent Norms: Operational control, targeting methodology, reporting requirements

---

### Example 2: Medical Access in Conflict Zone

**Scenario**: Médecins Sans Frontières negotiating hospital access

**Prompt to Claude**:
```
Use humanitarian_create_island_of_agreement with:

situation_description: "Médecins Sans Frontières (MSF) seeks to establish a surgical hospital 
in a city affected by armed conflict. The Ministry of Health supports medical services but 
military authorities require extensive security clearances. The city has 200,000 residents 
with only one functional hospital operating at 300% capacity. MSF proposes a 50-bed surgical 
facility focusing on trauma and maternal care. Military insists on vetting all staff and 
controlling access routes. Civilian casualties are increasing. International humanitarian law 
guarantees medical care for wounded. Both parties acknowledge the medical emergency but disagree 
on operational modalities."

organization_name: "Médecins Sans Frontières (MSF)"

counterpart_name: "Joint Military-Health Authority"

response_format: "markdown"

detail_level: "detailed"
```

---

## Iceberg & CSS Examples

### Example 1: Access Restrictions Analysis

**Scenario**: Comparing UN agency and government positions on movement restrictions

**Prompt to Claude**:
```
Use humanitarian_analyze_icebergs with:

organization_name: "UNHCR"

counterpart_name: "Department of Border Security"

organization_positions: [
  "Unrestricted access to refugee camps for protection monitoring",
  "Ability to conduct private interviews with asylum seekers",
  "Freedom to move between camps without prior authorization",
  "Independent needs assessments"
]

organization_reasoning: [
  "Protection monitoring requires confidential conversations to identify threats",
  "Private interviews essential to detect exploitation and abuse",
  "Rapid response to protection incidents requires immediate access",
  "Independent assessment ensures objective needs identification"
]

organization_motives: [
  "Mandate to protect refugees under international law",
  "Accountability to refugees for their safety and wellbeing",
  "Duty to report protection violations to international community",
  "Humanitarian principle of independence"
]

counterpart_positions: [
  "All camp visits must be pre-approved 72 hours in advance",
  "Government liaison officer must accompany all visits",
  "Interview topics must be disclosed beforehand",
  "Joint assessment teams only"
]

counterpart_assumed_reasoning: [
  "Need to maintain security and prevent unauthorized activities",
  "Ensure refugees don't receive mixed messages from different actors",
  "Government must be aware of any issues to address them",
  "Coordinate all assessments to avoid duplication"
]

counterpart_assumed_motives: [
  "Sovereignty and control over national territory",
  "Prevent refugees from being used for political purposes",
  "Demonstrate government is managing refugee situation competently",
  "Avoid international criticism of refugee treatment"
]

response_format: "markdown"
```

**Expected Output**: Comparative iceberg showing:
- Common Shared Space: Both want to avoid refugee exploitation, both seek orderly operations, both concerned about reputational risk
- Compromise Opportunities: Joint protection protocols, graduated access system, shared reporting framework

---

### Example 2: Aid Coordination Dispute

**Scenario**: International NGO and local government disagreeing on coordination mechanisms

**Prompt to Claude**:
```
Use humanitarian_analyze_icebergs with:

organization_name: "International Rescue Committee (IRC)"

counterpart_name: "Provincial Disaster Management Authority"

organization_positions: [
  "IRC should have direct relationships with affected communities",
  "Flexibility to adjust programs based on community feedback",
  "Independent monitoring and evaluation",
  "Rapid procurement and implementation processes"
]

organization_reasoning: [
  "Community-driven approach ensures programs meet actual needs",
  "Flexibility allows adaptation to changing circumstances",
  "Independent M&E maintains donor confidence and accountability",
  "Speed is essential in emergency response"
]

organization_motives: [
  "Effectiveness - reaching those most in need",
  "Accountability to donors and beneficiaries",
  "Humanitarian principles of humanity and impartiality",
  "Organizational reputation for quality programming"
]

counterpart_positions: [
  "All programs must be approved through provincial coordination mechanism",
  "IRC should strengthen government systems, not parallel structures",
  "Joint monitoring with government officials",
  "Follow government procurement procedures"
]

counterpart_assumed_reasoning: [
  "Government must coordinate to avoid gaps and overlaps",
  "Building government capacity ensures sustainability",
  "Government needs visibility into all activities in province",
  "National procedures ensure accountability and prevent corruption"
]

counterpart_assumed_motives: [
  "Sovereignty and government authority",
  "Long-term capacity building and sustainability",
  "Political legitimacy through visible disaster response",
  "Avoid appearance of government incapacity"
]

response_format: "markdown"
```

---

## Stakeholder Analysis Examples

### Example 1: Multi-Party Ceasefire Negotiation

**Scenario**: Negotiating humanitarian pause for vaccination campaign

**Prompt to Claude**:
```
Use humanitarian_analyze_stakeholders with:

negotiation_context: "Negotiating 5-day ceasefire for polio vaccination campaign reaching 500,000 children in conflict-affected areas"

stakeholders: [
  {
    "name": "UN Special Envoy for Peace",
    "power": 0.9,
    "urgency": 1.0,
    "legitimacy": 1.0,
    "position": 1.0,
    "role": "International Mediator",
    "influence_connections": ["Government Chief Negotiator", "Armed Opposition Leader", "Regional Bloc Chair"]
  },
  {
    "name": "Government Chief Negotiator",
    "power": 1.0,
    "urgency": 0.6,
    "legitimacy": 0.8,
    "position": 0.2,
    "role": "Government Representative",
    "influence_connections": ["Minister of Defense", "President's Chief of Staff"]
  },
  {
    "name": "Armed Opposition Leader",
    "power": 0.9,
    "urgency": 0.5,
    "legitimacy": 0.6,
    "position": -0.3,
    "role": "Military Commander",
    "influence_connections": ["Opposition Political Wing", "External State Sponsor"]
  },
  {
    "name": "UNICEF Country Representative",
    "power": 0.7,
    "urgency": 1.0,
    "legitimacy": 1.0,
    "position": 1.0,
    "role": "UN Agency Head",
    "influence_connections": ["UN Special Envoy for Peace", "WHO Representative", "Donor Coordination Group"]
  },
  {
    "name": "WHO Representative",
    "power": 0.6,
    "urgency": 1.0,
    "legitimacy": 1.0,
    "position": 1.0,
    "role": "Technical Health Authority",
    "influence_connections": ["UNICEF Country Representative", "Ministry of Health"]
  },
  {
    "name": "Minister of Defense",
    "power": 0.95,
    "urgency": 0.7,
    "legitimacy": 0.7,
    "position": -0.4,
    "role": "Security Authority",
    "influence_connections": ["Government Chief Negotiator", "Military Chiefs of Staff"]
  },
  {
    "name": "Regional Bloc Chair",
    "power": 0.8,
    "urgency": 0.8,
    "legitimacy": 0.9,
    "position": 0.7,
    "role": "Regional Political Leader",
    "influence_connections": ["Government Chief Negotiator", "External State Sponsor", "International Donor Group"]
  },
  {
    "name": "External State Sponsor (Opposition)",
    "power": 0.85,
    "urgency": 0.5,
    "legitimacy": 0.5,
    "position": -0.2,
    "role": "External Backer",
    "influence_connections": ["Armed Opposition Leader", "Opposition Political Wing"]
  },
  {
    "name": "Local Religious Leaders Council",
    "power": 0.5,
    "urgency": 0.9,
    "legitimacy": 0.9,
    "position": 0.8,
    "role": "Community Representatives",
    "influence_connections": ["Community Elders", "Local Population"]
  },
  {
    "name": "International Media Correspondent",
    "power": 0.4,
    "urgency": 0.7,
    "legitimacy": 0.6,
    "position": 0.5,
    "role": "Media/Public Opinion",
    "influence_connections": []
  }
]

response_format: "markdown"
```

**Expected Output**: 
- Characterization table showing all stakeholders
- First Priority: UN Special Envoy, UNICEF, WHO, Government Negotiator, Opposition Leader, Minister of Defense, Regional Bloc Chair
- Engagement strategies for each priority level
- Relationship mapping showing influence pathways

---

### Example 2: Aid Distribution Coordination

**Scenario**: Coordinating multiple actors for flood response

**Prompt to Claude**:
```
Use humanitarian_analyze_stakeholders with:

negotiation_context: "Coordinating flood response affecting 100,000 people - establishing distribution sites and logistics"

stakeholders: [
  {
    "name": "Provincial Governor",
    "power": 0.95,
    "urgency": 0.9,
    "legitimacy": 0.8,
    "position": 0.3,
    "role": "Local Government Authority",
    "influence_connections": ["District Commissioner", "Provincial Police Chief", "National Disaster Agency"]
  },
  {
    "name": "WFP Logistics Coordinator",
    "power": 0.8,
    "urgency": 1.0,
    "legitimacy": 1.0,
    "position": 1.0,
    "role": "UN Agency Lead",
    "influence_connections": ["OCHA Head of Office", "NGO Consortium Chair"]
  },
  {
    "name": "National Disaster Management Agency Director",
    "power": 0.85,
    "urgency": 0.9,
    "legitimacy": 0.9,
    "position": 0.5,
    "role": "National Coordinator",
    "influence_connections": ["Provincial Governor", "Ministry of Interior", "International Partners"]
  },
  {
    "name": "NGO Consortium Chair (Oxfam)",
    "power": 0.6,
    "urgency": 1.0,
    "legitimacy": 0.9,
    "position": 0.9,
    "role": "Civil Society Coordinator",
    "influence_connections": ["Local NGO Network", "Donor Group"]
  },
  {
    "name": "Military Logistics Commander",
    "power": 0.9,
    "urgency": 0.7,
    "legitimacy": 0.7,
    "position": 0.0,
    "role": "Military Support",
    "influence_connections": ["Provincial Governor", "Minister of Defense"]
  },
  {
    "name": "Affected Community Representatives (6 villages)",
    "power": 0.3,
    "urgency": 1.0,
    "legitimacy": 1.0,
    "position": 0.6,
    "role": "Beneficiaries",
    "influence_connections": ["NGO Consortium Chair", "Media"]
  },
  {
    "name": "Private Logistics Company CEO",
    "power": 0.5,
    "urgency": 0.6,
    "legitimacy": 0.5,
    "position": 0.7,
    "role": "Commercial Partner",
    "influence_connections": ["WFP Logistics Coordinator"]
  }
]

response_format: "markdown"
```

---

## Influence Leverage Examples

### Example 1: Influencing Opposition Military Leader

**Scenario**: Using stakeholder network to shift armed group leader's position on ceasefire

**Prompt to Claude**:
```
First, run humanitarian_analyze_stakeholders (see Example 1 above), then:

Use humanitarian_leverage_stakeholder_influence with:

target_stakeholder: "Armed Opposition Leader"

stakeholder_analysis_data: [Paste the JSON output from the previous humanitarian_analyze_stakeholders call]

response_format: "markdown"
```

**Expected Output**:
- Direct influence pathways through UN Special Envoy and External State Sponsor
- Tactics for leveraging Regional Bloc Chair as intermediary
- Coalition opportunities with Opposition Political Wing
- Risk mitigation strategies for Minister of Defense opposition

---

### Example 2: Influencing Resistant Government Official

**Scenario**: Shifting Provincial Governor from neutral to supportive

**Prompt to Claude**:
```
After running stakeholder analysis from Example 2:

Use humanitarian_leverage_stakeholder_influence with:

target_stakeholder: "Provincial Governor"

stakeholder_analysis_data: [Paste JSON from flood response stakeholder analysis]

response_format: "markdown"
```

**Expected Output**:
- Leverage National Disaster Agency Director's supportive influence
- Use Military Logistics Commander as neutral bridge
- Build coalition with Provincial Police Chief and District Commissioner
- Address concerns through community representatives' legitimacy

---

## Complete Workflow Example

### Scenario: Comprehensive Analysis for IDP Camp Access

**Step 1: Island of Agreement**
```
Use humanitarian_create_island_of_agreement with:

situation_description: "UNHCR seeking to establish protection presence in IDP camp housing 
35,000 displaced persons. Camp is managed by Ministry of Interior. Recent allegations of 
forced returns and restricted freedom of movement. Government claims all IDPs are there 
voluntarily and have freedom to leave. International human rights groups expressing concern. 
UNHCR wants regular access for protection monitoring. Government wants all activities 
coordinated through government focal point."

organization_name: "UNHCR"
counterpart_name: "Ministry of Interior"
response_format: "markdown"
detail_level: "detailed"
```

**Step 2: Iceberg Analysis** (wait for IoA results, then):
```
Use humanitarian_analyze_icebergs with details from IoA analysis...
```

**Step 3: Stakeholder Analysis**
```
Use humanitarian_analyze_stakeholders with comprehensive stakeholder list...
```

**Step 4: Influence Tactics** (targeting key resistant stakeholder):
```
Use humanitarian_leverage_stakeholder_influence focusing on Minister of Interior...
```

---

## Tips for Effective Use

### Input Quality
- Provide comprehensive situation descriptions (200-500 words ideal)
- Be specific about positions, reasoning, and motives
- Include relevant context (history, constraints, external factors)
- Use concrete examples rather than generalities

### Sequential Analysis
- Always start with Island of Agreement for foundation
- Use Iceberg analysis to understand deeper motivations
- Conduct Stakeholder Analysis for engagement planning
- Apply Influence Leverage for specific tactical situations

### Iterative Refinement
- Re-run analyses as situations evolve
- Update stakeholder positions as negotiations progress
- Adjust strategies based on actual outcomes
- Document lessons learned for future negotiations

### Output Utilization
- Use Markdown output for presentations and briefings
- Use JSON output for integration with other tools
- Extract specific recommendations for action plans
- Share analyses with team members for coordination

---

## Common Pitfalls to Avoid

1. **Insufficient Context**: Providing too little background information
2. **Premature Tactics**: Jumping to influence tactics without foundation analysis
3. **Static Analysis**: Not updating analyses as situations change
4. **Ignoring Relationships**: Overlooking influence connections between stakeholders
5. **Cultural Blindness**: Not adapting recommendations to local context
6. **Over-Reliance**: Treating tool outputs as final decisions rather than informed recommendations

---

## Additional Resources

- See README.md for methodology overviews
- Use `humanitarian_negotiation_guide` tool for comprehensive methodology guide
- Review actual negotiation documentation for your organization's specific protocols
- Consult experienced negotiators for context-specific guidance

---

**Remember**: These tools support decision-making but don't replace experienced professional judgment, cultural awareness, and adaptive strategy.
