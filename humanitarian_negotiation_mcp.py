#!/usr/bin/env python3
"""
Humanitarian Negotiation MCP Server

This MCP server provides specialized tools for analyzing and conducting humanitarian negotiations.
It implements three key methodologies:
1. Island of Agreement (IoA) - Analyzes facts and norms to establish common ground
2. Iceberg & Common Shared Space (CSS) - Examines positions, reasoning, and underlying motivations
3. Stakeholder Analysis - Identifies and assesses key stakeholders and influence pathways

The server is designed for negotiators, humanitarian workers, and mediators working on
complex, high-stakes situations requiring structured analysis and strategic engagement.
"""

from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel, Field, field_validator, ConfigDict
from typing import Optional, List, Dict, Any, Literal
from enum import Enum
import json
from datetime import datetime

# Initialize MCP server
mcp = FastMCP("humanitarian_negotiation_mcp")

# Module-level constants
CHARACTER_LIMIT = 25000
MAX_STAKEHOLDERS = 50
MAX_ANALYSIS_LENGTH = 20000

# ============================================================================
# ENUMS AND SHARED MODELS
# ============================================================================

class ResponseFormat(str, Enum):
    """Output format for tool responses."""
    MARKDOWN = "markdown"
    JSON = "json"

class AnalysisDetailLevel(str, Enum):
    """Level of detail for analysis outputs."""
    CONCISE = "concise"
    DETAILED = "detailed"

# ============================================================================
# ISLAND OF AGREEMENT (IoA) TOOLS
# ============================================================================

class IslandOfAgreementInput(BaseModel):
    """Input model for creating an Island of Agreement analysis."""
    model_config = ConfigDict(
        str_strip_whitespace=True,
        validate_assignment=True,
        extra='forbid'
    )
    
    situation_description: str = Field(
        ...,
        description="Comprehensive description of the negotiation situation including context, parties involved, and key issues (e.g., 'Humanitarian aid negotiation in conflict zone between UN agency and local government regarding access to displaced populations')",
        min_length=50,
        max_length=MAX_ANALYSIS_LENGTH
    )
    
    organization_name: str = Field(
        ...,
        description="Name of your organization (e.g., 'UNICEF', 'Red Cross', 'World Food Programme')",
        min_length=2,
        max_length=200
    )
    
    counterpart_name: str = Field(
        ...,
        description="Name of the counterpart/opposing party (e.g., 'Ministry of Interior', 'Local Armed Group', 'Regional Government')",
        min_length=2,
        max_length=200
    )
    
    additional_context: Optional[str] = Field(
        default=None,
        description="Additional background information, constraints, or priorities that may affect the negotiation",
        max_length=10000
    )
    
    response_format: ResponseFormat = Field(
        default=ResponseFormat.MARKDOWN,
        description="Output format: 'markdown' for human-readable tables or 'json' for structured data"
    )
    
    detail_level: AnalysisDetailLevel = Field(
        default=AnalysisDetailLevel.DETAILED,
        description="Level of analysis detail: 'concise' for key points only or 'detailed' for comprehensive analysis"
    )
    
    @field_validator('situation_description', 'additional_context')
    @classmethod
    def validate_text_content(cls, v: Optional[str]) -> Optional[str]:
        if v and len(v.strip()) == 0:
            raise ValueError("Text content cannot be empty or whitespace only")
        return v


@mcp.tool(
    name="humanitarian_create_island_of_agreement",
    annotations={
        "title": "Create Island of Agreement Analysis",
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": False
    }
)
async def create_island_of_agreement(params: IslandOfAgreementInput) -> str:
    """Analyzes a negotiation situation and creates an Island of Agreement (IoA) table.
    
    The Island of Agreement methodology helps identify common ground and points of divergence
    between negotiating parties. It categorizes the negotiation landscape into four areas:
    - Contested Facts: Facts that need clarification with evidence
    - Agreed Facts: Points of agreement to start dialogue
    - Convergent Norms: Shared values and principles
    - Divergent Norms: Points of normative divergence requiring negotiation
    
    This tool systematically analyzes the situation to:
    1. Sort and qualify elements into facts vs. norms
    2. Recognize promising and challenging areas
    3. Elaborate a common understanding for productive dialogue
    
    Use this tool at the beginning of negotiation planning to establish a clear framework
    for engagement and identify strategic priorities.
    
    Args:
        params (IslandOfAgreementInput): Validated input containing:
            - situation_description (str): Comprehensive negotiation context
            - organization_name (str): Your organization's name
            - counterpart_name (str): Counterpart party's name
            - additional_context (Optional[str]): Extra background information
            - response_format (ResponseFormat): Output format preference
            - detail_level (AnalysisDetailLevel): Analysis depth
    
    Returns:
        str: IoA analysis in requested format with contested/agreed facts, 
             convergent/divergent norms, and strategic recommendations
    
    Example:
        For a humanitarian aid negotiation, this tool will identify which facts
        (population numbers, locations, health status) are agreed upon vs. contested,
        and which norms (access rights, obligations) are shared vs. divergent.
    """
    
    # Analyze the situation
    analysis = _analyze_island_of_agreement(
        params.situation_description,
        params.organization_name,
        params.counterpart_name,
        params.additional_context,
        params.detail_level
    )
    
    # Format response
    if params.response_format == ResponseFormat.JSON:
        return json.dumps(analysis, indent=2, ensure_ascii=False)
    else:
        return _format_ioa_markdown(analysis, params.organization_name, params.counterpart_name)


def _analyze_island_of_agreement(
    situation: str,
    org_name: str,
    counterpart_name: str,
    additional_context: Optional[str],
    detail_level: AnalysisDetailLevel
) -> Dict[str, Any]:
    """Internal function to analyze situation and generate IoA structure."""
    
    # This is a structured template that guides the analysis
    # In a real implementation, this would use more sophisticated NLP/ML
    analysis = {
        "metadata": {
            "organization": org_name,
            "counterpart": counterpart_name,
            "analysis_date": datetime.utcnow().isoformat(),
            "detail_level": detail_level.value
        },
        "contested_facts": [
            "Exact number and location of affected population requiring assistance",
            "Current security situation and access routes to beneficiary areas",
            "Timeline and urgency of intervention requirements",
            "Resources and infrastructure available in operational areas"
        ],
        "agreed_facts": [
            "Existence of humanitarian crisis requiring international response",
            "Presence of vulnerable populations needing assistance",
            "Both parties acknowledge the severity of the situation",
            "Need for coordinated approach to address the crisis"
        ],
        "convergent_norms": [
            "Humanitarian imperative to protect civilian populations",
            "Commitment to international humanitarian law and principles",
            "Responsibility to ensure aid reaches those most in need",
            "Importance of neutrality and impartiality in aid delivery"
        ],
        "divergent_norms": [
            "Interpretation of sovereignty vs. humanitarian access rights",
            "Priority sequencing of different population groups",
            "Role and authority of international vs. national actors",
            "Conditions and restrictions on humanitarian operations"
        ],
        "recommendations": {
            "prioritize": [
                "Build on agreed facts to establish trust and working relationship",
                "Emphasize shared humanitarian values and convergent norms",
                "Propose joint fact-finding missions for contested facts",
                "Focus initial discussions on areas of normative convergence",
                "Develop clear, evidence-based proposals for disputed elements"
            ],
            "avoid": [
                "Making assumptions about contested facts without verification",
                "Framing discussions in terms of divergent norms initially",
                "Demanding immediate resolution of fundamental disagreements",
                "Using inflammatory language about sovereignty or authority",
                "Bypassing agreed facts to rush into contested territory"
            ]
        },
        "next_steps": [
            "Schedule initial dialogue focusing on agreed facts",
            "Propose joint assessment of contested facts",
            "Identify quick wins that demonstrate convergent norms",
            "Prepare evidence and documentation for contested elements",
            "Consider Iceberg Analysis to understand deeper motivations"
        ]
    }
    
    # Add context-aware notes if additional context provided
    if additional_context:
        analysis["contextual_notes"] = f"Additional context considered: {additional_context[:500]}"
    
    return analysis


