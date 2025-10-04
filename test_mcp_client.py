#!/usr/bin/env python3
"""
Test client for the Finance Tracker MCP Server
This script demonstrates how to interact with the MCP server tools.
"""

import asyncio
import json
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def test_mcp_server():
    """Test the MCP server tools"""
    
    # Server parameters
    server_params = StdioServerParameters(
        command="python",
        args=["start_mcp_server.py"]
    )
    
    print("🔗 Connecting to Finance Tracker MCP Server...")
    
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the session
            await session.initialize()
            
            print("✅ Connected to MCP server!")
            print()
            
            # List available tools
            print("📋 Available tools:")
            tools = await session.list_tools()
            for tool in tools.tools:
                print(f"  • {tool.name}: {tool.description}")
            print()
            
            # Test adding a transaction
            print("🧪 Testing: Adding a transaction...")
            try:
                result = await session.call_tool(
                    "add_transaction",
                    {
                        "amount": 1500.0,
                        "description": "Salary payment",
                        "transaction_type": "income",
                        "category": "salary"
                    }
                )
                print(f"✅ Transaction added: {result.content}")
            except Exception as e:
                print(f"❌ Error adding transaction: {e}")
            
            # Test adding an expense
            print("\n🧪 Testing: Adding an expense...")
            try:
                result = await session.call_tool(
                    "add_transaction",
                    {
                        "amount": 50.0,
                        "description": "Grocery shopping",
                        "transaction_type": "expense",
                        "category": "food"
                    }
                )
                print(f"✅ Expense added: {result.content}")
            except Exception as e:
                print(f"❌ Error adding expense: {e}")
            
            # Test getting financial summary
            print("\n🧪 Testing: Getting financial summary...")
            try:
                result = await session.call_tool("get_financial_summary", {})
                print(f"✅ Financial summary: {result.content}")
            except Exception as e:
                print(f"❌ Error getting summary: {e}")
            
            # Test creating a budget
            print("\n🧪 Testing: Creating a budget...")
            try:
                result = await session.call_tool(
                    "create_budget",
                    {
                        "name": "Monthly Food Budget",
                        "category": "food",
                        "amount": 300.0,
                        "period": "monthly",
                        "start_date": "2024-01-01",
                        "end_date": "2024-01-31"
                    }
                )
                print(f"✅ Budget created: {result.content}")
            except Exception as e:
                print(f"❌ Error creating budget: {e}")
            
            # Test getting budget status
            print("\n🧪 Testing: Getting budget status...")
            try:
                result = await session.call_tool("get_budget_status", {})
                print(f"✅ Budget status: {result.content}")
            except Exception as e:
                print(f"❌ Error getting budget status: {e}")
            
            # Test creating a financial goal
            print("\n🧪 Testing: Creating a financial goal...")
            try:
                result = await session.call_tool(
                    "create_financial_goal",
                    {
                        "title": "Emergency Fund",
                        "description": "Build emergency fund for 6 months expenses",
                        "target_amount": 10000.0,
                        "target_date": "2024-12-31"
                    }
                )
                print(f"✅ Goal created: {result.content}")
            except Exception as e:
                print(f"❌ Error creating goal: {e}")
            
            # Test analyzing spending patterns
            print("\n🧪 Testing: Analyzing spending patterns...")
            try:
                result = await session.call_tool("analyze_spending_patterns", {"days": 30})
                print(f"✅ Spending analysis: {result.content}")
            except Exception as e:
                print(f"❌ Error analyzing spending: {e}")
            
            print("\n🎉 MCP server testing completed!")

if __name__ == "__main__":
    print("Finance Tracker MCP Server Test Client")
    print("=" * 50)
    asyncio.run(test_mcp_server())
