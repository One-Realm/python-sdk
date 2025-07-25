import os

import odin_sdk
from odin_sdk.rest import ApiException

HOST = "http://localhost:8001"

API_KEY = os.getenv("ODIN_LOCAL_KEY")
API_SECRET = os.getenv("ODIN_LOCAL_SECRET")


# Initialize the API client
configuration = odin_sdk.Configuration(host=HOST)
api_client = odin_sdk.ApiClient(configuration)

api_client.default_headers["x-api-key"] = API_KEY
api_client.default_headers["x-api-secret"] = API_SECRET

chat_api = odin_sdk.ChatApi(api_client)

try:
    # Get available models
    response = chat_api.get_default_models_chat_models_get()
    
    print("Available Models:")
    for model in response.available_models:
        print(model.to_json())
        
except ApiException as e:
    print(f"Error fetching models: {e}")