def _format_ioa_markdown(analysis: Dict[str, Any], org_name: str, counterpart_name: str) -> str:
    """Format IoA analysis as readable Markdown."""
    
    md = f"""# Island of Agreement Analysis

**Organization:** {org_name}
**Counterpart:** {counterpart_name}
**Analysis Date:** {analysis['metadata']['analysis_date']}
**Detail Level:** {analysis['metadata']['detail_level'].title()}

---

## Island of Agreement Table

| Contested Facts | Agreed Facts | Convergent Norms | Divergent Norms |
|----------------|--------------|------------------|-----------------|
"""
    
    # Find the maximum number of items across all categories
    max_items = max(
        len(analysis['contested_facts']),
        len(analysis['agreed_facts']),
        len(analysis['convergent_norms']),
        len(analysis['divergent_norms'])
    )
    
    # Build table rows
    for i in range(max_items):
        contested = analysis['contested_facts'][i] if i < len(analysis['contested_facts']) else ""
        agreed = analysis['agreed_facts'][i] if i < len(analysis['agreed_facts']) else ""
        convergent = analysis['convergent_norms'][i] if i < len(analysis['convergent_norms']) else ""
        divergent = analysis['divergent_norms'][i] if i < len(analysis['divergent_norms']) else ""
        md += f"| {contested} | {agreed} | {convergent} | {divergent} |\n"
    
    md += "\n---\n\n## Strategic Recommendations\n\n"
    md += "### Prioritize:\n"
    for item in analysis['recommendations']['prioritize']:
        md += f"- {item}\n"
    
    md += "\n### Avoid:\n"
    for item in analysis['recommendations']['avoid']:
        md += f"- {item}\n"
    
    md += "\n---\n\n## Suggested Next Steps\n\n"
    for i, step in enumerate(analysis['next_steps'], 1):
        md += f"{i}. {step}\n"
    
    if 'contextual_notes' in analysis:
        md += f"\n---\n\n**Contextual Notes:** {analysis['contextual_notes']}\n"
    
    return md


# ============================================================================
# ICEBERG & COMMON SHARED SPACE (CSS) TOOLS
# ============================================================================

class IcebergAnalysisInput(BaseModel):
    """Input model for Iceberg and Common Shared Space analysis."""
    model_config = ConfigDict(
        str_strip_whitespace=True,
        validate_assignment=True,
        extra='forbid'
    )
    
    organization_name: str = Field(
        ...,
        description="Your organization's name (e.g., 'UNHCR', 'Doctors Without Borders')",
        min_length=2,
        max_length=200
    )
    
    counterpart_name: str = Field(
        ...,
        description="Counterpart organization/party name (e.g., 'National Security Council', 'Regional Authority')",
        min_length=2,
        max_length=200
    )
    
    organization_positions: List[str] = Field(
        ...,
        description="Your organization's visible positions/demands (what you are asking for, e.g., ['Unrestricted access to affected areas', 'Guarantee of staff safety'])",
        min_items=1,
        max_items=15
    )
    
    organization_reasoning: List[str] = Field(
        ...,
        description="Tactical reasoning behind your positions (how/why these specific demands, e.g., ['Access needed to assess needs accurately', 'Safety essential for sustained operations'])",
        min_items=1,
        max_items=15
    )
    
    organization_motives: List[str] = Field(
        ...,
        description="Core values and motives driving your organization (deep why, e.g., ['Humanitarian imperative to save lives', 'Neutrality and impartiality principles'])",
        min_items=1,
        max_items=15
    )
    
    counterpart_positions: List[str] = Field(
        ...,
        description="Counterpart's visible positions/demands (what they are asking for, e.g., ['All aid must be coordinated through government', 'Restrictions on movement in certain zones'])",
        min_items=1,
        max_items=15
    )
    
    counterpart_assumed_reasoning: Optional[List[str]] = Field(
        default=None,
        description="Your understanding of their reasoning (if known, e.g., ['Need to maintain control', 'Security concerns in contested areas'])",
        max_items=15
    )
    
    counterpart_assumed_motives: Optional[List[str]] = Field(
        default=None,
        description="Your understanding of their underlying motives/values (if known, e.g., ['Sovereignty protection', 'Reputation management', 'Political stability'])",
        max_items=15
    )
    
    response_format: ResponseFormat = Field(
        default=ResponseFormat.MARKDOWN,
        description="Output format: 'markdown' for visual tables or 'json' for structured data"
    )


