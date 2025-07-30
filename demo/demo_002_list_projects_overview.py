#!/usr/bin/env python3
"""
📋 ODIN SDK v3 - Projects Overview Demo

This demo showcases project inspection functionality with the ODIN SDK v3:
- 📁 List all projects in the workspace
- 🤖 List agents for each project
- 💬 List available AI models
- 🗄️ List smart tables/data types for each project
- 📚 Knowledge base overview (files cannot be listed directly via API)
- 📊 Comprehensive project dashboard view

This demonstrates read-only operations for getting a complete overview
of your ODIN workspace contents and project structure.
"""

import json
from typing import Dict, List, Any
from odin_sdk.v3 import create_client, OdinError


def format_size(size_bytes: int) -> str:
    """Format file size in human-readable format."""
    if size_bytes == 0:
        return "0 B"
    
    size_names = ["B", "KB", "MB", "GB"]
    i = 0
    while size_bytes >= 1024 and i < len(size_names) - 1:
        size_bytes /= 1024.0
        i += 1
    return f"{size_bytes:.1f} {size_names[i]}"


def safe_get_attribute(obj: Any, attr: str, default: str = "N/A") -> str:
    """Safely get an attribute from an object with fallback."""
    try:
        value = getattr(obj, attr, default)
        return str(value) if value is not None else default
    except Exception:
        return default


def list_available_models(client) -> List[Dict]:
    """List all available AI models."""
    try:
        print("🧠 Fetching available AI models...")
        
        # Use the proper v3 SDK method to get models
        models_response = client.chats().get_models()
        
        # The API returns a ChatModelInfoResponse with available_models field
        if hasattr(models_response, 'available_models') and models_response.available_models:
            models = []
            for model in models_response.available_models:
                # Models have display_name, key, description, etc.
                model_info = {
                    'name': safe_get_attribute(model, 'display_name', safe_get_attribute(model, 'name', 'Unknown')),
                    'key': safe_get_attribute(model, 'key', 'Unknown'),
                    'description': safe_get_attribute(model, 'description', 'No description'),
                    'provider': safe_get_attribute(model, 'provider', 'Unknown'),
                    'type': safe_get_attribute(model, 'type', 'LLM')
                }
                models.append(model_info)
            print(f"   ✅ Successfully fetched {len(models)} models from API")
            return models
        else:
            print("   ⚠️  API returned empty models list, using fallback")
            # Fallback to known models if API doesn't return them
            return [
                {'name': 'GPT 4.1', 'key': 'gpt-4-turbo', 'description': 'OpenAI GPT-4 Turbo', 'provider': 'OpenAI', 'type': 'LLM'},
                {'name': 'claude-sonnet-4-20250514', 'key': 'claude-sonnet-4', 'description': 'Anthropic Claude Sonnet', 'provider': 'Anthropic', 'type': 'LLM'}
            ]
            
    except Exception as e:
        print(f"   ⚠️  Error fetching models: {e}")
        print(f"   🔍 Error type: {type(e).__name__}")
        # Return default known models
        return [
            {'name': 'GPT 4.1', 'key': 'gpt-4-turbo', 'description': 'OpenAI GPT-4 Turbo', 'provider': 'OpenAI', 'type': 'LLM'},
            {'name': 'claude-sonnet-4-20250514', 'key': 'claude-sonnet-4', 'description': 'Anthropic Claude Sonnet', 'provider': 'Anthropic', 'type': 'LLM'}
        ]


