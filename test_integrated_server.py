#!/usr/bin/env python3
"""
Test the Integrated Server (FastAPI + MCP)
"""

import requests
import json
import time

def test_integrated_server():
    """Test the integrated server endpoints"""
    base_url = "http://localhost:8000"
    
    print("🧪 Testing Integrated Server")
    print("=" * 50)
    
    # Test 1: Root endpoint
    print("1. Testing root endpoint...")
    try:
        response = requests.get(f"{base_url}/")
        if response.status_code == 200:
            data = response.json()
            print(f"   ✅ Server running: {data.get('message', 'Unknown')}")
            print(f"   ✅ Version: {data.get('version', 'Unknown')}")
            print(f"   ✅ MCP Server: {data.get('mcp_server', 'Unknown')}")
        else:
            print(f"   ❌ Status: {response.status_code}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test 2: Health check
    print("\n2. Testing health endpoint...")
    try:
        response = requests.get(f"{base_url}/health")
        if response.status_code == 200:
            data = response.json()
            print(f"   ✅ Status: {data.get('status', 'Unknown')}")
            print(f"   ✅ MCP Server: {data.get('mcp_server', 'Unknown')}")
        else:
            print(f"   ❌ Status: {response.status_code}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test 3: MCP tools list
    print("\n3. Testing MCP tools endpoint...")
    try:
        response = requests.get(f"{base_url}/mcp/tools")
        if response.status_code == 200:
            data = response.json()
            tools = data.get('available_tools', [])
            print(f"   ✅ Found {len(tools)} MCP tools:")
            for tool in tools[:3]:  # Show first 3 tools
                print(f"      - {tool.get('name', 'Unknown')}: {tool.get('description', 'No description')}")
        else:
            print(f"   ❌ Status: {response.status_code}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test 4: MCP status
    print("\n4. Testing MCP status endpoint...")
    try:
        response = requests.get(f"{base_url}/mcp/status")
        if response.status_code == 200:
            data = response.json()
            print(f"   ✅ MCP Running: {data.get('mcp_server_running', 'Unknown')}")
            print(f"   ✅ Protocol: {data.get('protocol', 'Unknown')}")
        else:
            print(f"   ❌ Status: {response.status_code}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test 5: API documentation
    print("\n5. Testing API documentation...")
    try:
        response = requests.get(f"{base_url}/docs")
        if response.status_code == 200:
            print(f"   ✅ API docs available at {base_url}/docs")
        else:
            print(f"   ❌ Status: {response.status_code}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    print("\n🎉 Integrated Server Testing Completed!")
    print("=" * 50)

if __name__ == "__main__":
    print("Make sure the integrated server is running:")
    print("python integrated_server.py")
    print()
    test_integrated_server()
