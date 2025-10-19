@echo off
REM ===================================================================
REM Humanitarian Negotiation MCP - Claude Desktop Installation Script
REM Version: 1.0.0
REM Description: Automated installer for Humanitarian Negotiation MCP Server
REM Developed by: Jhozman Camacho
REM License: MIT
REM ===================================================================

setlocal enabledelayedexpansion
cd /d "%~dp0"

echo.
echo ===================================================================
echo Humanitarian Negotiation MCP - Claude Desktop Installer
echo Developed by: Jhozman Camacho
echo License: MIT
echo ===================================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH
    echo Please install Python 3.10 or higher from https://www.python.org
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

echo [OK] Python found:
python --version
echo.

REM Install dependencies
echo [STEP 1/4] Installing MCP dependencies...
pip install -r requirements_mcp.txt
if errorlevel 1 (
    echo [ERROR] Failed to install dependencies
    pause
    exit /b 1
)
echo [OK] Dependencies installed successfully
echo.

REM Get the full path of the MCP script
set "MCP_PATH=%CD%\humanitarian_negotiation_mcp.py"
echo [STEP 2/4] MCP Server Path: %MCP_PATH%
echo.

REM Get Claude config path
set "CLAUDE_CONFIG=%APPDATA%\Claude\claude_desktop_config.json"

echo [STEP 3/4] Configuring Claude Desktop...
echo Claude config location: %CLAUDE_CONFIG%
echo.

REM Check if Claude Desktop config exists
if not exist "%APPDATA%\Claude\" (
    echo [INFO] Creating Claude config directory...
    mkdir "%APPDATA%\Claude"
)

REM Create or update the Claude Desktop config
if not exist "%CLAUDE_CONFIG%" (
    echo [INFO] Creating new Claude Desktop config...
    (
        echo {
        echo   "mcpServers": {
        echo     "humanitarian-negotiation": {
        echo       "command": "python",
        echo       "args": ["%MCP_PATH%"]
        echo     }
        echo   }
        echo }
    ) > "%CLAUDE_CONFIG%"
    echo [OK] Config created successfully
) else (
    echo [INFO] Claude config already exists
    echo [WARNING] Please manually add the following to %CLAUDE_CONFIG%:
    echo.
    echo   "humanitarian-negotiation": {
    echo     "command": "python",
    echo     "args": ["%MCP_PATH%"]
    echo   }
    echo.
)

echo [STEP 4/4] Verifying installation...
if exist "%MCP_PATH%" (
    echo [OK] MCP server file found: %MCP_PATH%
) else (
    echo [ERROR] MCP server file not found
    pause
    exit /b 1
)

echo.
echo ===================================================================
echo Installation Complete!
echo ===================================================================
echo.
echo NEXT STEPS:
echo 1. Restart Claude Desktop completely
echo 2. Check that the "humanitarian-negotiation" MCP is available
echo 3. Start using the FACT Negotiation tools
echo.
echo CONFIGURATION DETAILS:
echo - Python Version:
python --version
echo - MCP Server: %MCP_PATH%
echo - Config File: %CLAUDE_CONFIG%
echo.
echo AVAILABLE TOOLS:
echo - humanitarian_create_island_of_agreement
echo - humanitarian_analyze_icebergs
echo - humanitarian_analyze_stakeholders
echo - humanitarian_leverage_stakeholder_influence
echo - humanitarian_negotiation_guide
echo.
echo For more information, see README.md
echo ===================================================================
echo.

pause
