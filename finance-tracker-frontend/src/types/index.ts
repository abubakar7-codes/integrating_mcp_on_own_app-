// No user authentication required

export interface Transaction {
  id: number;
  amount: number;
  description: string;
  transaction_type: 'income' | 'expense';
  category: string;
  date: string;
  user_id: number;
}

export interface Budget {
  id: number;
  name: string;
  category: string;
  amount: number;
  period: string;
  start_date: string;
  end_date: string;
  user_id: number;
  created_at: string;
}

export interface Goal {
  id: number;
  title: string;
  description?: string;
  target_amount: number;
  current_amount: number;
  target_date: string;
  status: 'active' | 'completed' | 'paused';
  user_id: number;
  created_at: string;
}

export interface SpendingReport {
  total_income: number;
  total_expenses: number;
  net_income: number;
  category_breakdown: Record<string, number>;
  period: string;
}

export interface BudgetStatus {
  budget_id: number;
  budget_name: string;
  budget_amount: number;
  spent_amount: number;
  remaining_amount: number;
  percentage_used: number;
  status: 'on_track' | 'over_budget' | 'under_budget';
}

// No authentication forms needed

export interface TransactionForm {
  amount: number;
  description: string;
  transaction_type: 'income' | 'expense';
  category: string;
  date?: string;
}

export interface BudgetForm {
  name: string;
  category: string;
  amount: number;
  period: string;
  start_date: string;
  end_date: string;
}

export interface GoalForm {
  title: string;
  description?: string;
  target_amount: number;
  current_amount?: number;
  target_date: string;
}
