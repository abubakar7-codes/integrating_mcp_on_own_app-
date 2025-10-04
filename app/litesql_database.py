"""
LiteSQL Database Configuration
Replaces SQLite with LiteSQL for the finance tracker
"""

import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from litesql import LiteSQL

# Database URL for LiteSQL
DATABASE_URL = "litesql:///./finance_tracker_litesql.db"

# Create LiteSQL engine
engine = create_engine(
    DATABASE_URL,
    echo=True,  # Enable SQL logging for debugging
    pool_pre_ping=True,
    pool_recycle=300
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    """Get database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_litesql_database():
    """Initialize LiteSQL database with tables"""
    # Create all tables
    Base.metadata.create_all(bind=engine)
    print("✅ LiteSQL database initialized successfully")

def get_litesql_connection():
    """Get direct LiteSQL connection for advanced operations"""
    return LiteSQL("./finance_tracker_litesql.db")
