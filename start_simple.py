#!/usr/bin/env python3
"""
Simple startup script without authentication
"""

import uvicorn

if __name__ == "__main__":
    print("🚀 Starting Personal Finance Tracker API (No Auth)")
    print("📍 Environment: Development")
    print("🌐 Server: http://127.0.0.1:8000")
    print("📚 Docs: http://127.0.0.1:8000/docs")
    print("🔓 No authentication required")
    
    uvicorn.run(
        "app.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
        log_level="info"
    )
