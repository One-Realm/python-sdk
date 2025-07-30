import os
import sys

# Add the parent directory to the path to import odin_sdk
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../odin_sdk/'))

from odin_sdk.v2 import create_client, OdinError

def main():
    """
    Simplified Knowledge Base Agent Demo using the elegant wrapper.
    
    This example demonstrates:
    - Creating a project
    - Adding a PDF to knowledge base
    - Creating a KB-enabled agent
    - Having a conversation about the document
    - Automatic cleanup
    
    Reduced from 300+ lines to ~50 lines!
    """
    
    # Initialize client with credentials
    client = create_client(
        api_key="b13cc8df-e33a-4828-a86c-0be3c96dcd0a",
        api_secret="IHeKHeRVZawSzl4wmjexf3e4/i3w8CxfzVqAMMGT2Y0="
    )
    
    try:
        print("🚀 Starting Knowledge Base Agent Demo (V2 - Elegant Version)")
        
        # Clean up any existing projects with 3+ duplicates
        print("\n🧹 Cleaning up duplicate projects...")
        existing_projects = client.projects().list()
        if existing_projects.projects:
            project_groups = {}
            for project in existing_projects.projects:
                name = project.name
                if name not in project_groups:
                    project_groups[name] = []
                project_groups[name].append(project)
            
            for name, projects in project_groups.items():
                if len(projects) >= 3:
                    print(f"Deleting {len(projects)} duplicate projects named '{name}'")
                    for project in projects:
                        try:
                            client.projects().delete(project.id)
                            print(f"   ✅ Deleted: {project.name}")
                        except Exception as e:
                            print(f"   ❌ Failed to delete: {e}")
        
        # Create project in one line
        print("\n📁 Creating project...")
        project = client.projects().create(
            name="SDK KB Agent Demo V2",
            description="Elegant knowledge base demo using wrapper SDK"
        )
        print(f"✅ Project created: {project.project.name} (ID: {project.project.id})")
        
        # Add PDF to knowledge base
        print("\n📄 Adding PDF to knowledge base...")
        pdf_path = os.path.join(os.path.dirname(__file__), "attention_paper.pdf")
        
        kb_response = client.knowledge().add_file(
            project_id=project.project.id,
            file_path=pdf_path,
            metadata={},
            file_type="application/pdf",
            path="/"
        )
        print("✅ PDF added to knowledge base successfully")
        
        # Create knowledge base agent (simplified!)
        print("\n🤖 Creating knowledge base agent...")
        
        # Build agent configuration directly (just like original)
        building_blocks = [
            {
                "name": "knowledge_base",
                "project_id": project.project.id,
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
                "name": "ai_model",
                "model": "GPT 4.1"
            },
            {
                "name": "agent_type",
                "agent_type": "tool_use_agent"
            },
            {
                "name": "toolkits",
                "toolkits": {
                    "knowledge_base": {
                        "config": [{
                            "name": "Current Project",
                            "project_id": project.project.id,
                            "description": "Access knowledge base from the current project"
                        }]
                    }
                }
            }
        ]
        
        agent = client.agents().create(
            project_id=project.project.id,
            name="Document Analysis Agent",
            personality="You are a helpful assistant that can analyze documents and explain complex concepts in simple terms.",
            building_blocks=building_blocks
        )
        print(f"✅ Agent created: {agent.agent_id}")
        
        # Activate agent
        print("\n⚡ Activating agent...")
        client.agents().activate(project.project.id, agent.agent_id)
        print("✅ Agent activated successfully")
        
        # Create chat session
        print("\n💬 Creating chat session...")
        chat = client.chats().create(
            project_id=project.project.id,
            name="Document Summary Chat",
            context="Please provide comprehensive summaries and explanations of the uploaded document."
        )
        print(f"✅ Chat created: {chat.chat_id}")
        
        # Send message to analyze document
        print("\n🔍 Asking AI to summarize the document...")
        message = "Summarize my document and explain it to me like I am 12 years old"
        
        response = client.chats().send_message(
            message=message,
            project_id=project.project.id,
            chat_id=chat.chat_id,
            skip_stream=True
        )
        
        print(f"\n📝 Question: {message}")
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
        print("\n✅ Document analysis complete!")
        
        # Wait for user input before cleanup
        print("\n" + "="*80)
        print("🎯 DEMO COMPLETE! Press Enter to clean up and delete the project...")
        print("="*80)
        input()
        
        # Clean up
        print("\n🧹 Cleaning up...")
        client.projects().delete(project.project.id)
        print(f"✅ Project '{project.project.name}' deleted successfully!")
        print("🔄 Demo completed successfully!")
        
    except OdinError as e:
        print(f"❌ API Error: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
    
    print("\n🏁 Knowledge Base Agent Demo V2 completed!")

if __name__ == "__main__":
    main()
