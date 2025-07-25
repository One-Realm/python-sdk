import odin_sdk
from odin_sdk.rest import ApiException

# Initialize the API client
configuration = odin_sdk.Configuration(host="http://localhost:8001")
api_client = odin_sdk.ApiClient(configuration)
projects_api = odin_sdk.ProjectsApi(api_client)

api_client.default_headers["x-api-key"] = "b13cc8df-e33a-4828-a86c-0be3c96dcd0a"
api_client.default_headers["x-api-secret"] = "IHeKHeRVZawSzl4wmjexf3e4/i3w8CxfzVqAMMGT2Y0="

# API_KEY = "b13cc8df-e33a-4828-a86c-0be3c96dcd0a"
# API_SECRET = "IHeKHeRVZawSzl4wmjexf3e4/i3w8CxfzVqAMMGT2Y0="

# Create project request
create_request = odin_sdk.CreateProjectRequest(
    project_name="My AI Assistant Project New",
    project_description="A project for building an intelligent customer support assistant",
    project_type="kb_chat"  # Knowledge base chat project
)

try:
    # Create the project
    response = projects_api.create_project_project_create_post(
        create_project_request=create_request,
        # x_api_key=API_KEY,
        # x_api_secret=API_SECRET
    )
    
    print(f"Project created successfully!")
    print(f"Project ID: {response.project.id}")
    print(f"Project Name: {response.project.name}")
    
except ApiException as e:
    print(f"Error creating project: {e}")