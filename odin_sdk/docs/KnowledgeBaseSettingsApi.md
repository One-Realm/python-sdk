# odin_sdk.KnowledgeBaseSettingsApi

All URIs are relative to *http://127.0.0.1:8001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apply_settings_knowledgebase_settings_apply_project_id_post**](KnowledgeBaseSettingsApi.md#apply_settings_knowledgebase_settings_apply_project_id_post) | **POST** /knowledgebase-settings/apply/{project_id} | Apply Settings
[**create_settings_knowledgebase_settings_post**](KnowledgeBaseSettingsApi.md#create_settings_knowledgebase_settings_post) | **POST** /knowledgebase-settings | Create Settings
[**get_settings_knowledgebase_settings_project_id_get**](KnowledgeBaseSettingsApi.md#get_settings_knowledgebase_settings_project_id_get) | **GET** /knowledgebase-settings/{project_id} | Get Settings
[**update_settings_knowledgebase_settings_project_id_put**](KnowledgeBaseSettingsApi.md#update_settings_knowledgebase_settings_project_id_put) | **PUT** /knowledgebase-settings/{project_id} | Update Settings


# **apply_settings_knowledgebase_settings_apply_project_id_post**
> ApplySettingsResponse apply_settings_knowledgebase_settings_apply_project_id_post(project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Apply Settings

Apply knowledgebase settings to all documents in the project.

### Example


```python
import odin_sdk
from odin_sdk.models.apply_settings_response import ApplySettingsResponse
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
    api_instance = odin_sdk.KnowledgeBaseSettingsApi(api_client)
    project_id = 'project_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Apply Settings
        api_response = api_instance.apply_settings_knowledgebase_settings_apply_project_id_post(project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of KnowledgeBaseSettingsApi->apply_settings_knowledgebase_settings_apply_project_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBaseSettingsApi->apply_settings_knowledgebase_settings_apply_project_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**ApplySettingsResponse**](ApplySettingsResponse.md)

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

# **create_settings_knowledgebase_settings_post**
> KnowledgeBaseSettingsResponse create_settings_knowledgebase_settings_post(knowledge_base_settings, x_api_key=x_api_key, x_api_secret=x_api_secret)

Create Settings

Create or update knowledge base settings for a project.

Args:
    settings (KnowledgeBaseSettings): The settings to create or update
    user (User): The authenticated user

Returns:
    KnowledgeBaseSettingsResponse: The created or updated settings

### Example


```python
import odin_sdk
from odin_sdk.models.knowledge_base_settings import KnowledgeBaseSettings
from odin_sdk.models.knowledge_base_settings_response import KnowledgeBaseSettingsResponse
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
    api_instance = odin_sdk.KnowledgeBaseSettingsApi(api_client)
    knowledge_base_settings = odin_sdk.KnowledgeBaseSettings() # KnowledgeBaseSettings | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Create Settings
        api_response = api_instance.create_settings_knowledgebase_settings_post(knowledge_base_settings, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of KnowledgeBaseSettingsApi->create_settings_knowledgebase_settings_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBaseSettingsApi->create_settings_knowledgebase_settings_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **knowledge_base_settings** | [**KnowledgeBaseSettings**](KnowledgeBaseSettings.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**KnowledgeBaseSettingsResponse**](KnowledgeBaseSettingsResponse.md)

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

# **get_settings_knowledgebase_settings_project_id_get**
> KnowledgeBaseSettingsResponse get_settings_knowledgebase_settings_project_id_get(project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Settings

Get knowledge base settings for a project.

Args:
    project_id (str): The project ID
    user (User): The authenticated user

Returns:
    KnowledgeBaseSettingsResponse: The project settings

### Example


```python
import odin_sdk
from odin_sdk.models.knowledge_base_settings_response import KnowledgeBaseSettingsResponse
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
    api_instance = odin_sdk.KnowledgeBaseSettingsApi(api_client)
    project_id = 'project_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Settings
        api_response = api_instance.get_settings_knowledgebase_settings_project_id_get(project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of KnowledgeBaseSettingsApi->get_settings_knowledgebase_settings_project_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBaseSettingsApi->get_settings_knowledgebase_settings_project_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**KnowledgeBaseSettingsResponse**](KnowledgeBaseSettingsResponse.md)

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

# **update_settings_knowledgebase_settings_project_id_put**
> KnowledgeBaseSettingsResponse update_settings_knowledgebase_settings_project_id_put(project_id, knowledge_base_settings, x_api_key=x_api_key, x_api_secret=x_api_secret)

Update Settings

Update or create knowledge base settings for a project.

Args:
    project_id (str): The project ID
    settings (KnowledgeBaseSettings): The settings to update or create
    user (User): The authenticated user

Returns:
    KnowledgeBaseSettingsResponse: The updated or created settings

### Example


```python
import odin_sdk
from odin_sdk.models.knowledge_base_settings import KnowledgeBaseSettings
from odin_sdk.models.knowledge_base_settings_response import KnowledgeBaseSettingsResponse
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
    api_instance = odin_sdk.KnowledgeBaseSettingsApi(api_client)
    project_id = 'project_id_example' # str | 
    knowledge_base_settings = odin_sdk.KnowledgeBaseSettings() # KnowledgeBaseSettings | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Update Settings
        api_response = api_instance.update_settings_knowledgebase_settings_project_id_put(project_id, knowledge_base_settings, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of KnowledgeBaseSettingsApi->update_settings_knowledgebase_settings_project_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBaseSettingsApi->update_settings_knowledgebase_settings_project_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **knowledge_base_settings** | [**KnowledgeBaseSettings**](KnowledgeBaseSettings.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**KnowledgeBaseSettingsResponse**](KnowledgeBaseSettingsResponse.md)

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

