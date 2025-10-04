# Gemini CLI Integration Guide

## 🚀 MCP Server Configuration for Gemini CLI

This guide shows how to integrate your Finance Tracker MCP server with Gemini CLI.

## 📁 Configuration Files

### 1. Simple Configuration (`gemini_simple_config.json`)
```json
{
  "mcpServers": {
    "finance-tracker": {
      "command": "python",
      "args": [
        "D:/make_ownapp_and_mcp/start_mcp_for_gemini.py"
      ],
      "env": {
        "PYTHONPATH": "D:/make_ownapp_and_mcp",
        "DATABASE_URL": "sqlite:///./finance_tracker_litequery.db"
      }
    }
  }
}
```

### 2. Detailed Configuration (`gemini_mcp_config.json`)
Complete configuration with tool schemas and descriptions.

## 🛠️ Setup Instructions

### Step 1: Copy Configuration
Copy one of the configuration files to your Gemini CLI configuration directory:

**For Windows:**
```bash
copy gemini_simple_config.json %APPDATA%\gemini\mcp_servers.json
```

**For macOS/Linux:**
```bash
cp gemini_simple_config.json ~/.config/gemini/mcp_servers.json
```

### Step 2: Update Paths
Make sure to update the paths in the configuration to match your system:

```json
{
  "mcpServers": {
    "finance-tracker": {
      "command": "python",
      "args": [
        "/your/actual/path/to/make_ownapp_and_mcp/start_mcp_for_gemini.py"
      ],
      "env": {
        "PYTHONPATH": "/your/actual/path/to/make_ownapp_and_mcp",
        "DATABASE_URL": "sqlite:///./finance_tracker_litequery.db"
      }
    }
  }
}
```

### Step 3: Test Integration
Start Gemini CLI and test the integration:

```bash
gemini --mcp-servers
```

## 🎯 Available MCP Tools

Your Finance Tracker MCP server provides these tools for Gemini CLI:

### Financial Transaction Management
- **`add_transaction`** - Add income or expense transactions
- **`get_transactions`** - Retrieve transactions with filtering

### Financial Analytics
- **`get_financial_summary`** - Get comprehensive financial overview
- **`analyze_spending_patterns`** - Analyze spending behavior

### Budget Management
- **`create_budget`** - Create spending budgets
- **`get_budget_status`** - Check budget performance

### Financial Goals
- **`create_financial_goal`** - Set financial goals
- **`get_financial_goals`** - View all goals

## 💡 Usage Examples

Once integrated with Gemini CLI, you can use natural language to interact with your financial data:

### Example Commands:
- "Add a $50 expense for groceries"
- "Show me my spending summary for this month"
- "Create a $300 monthly food budget"
- "What are my financial goals?"
- "Analyze my spending patterns over the last 30 days"
- "How am I doing with my budgets?"

## 🔧 Troubleshooting

### Common Issues:

1. **Path Issues**
   - Make sure all paths in the configuration are absolute
   - Verify Python is in your PATH

2. **Database Issues**
   - Ensure the database file exists: `finance_tracker_litequery.db`
   - Run `python create_dummy_data.py` if needed

3. **Import Issues**
   - Check that all dependencies are installed: `pip install -r requirements.txt`
   - Verify PYTHONPATH is set correctly

### Debug Steps:

1. **Test MCP Server Directly:**
   ```bash
   python start_mcp_for_gemini.py
   ```

2. **Check Dependencies:**
   ```bash
   python -c "from mcp_server import mcp; print('MCP server imports successfully')"
   ```

3. **Verify Database:**
   ```bash
   python -c "from app.database import engine; print('Database connection successful')"
   ```

## 📊 Sample Data

Your MCP server comes with rich dummy data:
- **3 Users** with realistic profiles
- **142 Transactions** across various categories
- **18 Budgets** for different spending areas
- **15 Financial Goals** with progress tracking

## 🚀 Advanced Configuration

### Custom Environment Variables:
```json
{
  "mcpServers": {
    "finance-tracker": {
      "command": "python",
      "args": ["D:/make_ownapp_and_mcp/start_mcp_for_gemini.py"],
      "env": {
        "PYTHONPATH": "D:/make_ownapp_and_mcp",
        "DATABASE_URL": "sqlite:///./finance_tracker_litequery.db",
        "DEBUG": "false",
        "LOG_LEVEL": "INFO"
      }
    }
  }
}
```

### Multiple MCP Servers:
```json
{
  "mcpServers": {
    "finance-tracker": {
      "command": "python",
      "args": ["D:/make_ownapp_and_mcp/start_mcp_for_gemini.py"]
    },
    "other-server": {
      "command": "python",
      "args": ["/path/to/other/server.py"]
    }
  }
}
```

## 🎉 Ready to Use!

Once configured, your Finance Tracker MCP server will be available in Gemini CLI, allowing you to:

- ✅ Manage financial transactions through natural language
- ✅ Get insights and analytics on your spending
- ✅ Create and track budgets
- ✅ Set and monitor financial goals
- ✅ Analyze spending patterns with AI assistance

Your finance tracker is now fully integrated with Gemini CLI for AI-powered financial management!