def list_project_agents(client, project_id: str) -> List[Dict]:
    """List all agents in a project."""
    try:
        agents_response = client.agents().list(project_id)
        
        if hasattr(agents_response, 'agents') and agents_response.agents:
            agents = []
            # agents_response.agents is a dictionary with agent_id as keys and agent objects as values
            for agent_id, agent in agents_response.agents.items():
                # Handle both dict-like and object-like access
                if isinstance(agent, dict):
                    agent_info = {
                        'id': agent.get('agent_id', agent.get('id', agent_id)),
                        'name': agent.get('name', agent.get('agent_name', 'Unnamed Agent')),
                        'status': agent.get('status', 'Unknown'),
                        'created_at': agent.get('created_at', 'Unknown'),
                        'personality': agent.get('personality', 'No personality set')
                    }
                else:
                    agent_info = {
                        'id': safe_get_attribute(agent, 'agent_id', safe_get_attribute(agent, 'id', agent_id)),
                        'name': safe_get_attribute(agent, 'agent_name', safe_get_attribute(agent, 'name', 'Unnamed Agent')),
                        'status': safe_get_attribute(agent, 'status', 'Unknown'),
                        'created_at': safe_get_attribute(agent, 'created_at', 'Unknown'),
                        'personality': safe_get_attribute(agent, 'personality', 'No personality set')
                    }
                
                # Truncate long personality text
                if len(agent_info['personality']) > 100:
                    agent_info['personality'] = agent_info['personality'][:100] + "..."
                
                agents.append(agent_info)
            return agents
        else:
            return []
            
    except Exception as e:
        print(f"      ❌ Error listing agents: {e}")
        print(f"      🔍 Error details: {type(e).__name__}: {str(e)}")
        return []


def list_project_data_types(client, project_id: str) -> List[Dict]:
    """List all data types/smart tables in a project."""
    try:
        data_response = client.data().list(project_id)
        
        if hasattr(data_response, 'data_types') and data_response.data_types:
            data_types = []
            for data_type in data_response.data_types:
                dt_info = {
                    'id': safe_get_attribute(data_type, 'id', 'Unknown'),
                    'title': safe_get_attribute(data_type, 'title', 'Untitled'),
                    'description': safe_get_attribute(data_type, 'description', 'No description'),
                    'created_at': safe_get_attribute(data_type, 'created_at', 'Unknown'),
                    'table_id': safe_get_attribute(data_type, 'table_id', 'Unknown'),
                    'schema_count': len(getattr(data_type, 'var_schema', [])) if hasattr(data_type, 'var_schema') and data_type.var_schema else 0
                }
                data_types.append(dt_info)
            return data_types
        else:
            return []
            
    except Exception as e:
        print(f"      ❌ Error listing data types: {e}")
        return []


def get_knowledge_base_info(client, project_id: str) -> Dict:
    """
    Get knowledge base information for a project.
    Note: The ODIN API doesn't provide a direct method to list KB files,
    so we provide general information about KB capabilities.
    """
    try:
        # Since there's no direct list method for KB files in the API,
        # we return information about KB capabilities
        kb_info = {
            'files_count': 'Cannot be determined via API',
            'supported_formats': ['PDF', 'DOCX', 'TXT', 'CSV', 'JSON'],
            'features': [
                'Document ingestion and processing',
                'Semantic search and retrieval', 
                'Citation generation',
                'Multi-language support',
                'Metadata tagging'
            ],
            'note': 'File listing not available via API - files are accessed through search/retrieval'
        }
        return kb_info
        
    except Exception as e:
        print(f"      ❌ Error getting KB info: {e}")
        return {'error': str(e)}


