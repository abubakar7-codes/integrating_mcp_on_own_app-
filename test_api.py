#!/usr/bin/env python3
"""
Comprehensive test script for the Personal Finance Tracker API
This script demonstrates all the API functionality step by step.
"""

import requests
import json
import time
from datetime import datetime, date, timedelta

# API base URL
BASE_URL = "http://127.0.0.1:8000"
API_URL = f"{BASE_URL}/api/v1"

def test_api_connection():
    """Test if the API is running"""
    try:
        response = requests.get(f"{BASE_URL}/")
        print("✅ API Connection Test")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        return True
    except requests.exceptions.ConnectionError:
        print("❌ API Connection Failed - Make sure the server is running!")
        print("Run: python run_server.py")
        return False

def register_user():
    """Step 1: Register a new user"""
    print("\n📝 Step 1: Registering a new user")
    
    user_data = {
        "email": "john.doe@example.com",
        "username": "johndoe",
        "password": "securepassword123",
        "full_name": "John Doe"
    }
    
    try:
        response = requests.post(f"{API_URL}/auth/register", json=user_data)
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            print("✅ User registered successfully!")
            print(f"User Details: {response.json()}")
            return True
        else:
            print(f"❌ Registration failed: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Error during registration: {e}")
        return False

def login_user():
    """Step 2: Login and get access token"""
    print("\n🔐 Step 2: Logging in user")
    
    login_data = {
        "username": "johndoe",
        "password": "securepassword123"
    }
    
    try:
        response = requests.post(f"{API_URL}/auth/login", data=login_data)
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            token_data = response.json()
            print("✅ Login successful!")
            print(f"Access Token: {token_data['access_token'][:20]}...")
            return token_data['access_token']
        else:
            print(f"❌ Login failed: {response.text}")
            return None
    except Exception as e:
        print(f"❌ Error during login: {e}")
        return None

def add_transactions(token):
    """Step 3: Add sample transactions"""
    print("\n💰 Step 3: Adding sample transactions")
    
    headers = {"Authorization": f"Bearer {token}"}
    
    # Sample transactions
    transactions = [
        {
            "amount": 5000.00,
            "description": "Monthly Salary",
            "transaction_type": "income",
            "category": "Salary",
            "date": datetime.now().isoformat()
        },
        {
            "amount": 1200.00,
            "description": "Rent Payment",
            "transaction_type": "expense",
            "category": "Housing",
            "date": datetime.now().isoformat()
        },
        {
            "amount": 300.00,
            "description": "Grocery Shopping",
            "transaction_type": "expense",
            "category": "Food",
            "date": datetime.now().isoformat()
        },
        {
            "amount": 150.00,
            "description": "Gas Bill",
            "transaction_type": "expense",
            "category": "Utilities",
            "date": datetime.now().isoformat()
        },
        {
            "amount": 200.00,
            "description": "Dining Out",
            "transaction_type": "expense",
            "category": "Food",
            "date": datetime.now().isoformat()
        }
    ]
    
    created_transactions = []
    for i, transaction in enumerate(transactions, 1):
        try:
            response = requests.post(f"{API_URL}/transactions/", json=transaction, headers=headers)
            if response.status_code == 200:
                created_transactions.append(response.json())
                print(f"✅ Transaction {i} added: {transaction['description']} - ${transaction['amount']}")
            else:
                print(f"❌ Failed to add transaction {i}: {response.text}")
        except Exception as e:
            print(f"❌ Error adding transaction {i}: {e}")
    
    return created_transactions

def create_budgets(token):
    """Step 4: Create budgets"""
    print("\n📊 Step 4: Creating budgets")
    
    headers = {"Authorization": f"Bearer {token}"}
    
    budgets = [
        {
            "name": "Monthly Food Budget",
            "category": "Food",
            "amount": 500.00,
            "period": "monthly",
            "start_date": datetime.now().isoformat(),
            "end_date": (datetime.now() + timedelta(days=30)).isoformat()
        },
        {
            "name": "Housing Budget",
            "category": "Housing",
            "amount": 1500.00,
            "period": "monthly",
            "start_date": datetime.now().isoformat(),
            "end_date": (datetime.now() + timedelta(days=30)).isoformat()
        },
        {
            "name": "Utilities Budget",
            "category": "Utilities",
            "amount": 200.00,
            "period": "monthly",
            "start_date": datetime.now().isoformat(),
            "end_date": (datetime.now() + timedelta(days=30)).isoformat()
        }
    ]
    
    created_budgets = []
    for i, budget in enumerate(budgets, 1):
        try:
            response = requests.post(f"{API_URL}/budgets/", json=budget, headers=headers)
            if response.status_code == 200:
                created_budgets.append(response.json())
                print(f"✅ Budget {i} created: {budget['name']} - ${budget['amount']}")
            else:
                print(f"❌ Failed to create budget {i}: {response.text}")
        except Exception as e:
            print(f"❌ Error creating budget {i}: {e}")
    
    return created_budgets

