# ODIN SDK - CRUD Examples [WIP]

The examples directory contains comprehensive examples demonstrating CRUD (Create, Read, Update, Delete) operations for all major ODIN SDK APIs.

## 📋 Examples Overview

| Example | Description | File |
|---------|-------------|------|
| **Projects** | Create, read, update, delete, and clone projects | `projects_crud.py` |
| **Knowledge Base** | Add files/URLs, read documents, update metadata, delete content | `knowledgebase_crud.py` |
| **PDF Upload** | Upload PDF files to knowledge base with processing | `upload_pdf_example.py` |
| **Agents** | Create custom agents, manage configurations, activate/deactivate | `agents_crud.py` |
| **Chats** | Create chats, send messages, read history, update names, delete | `chats_crud.py` |
| **All Examples** | Run all CRUD examples in sequence | `run_all_examples.py` |

## 🚀 Quick Start

### Prerequisites

1. **ODIN API Server**: Ensure your ODIN API server is running
2. **API Keys**: Valid API key and secret (configured in the examples)
3. **Dependencies**: `pip install odinai-sdk`

### Setup

**Install Dependencies**:
```bash
pip install odinai-sdk
```


**Run Examples**:
```bash
cd examples

# Run individual examples
python projects_crud.py
python knowledgebase_crud.py
python upload_pdf_example.py
python agents_crud.py
python chats_crud.py

# Run all examples
python run_all_examples.py
```

## 📁 Detailed Example Descriptions

### 1. Projects CRUD (`projects_crud.py`)

Demonstrates complete project lifecycle management:

- ✅ **CREATE**: Create new projects with different types
- ✅ **READ**: Get project details and list all projects  
- ✅ **UPDATE**: Modify project settings and metadata
- ✅ **DELETE**: Remove projects
- ✅ **CLONE**: Duplicate existing projects
- ✅ **SEARCH**: Find projects by criteria

**Key Operations:**
- Project creation with metadata
- Project listing and filtering
- Project updates and modifications
- Project deletion and cleanup

### 2. Knowledge Base CRUD (`knowledgebase_crud.py`)

Comprehensive knowledge base management:

- ✅ **CREATE**: Add files, URLs, and HTML content
- ✅ **READ**: Retrieve documents and metadata
- ✅ **UPDATE**: Modify document metadata and settings
- ✅ **DELETE**: Remove documents from knowledge base

**Key Operations:**
- File upload to knowledge base
- URL indexing and processing
- HTML content direct addition
- Document metadata management
- Batch document operations
- Processing status monitoring

### 3. PDF Upload Example (`upload_pdf_example.py`)

Focused example for uploading PDF files to knowledge base:

- ✅ **FILE UPLOAD**: Upload PDF files with binary content
- ✅ **PROCESSING**: Monitor upload and processing status
- ✅ **VERIFICATION**: Confirm file appears in knowledge base
- ✅ **CLEANUP**: Proper resource management

**Key Operations:**
- Binary file reading and upload
- Using v3 file upload endpoint
- File existence validation
- Upload status verification
- Document removal and cleanup

**Example Usage:**
- Uploads the included `attention_paper.pdf` 
- Demonstrates real file upload vs. text content creation
- Shows complete upload workflow with error handling

### 4. Agents CRUD (`agents_crud.py`)

Complete agent lifecycle management:

- ✅ **CREATE**: Build custom agents with personalities
- ✅ **READ**: Get agent details and list agents
- ✅ **UPDATE**: Modify agent configurations
- ✅ **DELETE**: Remove custom agents
- ✅ **ACTIVATE/DEACTIVATE**: Manage agent status
- ✅ **CLONE**: Duplicate existing agents

**Key Operations:**
- Custom agent creation
- System prompt configuration
- Model and parameter settings
- Agent activation management
- Model configuration management

### 5. Chats CRUD (`chats_crud.py`)

Comprehensive chat session management:

- ✅ **CREATE**: Start new chat sessions and send messages
- ✅ **READ**: Get chat history and conversation details
- ✅ **UPDATE**: Modify chat names and send feedback
- ✅ **DELETE**: Remove chat sessions

**Key Operations:**
- Chat session creation
- Message sending and receiving
- Conversation history retrieval
- Chat metadata management
- User feedback submission
- Bulk chat operations

## 🔧 Configuration

All examples use the following configuration:

```python
HOST = "http://your-api-host" (e.g. http://api.getodin.ai)
API_KEY = "your-api-key"
API_SECRET = "your-api-secret"
```

**Note**: Update these values to match your local ODIN API server configuration.

## 🧪 Testing

### Individual Testing
```bash
# Test projects
python projects_crud.py

# Test knowledge base
python knowledgebase_crud.py

# Test PDF upload
python upload_pdf_example.py

# Test agents
python agents_crud.py

# Test chats
python chats_crud.py
```

### Comprehensive Testing
```bash
# Run all tests with detailed reporting
python run_all_examples.py
```

## 📊 Expected Output

Each example provides detailed console output showing:

- ✅ **Success indicators** for completed operations
- ❌ **Error messages** with troubleshooting information
- 📋 **Data summaries** of created/retrieved objects
- ⏱️ **Timing information** for operations
- 🧹 **Cleanup confirmations** for resource management

## 🐛 Troubleshooting

### Common Issues

1. **API Connection Error**:
   - Verify ODIN API server is running on localhost:8001
   - Check API keys are valid
   - Ensure network connectivity

2. **Authentication Errors**:
   - Verify API_KEY and API_SECRET values
   - Check API key permissions

3. **Timeout Errors**:
   - Some operations (especially knowledge base processing) may take time
   - Examples include appropriate delays

### Debug Mode

Add debug logging to any example:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 🔄 Continuous Testing

For development and testing workflows:

```bash
# Watch for changes and re-run tests
watch -n 30 python run_all_examples.py
```

## 📚 API Reference

Each example demonstrates the following SDK patterns:

- **Client Configuration**: Setting up API clients with authentication
- **Request Building**: Creating proper request objects
- **Response Handling**: Processing API responses and errors  
- **Error Management**: Graceful error handling and recovery
- **Resource Cleanup**: Proper cleanup of created resources

## 🎯 Use Cases

These examples are perfect for:

- **SDK Integration**: Learning how to integrate ODIN SDK
- **API Testing**: Validating API functionality
- **Development Reference**: Code samples for common operations
- **Automation**: Building automated workflows
- **Documentation**: Understanding API capabilities

## 📝 Notes

- All examples include proper error handling and cleanup
- Resource cleanup ensures no leftover test data
- Examples are designed to be run multiple times safely
- Timing delays account for async processing
- Comprehensive logging helps with debugging
