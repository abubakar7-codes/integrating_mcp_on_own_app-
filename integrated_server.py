#!/usr/bin/env python3
"""
Integrated Finance Tracker Server
Combines FastAPI backend with MCP server capabilities
"""

import asyncio
import threading
import time
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from contextlib import asynccontextmanager

# Import your existing modules
from app.database import get_db
from app.routers import transactions_simple, reports_simple
from app.models import Base
from app.database import engine
from app.config import settings

# Import MCP server
from mcp_server import mcp

# Global variable to store MCP server thread
mcp_server_thread = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan manager"""
    global mcp_server_thread
    
    # Start MCP server in background thread
    print("🚀 Starting MCP server in background...")
    mcp_server_thread = threading.Thread(target=run_mcp_server, daemon=True)
    mcp_server_thread.start()
    
    # Wait a moment for MCP server to initialize
    await asyncio.sleep(2)
    
    yield
    
    # Cleanup (if needed)
    print("🛑 Shutting down MCP server...")

def run_mcp_server():
    """Run MCP server in a separate thread"""
    try:
        print("📡 MCP Server starting in background thread...")
        mcp.run()
    except Exception as e:
        print(f"❌ MCP Server error: {e}")

# Create database tables
Base.metadata.create_all(bind=engine)

# Create FastAPI app with lifespan
app = FastAPI(
    title="Personal Finance Tracker API with MCP Integration",
    description="A comprehensive API for tracking income, expenses, budgets, and financial goals with AI-powered MCP tools",
    version="2.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

# Include existing routers
app.include_router(transactions_simple.router, prefix="/api/v1/transactions", tags=["Transactions"])
app.include_router(reports_simple.router, prefix="/api/v1/reports", tags=["Reports & Analytics"])

# Add MCP-specific endpoints
@app.get("/")
async def root():
    return {
        "message": "Welcome to Personal Finance Tracker API with MCP Integration",
        "version": "2.0.0",
        "docs": "/docs",
        "mcp_server": "Running in background",
        "features": [
            "REST API endpoints for financial data",
            "MCP server for AI tool integration",
            "Transaction management",
            "Budget tracking",
            "Financial goal setting",
            "Spending analytics"
        ]
    }

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "mcp_server": "active" if mcp_server_thread and mcp_server_thread.is_alive() else "inactive"
    }

@app.get("/mcp/tools")
async def list_mcp_tools():
    """List available MCP tools"""
    return {
        "available_tools": [
            {
                "name": "add_transaction",
                "description": "Add a new financial transaction (income or expense)",
                "parameters": ["amount", "description", "transaction_type", "category", "user_id"]
            },
            {
                "name": "get_transactions",
                "description": "Retrieve financial transactions with optional filtering",
                "parameters": ["user_id", "limit", "transaction_type", "category", "start_date", "end_date"]
            },
            {
                "name": "get_financial_summary",
                "description": "Get a comprehensive financial summary including income, expenses, and net worth",
                "parameters": ["user_id", "start_date", "end_date"]
            },
            {
                "name": "create_budget",
                "description": "Create a new budget for a specific category and time period",
                "parameters": ["name", "category", "amount", "period", "start_date", "end_date", "user_id"]
            },
            {
                "name": "get_budget_status",
                "description": "Get current status of all budgets including spending vs. budget amounts",
                "parameters": ["user_id"]
            },
            {
                "name": "create_financial_goal",
                "description": "Create a new financial goal",
                "parameters": ["title", "description", "target_amount", "target_date", "user_id"]
            },
            {
                "name": "get_financial_goals",
                "description": "Get all financial goals for a user",
                "parameters": ["user_id"]
            },
            {
                "name": "analyze_spending_patterns",
                "description": "Analyze spending patterns over a specified period",
                "parameters": ["user_id", "days"]
            }
        ],
        "usage": "These tools are available through the MCP protocol for AI model integration"
    }

@app.get("/mcp/status")
async def mcp_status():
    """Check MCP server status"""
    return {
        "mcp_server_running": mcp_server_thread and mcp_server_thread.is_alive(),
        "server_info": "MCP server provides AI tools for financial data management",
        "protocol": "Model Context Protocol (MCP)",
        "integration": "Seamlessly integrated with FastAPI backend"
    }

if __name__ == "__main__":
    print("=" * 80)
    print("🚀 Finance Tracker Integrated Server")
    print("=" * 80)
    print("Starting integrated server with:")
    print("  • FastAPI REST API (Port 8000)")
    print("  • MCP Server (Background)")
    print("  • Database integration")
    print("  • CORS enabled")
    print("=" * 80)
    print()
    print("Available endpoints:")
    print("  • http://localhost:8000/ - API information")
    print("  • http://localhost:8000/docs - Interactive API documentation")
    print("  • http://localhost:8000/mcp/tools - MCP tools list")
    print("  • http://localhost:8000/mcp/status - MCP server status")
    print()
    print("MCP tools available for AI integration:")
    print("  • Financial transaction management")
    print("  • Budget creation and tracking")
    print("  • Financial goal setting")
    print("  • Spending pattern analysis")
    print("=" * 80)
    
    uvicorn.run(
        "integrated_server:app", 
        host="0.0.0.0", 
        port=8000, 
        reload=True,
        log_level="info"
    )
