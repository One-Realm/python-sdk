"""
ODIN SDK - Projects CRUD Examples (Fixed & Idempotent)
Demonstrates Create, Read, Update, Delete operations for projects using localhost:8001
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
projects_api = odin_sdk.ProjectsApi(api_client)

# Set headers for authentication
api_client.default_headers["x-api-key"] = API_KEY
api_client.default_headers["x-api-secret"] = API_SECRET

# Global variable to track created project IDs for cleanup
created_project_ids = []

def cleanup_existing_test_projects():
    """Clean up any existing test projects from previous runs"""
    print("🧹 Cleaning up any existing test projects from previous runs...")
    try:
        # Get all projects - correct method name
        response = projects_api.get_projects_projects_get()
        
        test_project_names = [
            "Test Project - CRUD Example",
            "Updated Test Project - CRUD Example", 
            "Cloned Test Project - CRUD Example"
        ]
        
        for project in response.projects:
            if project.name in test_project_names:
                try:
                    delete_request = odin_sdk.DeleteProjectRequest(project_id=project.id)
                    projects_api.delete_project_project_delete_delete(delete_request)
                    print(f"   ✅ Cleaned up existing project: {project.name} (ID: {project.id})")
                except ApiException as e:
                    print(f"   ⚠️ Could not delete existing project {project.name}: {e}")
                except Exception as e:
                    print(f"   ⚠️ Error deleting existing project {project.name}: {e}")
                    
    except Exception as e:
        print(f"   ⚠️ Could not list projects for cleanup: {e}")

def create_project_example():
    """CREATE: Create a new project"""
    print("=" * 60)
    print("🔧 CREATE PROJECT EXAMPLE")
    print("=" * 60)
    
    try:
        # Create project request
        create_request = odin_sdk.CreateProjectRequest(
            project_name="Test Project - CRUD Example",
            project_description="A comprehensive test project for demonstrating CRUD operations",
            project_type="kb_chat"
        )
        
        response = projects_api.create_project_project_create_post(create_request)
        project_id = response.project_id
        created_project_ids.append(project_id)
        
        print("✅ Project created successfully!")
        print(f"   Project ID: {project_id}")
        print(f"   Project Name: {response.project.name}")
        print(f"   Project Type: {response.project.type}")
        print(f"   Description: {response.project.description}")
        print(f"   Created At: {response.project.created_at}")
        
        return project_id
        
    except ApiException as e:
        print(f"❌ API Error creating project: {e}")
        return None
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None

def read_project_example(project_id):
    """READ: Get project details"""
    print("\n" + "=" * 60)
    print("📖 READ PROJECT EXAMPLE")
    print("=" * 60)
    
    try:
        response = projects_api.get_project_project_project_id_get(project_id)
        
        print("✅ Project retrieved successfully!")
        # GetProjectResponse has project_data, not project
        project_data = response.project_data
        print(f"   Project ID: {project_data.get('id', 'N/A')}")
        print(f"   Project Name: {project_data.get('name', 'N/A')}")
        print(f"   Project Type: {project_data.get('type', 'N/A')}")
        print(f"   Description: {project_data.get('description', 'N/A')}")
        print(f"   Owner: {project_data.get('owner', 'N/A')}")
        print(f"   Created At: {project_data.get('created_at', 'N/A')}")
        
        return project_data
        
    except ApiException as e:
        print(f"❌ API Error reading project: {e}")
        return None
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None

def list_projects_example():
    """READ: List all projects"""
    print("\n" + "=" * 60)
    print("📋 LIST PROJECTS EXAMPLE")
    print("=" * 60)
    
    try:
        response = projects_api.get_projects_projects_get()
        
        print(f"✅ Found {len(response.projects)} projects:")
        for project in response.projects[:10]:  # Show first 10
            print(f"   - {project.name} (ID: {project.id}) - Type: {project.type}")
        
        if len(response.projects) > 10:
            print(f"   ... and {len(response.projects) - 10} more projects")
            
        return response.projects
        
    except ApiException as e:
        print(f"❌ API Error listing projects: {e}")
        return []
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return []

def update_project_example(project_id):
    """UPDATE: Modify project details"""
    print("\n" + "=" * 60)
    print("✏️ UPDATE PROJECT EXAMPLE")
    print("=" * 60)
    
    try:
        # Correct method name: update_project_project_update_post
        update_request = odin_sdk.UpdateProjectRequest(
            project_id=project_id,
            name="Updated Test Project - CRUD Example",
            description="Updated description for the comprehensive test project",
            model_name="gpt-4"
        )
        
        response = projects_api.update_project_project_update_post(update_request)
        
        print("✅ Project updated successfully!")
        print(f"   Updated project response: {response}")
        
        return response
        
    except ApiException as e:
        print(f"❌ API Error updating project: {e}")
        return None
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None

def clone_project_example(original_project_id):
    """CLONE: Clone an existing project"""
    print("\n" + "=" * 60)
    print("📋 CLONE PROJECT EXAMPLE")
    print("=" * 60)
    
    try:
        # Correct field name: new_project_name (not name)
        clone_request = odin_sdk.CloneProjectRequest(
            project_id=original_project_id,
            new_project_name="Cloned Test Project - CRUD Example"
        )
        
        response = projects_api.clone_project_project_clone_post(clone_request)
        cloned_project_id = response.new_project_id  # Correct field name
        created_project_ids.append(cloned_project_id)
        
        print("✅ Project cloned successfully!")
        print(f"   Original Project ID: {original_project_id}")
        print(f"   Cloned Project ID: {cloned_project_id}")
        print(f"   Clone response: {response}")
        
        return cloned_project_id
        
    except ApiException as e:
        print(f"❌ API Error cloning project: {e}")
        return None
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None

def delete_project_example(project_id):
    """DELETE: Remove a project"""
    print(f"\n🗑️ Deleting project: {project_id}")
    print("=" * 60)
    print("🗑️ DELETE PROJECT EXAMPLE")
    print("=" * 60)
    
    try:
        # Correct method name: delete_project_project_delete_delete
        delete_request = odin_sdk.DeleteProjectRequest(project_id=project_id)
        response = projects_api.delete_project_project_delete_delete(delete_request)
        
        print("✅ Project deleted successfully!")
        print(f"   Deleted project ID: {project_id}")
        print(f"   Delete response: {response}")
        
        # Remove from tracking list
        if project_id in created_project_ids:
            created_project_ids.remove(project_id)
            
        return True
        
    except ApiException as e:
        print(f"❌ API Error deleting project: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def cleanup_created_projects():
    """Clean up all projects created during this run"""
    print("\n" + "=" * 60)
    print("🧹 CLEANUP - DELETING ALL CREATED PROJECTS")
    print("=" * 60)
    
    for project_id in created_project_ids.copy():
        success = delete_project_example(project_id)
        if success:
            print(f"✅ Successfully cleaned up project: {project_id}")
        else:
            print(f"⚠️ Failed to clean up project: {project_id}")
        time.sleep(0.5)  # Brief pause between deletions

def main():
    """Run all CRUD examples"""
    print("🚀 ODIN SDK - Projects CRUD Examples (Fixed & Idempotent)")
    print("Using localhost:8001 with local API keys")
    
    # Clean up any existing test projects first
    cleanup_existing_test_projects()
    time.sleep(1)
    
    # CREATE
    project_id = create_project_example()
    if not project_id:
        print("❌ Failed to create project. Stopping examples.")
        return
    
    time.sleep(1)
    
    # READ
    project_data = read_project_example(project_id)
    time.sleep(1)
    
    # LIST
    all_projects = list_projects_example()
    time.sleep(1)
    
    # UPDATE
    update_response = update_project_example(project_id)
    time.sleep(1)
    
    # Re-read to confirm update
    print("\n📖 Reading updated project:")
    read_project_example(project_id)
    time.sleep(1)
    
    # CLONE
    cloned_project_id = clone_project_example(project_id)
    time.sleep(1)
    
    # List projects to show the cloned project
    print("\n📋 Listing projects after cloning:")
    list_projects_example()
    time.sleep(1)
    
    # CLEANUP
    cleanup_created_projects()
    
    print("\n" + "=" * 60)
    print("✅ PROJECTS CRUD EXAMPLES COMPLETED!")
    print("=" * 60)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n🛑 Script interrupted by user")
        print("🧹 Performing emergency cleanup...")
        cleanup_created_projects()
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error in main: {e}")
        print("🧹 Performing emergency cleanup...")
        cleanup_created_projects()
        sys.exit(1) 