#!/usr/bin/env python3
"""
MCP Server Startup Script for Gemini CLI Integration
Optimized for Gemini CLI compatibility
"""

import sys
import os
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

# Set environment variables
os.environ.setdefault("DATABASE_URL", "sqlite:///./finance_tracker_litequery.db")
os.environ.setdefault("PYTHONPATH", str(project_root))

# Import and run the MCP server
from mcp_server import mcp

if __name__ == "__main__":
    # Run the MCP server
    mcp.run()