def display_project_overview(project: Any, agents: List[Dict], data_types: List[Dict], kb_info: Dict):
    """Display a comprehensive overview of a single project."""
    print(f"\n📁 PROJECT: {safe_get_attribute(project, 'name', 'Unnamed Project')}")
    print("=" * 80)
    
    # Basic project info
    print(f"   🆔 ID: {safe_get_attribute(project, 'id', 'Unknown')}")
    print(f"   📝 Description: {safe_get_attribute(project, 'description', 'No description')}")
    print(f"   📅 Created: {safe_get_attribute(project, 'created_at', 'Unknown')}")
    print(f"   📊 Type: {safe_get_attribute(project, 'project_type', 'Unknown')}")
    
    # Agents section
    print(f"\n   🤖 AGENTS ({len(agents)}):")
    if agents:
        for i, agent in enumerate(agents, 1):
            print(f"      {i}. {agent['name']}")
            print(f"         • ID: {agent['id']}")
            print(f"         • Status: {agent['status']}")
            print(f"         • Created: {agent['created_at']}")
            print(f"         • Personality: {agent['personality']}")
            if i < len(agents):
                print()
    else:
        print("      No agents found in this project")
    
    # Smart Tables section
    print(f"\n   🗄️  SMART TABLES/DATA TYPES ({len(data_types)}):")
    if data_types:
        for i, dt in enumerate(data_types, 1):
            print(f"      {i}. {dt['title']}")
            print(f"         • ID: {dt['id']}")
            print(f"         • Table ID: {dt['table_id']}")
            print(f"         • Description: {dt['description']}")
            print(f"         • Created: {dt['created_at']}")
            print(f"         • Schema Fields: {dt['schema_count']}")
            if i < len(data_types):
                print()
    else:
        print("      No smart tables found in this project")
    
    # Knowledge Base section
    print(f"\n   📚 KNOWLEDGE BASE:")
    if 'error' not in kb_info:
        print(f"      • Files Count: {kb_info['files_count']}")
        print(f"      • Supported Formats: {', '.join(kb_info['supported_formats'])}")
        print(f"      • Features:")
        for feature in kb_info['features']:
            print(f"        - {feature}")
        print(f"      • Note: {kb_info['note']}")
    else:
        print(f"      ❌ Error: {kb_info['error']}")


def generate_workspace_summary(projects: List[Any], models: List[Dict]):
    """Generate a summary of the entire workspace."""
    total_agents = 0
    total_data_types = 0
    project_types = {}
    
    # Count totals and categorize projects
    for project_data in projects:
        project = project_data['project']
        agents = project_data['agents']
        data_types = project_data['data_types']
        
        total_agents += len(agents)
        total_data_types += len(data_types)
        
        project_type = safe_get_attribute(project, 'project_type', 'Unknown')
        project_types[project_type] = project_types.get(project_type, 0) + 1
    
    print("\n" + "=" * 80)
    print("📊 WORKSPACE SUMMARY")
    print("=" * 80)
    print(f"🏢 Total Projects: {len(projects)}")
    print(f"🤖 Total Agents: {total_agents}")
    print(f"🗄️  Total Smart Tables: {total_data_types}")
    print(f"🧠 Available Models: {len(models)}")
    
    print(f"\n📁 Project Types:")
    for ptype, count in project_types.items():
        print(f"   • {ptype}: {count} project(s)")
    
    print(f"\n🧠 Available AI Models:")
    for i, model in enumerate(models, 1):
        print(f"   {i}. {model['name']} ({model['provider']})")
        if 'key' in model and model['key'] != 'Unknown':
            print(f"      Key: {model['key']}")
        print(f"      {model['description']}")


