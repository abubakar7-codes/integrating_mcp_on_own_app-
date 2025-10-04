#!/usr/bin/env python3
"""
Production-ready backend startup script
Loads environment variables and starts the FastAPI server
"""

import os
import uvicorn
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv('backend.env')

if __name__ == "__main__":
    # Get configuration from environment
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "8000"))
    reload = os.getenv("ENVIRONMENT", "development") == "development"
    
    print(f"🚀 Starting Personal Finance Tracker API")
    print(f"📍 Environment: {os.getenv('ENVIRONMENT', 'development')}")
    print(f"🌐 Server: http://{host}:{port}")
    print(f"📚 Docs: http://{host}:{port}/docs")
    print(f"🔄 Reload: {reload}")
    
    uvicorn.run(
        "app.main:app",
        host=host,
        port=port,
        reload=reload,
        log_level="info"
    )
