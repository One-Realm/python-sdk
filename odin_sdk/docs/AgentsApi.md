# odin_sdk.AgentsApi

All URIs are relative to *http://127.0.0.1:8001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_custom_agent_agents_activate_post**](AgentsApi.md#activate_custom_agent_agents_activate_post) | **POST** /agents/activate | Activate an Existing Custom Agent
[**activate_custom_agent_on_chat_chat_agents_activate_post**](AgentsApi.md#activate_custom_agent_on_chat_chat_agents_activate_post) | **POST** /chat/agents/activate | Activate an Existing Custom Agent
[**clone_existing_custom_agent_agents_clone_post**](AgentsApi.md#clone_existing_custom_agent_agents_clone_post) | **POST** /agents/clone | Clone an Existing Custom Agent
[**deactivate_custom_agent_agents_deactivate_post**](AgentsApi.md#deactivate_custom_agent_agents_deactivate_post) | **POST** /agents/deactivate | Deactivate an Active Custom Agent
[**delete_custom_agent_agents_delete_delete**](AgentsApi.md#delete_custom_agent_agents_delete_delete) | **DELETE** /agents/delete | Delete an Existing Custom Agent
[**delete_model_agents_project_id_model_model_id_delete**](AgentsApi.md#delete_model_agents_project_id_model_model_id_delete) | **DELETE** /agents/{project_id}/model/{model_id} | Delete Model
[**edit_existing_custom_agent_agents_edit_post**](AgentsApi.md#edit_existing_custom_agent_agents_edit_post) | **POST** /agents/edit | Edit an Existing Custom Agent
[**get_all_models_agents_project_id_model_get**](AgentsApi.md#get_all_models_agents_project_id_model_get) | **GET** /agents/{project_id}/model | Get All Models
[**get_custom_agent_agents_project_id_agent_id_get_get**](AgentsApi.md#get_custom_agent_agents_project_id_agent_id_get_get) | **GET** /agents/{project_id}/{agent_id}/get | Get a Custom Agent
[**get_model_agents_project_id_model_model_id_get**](AgentsApi.md#get_model_agents_project_id_model_model_id_get) | **GET** /agents/{project_id}/model/{model_id} | Get Model
[**insert_model_agents_project_id_model_add_post**](AgentsApi.md#insert_model_agents_project_id_model_add_post) | **POST** /agents/{project_id}/model/add | Insert Model
[**list_agents_for_project_agents_project_id_list_get**](AgentsApi.md#list_agents_for_project_agents_project_id_list_get) | **GET** /agents/{project_id}/list | List Agents for Project
[**list_default_agents_agents_list_default_get**](AgentsApi.md#list_default_agents_agents_list_default_get) | **GET** /agents/list_default | List Default Agents
[**save_new_custom_agent_agents_new_post**](AgentsApi.md#save_new_custom_agent_agents_new_post) | **POST** /agents/new | Save a New Custom Agent
[**update_model_agents_project_id_model_model_id_post**](AgentsApi.md#update_model_agents_project_id_model_model_id_post) | **POST** /agents/{project_id}/model/{model_id} | Update Model


# **activate_custom_agent_agents_activate_post**
> ActivateCustomAgentResponse activate_custom_agent_agents_activate_post(routes_projects_activate_custom_agent_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Activate an Existing Custom Agent

Activate an existing custom agent in a project.

### Example


```python
import odin_sdk
from odin_sdk.models.activate_custom_agent_response import ActivateCustomAgentResponse
from odin_sdk.models.routes_projects_activate_custom_agent_request import RoutesProjectsActivateCustomAgentRequest
from odin_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = odin_sdk.Configuration(
    host = "http://127.0.0.1:8001"
)


# Enter a context with an instance of the API client
with odin_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = odin_sdk.AgentsApi(api_client)
    routes_projects_activate_custom_agent_request = odin_sdk.RoutesProjectsActivateCustomAgentRequest() # RoutesProjectsActivateCustomAgentRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Activate an Existing Custom Agent
        api_response = api_instance.activate_custom_agent_agents_activate_post(routes_projects_activate_custom_agent_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of AgentsApi->activate_custom_agent_agents_activate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->activate_custom_agent_agents_activate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **routes_projects_activate_custom_agent_request** | [**RoutesProjectsActivateCustomAgentRequest**](RoutesProjectsActivateCustomAgentRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**ActivateCustomAgentResponse**](ActivateCustomAgentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **activate_custom_agent_on_chat_chat_agents_activate_post**
> ActivateCustomAgentResponse activate_custom_agent_on_chat_chat_agents_activate_post(routes_chat_activate_custom_agent_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Activate an Existing Custom Agent

Activate an existing custom agent in a project.

### Example


```python
import odin_sdk
from odin_sdk.models.activate_custom_agent_response import ActivateCustomAgentResponse
from odin_sdk.models.routes_chat_activate_custom_agent_request import RoutesChatActivateCustomAgentRequest
from odin_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = odin_sdk.Configuration(
    host = "http://127.0.0.1:8001"
)


# Enter a context with an instance of the API client
with odin_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = odin_sdk.AgentsApi(api_client)
    routes_chat_activate_custom_agent_request = odin_sdk.RoutesChatActivateCustomAgentRequest() # RoutesChatActivateCustomAgentRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Activate an Existing Custom Agent
        api_response = api_instance.activate_custom_agent_on_chat_chat_agents_activate_post(routes_chat_activate_custom_agent_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of AgentsApi->activate_custom_agent_on_chat_chat_agents_activate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->activate_custom_agent_on_chat_chat_agents_activate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **routes_chat_activate_custom_agent_request** | [**RoutesChatActivateCustomAgentRequest**](RoutesChatActivateCustomAgentRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**ActivateCustomAgentResponse**](ActivateCustomAgentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clone_existing_custom_agent_agents_clone_post**
> CloneExistingCustomAgentResponse clone_existing_custom_agent_agents_clone_post(clone_existing_custom_agent_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Clone an Existing Custom Agent

Clone an existing custom agent in a project.

### Example


```python
import odin_sdk
from odin_sdk.models.clone_existing_custom_agent_request import CloneExistingCustomAgentRequest
from odin_sdk.models.clone_existing_custom_agent_response import CloneExistingCustomAgentResponse
from odin_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = odin_sdk.Configuration(
    host = "http://127.0.0.1:8001"
)


# Enter a context with an instance of the API client
with odin_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = odin_sdk.AgentsApi(api_client)
    clone_existing_custom_agent_request = odin_sdk.CloneExistingCustomAgentRequest() # CloneExistingCustomAgentRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Clone an Existing Custom Agent
        api_response = api_instance.clone_existing_custom_agent_agents_clone_post(clone_existing_custom_agent_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of AgentsApi->clone_existing_custom_agent_agents_clone_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->clone_existing_custom_agent_agents_clone_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clone_existing_custom_agent_request** | [**CloneExistingCustomAgentRequest**](CloneExistingCustomAgentRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**CloneExistingCustomAgentResponse**](CloneExistingCustomAgentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivate_custom_agent_agents_deactivate_post**
> DeactivateCustomAgentResponse deactivate_custom_agent_agents_deactivate_post(deactivate_custom_agent_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Deactivate an Active Custom Agent

Deactivate an active custom agent in a project.

### Example


```python
import odin_sdk
from odin_sdk.models.deactivate_custom_agent_request import DeactivateCustomAgentRequest
from odin_sdk.models.deactivate_custom_agent_response import DeactivateCustomAgentResponse
from odin_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = odin_sdk.Configuration(
    host = "http://127.0.0.1:8001"
)


# Enter a context with an instance of the API client
with odin_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = odin_sdk.AgentsApi(api_client)
    deactivate_custom_agent_request = odin_sdk.DeactivateCustomAgentRequest() # DeactivateCustomAgentRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Deactivate an Active Custom Agent
        api_response = api_instance.deactivate_custom_agent_agents_deactivate_post(deactivate_custom_agent_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of AgentsApi->deactivate_custom_agent_agents_deactivate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->deactivate_custom_agent_agents_deactivate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deactivate_custom_agent_request** | [**DeactivateCustomAgentRequest**](DeactivateCustomAgentRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**DeactivateCustomAgentResponse**](DeactivateCustomAgentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_custom_agent_agents_delete_delete**
> DeleteCustomAgentResponse delete_custom_agent_agents_delete_delete(delete_custom_agent_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Delete an Existing Custom Agent

Delete an existing custom agent in a project.

### Example


```python
import odin_sdk
from odin_sdk.models.delete_custom_agent_request import DeleteCustomAgentRequest
from odin_sdk.models.delete_custom_agent_response import DeleteCustomAgentResponse
from odin_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = odin_sdk.Configuration(
    host = "http://127.0.0.1:8001"
)


# Enter a context with an instance of the API client
with odin_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = odin_sdk.AgentsApi(api_client)
    delete_custom_agent_request = odin_sdk.DeleteCustomAgentRequest() # DeleteCustomAgentRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Delete an Existing Custom Agent
        api_response = api_instance.delete_custom_agent_agents_delete_delete(delete_custom_agent_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of AgentsApi->delete_custom_agent_agents_delete_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->delete_custom_agent_agents_delete_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_custom_agent_request** | [**DeleteCustomAgentRequest**](DeleteCustomAgentRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**DeleteCustomAgentResponse**](DeleteCustomAgentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_model_agents_project_id_model_model_id_delete**
> GetModelResponse delete_model_agents_project_id_model_model_id_delete(project_id, model_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Delete Model

Delete a model

### Example


```python
import odin_sdk
from odin_sdk.models.get_model_response import GetModelResponse
from odin_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = odin_sdk.Configuration(
    host = "http://127.0.0.1:8001"
)


# Enter a context with an instance of the API client
with odin_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = odin_sdk.AgentsApi(api_client)
    project_id = 'project_id_example' # str | 
    model_id = 'model_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Delete Model
        api_response = api_instance.delete_model_agents_project_id_model_model_id_delete(project_id, model_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of AgentsApi->delete_model_agents_project_id_model_model_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->delete_model_agents_project_id_model_model_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **model_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**GetModelResponse**](GetModelResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_existing_custom_agent_agents_edit_post**
> EditExistingCustomAgentResponse edit_existing_custom_agent_agents_edit_post(edit_existing_custom_agent, x_api_key=x_api_key, x_api_secret=x_api_secret)

Edit an Existing Custom Agent

Edit an existing custom agent in a project.
<br><br>
The most complex component of the API is the <b>building_blocks</b> field. It is an array of json objects, each of which represents a building block that can be attached to the agent.<br>
Each block is identified by the "name" field in its json structure. It is <b>vital</b> that the names are provided correctly, or the blocks will not be reconstituted properly.<br>
The types of the building blocks available, and their json structure, is as follows:

<ul>
<li>
<b>Enhanced Search</b><ul>
<li>name: enhanced_search</li>
<li>Improved version of basic chat with KB, using multiple calls to the LLM and vector search to refine and source the answer.</li>
<li>Resource-intensive. Does not support basic GPT-3.5 model.</li>
<li>json format: <code>{"name": "enhanced_search", "answered_rules": ["Say 'thank you'."], "group_on_backend": false}</code></li>
<li>JSON keys: <ul>
    <li><b>name</b> - identifier for the block, must be "enhanced_search"</li>
    <li><b>answered_rules</b> - array of strings defining rules for how the agent should answer the user when the user indicates that their initial query has been satisfactorily resolved.</li>
    <li><b>group_on_backend</b> - whether to group search results by source before they go into the language model. Enabling this will increase the diversity of sources available to the model.</li>
</ul></li>
</ul>
</li>
</ul>

### Example


```python
import odin_sdk
from odin_sdk.models.edit_existing_custom_agent import EditExistingCustomAgent
from odin_sdk.models.edit_existing_custom_agent_response import EditExistingCustomAgentResponse
from odin_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = odin_sdk.Configuration(
    host = "http://127.0.0.1:8001"
)


# Enter a context with an instance of the API client
with odin_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = odin_sdk.AgentsApi(api_client)
    edit_existing_custom_agent = odin_sdk.EditExistingCustomAgent() # EditExistingCustomAgent | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Edit an Existing Custom Agent
        api_response = api_instance.edit_existing_custom_agent_agents_edit_post(edit_existing_custom_agent, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of AgentsApi->edit_existing_custom_agent_agents_edit_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->edit_existing_custom_agent_agents_edit_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edit_existing_custom_agent** | [**EditExistingCustomAgent**](EditExistingCustomAgent.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**EditExistingCustomAgentResponse**](EditExistingCustomAgentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_models_agents_project_id_model_get**
> GetAllModelsResponse get_all_models_agents_project_id_model_get(project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get All Models

Get all models

### Example


```python
import odin_sdk
from odin_sdk.models.get_all_models_response import GetAllModelsResponse
from odin_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = odin_sdk.Configuration(
    host = "http://127.0.0.1:8001"
)


# Enter a context with an instance of the API client
with odin_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = odin_sdk.AgentsApi(api_client)
    project_id = 'project_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get All Models
        api_response = api_instance.get_all_models_agents_project_id_model_get(project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of AgentsApi->get_all_models_agents_project_id_model_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->get_all_models_agents_project_id_model_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**GetAllModelsResponse**](GetAllModelsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_agent_agents_project_id_agent_id_get_get**
> GetCustomAgentResponse get_custom_agent_agents_project_id_agent_id_get_get(project_id, agent_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get a Custom Agent

Get a custom agent in a project.

### Example


```python
import odin_sdk
from odin_sdk.models.get_custom_agent_response import GetCustomAgentResponse
from odin_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = odin_sdk.Configuration(
    host = "http://127.0.0.1:8001"
)


# Enter a context with an instance of the API client
with odin_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = odin_sdk.AgentsApi(api_client)
    project_id = None # object | ID of the project from which to get the agent.
    agent_id = None # object | ID of the agent to get.
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get a Custom Agent
        api_response = api_instance.get_custom_agent_agents_project_id_agent_id_get_get(project_id, agent_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of AgentsApi->get_custom_agent_agents_project_id_agent_id_get_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->get_custom_agent_agents_project_id_agent_id_get_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)| ID of the project from which to get the agent. | 
 **agent_id** | [**object**](.md)| ID of the agent to get. | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**GetCustomAgentResponse**](GetCustomAgentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_model_agents_project_id_model_model_id_get**
> GetModelResponse get_model_agents_project_id_model_model_id_get(project_id, model_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Model

Get a model with api link and api key

### Example


```python
import odin_sdk
from odin_sdk.models.get_model_response import GetModelResponse
from odin_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = odin_sdk.Configuration(
    host = "http://127.0.0.1:8001"
)


# Enter a context with an instance of the API client
with odin_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = odin_sdk.AgentsApi(api_client)
    project_id = 'project_id_example' # str | 
    model_id = 'model_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Model
        api_response = api_instance.get_model_agents_project_id_model_model_id_get(project_id, model_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of AgentsApi->get_model_agents_project_id_model_model_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->get_model_agents_project_id_model_model_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **model_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**GetModelResponse**](GetModelResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_model_agents_project_id_model_add_post**
> RoutesProjectsInsertModelResponse insert_model_agents_project_id_model_add_post(project_id, insert_model_key, x_api_key=x_api_key, x_api_secret=x_api_secret)

Insert Model

Add an ai model

### Example


```python
import odin_sdk
from odin_sdk.models.insert_model_key import InsertModelKey
from odin_sdk.models.routes_projects_insert_model_response import RoutesProjectsInsertModelResponse
from odin_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = odin_sdk.Configuration(
    host = "http://127.0.0.1:8001"
)


# Enter a context with an instance of the API client
with odin_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = odin_sdk.AgentsApi(api_client)
    project_id = 'project_id_example' # str | 
    insert_model_key = odin_sdk.InsertModelKey() # InsertModelKey | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Insert Model
        api_response = api_instance.insert_model_agents_project_id_model_add_post(project_id, insert_model_key, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of AgentsApi->insert_model_agents_project_id_model_add_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->insert_model_agents_project_id_model_add_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **insert_model_key** | [**InsertModelKey**](InsertModelKey.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**RoutesProjectsInsertModelResponse**](RoutesProjectsInsertModelResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_agents_for_project_agents_project_id_list_get**
> ListAgentsForProjectResponse list_agents_for_project_agents_project_id_list_get(project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

List Agents for Project

List all agents in a project, including default agents.

### Example


```python
import odin_sdk
from odin_sdk.models.list_agents_for_project_response import ListAgentsForProjectResponse
from odin_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = odin_sdk.Configuration(
    host = "http://127.0.0.1:8001"
)


# Enter a context with an instance of the API client
with odin_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = odin_sdk.AgentsApi(api_client)
    project_id = 'project_id_example' # str | ID of the project.
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # List Agents for Project
        api_response = api_instance.list_agents_for_project_agents_project_id_list_get(project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of AgentsApi->list_agents_for_project_agents_project_id_list_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->list_agents_for_project_agents_project_id_list_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| ID of the project. | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**ListAgentsForProjectResponse**](ListAgentsForProjectResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_default_agents_agents_list_default_get**
> ListAgentsForProjectResponse list_default_agents_agents_list_default_get(x_api_key=x_api_key, x_api_secret=x_api_secret)

List Default Agents

List all default agents.

### Example


```python
import odin_sdk
from odin_sdk.models.list_agents_for_project_response import ListAgentsForProjectResponse
from odin_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = odin_sdk.Configuration(
    host = "http://127.0.0.1:8001"
)


# Enter a context with an instance of the API client
with odin_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = odin_sdk.AgentsApi(api_client)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # List Default Agents
        api_response = api_instance.list_default_agents_agents_list_default_get(x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of AgentsApi->list_default_agents_agents_list_default_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->list_default_agents_agents_list_default_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**ListAgentsForProjectResponse**](ListAgentsForProjectResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_new_custom_agent_agents_new_post**
> SaveNewCustomAgentResponse save_new_custom_agent_agents_new_post(save_new_custom_agent, x_api_key=x_api_key, x_api_secret=x_api_secret)

Save a New Custom Agent

Save a new custom agent in a project.
<br><br>
The most complex component of the API is the <b>building_blocks</b> field. It is an array of json objects, each of which represents a building block that can be attached to the agent.<br>
Each block is identified by the "name" field in its json structure. It is <b>vital</b> that the names are provided correctly, or the blocks will not be reconstituted properly.<br>
The types of the building blocks available, and their json structure, is as follows:

<ul>
<li>
<b>Enhanced Search</b><ul>
<li>name: enhanced_search</li>
<li>Improved version of basic chat with KB, using multiple calls to the LLM and vector search to refine and source the answer.</li>
<li>Resource-intensive. Does not support basic GPT-3.5 model.</li>
<li>json format: <code>{"name": "enhanced_search", "answered_rules": ["Say 'thank you'."], "group_on_backend": false}</code></li>
<li>JSON keys: <ul>
    <li><b>name</b> - identifier for the block, must be "enhanced_search"</li>
    <li><b>answered_rules</b> - array of strings defining rules for how the agent should answer the user when the user indicates that their initial query has been satisfactorily resolved.</li>
    <li><b>group_on_backend</b> - whether to group search results by source before they go into the language model. Enabling this will increase the diversity of sources available to the model.</li>
</ul></li>
</ul>
</li>
</ul>

### Example


```python
import odin_sdk
from odin_sdk.models.save_new_custom_agent import SaveNewCustomAgent
from odin_sdk.models.save_new_custom_agent_response import SaveNewCustomAgentResponse
from odin_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = odin_sdk.Configuration(
    host = "http://127.0.0.1:8001"
)


# Enter a context with an instance of the API client
with odin_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = odin_sdk.AgentsApi(api_client)
    save_new_custom_agent = odin_sdk.SaveNewCustomAgent() # SaveNewCustomAgent | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Save a New Custom Agent
        api_response = api_instance.save_new_custom_agent_agents_new_post(save_new_custom_agent, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of AgentsApi->save_new_custom_agent_agents_new_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->save_new_custom_agent_agents_new_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **save_new_custom_agent** | [**SaveNewCustomAgent**](SaveNewCustomAgent.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**SaveNewCustomAgentResponse**](SaveNewCustomAgentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_model_agents_project_id_model_model_id_post**
> RoutesProjectsInsertModelResponse update_model_agents_project_id_model_model_id_post(project_id, model_id, insert_model_key, x_api_key=x_api_key, x_api_secret=x_api_secret)

Update Model

Update a model

### Example


```python
import odin_sdk
from odin_sdk.models.insert_model_key import InsertModelKey
from odin_sdk.models.routes_projects_insert_model_response import RoutesProjectsInsertModelResponse
from odin_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = odin_sdk.Configuration(
    host = "http://127.0.0.1:8001"
)


# Enter a context with an instance of the API client
with odin_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = odin_sdk.AgentsApi(api_client)
    project_id = 'project_id_example' # str | 
    model_id = 'model_id_example' # str | 
    insert_model_key = odin_sdk.InsertModelKey() # InsertModelKey | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Update Model
        api_response = api_instance.update_model_agents_project_id_model_model_id_post(project_id, model_id, insert_model_key, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of AgentsApi->update_model_agents_project_id_model_model_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->update_model_agents_project_id_model_model_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **model_id** | **str**|  | 
 **insert_model_key** | [**InsertModelKey**](InsertModelKey.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**RoutesProjectsInsertModelResponse**](RoutesProjectsInsertModelResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

