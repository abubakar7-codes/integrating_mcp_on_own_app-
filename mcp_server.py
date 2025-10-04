#!/usr/bin/env python3
"""
Finance Tracker MCP Server
A Model Context Protocol server that provides AI tools for financial data management.
"""

from fastmcp import FastMCP
from sqlalchemy.orm import Session
from sqlalchemy import func, and_
from typing import List, Optional, Dict, Any
from datetime import datetime, date, timedelta
import json

# Import your existing models and database
from app.database import get_db, engine
from app.models import Transaction, Budget, Goal, User, TransactionType, GoalStatus
from app.schemas import TransactionCreate, TransactionResponse

# Initialize FastMCP server
mcp = FastMCP("Finance Tracker MCP Server")

# Database session dependency
def get_database_session():
    """Get database session for MCP tools"""
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()

@mcp.tool
def add_transaction(
    amount: float,
    description: str,
    transaction_type: str,
    category: str,
    user_id: int = 1
) -> Dict[str, Any]:
    """
    Add a new financial transaction (income or expense)
    
    Args:
        amount: Transaction amount (positive for income, negative for expense)
        description: Description of the transaction
        transaction_type: Either 'income' or 'expense'
        category: Transaction category (e.g., 'food', 'salary', 'rent')
        user_id: User ID (defaults to 1 for demo)
    
    Returns:
        Dictionary with transaction details
    """
    db = Session(engine)
    try:
        # Validate transaction type
        if transaction_type not in ["income", "expense"]:
            return {"error": "Transaction type must be 'income' or 'expense'"}
        
        # Create transaction
        transaction = Transaction(
            amount=amount,
            description=description,
            transaction_type=TransactionType(transaction_type),
            category=category,
            user_id=user_id
        )
        
        db.add(transaction)
        db.commit()
        db.refresh(transaction)
        
        return {
            "id": transaction.id,
            "amount": transaction.amount,
            "description": transaction.description,
            "transaction_type": transaction.transaction_type.value,
            "category": transaction.category,
            "date": transaction.date.isoformat(),
            "user_id": transaction.user_id
        }
    except Exception as e:
        db.rollback()
        return {"error": f"Failed to add transaction: {str(e)}"}
    finally:
        db.close()

@mcp.tool
def get_transactions(
    user_id: int = 1,
    limit: int = 50,
    transaction_type: Optional[str] = None,
    category: Optional[str] = None,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None
) -> List[Dict[str, Any]]:
    """
    Retrieve financial transactions with optional filtering
    
    Args:
        user_id: User ID (defaults to 1 for demo)
        limit: Maximum number of transactions to return
        transaction_type: Filter by 'income' or 'expense'
        category: Filter by category
        start_date: Start date filter (YYYY-MM-DD format)
        end_date: End date filter (YYYY-MM-DD format)
    
    Returns:
        List of transaction dictionaries
    """
    db = Session(engine)
    try:
        query = db.query(Transaction).filter(Transaction.user_id == user_id)
        
        if transaction_type:
            query = query.filter(Transaction.transaction_type == transaction_type)
        if category:
            query = query.filter(Transaction.category == category)
        if start_date:
            query = query.filter(Transaction.date >= datetime.fromisoformat(start_date))
        if end_date:
            query = query.filter(Transaction.date <= datetime.fromisoformat(end_date))
        
        transactions = query.order_by(Transaction.date.desc()).limit(limit).all()
        
        return [
            {
                "id": t.id,
                "amount": t.amount,
                "description": t.description,
                "transaction_type": t.transaction_type.value,
                "category": t.category,
                "date": t.date.isoformat(),
                "user_id": t.user_id
            }
            for t in transactions
        ]
    except Exception as e:
        return [{"error": f"Failed to retrieve transactions: {str(e)}"}]
    finally:
        db.close()

