from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from app.models import TransactionType, GoalStatus

# Transaction schemas
class TransactionBase(BaseModel):
    amount: float
    description: str
    transaction_type: TransactionType
    category: str
    date: Optional[datetime] = None

class TransactionCreate(TransactionBase):
    pass

class TransactionResponse(TransactionBase):
    id: int
    user_id: int
    date: datetime
    
    class Config:
        from_attributes = True

# Budget schemas
class BudgetBase(BaseModel):
    name: str
    category: str
    amount: float
    period: str
    start_date: datetime
    end_date: datetime

class BudgetCreate(BudgetBase):
    pass

class BudgetResponse(BudgetBase):
    id: int
    user_id: int
    created_at: datetime
    
    class Config:
        from_attributes = True

# Goal schemas
class GoalBase(BaseModel):
    title: str
    description: Optional[str] = None
    target_amount: float
    current_amount: float = 0.0
    target_date: datetime

class GoalCreate(GoalBase):
    pass

class GoalUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    target_amount: Optional[float] = None
    current_amount: Optional[float] = None
    target_date: Optional[datetime] = None
    status: Optional[GoalStatus] = None

class GoalResponse(GoalBase):
    id: int
    user_id: int
    status: GoalStatus
    created_at: datetime
    
    class Config:
        from_attributes = True

# No authentication schemas needed

# Report schemas
class SpendingReport(BaseModel):
    total_income: float
    total_expenses: float
    net_income: float
    category_breakdown: dict
    period: str

class BudgetStatus(BaseModel):
    budget_id: int
    budget_name: str
    budget_amount: float
    spent_amount: float
    remaining_amount: float
    percentage_used: float
    status: str  # "on_track", "over_budget", "under_budget"
