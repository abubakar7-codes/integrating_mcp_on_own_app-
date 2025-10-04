#!/usr/bin/env python3
"""
Test script for the fast server setup
Verifies that all server configurations work correctly
"""

import subprocess
import time
import requests
import sys
import os
from pathlib import Path

def test_server_startup(server_type, timeout=30):
    """Test if a server can start successfully"""
    print(f"🧪 Testing {server_type} server startup...")
    
    try:
        # Start server in background
        if server_type == "hypercorn":
            cmd = ["hypercorn", "app.main:app", "--bind", "127.0.0.1:8001", "--workers", "1"]
        elif server_type == "gunicorn":
            cmd = ["gunicorn", "app.main:app", "-w", "1", "-k", "uvicorn.workers.UvicornWorker", "-b", "127.0.0.1:8001"]
        elif server_type == "uvicorn":
            cmd = ["uvicorn", "app.main:app", "--host", "127.0.0.1", "--port", "8001", "--workers", "1"]
        else:
            print(f"❌ Unknown server type: {server_type}")
            return False
        
        # Start process
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Wait for server to start
        start_time = time.time()
        while time.time() - start_time < timeout:
            try:
                response = requests.get("http://127.0.0.1:8001/health", timeout=1)
                if response.status_code == 200:
                    print(f"✅ {server_type} server started successfully!")
                    process.terminate()
                    process.wait(timeout=5)
                    return True
            except requests.exceptions.RequestException:
                time.sleep(1)
        
        # If we get here, server didn't start in time
        print(f"❌ {server_type} server failed to start within {timeout}s")
        process.terminate()
        process.wait(timeout=5)
        return False
        
    except Exception as e:
        print(f"❌ Error testing {server_type}: {e}")
        return False

def test_performance_monitor():
    """Test the performance monitoring script"""
    print("🧪 Testing performance monitor...")
    
    try:
        # Test if monitor script can be imported
        import monitor_performance
        print("✅ Performance monitor script imports successfully")
        
        # Test basic functionality
        monitor = monitor_performance.PerformanceMonitor("http://127.0.0.1:8001")
        stats = monitor.get_system_stats()
        
        if "cpu_percent" in stats and "memory_percent" in stats:
            print("✅ Performance monitor can collect system stats")
            return True
        else:
            print("❌ Performance monitor failed to collect stats")
            return False
            
    except Exception as e:
        print(f"❌ Error testing performance monitor: {e}")
        return False

def test_configuration_files():
    """Test that all configuration files exist and are valid"""
    print("🧪 Testing configuration files...")
    
    config_files = [
        "server_config.py",
        "gunicorn.conf.py", 
        "hypercorn.toml",
        "start_fast_server.py",
        "monitor_performance.py"
    ]
    
    all_exist = True
    for file in config_files:
        if Path(file).exists():
            print(f"✅ {file} exists")
        else:
            print(f"❌ {file} missing")
            all_exist = False
    
    return all_exist

def test_dependencies():
    """Test that all required dependencies are available"""
    print("🧪 Testing dependencies...")
    
    required_packages = [
        "fastapi",
        "uvicorn", 
        "hypercorn",
        "gunicorn",
        "psutil",
        "requests"
    ]
    
    all_available = True
    for package in required_packages:
        try:
            __import__(package)
            print(f"✅ {package} available")
        except ImportError:
            print(f"❌ {package} not available")
            all_available = False
    
    return all_available

def main():
    """Run all tests"""
    print("🚀 Fast Server Setup Test Suite")
    print("=" * 50)
    
    tests = [
        ("Configuration Files", test_configuration_files),
        ("Dependencies", test_dependencies),
        ("Performance Monitor", test_performance_monitor),
        ("Hypercorn Server", lambda: test_server_startup("hypercorn")),
        ("Gunicorn Server", lambda: test_server_startup("gunicorn")),
        ("Uvicorn Server", lambda: test_server_startup("uvicorn"))
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n📋 {test_name}")
        print("-" * 30)
        
        try:
            if test_func():
                passed += 1
                print(f"✅ {test_name} PASSED")
            else:
                print(f"❌ {test_name} FAILED")
        except Exception as e:
            print(f"❌ {test_name} ERROR: {e}")
    
    print("\n" + "=" * 50)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Fast server setup is ready!")
        print("\n🚀 Quick start commands:")
        print("   python start_fast_server.py --server hypercorn")
        print("   python start_fast_server.py --server gunicorn") 
        print("   python start_fast_server.py --server uvicorn")
        return 0
    else:
        print("⚠️  Some tests failed. Please check the output above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