def main():
    """
    Main demo function that provides a comprehensive overview of all projects.
    """
    print("📋 ODIN SDK v3 - Projects Overview Demo")
    print("=" * 80)
    print("This demo provides a comprehensive overview of your ODIN workspace.")
    print("It will list all projects and their components (agents, data, KB info).")
    print()
    print("⚠️  Note: This demo uses localhost:8001 as the host.")
    print("   Make sure your ODIN server is running locally for full functionality.")
    print()
    
    # Initialize client with credentials
    credentials = {
        "api_key": "b13cc8df-e33a-4828-a86c-0be3c96dcd0a",
        "api_secret": "IHeKHeRVZawSzl4wmjexf3e4/i3w8CxfzVqAMMGT2Y0=",
        "host": "http://localhost:8001"
    }
    
    try:
        print("🔑 Initializing ODIN client...")
        client = create_client(**credentials)
        print("✅ Client initialized successfully!")
        
        # Test authentication
        print("\n🔍 Testing authentication...")
        try:
            projects_response = client.projects().list()
            print("✅ Authentication successful!")
        except OdinError as e:
            print(f"❌ Authentication failed: {e}")
            print("Please check your credentials and server status.")
            return
        
        # Get available models first
        print("\n" + "=" * 80)
        print("🧠 AVAILABLE AI MODELS")
        print("=" * 80)
        
        models = list_available_models(client)
        if models:
            for i, model in enumerate(models, 1):
                print(f"{i}. {model['name']} ({model['provider']})")
                if 'key' in model and model['key'] != 'Unknown':
                    print(f"   Key: {model['key']}")
                print(f"   {model['description']}")
                print(f"   Type: {model['type']}")
                if i < len(models):
                    print()
        else:
            print("No models found")
        
        # Get and process all projects
        print(f"\n" + "=" * 80)
        print("📁 PROJECT DETAILS")
        print("=" * 80)
        
        if projects_response.projects and len(projects_response.projects) > 0:
            print(f"Found {len(projects_response.projects)} project(s). Analyzing each project...")
            
            projects_data = []
            
            for i, project in enumerate(projects_response.projects, 1):
                print(f"\n🔍 Analyzing project {i}/{len(projects_response.projects)} | Name: {safe_get_attribute(project, 'name', 'Unnamed')}")
                
                # Get project components
                project_id = safe_get_attribute(project, 'id', None)
                if project_id and project_id != 'Unknown':
                    print(f"   📊 Listing agents for project: {safe_get_attribute(project, 'name', 'Unnamed')}")
                    agents = list_project_agents(client, project_id)
                    print(f"      ✅ Found {len(agents)} agent(s)")
                    
                    print(f"   🗄️  Listing smart tables for project: {safe_get_attribute(project, 'name', 'Unnamed')}")
                    data_types = list_project_data_types(client, project_id)
                    print(f"      ✅ Found {len(data_types)} data type(s)")

                    # if len(data_types) != 0:
                    #     breakpoint()
                    
                    print(f"   📚 Getting knowledge base info for project: {safe_get_attribute(project, 'name', 'Unnamed')}")
                    kb_info = get_knowledge_base_info(client, project_id)
                    
                    projects_data.append({
                        'project': project,
                        'agents': agents,
                        'data_types': data_types,
                        'kb_info': kb_info
                    })
                    
                    # Display detailed project overview if there's meaningful content
                    if agents or data_types:
                        display_project_overview(project, agents, data_types, kb_info)
                else:
                    print(f"   ⚠️  Project {safe_get_attribute(project, 'name', 'Unnamed')} has no valid ID")
            
            # Generate workspace summary
            generate_workspace_summary(projects_data, models)
            
        else:
            print("No projects found in this workspace.")
            print("\n💡 To get started:")
            print("   • Create a project using the SDK or web interface")
            print("   • Add agents, upload data, or create knowledge bases")
            print("   • Run this demo again to see your workspace overview")
        
        print("\n" + "=" * 80)
        print("🎯 OVERVIEW DEMO COMPLETE!")
        print("=" * 80)
        print()
        print("Summary of what we demonstrated:")
        print("✅ Authentication and connection testing")
        print("✅ Listing all projects in the workspace")
        print("✅ Listing agents for each project")
        print("✅ Listing smart tables/data types for each project")
        print("✅ Knowledge base capabilities overview")
        print("✅ Available AI models listing")
        print("✅ Comprehensive workspace summary")
        print()
        print("Key Insights:")
        print("• Project structure and organization")
        print("• Resource distribution across projects")
        print("• Agent configurations and capabilities")
        print("• Data assets and smart table schemas")
        print("• Knowledge base integration points")
        print()
        print("🔗 Next Steps:")
        print("• Explore specific projects in more detail")
        print("• Create new agents with different toolkits")
        print("• Import data and create smart table analyses")
        print("• Build knowledge bases with document uploads")
        
    except OdinError as e:
        print(f"❌ ODIN API Error: {e}")
        print("This might indicate:")
        print("• Invalid credentials")
        print("• Server connectivity issues") 
        print("• API endpoint changes")
        
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        print("This might indicate:")
        print("• Network connectivity issues")
        print("• Server not running")
        print("• SDK version compatibility")
    
    print("\n🏁 Projects Overview Demo completed!")
    print("Thank you for using the ODIN SDK v3! 🎉")


if __name__ == "__main__":
    main()