@mcp.tool(
    name="humanitarian_analyze_icebergs",
    annotations={
        "title": "Analyze Icebergs and Common Shared Space",
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": False
    }
)
async def analyze_icebergs(params: IcebergAnalysisInput) -> str:
    """Conducts Iceberg and Common Shared Space (CSS) analysis comparing two negotiating parties.
    
    The Iceberg methodology reveals the hidden structure of negotiation positions by examining
    three levels for each party:
    - Surface Level (WHAT): Visible positions and explicit demands
    - Middle Level (HOW): Tactical reasoning and strategic thinking
    - Deep Level (WHY): Core motives, values, and fundamental drivers
    
    This tool:
    1. Maps both parties' iceberg structures side-by-side
    2. Identifies the Common Shared Space where interests align
    3. Suggests compromise opportunities based on shared values and complementary reasoning
    4. Highlights potential areas for mutual gain and risk mitigation
    
    Use this tool AFTER the Island of Agreement to dig deeper into the underlying
    motivations and find creative solutions that satisfy both parties' core interests.
    
    Args:
        params (IcebergAnalysisInput): Validated input containing:
            - organization_name (str): Your organization
            - counterpart_name (str): Their organization
            - organization_positions (List[str]): Your visible demands
            - organization_reasoning (List[str]): Your tactical reasoning
            - organization_motives (List[str]): Your core values
            - counterpart_positions (List[str]): Their visible demands
            - counterpart_assumed_reasoning (Optional[List[str]]): Their reasoning (if known)
            - counterpart_assumed_motives (Optional[List[str]]): Their motives (if known)
            - response_format (ResponseFormat): Output format
    
    Returns:
        str: Comparative iceberg analysis with Common Shared Space identification
             and compromise recommendations focused on shared values and mutual benefits
    
    Example:
        This tool reveals that while surface positions may conflict (e.g., "unrestricted access" 
        vs. "controlled coordination"), deeper analysis might show shared values (e.g., both 
        parties want to avoid reputational damage from humanitarian crisis escalation).
    """
    
    # Perform iceberg analysis
    analysis = _analyze_iceberg_structure(
        params.organization_name,
        params.counterpart_name,
        params.organization_positions,
        params.organization_reasoning,
        params.organization_motives,
        params.counterpart_positions,
        params.counterpart_assumed_reasoning or [],
        params.counterpart_assumed_motives or []
    )
    
    # Format response
    if params.response_format == ResponseFormat.JSON:
        return json.dumps(analysis, indent=2, ensure_ascii=False)
    else:
        return _format_iceberg_markdown(analysis)


def _analyze_iceberg_structure(
    org_name: str,
    counterpart_name: str,
    org_positions: List[str],
    org_reasoning: List[str],
    org_motives: List[str],
    cp_positions: List[str],
    cp_reasoning: List[str],
    cp_motives: List[str]
) -> Dict[str, Any]:
    """Internal function to structure iceberg analysis."""
    
    # Identify common shared space
    common_space = _identify_common_space(
        org_positions, org_reasoning, org_motives,
        cp_positions, cp_reasoning, cp_motives
    )
    
    analysis = {
        "metadata": {
            "organization": org_name,
            "counterpart": counterpart_name,
            "analysis_date": datetime.utcnow().isoformat()
        },
        "organization_iceberg": {
            "positions": org_positions,
            "reasoning": org_reasoning,
            "motives_values": org_motives
        },
        "counterpart_iceberg": {
            "positions": cp_positions,
            "reasoning": cp_reasoning if cp_reasoning else ["[To be explored through dialogue]"],
            "motives_values": cp_motives if cp_motives else ["[To be explored through dialogue]"]
        },
        "common_shared_space": common_space,
        "compromise_opportunities": _generate_compromise_opportunities(common_space),
        "next_steps": [
            "Test assumptions about counterpart's reasoning through careful questioning",
            "Probe for underlying motives by discussing shared values identified",
            "Propose solutions that address common shared space elements",
            "Frame positions in terms of mutual benefit and risk mitigation",
            "Use identified shared values as foundation for creative problem-solving"
        ]
    }
    
    return analysis


def _identify_common_space(
    org_pos: List[str], org_reas: List[str], org_mot: List[str],
    cp_pos: List[str], cp_reas: List[str], cp_mot: List[str]
) -> Dict[str, List[str]]:
    """Identify potential areas of shared interests across levels."""
    
    # This is a template structure. In production, would use semantic similarity
    common_space = {
        "shared_values": [
            "Both parties recognize the severity of the humanitarian situation",
            "Both seek to avoid international criticism and reputational damage",
            "Both want efficient use of available resources",
            "Both prefer orderly, predictable operational frameworks"
        ],
        "complementary_reasoning": [
            "Coordination can satisfy both access needs and control requirements",
            "Clear protocols can provide both flexibility and oversight",
            "Joint planning can address both humanitarian and security concerns",
            "Phased approaches can build trust while maintaining progress"
        ],
        "potential_aligned_positions": [
            "Establish joint coordination mechanism with defined parameters",
            "Create tiered access system based on zone security assessments",
            "Develop shared reporting framework for transparency",
            "Implement pilot program in less contested areas first"
        ]
    }
    
    return common_space


def _generate_compromise_opportunities(common_space: Dict[str, List[str]]) -> List[Dict[str, str]]:
    """Generate specific compromise recommendations."""
    
    opportunities = [
        {
            "opportunity": "Joint Coordination Mechanism",
            "description": "Establish a formal coordination body with representatives from both parties to approve and monitor operations",
            "benefit_organization": "Provides structured pathway for access and operations",
            "benefit_counterpart": "Maintains oversight and coordination authority",
            "shared_value": "Orderly, predictable framework for all parties"
        },
        {
            "opportunity": "Phased Access Expansion",
            "description": "Begin with pilot operations in agreed areas, expanding based on demonstrated success and trust-building",
            "benefit_organization": "Gains initial access to start critical work",
            "benefit_counterpart": "Tests arrangements before full commitment, reduces risk",
            "shared_value": "Gradual approach that builds confidence incrementally"
        },
        {
            "opportunity": "Enhanced Transparency Protocol",
            "description": "Implement agreed reporting standards that satisfy both humanitarian principles and governmental information needs",
            "benefit_organization": "Maintains operational independence within clear framework",
            "benefit_counterpart": "Receives regular updates and visibility",
            "shared_value": "Transparency builds trust and demonstrates responsibility"
        }
    ]
    
    return opportunities


def _format_iceberg_markdown(analysis: Dict[str, Any]) -> str:
    """Format iceberg analysis as readable Markdown."""
    
    org = analysis['metadata']['organization']
    cp = analysis['metadata']['counterpart']
    
    md = f"""# Iceberg & Common Shared Space Analysis

**Organization:** {org}
**Counterpart:** {cp}
**Analysis Date:** {analysis['metadata']['analysis_date']}

---

## Comparative Iceberg Structure

| Level | {org} | Common Shared Space | {cp} |
|-------|""" + "-" * len(org) + "|---------------------|" + "-" * len(cp) + """---|
| **WHAT** (Visible Positions) | """
    
    # Build positions row
    org_pos = "<br>".join([f"• {p}" for p in analysis['organization_iceberg']['positions']])
    cp_pos = "<br>".join([f"• {p}" for p in analysis['counterpart_iceberg']['positions']])
    css_pos = "<br>".join([f"• {p}" for p in analysis['common_shared_space']['potential_aligned_positions'][:3]])
    
    md += f"{org_pos} | {css_pos} | {cp_pos} |\n"
    
    # Build reasoning row
    md += "| **HOW** (Tactical Reasoning) | "
    org_reas = "<br>".join([f"• {r}" for r in analysis['organization_iceberg']['reasoning']])
    cp_reas = "<br>".join([f"• {r}" for r in analysis['counterpart_iceberg']['reasoning']])
    css_reas = "<br>".join([f"• {r}" for r in analysis['common_shared_space']['complementary_reasoning'][:3]])
    
    md += f"{org_reas} | {css_reas} | {cp_reas} |\n"
    
    # Build motives row
    md += "| **WHY** (Core Motives & Values) | "
    org_mot = "<br>".join([f"• {m}" for m in analysis['organization_iceberg']['motives_values']])
    cp_mot = "<br>".join([f"• {m}" for m in analysis['counterpart_iceberg']['motives_values']])
    css_val = "<br>".join([f"• {v}" for v in analysis['common_shared_space']['shared_values'][:3]])
    
    md += f"{org_mot} | {css_val} | {cp_mot} |\n\n"
    
    md += "---\n\n## Compromise Opportunities\n\n"
    
    for i, opp in enumerate(analysis['compromise_opportunities'], 1):
        md += f"### {i}. {opp['opportunity']}\n\n"
        md += f"**Description:** {opp['description']}\n\n"
        md += f"**Benefits:**\n"
        md += f"- *For {org}:* {opp['benefit_organization']}\n"
        md += f"- *For {cp}:* {opp['benefit_counterpart']}\n"
        md += f"- *Shared Value:* {opp['shared_value']}\n\n"
    
    md += "---\n\n## Recommended Next Steps\n\n"
    for i, step in enumerate(analysis['next_steps'], 1):
        md += f"{i}. {step}\n"
    
    return md


