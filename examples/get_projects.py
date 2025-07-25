import os

import odin_sdk
from odin_sdk.rest import ApiException

HOST = "https://api.getodin.ai"

# Initialize the API client
configuration = odin_sdk.Configuration(host=HOST)
api_client = odin_sdk.ApiClient(configuration)
projects_api = odin_sdk.ProjectsApi(api_client)


API_KEY = os.getenv("ODIN_PROD_KEY")
API_SECRET = os.getenv("ODIN_PROD_SECRET")

api_client.default_headers["x-api-key"] = API_KEY
api_client.default_headers["x-api-secret"] = API_SECRET

# Get all projects
try:
    response = projects_api.get_projects_projects_get(
        limit=100,  # Optional: limit number of results
        # offset=10   # Optional: pagination offset
    )
    
    print(f"Found {len(response.projects)} projects:")
    for project in response.projects:
        print(f"- {project.name} (ID: {project.id})")
        
except ApiException as e:
    print(f"Error fetching projects: {e}")







