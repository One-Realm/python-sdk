"""
ODIN SDK - Agents CRUD Examples (Fixed & Idempotent)
Demonstrates Create, Read, Update, Delete operations for agents using localhost:8001
All operations are idempotent and include proper cleanup.
"""
import odin_sdk
from odin_sdk.rest import ApiException
import time
import sys

# Configuration
HOST = "http://localhost:8001"
API_KEY = "b13cc8df-e33a-4828-a86c-0be3c96dcd0a"
API_SECRET = "IHeKHeRVZawSzl4wmjexf3e4/i3w8CxfzVqAMMGT2Y0="

# Initialize the API client
configuration = odin_sdk.Configuration(host=HOST)
api_client = odin_sdk.ApiClient(configuration)
agents_api = odin_sdk.AgentsApi(api_client)
projects_api = odin_sdk.ProjectsApi(api_client)

# Set headers for authentication
api_client.default_headers["x-api-key"] = API_KEY
api_client.default_headers["x-api-secret"] = API_SECRET

# Global variables to track created resources for cleanup
test_project_id = None
created_agent_ids = []

def create_test_project():
    """Create a test project for agent operations"""
    print("🔧 Creating test project for Agents CRUD operations...")
    
    global test_project_id
    
    try:
        # Clean up any existing test project first
        try:
            response = projects_api.get_projects_projects_get()
            for project in response.projects:
                if project.name == "Agents CRUD Test Project":
                    delete_request = odin_sdk.DeleteProjectRequest(project_id=project.id)
                    projects_api.delete_project_project_delete_delete(delete_request)
                    print(f"   ✅ Cleaned up existing project: {project.id}")
                    time.sleep(1)
        except Exception as e:
            print(f"   ⚠️ Error during cleanup: {e}")
        
        # Create new test project
        create_request = odin_sdk.CreateProjectRequest(
            project_name="Agents CRUD Test Project",
            project_description="Test project for demonstrating Agents CRUD operations",
            project_type="kb_chat"
        )
        
        response = projects_api.create_project_project_create_post(create_request)
        test_project_id = response.project_id
        
        print(f"✅ Test project created successfully!")
        print(f"   Project ID: {test_project_id}")
        print(f"   Project Name: {response.project.name}")
        
        return test_project_id
        
    except ApiException as e:
        print(f"❌ API Error creating test project: {e}")
        return None
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None

def create_agent_example():
    """CREATE: Create a new custom agent"""
    print("\n" + "=" * 60)
    print("🤖 CREATE CUSTOM AGENT EXAMPLE")
    print("=" * 60)
    
    if not test_project_id:
        print("❌ No test project available")
        return None
    
    try:
        # Create a new custom agent
        agent_request = odin_sdk.SaveNewCustomAgent(
            project_id=test_project_id,
            agent_name="CRUD Test Agent",
            personality="You are a helpful AI assistant created for testing CRUD operations. You are knowledgeable, precise, and always ready to help with questions.",
            building_blocks=[
                {
                    "name": "enhanced_search",
                    "answered_rules": ["Thank you for using the CRUD test agent!"],
                    "group_on_backend": False
                }
            ],
            temperature=0.7
        )
        
        response = agents_api.save_new_custom_agent_agents_new_post(agent_request)
        
        if response.success:
            agent_id = response.agent_id
            created_agent_ids.append(agent_id)
            
            print("✅ Custom agent created successfully!")
            print(f"   Agent ID: {agent_id}")
            print(f"   Message: {response.msg}")
            print(f"   Success: {response.success}")
            
            return agent_id
        else:
            print(f"❌ Failed to create agent: {response.msg}")
            return None
        
    except ApiException as e:
        print(f"❌ API Error creating agent: {e}")
        return None
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None

def list_agents_example():
    """READ: List all agents for the project"""
    print("\n" + "=" * 60)
    print("📋 LIST AGENTS EXAMPLE")
    print("=" * 60)
    
    if not test_project_id:
        print("❌ No test project available")
        return None
    
    try:
        # List agents for the project
        response = agents_api.list_agents_for_project_agents_project_id_list_get(test_project_id)
        
        print("✅ Agents list retrieved successfully!")
        print(f"   Total agents: {len(response.agents)}")
        
        for i, agent in enumerate(response.agents, 1):
            print(f"\n   🤖 Agent {i}:")
            print(f"      ID: {agent.id}")
            print(f"      Name: {agent.name}")
            print(f"      Type: {agent.type}")
            print(f"      Active: {agent.is_active}")
            if hasattr(agent, 'description') and agent.description:
                print(f"      Description: {agent.description}")
        
        return response.agents
        
    except ApiException as e:
        print(f"❌ API Error listing agents: {e}")
        return None
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None