def create_goals(token):
    """Step 5: Create financial goals"""
    print("\n🎯 Step 5: Creating financial goals")
    
    headers = {"Authorization": f"Bearer {token}"}
    
    goals = [
        {
            "title": "Emergency Fund",
            "description": "Build a 6-month emergency fund",
            "target_amount": 15000.00,
            "current_amount": 2000.00,
            "target_date": (datetime.now() + timedelta(days=365)).isoformat()
        },
        {
            "title": "Vacation Fund",
            "description": "Save for a dream vacation",
            "target_amount": 5000.00,
            "current_amount": 500.00,
            "target_date": (datetime.now() + timedelta(days=180)).isoformat()
        },
        {
            "title": "New Car Fund",
            "target_amount": 25000.00,
            "current_amount": 5000.00,
            "target_date": (datetime.now() + timedelta(days=730)).isoformat()
        }
    ]
    
    created_goals = []
    for i, goal in enumerate(goals, 1):
        try:
            response = requests.post(f"{API_URL}/goals/", json=goal, headers=headers)
            if response.status_code == 200:
                created_goals.append(response.json())
                print(f"✅ Goal {i} created: {goal['title']} - ${goal['current_amount']}/${goal['target_amount']}")
            else:
                print(f"❌ Failed to create goal {i}: {response.text}")
        except Exception as e:
            print(f"❌ Error creating goal {i}: {e}")
    
    return created_goals

def generate_reports(token):
    """Step 6: Generate reports and analytics"""
    print("\n📈 Step 6: Generating reports and analytics")
    
    headers = {"Authorization": f"Bearer {token}"}
    
    # Get spending report
    try:
        response = requests.get(f"{API_URL}/reports/spending", headers=headers)
        if response.status_code == 200:
            report = response.json()
            print("✅ Spending Report Generated:")
            print(f"   Total Income: ${report['total_income']}")
            print(f"   Total Expenses: ${report['total_expenses']}")
            print(f"   Net Income: ${report['net_income']}")
            print(f"   Period: {report['period']}")
            print("   Category Breakdown:")
            for category, amount in report['category_breakdown'].items():
                print(f"     {category}: ${amount}")
        else:
            print(f"❌ Failed to get spending report: {response.text}")
    except Exception as e:
        print(f"❌ Error getting spending report: {e}")
    
    # Get budget status
    try:
        response = requests.get(f"{API_URL}/reports/budget-status", headers=headers)
        if response.status_code == 200:
            budget_statuses = response.json()
            print("\n✅ Budget Status Report:")
            for status in budget_statuses:
                print(f"   {status['budget_name']}: ${status['spent_amount']:.2f}/${status['budget_amount']:.2f} ({status['percentage_used']:.1f}%) - {status['status']}")
        else:
            print(f"❌ Failed to get budget status: {response.text}")
    except Exception as e:
        print(f"❌ Error getting budget status: {e}")

def test_csv_export(token):
    """Step 7: Test CSV export"""
    print("\n📄 Step 7: Testing CSV export")
    
    headers = {"Authorization": f"Bearer {token}"}
    
    try:
        response = requests.get(f"{API_URL}/reports/export/csv", headers=headers)
        if response.status_code == 200:
            csv_data = response.json()
            print("✅ CSV Export Successful!")
            print("CSV Content Preview:")
            print(csv_data['csv_content'][:500] + "..." if len(csv_data['csv_content']) > 500 else csv_data['csv_content'])
        else:
            print(f"❌ Failed to export CSV: {response.text}")
    except Exception as e:
        print(f"❌ Error exporting CSV: {e}")

def get_all_transactions(token):
    """Get all transactions to verify"""
    print("\n📋 Getting all transactions")
    
    headers = {"Authorization": f"Bearer {token}"}
    
    try:
        response = requests.get(f"{API_URL}/transactions/", headers=headers)
        if response.status_code == 200:
            transactions = response.json()
            print(f"✅ Retrieved {len(transactions)} transactions:")
            for transaction in transactions:
                print(f"   {transaction['description']}: ${transaction['amount']} ({transaction['transaction_type']})")
        else:
            print(f"❌ Failed to get transactions: {response.text}")
    except Exception as e:
        print(f"❌ Error getting transactions: {e}")

def main():
    """Main test function"""
    print("🚀 Personal Finance Tracker API - Comprehensive Test")
    print("=" * 60)
    
    # Test API connection
    if not test_api_connection():
        return
    
    # Register user
    if not register_user():
        return
    
    # Login and get token
    token = login_user()
    if not token:
        return
    
    # Add transactions
    transactions = add_transactions(token)
    
    # Create budgets
    budgets = create_budgets(token)
    
    # Create goals
    goals = create_goals(token)
    
    # Generate reports
    generate_reports(token)
    
    # Test CSV export
    test_csv_export(token)
    
    # Get all transactions
    get_all_transactions(token)
    
    print("\n🎉 All tests completed successfully!")
    print("\n📖 Next Steps:")
    print("1. Open http://127.0.0.1:8000/docs in your browser to see the interactive API documentation")
    print("2. Use the Swagger UI to explore all endpoints")
    print("3. Try different API calls and see the responses")
    print("4. Customize the application for your specific needs")

if __name__ == "__main__":
    main()
