#!/usr/bin/env python3
"""
Simple MCP Server Test
Tests the MCP server tools directly without client connection
"""

import sys
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from mcp_server import mcp
from sqlalchemy.orm import Session
from app.database import engine
from app.models import Transaction, TransactionType
import json

def test_mcp_tools():
    """Test MCP tools directly"""
    print("🧪 Testing MCP Server Tools Directly")
    print("=" * 50)
    
    # Test 1: Add a transaction
    print("1. Testing add_transaction...")
    try:
        # Import the tool function directly
        from mcp_server import add_transaction
        result = add_transaction(
            amount=100.0,
            description="Test transaction",
            transaction_type="income",
            category="test",
            user_id=1
        )
        print(f"   ✅ Result: {result}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test 2: Get transactions
    print("\n2. Testing get_transactions...")
    try:
        from mcp_server import get_transactions
        result = get_transactions(user_id=1, limit=5)
        print(f"   ✅ Found {len(result)} transactions")
        for tx in result[:2]:  # Show first 2
            print(f"      - {tx.get('description', 'N/A')}: ${tx.get('amount', 0)}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test 3: Get financial summary
    print("\n3. Testing get_financial_summary...")
    try:
        from mcp_server import get_financial_summary
        result = get_financial_summary(user_id=1)
        print(f"   ✅ Summary: {result}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test 4: Create budget
    print("\n4. Testing create_budget...")
    try:
        from mcp_server import create_budget
        result = create_budget(
            name="Test Budget",
            category="test",
            amount=500.0,
            period="monthly",
            start_date="2024-01-01",
            end_date="2024-01-31",
            user_id=1
        )
        print(f"   ✅ Budget created: {result}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test 5: Get budget status
    print("\n5. Testing get_budget_status...")
    try:
        from mcp_server import get_budget_status
        result = get_budget_status(user_id=1)
        print(f"   ✅ Budget status: {len(result)} budgets found")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test 6: Create financial goal
    print("\n6. Testing create_financial_goal...")
    try:
        from mcp_server import create_financial_goal
        result = create_financial_goal(
            title="Test Goal",
            description="Test financial goal",
            target_amount=1000.0,
            target_date="2024-12-31",
            user_id=1
        )
        print(f"   ✅ Goal created: {result}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test 7: Analyze spending patterns
    print("\n7. Testing analyze_spending_patterns...")
    try:
        from mcp_server import analyze_spending_patterns
        result = analyze_spending_patterns(user_id=1, days=30)
        print(f"   ✅ Analysis: {result}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    print("\n🎉 MCP Tools Testing Completed!")
    print("=" * 50)

if __name__ == "__main__":
    test_mcp_tools()
