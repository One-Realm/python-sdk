"""
ODIN SDK - Chats CRUD Examples (Fixed & Idempotent)
Demonstrates Create, Read, Update, Delete operations for chats using localhost:8001
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
chat_api = odin_sdk.ChatApi(api_client)
projects_api = odin_sdk.ProjectsApi(api_client)

# Set headers for authentication
api_client.default_headers["x-api-key"] = API_KEY
api_client.default_headers["x-api-secret"] = API_SECRET

# Global variables to track created resources for cleanup
test_project_id = None
created_chat_ids = []

def create_test_project():
    """Create a test project for chat operations"""
    print("🔧 Creating test project for Chats CRUD operations...")
    
    global test_project_id
    
    try:
        # Clean up any existing test project first
        try:
            response = projects_api.get_projects_projects_get()
            for project in response.projects:
                if project.name == "Chats CRUD Test Project":
                    delete_request = odin_sdk.DeleteProjectRequest(project_id=project.id)
                    projects_api.delete_project_project_delete_delete(delete_request)
                    print(f"   ✅ Cleaned up existing project: {project.id}")
                    time.sleep(1)
        except Exception as e:
            print(f"   ⚠️ Error during cleanup: {e}")
        
        # Create new test project
        create_request = odin_sdk.CreateProjectRequest(
            project_name="Chats CRUD Test Project",
            project_description="Test project for demonstrating Chats CRUD operations",
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

def create_chat_example():
    """CREATE: Create a new chat"""
    print("\n" + "=" * 60)
    print("💬 CREATE CHAT EXAMPLE")
    print("=" * 60)
    
    if not test_project_id:
        print("❌ No test project available")
        return None
    
    try:
        # Create a new chat
        chat_request = odin_sdk.CreateChatPromptRequest(
            project_id=test_project_id,
            name="CRUD Test Chat",
            context="This is a test chat created for demonstrating CRUD operations with the ODIN SDK",
            metadata={
                "purpose": "testing",
                "created_by": "crud_example",
                "version": "1.0"
            }
        )
        
        response = chat_api.create_chat_chat_create_post(chat_request)
        
        chat_id = response.chat_id
        created_chat_ids.append(chat_id)
        
        print("✅ Chat created successfully!")
        print(f"   Chat ID: {chat_id}")
        print(f"   Chat Name: {response.name}")
        print(f"   Created At: {response.created_at}")
        if response.metadata:
            print(f"   Metadata: {response.metadata}")
        
        return chat_id
        
    except ApiException as e:
        print(f"❌ API Error creating chat: {e}")
        return None
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None

def send_message_example(chat_id):
    """CREATE: Send a message to the chat"""
    print("\n" + "=" * 60)
    print("📤 SEND MESSAGE EXAMPLE")
    print("=" * 60)
    
    if not test_project_id or not chat_id:
        print("❌ No test project or chat ID available")
        return None
    
    try:
        # Send a message to the chat using the multipart form method
        response = chat_api.send_message_chat_message_post(
            message="Hello! This is a test message for the CRUD example. Can you tell me about the ODIN platform?",
            project_id=test_project_id,
            chat_id=chat_id,
            chat_name="CRUD Test Chat",
            use_knowledgebase=True,
            ai_response=True,
            return_message=True,
            model_name="gpt-4",
            skip_stream=True  # Don't stream the response for testing
        )
        
        print("✅ Message sent successfully!")
        print(f"   Chat ID: {chat_id}")
        if hasattr(response, 'message_id'):
            print(f"   Message ID: {response.message_id}")
        if hasattr(response, 'message'):
            print(f"   Response Preview: {str(response.message)[:100]}...")
        print(f"   Full Response: {response}")
        
        return response
        
    except ApiException as e:
        print(f"❌ API Error sending message: {e}")
        return None
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None

def get_chats_example():
    """READ: Get all chats in the project"""
    print("\n" + "=" * 60)
    print("📋 GET CHATS EXAMPLE")
    print("=" * 60)
    
    if not test_project_id:
        print("❌ No test project available")
        return None
    
    try:
        # Get all chats in the project
        response = chat_api.get_chats_project_project_id_chat_get(test_project_id, limit=10)
        
        print("✅ Chats list retrieved successfully!")
        
        if hasattr(response, 'chats') and response.chats:
            print(f"   Total chats: {len(response.chats)}")
            
            for i, chat in enumerate(response.chats, 1):
                print(f"\n   💬 Chat {i}:")
                print(f"      ID: {chat.id if hasattr(chat, 'id') else 'N/A'}")
                print(f"      Name: {chat.name if hasattr(chat, 'name') else 'N/A'}")
                if hasattr(chat, 'created_at'):
                    print(f"      Created At: {chat.created_at}")
                if hasattr(chat, 'updated_at'):
                    print(f"      Updated At: {chat.updated_at}")
                if hasattr(chat, 'message_count'):
                    print(f"      Message Count: {chat.message_count}")
        else:
            print("   No chats found or different response structure")
            print(f"   Response: {response}")
        
        return response
        
    except ApiException as e:
        print(f"❌ API Error getting chats: {e}")
        return None
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None

def get_chats_v2_example():
    """READ: Get all chats using V2 API (page-based pagination)"""
    print("\n" + "=" * 60)
    print("📋 GET CHATS V2 EXAMPLE")
    print("=" * 60)
    
    if not test_project_id:
        print("❌ No test project available")
        return None
    
    try:
        # Get all chats using V2 API
        response = chat_api.get_chats_v2_v2_project_project_id_chat_get(
            test_project_id, 
            page=1, 
            page_size=10
        )
        
        print("✅ Chats list (V2) retrieved successfully!")
        
        if hasattr(response, 'chats') and response.chats:
            print(f"   Total chats on page: {len(response.chats)}")
            
            for i, chat in enumerate(response.chats, 1):
                print(f"\n   💬 Chat {i}:")
                if hasattr(chat, 'id'):
                    print(f"      ID: {chat.id}")
                if hasattr(chat, 'name'):
                    print(f"      Name: {chat.name}")
                if hasattr(chat, 'created_at'):
                    print(f"      Created At: {chat.created_at}")
        else:
            print(f"   Response structure: {response}")
        
        return response
        
    except ApiException as e:
        print(f"❌ API Error getting chats V2: {e}")
        return None
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None

def get_specific_chat_example(chat_id):
    """READ: Get a specific chat"""
    print("\n" + "=" * 60)
    print("🔍 GET SPECIFIC CHAT EXAMPLE")
    print("=" * 60)
    
    if not test_project_id or not chat_id:
        print("❌ No test project or chat ID available")
        return None
    
    try:
        # Get specific chat details
        response = chat_api.get_chat_project_project_id_chat_chat_id_get(test_project_id, chat_id)
        
        print("✅ Chat details retrieved successfully!")
        print(f"   Chat ID: {chat_id}")
        print(f"   Response: {response}")
        
        return response
        
    except ApiException as e:
        print(f"❌ API Error getting specific chat: {e}")
        return None
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None

def get_chat_history_example(chat_id):
    """READ: Get full chat history"""
    print("\n" + "=" * 60)
    print("📜 GET CHAT HISTORY EXAMPLE")
    print("=" * 60)
    
    if not test_project_id or not chat_id:
        print("❌ No test project or chat ID available")
        return None
    
    try:
        # Get all messages in the chat
        response = chat_api.get_chat_all_project_project_id_chat_chat_id_all_get(test_project_id, chat_id)
        
        print("✅ Chat history retrieved successfully!")
        print(f"   Chat ID: {chat_id}")
        
        if hasattr(response, 'messages') and response.messages:
            print(f"   Total messages: {len(response.messages)}")
            
            for i, message in enumerate(response.messages[:3], 1):  # Show first 3 messages
                print(f"\n   📩 Message {i}:")
                if hasattr(message, 'id'):
                    print(f"      Message ID: {message.id}")
                if hasattr(message, 'content'):
                    print(f"      Content: {str(message.content)[:100]}...")
                if hasattr(message, 'role'):
                    print(f"      Role: {message.role}")
                if hasattr(message, 'timestamp'):
                    print(f"      Timestamp: {message.timestamp}")
        else:
            print(f"   Response structure: {response}")
        
        return response
        
    except ApiException as e:
        print(f"❌ API Error getting chat history: {e}")
        return None
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None

def update_chat_name_example(chat_id):
    """UPDATE: Update chat name"""
    print("\n" + "=" * 60)
    print("✏️ UPDATE CHAT NAME EXAMPLE")
    print("=" * 60)
    
    if not test_project_id or not chat_id:
        print("❌ No test project or chat ID available")
        return None
    
    try:
        # Update chat name
        update_request = odin_sdk.ChatUpdateName(
            project_id=test_project_id,
            chat_id=chat_id,
            title="CRUD Test Chat (Updated)"
        )
        
        response = chat_api.update_chat_name_chat_update_name_post(update_request)
        
        print("✅ Chat name updated successfully!")
        print(f"   Chat ID: {chat_id}")
        print(f"   New Title: CRUD Test Chat (Updated)")
        print(f"   Response: {response}")
        
        return response
        
    except ApiException as e:
        print(f"❌ API Error updating chat name: {e}")
        return None
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None

def delete_chat_example(chat_id):
    """DELETE: Delete a chat"""
    print(f"\n🗑️ Deleting chat: {chat_id}")
    print("=" * 60)
    print("🗑️ DELETE CHAT EXAMPLE")
    print("=" * 60)
    
    if not test_project_id or not chat_id:
        print("❌ No test project or chat ID available")
        return False
    
    try:
        # Delete the chat
        delete_request = odin_sdk.DeleteChatRequest(
            project_id=test_project_id,
            chat_id=chat_id
        )
        
        response = chat_api.delete_chat_chat_delete_delete(delete_request)
        
        print("✅ Chat deleted successfully!")
        print(f"   Chat ID: {chat_id}")
        print(f"   Response: {response}")
        
        # Remove from tracking list
        if chat_id in created_chat_ids:
            created_chat_ids.remove(chat_id)
            
        return True
        
    except ApiException as e:
        print(f"❌ API Error deleting chat: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def get_default_models_example():
    """READ: List default chat models available"""
    print("\n" + "=" * 60)
    print("🤖 GET DEFAULT MODELS EXAMPLE")
    print("=" * 60)
    
    try:
        # List default models
        response = chat_api.get_default_models_chat_models_get()
        
        print("✅ Default models retrieved successfully!")
        
        if hasattr(response, 'models') and response.models:
            print(f"   Total models: {len(response.models)}")
            
            for i, model in enumerate(response.models[:5], 1):  # Show first 5
                print(f"\n   🤖 Model {i}:")
                if hasattr(model, 'name'):
                    print(f"      Name: {model.name}")
                if hasattr(model, 'provider'):
                    print(f"      Provider: {model.provider}")
                if hasattr(model, 'description'):
                    print(f"      Description: {model.description}")
        else:
            print("   No models found or different response structure")
            print(f"   Response: {response}")
        
        return response
        
    except ApiException as e:
        print(f"❌ API Error getting default models: {e}")
        return None
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None

def cleanup_created_chats():
    """Clean up all chats created during this run"""
    print("\n" + "=" * 60)
    print("🧹 CLEANUP - DELETING ALL CREATED CHATS")
    print("=" * 60)
    
    if not created_chat_ids:
        print("No chats to clean up")
        return
    
    for chat_id in created_chat_ids.copy():
        success = delete_chat_example(chat_id)
        if success:
            print(f"✅ Successfully cleaned up chat: {chat_id}")
        else:
            print(f"⚠️ Failed to clean up chat: {chat_id}")
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
    """Run all Chats CRUD examples"""
    print("🚀 ODIN SDK - Chats CRUD Examples (Fixed & Idempotent)")
    print("Using localhost:8001 with local API keys")
    
    # CREATE test project
    project_id = create_test_project()
    if not project_id:
        print("❌ Failed to create test project. Stopping examples.")
        return
    
    time.sleep(2)  # Wait for project to be ready
    
    # READ - List default models first
    default_models = get_default_models_example()
    time.sleep(1)
    
    # CREATE operations
    chat_id = create_chat_example()
    time.sleep(2)
    
    # READ operations
    chats_list = get_chats_example()
    time.sleep(1)
    
    chats_v2_list = get_chats_v2_example()
    time.sleep(1)
    
    if chat_id:
        chat_details = get_specific_chat_example(chat_id)
        time.sleep(1)
        
        # SEND MESSAGE (another CREATE operation)
        message_response = send_message_example(chat_id)
        time.sleep(3)  # Wait for message processing
        
        # READ chat history after sending message
        chat_history = get_chat_history_example(chat_id)
        time.sleep(1)
        
        # UPDATE operations
        update_response = update_chat_name_example(chat_id)
        time.sleep(1)
        
        # Re-read to confirm update
        print("\n📖 Reading chats list after name update:")
        get_chats_example()
    
    time.sleep(1)
    
    # CLEANUP
    cleanup_created_chats()
    cleanup_test_project()
    
    print("\n" + "=" * 60)
    print("✅ CHATS CRUD EXAMPLES COMPLETED!")
    print("=" * 60)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n🛑 Script interrupted by user")
        print("🧹 Performing emergency cleanup...")
        cleanup_created_chats()
        cleanup_test_project()
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error in main: {e}")
        print("🧹 Performing emergency cleanup...")
        cleanup_created_chats()
        cleanup_test_project()
        sys.exit(1) 