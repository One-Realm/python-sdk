import os
import odin_sdk
from odin_sdk.rest import ApiException

# Initialize the API client
configuration = odin_sdk.Configuration(host="http://localhost:8001")
api_client = odin_sdk.ApiClient(configuration)
projects_api = odin_sdk.ProjectsApi(api_client)

api_client.default_headers["x-api-key"] = "b13cc8df-e33a-4828-a86c-0be3c96dcd0a"
api_client.default_headers["x-api-secret"] = "IHeKHeRVZawSzl4wmjexf3e4/i3w8CxfzVqAMMGT2Y0="

# First, let's get and print all existing projects
print("=== EXISTING PROJECTS ===")
existing_projects_response = None
try:
    existing_projects_response = projects_api.get_projects_projects_get()
    if existing_projects_response.projects:
        for project in existing_projects_response.projects:
            print(f"Project ID: {project.id}, Name: {project.name}")
    else:
        print("No existing projects found.")
except ApiException as e:
    print(f"Error retrieving existing projects: {e}")
print("========================\n")

# Group projects by name and delete groups with 3 or more projects
print("=== CLEANING UP DUPLICATE PROJECT GROUPS ===")
try:
    if existing_projects_response and existing_projects_response.projects:
        # Group projects by name
        project_groups = {}
        for project in existing_projects_response.projects:
            project_name = project.name
            if project_name not in project_groups:
                project_groups[project_name] = []
            project_groups[project_name].append(project)
        
        # Find groups with 3 or more projects and delete them
        groups_to_delete = []
        for name, projects in project_groups.items():
            if len(projects) >= 3:
                groups_to_delete.append((name, projects))
                print(f"Found group '{name}' with {len(projects)} projects - marking for deletion")
        
        if groups_to_delete:
            print(f"\nDeleting {len(groups_to_delete)} groups with 3+ duplicate projects...")
            
            for group_name, projects in groups_to_delete:
                print(f"\nDeleting group '{group_name}' ({len(projects)} projects):")
                for project in projects:
                    try:
                        delete_request = odin_sdk.DeleteProjectRequest(project_id=project.id)
                        projects_api.delete_project_project_delete_delete(delete_request)
                        print(f"   ✅ Deleted: {project.name} (ID: {project.id})")
                    except ApiException as e:
                        print(f"   ❌ Failed to delete {project.name} (ID: {project.id}): {e}")
                    except Exception as e:
                        print(f"   ❌ Error deleting {project.name} (ID: {project.id}): {e}")
        else:
            print("No groups with 3+ duplicate projects found.")
    else:
        print("No existing projects to process.")
        
except Exception as e:
    print(f"Error during duplicate group cleanup: {e}")
print("==============================================\n")

# Create project request
create_request = odin_sdk.CreateProjectRequest(
    project_name="SDK Multi-Toolkit Agent 1.0",
    project_description="A project for building an intelligent AI assistant with web search, Python execution, and financial data analysis capabilities",
    project_type="kb_chat"  # Knowledge base chat project
)

