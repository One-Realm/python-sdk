# 🧠 ODIN SDK v3 - Python Client for Intelligent AI Agents

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**ODIN SDK v3** is a powerful Python client library for building and managing intelligent AI agents with advanced capabilities including knowledge base integration, multi-toolkit functionality, web search, code execution, financial analysis, and SQL database operations.

## ✨ Key Features

- 🚀 **Enhanced Resource Objects** - Flattened response objects with intuitive attribute access
- 🎯 **Convenience Methods** - Resource-aware methods like `project.delete()`, `agent.activate()`
- 🔗 **Project-Scoped Managers** - Clean API design with `project.agents.create()`, `project.chats.create()`
- 🧰 **Multi-Toolkit Agents** - Web search, Python execution, financial analysis, and SQL operations
- 📚 **Knowledge Base Integration** - PDF upload, document management, and intelligent retrieval
- 💬 **Advanced Chat Management** - Conversational AI with context and memory
- 📊 **Smart Tables & SQL** - CSV import, database operations, and intelligent querying
- 🔄 **Full Backward Compatibility** - Seamless upgrade from v2 with enhanced functionality
- 📖 **Comprehensive Documentation** - Complete references for [Building Blocks](Blocks.md) and [Toolkits](ToolKits.md)

## 🚀 Quick Start

### Installation

```bash
pip install odinai-sdk
```

### Basic Usage

```python
from odin_sdk.v3 import create_client, OdinError

# Initialize client
client = create_client(
    api_key="your-api-key",
    api_secret="your-api-secret",
    host="https://api.example.com"  # Your ODIN API host
)

# Create a project
project = client.projects().create(
    name="My AI Project",
    description="A project showcasing ODIN SDK capabilities"
)

print(f"Project created: {project.name} (ID: {project.id})")

# Add knowledge to the project
kb_response = project.knowledge.add_file(
    file_path="./document.pdf",
    metadata={"category": "documentation"},
    file_type="application/pdf"
)

# Create an intelligent agent
agent = project.agents.create(
    name="Research Assistant",
    personality="You are a helpful research assistant with access to uploaded documents.",
    building_blocks=[
        {
            "name": "knowledge_base",  # See Blocks.md for complete knowledge_base options
            "project_id": project.id,
            "generate_inline_citations": True,
            "enforce_strict_adherence": False
        },
        {"name": "ai_model", "model": "GPT 4.1"},  # See Blocks.md for all available models
        {"name": "agent_type", "agent_type": "tool_use_agent"}  # Required core block
    ]
)

# Activate the agent
agent.activate()

# Create a chat session
chat = project.chats.create(
    name="Research Discussion",
    context="Help me understand the uploaded documents"
)

# Send a message
response = chat.send_message(
    message="Summarize the key points from the uploaded document",
    skip_stream=True
)

print(f"AI Response: {response.message}")

# Cleanup
project.delete()
```

> **🚀 Next Steps**: This quick start uses basic building blocks. For advanced configurations, see [Blocks.md](Blocks.md) for all building block options and [ToolKits.md](ToolKits.md) for additional capabilities like web search, Python execution, and database operations.

## 🔧 API Overview

### Core Client & Resources

#### Client Initialization
```python
from odin_sdk.v3 import create_client

client = create_client(
    api_key="your-api-key",
    api_secret="your-api-secret", 
    host="https://your-odin-host.com"
)
```

#### Project Management
```python
# Create project
project = client.projects().create(
    name="AI Project",
    description="Project description",
    project_type="kb_chat"  # Options: kb_chat, data_analysis, etc.
)

# Enhanced project methods
project.update(name="Updated Name")
project.add_user("user@example.com", role="editor")
project.get_members()
project.delete()

# List all projects
projects = client.projects().list()
for proj in projects.projects:
    print(f"{proj.name}: {proj.id}")
```

## 🧰 Agent Toolkits & Capabilities

> **📖 For complete toolkit documentation and advanced configurations, see [ToolKits.md](ToolKits.md)**

