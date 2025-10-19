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

# Import the MCP tools
# Note: This imports the tool functions directly
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from humanitarian_negotiation_mcp import mcp
except ImportError:
    print("Error: Could not import humanitarian_negotiation_mcp")
    print("Make sure humanitarian_negotiation_mcp.py is in the same directory")
    sys.exit(1)

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
        # Call the MCP tool
        result = await mcp.call_tool(
            "humanitarian_create_island_of_agreement",
            {
                "situation_description": request.situation_description,
                "organization_name": request.organization_name,
                "counterpart_name": request.counterpart_name,
                "additional_context": request.additional_context or "",
                "response_format": request.response_format,
                "detail_level": request.detail_level
            }
        )

        return APIResponse(
            success=True,
            data=result,
            message="Island of Agreement analysis completed successfully"
        )
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Analysis failed: {str(e)}"
        )

@app.post("/api/v1/analyze-icebergs", response_model=APIResponse, tags=["Analysis Tools"])
async def api_analyze_icebergs(request: IcebergAnalysisRequest):
    """
    Conduct an Iceberg & Common Shared Space analysis

    Compares both parties' positions (WHAT), reasoning (HOW), and motives (WHY)
    to identify Common Shared Space and compromise opportunities.
    """
    try:
        result = await mcp.call_tool(
            "humanitarian_analyze_icebergs",
            {
                "organization_name": request.organization_name,
                "counterpart_name": request.counterpart_name,
                "organization_positions": request.organization_positions,
                "organization_reasoning": request.organization_reasoning,
                "organization_motives": request.organization_motives,
                "counterpart_positions": request.counterpart_positions,
                "counterpart_assumed_reasoning": request.counterpart_reasoning or [],
                "counterpart_assumed_motives": request.counterpart_motives or [],
                "response_format": request.response_format,
                "detail_level": request.detail_level
            }
        )

        return APIResponse(
            success=True,
            data=result,
            message="Iceberg analysis completed successfully"
        )
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Analysis failed: {str(e)}"
        )

@app.post("/api/v1/analyze-stakeholders", response_model=APIResponse, tags=["Analysis Tools"])
async def api_analyze_stakeholders(request: StakeholderAnalysisRequest):
    """
    Analyze and prioritize stakeholders

    Characterizes stakeholders by Power, Urgency, Legitimacy, and Position,
    then prioritizes them into First/Second/Third priority levels.
    """
    try:
        # Convert stakeholders to format expected by MCP
        stakeholders_dict = []
        for sh in request.stakeholders:
            stakeholders_dict.append({
                "name": sh.name,
                "power": sh.power,
                "urgency": sh.urgency,
                "legitimacy": sh.legitimacy,
                "position": sh.position,
                "influenced_by": sh.influenced_by or []
            })

        result = await mcp.call_tool(
            "humanitarian_analyze_stakeholders",
            {
                "context": request.context,
                "stakeholders": stakeholders_dict,
                "response_format": request.response_format,
                "detail_level": request.detail_level
            }
        )

        return APIResponse(
            success=True,
            data=result,
            message="Stakeholder analysis completed successfully"
        )
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Analysis failed: {str(e)}"
        )

@app.post("/api/v1/leverage-influence", response_model=APIResponse, tags=["Analysis Tools"])
async def api_leverage_influence(request: InfluenceLeverageRequest):
    """
    Develop influence tactics for a target stakeholder

    Based on a previous stakeholder analysis, develops specific tactics to
    influence a particular stakeholder by leveraging coalitions and relationships.
    """
    try:
        result = await mcp.call_tool(
            "humanitarian_leverage_stakeholder_influence",
            {
                "target_stakeholder_name": request.target_stakeholder_name,
                "stakeholders_analysis_json": request.stakeholders_analysis_json,
                "response_format": request.response_format
            }
        )

        return APIResponse(
            success=True,
            data=result,
            message="Influence tactics developed successfully"
        )
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Failed to develop tactics: {str(e)}"
        )

@app.get("/api/v1/guide", response_model=APIResponse, tags=["Documentation"])
async def api_guide(format: Literal["markdown", "text"] = Query("markdown")):
    """
    Get the comprehensive negotiation methodology guide

    Returns detailed information about all three methodologies and how to use them.
    """
    try:
        result = await mcp.call_tool(
            "humanitarian_negotiation_guide",
            {}
        )

        return APIResponse(
            success=True,
            data=result,
            message="Guide retrieved successfully"
        )
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Failed to retrieve guide: {str(e)}"
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
    print("Starting Humanitarian Negotiation MCP HTTP Server...")
    print()
    print("Access the server at:")
    print("  - http://localhost:8000")
    print()
    print("Documentation:")
    print("  - Swagger UI: http://localhost:8000/docs")
    print("  - ReDoc: http://localhost:8000/redoc")
    print()
    print("Tools endpoint: http://localhost:8000/tools")
    print()

    uvicorn.run(
        "http_server:app",
        host="0.0.0.0",
        port=8000,
        reload=False,
        log_level="info"
    )

if __name__ == "__main__":
    main()
