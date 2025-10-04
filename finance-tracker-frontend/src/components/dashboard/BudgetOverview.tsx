'use client';

import { BudgetStatus } from '@/types';
import { formatCurrency, getBudgetStatusColor } from '@/lib/utils';
import Card from '@/components/ui/Card';

interface BudgetOverviewProps {
  budgets: BudgetStatus[];
}

export default function BudgetOverview({ budgets }: BudgetOverviewProps) {
  return (
    <Card title="Budget Overview" className="h-full">
      <div className="space-y-4">
        {budgets.length === 0 ? (
          <div className="text-center py-8">
            <p className="text-gray-500">No budgets set</p>
            <p className="text-sm text-gray-400 mt-1">Create your first budget to track spending</p>
          </div>
        ) : (
          budgets.map((budget) => (
            <div key={budget.budget_id} className="space-y-2">
              <div className="flex items-center justify-between">
                <h4 className="font-medium text-gray-900">{budget.budget_name}</h4>
                <span className={`px-2 py-1 rounded-full text-xs font-medium ${
                  getBudgetStatusColor(budget.status)
                }`}>
                  {budget.status.replace('_', ' ')}
                </span>
              </div>
              <div className="space-y-1">
                <div className="flex justify-between text-sm text-gray-600">
                  <span>Spent: {formatCurrency(budget.spent_amount)}</span>
                  <span>Budget: {formatCurrency(budget.budget_amount)}</span>
                </div>
                <div className="w-full bg-gray-200 rounded-full h-2">
                  <div
                    className={`h-2 rounded-full ${
                      budget.percentage_used > 100 
                        ? 'bg-red-500' 
                        : budget.percentage_used > 80 
                        ? 'bg-yellow-500' 
                        : 'bg-green-500'
                    }`}
                    style={{ width: `${Math.min(budget.percentage_used, 100)}%` }}
                  />
                </div>
                <div className="flex justify-between text-xs text-gray-500">
                  <span>{budget.percentage_used.toFixed(1)}% used</span>
                  <span>Remaining: {formatCurrency(budget.remaining_amount)}</span>
                </div>
              </div>
            </div>
          ))
        )}
      </div>
    </Card>
  );
}
