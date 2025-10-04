# Personal Finance Tracker - Frontend

A modern Next.js frontend for the Personal Finance Tracker API.

## Features

- **Modern UI**: Built with Next.js 14, TypeScript, and Tailwind CSS
- **Authentication**: Secure login and registration
- **Dashboard**: Overview of financial data with charts and statistics
- **Transaction Management**: Add, edit, and delete income/expenses
- **Budget Tracking**: Monitor spending against budgets
- **Financial Goals**: Set and track progress towards goals
- **Reports**: Generate spending reports and analytics
- **Responsive Design**: Works on desktop, tablet, and mobile

## Tech Stack

- **Next.js 14** - React framework with App Router
- **TypeScript** - Type safety and better development experience
- **Tailwind CSS** - Utility-first CSS framework
- **Axios** - HTTP client for API calls
- **Recharts** - Data visualization library
- **Lucide React** - Beautiful icons
- **Headless UI** - Accessible UI components

## Getting Started

### Prerequisites

- Node.js 18+ 
- npm or yarn
- Backend API running on http://127.0.0.1:8000

### Installation

1. **Install dependencies:**
   ```bash
   npm install
   ```

2. **Set up environment variables:**
   Create a `.env.local` file in the root directory:
   ```
   NEXT_PUBLIC_API_URL=http://127.0.0.1:8000
   ```

3. **Start the development server:**
   ```bash
   npm run dev
   ```

4. **Open your browser:**
   Navigate to [http://localhost:3000](http://localhost:3000)

## Project Structure

```
src/
├── app/                    # Next.js App Router pages
│   ├── dashboard/          # Dashboard page
│   ├── transactions/       # Transactions page
│   ├── budgets/           # Budgets page
│   ├── goals/             # Goals page
│   ├── reports/           # Reports page
│   ├── login/             # Login page
│   └── register/          # Registration page
├── components/            # React components
│   ├── auth/             # Authentication components
│   ├── dashboard/        # Dashboard components
│   ├── layout/           # Layout components
│   └── ui/               # Reusable UI components
├── lib/                  # Utility functions
│   ├── api.ts           # API client
│   └── utils.ts         # Helper functions
└── types/               # TypeScript type definitions
```

## Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run start` - Start production server
- `npm run lint` - Run ESLint

## API Integration

The frontend communicates with the FastAPI backend through the following endpoints:

- **Authentication**: `/api/v1/auth/login`, `/api/v1/auth/register`
- **Transactions**: `/api/v1/transactions/`
- **Budgets**: `/api/v1/budgets/`
- **Goals**: `/api/v1/goals/`
- **Reports**: `/api/v1/reports/`

## Features Overview

### Dashboard
- Financial overview with key metrics
- Recent transactions list
- Budget status overview
- Quick access to main features

### Transaction Management
- Add income and expenses
- Categorize transactions
- Filter and search
- Edit and delete transactions

### Budget Tracking
- Create monthly budgets by category
- Monitor spending against budgets
- Visual progress indicators
- Budget status alerts

### Financial Goals
- Set savings goals
- Track progress over time
- Goal completion tracking
- Visual progress charts

### Reports & Analytics
- Spending reports by category
- Income vs expenses analysis
- Budget performance tracking
- Data export to CSV

## Customization

### Styling
The app uses Tailwind CSS for styling. You can customize the design by:
- Modifying the Tailwind configuration in `tailwind.config.js`
- Updating component styles in the component files
- Changing the color scheme in the utility classes

### API Configuration
Update the API URL in `.env.local` to point to your backend:
```
NEXT_PUBLIC_API_URL=http://your-backend-url:8000
```

## Deployment

### Vercel (Recommended)
1. Push your code to GitHub
2. Connect your repository to Vercel
3. Set environment variables in Vercel dashboard
4. Deploy automatically

### Other Platforms
The app can be deployed to any platform that supports Next.js:
- Netlify
- AWS Amplify
- Railway
- DigitalOcean App Platform

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is open source and available under the MIT License.