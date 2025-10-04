# Finance Tracker MCP Integration Guide

This guide explains how to use the Model Context Protocol (MCP) server integration with your Finance Tracker application.

## 🚀 Quick Start

### 1. Start the Integrated Server
```bash
python integrated_server.py
```

This starts both the FastAPI backend and MCP server together.

### 2. Start MCP Server Separately (Optional)
```bash
python start_mcp_server.py
```

### 3. Test the MCP Server
```bash
python test_mcp_client.py
```

## 📊 Available MCP Tools

The MCP server provides the following AI-callable tools:

### Financial Transaction Management
- **`add_transaction`** - Add income or expense transactions
- **`get_transactions`** - Retrieve transactions with filtering
- **`get_financial_summary`** - Get comprehensive financial overview

### Budget Management
- **`create_budget`** - Create spending budgets for categories
- **`get_budget_status`** - Check budget performance and spending

### Financial Goals
- **`create_financial_goal`** - Set financial goals and targets
- **`get_financial_goals`** - View all financial goals

### Analytics
- **`analyze_spending_patterns`** - Analyze spending behavior over time

## 🔧 Tool Usage Examples

### Adding a Transaction
```python
# Add income
await session.call_tool("add_transaction", {
    "amount": 1500.0,
    "description": "Salary payment",
    "transaction_type": "income",
    "category": "salary"
})

# Add expense
await session.call_tool("add_transaction", {
    "amount": 50.0,
    "description": "Grocery shopping",
    "transaction_type": "expense",
    "category": "food"
})
```

### Getting Financial Summary
```python
summary = await session.call_tool("get_financial_summary", {
    "user_id": 1,
    "start_date": "2024-01-01",
    "end_date": "2024-01-31"
})
```

### Creating a Budget
```python
budget = await session.call_tool("create_budget", {
    "name": "Monthly Food Budget",
    "category": "food",
    "amount": 300.0,
    "period": "monthly",
    "start_date": "2024-01-01",
    "end_date": "2024-01-31"
})
```

### Analyzing Spending Patterns
```python
analysis = await session.call_tool("analyze_spending_patterns", {
    "user_id": 1,
    "days": 30
})
```

## 🌐 API Endpoints

The integrated server provides these additional endpoints:

- `GET /` - API information and features
- `GET /health` - Health check including MCP server status
- `GET /mcp/tools` - List all available MCP tools
- `GET /mcp/status` - MCP server status and information

## 🔌 MCP Client Integration

### Using with Claude Desktop
Add to your Claude Desktop configuration:

```json
{
  "mcpServers": {
    "finance-tracker": {
      "command": "python",
      "args": ["D:/make_ownapp_and_mcp/start_mcp_server.py"]
    }
  }
}
```

### Using with Other MCP Clients
The MCP server can be integrated with any MCP-compatible client by connecting to the stdio interface.

## 📁 File Structure

```
├── mcp_server.py              # Main MCP server implementation
├── start_mcp_server.py        # MCP server startup script
├── integrated_server.py       # Combined FastAPI + MCP server
├── test_mcp_client.py         # MCP client test script
├── MCP_INTEGRATION_GUIDE.md   # This guide
└── app/                       # Your existing FastAPI application
    ├── main.py
    ├── models.py
    ├── database.py
    └── routers/
```

## 🛠️ Development

### Adding New MCP Tools

1. Add a new function to `mcp_server.py` with the `@mcp.tool` decorator
2. Include proper type hints and docstring
3. Handle database operations safely with try/catch
4. Return structured data

Example:
```python
@mcp.tool
def my_new_tool(param1: str, param2: int) -> Dict[str, Any]:
    """
    Description of what this tool does
    
    Args:
        param1: Description of param1
        param2: Description of param2
    
    Returns:
        Dictionary with results
    """
    # Implementation here
    return {"result": "success"}
```

### Testing MCP Tools

Use the test client to verify your tools work correctly:

```bash
python test_mcp_client.py
```

## 🔒 Security Considerations

- All database operations use parameterized queries
- User ID validation is implemented
- Error handling prevents information leakage
- Database sessions are properly managed

## 📈 Performance

- MCP server runs in background thread
- Database connections are pooled
- Async operations where possible
- Minimal memory footprint

## 🐛 Troubleshooting

### MCP Server Not Starting
- Check Python path and dependencies
- Verify database connection
- Check for port conflicts

### Database Errors
- Ensure database file exists
- Check database permissions
- Verify model imports

### Tool Execution Errors
- Check parameter types
- Verify database session
- Review error messages in logs

## 📚 Additional Resources

- [FastMCP Documentation](https://gofastmcp.com)
- [Model Context Protocol Specification](https://modelcontextprotocol.io)
- [FastAPI Documentation](https://fastapi.tiangolo.com)

## 🤝 Contributing

When adding new MCP tools:

1. Follow the existing pattern in `mcp_server.py`
2. Add comprehensive docstrings
3. Include error handling
4. Test with the client script
5. Update this guide

## 📞 Support

For issues with the MCP integration:

1. Check the logs for error messages
2. Verify all dependencies are installed
3. Test with the provided client script
4. Review the FastMCP documentation
