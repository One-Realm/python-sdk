# odin_sdk.AgentsApi

All URIs are relative to *http://127.0.0.1:8001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_custom_agent_agents_activate_post**](AgentsApi.md#activate_custom_agent_agents_activate_post) | **POST** /agents/activate | Activate an Existing Custom Agent
[**edit_existing_custom_agent_agents_edit_post**](AgentsApi.md#edit_existing_custom_agent_agents_edit_post) | **POST** /agents/edit | Edit an Existing Custom Agent
[**list_agents_for_project_agents_project_id_list_get**](AgentsApi.md#list_agents_for_project_agents_project_id_list_get) | **GET** /agents/{project_id}/list | List Agents for Project
[**save_new_custom_agent_agents_new_post**](AgentsApi.md#save_new_custom_agent_agents_new_post) | **POST** /agents/new | Save a New Custom Agent


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

