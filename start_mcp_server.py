#!/usr/bin/env python3
"""
Startup script for the Finance Tracker MCP Server
"""

import os
import sys
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

# Set environment variables for database
os.environ.setdefault("DATABASE_URL", "sqlite:///./finance_tracker.db")

if __name__ == "__main__":
    print("=" * 60)
    print("Finance Tracker MCP Server")
    print("=" * 60)
    print("Starting MCP server with the following tools:")
    print()
    print("Financial Management Tools:")
    print("  • add_transaction - Add income/expense transactions")
    print("  • get_transactions - Retrieve transactions with filters")
    print("  • get_financial_summary - Get comprehensive financial overview")
    print()
    print("Budget Management Tools:")
    print("  • create_budget - Create spending budgets")
    print("  • get_budget_status - Check budget performance")
    print()
    print("Goal Management Tools:")
    print("  • create_financial_goal - Set financial goals")
    print("  • get_financial_goals - View all goals")
    print()
    print("Analytics Tools:")
    print("  • analyze_spending_patterns - Analyze spending behavior")
    print()
    print("=" * 60)
    print("Server is starting...")
    print("=" * 60)
    
    # Import and run the MCP server
    from mcp_server import mcp
    mcp.run()
