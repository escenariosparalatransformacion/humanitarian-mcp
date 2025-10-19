# Humanitarian Negotiation MCP Server - Project Summary

## Overview

This is a complete Model Context Protocol (MCP) server implementation for humanitarian negotiation analysis, based on proven methodologies used by international humanitarian organizations.

## What's Included

### Core Server File
**`humanitarian_negotiation_mcp.py`** (Main server implementation)
- 1,800+ lines of production-ready Python code
- 5 specialized tools for negotiation analysis
- Complete input validation using Pydantic v2
- Both Markdown and JSON output formats
- Comprehensive error handling and documentation

### Documentation Files

1. **`README.md`** - Complete project documentation
   - Installation instructions
   - Methodology overviews
   - Tool descriptions
   - Best practices
   - Use cases

2. **`EXAMPLES.md`** - Practical usage examples
   - Ready-to-use prompts for each tool
   - Complete workflow demonstrations
   - Real-world scenarios
   - Common pitfalls and solutions

3. **`QUICKSTART.md`** - Fast onboarding guide
   - 3-minute installation
   - 5-minute first use
   - Troubleshooting tips
   - Quick reference table

4. **`requirements_mcp.txt`** - Python dependencies
   - All required packages with versions
   - Ready for `pip install -r`

5. **`setup.py`** - Automated configuration script
   - Auto-detects Claude Desktop config location
   - Validates Python version and dependencies
   - Configures server automatically
   - Cross-platform support (macOS, Windows, Linux)

## Methodologies Implemented

### 1. Island of Agreement (IoA)
**Tool**: `humanitarian_create_island_of_agreement`

Categorizes negotiation elements into:
- **Contested Facts**: Need clarification (e.g., population numbers, security status)
- **Agreed Facts**: Common ground (e.g., crisis severity, need for action)
- **Convergent Norms**: Shared values (e.g., humanitarian principles)
- **Divergent Norms**: Normative differences (e.g., sovereignty vs. access)

**Output**: 4-column table + strategic recommendations

**Based on your documents**:
- Instructions_for_Setting_Up_an_AI_Assistant_for_Analysing_Complex_Environments.docx
- instructions1.txt

### 2. Iceberg & Common Shared Space (CSS)
**Tool**: `humanitarian_analyze_icebergs`

Analyzes three levels for each party:
- **WHAT** (Surface): Visible positions and demands
- **HOW** (Middle): Tactical reasoning and strategy
- **WHY** (Deep): Core motives and values

Identifies Common Shared Space where interests align and suggests compromise opportunities.

**Output**: Comparative iceberg table + compromise recommendations

**Based on your documents**:
- Instructions_For_Icebergs_and_CSS_New.docx
- instructions2.txt

### 3. Stakeholder Analysis
**Tools**: 
- `humanitarian_analyze_stakeholders` - Full analysis
- `humanitarian_leverage_stakeholder_influence` - Targeted tactics

Assesses stakeholders on:
- **Power**: Ability to influence decisions (0.0-1.0)
- **Urgency**: Time-sensitivity of issue (0.0-1.0)
- **Legitimacy**: Relevance to contribute (0.0-1.0)
- **Position**: Stance on issue (-1.0 to +1.0)

Prioritizes into First/Second/Third priority levels and develops engagement strategies.

**Output**: Characterization table + priority rankings + relationship mapping + influence pathways

**Based on your documents**:
- Instructions_for_Stakeholder_Analysis.docx
- instructions3.txt

### 4. Comprehensive Guide
**Tool**: `humanitarian_negotiation_guide`

Provides complete methodology documentation, workflow recommendations, and tool selection guidance.

## Technical Features

### Input Validation
- Pydantic v2 models with strict validation
- Field-level constraints (min/max length, ranges)
- Custom validators for complex rules
- Clear, actionable error messages

### Response Formats
- **Markdown**: Human-readable tables and formatted text
- **JSON**: Structured data for programmatic use
- **Detail Levels**: Concise or detailed analysis

