# 🎯 Gemini CLI MCP Server JSON Configurations

## 📋 Available Configuration Files

### 1. **Simple Configuration** (`gemini_simple_config.json`)
**Recommended for most users**

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

### 2. **Detailed Configuration** (`gemini_mcp_config.json`)
**Complete with tool schemas and descriptions**

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
      },
      "description": "Finance Tracker MCP Server with 8 financial management tools",
      "version": "2.0.0",
      "capabilities": {
        "tools": true,
        "resources": false,
        "prompts": false
      }
    }
  }
}
```

### 3. **Basic Configuration** (`mcp_server_config.json`)
**Minimal setup**

```json
{
  "mcpServers": {
    "finance-tracker": {
      "command": "python",
      "args": [
        "D:/make_ownapp_and_mcp/start_mcp_server.py"
      ],
      "env": {
        "PYTHONPATH": "D:/make_ownapp_and_mcp"
      }
    }
  }
}
```

## 🚀 Quick Setup Instructions

### Step 1: Choose Your Configuration
- **For beginners**: Use `gemini_simple_config.json`
- **For advanced users**: Use `gemini_mcp_config.json`
- **For minimal setup**: Use `mcp_server_config.json`

### Step 2: Copy to Gemini CLI Config Directory

**Windows:**
```bash
copy gemini_simple_config.json %APPDATA%\gemini\mcp_servers.json
```

**macOS:**
```bash
cp gemini_simple_config.json ~/.config/gemini/mcp_servers.json
```

**Linux:**
```bash
cp gemini_simple_config.json ~/.config/gemini/mcp_servers.json
```

### Step 3: Update Paths
Make sure to update the paths in the JSON file to match your system:

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

## 🛠️ Available MCP Tools

Your Finance Tracker MCP server provides these 8 tools:

### 📊 Transaction Management
1. **`add_transaction`** - Add income or expense transactions
2. **`get_transactions`** - Retrieve transactions with filtering

### 💰 Financial Analytics  
3. **`get_financial_summary`** - Get comprehensive financial overview
4. **`analyze_spending_patterns`** - Analyze spending behavior

### 📈 Budget Management
5. **`create_budget`** - Create spending budgets
6. **`get_budget_status`** - Check budget performance

### 🎯 Goal Setting
7. **`create_financial_goal`** - Set financial goals
8. **`get_financial_goals`** - View all goals

## 💡 Usage Examples

Once integrated with Gemini CLI, you can use natural language:

### Example Commands:
- **"Add a $50 expense for groceries"**
- **"Show me my spending summary for this month"**
- **"Create a $300 monthly food budget"**
- **"What are my financial goals?"**
- **"Analyze my spending patterns over the last 30 days"**
- **"How am I doing with my budgets?"**

## 🔧 Troubleshooting

### Test Your Setup:
```bash
# Test MCP server directly
python start_mcp_for_gemini.py

# Test imports
python -c "from mcp_server import mcp; print('MCP server ready')"

# Test database
python -c "from app.database import engine; print('Database connected')"
```

### Common Issues:
1. **Path Issues**: Make sure all paths are absolute and correct
2. **Python PATH**: Ensure Python is in your system PATH
3. **Dependencies**: Run `pip install -r requirements.txt`
4. **Database**: Ensure `finance_tracker_litequery.db` exists

## 📊 Sample Data Available

Your MCP server comes with rich dummy data:
- **3 Users** with realistic profiles
- **142 Transactions** across various categories  
- **18 Budgets** for different spending areas
- **15 Financial Goals** with progress tracking

## 🎉 Ready to Use!

Your Finance Tracker MCP server is now ready for Gemini CLI integration with:

✅ **8 Financial Management Tools**  
✅ **Rich Sample Data**  
✅ **Natural Language Interface**  
✅ **AI-Powered Analytics**  
✅ **Budget Tracking**  
✅ **Goal Management**  

Choose your configuration file and follow the setup instructions to start using your Finance Tracker with Gemini CLI!
