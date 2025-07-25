"""
ODIN SDK - Knowledge Base CRUD Examples (Fixed & Idempotent)
Demonstrates Create, Read, Update, Delete operations for knowledge base using localhost:8001
All operations are idempotent and include proper cleanup.
"""
import odin_sdk
from odin_sdk.rest import ApiException
import time
import sys
import tempfile
import os

# Configuration
HOST = "http://localhost:8001"
API_KEY = "b13cc8df-e33a-4828-a86c-0be3c96dcd0a"
API_SECRET = "IHeKHeRVZawSzl4wmjexf3e4/i3w8CxfzVqAMMGT2Y0="

# Initialize the API client
configuration = odin_sdk.Configuration(host=HOST)
api_client = odin_sdk.ApiClient(configuration)
kb_api = odin_sdk.KnowledgeBaseApi(api_client)
projects_api = odin_sdk.ProjectsApi(api_client)

# Set headers for authentication
api_client.default_headers["x-api-key"] = API_KEY
api_client.default_headers["x-api-secret"] = API_SECRET

# Global variables to track created resources for cleanup
test_project_id = None
created_document_keys = []

def create_test_project():
    """Create a test project for knowledge base operations"""
    print("🔧 Creating test project for Knowledge Base CRUD operations...")
    
    global test_project_id
    
    try:
        # Clean up any existing test project first
        try:
            response = projects_api.get_projects_projects_get()
            for project in response.projects:
                if project.name == "KB CRUD Test Project":
                    delete_request = odin_sdk.DeleteProjectRequest(project_id=project.id)
                    projects_api.delete_project_project_delete_delete(delete_request)
                    print(f"   ✅ Cleaned up existing project: {project.id}")
                    time.sleep(1)
        except Exception as e:
            print(f"   ⚠️ Error during cleanup: {e}")
        
        # Create new test project
        create_request = odin_sdk.CreateProjectRequest(
            project_name="KB CRUD Test Project",
            project_description="Test project for demonstrating Knowledge Base CRUD operations",
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

def create_file_example():
    """CREATE: Add a file to knowledge base"""
    print("\n" + "=" * 60)
    print("📄 CREATE FILE IN KNOWLEDGE BASE EXAMPLE")
    print("=" * 60)
    
    if not test_project_id:
        print("❌ No test project available")
        return None
    
    try:
        # Create a sample file content
        file_content = """
# Sample Document for ODIN Knowledge Base

This is a sample document created for testing the Knowledge Base CRUD operations.

## Features Demonstrated

1. File creation and upload
2. Content processing
3. Metadata extraction
4. Document management

## Important Information

This document contains sample information to demonstrate how the ODIN Knowledge Base
processes and stores documents for retrieval and analysis.

The knowledge base can handle various file formats including:
- PDF documents
- Text files
- Word documents
- HTML content
- URLs and web pages

## Conclusion

This sample document helps test the complete CRUD functionality of the knowledge base system.
        """
        
        # Use the create file API method
        response = kb_api.create_file_in_knowledge_base_v2_project_knowledge_create_file_post(
            project_id=test_project_id,
            file_name="sample_document_crud_test",
            content=file_content,
            file_extension="md",
            metadata='{"category": "test", "source": "crud_example"}',
            force=True
        )
        
        document_key = response.document_key
        created_document_keys.append(document_key)
        
        print("✅ File created successfully in knowledge base!")
        print(f"   Document Key: {document_key}")
        print(f"   Message: {response.message}")
        print(f"   Content Preview: {response.content[:100]}...")
        print(f"   Status: {response.status}")
        
        return document_key
        
    except ApiException as e:
        print(f"❌ API Error creating file: {e}")
        return None
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None

def add_url_example():
    """CREATE: Add a URL to knowledge base"""
    print("\n" + "=" * 60)
    print("🌐 CREATE URL IN KNOWLEDGE BASE EXAMPLE")
    print("=" * 60)
    
    if not test_project_id:
        print("❌ No test project available")
        return None
    
    try:
        # Add a URL to the knowledge base
        response = kb_api.add_url_to_knowledge_base_v1_project_knowledge_add_url_post(
            project_id=test_project_id,
            url="https://docs.python.org/3/tutorial/",
            metadata='{"category": "documentation", "source": "crud_example"}'
        )
        
        document_key = response.document_key
        created_document_keys.append(document_key)
        
        print("✅ URL added successfully to knowledge base!")
        print(f"   Document Key: {document_key}")
        print(f"   Message: {response.message}")
        print(f"   URL: {response.url}")
        print(f"   Status: {response.status}")
        
        return document_key
        
    except ApiException as e:
        print(f"❌ API Error adding URL: {e}")
        return None
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None

def read_knowledge_base_example():
    """READ: Get knowledge base contents"""
    print("\n" + "=" * 60)
    print("📖 READ KNOWLEDGE BASE EXAMPLE")
    print("=" * 60)
    
    if not test_project_id:
        print("❌ No test project available")
        return None
    
    try:
        # Get knowledge base contents
        response = kb_api.get_knowledge_base_project_project_id_knowledge_get(test_project_id)
        
        print("✅ Knowledge base retrieved successfully!")
        print(f"   Total documents: {len(response.knowledge_base)}")
        
        # Display information about each document
        for key, item in response.knowledge_base.items():
            print(f"\n   📄 Document: {key}")
            print(f"      Type: {item.doc_type}")
            print(f"      URL: {item.url}")
            print(f"      Status: {item.status}")
            if item.upload_date:
                print(f"      Upload Date: {item.upload_date}")
            if item.metadata:
                print(f"      Metadata: {item.metadata}")
        
        return response.knowledge_base
        
    except ApiException as e:
        print(f"❌ API Error reading knowledge base: {e}")
        return None
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None

def get_knowledge_base_page_example():
    """READ: Get paginated knowledge base view"""
    print("\n" + "=" * 60)
    print("📋 GET KNOWLEDGE BASE PAGE EXAMPLE")
    print("=" * 60)
    
    if not test_project_id:
        print("❌ No test project available")
        return None
    
    try:
        # Create request for paginated view
        page_request = odin_sdk.GetKBPageRequest(
            page=1,
            items_per_page=10
        )
        
        response = kb_api.get_knowledge_base_page_project_project_id_knowledgebase_post(
            test_project_id, 
            page_request
        )
        
        print("✅ Knowledge base page retrieved successfully!")
        print(f"   Documents on this page: {len(response.docs)}")
        
        for i, doc in enumerate(response.docs, 1):
            print(f"\n   📄 Document {i}:")
            print(f"      Content Key: {doc.content_key}")
            print(f"      Type: {doc.doc_type}")
            if hasattr(doc, 'metadata') and doc.metadata:
                print(f"      Metadata: {doc.metadata}")
        
        if response.folders:
            print(f"   📁 Folders: {len(response.folders)}")
        
        if response.kb_info:
            print(f"   ℹ️ KB Info available")
        
        return response
        
    except ApiException as e:
        print(f"❌ API Error getting KB page: {e}")
        return None
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None

def update_metadata_example(document_key):
    """UPDATE: Update document metadata"""
    print("\n" + "=" * 60)
    print("✏️ UPDATE DOCUMENT METADATA EXAMPLE")
    print("=" * 60)
    
    if not test_project_id or not document_key:
        print("❌ No test project or document key available")
        return None
    
    try:
        # Update document metadata
        metadata_request = odin_sdk.KnowledgeBaseMetadataRequest(
            metadata={
                "category": "updated_test",
                "source": "crud_example_updated",
                "last_modified": "2025-01-21",
                "importance": "high"
            }
        )
        
        response = kb_api.change_knowledge_base_metadata_project_project_id_knowledge_document_name_metadata_patch(
            test_project_id,
            document_key,
            metadata_request
        )
        
        print("✅ Document metadata updated successfully!")
        print(f"   Document Key: {document_key}")
        print(f"   Response: {response}")
        
        return response
        
    except ApiException as e:
        print(f"❌ API Error updating metadata: {e}")
        return None
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None

def delete_document_example(document_key):
    """DELETE: Remove a document from knowledge base"""
    print(f"\n🗑️ Deleting document: {document_key}")
    print("=" * 60)
    print("🗑️ DELETE DOCUMENT EXAMPLE")
    print("=" * 60)
    
    if not test_project_id or not document_key:
        print("❌ No test project or document key available")
        return False
    
    try:
        # Remove document from knowledge base
        response = kb_api.remove_from_knowledge_base_project_knowledge_remove_delete(
            name=document_key,
            project_id=test_project_id
        )
        
        print("✅ Document deleted successfully!")
        print(f"   Document Key: {document_key}")
        print(f"   Response: {response}")
        
        # Remove from tracking list
        if document_key in created_document_keys:
            created_document_keys.remove(document_key)
            
        return True
        
    except ApiException as e:
        print(f"❌ API Error deleting document: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def cleanup_created_documents():
    """Clean up all documents created during this run"""
    print("\n" + "=" * 60)
    print("🧹 CLEANUP - DELETING ALL CREATED DOCUMENTS")
    print("=" * 60)
    
    if not created_document_keys:
        print("No documents to clean up")
        return
    
    for document_key in created_document_keys.copy():
        success = delete_document_example(document_key)
        if success:
            print(f"✅ Successfully cleaned up document: {document_key}")
        else:
            print(f"⚠️ Failed to clean up document: {document_key}")
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
    """Run all Knowledge Base CRUD examples"""
    print("🚀 ODIN SDK - Knowledge Base CRUD Examples (Fixed & Idempotent)")
    print("Using localhost:8001 with local API keys")
    
    # CREATE test project
    project_id = create_test_project()
    if not project_id:
        print("❌ Failed to create test project. Stopping examples.")
        return
    
    time.sleep(2)  # Wait for project to be ready
    
    # CREATE operations
    document_key1 = create_file_example()
    time.sleep(1)
    
    document_key2 = add_url_example()
    time.sleep(2)  # Wait for URL processing
    
    # READ operations
    knowledge_base = read_knowledge_base_example()
    time.sleep(1)
    
    kb_page = get_knowledge_base_page_example()
    time.sleep(1)
    
    # UPDATE operations
    if document_key1:
        update_response = update_metadata_example(document_key1)
        time.sleep(1)
        
        # Re-read to confirm update
        print("\n📖 Reading knowledge base after metadata update:")
        read_knowledge_base_example()
    
    time.sleep(1)
    
    # CLEANUP
    cleanup_created_documents()
    cleanup_test_project()
    
    print("\n" + "=" * 60)
    print("✅ KNOWLEDGE BASE CRUD EXAMPLES COMPLETED!")
    print("=" * 60)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n🛑 Script interrupted by user")
        print("🧹 Performing emergency cleanup...")
        cleanup_created_documents()
        cleanup_test_project()
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error in main: {e}")
        print("🧹 Performing emergency cleanup...")
        cleanup_created_documents()
        cleanup_test_project()
        sys.exit(1) 