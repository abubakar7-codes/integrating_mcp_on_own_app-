from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import func, and_
from typing import List, Optional
from datetime import datetime, date, timedelta
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64

from app.database import get_db
from app.models import Transaction, Budget, User
from app.schemas import SpendingReport, BudgetStatus

router = APIRouter()

@router.get("/spending", response_model=SpendingReport)
async def get_spending_report(
    start_date: Optional[date] = None,
    end_date: Optional[date] = None,
    db: Session = Depends(get_db)
):
    # Default to current month if no dates provided
    if not start_date:
        start_date = date.today().replace(day=1)
    if not end_date:
        end_date = date.today()
    
    # Get transactions in date range
    transactions = db.query(Transaction).filter(
        and_(
            Transaction.user_id == 1,  # Default user
            Transaction.date >= start_date,
            Transaction.date <= end_date
        )
    ).all()
    
    # Calculate totals
    total_income = sum(t.amount for t in transactions if t.transaction_type == "income")
    total_expenses = sum(t.amount for t in transactions if t.transaction_type == "expense")
    net_income = total_income - total_expenses
    
    # Category breakdown
    category_breakdown = {}
    for transaction in transactions:
        if transaction.transaction_type == "expense":
            category = transaction.category
            if category not in category_breakdown:
                category_breakdown[category] = 0
            category_breakdown[category] += transaction.amount
    
    return SpendingReport(
        total_income=total_income,
        total_expenses=total_expenses,
        net_income=net_income,
        category_breakdown=category_breakdown,
        period=f"{start_date} to {end_date}"
    )

@router.get("/budget-status", response_model=List[BudgetStatus])
async def get_budget_status(
    db: Session = Depends(get_db)
):
    budgets = db.query(Budget).filter(Budget.user_id == 1).all()  # Default user
    budget_statuses = []
    
    for budget in budgets:
        # Calculate spent amount for this budget
        spent = db.query(func.sum(Transaction.amount)).filter(
            and_(
                Transaction.user_id == 1,  # Default user
                Transaction.transaction_type == "expense",
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
        
        budget_statuses.append(BudgetStatus(
            budget_id=budget.id,
            budget_name=budget.name,
            budget_amount=budget.amount,
            spent_amount=spent,
            remaining_amount=remaining,
            percentage_used=percentage_used,
            status=status
        ))
    
    return budget_statuses

@router.get("/export/csv")
async def export_transactions_csv(
    start_date: Optional[date] = None,
    end_date: Optional[date] = None,
    db: Session = Depends(get_db)
):
    if not start_date:
        start_date = date.today().replace(day=1)
    if not end_date:
        end_date = date.today()
    
    transactions = db.query(Transaction).filter(
        and_(
            Transaction.user_id == 1,  # Default user
            Transaction.date >= start_date,
            Transaction.date <= end_date
        )
    ).all()
    
    # Create CSV content
    csv_content = "Date,Type,Category,Description,Amount\n"
    for transaction in transactions:
        csv_content += f"{transaction.date},{transaction.transaction_type},{transaction.category},{transaction.description},{transaction.amount}\n"
    
    return {"csv_content": csv_content}
