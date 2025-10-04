'use client';

import { useEffect, useState } from 'react';
import Layout from '@/components/layout/Layout';
import StatsCards from '@/components/dashboard/StatsCards';
import RecentTransactions from '@/components/dashboard/RecentTransactions';
import BudgetOverview from '@/components/dashboard/BudgetOverview';
import Skeleton, { CardSkeleton } from '@/components/ui/Skeleton';
import { transactionsAPI, reportsAPI } from '@/lib/api';
import { Transaction, SpendingReport, BudgetStatus } from '@/types';

export default function DashboardPage() {
  const [transactions, setTransactions] = useState<Transaction[]>([]);
  const [spendingReport, setSpendingReport] = useState<SpendingReport | null>(null);
  const [budgetStatus, setBudgetStatus] = useState<BudgetStatus[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadDashboardData();
  }, []);

  const loadDashboardData = async () => {
    try {
      const [transactionsData, spendingData, budgetData] = await Promise.all([
        transactionsAPI.getAll({ limit: 10 }),
        reportsAPI.getSpending(),
        reportsAPI.getBudgetStatus(),
      ]);

      setTransactions(transactionsData);
      setSpendingReport(spendingData);
      setBudgetStatus(budgetData);
    } catch (error) {
      console.error('Failed to load dashboard data:', error);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <Layout>
        <div className="space-y-6">
          <div>
            <Skeleton className="h-8 w-48 mb-2" />
            <Skeleton className="h-4 w-64" />
          </div>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            {[...Array(4)].map((_, i) => (
              <CardSkeleton key={i} />
            ))}
          </div>
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <CardSkeleton />
            <CardSkeleton />
          </div>
        </div>
      </Layout>
    );
  }

  return (
    <Layout>
      <div className="space-y-6">
        <div>
          <h1 className="text-2xl font-bold text-gray-900">Dashboard</h1>
          <p className="text-gray-600">Overview of your financial activity</p>
        </div>

        {spendingReport && (
          <StatsCards
            totalIncome={spendingReport.total_income}
            totalExpenses={spendingReport.total_expenses}
            netIncome={spendingReport.net_income}
            activeGoals={0} // TODO: Get from goals API
          />
        )}

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          <RecentTransactions transactions={transactions} />
          <BudgetOverview budgets={budgetStatus} />
        </div>
      </div>
    </Layout>
  );
}