@mcp.tool
def get_financial_summary(
    user_id: int = 1,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None
) -> Dict[str, Any]:
    """
    Get a comprehensive financial summary including income, expenses, and net worth
    
    Args:
        user_id: User ID (defaults to 1 for demo)
        start_date: Start date for analysis (YYYY-MM-DD format)
        end_date: End date for analysis (YYYY-MM-DD format)
    
    Returns:
        Dictionary with financial summary
    """
    db = Session(engine)
    try:
        query = db.query(Transaction).filter(Transaction.user_id == user_id)
        
        if start_date:
            query = query.filter(Transaction.date >= datetime.fromisoformat(start_date))
        if end_date:
            query = query.filter(Transaction.date <= datetime.fromisoformat(end_date))
        
        transactions = query.all()
        
        # Calculate totals
        total_income = sum(t.amount for t in transactions if t.transaction_type == TransactionType.INCOME)
        total_expenses = sum(t.amount for t in transactions if t.transaction_type == TransactionType.EXPENSE)
        net_worth = total_income - total_expenses
        
        # Category breakdown
        category_breakdown = {}
        for transaction in transactions:
            if transaction.transaction_type == TransactionType.EXPENSE:
                category = transaction.category
                if category not in category_breakdown:
                    category_breakdown[category] = 0
                category_breakdown[category] += transaction.amount
        
        # Top categories by spending
        top_categories = sorted(category_breakdown.items(), key=lambda x: x[1], reverse=True)[:5]
        
        return {
            "total_income": total_income,
            "total_expenses": total_expenses,
            "net_worth": net_worth,
            "transaction_count": len(transactions),
            "category_breakdown": category_breakdown,
            "top_spending_categories": top_categories,
            "period": f"{start_date or 'all time'} to {end_date or 'now'}"
        }
    except Exception as e:
        return {"error": f"Failed to generate financial summary: {str(e)}"}
    finally:
        db.close()

@mcp.tool
def create_budget(
    name: str,
    category: str,
    amount: float,
    period: str,
    start_date: str,
    end_date: str,
    user_id: int = 1
) -> Dict[str, Any]:
    """
    Create a new budget for a specific category and time period
    
    Args:
        name: Budget name
        category: Category to budget for
        amount: Budget amount
        period: Budget period (monthly, weekly, yearly)
        start_date: Budget start date (YYYY-MM-DD format)
        end_date: Budget end date (YYYY-MM-DD format)
        user_id: User ID (defaults to 1 for demo)
    
    Returns:
        Dictionary with budget details
    """
    db = Session(engine)
    try:
        budget = Budget(
            name=name,
            category=category,
            amount=amount,
            period=period,
            start_date=datetime.fromisoformat(start_date),
            end_date=datetime.fromisoformat(end_date),
            user_id=user_id
        )
        
        db.add(budget)
        db.commit()
        db.refresh(budget)
        
        return {
            "id": budget.id,
            "name": budget.name,
            "category": budget.category,
            "amount": budget.amount,
            "period": budget.period,
            "start_date": budget.start_date.isoformat(),
            "end_date": budget.end_date.isoformat(),
            "user_id": budget.user_id
        }
    except Exception as e:
        db.rollback()
        return {"error": f"Failed to create budget: {str(e)}"}
    finally:
        db.close()

@mcp.tool
def get_budget_status(user_id: int = 1) -> List[Dict[str, Any]]:
    """
    Get current status of all budgets including spending vs. budget amounts
    
    Args:
        user_id: User ID (defaults to 1 for demo)
    
    Returns:
        List of budget status dictionaries
    """
    db = Session(engine)
    try:
        budgets = db.query(Budget).filter(Budget.user_id == user_id).all()
        budget_statuses = []
        
        for budget in budgets:
            # Calculate spent amount for this budget
            spent = db.query(func.sum(Transaction.amount)).filter(
                and_(
                    Transaction.user_id == user_id,
                    Transaction.transaction_type == TransactionType.EXPENSE,
                    Transaction.category == budget.category,
                    Transaction.date >= budget.start_date,
                    Transaction.date <= budget.end_date
                )
            ).scalar() or 0
            
            remaining = budget.amount - spent
            percentage_used = (spent / budget.amount) * 100 if budget.amount > 0 else 0
            
            if percentage_used > 100:
                status = "over_budget"
            elif percentage_used > 80:
                status = "on_track"
            else:
                status = "under_budget"
            
            budget_statuses.append({
                "budget_id": budget.id,
                "budget_name": budget.name,
                "category": budget.category,
                "budget_amount": budget.amount,
                "spent_amount": spent,
                "remaining_amount": remaining,
                "percentage_used": round(percentage_used, 2),
                "status": status
            })
        
        return budget_statuses
    except Exception as e:
        return [{"error": f"Failed to get budget status: {str(e)}"}]
    finally:
        db.close()

