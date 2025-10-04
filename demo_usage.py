#!/usr/bin/env python3
"""
Demo script showing how to use the Personal Finance Tracker API
This script provides examples of all API calls you can make.
"""

print("🚀 Personal Finance Tracker API - Usage Demo")
print("=" * 60)

print("""
📖 STEP-BY-STEP API USAGE GUIDE

1. 🚀 START THE SERVER
   Run this command in your terminal:
   python run_server.py
   
   Or alternatively:
   uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload

2. 📚 ACCESS THE INTERACTIVE DOCS
   Open your browser and go to:
   http://127.0.0.1:8000/docs
   
   This will show you the Swagger UI with all available endpoints!

3. 🔐 REGISTER A NEW USER
   POST /api/v1/auth/register
   {
     "email": "john.doe@example.com",
     "username": "johndoe", 
     "password": "securepassword123",
     "full_name": "John Doe"
   }

4. 🔑 LOGIN AND GET TOKEN
   POST /api/v1/auth/login
   Form data:
   username: johndoe
   password: securepassword123
   
   This returns an access token you'll need for other requests.

5. 💰 ADD TRANSACTIONS
   POST /api/v1/transactions/
   Headers: Authorization: Bearer YOUR_TOKEN
   {
     "amount": 5000.00,
     "description": "Monthly Salary",
     "transaction_type": "income",
     "category": "Salary"
   }
   
   Example expenses:
   {
     "amount": 300.00,
     "description": "Grocery Shopping", 
     "transaction_type": "expense",
     "category": "Food"
   }

6. 📊 CREATE BUDGETS
   POST /api/v1/budgets/
   Headers: Authorization: Bearer YOUR_TOKEN
   {
     "name": "Monthly Food Budget",
     "category": "Food",
     "amount": 500.00,
     "period": "monthly",
     "start_date": "2024-01-01T00:00:00",
     "end_date": "2024-01-31T23:59:59"
   }

7. 🎯 SET FINANCIAL GOALS
   POST /api/v1/goals/
   Headers: Authorization: Bearer YOUR_TOKEN
   {
     "title": "Emergency Fund",
     "description": "Build a 6-month emergency fund",
     "target_amount": 15000.00,
     "current_amount": 2000.00,
     "target_date": "2024-12-31T00:00:00"
   }

8. 📈 GENERATE REPORTS
   GET /api/v1/reports/spending
   Headers: Authorization: Bearer YOUR_TOKEN
   
   GET /api/v1/reports/budget-status
   Headers: Authorization: Bearer YOUR_TOKEN
   
   GET /api/v1/reports/export/csv
   Headers: Authorization: Bearer YOUR_TOKEN

9. 📊 GET ALL YOUR DATA
   GET /api/v1/transactions/ - Get all transactions
   GET /api/v1/budgets/ - Get all budgets  
   GET /api/v1/goals/ - Get all goals

10. 🔧 UPDATE AND DELETE
    PUT /api/v1/transactions/{id} - Update transaction
    DELETE /api/v1/transactions/{id} - Delete transaction
    PUT /api/v1/budgets/{id} - Update budget
    DELETE /api/v1/budgets/{id} - Delete budget
    PUT /api/v1/goals/{id} - Update goal
    DELETE /api/v1/goals/{id} - Delete goal

""")

print("🎯 SAMPLE CURL COMMANDS")
print("-" * 30)

print("""
# 1. Register a user
curl -X POST "http://127.0.0.1:8000/api/v1/auth/register" \\
     -H "Content-Type: application/json" \\
     -d '{
       "email": "john.doe@example.com",
       "username": "johndoe",
       "password": "securepassword123",
       "full_name": "John Doe"
     }'

# 2. Login
curl -X POST "http://127.0.0.1:8000/api/v1/auth/login" \\
     -H "Content-Type: application/x-www-form-urlencoded" \\
     -d "username=johndoe&password=securepassword123"

# 3. Add a transaction (replace YOUR_TOKEN with actual token)
curl -X POST "http://127.0.0.1:8000/api/v1/transactions/" \\
     -H "Authorization: Bearer YOUR_TOKEN" \\
     -H "Content-Type: application/json" \\
     -d '{
       "amount": 5000.00,
       "description": "Monthly Salary",
       "transaction_type": "income",
       "category": "Salary"
     }'

# 4. Get spending report
curl -X GET "http://127.0.0.1:8000/api/v1/reports/spending" \\
     -H "Authorization: Bearer YOUR_TOKEN"
""")

print("🌐 WEB INTERFACE")
print("-" * 20)
print("""
The easiest way to test the API is through the web interface:

1. Start the server: python run_server.py
2. Open browser: http://127.0.0.1:8000/docs
3. Click "Try it out" on any endpoint
4. Fill in the required fields
5. Click "Execute" to see the response

The Swagger UI will show you:
- All available endpoints
- Required parameters
- Example requests and responses
- Interactive testing interface
""")

print("🎉 FEATURES DEMONSTRATED")
print("-" * 30)
print("""
✅ User Authentication (JWT tokens)
✅ Transaction Management (CRUD operations)
✅ Budget Tracking and Monitoring
✅ Financial Goal Setting and Progress Tracking
✅ Spending Reports and Analytics
✅ Budget Status Reports
✅ CSV Export Functionality
✅ Data Visualization (Charts)
✅ Category-based Organization
✅ Date Range Filtering
✅ Secure API with Authentication
""")

print("🚀 NEXT STEPS")
print("-" * 15)
print("""
1. Start the server: python run_server.py
2. Open http://127.0.0.1:8000/docs in your browser
3. Register a user account
4. Login to get your access token
5. Start adding your real financial data
6. Set up budgets for different categories
7. Create financial goals
8. Generate reports to analyze your spending
9. Export data to CSV for external analysis
10. Customize the application for your needs!

The API is fully functional and ready to use! 🎊
""")
