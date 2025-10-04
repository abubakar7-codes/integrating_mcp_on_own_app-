"""
LiteQuery Helper Module
Provides enhanced database operations using litequery for better performance
"""

import asyncio
import aiosqlite
from typing import List, Dict, Any, Optional
from datetime import datetime, date
import json

class LiteQueryHelper:
    """Helper class for enhanced database operations with litequery"""
    
    def __init__(self, db_path: str = "./finance_tracker_litequery.db"):
        self.db_path = db_path
    
    async def get_connection(self):
        """Get async database connection"""
        return await aiosqlite.connect(self.db_path)
    
    async def execute_query(self, query: str, params: tuple = ()) -> List[Dict[str, Any]]:
        """Execute a SELECT query and return results as list of dictionaries"""
        async with self.get_connection() as db:
            db.row_factory = aiosqlite.Row
            cursor = await db.execute(query, params)
            rows = await cursor.fetchall()
            return [dict(row) for row in rows]
    
    async def execute_insert(self, query: str, params: tuple = ()) -> int:
        """Execute an INSERT query and return the last row ID"""
        async with self.get_connection() as db:
            cursor = await db.execute(query, params)
            await db.commit()
            return cursor.lastrowid
    
    async def execute_update(self, query: str, params: tuple = ()) -> int:
        """Execute an UPDATE query and return the number of affected rows"""
        async with self.get_connection() as db:
            cursor = await db.execute(query, params)
            await db.commit()
            return cursor.rowcount
    
    async def execute_delete(self, query: str, params: tuple = ()) -> int:
        """Execute a DELETE query and return the number of affected rows"""
        async with self.get_connection() as db:
            cursor = await db.execute(query, params)
            await db.commit()
            return cursor.rowcount
    
    # Financial Analytics Methods
    async def get_user_financial_summary(self, user_id: int, start_date: Optional[str] = None, end_date: Optional[str] = None) -> Dict[str, Any]:
        """Get comprehensive financial summary for a user"""
        date_filter = ""
        params = [user_id]
        
        if start_date:
            date_filter += " AND date >= ?"
            params.append(start_date)
        if end_date:
            date_filter += " AND date <= ?"
            params.append(end_date)
        
        query = f"""
        SELECT 
            SUM(CASE WHEN transaction_type = 'income' THEN amount ELSE 0 END) as total_income,
            SUM(CASE WHEN transaction_type = 'expense' THEN amount ELSE 0 END) as total_expenses,
            COUNT(*) as transaction_count
        FROM transactions 
        WHERE user_id = ? {date_filter}
        """
        
        result = await self.execute_query(query, tuple(params))
        if result:
            data = result[0]
            total_income = data['total_income'] or 0
            total_expenses = data['total_expenses'] or 0
            return {
                'total_income': total_income,
                'total_expenses': total_expenses,
                'net_worth': total_income - total_expenses,
                'transaction_count': data['transaction_count'],
                'period': f"{start_date or 'all time'} to {end_date or 'now'}"
            }
        return {'total_income': 0, 'total_expenses': 0, 'net_worth': 0, 'transaction_count': 0}
    
    async def get_spending_by_category(self, user_id: int, start_date: Optional[str] = None, end_date: Optional[str] = None) -> List[Dict[str, Any]]:
        """Get spending breakdown by category"""
        date_filter = ""
        params = [user_id]
        
        if start_date:
            date_filter += " AND date >= ?"
            params.append(start_date)
        if end_date:
            date_filter += " AND date <= ?"
            params.append(end_date)
        
        query = f"""
        SELECT 
            category,
            SUM(amount) as total_spent,
            COUNT(*) as transaction_count
        FROM transactions 
        WHERE user_id = ? AND transaction_type = 'expense' {date_filter}
        GROUP BY category
        ORDER BY total_spent DESC
        """
        
        return await self.execute_query(query, tuple(params))
    
    async def get_monthly_trends(self, user_id: int, months: int = 12) -> List[Dict[str, Any]]:
        """Get monthly income and expense trends"""
        query = """
        SELECT 
            strftime('%Y-%m', date) as month,
            SUM(CASE WHEN transaction_type = 'income' THEN amount ELSE 0 END) as income,
            SUM(CASE WHEN transaction_type = 'expense' THEN amount ELSE 0 END) as expenses
        FROM transactions 
        WHERE user_id = ? 
        AND date >= date('now', '-{} months')
        GROUP BY strftime('%Y-%m', date)
        ORDER BY month
        """.format(months)
        
        return await self.execute_query(query, (user_id,))
    
    async def get_budget_performance(self, user_id: int) -> List[Dict[str, Any]]:
        """Get budget performance analysis"""
        query = """
        SELECT 
            b.id as budget_id,
            b.name as budget_name,
            b.category,
            b.amount as budget_amount,
            COALESCE(SUM(t.amount), 0) as spent_amount,
            b.amount - COALESCE(SUM(t.amount), 0) as remaining_amount,
            CASE 
                WHEN COALESCE(SUM(t.amount), 0) > b.amount THEN 'over_budget'
                WHEN COALESCE(SUM(t.amount), 0) > b.amount * 0.8 THEN 'on_track'
                ELSE 'under_budget'
            END as status
        FROM budgets b
        LEFT JOIN transactions t ON b.category = t.category 
            AND t.transaction_type = 'expense'
            AND t.date >= b.start_date 
            AND t.date <= b.end_date
            AND t.user_id = b.user_id
        WHERE b.user_id = ?
        GROUP BY b.id, b.name, b.category, b.amount
        """
        
        return await self.execute_query(query, (user_id,))
    
    async def get_goal_progress(self, user_id: int) -> List[Dict[str, Any]]:
        """Get financial goal progress"""
        query = """
        SELECT 
            id,
            title,
            description,
            target_amount,
            current_amount,
            target_date,
            status,
            ROUND((current_amount / target_amount) * 100, 2) as progress_percentage
        FROM goals
        WHERE user_id = ?
        ORDER BY target_date
        """
        
        return await self.execute_query(query, (user_id,))
    
    async def get_recent_transactions(self, user_id: int, limit: int = 10) -> List[Dict[str, Any]]:
        """Get recent transactions for a user"""
        query = """
        SELECT 
            id,
            amount,
            description,
            transaction_type,
            category,
            date
        FROM transactions
        WHERE user_id = ?
        ORDER BY date DESC
        LIMIT ?
        """
        
        return await self.execute_query(query, (user_id, limit))

# Global instance for easy access
litequery_helper = LiteQueryHelper()
