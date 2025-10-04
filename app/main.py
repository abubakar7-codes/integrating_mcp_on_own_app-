from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from app.database import get_db
from app.routers import transactions_simple, reports_simple
from app.models import Base
from app.database import engine

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Personal Finance Tracker API",
    description="A comprehensive API for tracking income, expenses, budgets, and financial goals",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS middleware
from app.config import settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

# No authentication required

# Include routers (no authentication required)
app.include_router(transactions_simple.router, prefix="/api/v1/transactions", tags=["Transactions"])
app.include_router(reports_simple.router, prefix="/api/v1/reports", tags=["Reports & Analytics"])

@app.get("/")
async def root():
    return {
        "message": "Welcome to Personal Finance Tracker API",
        "version": "1.0.0",
        "docs": "/docs"
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
