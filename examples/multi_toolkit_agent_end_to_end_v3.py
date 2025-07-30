import os
import sys

# Add the parent directory to the path to import odin_sdk
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../odin_sdk/'))

from odin_sdk.v3 import create_client, OdinError

def main():
    """
    Enhanced Multi-Toolkit Agent Demo using the v3 wrapper.
    
    This example demonstrates v3 improvements:
    - Flattened response objects (project.id vs project.project.id)
    - Convenience methods (project.delete() vs client.projects().delete(id))
    - Project-scoped managers (project.agents.create())
    - Resource self-awareness (agent.activate(), chat.send_message())
    
    Shows the same multi-toolkit functionality as v2 but with cleaner API usage.
    """
    
    # Initialize client with credentials
    client = create_client(
        api_key="b13cc8df-e33a-4828-a86c-0be3c96dcd0a",
        api_secret="IHeKHeRVZawSzl4wmjexf3e4/i3w8CxfzVqAMMGT2Y0="
    )
    
    try:
        print("🚀 Starting Multi-Toolkit Agent Demo (V3 - Enhanced Wrapper)")
        
        # Clean up any existing projects with 3+ duplicates
        print("\n🧹 Cleaning up duplicate projects...")
        existing_projects = client.projects().list()
        if existing_projects.projects:
            project_groups = {}
            for project in existing_projects.projects:
                name = project.name  # v3: Flattened attribute access
                if name not in project_groups:
                    project_groups[name] = []
                project_groups[name].append(project)
            
            for name, projects in project_groups.items():
                if len(projects) >= 3:
                    print(f"Deleting {len(projects)} duplicate projects named '{name}'")
                    for project in projects:
                        try:
                            project.delete()  # v3: Convenience method!
                            print(f"   ✅ Deleted: {project.name}")
                        except Exception as e:
                            print(f"   ❌ Failed to delete: {e}")
        
        # Create project - returns enhanced Project object
        print("\n📁 Creating project...")
        project = client.projects().create(
            name="SDK Multi-Toolkit Agent V3",
            description="Multi-toolkit research agent with web search, Python, and financial analysis"
        )
        print(f"✅ Project created: {project.name} (ID: {project.id})")  # v3: Flattened attributes!
        
        # Create multi-toolkit agent using project-scoped manager
        print("\n🤖 Creating multi-toolkit research agent...")
        
        # Enhanced personality for comprehensive analysis
        personality = """You are an intelligent AI research and analysis assistant with advanced capabilities in web research, data analysis, and financial market insights. 

Your core strengths include:

🔍 **Web Research & Information Gathering**
- Conduct thorough web searches to find the latest news, trends, and information
- Cross-reference multiple sources for accuracy and comprehensiveness
- Summarize complex information in clear, actionable insights

📊 **Data Analysis & Python Programming**
- Execute Python code to perform sophisticated data analysis and visualization
- Work with various data formats using built-in Python libraries and pandas only
- Create meaningful charts, graphs, and statistical summaries
- Process and clean data to extract valuable insights

💼 **Financial Market Analysis**
- Analyze stock performance, market trends, and financial metrics using yfinance
- Compare multiple stocks and create portfolio analysis
- Generate technical indicators and market insights
- Correlate market data with news events and economic factors

Always strive to provide thorough, well-researched responses that leverage all your available tools to deliver maximum value."""

        # Build agent configuration (same as v2 but cleaner usage)
        building_blocks = [
            {
                "name": "knowledge_base",
                "project_id": project.id,  # v3: Flattened attribute
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
                "model": "claude-sonnet-4-20250514"
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
        ]
        
        agent = project.agents.create(  # v3: Project-scoped manager!
            name="Multi-Toolkit Research Agent",
            personality=personality,
            building_blocks=building_blocks,
            temperature=0.5
        )
        print(f"✅ Agent created with multiple toolkits: {agent.agent_id}")
        
        # Activate agent using convenience method
        print("\n⚡ Activating agent...")
        agent.activate()  # v3: Agent knows its own context!
        print("✅ Agent activated successfully")
        
        # Create chat session using project-scoped manager
        print("\n💬 Creating analysis chat...")
        chat = project.chats.create(  # v3: Project-scoped manager!
            name="Multi-Toolkit Analysis Chat",
            context="You are equipped with web search, Python execution, and financial data analysis capabilities. Use all available tools to provide comprehensive, data-driven insights."
        )
        print(f"✅ Chat created: {chat.chat_id}")
        
        # Send comprehensive analysis request using chat convenience method
        print("\n🔍 Requesting comprehensive Apple stock analysis...")
        message = """I need a comprehensive analysis of Apple Inc. (AAPL) stock. Please:

1. Search the web for the latest news and developments about Apple in the past week
2. Use yfinance to get AAPL stock data for the last 3 months 
3. Use Python to create a visualization showing:
   - Stock price trend over the 3-month period
   - Volume analysis
   - Calculate and display key metrics like average price, volatility, and recent performance

4. Correlate any significant news events with stock price movements
5. Provide a summary with insights about Apple's recent performance and potential outlook

Please use all your available tools to give me the most comprehensive analysis possible."""
        
        response = chat.send_message(  # v3: Chat knows its own context!
            message=message,
            skip_stream=True
        )
        
        print(f"\n📝 Analysis Request: Multi-toolkit Apple stock analysis")
        print("\n🤖 AI Response:")
        print("=" * 80)
        
        # Handle different response formats
        if hasattr(response, 'message') and response.message:
            print(response.message)
        elif hasattr(response, 'response_text') and response.response_text:
            print(response.response_text)
        else:
            print(f"Response received: {response}")
        
        print("=" * 80)
        print("\n✅ Comprehensive analysis complete!")
        print("The AI agent used web search, Python, and financial data tools for this analysis!")
        
        # Wait for user input before cleanup
        print("\n" + "="*80)
        print("🎯 DEMO COMPLETE! Press Enter to clean up and delete the project...")
        print("="*80)
        input()
        
        # Clean up using convenience method
        print("\n🧹 Cleaning up...")
        project.delete()  # v3: Much cleaner!
        print(f"✅ Project '{project.name}' deleted successfully!")
        print("🔄 Demo completed successfully!")
        
    except OdinError as e:
        print(f"❌ API Error: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
    
    print("\n🏁 Multi-Toolkit Agent Demo V3 completed!")
    print("\n📈 V3 Improvements showcased:")
    print("   • Flattened response objects: project.id vs project.project.id")
    print("   • Convenience methods: project.delete() vs client.projects().delete(id)")
    print("   • Project-scoped managers: project.agents.create(), project.chats.create()")
    print("   • Resource self-awareness: agent.activate(), chat.send_message()")

if __name__ == "__main__":
    main() 