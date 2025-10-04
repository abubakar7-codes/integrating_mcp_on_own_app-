#!/bin/bash
# Production-ready frontend startup script

echo "🚀 Starting Personal Finance Tracker Frontend"
echo "📍 Environment: $NODE_ENV"
echo "🌐 Server: http://localhost:3000"

# Load environment variables
if [ -f "frontend.env" ]; then
    export $(cat frontend.env | xargs)
    echo "✅ Environment variables loaded"
fi

# Install dependencies if needed
if [ ! -d "node_modules" ]; then
    echo "📦 Installing dependencies..."
    npm install
fi

# Start the development server
npm run dev
