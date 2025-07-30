import os
import sys

# Add the parent directory to the path to import odin_sdk
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../odin_sdk/'))

from odin_sdk.v3 import create_client, OdinError

def main():
    """
    Enhanced Knowledge Base Agent Demo using the v3 wrapper.
    
    This example demonstrates v3 improvements:
    - Flattened response objects (project.id vs project.project.id)
    - Convenience methods (project.delete() vs client.projects().delete(id))
    - Project-scoped managers (project.agents.create())
    - Resource self-awareness (agent.activate())
    
    Shows the same functionality as v2 but with cleaner, more elegant API usage.
    """
    
    # Initialize client with credentials
    client = create_client(
        api_key="b13cc8df-e33a-4828-a86c-0be3c96dcd0a",
        api_secret="IHeKHeRVZawSzl4wmjexf3e4/i3w8CxfzVqAMMGT2Y0="
    )
    
    try:
        print("🚀 Starting Knowledge Base Agent Demo (V3 - Enhanced Wrapper)")
        
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
            name="SDK KB Agent Demo V3",
            description="Enhanced knowledge base demo using v3 wrapper SDK"
        )
        print(f"✅ Project created: {project.name} (ID: {project.id})")  # v3: Flattened attributes!
        
        # Add PDF to knowledge base using project-scoped manager
        print("\n📄 Adding PDF to knowledge base...")
        pdf_path = os.path.join(os.path.dirname(__file__), "attention_paper.pdf")
        
        kb_response = project.knowledge.add_file(  # v3: Project-scoped manager!
            file_path=pdf_path,
            metadata={},
            file_type="application/pdf",
            path="/"
        )
        print("✅ PDF added to knowledge base successfully")
        
        # Create knowledge base agent using project-scoped manager
        print("\n🤖 Creating knowledge base agent...")
        
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
                            "project_id": project.id,  # v3: Flattened attribute
                            "description": "Access knowledge base from the current project"
                        }]
                    }
                }
            }
        ]
        
        agent = project.agents.create(  # v3: Project-scoped manager!
            name="Document Analysis Agent",
            personality="You are a helpful assistant that can analyze documents and explain complex concepts in simple terms.",
            building_blocks=building_blocks
        )
        print(f"✅ Agent created: {agent.agent_id}")
        
        # Activate agent using convenience method
        print("\n⚡ Activating agent...")
        agent.activate()  # v3: Agent knows its own context!
        print("✅ Agent activated successfully")
        
        # Create chat session using project-scoped manager
        print("\n💬 Creating chat session...")
        chat = project.chats.create(  # v3: Project-scoped manager!
            name="Document Summary Chat",
            context="Please provide comprehensive summaries and explanations of the uploaded document."
        )
        print(f"✅ Chat created: {chat.chat_id}")
        
        # Send message using chat convenience method
        print("\n🔍 Asking AI to summarize the document...")
        message = "Summarize my document and explain it to me like I am 12 years old"
        
        response = chat.send_message(  # v3: Chat knows its own context!
            message=message,
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
        
        # Clean up using convenience method
        print("\n🧹 Cleaning up...")
        project.delete()  # v3: Much cleaner!
        print(f"✅ Project '{project.name}' deleted successfully!")
        print("🔄 Demo completed successfully!")
        
    except OdinError as e:
        print(f"❌ API Error: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
    
    print("\n🏁 Knowledge Base Agent Demo V3 completed!")
    print("\n📈 V3 Improvements showcased:")
    print("   • Flattened response objects: project.id vs project.project.id")
    print("   • Convenience methods: project.delete() vs client.projects().delete(id)")
    print("   • Project-scoped managers: project.agents.create(), project.chats.create()")
    print("   • Resource self-awareness: agent.activate(), chat.send_message()")

if __name__ == "__main__":
    main() 