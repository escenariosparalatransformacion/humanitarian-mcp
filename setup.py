#!/usr/bin/env python3
"""
Setup script for Humanitarian Negotiation MCP Server
Helps configure the server for use with Claude Desktop
"""

import json
import os
import platform
import sys
from pathlib import Path

def get_config_path():
    """Get the Claude Desktop config path for the current platform."""
    system = platform.system()
    
    if system == "Darwin":  # macOS
        return Path.home() / "Library/Application Support/Claude/claude_desktop_config.json"
    elif system == "Windows":
        return Path(os.getenv("APPDATA")) / "Claude/claude_desktop_config.json"
    elif system == "Linux":
        return Path.home() / ".config/Claude/claude_desktop_config.json"
    else:
        return None

def get_server_path():
    """Get the absolute path to the MCP server script."""
    return Path(__file__).parent.absolute() / "humanitarian_negotiation_mcp.py"

def read_config(config_path):
    """Read existing Claude Desktop config."""
    if not config_path.exists():
        return {"mcpServers": {}}
    
    try:
        with open(config_path, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        print(f"Warning: Config file exists but is not valid JSON: {config_path}")
        return {"mcpServers": {}}

def write_config(config_path, config):
    """Write Claude Desktop config."""
    # Ensure directory exists
    config_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=2)

def check_python_version():
    """Check if Python version is adequate."""
    if sys.version_info < (3, 10):
        print("Error: Python 3.10 or higher is required")
        print(f"Current version: {sys.version}")
        return False
    return True

def check_dependencies():
    """Check if required dependencies are installed."""
    required = ['mcp', 'pydantic', 'httpx']
    missing = []
    
    for package in required:
        try:
            __import__(package)
        except ImportError:
            missing.append(package)
    
    return missing

def main():
    """Main setup function."""
    print("=" * 70)
    print("Humanitarian Negotiation MCP Server - Setup")
    print("=" * 70)
    print()
    
    # Check Python version
    print("1. Checking Python version...")
    if not check_python_version():
        sys.exit(1)
    print(f"   [OK] Python {sys.version.split()[0]} - OK")
    print()

    # Check dependencies
    print("2. Checking dependencies...")
    missing = check_dependencies()
    if missing:
        print(f"   [ERROR] Missing dependencies: {', '.join(missing)}")
        print()
        print("   Please install dependencies first:")
        print("   pip install -r requirements_mcp.txt")
        print()
        response = input("   Continue anyway? (y/n): ")
        if response.lower() != 'y':
            sys.exit(1)
    else:
        print("   [OK] All dependencies installed")
    print()

    # Get config path
    print("3. Locating Claude Desktop config...")
    config_path = get_config_path()
    if config_path is None:
        print("   [ERROR] Could not determine config path for this platform")
        print()
        print("   Please manually add the following to your Claude Desktop config:")
        server_path = get_server_path()
        print()
        print("   {")
        print("     \"mcpServers\": {")
        print("       \"humanitarian-negotiation\": {")
        print("         \"command\": \"python\",")
        print(f"         \"args\": [\"{server_path}\"]")
        print("       }")
        print("     }")
        print("   }")
        sys.exit(1)
    
    print(f"   [OK] Config path: {config_path}")
    print()

    # Get server path
    print("4. Locating MCP server script...")
    server_path = get_server_path()
    if not server_path.exists():
        print(f"   [ERROR] Server script not found: {server_path}")
        sys.exit(1)
    print(f"   [OK] Server path: {server_path}")
    print()

    # Read existing config
    print("5. Reading existing configuration...")
    config = read_config(config_path)
    if "mcpServers" not in config:
        config["mcpServers"] = {}
    print(f"   [OK] Found {len(config['mcpServers'])} existing MCP server(s)")
    print()

    # Check if already configured
    if "humanitarian-negotiation" in config["mcpServers"]:
        print("   [WARNING] Server 'humanitarian-negotiation' is already configured")
        print()
        print("   Current configuration:")
        print(f"   Command: {config['mcpServers']['humanitarian-negotiation'].get('command')}")
        print(f"   Args: {config['mcpServers']['humanitarian-negotiation'].get('args')}")
        print()
        response = input("   Overwrite existing configuration? (y/n): ")
        if response.lower() != 'y':
            print()
            print("Setup cancelled. No changes made.")
            sys.exit(0)
    
    # Add/update server configuration
    print("6. Configuring MCP server...")
    config["mcpServers"]["humanitarian-negotiation"] = {
        "command": "python" if platform.system() == "Windows" else "python3",
        "args": [str(server_path)]
    }

    # Write config
    try:
        write_config(config_path, config)
        print("   [OK] Configuration updated successfully")
    except Exception as e:
        print(f"   [ERROR] Error writing configuration: {e}")
        sys.exit(1)
    print()

    # Success message
    print("=" * 70)
    print("Setup completed successfully!")
    print("=" * 70)
    print()
    print("Next steps:")
    print("1. Restart Claude Desktop")
    print("2. Look for the [CONNECTED] icon to verify MCP connection")
    print("3. Use the humanitarian negotiation tools in your conversations")
    print()
    print("Available tools:")
    print("  - humanitarian_create_island_of_agreement")
    print("  - humanitarian_analyze_icebergs")
    print("  - humanitarian_analyze_stakeholders")
    print("  - humanitarian_leverage_stakeholder_influence")
    print("  - humanitarian_negotiation_guide")
    print()
    print("Documentation:")
    print("  - README.md - Overview and installation")
    print("  - EXAMPLES.md - Practical usage examples")
    print()
    print("For help, run: humanitarian_negotiation_guide")
    print("=" * 70)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
        print()
        print("Setup cancelled by user.")
        sys.exit(1)
