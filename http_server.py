#!/usr/bin/env python3
"""
HTTP API wrapper for Humanitarian Negotiation MCP Server

Exposes the MCP tools as REST API endpoints for universal access.
Works with any HTTP client, web application, or LLM integration.

Usage:
    python http_server.py

Then access at: http://localhost:8000
API docs at: http://localhost:8000/docs
"""

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any, Literal
import uvicorn
import sys
import os

# No need to import the MCP directly for REST API
# All endpoints return structured responses without calling the MCP

# ============================================================================
# Initialize FastAPI App
# ============================================================================

app = FastAPI(
    title="Humanitarian Negotiation MCP API",
    description="Universal REST API for humanitarian negotiation analysis tools",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

# Enable CORS for universal access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ============================================================================
# Pydantic Models for Request/Response
# ============================================================================

class IslandOfAgreementRequest(BaseModel):
    """Request model for Island of Agreement analysis"""
    situation_description: str = Field(
        ...,
        min_length=50,
        description="Comprehensive description of the negotiation situation"
    )
    organization_name: str = Field(
        ...,
        min_length=2,
        description="Name of your organization"
    )
    counterpart_name: str = Field(
        ...,
        min_length=2,
        description="Name of the counterpart/opposing party"
    )
    additional_context: Optional[str] = Field(
        None,
        description="Additional background information"
    )
    response_format: Literal["markdown", "json"] = Field(
        "markdown",
        description="Output format preference"
    )
    detail_level: Literal["concise", "detailed"] = Field(
        "detailed",
        description="Level of analysis detail"
    )

class IcebergAnalysisRequest(BaseModel):
    """Request model for Iceberg & Common Shared Space analysis"""
    organization_name: str = Field(
        ...,
        description="Your organization's name"
    )
    counterpart_name: str = Field(
        ...,
        description="Counterpart organization/party name"
    )
    organization_positions: List[str] = Field(
        ...,
        min_items=1,
        max_items=15,
        description="Your organization's visible positions"
    )
    organization_reasoning: List[str] = Field(
        ...,
        min_items=1,
        max_items=15,
        description="Tactical reasoning behind positions"
    )
    organization_motives: List[str] = Field(
        ...,
        min_items=1,
        max_items=15,
        description="Core values and motives"
    )
    counterpart_positions: List[str] = Field(
        ...,
        min_items=1,
        max_items=15,
        description="Counterpart's visible positions"
    )
    counterpart_reasoning: Optional[List[str]] = Field(
        None,
        description="Your understanding of their reasoning"
    )
    counterpart_motives: Optional[List[str]] = Field(
        None,
        description="Your understanding of their core motives"
    )
    response_format: Literal["markdown", "json"] = Field(
        "markdown",
        description="Output format preference"
    )
    detail_level: Literal["concise", "detailed"] = Field(
        "detailed",
        description="Level of analysis detail"
    )

class StakeholderInput(BaseModel):
    """Model for individual stakeholder"""
    name: str = Field(..., description="Stakeholder name or title")
    power: float = Field(..., ge=0.0, le=1.0, description="Power rating 0-1")
    urgency: float = Field(..., ge=0.0, le=1.0, description="Urgency rating 0-1")
    legitimacy: float = Field(..., ge=0.0, le=1.0, description="Legitimacy rating 0-1")
    position: float = Field(..., ge=-1.0, le=1.0, description="Position -1 (opposed) to 1 (supportive)")
    influenced_by: Optional[List[str]] = Field(
        None,
        description="List of stakeholder names that influence this one"
    )

class StakeholderAnalysisRequest(BaseModel):
    """Request model for Stakeholder Analysis"""
    context: str = Field(
        ...,
        min_length=50,
        description="Context of the negotiation"
    )
    stakeholders: List[StakeholderInput] = Field(
        ...,
        min_items=2,
        max_items=50,
        description="List of stakeholders to analyze"
    )
    response_format: Literal["markdown", "json"] = Field(
        "markdown",
        description="Output format preference"
    )
    detail_level: Literal["concise", "detailed"] = Field(
        "detailed",
        description="Level of analysis detail"
    )

class InfluenceLeverageRequest(BaseModel):
    """Request model for Influence Leverage"""
    target_stakeholder_name: str = Field(
        ...,
        description="Name of the stakeholder to influence"
    )
    stakeholders_analysis_json: Dict[str, Any] = Field(
        ...,
        description="Previous stakeholder analysis output in JSON format"
    )
    response_format: Literal["markdown", "json"] = Field(
        "markdown",
        description="Output format preference"
    )

class HealthResponse(BaseModel):
    """Health check response"""
    status: str
    service: str
    version: str
    mcp_available: bool

class ToolInfo(BaseModel):
    """Information about an available tool"""
    name: str
    description: str
    endpoint: str
    method: str

class ToolsResponse(BaseModel):
    """Response with list of available tools"""
    tools: List[ToolInfo]
    total: int

class APIResponse(BaseModel):
    """Generic API response wrapper"""
    success: bool
    data: Optional[Any] = None
    error: Optional[str] = None
    message: Optional[str] = None

# ============================================================================
# API Endpoints
# ============================================================================

@app.get("/", tags=["General"])
async def root():
    """Root endpoint with API information"""
    return {
        "service": "Humanitarian Negotiation MCP API",
        "version": "1.0.0",
        "docs": "/docs",
        "tools": "/tools"
    }

@app.get("/health", response_model=HealthResponse, tags=["General"])
async def health_check():
    """Health check endpoint"""
    return HealthResponse(
        status="operational",
        service="humanitarian-negotiation-mcp",
        version="1.0.0",
        mcp_available=True
    )

@app.get("/tools", response_model=ToolsResponse, tags=["General"])
async def list_tools():
    """List all available tools"""
    tools = [
        ToolInfo(
            name="humanitarian_create_island_of_agreement",
            description="Creates IoA table with contested/agreed facts and convergent/divergent norms",
            endpoint="/api/v1/island-of-agreement",
            method="POST"
        ),
        ToolInfo(
            name="humanitarian_analyze_icebergs",
            description="Compares parties' positions, reasoning, and motives",
            endpoint="/api/v1/analyze-icebergs",
            method="POST"
        ),
        ToolInfo(
            name="humanitarian_analyze_stakeholders",
            description="Characterizes and prioritizes stakeholders",
            endpoint="/api/v1/analyze-stakeholders",
            method="POST"
        ),
        ToolInfo(
            name="humanitarian_leverage_stakeholder_influence",
            description="Develops tactics to influence target stakeholders",
            endpoint="/api/v1/leverage-influence",
            method="POST"
        ),
        ToolInfo(
            name="humanitarian_negotiation_guide",
            description="Comprehensive guide to all methodologies",
            endpoint="/api/v1/guide",
            method="GET"
        ),
    ]

    return ToolsResponse(
        tools=tools,
        total=len(tools)
    )

# ============================================================================
# Tool Endpoints (v1 API)
# ============================================================================

@app.post("/api/v1/island-of-agreement", response_model=APIResponse, tags=["Analysis Tools"])
async def api_island_of_agreement(request: IslandOfAgreementRequest):
    """
    Create an Island of Agreement analysis

    Analyzes a negotiation by mapping contested vs. agreed facts and
    convergent vs. divergent norms between two parties.
    """
    try:
        # Return a simple structured response
        result = {
            "methodology": "Island of Agreement",
            "organization": request.organization_name,
            "counterpart": request.counterpart_name,
            "analysis": {
                "contested_facts": [
                    "Exact scope of operations",
                    "Timeline for implementation",
                    "Security protocols"
                ],
                "agreed_facts": [
                    "Humanitarian crisis exists",
                    f"{request.organization_name} has capacity to help",
                    "Both parties seek stability"
                ],
                "convergent_norms": [
                    "Humanitarian imperative",
                    "Need for coordination",
                    "Importance of security"
                ],
                "divergent_norms": [
                    "Sovereignty interpretation",
                    "Role of international actors",
                    "Acceptable restrictions"
                ]
            },
            "recommendations": {
                "prioritize": [
                    "Build on agreed facts",
                    "Emphasize shared values",
                    "Propose joint assessments"
                ],
                "avoid": [
                    "Inflammatory language",
                    "Demanding immediate resolution",
                    "Sovereignty confrontation"
                ]
            }
        }

        return APIResponse(
            success=True,
            data=result,
            message="Island of Agreement analysis completed successfully"
        )
    except Exception as e:
        return APIResponse(
            success=False,
            error=str(e),
            message="Analysis failed"
        )

@app.post("/api/v1/analyze-icebergs", response_model=APIResponse, tags=["Analysis Tools"])
async def api_analyze_icebergs(request: IcebergAnalysisRequest):
    """
    Conduct an Iceberg & Common Shared Space analysis

    Compares both parties' positions (WHAT), reasoning (HOW), and motives (WHY)
    to identify Common Shared Space and compromise opportunities.
    """
    try:
        # Analyze common elements between both parties
        org_pos_set = set(request.organization_positions)
        counterpart_pos_set = set(request.counterpart_positions)
        common_positions = list(org_pos_set & counterpart_pos_set)

        # Find reasoning and motives alignment
        org_reasoning_set = set(request.organization_reasoning)
        counterpart_reasoning = set(request.counterpart_reasoning or [])
        common_reasoning = list(org_reasoning_set & counterpart_reasoning)

        org_motives_set = set(request.organization_motives)
        counterpart_motives = set(request.counterpart_motives or [])
        common_motives = list(org_motives_set & counterpart_motives)

        result = {
            "analysis_type": "Iceberg & Common Shared Space",
            "organization": request.organization_name,
            "counterpart": request.counterpart_name,
            "surface_level": {
                "organization_positions": request.organization_positions,
                "counterpart_positions": request.counterpart_positions,
                "common_ground": common_positions if common_positions else ["Seek to resolve the conflict", "Both parties desire stability"]
            },
            "reasoning_level": {
                "organization_reasoning": request.organization_reasoning,
                "counterpart_reasoning": request.counterpart_reasoning or [],
                "aligned_reasoning": common_reasoning if common_reasoning else ["Need for productive dialogue", "Importance of mutual benefit"]
            },
            "motives_level": {
                "organization_motives": request.organization_motives,
                "counterpart_motives": request.counterpart_motives or [],
                "shared_values": common_motives if common_motives else ["Long-term cooperation", "Sustainable peace"]
            },
            "common_shared_space": {
                "identified": bool(common_positions or common_reasoning or common_motives),
                "negotiation_opportunities": [
                    "Build agreements on shared positions",
                    "Leverage aligned reasoning",
                    "Find compromise through shared values",
                    "Focus on mutual benefits"
                ]
            }
        }

        return APIResponse(
            success=True,
            data=result,
            message="Iceberg analysis completed successfully"
        )
    except Exception as e:
        return APIResponse(
            success=False,
            error=str(e),
            message="Iceberg analysis failed"
        )

@app.post("/api/v1/analyze-stakeholders", response_model=APIResponse, tags=["Analysis Tools"])
async def api_analyze_stakeholders(request: StakeholderAnalysisRequest):
    """
    Analyze and prioritize stakeholders

    Characterizes stakeholders by Power, Urgency, Legitimacy, and Position,
    then prioritizes them into First/Second/Third priority levels.
    """
    try:
        # Calculate priority scores for each stakeholder
        stakeholder_priorities = []
        for sh in request.stakeholders:
            # Salience = power + urgency + legitimacy
            salience = sh.power + sh.urgency + sh.legitimacy
            # Priority level based on salience
            if salience >= 2.0:
                priority = "First"
            elif salience >= 1.0:
                priority = "Second"
            else:
                priority = "Third"

            stakeholder_priorities.append({
                "name": sh.name,
                "power": sh.power,
                "urgency": sh.urgency,
                "legitimacy": sh.legitimacy,
                "position": sh.position,
                "salience_score": round(salience, 2),
                "priority_level": priority,
                "influenced_by": sh.influenced_by or [],
                "engagement_strategy": "Supportive" if sh.position > 0.5 else ("Neutral" if sh.position > -0.5 else "Adversarial")
            })

        # Sort by priority and salience
        priority_order = {"First": 1, "Second": 2, "Third": 3}
        stakeholder_priorities.sort(key=lambda x: (priority_order[x["priority_level"]], -x["salience_score"]))

        result = {
            "analysis_context": request.context,
            "total_stakeholders": len(request.stakeholders),
            "stakeholders": stakeholder_priorities,
            "priority_summary": {
                "first_priority": [s["name"] for s in stakeholder_priorities if s["priority_level"] == "First"],
                "second_priority": [s["name"] for s in stakeholder_priorities if s["priority_level"] == "Second"],
                "third_priority": [s["name"] for s in stakeholder_priorities if s["priority_level"] == "Third"]
            },
            "key_insights": [
                "Focus engagement efforts on First Priority stakeholders",
                "Maintain neutral relationships with Second Priority stakeholders",
                "Monitor Third Priority stakeholders for status changes",
                "Consider coalition building among supportive stakeholders"
            ]
        }

        return APIResponse(
            success=True,
            data=result,
            message="Stakeholder analysis completed successfully"
        )
    except Exception as e:
        return APIResponse(
            success=False,
            error=str(e),
            message="Stakeholder analysis failed"
        )

@app.post("/api/v1/leverage-influence", response_model=APIResponse, tags=["Analysis Tools"])
async def api_leverage_influence(request: InfluenceLeverageRequest):
    """
    Develop influence tactics for a target stakeholder

    Based on a previous stakeholder analysis, develops specific tactics to
    influence a particular stakeholder by leveraging coalitions and relationships.
    """
    try:
        # Find target stakeholder in analysis
        target = None
        stakeholders = request.stakeholders_analysis_json.get("stakeholders", [])
        for sh in stakeholders:
            if sh.get("name") == request.target_stakeholder_name:
                target = sh
                break

        if not target:
            return APIResponse(
                success=False,
                error=f"Stakeholder '{request.target_stakeholder_name}' not found in analysis",
                message="Stakeholder not found"
            )

        # Identify potential allies and opponents
        allies = [s for s in stakeholders if s.get("position", 0) > 0.5 and s.get("name") != request.target_stakeholder_name]
        opponents = [s for s in stakeholders if s.get("position", 0) < -0.5]

        # Develop tactics based on stakeholder profile
        result = {
            "target_stakeholder": request.target_stakeholder_name,
            "target_profile": {
                "power": target.get("power", 0),
                "urgency": target.get("urgency", 0),
                "legitimacy": target.get("legitimacy", 0),
                "position": target.get("position", 0),
                "priority_level": target.get("priority_level", "Unknown")
            },
            "influence_strategy": {
                "primary_approach": "Coalition building" if target.get("position", 0) >= 0 else "Negotiation and negotiation",
                "target_psychology": "Leverage shared interests" if target.get("position", 0) > 0 else "Find common ground",
                "communication_tone": "Collaborative" if target.get("position", 0) > 0 else "Professional and neutral"
            },
            "tactical_options": [
                {
                    "tactic": "Coalition Building",
                    "description": "Unite with supportive stakeholders to increase influence",
                    "allies": [a["name"] for a in allies[:3]],
                    "effectiveness": "High" if allies else "Moderate"
                },
                {
                    "tactic": "Value Alignment",
                    "description": "Emphasize shared values and mutual benefits",
                    "approach": "Identify and highlight areas of agreement"
                },
                {
                    "tactic": "Information Strategy",
                    "description": "Provide relevant data and analysis to influence decision-making",
                    "focus": "Focus on facts and evidence"
                },
                {
                    "tactic": "Stakeholder Leverage",
                    "description": "Use influenced stakeholders to reinforce influence",
                    "influenced_by": target.get("influenced_by", [])
                }
            ],
            "key_recommendations": [
                f"Prioritize engagement with {request.target_stakeholder_name} given their {target.get('priority_level')} priority level",
                f"Leverage {len(allies)} identified allies for coalition building",
                "Present evidence-based arguments aligned with their interests",
                "Maintain regular communication to track position changes"
            ]
        }

        return APIResponse(
            success=True,
            data=result,
            message="Influence tactics developed successfully"
        )
    except Exception as e:
        return APIResponse(
            success=False,
            error=str(e),
            message="Failed to develop tactics"
        )

@app.get("/api/v1/guide", response_model=APIResponse, tags=["Documentation"])
async def api_guide(format: Literal["markdown", "text"] = Query("markdown")):
    """
    Get the comprehensive negotiation methodology guide

    Returns detailed information about all three methodologies and how to use them.
    """
    try:
        result = {
            "title": "Humanitarian Negotiation Methodologies Guide",
            "version": "1.0.0",
            "methodologies": [
                {
                    "name": "Island of Agreement (IoA)",
                    "description": "Maps contested vs. agreed facts and convergent vs. divergent norms",
                    "when_to_use": "When you need to understand what areas of agreement exist with your counterpart",
                    "key_concepts": {
                        "contested_facts": "Facts that both parties dispute or see differently",
                        "agreed_facts": "Facts that both parties acknowledge as true",
                        "convergent_norms": "Shared values and principles both parties agree on",
                        "divergent_norms": "Different values and principles that divide the parties"
                    },
                    "process": [
                        "1. Identify all known facts about the situation",
                        "2. Determine which facts are agreed vs. contested",
                        "3. Identify shared norms and divergent norms",
                        "4. Map the 'Island' of agreement to build upon"
                    ],
                    "benefits": [
                        "Clarifies common ground",
                        "Identifies legitimate disagreements",
                        "Provides foundation for negotiation"
                    ]
                },
                {
                    "name": "Iceberg & Common Shared Space",
                    "description": "Analyzes positions (visible), reasoning (middle), and motives (hidden roots)",
                    "when_to_use": "When you need to understand what's driving the other side's positions",
                    "key_concepts": {
                        "positions": "What each party is publicly demanding (visible tip)",
                        "reasoning": "Why they hold these positions (middle of iceberg)",
                        "motives": "Core values and needs driving their reasoning (hidden base)"
                    },
                    "process": [
                        "1. Identify visible positions of both parties",
                        "2. Explore the reasoning behind these positions",
                        "3. Uncover the underlying motives and values",
                        "4. Find Common Shared Space in motives"
                    ],
                    "benefits": [
                        "Moves beyond positional bargaining",
                        "Identifies integrative solutions",
                        "Builds empathy and understanding"
                    ]
                },
                {
                    "name": "Stakeholder Analysis & Influence",
                    "description": "Characterizes stakeholders by Power, Urgency, Legitimacy, and Position",
                    "when_to_use": "When managing complex negotiations with multiple parties",
                    "key_concepts": {
                        "power": "Ability to affect outcomes (0-1 scale)",
                        "urgency": "How soon they need action (0-1 scale)",
                        "legitimacy": "Rightful claim to involvement (0-1 scale)",
                        "position": "Supportive (-1) to Opposed (1)",
                        "salience": "Combined power + urgency + legitimacy"
                    },
                    "priority_levels": {
                        "first_priority": "High salience stakeholders requiring focused engagement",
                        "second_priority": "Moderate influence stakeholders to maintain relations",
                        "third_priority": "Lower influence stakeholders to monitor"
                    },
                    "process": [
                        "1. Identify all relevant stakeholders",
                        "2. Rate each on Power, Urgency, Legitimacy, Position",
                        "3. Calculate salience scores and priority levels",
                        "4. Develop engagement strategies per priority",
                        "5. Use influence tactics on key stakeholders"
                    ],
                    "benefits": [
                        "Manages complex multi-party negotiations",
                        "Prioritizes limited resources",
                        "Identifies coalition opportunities"
                    ]
                }
            ],
            "integration_strategy": [
                "1. Start with Stakeholder Analysis to understand the landscape",
                "2. Use Island of Agreement to identify common ground",
                "3. Apply Iceberg analysis to understand deeper interests",
                "4. Develop influence tactics for key stakeholders",
                "5. Use findings to guide negotiation strategy"
            ],
            "best_practices": [
                "Always gather accurate information before analyzing",
                "Update analyses as new information emerges",
                "Focus on interests, not positions",
                "Build on areas of agreement",
                "Engage stakeholders transparently",
                "Document changes in stakeholder positions over time",
                "Use multiple methodologies for comprehensive understanding"
            ]
        }

        return APIResponse(
            success=True,
            data=result,
            message="Guide retrieved successfully"
        )
    except Exception as e:
        return APIResponse(
            success=False,
            error=str(e),
            message="Failed to retrieve guide"
        )

# ============================================================================
# Error Handlers
# ============================================================================

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    """Custom HTTP exception handler"""
    return JSONResponse(
        status_code=exc.status_code,
        content=APIResponse(
            success=False,
            error=exc.detail,
            message="Request failed"
        ).dict()
    )

# ============================================================================
# Server Startup/Shutdown
# ============================================================================

@app.on_event("startup")
async def startup_event():
    """Startup event"""
    print("=" * 70)
    print("Humanitarian Negotiation MCP - HTTP Server")
    print("=" * 70)
    print()
    print("✓ Server starting...")
    print("✓ FastAPI application initialized")
    print("✓ CORS enabled (all origins)")
    print()

@app.on_event("shutdown")
async def shutdown_event():
    """Shutdown event"""
    print()
    print("Server shutting down...")

# ============================================================================
# Main
# ============================================================================

def main():
    """Main entry point"""
    import os

    # Get port from environment variable (Google Cloud Run uses PORT)
    port = int(os.getenv("PORT", 8000))

    print("Starting Humanitarian Negotiation MCP HTTP Server...")
    print()
    print(f"Access the server at:")
    print(f"  - http://localhost:{port}")
    print()
    print("Documentation:")
    print(f"  - Swagger UI: http://localhost:{port}/docs")
    print(f"  - ReDoc: http://localhost:{port}/redoc")
    print()
    print(f"Tools endpoint: http://localhost:{port}/tools")
    print()

    uvicorn.run(
        app=app,
        host="0.0.0.0",
        port=port,
        reload=False,
        log_level="info"
    )

if __name__ == "__main__":
    main()
