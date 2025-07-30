# 🧰 ODIN SDK Toolkits - Complete Reference Guide

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![ODIN SDK v3](https://img.shields.io/badge/ODIN%20SDK-v3-green.svg)](https://github.com/One-Realm/python-sdk)

**Toolkits** are specialized capability modules that extend `tool_use_agent` functionality in the ODIN SDK. Each toolkit provides a specific set of tools and integrations, from web search and code execution to database operations and financial analysis.

## 📋 Overview

Toolkits are attached to agents via the `toolkits` building block and provide:
- **Specialized Tools**: Domain-specific functionality (search, SQL, Python, etc.)
- **External Integrations**: APIs, databases, and third-party services
- **Enhanced Capabilities**: Beyond basic chat to actionable intelligence

### Quick Start Example

```python
from odin_sdk.v3 import create_client

client = create_client(api_key="your-key", api_secret="your-secret")
project = client.projects().create(name="Toolkit Demo")

# Create agent with multiple toolkits
agent = project.agents.create(
    name="Multi-Toolkit Agent",
    building_blocks=[
        {"name": "agent_type", "agent_type": "tool_use_agent"},
        {"name": "ai_model", "model": "claude-sonnet-4-20250514"},
        {
            "name": "toolkits",
            "toolkits": {
                "websearch": {"config": {}},
                "python": {"config": {"enabled_tools": ["execute_python"]}, "type": "python"},
                "knowledge_base": {
                    "config": [{"project_id": project.id, "name": "KB", "description": "Knowledge base"}]
                }
            }
        }
    ]
)
```

## 🔍 Available Toolkits

| Toolkit | Purpose | Key Tools | Use Cases |
|---------|---------|-----------|-----------|
| **`websearch`** | Web search & content retrieval | `google_search`, `download_web_url` | Research, fact-checking, current events |
| **`knowledge_base`** | Document search & retrieval | `search`, `search_for_files` | Document analysis, Q&A systems |
| **`sql_database`** | Database operations | `sql_db_query`, `sql_db_schema` | Data analysis, business intelligence |
| **`python`** | Code execution & analysis | `execute_python`, `upload_file_to_sandbox` | Data science, automation, calculations |
| **`yfinance`** | Financial data analysis | Stock data retrieval, market analysis | Financial research, portfolio analysis |
| **`asana`** | Project management | Task management, project tracking | Workflow automation, productivity |
| **`azure_ad`** | Azure Active Directory | User management, authentication | Enterprise identity, access control |
| **`office365`** | Microsoft Office integration | Email, calendar, documents | Business productivity, communication |

---

## 🌐 WebSearch Toolkit

**Purpose**: Enable agents to search the web and retrieve current information from external sources.

### Schema

```python
{
    "websearch": {
        "config": {}  # Uses default configuration
    }
}
```

### Available Tools

- **`google_search`**: Search Google for articles and web pages
- **`download_web_url`**: Download and extract content from specific URLs

### SDK Usage Example

```python
# Create web search agent
web_agent = project.agents.create(
    name="Research Assistant",
    personality="You are a research assistant who finds current information online.",
    building_blocks=[
        {"name": "agent_type", "agent_type": "tool_use_agent"},
        {"name": "ai_model", "model": "GPT 4.1"},
        {
            "name": "toolkits",
            "toolkits": {
                "websearch": {"config": {}}
            }
        }
    ]
)

web_agent.activate()
chat = project.chats.create(name="Research Chat")

# Use the web search capability
response = chat.send_message(
    "What are the latest developments in AI technology this week?",
    skip_stream=True
)
```

### Use Cases

- **Current Events Research**: Get latest news and developments
- **Fact Checking**: Verify information against multiple sources
- **Market Research**: Gather competitive intelligence
- **Content Research**: Find supporting materials for reports

---

## 📚 Knowledge Base Toolkit

**Purpose**: Search and retrieve information from uploaded documents and files within projects.

### Schema

#### Single Knowledge Base
```python
{
    "knowledge_base": {
        "type": "knowledge_base",
        "config": [
            {
                "name": "Main Knowledge Base",
                "project_id": "your_project_id",
                "description": "Primary document repository"
            }
        ]
    }
}
```

#### Multiple Knowledge Bases
```python
{
    "knowledge_base": {
        "type": "knowledge_base",
        "config": [
            {
                "project_id": "docs_project_id",
                "name": "Documentation",
                "description": "Technical documentation and API references"
            },
            {
                "project_id": "support_project_id", 
                "name": "Support KB",
                "description": "Customer support articles and troubleshooting"
            }
        ]
    }
}
```

### Generated Tools

**Single KB**: `search`, `search_for_files`
**Multi KB**: `search_1`, `search_for_files_1`, `search_2`, `search_for_files_2`, etc.

### SDK Usage Example

```python
# Add documents to knowledge base
project.knowledge.add_file(
    file_path="./research_paper.pdf",
    metadata={"category": "research"},
    file_type="application/pdf"
)

# Create knowledge base agent
kb_agent = project.agents.create(
    name="Document Analyst",
    personality="You analyze documents and extract key insights with citations.",
    building_blocks=[
        {
            "name": "knowledge_base",
            "project_id": project.id,
            "generate_inline_citations": True,
            "enforce_strict_adherence": False
        },
        {"name": "agent_type", "agent_type": "tool_use_agent"},
        {"name": "ai_model", "model": "GPT 4.1"},
        {
            "name": "toolkits",
            "toolkits": {
                "knowledge_base": {
                    "config": [
                        {
                            "name": "Project Documents",
                            "project_id": project.id,
                            "description": "Uploaded research and documentation files"
                        }
                    ]
                }
            }
        }
    ]
)

kb_agent.activate()
chat = project.chats.create(name="Document Analysis")

response = chat.send_message(
    "Summarize the methodology described in the uploaded research paper.",
    skip_stream=True
)
```

### Use Cases

- **Document Q&A**: Answer questions about uploaded documents
- **Research Analysis**: Extract insights from academic papers
- **Policy Compliance**: Search internal documentation and policies
- **Technical Support**: Find solutions in knowledge bases

---

## 🗄️ SQL Database Toolkit

**Purpose**: Execute SQL queries against databases and smart tables for data analysis and business intelligence.

### Schema

#### Standard SQL Database
```python
{
    "sql_database": {
        "connection_id": "your_db_connection_id",
        "data_source_type": "sql",
        "type": "sql_database",
        "config": [
            {
                "name": "Database Configuration",
                "connection_id": "your_db_connection_id",
                "enabled_tools": [
                    "sql_db_query",
                    "sql_db_list_tables",
                    "sql_db_query_checker",
                    "sql_db_schema",
                    "describe_table",
                    "list_tables"
                ],
                "block_type": "sql"
            }
        ]
    }
}
```

#### Smart Tables Configuration
```python
{
    "sql_database": {
        "connection_id": "",
        "data_source_type": "sql",
        "type": "sql_database",
        "config": [
            {
                "name": "Smart Tables Configuration",
                "connection_id": "",
                "enabled_tools": [
                    "sql_db_query",
                    "sql_db_list_tables",
                    "sql_db_query_checker",
                    "sql_db_schema",
                    "describe_table",
                    "list_tables"
                ],
                "csv_names": [],
                "enable_all_smart_tables": True,
                "block_type": "smart_table"
            }
        ]
    }
}
```

### Available Tools

- **`sql_db_query`**: Execute SQL queries against the database
- **`sql_db_list_tables`**: List all available tables
- **`sql_db_schema`**: Get schema information for tables
- **`describe_table`**: Get detailed table structure
- **`sql_db_query_checker`**: Validate SQL query syntax

### SDK Usage Example

```python
import json

# Import CSV data first
column_mappings = [
    {"sourceColumn": "product_id", "targetColumn": "product_id", "dataType": "number"},
    {"sourceColumn": "product_name", "targetColumn": "product_name", "dataType": "text"},
    {"sourceColumn": "price", "targetColumn": "price", "dataType": "number"},
    {"sourceColumn": "category", "targetColumn": "category", "dataType": "text"}
]

table_import = project.data.import_table(
    title="products",
    description="Product catalog data",
    file_path="./products.csv",
    column_mappings=json.dumps(column_mappings)
)

# Create SQL agent
sql_agent = project.agents.create(
    name="Data Analyst",
    personality="You are a SQL expert who helps analyze business data and answer questions with precise queries.",
    building_blocks=[
        {"name": "agent_type", "agent_type": "tool_use_agent"},
        {"name": "ai_model", "model": "GPT 4.1"},
        {
            "name": "toolkits",
            "toolkits": {
                "sql_database": {
                    "connection_id": "",
                    "data_source_type": "sql",
                    "config": [
                        {
                            "name": "Database Configuration",
                            "enabled_tools": [
                                "sql_db_query",
                                "sql_db_list_tables",
                                "sql_db_schema",
                                "describe_table"
                            ],
                            "enable_all_smart_tables": True,
                            "block_type": "smart_table"
                        }
                    ],
                    "type": "sql_database"
                }
            }
        }
    ],
    temperature=0.0
)

sql_agent.activate()
chat = project.chats.create(name="Data Analysis")

response = chat.send_message(
    "What are the top 5 products by price? Show me the product name, price, and category.",
    skip_stream=True
)
```

### Use Cases

- **Business Intelligence**: Generate reports and dashboards
- **Data Analysis**: Explore datasets and find patterns
- **Financial Reporting**: Calculate KPIs and metrics
- **Inventory Management**: Track products and stock levels

---

## 🐍 Python Toolkit

**Purpose**: Execute Python code for data analysis, calculations, visualizations, and automation tasks.

### Schema

```python
{
    "python": {
        "config": {
            "enabled_tools": [
                "execute_python",
                "search_knowledge_base_files",
                "upload_file_to_sandbox",
                "list_sandbox_files",
                "create_download_url"
            ]
        },
        "type": "python"
    }
}
```

### Available Tools

- **`execute_python`**: Execute Python code in a secure sandbox
- **`upload_file_to_sandbox`**: Upload files to the Python environment
- **`list_sandbox_files`**: List files in the sandbox
- **`create_download_url`**: Create download links for generated files
- **`search_knowledge_base_files`**: Search uploaded knowledge base files

### SDK Usage Example

```python
# Create Python-enabled research agent
python_agent = project.agents.create(
    name="Data Science Agent",
    personality="""You are a data scientist with Python expertise. You can:
    - Analyze data and create visualizations
    - Perform statistical calculations
    - Generate reports and charts
    - Process and clean datasets""",
    building_blocks=[
        {"name": "agent_type", "agent_type": "tool_use_agent"},
        {"name": "ai_model", "model": "claude-sonnet-4-20250514"},
        {
            "name": "toolkits",
            "toolkits": {
                "python": {
                    "config": {
                        "enabled_tools": [
                            "execute_python",
                            "upload_file_to_sandbox",
                            "list_sandbox_files",
                            "create_download_url"
                        ]
                    },
                    "type": "python"
                }
            }
        }
    ],
    temperature=0.3
)

python_agent.activate()
chat = project.chats.create(name="Data Analysis")

response = chat.send_message("""
Create a Python analysis that:
1. Generates sample sales data for 12 months
2. Calculates monthly growth rates
3. Creates a line chart showing the trend
4. Saves the chart as a PNG file
""", skip_stream=True)
```

### Use Cases

- **Data Visualization**: Create charts, graphs, and dashboards
- **Statistical Analysis**: Perform complex calculations and modeling
- **Data Processing**: Clean, transform, and analyze datasets
- **Automation**: Build scripts for repetitive tasks
- **Machine Learning**: Develop and test ML models

---

## 💰 YFinance Toolkit

**Purpose**: Access financial market data and perform stock analysis using the yfinance library.

### Schema

```python
{
    "yfinance": {
        "config": {}  # Uses default configuration
    }
}
```

### SDK Usage Example

```python
# Create financial analysis agent
finance_agent = project.agents.create(
    name="Financial Analyst",
    personality="""You are an expert financial analyst with access to real-time market data. 
    You provide comprehensive stock analysis, market insights, and investment recommendations.""",
    building_blocks=[
        {"name": "agent_type", "agent_type": "tool_use_agent"},
        {"name": "ai_model", "model": "claude-sonnet-4-20250514"},
        {
            "name": "toolkits",
            "toolkits": {
                "websearch": {"config": {}},
                "python": {
                    "config": {"enabled_tools": ["execute_python"]},
                    "type": "python"
                },
                "yfinance": {"config": {}}
            }
        }
    ],
    temperature=0.3
)

finance_agent.activate()
chat = project.chats.create(name="Financial Analysis")

response = chat.send_message("""
Analyze Apple (AAPL) stock performance:
1. Get the last 3 months of stock data
2. Calculate key metrics (RSI, moving averages)
3. Search for recent news about Apple
4. Create a price chart with technical indicators
5. Provide investment recommendation
""", skip_stream=True)
```

### Use Cases

- **Stock Analysis**: Technical and fundamental analysis of individual stocks
- **Portfolio Management**: Track and analyze investment portfolios
- **Market Research**: Compare multiple stocks and sectors
- **Financial Reporting**: Generate investment reports and summaries

---

## 🚀 Multi-Toolkit Combinations

### Research & Analysis Powerhouse

```python
research_agent = project.agents.create(
    name="Comprehensive Research Agent",
    personality="""You are an intelligent research analyst with capabilities in:
    - Web research and fact-checking
    - Document analysis and knowledge extraction  
    - Data analysis and visualization with Python
    - Financial market analysis using yfinance
    - Comprehensive report generation""",
    building_blocks=[
        {"name": "agent_type", "agent_type": "tool_use_agent"},
        {"name": "ai_model", "model": "claude-sonnet-4-20250514"},
        {
            "name": "toolkits",
            "toolkits": {
                "websearch": {"config": {}},
                "knowledge_base": {
                    "config": [{
                        "project_id": project.id,
                        "name": "Research Documents",
                        "description": "Uploaded research papers and documents"
                    }]
                },
                "python": {
                    "config": {
                        "enabled_tools": [
                            "execute_python",
                            "upload_file_to_sandbox",
                            "create_download_url"
                        ]
                    },
                    "type": "python"
                },
                "yfinance": {"config": {}}
            }
        }
    ],
    temperature=0.5
)
```

### Business Intelligence Suite

```python
bi_agent = project.agents.create(
    name="Business Intelligence Agent",
    building_blocks=[
        {"name": "agent_type", "agent_type": "tool_use_agent"},
        {"name": "ai_model", "model": "GPT 4.1"},
        {
            "name": "toolkits",
            "toolkits": {
                "sql_database": {
                    "config": [{"enable_all_smart_tables": True}],
                    "type": "sql_database"
                },
                "python": {
                    "config": {"enabled_tools": ["execute_python"]},
                    "type": "python"
                },
                "websearch": {"config": {}}
            }
        }
    ]
)
```

## 🔧 Best Practices

### 1. Toolkit Selection
- **Single Purpose**: Use specific toolkits for focused tasks
- **Multi-Toolkit**: Combine complementary toolkits for complex workflows
- **Performance**: More toolkits = more tools = potentially slower responses

### 2. Configuration Tips
- **Enable Only Needed Tools**: Specify `enabled_tools` to limit scope
- **Temperature Settings**: Lower temperature (0.0-0.3) for analytical tasks
- **Model Selection**: Choose appropriate models for toolkit complexity

### 3. Error Handling
```python
from odin_sdk.v3 import OdinError

try:
    agent = project.agents.create(
        name="Test Agent",
        building_blocks=[
            {"name": "agent_type", "agent_type": "tool_use_agent"},
            {"name": "toolkits", "toolkits": {"websearch": {"config": {}}}}
        ]
    )
    agent.activate()
except OdinError as e:
    print(f"Toolkit configuration error: {e}")
```

### 4. Resource Management
```python
# Always clean up resources
try:
    # Create and use agent
    pass
finally:
    if 'project' in locals():
        project.delete()
```

## 🎯 Toolkit Combinations by Use Case

| Use Case | Recommended Toolkits | Example |
|----------|----------------------|---------|
| **Research & Analysis** | `websearch` + `knowledge_base` + `python` | Market research with data visualization |
| **Financial Analysis** | `yfinance` + `python` + `websearch` | Stock analysis with current news |
| **Business Intelligence** | `sql_database` + `python` + `websearch` | Dashboard creation with market context |
| **Document Processing** | `knowledge_base` + `python` | PDF analysis with data extraction |
| **Data Science** | `python` + `sql_database` | Statistical analysis of business data |

## 📚 Additional Resources

- **SDK Documentation**: [ODIN SDK v3 Guide](README.md)
- **Building Blocks**: [Complete Building Blocks Reference](Blocks.md)
- **Examples**: See `examples/` directory for working implementations
- **Documentation**: [https://api.getodin.ai/docs](https://api.getodin.ai/docs)
- **Website**: [https://getodin.ai](https://getodin.ai)

---

**Built with ❤️ by the ODIN AI Team**

---

**💡 Pro Tip**: Start with single-toolkit agents to understand capabilities, then combine toolkits for more sophisticated workflows. The examples in the SDK repository demonstrate real-world usage patterns for each toolkit combination.