### Scalability
- Character limits to prevent token overflow
- Pagination support for large datasets
- Configurable output verbosity
- Handles up to 50 stakeholders per analysis

### Error Handling
- Comprehensive try-catch blocks
- Descriptive error messages
- Input validation before processing
- Graceful degradation

### Documentation
- Detailed docstrings for all functions
- Type hints throughout
- Usage examples in tool descriptions
- MCP annotations for tool metadata

## Installation Process

### Quick Installation
```bash
# 1. Install dependencies
pip install -r requirements_mcp.txt

# 2. Run setup script
python setup.py

# 3. Restart Claude Desktop
```

### Manual Installation
1. Install Python 3.10+
2. Install dependencies from requirements_mcp.txt
3. Add server to Claude Desktop config:
```json
{
  "mcpServers": {
    "humanitarian-negotiation": {
      "command": "python",
      "args": ["/path/to/humanitarian_negotiation_mcp.py"]
    }
  }
}
```
4. Restart Claude Desktop

## Usage Examples

### Example 1: Starting a Negotiation
```
Use humanitarian_create_island_of_agreement to analyze a food aid negotiation 
between WFP and the Ministry of Agriculture...
```

### Example 2: Understanding Motivations
```
Conduct an Iceberg analysis comparing UNHCR and Border Security positions on 
refugee camp access...
```

### Example 3: Mapping Stakeholders
```
Analyze stakeholders for a ceasefire negotiation involving UN, government, 
armed opposition, and regional actors...
```

### Example 4: Influencing Key Actors
```
Develop influence tactics for the Armed Opposition Leader using the previous 
stakeholder analysis...
```

See **EXAMPLES.md** for complete, ready-to-use examples.

## File Structure

```
humanitarian-negotiation-mcp/
├── humanitarian_negotiation_mcp.py   # Main server (1,800+ lines)
├── setup.py                          # Automated setup script
├── requirements_mcp.txt              # Python dependencies
├── README.md                         # Complete documentation
├── EXAMPLES.md                       # Practical examples
├── QUICKSTART.md                     # Fast start guide
└── PROJECT_SUMMARY.md               # This file
```

## Key Capabilities

### For Humanitarian Negotiators
- Systematic analysis of complex negotiations
- Evidence-based strategy recommendations
- Stakeholder prioritization and engagement planning
- Influence pathway identification
- Coalition-building opportunities

### For Mediators
- Structured framework for understanding parties
- Common ground identification
- Compromise opportunity discovery
- Relationship mapping and analysis

### For Coordination Teams
- Multi-party stakeholder analysis
- Priority-based engagement strategies
- Influence leverage recommendations
- Risk identification and mitigation

## Technical Specifications

- **Language**: Python 3.10+
- **Framework**: MCP (Model Context Protocol)
- **SDK**: FastMCP from mcp-python-sdk
- **Validation**: Pydantic v2
- **Lines of Code**: ~1,800 (main server)
- **Tools**: 5 specialized analysis tools
- **Output Formats**: Markdown, JSON
- **Character Limit**: 25,000 per response
- **Max Stakeholders**: 50 per analysis

## Quality Standards

### Code Quality
✓ Type hints throughout
✓ Comprehensive docstrings
✓ Input validation on all parameters
✓ Error handling with clear messages
✓ DRY principle (no code duplication)
✓ Modular, composable functions

### MCP Standards
✓ Follows MCP best practices
✓ Proper tool annotations (readOnlyHint, etc.)
✓ Clear tool names and descriptions
✓ Detailed parameter documentation
✓ Example-rich descriptions

### User Experience
✓ Clear, actionable outputs
✓ Professional, formal tone
✓ Structured, scannable formatting
✓ Strategic recommendations
✓ Concrete next steps

## Testing Recommendations

### Basic Validation
```bash
# Check syntax
python -m py_compile humanitarian_negotiation_mcp.py

# Verify imports
python -c "from humanitarian_negotiation_mcp import mcp"
```