def get_agent_example(agent_id):
    """READ: Get a specific agent"""
    print("\n" + "=" * 60)
    print("🔍 GET SPECIFIC AGENT EXAMPLE")
    print("=" * 60)
    
    if not test_project_id or not agent_id:
        print("❌ No test project or agent ID available")
        return None
    
    try:
        # Get specific agent details
        response = agents_api.get_custom_agent_agents_project_id_agent_id_get_get(test_project_id, agent_id)
        
        print("✅ Agent details retrieved successfully!")
        print(f"   Agent ID: {agent_id}")
        print(f"   Agent Details: {response}")
        
        return response
        
    except ApiException as e:
        print(f"❌ API Error getting agent: {e}")
        return None
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None

def edit_agent_example(agent_id):
    """UPDATE: Edit an existing agent"""
    print("\n" + "=" * 60)
    print("✏️ EDIT AGENT EXAMPLE")
    print("=" * 60)
    
    if not test_project_id or not agent_id:
        print("❌ No test project or agent ID available")
        return None
    
    try:
        # Edit the existing agent
        edit_request = odin_sdk.EditExistingCustomAgent(
            project_id=test_project_id,
            agent_name="CRUD Test Agent (Updated)",
            edit_agent_id=agent_id,
            personality="You are an updated AI assistant created for testing CRUD operations. You are more knowledgeable, extremely precise, and always enthusiastic to help with any questions!",
            building_blocks=[
                {
                    "name": "enhanced_search",
                    "answered_rules": ["Thank you for using the updated CRUD test agent! I hope I was helpful!"],
                    "group_on_backend": True  # Changed this setting
                }
            ],
            temperature=0.5  # Changed temperature
        )
        
        response = agents_api.edit_existing_custom_agent_agents_edit_post(edit_request)
        
        if response.success:
            print("✅ Agent edited successfully!")
            print(f"   Agent ID: {response.agent_id}")
            print(f"   Message: {response.msg}")
            print(f"   Success: {response.success}")
            
            return response
        else:
            print(f"❌ Failed to edit agent: {response.msg}")
            return None
        
    except ApiException as e:
        print(f"❌ API Error editing agent: {e}")
        return None
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None

def clone_agent_example(agent_id):
    """CLONE: Clone an existing agent"""
    print("\n" + "=" * 60)
    print("🔄 CLONE AGENT EXAMPLE")
    print("=" * 60)
    
    if not test_project_id or not agent_id:
        print("❌ No test project or agent ID available")
        return None
    
    try:
        # Clone the existing agent
        clone_request = odin_sdk.CloneExistingCustomAgentRequest(
            project_id=test_project_id,
            agent_id=agent_id,
            agent_name="Cloned CRUD Test Agent"
        )
        
        response = agents_api.clone_existing_custom_agent_agents_clone_post(clone_request)
        
        cloned_agent_id = response.agent_id
        created_agent_ids.append(cloned_agent_id)
        
        print("✅ Agent cloned successfully!")
        print(f"   Original Agent ID: {agent_id}")
        print(f"   Cloned Agent ID: {cloned_agent_id}")
        print(f"   Message: {response.msg}")
        
        return cloned_agent_id
        
    except ApiException as e:
        print(f"❌ API Error cloning agent: {e}")
        return None
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None