try:
    # Create the project
    response = projects_api.create_project_project_create_post(
        create_project_request=create_request,
    )
    
    print(f"Project created successfully!")
    print(f"Project ID: {response.project.id}")
    print(f"Project Name: {response.project.name}")
    
    # Get available models first
    chat_api = odin_sdk.ChatApi(api_client)
    
    try:
        models_response = chat_api.get_default_models_chat_models_get()
        print(f"\nAvailable models retrieved successfully!")
        
        # Find a suitable model (let's use claude-sonnet-4-20250514 if available, otherwise use the first available)
        selected_model = None
        if models_response.available_models:
            # Try to find claude-sonnet-4-20250514 first
            for model in models_response.available_models:
                if model.display_name == "claude-sonnet-4-20250514":
                    selected_model = model
                    break
            
            # If claude-sonnet-4-20250514 not found, use the first available model
            if not selected_model:
                selected_model = models_response.available_models[0]
            
            print(f"Selected model: {selected_model.display_name} (key: {selected_model.key})")
        else:
            print("No models available, using hardcoded values")
            
    except ApiException as e:
        print(f"Error retrieving models: {e}")
        selected_model = None

    # Create an agent for the project with multiple toolkits
    agents_api = odin_sdk.AgentsApi(api_client)
    
    # Enhanced personality for multi-toolkit agent
    personality = """You are an intelligent AI research and analysis assistant with advanced capabilities in web research, data analysis, and financial market insights. 

Your core strengths include:

🔍 **Web Research & Information Gathering**
- Conduct thorough web searches to find the latest news, trends, and information
- Cross-reference multiple sources for accuracy and comprehensiveness
- Summarize complex information in clear, actionable insights

📊 **Data Analysis & Python Programming**
- Execute Python code to perform sophisticated data analysis and visualization
- Work with various data formats (CSV, JSON, APIs) using built-in Python libraries and pandas only
- Create meaningful charts, graphs, and statistical summaries without external libraries (except pandas)
- Process and clean data to extract valuable insights using Python's standard library and pandas
- Note: You should avoid using external libraries other than pandas - rely on built-in Python capabilities

💼 **Financial Market Analysis**
- Analyze stock performance, market trends, and financial metrics using yfinance
- Compare multiple stocks and create portfolio analysis
- Generate technical indicators and market insights
- Correlate market data with news events and economic factors

🎯 **Integrated Analysis Approach**
When given a task, you:
1. First gather current information through web search
2. Collect relevant financial/quantitative data when applicable
3. Use Python (with only pandas as external library) to analyze, process, and visualize the data
4. Provide comprehensive insights that combine current events with data-driven analysis
5. Present findings in a clear, professional manner with supporting visualizations

Always strive to provide thorough, well-researched responses that leverage all your available tools to deliver maximum value to the user."""
    
    # Create agent request with multiple toolkits
    agent_request = odin_sdk.SaveNewCustomAgent(
        project_id=response.project.id,
        agent_name="Multi-Toolkit Research Agent",
        personality=personality,
        building_blocks=[
            {
                "name": "knowledge_base",
                "project_id": response.project.id,
                "document_keys": [],
                "enrich_sources": False,
                "generate_inline_citations": False,
                "enforce_strict_adherence": False,
                "query_language": "English",
                "translate_queries": False,
                "additional_kb_ids": [],
                "kb_search_results_to_return": 10,
                "kb_search_score_threshold": 0,
                "extra_strict_adherence_test_rules": [],
                "extra_strict_adherence_failure_response_rules": [],
                "use_kb_cache": False,
                "should_enrich": False,
                "use_whole_document": False,
                "cache_threshold": 0.6,
                "max_context_size": 2500
            },
            {
                "name": "agent_type",
                "agent_type": "tool_use_agent"
            },
            {
                "name": "ai_model",
                "model": selected_model.display_name if selected_model else "claude-sonnet-4-20250514"
            },
            {
                "name": "toolkits",
                "toolkits": {
                    "websearch": {
                        "config": {}
                    },
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
                    "yfinance": {
                        "config": {}
                    }
                }
            }
        ],
        temperature=0.5,
        mask_urls=True
    )
    
    # Create the agent
    agent_response = agents_api.save_new_custom_agent_agents_new_post(agent_request)
    
    if agent_response.success:
        print(f"\nAgent created successfully!")
        print(f"Agent ID: {agent_response.agent_id}")
        print(f"Message: {agent_response.msg}")
        
        # Activate the agent (set as default)
        activate_request = odin_sdk.RoutesProjectsActivateCustomAgentRequest(
            project_id=response.project.id,
            agent_id=agent_response.agent_id
        )
        
        activate_response = agents_api.activate_custom_agent_agents_activate_post(activate_request)
        
        if activate_response.message and activate_response.message == "Successfully activated custom agent!":
            print(f"\nAgent activated successfully!")
            
            # Create a chat for comprehensive analysis
            chat_api = odin_sdk.ChatApi(api_client)
            
            chat_request = odin_sdk.CreateChatPromptRequest(
                project_id=response.project.id,
                name="Multi-Toolkit Analysis Chat",
                context="You are equipped with web search, Python execution, and financial data analysis capabilities. Use all available tools to provide comprehensive, data-driven insights and analysis."
            )
            
            chat_response = chat_api.create_chat_chat_create_post(chat_request)
            
            print(f"\nChat created successfully!")
            print(f"Chat ID: {chat_response.chat_id}")
            print(f"Chat Name: {chat_response.name}")
            
            # Send a comprehensive message that uses all toolkits
            print("\nSending comprehensive analysis request to chat...")
            message_text = """I need a comprehensive analysis of Apple Inc. (AAPL) stock. Please:

1. Search the web for the latest news and developments about Apple in the past week
2. Use yfinance to get AAPL stock data for the last 3 months 
3. Use Python to create a visualization showing:
   - Stock price trend over the 3-month period
   - Volume analysis
   - Calculate and display key metrics like average price, volatility, and recent performance

4. Correlate any significant news events with stock price movements
5. Provide a summary with insights about Apple's recent performance and potential outlook

Please use all your available tools to give me the most comprehensive analysis possible."""
            
            try:
                message_response = chat_api.send_message_v3_v3_chat_message_post(
                    message=message_text,
                    project_id=response.project.id,
                    chat_id=chat_response.chat_id,
                    skip_stream=True  # Get the full response without streaming
                )
                
                print(f"\nMessage sent successfully!")
                print(f"Analysis Request: {message_text}")
                print(f"\nAI Response:")
                print("=" * 80)
                if hasattr(message_response, 'message') and message_response.message:
                    print(message_response.message)
                elif hasattr(message_response, 'response_text') and message_response.response_text:
                    print(message_response.response_text)
                else:
                    print("Response received but format may vary. Full response object:")
                    print(message_response)
                print("=" * 80)
                
            except ApiException as msg_e:
                print(f"❌ Failed to send message: {msg_e}")
            except Exception as msg_e:
                print(f"❌ Error sending message: {msg_e}")
            
            print("\nThe AI agent has processed your comprehensive analysis request using web search, Python, and financial data tools!")
            
            # Wait for user input before cleanup
            print("\n" + "="*80)
            print("🎯 DEMO COMPLETE! Press any key to clean up and delete the project...")
            print("="*80)
            try:
                input()  # Block until user presses any key
            except KeyboardInterrupt:
                print("\nReceived interrupt signal...")
            
            # Clean up: Delete the project
            print("\n🧹 CLEANING UP...")
            print(f"Deleting project: {response.project.name} (ID: {response.project.id})")
            
            try:
                delete_request = odin_sdk.DeleteProjectRequest(project_id=response.project.id)
                delete_response = projects_api.delete_project_project_delete_delete(delete_request)
                print(f"✅ Project '{response.project.name}' deleted successfully!")
                print("🔄 Script is now idempotent - ready for next run!")
            except ApiException as del_e:
                print(f"❌ Failed to delete project: {del_e}")
            except Exception as del_e:
                print(f"❌ Error during cleanup: {del_e}")
            
        else:
            print(f"Failed to activate agent: {activate_response.message}")
            # Still try to clean up the project even if agent activation failed
            print("\n🧹 CLEANING UP FAILED SETUP...")
            try:
                delete_request = odin_sdk.DeleteProjectRequest(project_id=response.project.id)
                projects_api.delete_project_project_delete_delete(delete_request)
                print(f"✅ Cleaned up project after failure")
            except Exception as cleanup_e:
                print(f"❌ Failed to clean up project: {cleanup_e}")
    else:
        print(f"Failed to create agent: {agent_response}")
        # Still try to clean up the project even if agent creation failed
        print("\n🧹 CLEANING UP FAILED SETUP...")
        try:
            delete_request = odin_sdk.DeleteProjectRequest(project_id=response.project.id)
            projects_api.delete_project_project_delete_delete(delete_request)
            print(f"✅ Cleaned up project after failure")
        except Exception as cleanup_e:
            print(f"❌ Failed to clean up project: {cleanup_e}")
    
except ApiException as e:
    print(f"Error creating project, agent, or chat: {e}")
    print("\n❌ Setup failed - no cleanup needed")
except Exception as e:
    print(f"Unexpected error: {e}")
    print("\n❌ Setup failed - no cleanup needed")

print("\n🏁 Script execution completed!") 