The ODIN SDK supports multiple specialized toolkits that extend agent capabilities. Each toolkit provides domain-specific tools for web search, code execution, database operations, financial analysis, and more.

### 1. Knowledge Base Agents

Perfect for document analysis, Q&A systems, and information retrieval:

```python
# Create knowledge base agent
kb_agent = project.agents.create(
    name="Document Analyst",
    personality="You are an expert document analyst who provides detailed insights.",
    building_blocks=[
        {
            "name": "knowledge_base",
            "project_id": project.id,
            "document_keys": [],
            "generate_inline_citations": True,
            "enforce_strict_adherence": False,
            "query_language": "English",
            "kb_search_results_to_return": 10,
            "max_context_size": 2500
        },
        {"name": "ai_model", "model": "GPT 4.1"},
        {"name": "agent_type", "agent_type": "tool_use_agent"},
        {
            "name": "toolkits",
            "toolkits": {
                "knowledge_base": {
                    "config": [{
                        "name": "Project Knowledge",
                        "project_id": project.id,
                        "description": "Access to project documents"
                    }]
                }
            }
        }
    ],
    temperature=0.1
)
```

### 2. Multi-Toolkit Research Agents

Combine web search, code execution, and financial analysis:

```python
# Create multi-toolkit agent
research_agent = project.agents.create(
    name="Research Agent",
    personality="""You are an intelligent research analyst with capabilities in:
    - Web research and fact-checking
    - Data analysis and visualization with Python
    - Financial market analysis using yfinance
    - Comprehensive report generation""",
    building_blocks=[
        {"name": "ai_model", "model": "claude-sonnet-4-20250514"},
        {"name": "agent_type", "agent_type": "tool_use_agent"},
        {
            "name": "toolkits",
            "toolkits": {
                "websearch": {"config": {}},
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
                },
                "yfinance": {"config": {}}
            }
        }
    ],
    temperature=0.5
)
```

### 3. SQL & Smart Tables Agents

For database operations and intelligent data querying:

```python
# Import CSV data first
import json

column_mappings = [
    {"sourceColumn": "id", "targetColumn": "id", "dataType": "number"},
    {"sourceColumn": "name", "targetColumn": "name", "dataType": "text"},
    {"sourceColumn": "price", "targetColumn": "price", "dataType": "number"}
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
    personality="You are a SQL expert who helps analyze data and answer business questions.",
    building_blocks=[
        {"name": "ai_model", "model": "GPT 4.1"},
        {"name": "agent_type", "agent_type": "tool_use_agent"},
        {
            "name": "toolkits",
            "toolkits": {
                "sql_database": {
                    "config": [{
                        "name": "Database Configuration",
                        "enabled_tools": [
                            "sql_db_query",
                            "sql_db_list_tables", 
                            "sql_db_schema",
                            "describe_table"
                        ],
                        "enable_all_smart_tables": True,
                        "block_type": "smart_table"
                    }],
                    "type": "sql_database"
                }
            }
        }
    ],
    temperature=0.0
)
```

## 💬 Chat Management

### Creating and Managing Conversations

```python
# Create chat session
chat = project.chats.create(
    name="Analysis Session",
    context="Analyze data and provide insights on business metrics"
)

# Send messages
response = chat.send_message(
    message="What are the top 5 products by revenue?",
    skip_stream=True
)

# Get chat details
chat_details = chat.get_details(prompt_debug=True)

# List all chats in project
chats = project.chats.list(limit=50)

# Delete chat
chat.delete()
```

## 📚 Knowledge Base Management

### File Upload and Management

```python
# Add PDF file
pdf_response = project.knowledge.add_file(
    file_path="./research_paper.pdf",
    metadata={"category": "research", "author": "Dr. Smith"},
    file_type="application/pdf",
    path="/documents/"
)

# Add multiple file types
documents = [
    ("./manual.pdf", "application/pdf"),
    ("./data.csv", "text/csv"), 
    ("./report.docx", "application/vnd.openxmlformats-officedocument.wordprocessingml.document")
]

for file_path, file_type in documents:
    project.knowledge.add_file(
        file_path=file_path,
        file_type=file_type,
        metadata={"upload_batch": "batch_001"}
    )
```