def delete_agent_example(agent_id):
    """DELETE: Delete an agent"""
    print(f"\n🗑️ Deleting agent: {agent_id}")
    print("=" * 60)
    print("🗑️ DELETE AGENT EXAMPLE")
    print("=" * 60)
    
    if not test_project_id or not agent_id:
        print("❌ No test project or agent ID available")
        return False
    
    try:
        # Delete the agent
        delete_request = odin_sdk.DeleteCustomAgentRequest(
            project_id=test_project_id,
            agent_id=agent_id
        )
        
        response = agents_api.delete_custom_agent_agents_delete_delete(delete_request)
        
        print("✅ Agent deleted successfully!")
        print(f"   Agent ID: {agent_id}")
        print(f"   Response: {response}")
        
        # Remove from tracking list
        if agent_id in created_agent_ids:
            created_agent_ids.remove(agent_id)
            
        return True
        
    except ApiException as e:
        print(f"❌ API Error deleting agent: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def list_default_agents_example():
    """READ: List default/system agents"""
    print("\n" + "=" * 60)
    print("🏭 LIST DEFAULT AGENTS EXAMPLE")
    print("=" * 60)
    
    try:
        # List default agents
        response = agents_api.list_default_agents_agents_list_default_get()
        
        print("✅ Default agents list retrieved successfully!")
        
        if hasattr(response, 'agents') and response.agents:
            print(f"   Total default agents: {len(response.agents)}")
            
            for i, agent in enumerate(response.agents[:3], 1):  # Show first 3
                print(f"\n   🏭 Default Agent {i}:")
                print(f"      Name: {agent.name if hasattr(agent, 'name') else 'N/A'}")
                print(f"      Type: {agent.type if hasattr(agent, 'type') else 'N/A'}")
                if hasattr(agent, 'description'):
                    print(f"      Description: {agent.description}")
        else:
            print("   No default agents found or different response structure")
            print(f"   Response: {response}")
        
        return response
        
    except ApiException as e:
        print(f"❌ API Error listing default agents: {e}")
        return None
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None

def cleanup_created_agents():
    """Clean up all agents created during this run"""
    print("\n" + "=" * 60)
    print("🧹 CLEANUP - DELETING ALL CREATED AGENTS")
    print("=" * 60)
    
    if not created_agent_ids:
        print("No agents to clean up")
        return
    
    for agent_id in created_agent_ids.copy():
        success = delete_agent_example(agent_id)
        if success:
            print(f"✅ Successfully cleaned up agent: {agent_id}")
        else:
            print(f"⚠️ Failed to clean up agent: {agent_id}")
        time.sleep(0.5)  # Brief pause between deletions

def cleanup_test_project():
    """Clean up the test project"""
    print("\n🗑️ Cleaning up test project...")
    
    global test_project_id
    
    if not test_project_id:
        print("No test project to clean up")
        return
    
    try:
        delete_request = odin_sdk.DeleteProjectRequest(project_id=test_project_id)
        response = projects_api.delete_project_project_delete_delete(delete_request)
        
        print(f"✅ Test project cleaned up: {test_project_id}")
        test_project_id = None
        
    except ApiException as e:
        print(f"⚠️ Failed to delete test project: {e}")
    except Exception as e:
        print(f"⚠️ Error deleting test project: {e}")

def main():
    """Run all Agents CRUD examples"""
    print("🚀 ODIN SDK - Agents CRUD Examples (Fixed & Idempotent)")
    print("Using localhost:8001 with local API keys")
    
    # CREATE test project
    project_id = create_test_project()
    if not project_id:
        print("❌ Failed to create test project. Stopping examples.")
        return
    
    time.sleep(2)  # Wait for project to be ready
    
    # READ - List default agents first
    default_agents = list_default_agents_example()
    time.sleep(1)
    
    # CREATE operations
    agent_id = create_agent_example()
    time.sleep(2)
    
    # READ operations
    agents_list = list_agents_example()
    time.sleep(1)
    
    if agent_id:
        agent_details = get_agent_example(agent_id)
        time.sleep(1)
        
        # UPDATE operations
        edit_response = edit_agent_example(agent_id)
        time.sleep(1)
        
        # Re-read to confirm update
        print("\n📖 Reading agents list after update:")
        list_agents_example()
        time.sleep(1)
        
        # CLONE operations
        cloned_agent_id = clone_agent_example(agent_id)
        time.sleep(1)
        
        # Re-read to confirm clone
        print("\n📖 Reading agents list after cloning:")
        list_agents_example()
    
    time.sleep(1)
    
    # CLEANUP
    cleanup_created_agents()
    cleanup_test_project()
    
    print("\n" + "=" * 60)
    print("✅ AGENTS CRUD EXAMPLES COMPLETED!")
    print("=" * 60)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n🛑 Script interrupted by user")
        print("🧹 Performing emergency cleanup...")
        cleanup_created_agents()
        cleanup_test_project()
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error in main: {e}")
        print("🧹 Performing emergency cleanup...")
        cleanup_created_agents()
        cleanup_test_project()
        sys.exit(1) 