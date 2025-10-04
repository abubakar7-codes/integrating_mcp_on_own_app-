#!/usr/bin/env python3
"""
Direct test of MCP tools without client connection
"""

import sys
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

def test_mcp_tools_direct():
    """Test MCP tools by calling them directly"""
    print("🧪 Testing MCP Tools Directly")
    print("=" * 50)
    
    # Import the actual tool functions
    from mcp_server import (
        add_transaction, get_transactions, get_financial_summary,
        create_budget, get_budget_status, create_financial_goal,
        get_financial_goals, analyze_spending_patterns
    )
    
    # Test 1: Add a transaction
    print("1. Testing add_transaction...")
    try:
        result = add_transaction(
            amount=100.0,
            description="Test income",
            transaction_type="income",
            category="test",
            user_id=1
        )
        print(f"   ✅ Transaction added: {result.get('id', 'Unknown ID')}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test 2: Add an expense
    print("\n2. Testing add_transaction (expense)...")
    try:
        result = add_transaction(
            amount=25.0,
            description="Test expense",
            transaction_type="expense",
            category="food",
            user_id=1
        )
        print(f"   ✅ Expense added: {result.get('id', 'Unknown ID')}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test 3: Get transactions
    print("\n3. Testing get_transactions...")
    try:
        result = get_transactions(user_id=1, limit=5)
        print(f"   ✅ Found {len(result)} transactions")
        for tx in result[:2]:
            print(f"      - {tx.get('description')}: ${tx.get('amount')} ({tx.get('transaction_type')})")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test 4: Get financial summary
    print("\n4. Testing get_financial_summary...")
    try:
        result = get_financial_summary(user_id=1)
        print(f"   ✅ Summary: Income=${result.get('total_income', 0)}, Expenses=${result.get('total_expenses', 0)}, Net=${result.get('net_worth', 0)}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test 5: Create budget
    print("\n5. Testing create_budget...")
    try:
        result = create_budget(
            name="Test Budget",
            category="food",
            amount=200.0,
            period="monthly",
            start_date="2024-01-01",
            end_date="2024-01-31",
            user_id=1
        )
        print(f"   ✅ Budget created: {result.get('id', 'Unknown ID')}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test 6: Get budget status
    print("\n6. Testing get_budget_status...")
    try:
        result = get_budget_status(user_id=1)
        print(f"   ✅ Found {len(result)} budgets")
        for budget in result:
            print(f"      - {budget.get('budget_name')}: ${budget.get('spent_amount', 0)}/${budget.get('budget_amount', 0)} ({budget.get('status')})")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test 7: Create financial goal
    print("\n7. Testing create_financial_goal...")
    try:
        result = create_financial_goal(
            title="Test Emergency Fund",
            description="Test emergency fund goal",
            target_amount=5000.0,
            target_date="2024-12-31",
            user_id=1
        )
        print(f"   ✅ Goal created: {result.get('id', 'Unknown ID')}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test 8: Get financial goals
    print("\n8. Testing get_financial_goals...")
    try:
        result = get_financial_goals(user_id=1)
        print(f"   ✅ Found {len(result)} goals")
        for goal in result:
            print(f"      - {goal.get('title')}: ${goal.get('current_amount', 0)}/${goal.get('target_amount', 0)} ({goal.get('progress_percentage', 0)}%)")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test 9: Analyze spending patterns
    print("\n9. Testing analyze_spending_patterns...")
    try:
        result = analyze_spending_patterns(user_id=1, days=30)
        print(f"   ✅ Analysis: Total spent=${result.get('total_spent', 0)}, Avg daily=${result.get('average_daily_spending', 0)}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    print("\n🎉 All MCP Tools Testing Completed!")
    print("=" * 50)

if __name__ == "__main__":
    test_mcp_tools_direct()
