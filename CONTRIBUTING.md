# Contributing to Humanitarian Negotiation MCP

Thank you for your interest in contributing to the Humanitarian Negotiation MCP Server! This project aims to provide accessible, high-quality tools for humanitarian negotiation analysis.

## Code of Conduct

- Be respectful and inclusive
- Focus on constructive feedback
- Welcome diverse perspectives
- Support the mission of humanitarian negotiation

## How to Contribute

### Reporting Bugs

1. Check existing issues to avoid duplicates
2. Create a new issue with:
   - Clear, descriptive title
   - Detailed description of the issue
   - Steps to reproduce
   - Expected vs. actual behavior
   - Python version and OS

### Suggesting Enhancements

1. Open an issue with the tag "enhancement"
2. Describe the enhancement and use case
3. Explain why it would be useful
4. Provide examples if applicable

### Submitting Code

1. **Fork the repository**
2. **Create a feature branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Follow code standards:**
   - Python 3.10+ compatible
   - Follow PEP 8 style guide
   - Use type hints throughout
   - Add docstrings for all functions
   - Include comments for complex logic

4. **Test your changes:**
   ```bash
   python -m py_compile humanitarian_negotiation_mcp.py
   python humanitarian_negotiation_mcp.py  # Basic functionality test
   ```

5. **Update documentation:**
   - Update README.md if adding features
   - Add examples to DEPLOYMENT.md if relevant
   - Update docstrings in code

6. **Commit with clear messages:**
   ```bash
   git commit -m "Add feature: Brief description"
   ```

7. **Push and create a Pull Request:**
   - Push to your fork
   - Create PR against main branch
   - Provide clear description of changes
   - Reference any related issues

## Code Style

### Python Standards

```python
# Type hints required
def analyze_negotiation(context: str, stakeholders: list[dict]) -> dict:
    """
    Analyze humanitarian negotiation context.

    Args:
        context: Negotiation context description
        stakeholders: List of stakeholder dictionaries

    Returns:
        Analysis results as dictionary
    """
    # Implementation here
    pass
```

### Documentation

- All public functions must have docstrings
- Include parameter types and return types
- Add usage examples for complex functions
- Keep documentation up to date

### Testing Approach

Verify your changes with:

```bash
# Syntax check
python -m py_compile humanitarian_negotiation_mcp.py

# Import check
python -c "from humanitarian_negotiation_mcp import mcp"

# Manual testing with Claude Desktop
# Test each tool with the examples in README.md
```

## Development Workflow

### Setting Up Development Environment

```bash
# Clone the repository
git clone https://github.com/jhozman/humanitarian-negotiation-mcp.git
cd humanitarian-negotiation-mcp

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements_mcp.txt

# Test installation
python setup.py
```

### Making Changes

1. Create feature branch from main
2. Make your changes
3. Test thoroughly
4. Update documentation
5. Create pull request

### Pull Request Process

1. **Ensure code quality:**
   - No syntax errors
   - Follows code style
   - Type hints included
   - Documentation updated

2. **Describe your changes:**
   - Clear title and description
   - Why this change is needed
   - What problems it solves
   - Any breaking changes

3. **Reference issues:**
   - Link to related issues
   - Close issues if applicable

4. **Be responsive:**
   - Respond to review feedback
   - Make requested changes
   - Test suggested modifications

## Areas for Contribution

### High Priority

- Bug fixes and stability improvements
- Performance optimizations
- Documentation improvements
- User experience enhancements

### Medium Priority

- New negotiation methodologies
- Additional output formats
- Deployment guides for new platforms
- Translation of documentation

### Lower Priority

- Visual enhancements
- Additional examples
- Community sharing

## Recognition

Contributors will be:
- Listed in README.md acknowledgments
- Credited in commit messages
- Recognized in release notes

## Questions?

- Check existing documentation
- Review closed issues for solutions
- Open a discussion issue
- Contact the maintainer

## License

By contributing to this project, you agree that your contributions will be licensed under the MIT License, the same license as the project.

---

**Thanks for helping make humanitarian negotiation analysis more accessible!**

**Developed by**: Jhozman Camacho
**License**: MIT