## 📊 Data Management & Smart Tables

### CSV Import and Data Operations

```python
# Define column mappings
mappings = [
    {"sourceColumn": "user_id", "targetColumn": "user_id", "dataType": "number"},
    {"sourceColumn": "username", "targetColumn": "username", "dataType": "text"},
    {"sourceColumn": "email", "targetColumn": "email", "dataType": "text"},
    {"sourceColumn": "created_at", "targetColumn": "created_at", "dataType": "text"},
    {"sourceColumn": "is_active", "targetColumn": "is_active", "dataType": "text"}
]

# Import table
import_result = project.data.import_table(
    title="users",
    description="User account data",
    file_path="./users.csv",
    column_mappings=json.dumps(mappings),
    delimiter=","
)

# Get table views
view_response = project.data.get_view(
    data_type_id=import_result.data_type_id
)

# Create custom views
view_config = {
    "name": "Active Users",
    "filter": "is_active = 'true'",
    "columns": ["username", "email", "created_at"]
}

custom_view = project.data.create_view(
    data_type_id=import_result.data_type_id,
    view_config=view_config
)
```

## 🔐 Authentication & Configuration

### Environment Setup

```python
import os
from odin_sdk.v3 import create_client

# Using environment variables (recommended)
client = create_client(
    api_key=os.getenv("ODIN_API_KEY"),
    api_secret=os.getenv("ODIN_API_SECRET"),
    host=os.getenv("ODIN_HOST", "https://api.example.com")
)

# Direct configuration
client = create_client(
    api_key="your-api-key-here",
    api_secret="your-api-secret-here", 
    host="https://your-odin-instance.com"
)
```

### Error Handling

```python
from odin_sdk.v3 import OdinError

try:
    project = client.projects().create(name="Test Project")
    agent = project.agents.create(name="Test Agent")
    agent.activate()
    
except OdinError as e:
    print(f"ODIN API Error: {e}")
    # Handle specific API errors
    
except Exception as e:
    print(f"Unexpected error: {e}")
    # Handle general errors
    
finally:
    # Cleanup resources
    if 'project' in locals():
        project.delete()
```

## 🎛️ Advanced Agent Configuration

> **📖 For complete building blocks documentation with all available options, see [Blocks.md](Blocks.md)**

Building blocks are modular components that define agent capabilities, behavior, and integrations. Each agent requires core blocks (agent type, AI model) and can include capability blocks (toolkits, knowledge base), behavior modifiers (rules, memory), and integration blocks (APIs, databases).

### Building Blocks Reference

```python
building_blocks = [
    # Knowledge Base Configuration
    {
        "name": "knowledge_base",
        "project_id": project.id,
        "document_keys": [],  # Specific documents or [] for all
        "enrich_sources": False,
        "generate_inline_citations": True,
        "enforce_strict_adherence": False,  # Set True for factual accuracy
        "query_language": "English",
        "translate_queries": False,
        "kb_search_results_to_return": 10,
        "kb_search_score_threshold": 0.0,
        "use_kb_cache": False,
        "max_context_size": 2500
    },
    
    # AI Model Selection
    {
        "name": "ai_model", 
        "model": "GPT 4.1"  # Options: "GPT 4.1", "claude-sonnet-4-20250514"
    },
    
    # Agent Type
    {
        "name": "agent_type",
        "agent_type": "tool_use_agent"  # Primary agent type for toolkit usage
    },
    
    # Toolkits Configuration
    {
        "name": "toolkits",
        "toolkits": {
            # Web Search
            "websearch": {"config": {}},
            
            # Python Code Execution
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
            },
            
            # Financial Data Analysis
            "yfinance": {"config": {}},
            
            # SQL Database Operations
            "sql_database": {
                "config": [{
                    "name": "Database Configuration",
                    "enabled_tools": [
                        "sql_db_query",
                        "sql_db_list_tables",
                        "sql_db_query_checker", 
                        "sql_db_schema",
                        "describe_table",
                        "list_tables"
                    ],
                    "enable_all_smart_tables": True,
                    "block_type": "smart_table"
                }],
                "type": "sql_database"
            },
            
            # Knowledge Base Tools
            "knowledge_base": {
                "config": [{
                    "name": "Project Knowledge",
                    "project_id": project.id,
                    "description": "Access to project documents and files"
                }]
            }
        }
    }
]
```

