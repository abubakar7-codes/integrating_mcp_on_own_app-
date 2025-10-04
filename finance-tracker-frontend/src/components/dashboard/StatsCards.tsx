'use client';

import { TrendingUp, TrendingDown, DollarSign, Target } from 'lucide-react';
import { formatCurrency } from '@/lib/utils';
import Card from '@/components/ui/Card';

interface StatsCardsProps {
  totalIncome: number;
  totalExpenses: number;
  netIncome: number;
  activeGoals: number;
}

export default function StatsCards({ totalIncome, totalExpenses, netIncome, activeGoals }: StatsCardsProps) {
  const stats = [
    {
      name: 'Total Income',
      value: formatCurrency(totalIncome),
      icon: TrendingUp,
      color: 'text-green-600',
      bgColor: 'bg-green-50',
    },
    {
      name: 'Total Expenses',
      value: formatCurrency(totalExpenses),
      icon: TrendingDown,
      color: 'text-red-600',
      bgColor: 'bg-red-50',
    },
    {
      name: 'Net Income',
      value: formatCurrency(netIncome),
      icon: DollarSign,
      color: netIncome >= 0 ? 'text-green-600' : 'text-red-600',
      bgColor: netIncome >= 0 ? 'bg-green-50' : 'bg-red-50',
    },
    {
      name: 'Active Goals',
      value: activeGoals.toString(),
      icon: Target,
      color: 'text-blue-600',
      bgColor: 'bg-blue-50',
    },
  ];

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
      {stats.map((stat) => {
        const Icon = stat.icon;
        return (
          <Card key={stat.name} className="p-6">
            <div className="flex items-center">
              <div className={`p-3 rounded-lg ${stat.bgColor}`}>
                <Icon className={`h-6 w-6 ${stat.color}`} />
              </div>
              <div className="ml-4">
                <p className="text-sm font-medium text-gray-600">{stat.name}</p>
                <p className={`text-2xl font-semibold ${stat.color}`}>{stat.value}</p>
              </div>
            </div>
          </Card>
        );
      })}
    </div>
  );
}