# ============================================================================
# STAKEHOLDER ANALYSIS TOOLS
# ============================================================================

class StakeholderInfo(BaseModel):
    """Individual stakeholder information."""
    model_config = ConfigDict(
        str_strip_whitespace=True,
        validate_assignment=True
    )
    
    name: str = Field(
        ...,
        description="Stakeholder name or identifier (e.g., 'Minister of Health', 'Local Community Leaders', 'UN Security Council')",
        min_length=2,
        max_length=200
    )
    
    power: float = Field(
        ...,
        description="Ability to influence decisions (0.0 = Low, 1.0 = High)",
        ge=0.0,
        le=1.0
    )
    
    urgency: float = Field(
        ...,
        description="Time-sensitivity from stakeholder's perspective (0.0 = Low, 1.0 = High)",
        ge=0.0,
        le=1.0
    )
    
    legitimacy: float = Field(
        ...,
        description="Relevance and ability to contribute meaningfully (0.0 = Low, 1.0 = High)",
        ge=0.0,
        le=1.0
    )
    
    position: float = Field(
        ...,
        description="Stance on the issue (-1.0 = Opposed, 0.0 = Neutral, 1.0 = Supportive)",
        ge=-1.0,
        le=1.0
    )
    
    role: Optional[str] = Field(
        default=None,
        description="Stakeholder's role or title (e.g., 'Government Official', 'International Observer', 'Aid Provider')",
        max_length=200
    )
    
    influence_connections: Optional[List[str]] = Field(
        default=None,
        description="Names of other stakeholders this person influences (for relationship mapping)",
        max_items=20
    )


class StakeholderAnalysisInput(BaseModel):
    """Input model for comprehensive stakeholder analysis."""
    model_config = ConfigDict(
        str_strip_whitespace=True,
        validate_assignment=True,
        extra='forbid'
    )
    
    negotiation_context: str = Field(
        ...,
        description="Brief description of the negotiation context (e.g., 'Access negotiation for IDP camps in northern region')",
        min_length=10,
        max_length=1000
    )
    
    stakeholders: List[StakeholderInfo] = Field(
        ...,
        description="List of identified stakeholders with their attributes",
        min_items=2,
        max_items=MAX_STAKEHOLDERS
    )
    
    response_format: ResponseFormat = Field(
        default=ResponseFormat.MARKDOWN,
        description="Output format: 'markdown' for tables or 'json' for structured data"
    )


@mcp.tool(
    name="humanitarian_analyze_stakeholders",
    annotations={
        "title": "Conduct Stakeholder Analysis",
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": False
    }
)
async def analyze_stakeholders(params: StakeholderAnalysisInput) -> str:
    """Conducts comprehensive stakeholder analysis for high-stakes negotiations.
    
    This tool helps identify, assess, and prioritize stakeholders based on their:
    - Power: Ability to influence decisions and outcomes
    - Urgency: Time-sensitivity of the issue from their perspective
    - Legitimacy: Relevance and meaningful contribution potential
    - Position: Current stance (opposed, neutral, supportive)
    
    The analysis provides:
    1. Stakeholder characterization table with all attributes
    2. Priority ranking (First/Second/Third priority based on P/U/L scores)
    3. Relationship and influence pathway mapping
    4. Tailored engagement strategies for each priority level
    5. Recommendations for building coalitions and neutralizing opposition
    
    Use this tool to:
    - Map the stakeholder landscape systematically
    - Prioritize engagement efforts efficiently
    - Identify key influencers and intermediaries
    - Develop targeted strategies to maximize support and reduce resistance
    
    After receiving the analysis, you can use the companion tool
    'humanitarian_leverage_stakeholder_influence' to develop specific tactics
    for influencing a target stakeholder.
    
    Args:
        params (StakeholderAnalysisInput): Validated input containing:
            - negotiation_context (str): Brief context description
            - stakeholders (List[StakeholderInfo]): Stakeholder details with P/U/L/Position scores
            - response_format (ResponseFormat): Output format preference
    
    Returns:
        str: Comprehensive stakeholder analysis with characterization table, priority rankings,
             relationship mapping, and engagement strategies for each priority level
    
    Example:
        For a negotiation involving 10 stakeholders, this tool will identify which 2-3
        require active management, which 3-4 need selective engagement, and which can
        be monitored with minimal resources.
    """
    
    # Perform stakeholder analysis
    analysis = _analyze_stakeholder_landscape(
        params.negotiation_context,
        params.stakeholders
    )
    
    # Format response
    if params.response_format == ResponseFormat.JSON:
        return json.dumps(analysis, indent=2, ensure_ascii=False)
    else:
        return _format_stakeholder_markdown(analysis, params.negotiation_context)


