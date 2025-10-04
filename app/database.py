from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Database URL - using SQLite with litequery for enhanced performance
DATABASE_URL = "sqlite:///./finance_tracker_litequery.db"

# Create SQLite engine with litequery optimizations
engine = create_engine(
    DATABASE_URL,
    echo=True,  # Enable SQL logging for debugging
    pool_pre_ping=True,
    pool_recycle=300,
    connect_args={
        "timeout": 20,
        "check_same_thread": False,
        "isolation_level": None  # Enable autocommit for better performance
    }
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
