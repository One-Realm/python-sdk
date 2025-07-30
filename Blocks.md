# 🧩 ODIN SDK Building Blocks - Complete Reference Guide

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![ODIN SDK v3](https://img.shields.io/badge/ODIN%20SDK-v3-green.svg)](https://github.com/One-Realm/python-sdk)

**Building Blocks** are modular components that define agent capabilities, behavior, and integrations in the ODIN SDK. Each block extends specific functionality, from core system settings to advanced integrations and specialized behaviors.

## 📋 Overview

Building blocks are the fundamental components that compose an AI agent:
- **Core Blocks**: Essential configuration (agent type, AI model)
- **Capability Blocks**: Add functionality (knowledge base, toolkits)
- **Behavior Blocks**: Modify agent behavior (rules, memory, responses)
- **Integration Blocks**: Connect external systems (APIs, databases, services)

### Block Architecture

```python
# Every agent requires building_blocks array
building_blocks = [
    {"name": "agent_type", "agent_type": "tool_use_agent"},  # Required
    {"name": "ai_model", "model": "GPT 4.1"},               # Required
    # Additional blocks extend functionality...
]

agent = project.agents.create(
    name="My Agent",
    personality="You are a helpful assistant.",
    building_blocks=building_blocks
)
```

## 📚 Complete Building Blocks Inventory

### **Core System Blocks** (Required)
| Block | Purpose | Required |
|-------|---------|----------|
| [`agent_type`](#agent_type---agent-type-specification) | Defines agent behavior type | ✅ Yes |
| [`ai_model`](#ai_model---ai-model-configuration) | AI model selection and configuration | ✅ Yes |

### **Capability Blocks** (Add Functionality)
| Block | Purpose | Agent Types |
|-------|---------|-------------|
| [`toolkits`](#toolkits---toolkit-integration) | Multi-toolkit functionality | `tool_use_agent` |
| [`knowledge_base`](#knowledge_base---core-knowledge-base) | Document search and retrieval | All |
| [`enhanced_search`](#enhanced_search---advanced-multi-llm-search) | Advanced search with multiple LLM calls | All |
| [`google_search`](#google_search---google-search-integration) | Google search capabilities | All |

### **Data & Database Blocks**
| Block | Purpose | Agent Types |
|-------|---------|-------------|
| [`sql_block`](#sql_block---sql-database-agent) | SQL database operations | `sql_agent` |
| [`smart_table_block`](#smart_table_block---smart-tables-agent) | Smart tables operations | `smart_table_agent` |
| [`data_agent_block`](#data_agent_block---csv-data-agent) | CSV data analysis | `data_agent` |

### **Integration Blocks** (External Systems)
| Block | Purpose | Use Cases |
|-------|---------|-----------|
| [`api`](#api---generic-api-integration) | Generic API integration | REST APIs, webhooks |
| [`salesforce`](#salesforce---salesforce-integration) | Salesforce CRM integration | Sales, customer management |
| [`shopify`](#shopify---shopify-integration) | E-commerce operations | Order management, inventory |
| [`automator_action`](#automator_action---automation-actions) | Workflow automation | Business process automation |
| [`meetingmate`](#meetingmate---meeting-management) | Meeting management | Calendar integration |

### **Behavior Modifier Blocks**
| Block | Purpose | Impact |
|-------|---------|--------|
| [`rules`](#rules---custom-agent-rules) | Custom behavioral rules | Response guidelines |
| [`information_extraction`](#information_extraction---structured-extraction) | Extract structured data | Data parsing |
| [`use_json_response`](#use_json_response---force-json-format) | Force JSON output format | Response structure |
| [`user_recognition`](#user_recognition---user-personalization) | User personalization | Context awareness |
| [`long_term_memory`](#long_term_memory---long-term-memory) | Persistent memory | Conversation continuity |
| [`ignore_chat_history`](#ignore_chat_history---disable-chat-history) | Disable chat history | Fresh context per message |

### **Specialized Blocks**
| Block | Purpose | Use Cases |
|-------|---------|-----------|
| [`dalle3`](#dalle3---dall-e-3-image-generation) | Image generation | Creative content, visualizations |
| [`document_filtering`](#document_filtering---filter-by-metadata) | Document metadata filtering | Content targeting |

---

# 🔧 Core System Blocks

## `agent_type` - Agent Type Specification

**Purpose**: Defines the fundamental behavior and capabilities of the agent.

### Schema
```python
{
    "name": "agent_type",
    "agent_type": "tool_use_agent"  # Required
}
```

### Available Agent Types

| Type | Description | Capabilities | Best For |
|------|-------------|--------------|----------|
| `tool_use_agent` | Multi-toolkit agent with advanced tools | Toolkits, external APIs, complex workflows | Research, analysis, automation |
| `chat_agent` | Basic conversational agent | Knowledge base, simple responses | Q&A, customer support |
| `sql_agent` | Database-focused agent | SQL operations, data analysis | Business intelligence, reporting |
| `smart_table_agent` | Smart tables specialist | CSV analysis, data manipulation | Data science, spreadsheet tasks |
| `data_agent` | CSV data analyst | File-based data operations | Data processing, analytics |
| `document_agent` | Document processing specialist | Document generation, editing | Content creation, document workflows |

### SDK Usage Example
```python
# Tool-use agent (most common)
agent = project.agents.create(
    name="Research Assistant",
    building_blocks=[
        {"name": "agent_type", "agent_type": "tool_use_agent"},
        {"name": "ai_model", "model": "claude-sonnet-4-20250514"},
        {
            "name": "toolkits",
            "toolkits": {
                "websearch": {"config": {}},
                "python": {"config": {"enabled_tools": ["execute_python"]}, "type": "python"}
            }
        }
    ]
)

# SQL agent for data analysis
sql_agent = project.agents.create(
    name="Data Analyst",
    building_blocks=[
        {"name": "agent_type", "agent_type": "sql_agent"},
        {"name": "ai_model", "model": "GPT 4.1"},
        {
            "name": "sql_block",
            "connection_type": "postgresql",
            "connection_id": "your_db_connection_id"
        }
    ]
)
```

---

## `ai_model` - AI Model Configuration

**Purpose**: Specifies which AI model to use and its configuration parameters.

### Schema

#### Standard Models
```python
{
    "name": "ai_model",
    "model": "GPT 4.1",  # Model display name
    "id": "gpt-4"        # Optional: Model identifier
}
```

#### Custom Models
```python
{
    "name": "ai_model",
    "model": "Custom Model",
    "id": "custom-model-id",
    "api_type": "openai",           # openai, anthropic, google_ai, etc.
    "api_key": "your-api-key",
    "api_url": "https://api.custom.com/v1",
    "max_response_tokens": 2000,
    "max_input_tokens": 8000,
    "api_version": "2023-05-15",
    "model_extra_params": {
        "temperature": 0.7,
        "top_p": 0.9
    }
}
```

### Available Models

| Model | Identifier | Best For | Capabilities |
|-------|------------|----------|--------------|
| **GPT 4.1** | `gpt-4` | General tasks, analysis | Excellent reasoning, code, analysis |
| **Claude Sonnet 4** | `claude-sonnet-4-20250514` | Complex reasoning, research | Advanced analysis, tool use |
| **GPT 4o Mini** | `gpt-4o-mini` | Fast responses, simple tasks | Quick responses, cost-effective |
| **Claude 2** | `claude-2` | Long content, creative tasks | Large context, creative writing |

### SDK Usage Example
```python
# Standard model selection
agent = project.agents.create(
    name="Analysis Agent",
    building_blocks=[
        {"name": "ai_model", "model": "claude-sonnet-4-20250514"},
        {"name": "agent_type", "agent_type": "tool_use_agent"}
    ],
    temperature=0.3  # Can also control temperature at agent level
)

# Custom model configuration
custom_agent = project.agents.create(
    name="Custom Model Agent",
    building_blocks=[
        {
            "name": "ai_model",
            "model": "Custom GPT",
            "api_type": "openai",
            "api_key": os.getenv("CUSTOM_API_KEY"),
            "api_url": "https://api.custom-provider.com/v1",
            "max_response_tokens": 1500
        },
        {"name": "agent_type", "agent_type": "tool_use_agent"}
    ]
)
```

---

# 🧰 Capability Blocks

## `toolkits` - Toolkit Integration

**Purpose**: Enables multi-toolkit functionality for `tool_use_agent` types. See [ToolKits.md](ToolKits.md) for complete toolkit documentation.

### Schema
```python
{
    "name": "toolkits",
    "toolkits": {
        "websearch": {"config": {}},
        "python": {"config": {"enabled_tools": ["execute_python"]}, "type": "python"},
        "knowledge_base": {
            "config": [{"project_id": "proj_id", "name": "KB", "description": "Knowledge base"}]
        }
    }
}
```

### SDK Usage Example
```python
# Multi-toolkit research agent
agent = project.agents.create(
    name="Research Agent",
    building_blocks=[
        {"name": "agent_type", "agent_type": "tool_use_agent"},
        {"name": "ai_model", "model": "claude-sonnet-4-20250514"},
        {
            "name": "toolkits",
            "toolkits": {
                "websearch": {"config": {}},
                "python": {
                    "config": {
                        "enabled_tools": ["execute_python", "upload_file_to_sandbox"]
                    },
                    "type": "python"
                },
                "yfinance": {"config": {}}
            }
        }
    ]
)
```

---

## `knowledge_base` - Core Knowledge Base

**Purpose**: Provides document search and retrieval capabilities from uploaded files.

### Schema
```python
{
    "name": "knowledge_base",
    "project_id": "your_project_id",
    "document_keys": [],  # Specific documents or [] for all
    "enforce_strict_adherence": False,
    "generate_inline_citations": True,
    "enrich_sources": False,
    "query_language": "English",
    "translate_queries": False,
    "filter_link_exceptions": ["domain.com"],
    "additional_kb_ids": ["other_project_id"],
    "kb_search_results_to_return": 10,
    "kb_search_score_threshold": 0.7,
    "extra_strict_adherence_test_rules": ["rule1"],
    "extra_strict_adherence_failure_response_rules": ["response1"],
    "use_kb_cache": False,
    "cache_threshold": 0.6,
    "max_context_size": 2500,
    "should_enrich": True,
    "use_whole_document": False
}
```

### Key Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `project_id` | string | Target project for knowledge base | Required |
| `document_keys` | array | Specific documents to search; empty = all | `[]` |
| `generate_inline_citations` | boolean | Include source citations in responses | `true` |
| `enforce_strict_adherence` | boolean | Only answer from knowledge base | `false` |
| `kb_search_results_to_return` | number | Number of search results to return | `10` |
| `max_context_size` | number | Maximum context size in tokens | `2500` |

### SDK Usage Example
```python
# Upload documents first
project.knowledge.add_file(
    file_path="./research_paper.pdf",
    metadata={"category": "research"},
    file_type="application/pdf"
)

# Create knowledge base agent
kb_agent = project.agents.create(
    name="Document Expert",
    personality="You are an expert at analyzing documents and providing detailed insights with proper citations.",
    building_blocks=[
        {
            "name": "knowledge_base",
            "project_id": project.id,
            "document_keys": [],  # Search all documents
            "generate_inline_citations": True,
            "enforce_strict_adherence": False,
            "kb_search_results_to_return": 15,
            "max_context_size": 3000
        },
        {"name": "ai_model", "model": "GPT 4.1"},
        {"name": "agent_type", "agent_type": "tool_use_agent"}
    ]
)

kb_agent.activate()
chat = project.chats.create(name="Document Analysis")

response = chat.send_message(
    "What are the key findings in the uploaded research paper?",
    skip_stream=True
)
```

---

## `enhanced_search` - Advanced Multi-LLM Search

**Purpose**: Provides advanced search capabilities using multiple LLM calls to refine and improve search results.

### Schema
```python
{
    "name": "enhanced_search",
    "answered_rules": ["Say 'thank you' when question is resolved"],
    "group_on_backend": False,
    "query_language": "English",
    "translate_queries": False,
    "allow_result_length_trimming": True,
    "extra_ranking_rules": ["custom_ranking_rule"]
}
```

### Key Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `answered_rules` | array | Rules for when user indicates satisfaction |
| `group_on_backend` | boolean | Group search results by source |
| `allow_result_length_trimming` | boolean | Allow trimming of long results |
| `extra_ranking_rules` | array | Custom ranking rules for results |

### SDK Usage Example
```python
# Enhanced search agent
enhanced_agent = project.agents.create(
    name="Advanced Search Agent",
    building_blocks=[
        {
            "name": "enhanced_search",
            "answered_rules": [
                "Thank the user when they indicate their question is answered",
                "Offer to help with follow-up questions"
            ],
            "group_on_backend": True,
            "allow_result_length_trimming": True
        },
        {"name": "ai_model", "model": "claude-sonnet-4-20250514"},
        {"name": "agent_type", "agent_type": "tool_use_agent"}
    ]
)
```

---

# 🗄️ Data & Database Blocks

## `sql_block` - SQL Database Agent

**Purpose**: Enables SQL database operations for `sql_agent` type agents.

### Schema
```python
{
    "name": "sql_block",
    "connection_type": "postgresql",  # postgresql, mysql, snowflake, etc.
    "connection_id": "db_connection_id",
    "helper_prompt": "Additional SQL context and instructions",
    "generate_response": True
}
```

### SDK Usage Example
```python
# SQL database agent
sql_agent = project.agents.create(
    name="Database Analyst",
    personality="You are a SQL expert who writes efficient queries and explains data insights.",
    building_blocks=[
        {"name": "agent_type", "agent_type": "sql_agent"},
        {"name": "ai_model", "model": "GPT 4.1"},
        {
            "name": "sql_block",
            "connection_type": "postgresql",
            "connection_id": "prod_db_connection",
            "helper_prompt": "Always use proper indexing and explain query performance.",
            "generate_response": True
        }
    ]
)
```

---

## `smart_table_block` - Smart Tables Agent

**Purpose**: Enables operations on smart tables (imported CSV data) for `smart_table_agent` type agents.

### Schema
```python
{
    "name": "smart_table_block",
    "table_ids": ["table1_id", "table2_id"],
    "helper_prompt": "Smart table analysis context",
    "generate_response": True
}
```

### SDK Usage Example
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
    description="Product data",
    file_path="./products.csv",
    column_mappings=json.dumps(column_mappings)
)

# Create smart table agent
smart_agent = project.agents.create(
    name="Data Table Analyst",
    building_blocks=[
        {"name": "agent_type", "agent_type": "smart_table_agent"},
        {"name": "ai_model", "model": "GPT 4.1"},
        {
            "name": "smart_table_block",
            "table_ids": [table_import.data_type_id],
            "helper_prompt": "Focus on finding patterns and trends in the product data.",
            "generate_response": True
        }
    ]
)
```

---

## `data_agent_block` - CSV Data Agent

**Purpose**: Enables CSV file analysis for `data_agent` type agents.

### Schema
```python
{
    "name": "data_agent_block",
    "csv_name": "primary_file.csv",      # Legacy: single file
    "csv_names": ["file1.csv", "file2.csv"],  # Modern: multiple files
    "helper_prompt": "Data analysis context and instructions",
    "generate_response": True
}
```

### SDK Usage Example
```python
# Upload CSV files to knowledge base first
project.knowledge.add_file(
    file_path="./sales_data.csv",
    file_type="text/csv",
    metadata={"type": "sales_data"}
)

# Create data agent
data_agent = project.agents.create(
    name="CSV Data Analyst",
    building_blocks=[
        {"name": "agent_type", "agent_type": "data_agent"},
        {"name": "ai_model", "model": "GPT 4.1"},
        {
            "name": "data_agent_block",
            "csv_names": ["sales_data.csv"],
            "helper_prompt": "Analyze sales trends and provide business insights.",
            "generate_response": True
        }
    ]
)
```

---

# 🔗 Integration Blocks

## `api` - Generic API Integration

**Purpose**: Integrates with external REST APIs and webhooks for custom functionality.

### Schema
```python
{
    "name": "api",
    "alias": "MyAPI",
    "root_url": "https://api.example.com/",
    "endpoints": [
        {
            "path": "v1/users/{user_id}",
            "method": "GET",
            "required_information": ["user_id"],
            "optional_information": ["include_profile"],
            "required_information_for_path": ["user_id"],
            "pass_params_as": "query",  # or "body", "header"
            "authentication_required": True,
            "route_name": "get_user",
            "route_display_name": "Get User Details",
            "description": "Retrieves user information by ID",
            "response_format": "json"
        }
    ],
    "authentication": {
        "type": "header",  # or "body"
        "auth_keys": {"Authorization": "Bearer {token}"},
        "auth_root_url": "https://auth.example.com/",     # Optional
        "auth_endpoint": "oauth/token",                    # Optional
        "auth_method": "POST",                             # Optional
        "auth_token_key_name": "access_token",             # Optional
        "auth_token_authentication_key_name": "Authorization", # Optional
        "auth_token_authentication_type": "header"        # Optional
    }
}
```

### SDK Usage Example
```python
# API integration agent
api_agent = project.agents.create(
    name="CRM Integration Agent",
    building_blocks=[
        {"name": "agent_type", "agent_type": "tool_use_agent"},
        {"name": "ai_model", "model": "GPT 4.1"},
        {
            "name": "api",
            "alias": "CRM API",
            "root_url": "https://api.crm-system.com/",
            "endpoints": [
                {
                    "path": "v1/contacts",
                    "method": "GET",
                    "required_information": [],
                    "optional_information": ["limit", "offset"],
                    "pass_params_as": "query",
                    "authentication_required": True,
                    "route_name": "list_contacts",
                    "route_display_name": "List All Contacts",
                    "description": "Retrieve all contacts from CRM",
                    "response_format": "json"
                }
            ],
            "authentication": {
                "type": "header",
                "auth_keys": {"Authorization": "Bearer YOUR_API_TOKEN"}
            }
        }
    ]
)
```

---

## `salesforce` - Salesforce Integration

**Purpose**: Integrates with Salesforce CRM for sales and customer management operations.

### Schema
```python
{
    "name": "salesforce",
    "salesforce_instance_url": "https://company.salesforce.com"
}
```

### SDK Usage Example
```python
# Salesforce integration agent
sf_agent = project.agents.create(
    name="Salesforce Assistant",
    personality="You are a Salesforce expert who helps manage leads, opportunities, and accounts.",
    building_blocks=[
        {"name": "agent_type", "agent_type": "tool_use_agent"},
        {"name": "ai_model", "model": "GPT 4.1"},
        {
            "name": "salesforce",
            "salesforce_instance_url": "https://mycompany.salesforce.com"
        }
    ]
)

sf_agent.activate()
chat = project.chats.create(name="Salesforce Operations")

response = chat.send_message(
    "Show me all open opportunities for accounts starting with 'Tech'",
    skip_stream=True
)
```

---

## `shopify` - Shopify Integration

**Purpose**: Integrates with Shopify for e-commerce operations including orders, inventory, and customer management.

### Schema
```python
{
    "name": "shopify",
    "shop_name": "my-store.myshopify.com",
    "permitted_actions": {
        "view_orders": True,
        "create_refund": True,
        "update_inventory": False,
        "view_customers": True,
        "create_order": False
    },
    "refund_shipping": True
}
```

### SDK Usage Example
```python
# Shopify e-commerce agent
shopify_agent = project.agents.create(
    name="E-commerce Assistant",
    building_blocks=[
        {"name": "agent_type", "agent_type": "tool_use_agent"},
        {"name": "ai_model", "model": "GPT 4.1"},
        {
            "name": "shopify",
            "shop_name": "mystore.myshopify.com",
            "permitted_actions": {
                "view_orders": True,
                "create_refund": True,
                "update_inventory": True,
                "view_customers": True
            },
            "refund_shipping": True
        }
    ]
)
```

---

# 🎛️ Behavior Modifier Blocks

## `rules` - Custom Agent Rules

**Purpose**: Defines custom behavioral rules and guidelines for agent responses.

### Schema
```python
{
    "name": "rules",
    "rules": [
        "Always be polite and professional",
        "Never share sensitive information",
        "Ask for confirmation before making changes",
        "Provide sources for factual claims"
    ]
}
```

### SDK Usage Example
```python
# Rule-based agent
rule_agent = project.agents.create(
    name="Corporate Assistant",
    building_blocks=[
        {"name": "agent_type", "agent_type": "tool_use_agent"},
        {"name": "ai_model", "model": "GPT 4.1"},
        {
            "name": "rules",
            "rules": [
                "Always maintain professional tone",
                "Never disclose internal company information",
                "Ask for approval before contacting external parties",
                "Include disclaimers for financial advice",
                "Verify user identity for sensitive requests"
            ]
        }
    ]
)
```

---

## `information_extraction` - Structured Information Extraction

**Purpose**: Extracts structured information from conversations and presents it in a defined format.

### Schema
```python
{
    "name": "information_extraction",
    "project_id": "project_id",
    "information_to_extract": [
        {
            "key": "customer_name",
            "description": "Customer's full name",
            "type": "string",
            "required": True
        },
        {
            "key": "order_amount",
            "description": "Total order value in USD",
            "type": "number",
            "required": False
        },
        {
            "key": "product_category",
            "description": "Main product category",
            "type": "string",
            "required": True
        }
    ],
    "extract_rules": [
        "Extract only explicitly mentioned information",
        "Use null for missing required fields",
        "Convert currency to USD if different currency mentioned"
    ]
}
```

### SDK Usage Example
```python
# Information extraction agent
extraction_agent = project.agents.create(
    name="Data Extraction Agent",
    building_blocks=[
        {"name": "agent_type", "agent_type": "tool_use_agent"},
        {"name": "ai_model", "model": "GPT 4.1"},
        {
            "name": "information_extraction",
            "project_id": project.id,
            "information_to_extract": [
                {
                    "key": "customer_email",
                    "description": "Customer email address",
                    "type": "string",
                    "required": True
                },
                {
                    "key": "issue_category",
                    "description": "Type of customer issue",
                    "type": "string",
                    "required": True
                },
                {
                    "key": "urgency_level",
                    "description": "Issue urgency (low, medium, high, critical)",
                    "type": "string",
                    "required": False
                }
            ],
            "extract_rules": [
                "Only extract information explicitly stated by the user",
                "Classify urgency based on keywords like 'urgent', 'asap', 'critical'",
                "Use lowercase for issue categories"
            ]
        }
    ]
)
```

---

## `use_json_response` - Force JSON Response Format

**Purpose**: Forces the agent to respond in structured JSON format using predefined templates.

### Schema
```python
{
    "name": "use_json_response",
    "use_json_response": True,
    "json_id": "response_template_id"  # References a JSON template
}
```

### SDK Usage Example
```python
# JSON response agent
json_agent = project.agents.create(
    name="Structured Response Agent",
    building_blocks=[
        {"name": "agent_type", "agent_type": "tool_use_agent"},
        {"name": "ai_model", "model": "GPT 4.1"},
        {
            "name": "use_json_response",
            "use_json_response": True,
            "json_id": "customer_support_template"
        }
    ]
)

# Agent will respond in structured JSON format
chat = project.chats.create(name="Structured Support")
response = chat.send_message("I need help with my order", skip_stream=True)
# Response will be in JSON format matching the template
```

---

## `user_recognition` - User Personalization

**Purpose**: Enables user recognition and personalization based on user context and history.

### Schema
```python
{
    "name": "user_recognition"
    # Configuration is auto-populated based on user context
}
```

### SDK Usage Example
```python
# Personalized agent
personal_agent = project.agents.create(
    name="Personal Assistant",
    personality="You are a personal assistant who remembers user preferences and provides tailored responses.",
    building_blocks=[
        {"name": "agent_type", "agent_type": "tool_use_agent"},
        {"name": "ai_model", "model": "GPT 4.1"},
        {"name": "user_recognition"}  # Auto-configured
    ]
)
```

---

## `long_term_memory` - Long-term Memory

**Purpose**: Enables persistent memory across chat sessions (requires Knowledge Base v2+).

### Schema
```python
{
    "name": "long_term_memory",
    "use_long_term_memory": True
}
```

### SDK Usage Example
```python
# Memory-enabled agent
memory_agent = project.agents.create(
    name="Persistent Memory Agent",
    building_blocks=[
        {"name": "agent_type", "agent_type": "tool_use_agent"},
        {"name": "ai_model", "model": "GPT 4.1"},
        {
            "name": "long_term_memory",
            "use_long_term_memory": True
        }
    ]
)

# Agent will remember context across different chat sessions
```

---

## `ignore_chat_history` - Disable Chat History

**Purpose**: Disables chat history, treating each message as independent.

### Schema
```python
{
    "name": "ignore_chat_history",
    "ignore_chat_history": True
}
```

### SDK Usage Example
```python
# Stateless agent
stateless_agent = project.agents.create(
    name="Independent Response Agent",
    building_blocks=[
        {"name": "agent_type", "agent_type": "tool_use_agent"},
        {"name": "ai_model", "model": "GPT 4.1"},
        {
            "name": "ignore_chat_history",
            "ignore_chat_history": True
        }
    ]
)
```

---

# 🎨 Specialized Blocks

## `dalle3` - DALL-E 3 Image Generation

**Purpose**: Enables AI image generation using DALL-E 3.

### Schema
```python
{
    "name": "dalle3",
    "project_id": "project_id"
}
```

### SDK Usage Example
```python
# Image generation agent
image_agent = project.agents.create(
    name="Creative Image Generator",
    personality="You are a creative assistant who can generate images based on descriptions.",
    building_blocks=[
        {"name": "agent_type", "agent_type": "tool_use_agent"},
        {"name": "ai_model", "model": "GPT 4.1"},
        {
            "name": "dalle3",
            "project_id": project.id
        }
    ]
)

image_agent.activate()
chat = project.chats.create(name="Image Creation")

response = chat.send_message(
    "Generate an image of a futuristic city skyline at sunset",
    skip_stream=True
)
```

---

## `document_filtering` - Filter Documents by Metadata

**Purpose**: Filters knowledge base documents based on metadata criteria.

### Schema
```python
{
    "name": "document_filtering",
    "data_type_id": "doc_type_id",
    "metadata": {
        "category": "technical",
        "version": "latest",
        "department": "engineering"
    },
    "data_type_ids_to_metadatas": {
        "type1": {"filter": "value1"},
        "type2": {"filter": "value2"}
    }
}
```

### SDK Usage Example
```python
# Upload documents with metadata
project.knowledge.add_file(
    file_path="./tech_manual.pdf",
    metadata={"category": "technical", "department": "engineering", "version": "2024"},
    file_type="application/pdf"
)

# Document filtering agent
filtered_agent = project.agents.create(
    name="Technical Documentation Agent",
    building_blocks=[
        {"name": "agent_type", "agent_type": "tool_use_agent"},
        {"name": "ai_model", "model": "GPT 4.1"},
        {
            "name": "document_filtering",
            "metadata": {
                "category": "technical",
                "department": "engineering"
            }
        },
        {
            "name": "knowledge_base",
            "project_id": project.id,
            "generate_inline_citations": True
        }
    ]
)
```

---

# 🔧 Advanced Usage Patterns

## Multi-Block Complex Agent

```python
# Comprehensive enterprise agent
enterprise_agent = project.agents.create(
    name="Enterprise AI Assistant",
    personality="""You are an enterprise AI assistant with comprehensive capabilities:
    - Access to company knowledge base and documentation
    - Integration with Salesforce CRM
    - Data analysis capabilities with Python and SQL
    - Web research for current information
    - Strict adherence to company policies and security rules""",
    building_blocks=[
        # Core configuration
        {"name": "agent_type", "agent_type": "tool_use_agent"},
        {"name": "ai_model", "model": "claude-sonnet-4-20250514"},
        
        # Knowledge and memory
        {
            "name": "knowledge_base",
            "project_id": project.id,
            "generate_inline_citations": True,
            "enforce_strict_adherence": False,
            "kb_search_results_to_return": 15
        },
        {
            "name": "long_term_memory",
            "use_long_term_memory": True
        },
        
        # Behavioral rules
        {
            "name": "rules",
            "rules": [
                "Always verify user identity for sensitive operations",
                "Include source citations for all factual claims",
                "Ask for confirmation before making external API calls",
                "Maintain professional tone in all communications",
                "Escalate security concerns to administrators"
            ]
        },
        
        # Information extraction
        {
            "name": "information_extraction",
            "project_id": project.id,
            "information_to_extract": [
                {"key": "user_department", "description": "User's department", "type": "string", "required": False},
                {"key": "request_type", "description": "Type of user request", "type": "string", "required": True},
                {"key": "priority_level", "description": "Request priority", "type": "string", "required": False}
            ],
            "extract_rules": ["Classify requests by department and priority"]
        },
        
        # External integrations
        {
            "name": "salesforce",
            "salesforce_instance_url": "https://company.salesforce.com"
        },
        
        # Multi-toolkit capabilities
        {
            "name": "toolkits",
            "toolkits": {
                "websearch": {"config": {}},
                "python": {
                    "config": {"enabled_tools": ["execute_python", "upload_file_to_sandbox"]},
                    "type": "python"
                },
                "sql_database": {
                    "config": [{"enable_all_smart_tables": True}],
                    "type": "sql_database"
                },
                "knowledge_base": {
                    "config": [{
                        "project_id": project.id,
                        "name": "Enterprise Knowledge",
                        "description": "Company documentation and policies"
                    }]
                }
            }
        }
    ],
    temperature=0.3
)
```

## Conditional Block Usage

```python
# Function to create different agent types based on use case
def create_specialized_agent(project, agent_type_name, use_case):
    base_blocks = [
        {"name": "agent_type", "agent_type": "tool_use_agent"},
        {"name": "ai_model", "model": "GPT 4.1"}
    ]
    
    if use_case == "research":
        specialized_blocks = [
            {
                "name": "toolkits",
                "toolkits": {
                    "websearch": {"config": {}},
                    "python": {"config": {"enabled_tools": ["execute_python"]}, "type": "python"}
                }
            }
        ]
    elif use_case == "customer_support":
        specialized_blocks = [
            {
                "name": "knowledge_base",
                "project_id": project.id,
                "generate_inline_citations": True
            },
            {
                "name": "rules",
                "rules": ["Always be helpful and polite", "Escalate complex issues to human agents"]
            }
        ]
    elif use_case == "data_analysis":
        specialized_blocks = [
            {
                "name": "toolkits",
                "toolkits": {
                    "python": {"config": {"enabled_tools": ["execute_python"]}, "type": "python"},
                    "sql_database": {"config": [{"enable_all_smart_tables": True}], "type": "sql_database"}
                }
            }
        ]
    
    return project.agents.create(
        name=agent_type_name,
        building_blocks=base_blocks + specialized_blocks
    )

# Usage
research_agent = create_specialized_agent(project, "Research Agent", "research")
support_agent = create_specialized_agent(project, "Support Agent", "customer_support")
data_agent = create_specialized_agent(project, "Data Agent", "data_analysis")
```

## Error Handling and Validation

```python
from odin_sdk.v3 import OdinError

def create_agent_with_validation(project, config):
    try:
        # Validate required blocks
        required_blocks = ["agent_type", "ai_model"]
        block_names = [block["name"] for block in config["building_blocks"]]
        
        for required in required_blocks:
            if required not in block_names:
                raise ValueError(f"Missing required block: {required}")
        
        # Create agent
        agent = project.agents.create(
            name=config["name"],
            personality=config.get("personality", "You are a helpful assistant."),
            building_blocks=config["building_blocks"],
            temperature=config.get("temperature", 0.6)
        )
        
        # Activate with error handling
        try:
            agent.activate()
            return agent
        except OdinError as e:
            print(f"Failed to activate agent: {e}")
            return None
            
    except OdinError as e:
        print(f"Failed to create agent: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

# Usage with error handling
agent_config = {
    "name": "Test Agent",
    "building_blocks": [
        {"name": "agent_type", "agent_type": "tool_use_agent"},
        {"name": "ai_model", "model": "GPT 4.1"}
    ]
}

agent = create_agent_with_validation(project, agent_config)
if agent:
    print("Agent created and activated successfully")
else:
    print("Failed to create agent")
```

## 📚 Best Practices

### 1. Block Selection Guidelines

- **Start Simple**: Begin with core blocks (`agent_type`, `ai_model`) and add functionality incrementally
- **Purpose-Driven**: Choose blocks based on specific use cases and requirements
- **Performance**: More blocks = more complexity = potentially slower responses

### 2. Configuration Tips

- **Validation**: Always validate required parameters before agent creation
- **Testing**: Test agents with simple configurations before adding complex blocks
- **Documentation**: Document custom configurations for team sharing

### 3. Common Patterns

```python
# Pattern 1: Knowledge Base Agent
kb_pattern = [
    {"name": "agent_type", "agent_type": "tool_use_agent"},
    {"name": "ai_model", "model": "GPT 4.1"},
    {"name": "knowledge_base", "project_id": project.id, "generate_inline_citations": True}
]

# Pattern 2: Multi-Toolkit Research Agent  
research_pattern = [
    {"name": "agent_type", "agent_type": "tool_use_agent"},
    {"name": "ai_model", "model": "claude-sonnet-4-20250514"},
    {
        "name": "toolkits",
        "toolkits": {
            "websearch": {"config": {}},
            "python": {"config": {"enabled_tools": ["execute_python"]}, "type": "python"}
        }
    }
]

# Pattern 3: Structured Response Agent
structured_pattern = [
    {"name": "agent_type", "agent_type": "tool_use_agent"},
    {"name": "ai_model", "model": "GPT 4.1"},
    {"name": "use_json_response", "use_json_response": True},
    {"name": "information_extraction", "project_id": project.id, "information_to_extract": [...]}
]
```

## 📖 Additional Resources

- **Toolkit Reference**: [ToolKits.md](ToolKits.md) - Complete toolkit documentation
- **SDK Guide**: [README.md](README.md) - SDK usage and examples
- **Examples**: Check `examples/` directory for working implementations
- **Documentation**: [https://api.getodin.ai/docs](https://api.getodin.ai/docs)
- **Website**: [https://getodin.ai](https://getodin.ai)

---

**Built with ❤️ by the ODIN AI Team**

---

**💡 Pro Tip**: Use the building blocks as modular components - start with basic functionality and progressively add more sophisticated capabilities as your use case evolves. The examples in this documentation provide tested patterns for common scenarios.