def _analyze_stakeholder_landscape(
    context: str,
    stakeholders: List[StakeholderInfo]
) -> Dict[str, Any]:
    """Internal function to analyze stakeholders and generate priorities."""
    
    # Calculate priority scores and categorize
    stakeholder_analysis = []
    
    for sh in stakeholders:
        # Count high attributes (>= 0.7 threshold)
        high_attrs = sum([
            1 if sh.power >= 0.7 else 0,
            1 if sh.urgency >= 0.7 else 0,
            1 if sh.legitimacy >= 0.7 else 0
        ])
        
        # Determine priority
        if high_attrs == 3:
            priority = "First Priority"
            strategy = "Actively engage and manage opposition"
        elif high_attrs == 2:
            priority = "Second Priority"
            strategy = "Selective engagement - leverage allies, monitor risks"
        else:
            priority = "Third Priority"
            strategy = "Minimal engagement unless influence increases"
        
        # Determine stance
        if sh.position >= 0.5:
            stance = "Supportive"
        elif sh.position <= -0.5:
            stance = "Opposed"
        else:
            stance = "Neutral"
        
        stakeholder_analysis.append({
            "name": sh.name,
            "role": sh.role or "Not specified",
            "power": sh.power,
            "urgency": sh.urgency,
            "legitimacy": sh.legitimacy,
            "position": sh.position,
            "stance": stance,
            "priority": priority,
            "priority_score": high_attrs,
            "engagement_strategy": strategy,
            "influence_connections": sh.influence_connections or []
        })
    
    # Sort by priority score (descending) then by power
    stakeholder_analysis.sort(key=lambda x: (x['priority_score'], x['power']), reverse=True)
    
    # Group by priority
    first_priority = [s for s in stakeholder_analysis if s['priority'] == "First Priority"]
    second_priority = [s for s in stakeholder_analysis if s['priority'] == "Second Priority"]
    third_priority = [s for s in stakeholder_analysis if s['priority'] == "Third Priority"]
    
    # Analyze relationships
    relationships = _analyze_relationships(stakeholder_analysis)
    
    analysis = {
        "metadata": {
            "context": context,
            "total_stakeholders": len(stakeholders),
            "analysis_date": datetime.utcnow().isoformat()
        },
        "all_stakeholders": stakeholder_analysis,
        "priority_groups": {
            "first_priority": first_priority,
            "second_priority": second_priority,
            "third_priority": third_priority
        },
        "relationship_analysis": relationships,
        "engagement_strategies": _generate_engagement_strategies(
            first_priority,
            second_priority,
            third_priority
        )
    }
    
    return analysis


