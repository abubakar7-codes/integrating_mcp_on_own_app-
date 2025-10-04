#!/usr/bin/env python3
"""
Test the Personal Finance Tracker API without authentication
"""

import requests
import json
from datetime import datetime

API_BASE = "http://127.0.0.1:8000"

def test_api():
    print("🧪 Testing Personal Finance Tracker API (No Auth)")
    print("=" * 50)
    
    # Test health endpoint
    try:
        response = requests.get(f"{API_BASE}/health")
        print(f"✅ Health check: {response.status_code}")
        print(f"   Response: {response.json()}")
    except Exception as e:
        print(f"❌ Health check failed: {e}")
        return
    
    # Test root endpoint
    try:
        response = requests.get(f"{API_BASE}/")
        print(f"✅ Root endpoint: {response.status_code}")
        print(f"   Response: {response.json()}")
    except Exception as e:
        print(f"❌ Root endpoint failed: {e}")
    
    # Test transactions endpoint
    try:
        response = requests.get(f"{API_BASE}/api/v1/transactions/")
        print(f"✅ Get transactions: {response.status_code}")
        if response.status_code == 200:
            transactions = response.json()
            print(f"   Found {len(transactions)} transactions")
        else:
            print(f"   Error: {response.text}")
    except Exception as e:
        print(f"❌ Get transactions failed: {e}")
    
    # Test creating a transaction
    try:
        transaction_data = {
            "amount": 100.50,
            "description": "Test transaction",
            "transaction_type": "expense",
            "category": "Food",
            "date": datetime.now().isoformat()
        }
        response = requests.post(f"{API_BASE}/api/v1/transactions/", json=transaction_data)
        print(f"✅ Create transaction: {response.status_code}")
        if response.status_code == 200:
            transaction = response.json()
            print(f"   Created transaction ID: {transaction['id']}")
        else:
            print(f"   Error: {response.text}")
    except Exception as e:
        print(f"❌ Create transaction failed: {e}")
    
    # Test reports endpoint
    try:
        response = requests.get(f"{API_BASE}/api/v1/reports/spending")
        print(f"✅ Get spending report: {response.status_code}")
        if response.status_code == 200:
            report = response.json()
            print(f"   Total income: ${report['total_income']}")
            print(f"   Total expenses: ${report['total_expenses']}")
        else:
            print(f"   Error: {response.text}")
    except Exception as e:
        print(f"❌ Get spending report failed: {e}")
    
    print("\n🎉 API testing completed!")
    print("🌐 Frontend should be available at: http://localhost:3000")
    print("📚 API docs available at: http://127.0.0.1:8000/docs")

if __name__ == "__main__":
    test_api()