## 📚 Example Use Cases

### 1. Document Analysis Pipeline

```python
# Upload research documents
docs = ["paper1.pdf", "paper2.pdf", "report.docx"]
for doc in docs:
    project.knowledge.add_file(
        file_path=f"./documents/{doc}",
        metadata={"type": "research"},
        file_type="application/pdf" if doc.endswith('.pdf') else "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )

# Create analysis agent
analyst = project.agents.create(
    name="Research Analyst",
    personality="Expert at analyzing research papers and extracting key insights.",
    building_blocks=[
        {"name": "knowledge_base", "project_id": project.id, "generate_inline_citations": True},
        {"name": "ai_model", "model": "GPT 4.1"},
        {"name": "agent_type", "agent_type": "tool_use_agent"}
    ]
)

analyst.activate()

# Analyze documents
chat = project.chats.create(name="Document Analysis")
response = chat.send_message(
    "Compare the methodologies used in the uploaded research papers and identify common themes."
)
```

### 2. Financial Research Automation

```python
# Create financial research agent
finance_agent = project.agents.create(
    name="Financial Analyst",
    personality="Expert financial analyst specializing in market research and stock analysis.",
    building_blocks=[
        {"name": "ai_model", "model": "claude-sonnet-4-20250514"},
        {"name": "agent_type", "agent_type": "tool_use_agent"},
        {
            "name": "toolkits",
            "toolkits": {
                "websearch": {"config": {}},
                "yfinance": {"config": {}},
                "python": {"config": {"enabled_tools": ["execute_python"]}, "type": "python"}
            }
        }
    ],
    temperature=0.3
)

finance_agent.activate()

# Perform comprehensive analysis
analysis_chat = project.chats.create(name="Market Analysis")
response = analysis_chat.send_message("""
Perform a comprehensive analysis of Apple (AAPL) stock:
1. Get the latest stock data and news
2. Calculate technical indicators (RSI, moving averages)
3. Create visualizations of price trends
4. Provide investment recommendations based on the analysis
""")
```

### 3. Business Intelligence Dashboard

```python
# Import business data
sales_data = project.data.import_table(
    title="sales_data",
    description="Monthly sales data",
    file_path="./sales.csv",
    column_mappings=json.dumps([
        {"sourceColumn": "date", "targetColumn": "date", "dataType": "text"},
        {"sourceColumn": "product", "targetColumn": "product", "dataType": "text"},
        {"sourceColumn": "revenue", "targetColumn": "revenue", "dataType": "number"},
        {"sourceColumn": "units_sold", "targetColumn": "units_sold", "dataType": "number"}
    ])
)

# Create BI agent
bi_agent = project.agents.create(
    name="Business Intelligence Agent",
    personality="Expert business analyst who creates insights from data.",
    building_blocks=[
        {"name": "ai_model", "model": "GPT 4.1"},
        {"name": "agent_type", "agent_type": "tool_use_agent"},
        {
            "name": "toolkits",
            "toolkits": {
                "sql_database": {"config": [{"enable_all_smart_tables": True}], "type": "sql_database"},
                "python": {"config": {"enabled_tools": ["execute_python"]}, "type": "python"}
            }
        }
    ]
)

bi_agent.activate()

# Generate insights
insights_chat = project.chats.create(name="Business Insights")
response = insights_chat.send_message("""
Analyze the sales data and provide:
1. Monthly revenue trends
2. Top performing products
3. Sales forecasts for next quarter
4. Visual charts showing key metrics
""")
```

## 📚 Documentation Structure

The ODIN SDK v3 provides comprehensive documentation across multiple files:

### Core Documentation
- **[README.md](README.md)** *(this file)* - Main SDK guide with quick start, examples, and common usage patterns
- **[Blocks.md](Blocks.md)** - Complete building blocks reference with all configuration options
- **[ToolKits.md](ToolKits.md)** - Detailed toolkit documentation with specific tools and capabilities

### How They Work Together

1. **Start Here**: Use this README for initial setup, basic concepts, and common examples
2. **Customize Agents**: Reference [Blocks.md](Blocks.md) for detailed building block configurations:
   - Core blocks: `agent_type`, `ai_model`
   - Capability blocks: `knowledge_base`, `toolkits`
   - Behavior blocks: `rules`, `memory`, `information_extraction`
   - Integration blocks: `api`, `salesforce`, `shopify`

3. **Add Functionality**: Reference [ToolKits.md](ToolKits.md) for specific toolkit implementations:
   - `websearch` - Web search and content retrieval
   - `python` - Code execution and data analysis
   - `sql_database` - Database operations and smart tables
   - `yfinance` - Financial data and market analysis

### Quick Navigation

```python
# Basic agent (covered in README.md)
agent = project.agents.create(
    name="Basic Agent",
    building_blocks=[
        {"name": "agent_type", "agent_type": "tool_use_agent"},
        {"name": "ai_model", "model": "GPT 4.1"}
    ]
)

# Advanced configuration (see Blocks.md for all options)
agent = project.agents.create(
    name="Advanced Agent",
    building_blocks=[
        {"name": "agent_type", "agent_type": "tool_use_agent"},
        {"name": "ai_model", "model": "claude-sonnet-4-20250514"},
        {
            "name": "toolkits",  # See ToolKits.md for complete toolkit reference
            "toolkits": {
                "websearch": {"config": {}},
                "python": {"config": {"enabled_tools": ["execute_python"]}, "type": "python"}
            }
        },
        {
            "name": "knowledge_base",  # See Blocks.md for all knowledge_base options
            "project_id": project.id,
            "generate_inline_citations": True
        }
    ]
)
```

## 🧪 Testing & Development

### Running Examples

The SDK includes comprehensive examples demonstrating various capabilities:

```bash
# Clone the repository and navigate to examples
cd examples

# Knowledge Base Agent Demo
python kb_agent_end_to_end_v3.py

# Multi-Toolkit Agent Demo  
python multi_toolkit_agent_end_to_end_v3.py

# Smart Tables/SQL Demo
python smart_tables_agent_end_to_end_v3.py
```

## 🚧 Migration from v2

The v3 SDK is fully backward compatible with v2, but offers enhanced convenience:

### v2 vs v3 Comparison

```python
# v2 Style (still works in v3)
project_response = client.projects().create(name="My Project")
project_id = project_response.project.id  # Nested attribute access
client.projects().delete(project_id)      # Manual ID management

# v3 Enhanced Style (recommended)
project = client.projects().create(name="My Project")
project_id = project.id                   # Flattened attribute access
project.delete()                          # Convenience method

# v2 Style
agent_response = client.agents().create(project_id, name="Agent")
client.agents().activate(project_id, agent_response.agent_id)

# v3 Enhanced Style  
agent = project.agents.create(name="Agent")  # Project-scoped manager
agent.activate()                             # Self-aware resource
```

### Development Setup

```bash
git clone https://github.com/your-org/odin-sdk
cd odin-sdk
pip install -e ".[dev]"
python -m pytest tests/
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support & Resources

### Documentation
- 📖 **API Documentation**: [https://api.getodin.ai/docs](https://api.getodin.ai/docs)
- 🧩 **Building Blocks Reference**: [Blocks.md](Blocks.md) - Complete configuration guide
- 🧰 **Toolkits Reference**: [ToolKits.md](ToolKits.md) - All available toolkits and tools
- 🚀 **SDK Guide**: [README.md](README.md) - This comprehensive guide

### Community & Support
- 💬 **Website**: [https://getodin.ai](https://getodin.ai)
- 📧 **Support**: Contact our team for enterprise support and custom integrations


---

**Built with ❤️ by the ODIN AI Team**
