"""
ODIN SDK - PDF Upload Example
Demonstrates uploading a PDF file to the knowledge base using localhost:8001
Uploads the attention_paper.pdf file and shows the complete process.
"""
import odin_sdk
from odin_sdk.rest import ApiException
import time
import sys
import os

# Configuration
HOST = "http://localhost:8001"
API_KEY = "b13cc8df-e33a-4828-a86c-0be3c96dcd0a"
API_SECRET = "IHeKHeRVZawSzl4wmjexf3e4/i3w8CxfzVqAMMGT2Y0="

# File to upload
PDF_FILE_PATH = "attention_paper.pdf"

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
uploaded_document_key = None

def check_pdf_file():
    """Check if the PDF file exists"""
    if not os.path.exists(PDF_FILE_PATH):
        print(f"❌ PDF file not found: {PDF_FILE_PATH}")
        print("   Make sure you're running this from the examples directory")
        return False
    
    file_size = os.path.getsize(PDF_FILE_PATH)
    print(f"✅ PDF file found: {PDF_FILE_PATH}")
    print(f"   File size: {file_size:,} bytes ({file_size/1024/1024:.2f} MB)")
    return True

def create_test_project():
    """Create a test project for PDF upload"""
    print("\n🔧 Creating test project for PDF upload...")
    
    global test_project_id
    
    try:
        # Clean up any existing test project first
        try:
            response = projects_api.get_projects_projects_get()
            for project in response.projects:
                if project.name == "PDF Upload Test Project":
                    delete_request = odin_sdk.DeleteProjectRequest(project_id=project.id)
                    projects_api.delete_project_project_delete_delete(delete_request)
                    print(f"   ✅ Cleaned up existing project: {project.id}")
                    time.sleep(1)
        except Exception as e:
            print(f"   ⚠️ Error during cleanup: {e}")
        
        # Create new test project
        create_request = odin_sdk.CreateProjectRequest(
            project_name="PDF Upload Test Project",
            project_description="Test project for demonstrating PDF upload to knowledge base",
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

def upload_pdf_example():
    """Upload the PDF file to knowledge base"""
    print("\n" + "=" * 60)
    print("📄 UPLOAD PDF TO KNOWLEDGE BASE EXAMPLE")
    print("=" * 60)
    
    if not test_project_id:
        print("❌ No test project available")
        return None
    
    try:
        # Read the PDF file
        with open(PDF_FILE_PATH, 'rb') as pdf_file:
            file_content = pdf_file.read()
        
        print(f"📖 Read PDF file: {len(file_content):,} bytes")
        
        # Upload using the v3 endpoint (matches the curl command)
        response = kb_api.add_file_to_knowledge_base_v3_v3_project_knowledge_add_file_post(
            file=file_content,
            project_id=test_project_id,
            metadata={},  # Empty metadata like in curl command
            file_type="application/pdf",
            path="/",  # Root path like in curl command
            is_quick_upload=False,  # Matches curl command
            force=True  # Force upload if file exists
        )
        
        global uploaded_document_key
        uploaded_document_key = response.document_key
        
        print("✅ PDF uploaded successfully to knowledge base!")
        print(f"   Document Key: {uploaded_document_key}")
        print(f"   Message: {response.message}")
        print(f"   Status: {response.status}")
        print(f"   URL: {response.url}")
        
        if hasattr(response, 'content') and response.content:
            content_preview = response.content[:200] + "..." if len(response.content) > 200 else response.content
            print(f"   Content Preview: {content_preview}")
        
        return uploaded_document_key
        
    except ApiException as e:
        print(f"❌ API Error uploading PDF: {e}")
        return None
    except FileNotFoundError:
        print(f"❌ PDF file not found: {PDF_FILE_PATH}")
        return None
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None

def check_upload_status():
    """Check if the uploaded file appears in knowledge base"""
    print("\n" + "=" * 60)
    print("🔍 CHECK UPLOAD STATUS")
    print("=" * 60)
    
    if not test_project_id:
        print("❌ No test project available")
        return None
    
    try:
        # Get knowledge base contents to verify upload
        response = kb_api.get_knowledge_base_project_project_id_knowledge_get(test_project_id)
        
        print("✅ Knowledge base retrieved successfully!")
        print(f"   Total documents: {len(response.knowledge_base)}")
        
        # Look for our uploaded PDF
        pdf_found = False
        for key, item in response.knowledge_base.items():
            print(f"\n   📄 Document: {key}")
            print(f"      Type: {item.doc_type}")
            print(f"      URL: {item.url}")
            print(f"      Status: {item.status}")
            
            if "attention_paper.pdf" in item.url or key == uploaded_document_key:
                pdf_found = True
                print(f"      ✅ This is our uploaded PDF!")
                
            if item.upload_date:
                print(f"      Upload Date: {item.upload_date}")
            if item.metadata:
                print(f"      Metadata: {item.metadata}")
        
        if pdf_found:
            print(f"\n✅ PDF found in knowledge base!")
        else:
            print(f"\n⚠️ PDF not found in knowledge base yet (may still be processing)")
        
        return response.knowledge_base
        
    except ApiException as e:
        print(f"❌ API Error checking knowledge base: {e}")
        return None
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None

def cleanup_uploaded_document():
    """Clean up the uploaded document"""
    print("\n🗑️ Cleaning up uploaded document...")
    
    if not test_project_id or not uploaded_document_key:
        print("No document to clean up")
        return
    
    try:
        # Remove document from knowledge base using query parameters
        response = kb_api.remove_from_knowledge_base_project_knowledge_remove_delete(
            name=uploaded_document_key,
            project_id=test_project_id
        )
        
        print(f"✅ Document cleaned up: {uploaded_document_key}")
        
    except ApiException as e:
        print(f"⚠️ Failed to delete document (API Error): {e}")
        # Since we're deleting the project anyway, this isn't critical
        print("   📝 Note: Document will be deleted when project is removed")
    except Exception as e:
        print(f"⚠️ Error deleting document (SDK issue): {e}")
        # Since we're deleting the project anyway, this isn't critical  
        print("   📝 Note: Document will be deleted when project is removed")

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
    """Run the PDF upload example"""
    print("🚀 ODIN SDK - PDF Upload Example")
    print("Uploading attention_paper.pdf to knowledge base")
    print("Using localhost:8001 with local API keys")
    print("=" * 60)
    
    # Check if PDF file exists
    if not check_pdf_file():
        return
    
    # CREATE test project
    project_id = create_test_project()
    if not project_id:
        print("❌ Failed to create test project. Stopping example.")
        return
    
    time.sleep(2)  # Wait for project to be ready
    
    # UPLOAD PDF
    document_key = upload_pdf_example()
    
    if document_key:
        time.sleep(3)  # Wait for upload processing
        
        # CHECK upload status
        check_upload_status()
        
        time.sleep(2)
        
        print(f"\n🎉 PDF upload completed successfully!")
        print(f"   Document Key: {document_key}")
        print(f"   Project ID: {project_id}")
        print(f"   The PDF is now available in the knowledge base for AI queries")
    else:
        print(f"\n❌ PDF upload failed")
    
    # CLEANUP
    cleanup_uploaded_document()
    cleanup_test_project()
    
    print("\n" + "=" * 60)
    print("✅ PDF UPLOAD EXAMPLE COMPLETED!")
    print("=" * 60)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n🛑 Script interrupted by user")
        print("🧹 Performing emergency cleanup...")
        cleanup_uploaded_document()
        cleanup_test_project()
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error in main: {e}")
        print("🧹 Performing emergency cleanup...")
        cleanup_uploaded_document()
        cleanup_test_project()
        sys.exit(1) 