### Integration Testing
1. Install in Claude Desktop
2. Verify 🔌 connection icon appears
3. Test each tool with example prompts from EXAMPLES.md
4. Verify outputs match expected formats

### Production Readiness Checklist
- [ ] All dependencies installed
- [ ] Server configured in Claude Desktop
- [ ] All 5 tools accessible
- [ ] Markdown output renders correctly
- [ ] JSON output is valid
- [ ] Error messages are clear
- [ ] Setup script runs successfully

## Deployment Notes

### For Individual Users
- Use setup.py for automatic configuration
- Store server in permanent location (don't move after setup)
- Restart Claude Desktop after any changes

### For Teams
- Share entire directory with team members
- Each user runs setup.py independently
- Consider version control for customizations
- Document any organization-specific adaptations

### For Organizations
- Host server on shared infrastructure if needed
- Customize tool outputs for organizational templates
- Add organization-specific examples to EXAMPLES.md
- Train team members using QUICKSTART.md

## Customization Options

### Easy Customizations
- Adjust CHARACTER_LIMIT in server code
- Modify MAX_STAKEHOLDERS for larger analyses
- Add organization-specific examples to EXAMPLES.md
- Customize output formatting templates

### Advanced Customizations
- Add new analysis tools following existing patterns
- Integrate with organizational databases
- Implement custom validation rules
- Add organization-specific methodologies

## Support Materials

### For Developers
- Comprehensive inline documentation
- Type hints for IDE support
- Modular structure for easy extension
- Clear separation of concerns

### For Users
- QUICKSTART.md for fast onboarding
- EXAMPLES.md for practical guidance
- README.md for complete reference
- humanitarian_negotiation_guide tool for in-app help

### For Trainers
- Complete methodology explanations
- Ready-to-use training examples
- Best practice guidelines
- Common pitfalls documentation

## Success Metrics

After setup, users should be able to:
- [ ] Run first analysis within 5 minutes
- [ ] Understand all three methodologies within 15 minutes
- [ ] Apply to real negotiation within 30 minutes
- [ ] Generate actionable insights consistently

## Next Steps After Delivery

1. **Installation**: Run setup.py
2. **Learning**: Read QUICKSTART.md
3. **Practice**: Try examples from EXAMPLES.md
4. **Application**: Analyze real negotiation
5. **Iteration**: Refine based on outcomes
6. **Sharing**: Distribute to team members

## Technical Support

### Common Issues
- **Connection errors**: Verify server path in config
- **Invalid inputs**: Check parameter ranges and formats
- **Poor outputs**: Provide more detailed context
- **Missing dependencies**: Run `pip install -r requirements_mcp.txt`

### Troubleshooting Resources
- QUICKSTART.md has troubleshooting section
- setup.py validates configuration
- Error messages provide specific guidance
- README.md has detailed documentation

## Credits and Acknowledgments

**Methodologies based on**:
- Island of Agreement: UN humanitarian negotiation frameworks
- Iceberg/CSS: ICRC and humanitarian mediation practices
- Stakeholder Analysis: Mitchell-Agle-Wood framework adapted for humanitarian context

**Implemented using**:
- Model Context Protocol (MCP) by Anthropic
- FastMCP framework from mcp-python-sdk
- Pydantic for data validation

## License and Usage

[Include your chosen license terms]

**Recommended for**:
- Humanitarian organizations and agencies
- Mediation and conflict resolution practitioners
- Coordination bodies and clusters
- Training and capacity building programs

## Version Information

**Version**: 1.0.0
**Release Date**: 2025
**Python**: 3.10+
**MCP SDK**: 0.9.0+

## Final Notes

This is a production-ready, professional-grade MCP server that:
- Implements all three methodologies from your documentation
- Follows MCP best practices and standards
- Provides comprehensive documentation and examples
- Includes automated setup and configuration
- Scales to real-world humanitarian negotiations
- Delivers actionable, strategic insights

All files are ready for immediate use. Start with QUICKSTART.md for fastest onboarding.

---

**Ready to deploy!** 🚀