def _analyze_relationships(stakeholders: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Analyze influence pathways and key connectors."""
    
    # Build influence map
    influence_map = {}
    influenced_by = {}
    
    for sh in stakeholders:
        influence_map[sh['name']] = sh['influence_connections']
        for influenced in sh['influence_connections']:
            if influenced not in influenced_by:
                influenced_by[influenced] = []
            influenced_by[influenced].append(sh['name'])
    
    # Find key connectors (stakeholders who influence many others)
    connectors = sorted(
        [(name, len(connections)) for name, connections in influence_map.items()],
        key=lambda x: x[1],
        reverse=True
    )
    
    # Find key influencers (stakeholders influenced by many others)
    influencers = sorted(
        [(name, len(influencers)) for name, influencers in influenced_by.items()],
        key=lambda x: x[1],
        reverse=True
    )
    
    return {
        "key_connectors": [{"name": name, "influences_count": count} for name, count in connectors[:5]],
        "key_influencers": [{"name": name, "influenced_by_count": count} for name, count in influencers[:5]],
        "total_connections": sum(len(conns) for conns in influence_map.values())
    }


def _generate_engagement_strategies(
    first: List[Dict], second: List[Dict], third: List[Dict]
) -> Dict[str, Any]:
    """Generate specific engagement strategies by priority level."""
    
    strategies = {
        "first_priority_strategy": {
            "description": "These stakeholders require active, continuous engagement and careful management",
            "actions": [
                "Schedule regular one-on-one meetings with each stakeholder",
                "Develop personalized engagement plans addressing their specific concerns",
                "For opposed stakeholders: understand their objections and seek compromise",
                "For supportive stakeholders: leverage their advocacy and visibility",
                "For neutral stakeholders: provide information to shift toward support",
                "Monitor their positions continuously and adjust strategies as needed"
            ],
            "stakeholders": [s['name'] for s in first]
        },
        "second_priority_strategy": {
            "description": "These stakeholders need selective engagement - focus efforts strategically",
            "actions": [
                "Engage through targeted communications and periodic updates",
                "Leverage supportive stakeholders as advocates and amplifiers",
                "Monitor opposed stakeholders for escalating resistance",
                "Use intermediaries to influence indirectly where appropriate",
                "Provide key information at critical decision points",
                "Build coalitions among aligned stakeholders in this group"
            ],
            "stakeholders": [s['name'] for s in second]
        },
        "third_priority_strategy": {
            "description": "These stakeholders require minimal engagement unless their influence grows",
            "actions": [
                "Include in general communications and broad stakeholder updates",
                "Monitor for changes in power, urgency, or position",
                "Respond to direct inquiries but don't proactively engage",
                "Keep informed of major developments that might affect them",
                "Re-assess if they show signs of increasing influence"
            ],
            "stakeholders": [s['name'] for s in third]
        }
    }
    
    return strategies


def _format_stakeholder_markdown(analysis: Dict[str, Any], context: str) -> str:
    """Format stakeholder analysis as readable Markdown."""
    
    md = f"""# Stakeholder Analysis

**Context:** {context}
**Total Stakeholders:** {analysis['metadata']['total_stakeholders']}
**Analysis Date:** {analysis['metadata']['analysis_date']}

---

## Stakeholder Characterization Table

| Stakeholder | Role | Power | Urgency | Legitimacy | Position | Stance | Priority |
|-------------|------|-------|---------|------------|----------|--------|----------|
"""
    
    for sh in analysis['all_stakeholders']:
        md += f"| {sh['name']} | {sh['role']} | {sh['power']:.1f} | {sh['urgency']:.1f} | {sh['legitimacy']:.1f} | {sh['position']:.1f} | {sh['stance']} | {sh['priority']} |\n"
    
    md += "\n---\n\n## Priority Analysis\n\n"
    
    # First Priority
    md += "### First Priority Stakeholders (High Power, Urgency, AND Legitimacy)\n\n"
    if analysis['priority_groups']['first_priority']:
        md += "**Require Active Engagement and Management:**\n\n"
        for sh in analysis['priority_groups']['first_priority']:
            md += f"- **{sh['name']}** ({sh['stance']}) - {sh['engagement_strategy']}\n"
    else:
        md += "*No stakeholders in this category*\n"
    
    md += "\n"
    
    # Second Priority
    md += "### Second Priority Stakeholders (Any Two High Attributes)\n\n"
    if analysis['priority_groups']['second_priority']:
        md += "**Require Selective Engagement:**\n\n"
        for sh in analysis['priority_groups']['second_priority']:
            md += f"- **{sh['name']}** ({sh['stance']}) - {sh['engagement_strategy']}\n"
    else:
        md += "*No stakeholders in this category*\n"
    
    md += "\n"
    
    # Third Priority
    md += "### Third Priority Stakeholders (One or Fewer High Attributes)\n\n"
    if analysis['priority_groups']['third_priority']:
        md += "**Require Minimal Engagement:**\n\n"
        for sh in analysis['priority_groups']['third_priority']:
            md += f"- **{sh['name']}** ({sh['stance']}) - {sh['engagement_strategy']}\n"
    else:
        md += "*No stakeholders in this category*\n"
    
    md += "\n---\n\n## Relationship & Influence Analysis\n\n"
    
    if analysis['relationship_analysis']['key_connectors']:
        md += "### Key Connectors (Most Outward Influence)\n\n"
        for connector in analysis['relationship_analysis']['key_connectors']:
            md += f"- **{connector['name']}** - Influences {connector['influences_count']} other stakeholder(s)\n"
        md += "\n"
    
    if analysis['relationship_analysis']['key_influencers']:
        md += "### Key Influencers (Most Inward Influence)\n\n"
        for influencer in analysis['relationship_analysis']['key_influencers']:
            md += f"- **{influencer['name']}** - Influenced by {influencer['influenced_by_count']} other stakeholder(s)\n"
        md += "\n"
    
    md += "---\n\n## Engagement Strategies by Priority\n\n"
    
    # First Priority Strategies
    md += f"### {analysis['engagement_strategies']['first_priority_strategy']['description']}\n\n"
    md += "**Actions:**\n"
    for action in analysis['engagement_strategies']['first_priority_strategy']['actions']:
        md += f"- {action}\n"
    md += "\n"
    
    # Second Priority Strategies
    md += f"### {analysis['engagement_strategies']['second_priority_strategy']['description']}\n\n"
    md += "**Actions:**\n"
    for action in analysis['engagement_strategies']['second_priority_strategy']['actions']:
        md += f"- {action}\n"
    md += "\n"
    
    # Third Priority Strategies
    md += f"### {analysis['engagement_strategies']['third_priority_strategy']['description']}\n\n"
    md += "**Actions:**\n"
    for action in analysis['engagement_strategies']['third_priority_strategy']['actions']:
        md += f"- {action}\n"
    md += "\n"
    
    md += "---\n\n## Next Steps\n\n"
    md += "Please review the engagement strategies above. Once ready, use the **humanitarian_leverage_stakeholder_influence** tool with a target stakeholder name to develop specific influence pathways and tactical recommendations.\n"
    
    return md


class LeverageInfluenceInput(BaseModel):
    """Input for developing influence tactics around a specific stakeholder."""
    model_config = ConfigDict(
        str_strip_whitespace=True,
        validate_assignment=True,
        extra='forbid'
    )
    
    target_stakeholder: str = Field(
        ...,
        description="Name of the stakeholder you want to influence (must match a name from previous stakeholder analysis)",
        min_length=2,
        max_length=200
    )
    
    stakeholder_analysis_data: str = Field(
        ...,
        description="JSON string of the stakeholder analysis data from previous humanitarian_analyze_stakeholders tool call",
        min_length=10
    )
    
    response_format: ResponseFormat = Field(
        default=ResponseFormat.MARKDOWN,
        description="Output format: 'markdown' or 'json'"
    )


@mcp.tool(
    name="humanitarian_leverage_stakeholder_influence",
    annotations={
        "title": "Develop Influence Tactics for Target Stakeholder",
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": False
    }
)
async def leverage_stakeholder_influence(params: LeverageInfluenceInput) -> str:
    """Develops specific influence pathways and tactics to affect a target stakeholder.
    
    This tool analyzes the influence network around a specific stakeholder and recommends
    concrete actions to:
    - Build coalitions around shared interests
    - Neutralize spoilers by reducing their influence
    - Use intermediaries to bridge divides
    - Encourage alliances to strengthen your position
    
    The analysis identifies:
    1. Who influences the target stakeholder (direct and indirect pathways)
    2. Which influencers are supportive, neutral, or opposed
    3. Specific tactics for engaging each influencer
    4. Coalition opportunities and alliance building strategies
    5. Risks and mitigation approaches
    
    Use this tool AFTER completing stakeholder analysis to focus tactical efforts
    on changing the position or behavior of a critical stakeholder.
    
    Args:
        params (LeverageInfluenceInput): Validated input containing:
            - target_stakeholder (str): Name of stakeholder to influence
            - stakeholder_analysis_data (str): JSON from previous analysis
            - response_format (ResponseFormat): Output format
    
    Returns:
        str: Targeted influence strategy with specific pathways, tactics, and actions
             for affecting the target stakeholder through their network
    
    Example:
        If targeting an opposed government official, this tool might identify supportive
        international organizations that have credibility with that official, suggest
        using shared connections as intermediaries, and recommend coalition-building
        with other government departments that support your position.
    """
    
    try:
        # Parse stakeholder analysis data
        analysis_data = json.loads(params.stakeholder_analysis_data)
    except json.JSONDecodeError:
        return "Error: Invalid stakeholder_analysis_data JSON format. Please provide the complete JSON output from humanitarian_analyze_stakeholders tool."
    
    # Generate influence tactics
    tactics = _generate_influence_tactics(
        params.target_stakeholder,
        analysis_data
    )
    
    if not tactics:
        return f"Error: Target stakeholder '{params.target_stakeholder}' not found in provided analysis data. Please check the spelling and ensure it matches a stakeholder from the previous analysis."
    
    # Format response
    if params.response_format == ResponseFormat.JSON:
        return json.dumps(tactics, indent=2, ensure_ascii=False)
    else:
        return _format_influence_tactics_markdown(tactics)


def _generate_influence_tactics(
    target_name: str,
    analysis_data: Dict[str, Any]
) -> Optional[Dict[str, Any]]:
    """Generate specific influence tactics for target stakeholder."""
    
    # Find target stakeholder
    target = None
    for sh in analysis_data['all_stakeholders']:
        if sh['name'].lower() == target_name.lower():
            target = sh
            break
    
    if not target:
        return None
    
    # Find who influences the target
    influencers = []
    for sh in analysis_data['all_stakeholders']:
        if target['name'] in sh['influence_connections']:
            influencers.append(sh)
    
    # Categorize influencers by stance
    supportive_influencers = [i for i in influencers if i['stance'] == "Supportive"]
    neutral_influencers = [i for i in influencers if i['stance'] == "Neutral"]
    opposed_influencers = [i for i in influencers if i['stance'] == "Opposed"]
    
    # Generate pathways
    pathways = []
    
    # Direct supportive influencer pathway
    if supportive_influencers:
        pathways.append({
            "pathway_type": "Direct Advocacy",
            "description": f"Leverage supportive influencers who have direct connection to {target['name']}",
            "influencers": [i['name'] for i in supportive_influencers],
            "tactic": f"Engage {', '.join([i['name'] for i in supportive_influencers])} to directly advocate your position with {target['name']}",
            "actions": [
                f"Brief supportive influencers on key talking points",
                f"Provide evidence and documentation to support their advocacy",
                f"Request they raise concerns directly with {target['name']}",
                f"Coordinate timing of advocacy for maximum impact"
            ]
        })
    
    # Neutral influencer conversion
    if neutral_influencers:
        pathways.append({
            "pathway_type": "Neutral Conversion",
            "description": f"Convert neutral influencers into advocates",
            "influencers": [i['name'] for i in neutral_influencers],
            "tactic": f"Educate and align {', '.join([i['name'] for i in neutral_influencers])} with your position before they engage {target['name']}",
            "actions": [
                f"Present compelling case to neutral influencers",
                f"Address their specific interests and concerns",
                f"Build relationship before requesting advocacy",
                f"Demonstrate how your position benefits them"
            ]
        })
    
    # Neutralize opposition
    if opposed_influencers:
        pathways.append({
            "pathway_type": "Opposition Neutralization",
            "description": f"Reduce negative influence on {target['name']}",
            "influencers": [i['name'] for i in opposed_influencers],
            "tactic": f"Mitigate impact of {', '.join([i['name'] for i in opposed_influencers])} by addressing their concerns or providing counter-narratives",
            "actions": [
                f"Understand and document objections of opposed influencers",
                f"Seek common ground or compromise positions",
                f"Provide counter-evidence to {target['name']} directly",
                f"Build coalitions that outnumber opposition"
            ]
        })
    
    # Build coalition recommendations
    coalition_opportunities = _identify_coalition_opportunities(
        target,
        analysis_data['all_stakeholders']
    )
    
    tactics = {
        "target_stakeholder": {
            "name": target['name'],
            "role": target['role'],
            "current_stance": target['stance'],
            "priority": target['priority'],
            "attributes": {
                "power": target['power'],
                "urgency": target['urgency'],
                "legitimacy": target['legitimacy']
            }
        },
        "influence_pathways": pathways,
        "coalition_opportunities": coalition_opportunities,
        "overall_strategy": _generate_overall_strategy(target, pathways),
        "risk_mitigation": _generate_risk_mitigation(target, opposed_influencers)
    }
    
    return tactics


def _identify_coalition_opportunities(
    target: Dict[str, Any],
    all_stakeholders: List[Dict[str, Any]]
) -> List[Dict[str, str]]:
    """Identify potential coalition partners."""
    
    opportunities = []
    
    # Find supportive stakeholders with high power
    powerful_supporters = [
        s for s in all_stakeholders
        if s['stance'] == "Supportive" and s['power'] >= 0.7
    ]
    
    if powerful_supporters:
        opportunities.append({
            "coalition_type": "Power Coalition",
            "description": "Alliance of high-power supportive stakeholders",
            "members": [s['name'] for s in powerful_supporters],
            "benefit": "Collective influence can counterbalance opposition and demonstrate broad support"
        })
    
    # Find stakeholders in same priority category as target
    same_priority = [
        s for s in all_stakeholders
        if s['priority'] == target['priority'] and s['name'] != target['name']
    ]
    
    if same_priority:
        opportunities.append({
            "coalition_type": "Peer Coalition",
            "description": f"Stakeholders at same priority level as {target['name']}",
            "members": [s['name'] for s in same_priority[:5]],
            "benefit": "Peers can influence each other through shared concerns and perspectives"
        })
    
    return opportunities


def _generate_overall_strategy(
    target: Dict[str, Any],
    pathways: List[Dict[str, Any]]
) -> str:
    """Generate overall strategic recommendation."""
    
    if target['stance'] == "Opposed":
        return f"Focus on building overwhelming coalition of supportive voices to counterbalance {target['name']}'s opposition. Use intermediaries with credibility to reduce resistance. Simultaneously address underlying concerns driving opposition."
    elif target['stance'] == "Neutral":
        return f"Convert {target['name']} to supportive stance through education, relationship building, and demonstrating clear benefits. Leverage existing supportive influencers for advocacy."
    else:
        return f"Reinforce and strengthen {target['name']}'s supportive position. Provide resources and ammunition for them to advocate effectively to others."


def _generate_risk_mitigation(
    target: Dict[str, Any],
    opposed_influencers: List[Dict[str, Any]]
) -> List[str]:
    """Generate risk mitigation strategies."""
    
    risks = []
    
    if opposed_influencers:
        risks.append(f"Risk: {len(opposed_influencers)} opposed influencer(s) may counteract your efforts - Mitigation: Build larger coalition of supportive voices to outnumber opposition")
    
    if target['power'] >= 0.8:
        risks.append(f"Risk: {target['name']} has very high power - Mitigation: Engage at highest organizational levels and use peer-level advocates")
    
    if target['urgency'] <= 0.3:
        risks.append(f"Risk: Low urgency may mean {target['name']} deprioritizes this issue - Mitigation: Demonstrate time-sensitivity and consequences of inaction")
    
    risks.append("Risk: Influence attempts may backfire if perceived as manipulation - Mitigation: Maintain transparency and focus on shared values and mutual benefits")
    
    return risks


def _format_influence_tactics_markdown(tactics: Dict[str, Any]) -> str:
    """Format influence tactics as readable Markdown."""
    
    target = tactics['target_stakeholder']
    
    md = f"""# Influence Strategy for {target['name']}

**Role:** {target['role']}
**Current Stance:** {target['current_stance']}
**Priority Level:** {target['priority']}
**Attributes:** Power={target['attributes']['power']:.1f}, Urgency={target['attributes']['urgency']:.1f}, Legitimacy={target['attributes']['legitimacy']:.1f}

---

## Influence Pathways

"""
    
    for i, pathway in enumerate(tactics['influence_pathways'], 1):
        md += f"### {i}. {pathway['pathway_type']}\n\n"
        md += f"**Description:** {pathway['description']}\n\n"
        md += f"**Key Influencers:** {', '.join(pathway['influencers'])}\n\n"
        md += f"**Tactic:** {pathway['tactic']}\n\n"
        md += "**Specific Actions:**\n"
        for action in pathway['actions']:
            md += f"- {action}\n"
        md += "\n"
    
    md += "---\n\n## Coalition Opportunities\n\n"
    
    for opp in tactics['coalition_opportunities']:
        md += f"### {opp['coalition_type']}\n\n"
        md += f"**Description:** {opp['description']}\n\n"
        md += f"**Potential Members:** {', '.join(opp['members'])}\n\n"
        md += f"**Strategic Benefit:** {opp['benefit']}\n\n"
    
    md += "---\n\n## Overall Strategy\n\n"
    md += f"{tactics['overall_strategy']}\n\n"
    
    md += "---\n\n## Risk Mitigation\n\n"
    for risk in tactics['risk_mitigation']:
        md += f"- {risk}\n"
    
    return md


# ============================================================================
# UTILITY TOOLS
# ============================================================================

@mcp.tool(
    name="humanitarian_negotiation_guide",
    annotations={
        "title": "Get Negotiation Methodology Guide",
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": False
    }
)
async def negotiation_guide() -> str:
    """Provides comprehensive guide on humanitarian negotiation methodologies and tool usage.
    
    This tool returns detailed information about:
    - The three core methodologies (Island of Agreement, Iceberg/CSS, Stakeholder Analysis)
    - When and how to use each methodology
    - Recommended workflow and tool sequencing
    - Best practices for humanitarian negotiations
    - Key principles and communication guidelines
    
    Use this tool when:
    - Starting a new negotiation analysis
    - Deciding which tool to use next
    - Understanding the overall negotiation framework
    - Training team members on the methodologies
    
    Returns:
        str: Comprehensive guide in Markdown format
    """
    
    guide = """# Humanitarian Negotiation Methodologies Guide

## Overview

This MCP server provides three interconnected methodologies for analyzing and conducting humanitarian negotiations:

1. **Island of Agreement (IoA)** - Establishes common ground
2. **Iceberg & Common Shared Space (CSS)** - Reveals deeper motivations
3. **Stakeholder Analysis** - Maps influence and develops engagement strategies

---

## Methodology 1: Island of Agreement (IoA)

### Purpose
Establish a clear foundation for negotiation by identifying:
- What facts are agreed upon vs. contested
- What values/norms are shared vs. divergent

### When to Use
- At the START of negotiation planning
- When parties have very different perspectives
- When you need to identify safe starting points for dialogue

### Tool
`humanitarian_create_island_of_agreement`

### Output
A four-column table containing:
- **Contested Facts**: Facts needing clarification (e.g., population numbers, security status)
- **Agreed Facts**: Points of agreement (e.g., crisis severity, need for action)
- **Convergent Norms**: Shared values (e.g., humanitarian principles, protection of civilians)
- **Divergent Norms**: Normative disagreements (e.g., sovereignty vs. access rights)

### Key Principle
Start discussions from AGREED FACTS and CONVERGENT NORMS to build trust, then gradually address contested and divergent elements.

---

## Methodology 2: Iceberg & Common Shared Space (CSS)

### Purpose
Understand the hidden structure of positions by examining:
- **WHAT** (Surface): Visible positions and demands
- **HOW** (Middle): Tactical reasoning and strategic thinking
- **WHY** (Deep): Core motives, values, and drivers

### When to Use
- AFTER completing Island of Agreement
- When positions seem incompatible but you suspect deeper alignment
- When seeking creative compromise solutions

### Tool
`humanitarian_analyze_icebergs`

### Output
Comparative analysis showing:
- Both parties' iceberg structures (positions → reasoning → motives)
- Common Shared Space where interests align
- Specific compromise opportunities based on shared values

### Key Principle
Surface positions may conflict, but deeper values often align. Find compromise by addressing shared motivations rather than rigid positions.

---

## Methodology 3: Stakeholder Analysis

### Purpose
Systematically identify, assess, and prioritize stakeholders to:
- Focus engagement efforts on highest-priority actors
- Map influence pathways and relationships
- Develop targeted strategies to maximize support

### When to Use
- Throughout the negotiation process
- When facing complex multi-party situations
- When you need to build coalitions or neutralize opposition

### Tools
1. `humanitarian_analyze_stakeholders` - Full stakeholder assessment
2. `humanitarian_leverage_stakeholder_influence` - Targeted influence tactics

### Output
- Stakeholder characterization table with Power/Urgency/Legitimacy/Position scores
- Priority rankings (First/Second/Third priority)
- Relationship mapping
- Engagement strategies by priority level
- Specific influence pathways for target stakeholders

### Key Principle
Not all stakeholders are equal. Prioritize based on Power, Urgency, and Legitimacy. Focus intensive efforts on First Priority stakeholders.

---

## Recommended Workflow

### Phase 1: Foundation (Week 1-2)
1. **Start with Island of Agreement**
   - Map the negotiation landscape
   - Identify common ground and divergences
   - Develop initial engagement strategy

### Phase 2: Deep Analysis (Week 2-3)
2. **Conduct Iceberg/CSS Analysis**
   - Understand underlying motivations
   - Identify creative compromise opportunities
   - Refine negotiation positions

### Phase 3: Stakeholder Engagement (Week 3-4)
3. **Perform Stakeholder Analysis**
   - Map all relevant actors
   - Prioritize engagement efforts
   - Develop influence tactics

4. **Leverage Specific Influence** (as needed)
   - Target critical stakeholders
   - Build coalitions
   - Neutralize opposition

### Phase 4: Execution (Ongoing)
5. **Iterate and Refine**
   - Update analyses as situation evolves
   - Adjust strategies based on outcomes
   - Monitor stakeholder positions

---

## Best Practices for Humanitarian Negotiations

### 1. Communication Principles
- Use formal, professional tone
- Avoid inflammatory or judgmental language
- Focus on shared interests and mutual benefits
- Frame proposals in terms of risk mitigation for all parties

### 2. Evidence-Based Approach
- Support claims with credible data
- Propose joint fact-finding for contested elements
- Document agreements and understandings
- Use objective criteria for decision-making

### 3. Relationship Building
- Start with areas of agreement
- Demonstrate understanding of counterpart's concerns
- Seek incremental progress rather than immediate resolution
- Build trust through transparency and consistency

### 4. Flexibility and Creativity
- Look beyond surface positions to underlying interests
- Generate multiple options before choosing
- Consider phased or pilot approaches
- Use objective standards and precedents

### 5. Reputational Awareness
- Recognize that all parties fear reputational damage
- Frame solutions that allow all parties to "save face"
- Emphasize shared responsibility and partnership
- Highlight positive outcomes for all stakeholders

---

## Tool Selection Guide

**Use Island of Agreement when:**
- Starting a new negotiation
- Positions are polarized
- Need to establish dialogue foundation

**Use Iceberg/CSS when:**
- Surface positions seem incompatible
- Need creative solutions
- Want to understand deeper motivations

**Use Stakeholder Analysis when:**
- Multiple parties involved
- Need to prioritize engagement
- Building coalitions or managing opposition

**Use Influence Tactics when:**
- Have specific target stakeholder
- Need actionable engagement plan
- Working through intermediaries

---

## Key Success Factors

1. **Preparation**: Thoroughly analyze before engaging
2. **Patience**: Build trust incrementally
3. **Empathy**: Understand all perspectives
4. **Evidence**: Use data and objective criteria
5. **Flexibility**: Generate multiple options
6. **Persistence**: Stay committed to humanitarian principles

---

## Getting Started

1. Call `humanitarian_negotiation_guide` (this tool) to review methodologies
2. Begin with `humanitarian_create_island_of_agreement` for initial analysis
3. Proceed to `humanitarian_analyze_icebergs` for deeper understanding
4. Use `humanitarian_analyze_stakeholders` to map and prioritize actors
5. Apply `humanitarian_leverage_stakeholder_influence` for targeted tactics

For questions or guidance on specific situations, provide detailed context to any tool and request detailed output level for comprehensive analysis.
"""
    
    return guide


# ============================================================================
# SERVER INITIALIZATION
# ============================================================================

if __name__ == "__main__":
    # Run the MCP server
    mcp.run()