@mcp.tool
def create_financial_goal(
    title: str,
    description: str,
    target_amount: float,
    target_date: str,
    user_id: int = 1
) -> Dict[str, Any]:
    """
    Create a new financial goal
    
    Args:
        title: Goal title
        description: Goal description
        target_amount: Target amount to save
        target_date: Target completion date (YYYY-MM-DD format)
        user_id: User ID (defaults to 1 for demo)
    
    Returns:
        Dictionary with goal details
    """
    db = Session(engine)
    try:
        goal = Goal(
            title=title,
            description=description,
            target_amount=target_amount,
            target_date=datetime.fromisoformat(target_date),
            user_id=user_id
        )
        
        db.add(goal)
        db.commit()
        db.refresh(goal)
        
        return {
            "id": goal.id,
            "title": goal.title,
            "description": goal.description,
            "target_amount": goal.target_amount,
            "current_amount": goal.current_amount,
            "target_date": goal.target_date.isoformat(),
            "status": goal.status.value,
            "user_id": goal.user_id
        }
    except Exception as e:
        db.rollback()
        return {"error": f"Failed to create financial goal: {str(e)}"}
    finally:
        db.close()

@mcp.tool
def get_financial_goals(user_id: int = 1) -> List[Dict[str, Any]]:
    """
    Get all financial goals for a user
    
    Args:
        user_id: User ID (defaults to 1 for demo)
    
    Returns:
        List of goal dictionaries
    """
    db = Session(engine)
    try:
        goals = db.query(Goal).filter(Goal.user_id == user_id).all()
        
        return [
            {
                "id": goal.id,
                "title": goal.title,
                "description": goal.description,
                "target_amount": goal.target_amount,
                "current_amount": goal.current_amount,
                "target_date": goal.target_date.isoformat(),
                "status": goal.status.value,
                "progress_percentage": round((goal.current_amount / goal.target_amount) * 100, 2) if goal.target_amount > 0 else 0,
                "user_id": goal.user_id
            }
            for goal in goals
        ]
    except Exception as e:
        return [{"error": f"Failed to get financial goals: {str(e)}"}]
    finally:
        db.close()

@mcp.tool
def analyze_spending_patterns(
    user_id: int = 1,
    days: int = 30
) -> Dict[str, Any]:
    """
    Analyze spending patterns over a specified period
    
    Args:
        user_id: User ID (defaults to 1 for demo)
        days: Number of days to analyze (defaults to 30)
    
    Returns:
        Dictionary with spending pattern analysis
    """
    db = Session(engine)
    try:
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)
        
        transactions = db.query(Transaction).filter(
            and_(
                Transaction.user_id == user_id,
                Transaction.transaction_type == TransactionType.EXPENSE,
                Transaction.date >= start_date,
                Transaction.date <= end_date
            )
        ).all()
        
        if not transactions:
            return {"message": "No transactions found for analysis"}
        
        # Daily spending analysis
        daily_spending = {}
        for transaction in transactions:
            day = transaction.date.date()
            if day not in daily_spending:
                daily_spending[day] = 0
            daily_spending[day] += transaction.amount
        
        # Category analysis
        category_totals = {}
        for transaction in transactions:
            category = transaction.category
            if category not in category_totals:
                category_totals[category] = 0
            category_totals[category] += transaction.amount
        
        # Calculate statistics
        total_spent = sum(transaction.amount for transaction in transactions)
        avg_daily_spending = total_spent / days
        max_daily_spending = max(daily_spending.values()) if daily_spending else 0
        min_daily_spending = min(daily_spending.values()) if daily_spending else 0
        
        return {
            "analysis_period_days": days,
            "total_spent": total_spent,
            "average_daily_spending": round(avg_daily_spending, 2),
            "max_daily_spending": max_daily_spending,
            "min_daily_spending": min_daily_spending,
            "category_breakdown": category_totals,
            "top_spending_category": max(category_totals.items(), key=lambda x: x[1]) if category_totals else None,
            "transaction_count": len(transactions)
        }
    except Exception as e:
        return {"error": f"Failed to analyze spending patterns: {str(e)}"}
    finally:
        db.close()

if __name__ == "__main__":
    print("Starting Finance Tracker MCP Server...")
    print("Available tools:")
    print("- add_transaction: Add income or expense")
    print("- get_transactions: Retrieve transactions with filters")
    print("- get_financial_summary: Get comprehensive financial overview")
    print("- create_budget: Create spending budgets")
    print("- get_budget_status: Check budget performance")
    print("- create_financial_goal: Set financial goals")
    print("- get_financial_goals: View all goals")
    print("- analyze_spending_patterns: Analyze spending behavior")
    print("\nServer is ready to accept connections!")
    
    mcp.run()
