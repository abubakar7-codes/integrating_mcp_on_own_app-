#!/usr/bin/env python3
"""
Create dummy data for Finance Tracker with LiteSQL
"""

import sys
from pathlib import Path
from datetime import datetime, timedelta
import random
from decimal import Decimal

# Add the project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from app.database import engine, SessionLocal, Base
from app.models import User, Transaction, Budget, Goal, TransactionType, GoalStatus
from sqlalchemy.orm import Session

def create_dummy_users(db: Session):
    """Create dummy users"""
    print("👤 Creating dummy users...")
    
    users_data = [
        {
            "email": "john.doe@example.com",
            "username": "johndoe",
            "hashed_password": "$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBPj4J/8KzK1K2",  # "password123"
            "full_name": "John Doe",
            "is_active": True
        },
        {
            "email": "jane.smith@example.com", 
            "username": "janesmith",
            "hashed_password": "$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBPj4J/8KzK1K2",  # "password123"
            "full_name": "Jane Smith",
            "is_active": True
        },
        {
            "email": "mike.wilson@example.com",
            "username": "mikewilson", 
            "hashed_password": "$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBPj4J/8KzK1K2",  # "password123"
            "full_name": "Mike Wilson",
            "is_active": True
        }
    ]
    
    users = []
    for user_data in users_data:
        user = User(**user_data)
        db.add(user)
        users.append(user)
    
    db.commit()
    print(f"✅ Created {len(users)} users")
    return users

def create_dummy_transactions(db: Session, users):
    """Create dummy transactions"""
    print("💰 Creating dummy transactions...")
    
    # Income categories
    income_categories = ["salary", "freelance", "investment", "bonus", "rental_income"]
    
    # Expense categories  
    expense_categories = ["food", "transportation", "entertainment", "utilities", "healthcare", 
                         "shopping", "education", "travel", "insurance", "subscriptions"]
    
    transactions = []
    
    for user in users:
        # Create income transactions
        for _ in range(random.randint(8, 15)):
            transaction = Transaction(
                amount=round(random.uniform(500, 5000), 2),
                description=random.choice([
                    "Monthly salary", "Freelance project", "Investment dividend", 
                    "Year-end bonus", "Rental property income", "Consulting work"
                ]),
                transaction_type=TransactionType.INCOME,
                category=random.choice(income_categories),
                date=datetime.now() - timedelta(days=random.randint(1, 90)),
                user_id=user.id
            )
            db.add(transaction)
            transactions.append(transaction)
        
        # Create expense transactions
        for _ in range(random.randint(20, 50)):
            transaction = Transaction(
                amount=round(random.uniform(5, 500), 2),
                description=random.choice([
                    "Grocery shopping", "Gas station", "Restaurant dinner", "Movie tickets",
                    "Electric bill", "Phone bill", "Gym membership", "Coffee shop",
                    "Online shopping", "Doctor visit", "Car maintenance", "Netflix subscription"
                ]),
                transaction_type=TransactionType.EXPENSE,
                category=random.choice(expense_categories),
                date=datetime.now() - timedelta(days=random.randint(1, 90)),
                user_id=user.id
            )
            db.add(transaction)
            transactions.append(transaction)
    
    db.commit()
    print(f"✅ Created {len(transactions)} transactions")
    return transactions

def create_dummy_budgets(db: Session, users):
    """Create dummy budgets"""
    print("📊 Creating dummy budgets...")
    
    budget_templates = [
        {"name": "Monthly Food Budget", "category": "food", "amount": 400.0, "period": "monthly"},
        {"name": "Transportation Budget", "category": "transportation", "amount": 200.0, "period": "monthly"},
        {"name": "Entertainment Budget", "category": "entertainment", "amount": 150.0, "period": "monthly"},
        {"name": "Utilities Budget", "category": "utilities", "amount": 300.0, "period": "monthly"},
        {"name": "Shopping Budget", "category": "shopping", "amount": 250.0, "period": "monthly"},
        {"name": "Healthcare Budget", "category": "healthcare", "amount": 100.0, "period": "monthly"},
    ]
    
    budgets = []
    for user in users:
        for template in budget_templates:
            start_date = datetime.now().replace(day=1)
            end_date = (start_date + timedelta(days=30)).replace(day=1) - timedelta(days=1)
            
            budget = Budget(
                name=template["name"],
                category=template["category"],
                amount=template["amount"],
                period=template["period"],
                start_date=start_date,
                end_date=end_date,
                user_id=user.id
            )
            db.add(budget)
            budgets.append(budget)
    
    db.commit()
    print(f"✅ Created {len(budgets)} budgets")
    return budgets

def create_dummy_goals(db: Session, users):
    """Create dummy financial goals"""
    print("🎯 Creating dummy financial goals...")
    
    goal_templates = [
        {
            "title": "Emergency Fund",
            "description": "Build emergency fund for 6 months of expenses",
            "target_amount": 10000.0,
            "current_amount": random.uniform(2000, 8000)
        },
        {
            "title": "Vacation Fund", 
            "description": "Save for dream vacation to Europe",
            "target_amount": 5000.0,
            "current_amount": random.uniform(500, 3000)
        },
        {
            "title": "New Car Fund",
            "description": "Save for down payment on new car",
            "target_amount": 15000.0,
            "current_amount": random.uniform(2000, 10000)
        },
        {
            "title": "Home Renovation",
            "description": "Kitchen and bathroom renovation project",
            "target_amount": 25000.0,
            "current_amount": random.uniform(5000, 15000)
        },
        {
            "title": "Retirement Boost",
            "description": "Additional retirement savings",
            "target_amount": 50000.0,
            "current_amount": random.uniform(10000, 30000)
        }
    ]
    
    goals = []
    for user in users:
        for template in goal_templates:
            # Random target date between 6 months and 2 years from now
            target_date = datetime.now() + timedelta(days=random.randint(180, 730))
            
            goal = Goal(
                title=template["title"],
                description=template["description"],
                target_amount=template["target_amount"],
                current_amount=template["current_amount"],
                target_date=target_date,
                status=random.choice([GoalStatus.ACTIVE, GoalStatus.ACTIVE, GoalStatus.ACTIVE, GoalStatus.PAUSED]),
                user_id=user.id
            )
            db.add(goal)
            goals.append(goal)
    
    db.commit()
    print(f"✅ Created {len(goals)} financial goals")
    return goals

def create_database_and_dummy_data():
    """Main function to create database and dummy data"""
    print("🚀 Finance Tracker LiteSQL Database Setup")
    print("=" * 60)
    
    # Create all tables
    print("📋 Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("✅ Database tables created")
    
    # Create database session
    db = SessionLocal()
    
    try:
        # Create dummy data
        users = create_dummy_users(db)
        transactions = create_dummy_transactions(db, users)
        budgets = create_dummy_budgets(db, users)
        goals = create_dummy_goals(db, users)
        
        print("\n🎉 Dummy Data Creation Complete!")
        print("=" * 60)
        print(f"👤 Users: {len(users)}")
        print(f"💰 Transactions: {len(transactions)}")
        print(f"📊 Budgets: {len(budgets)}")
        print(f"🎯 Goals: {len(goals)}")
        print("\nDatabase file: finance_tracker_litequery.db")
        print("Ready to use with your Finance Tracker application!")
        
    except Exception as e:
        print(f"❌ Error creating dummy data: {e}")
        db.rollback()
        raise
    finally:
        db.close()

if __name__ == "__main__":
    create_database_and_dummy_data()
