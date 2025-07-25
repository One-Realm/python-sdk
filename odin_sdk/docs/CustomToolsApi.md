# odin_sdk.CustomToolsApi

All URIs are relative to *http://127.0.0.1:8001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clone_public_tool_tools_custom_clone_post**](CustomToolsApi.md#clone_public_tool_tools_custom_clone_post) | **POST** /tools/custom/clone | Clone Public Tool
[**create_custom_tool_tools_custom_post**](CustomToolsApi.md#create_custom_tool_tools_custom_post) | **POST** /tools/custom | Create Custom Tool
[**delete_custom_tool_tools_custom_tool_id_delete**](CustomToolsApi.md#delete_custom_tool_tools_custom_tool_id_delete) | **DELETE** /tools/custom/{tool_id} | Delete Custom Tool
[**export_custom_tool_tools_custom_tool_id_export_post**](CustomToolsApi.md#export_custom_tool_tools_custom_tool_id_export_post) | **POST** /tools/custom/{tool_id}/export | Export Custom Tool
[**get_custom_tool_tools_custom_tool_id_get**](CustomToolsApi.md#get_custom_tool_tools_custom_tool_id_get) | **GET** /tools/custom/{tool_id} | Get Custom Tool
[**get_custom_tools_tools_custom_get**](CustomToolsApi.md#get_custom_tools_tools_custom_get) | **GET** /tools/custom | Get Custom Tools
[**get_public_custom_tools_tools_custom_public_get**](CustomToolsApi.md#get_public_custom_tools_tools_custom_public_get) | **GET** /tools/custom/public | Get Public Custom Tools
[**get_tool_versions_tools_custom_tool_id_versions_get**](CustomToolsApi.md#get_tool_versions_tools_custom_tool_id_versions_get) | **GET** /tools/custom/{tool_id}/versions | Get Tool Versions
[**import_custom_tool_tools_custom_import_post**](CustomToolsApi.md#import_custom_tool_tools_custom_import_post) | **POST** /tools/custom/import | Import Custom Tool
[**publish_custom_tool_tools_custom_tool_id_publish_post**](CustomToolsApi.md#publish_custom_tool_tools_custom_tool_id_publish_post) | **POST** /tools/custom/{tool_id}/publish | Publish Custom Tool
[**revert_draft_to_version_tools_custom_tool_id_revert_to_version_post**](CustomToolsApi.md#revert_draft_to_version_tools_custom_tool_id_revert_to_version_post) | **POST** /tools/custom/{tool_id}/revert-to-version | Revert Draft To Version
[**update_custom_tool_tools_custom_tool_id_put**](CustomToolsApi.md#update_custom_tool_tools_custom_tool_id_put) | **PUT** /tools/custom/{tool_id} | Update Custom Tool


# **clone_public_tool_tools_custom_clone_post**
> CustomToolResponse clone_public_tool_tools_custom_clone_post(clone_public_tool_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Clone Public Tool

Clone a public tool to a project and automatically publish it

### Example


```python
import odin_sdk
from odin_sdk.models.clone_public_tool_request import ClonePublicToolRequest
from odin_sdk.models.custom_tool_response import CustomToolResponse
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
    api_instance = odin_sdk.CustomToolsApi(api_client)
    clone_public_tool_request = odin_sdk.ClonePublicToolRequest() # ClonePublicToolRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Clone Public Tool
        api_response = api_instance.clone_public_tool_tools_custom_clone_post(clone_public_tool_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of CustomToolsApi->clone_public_tool_tools_custom_clone_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomToolsApi->clone_public_tool_tools_custom_clone_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clone_public_tool_request** | [**ClonePublicToolRequest**](ClonePublicToolRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**CustomToolResponse**](CustomToolResponse.md)

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

# **create_custom_tool_tools_custom_post**
> CustomToolResponse create_custom_tool_tools_custom_post(create_custom_tool_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Create Custom Tool

Create a new custom tool

### Example


```python
import odin_sdk
from odin_sdk.models.create_custom_tool_request import CreateCustomToolRequest
from odin_sdk.models.custom_tool_response import CustomToolResponse
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
    api_instance = odin_sdk.CustomToolsApi(api_client)
    create_custom_tool_request = odin_sdk.CreateCustomToolRequest() # CreateCustomToolRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Create Custom Tool
        api_response = api_instance.create_custom_tool_tools_custom_post(create_custom_tool_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of CustomToolsApi->create_custom_tool_tools_custom_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomToolsApi->create_custom_tool_tools_custom_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_custom_tool_request** | [**CreateCustomToolRequest**](CreateCustomToolRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**CustomToolResponse**](CustomToolResponse.md)

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

# **delete_custom_tool_tools_custom_tool_id_delete**
> object delete_custom_tool_tools_custom_tool_id_delete(tool_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Delete Custom Tool

Delete a custom tool

### Example


```python
import odin_sdk
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
    api_instance = odin_sdk.CustomToolsApi(api_client)
    tool_id = 'tool_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Delete Custom Tool
        api_response = api_instance.delete_custom_tool_tools_custom_tool_id_delete(tool_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of CustomToolsApi->delete_custom_tool_tools_custom_tool_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomToolsApi->delete_custom_tool_tools_custom_tool_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tool_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

**object**

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

# **export_custom_tool_tools_custom_tool_id_export_post**
> ExportToolResponse export_custom_tool_tools_custom_tool_id_export_post(tool_id, export_tool_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Export Custom Tool

Export a custom tool as JSON

### Example


```python
import odin_sdk
from odin_sdk.models.export_tool_request import ExportToolRequest
from odin_sdk.models.export_tool_response import ExportToolResponse
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
    api_instance = odin_sdk.CustomToolsApi(api_client)
    tool_id = 'tool_id_example' # str | 
    export_tool_request = odin_sdk.ExportToolRequest() # ExportToolRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Export Custom Tool
        api_response = api_instance.export_custom_tool_tools_custom_tool_id_export_post(tool_id, export_tool_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of CustomToolsApi->export_custom_tool_tools_custom_tool_id_export_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomToolsApi->export_custom_tool_tools_custom_tool_id_export_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tool_id** | **str**|  | 
 **export_tool_request** | [**ExportToolRequest**](ExportToolRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**ExportToolResponse**](ExportToolResponse.md)

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

# **get_custom_tool_tools_custom_tool_id_get**
> CustomToolResponse get_custom_tool_tools_custom_tool_id_get(tool_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Custom Tool

Get a specific custom tool by ID

### Example


```python
import odin_sdk
from odin_sdk.models.custom_tool_response import CustomToolResponse
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
    api_instance = odin_sdk.CustomToolsApi(api_client)
    tool_id = 'tool_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Custom Tool
        api_response = api_instance.get_custom_tool_tools_custom_tool_id_get(tool_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of CustomToolsApi->get_custom_tool_tools_custom_tool_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomToolsApi->get_custom_tool_tools_custom_tool_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tool_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**CustomToolResponse**](CustomToolResponse.md)

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

# **get_custom_tools_tools_custom_get**
> CustomToolListResponse get_custom_tools_tools_custom_get(project_id, limit=limit, offset=offset, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Custom Tools

Get all custom tools for a project

### Example


```python
import odin_sdk
from odin_sdk.models.custom_tool_list_response import CustomToolListResponse
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
    api_instance = odin_sdk.CustomToolsApi(api_client)
    project_id = 'project_id_example' # str | 
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Custom Tools
        api_response = api_instance.get_custom_tools_tools_custom_get(project_id, limit=limit, offset=offset, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of CustomToolsApi->get_custom_tools_tools_custom_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomToolsApi->get_custom_tools_tools_custom_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**CustomToolListResponse**](CustomToolListResponse.md)

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

# **get_public_custom_tools_tools_custom_public_get**
> CustomToolListResponse get_public_custom_tools_tools_custom_public_get(limit=limit, offset=offset, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Public Custom Tools

Get all public custom tools from any user

### Example


```python
import odin_sdk
from odin_sdk.models.custom_tool_list_response import CustomToolListResponse
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
    api_instance = odin_sdk.CustomToolsApi(api_client)
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Public Custom Tools
        api_response = api_instance.get_public_custom_tools_tools_custom_public_get(limit=limit, offset=offset, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of CustomToolsApi->get_public_custom_tools_tools_custom_public_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomToolsApi->get_public_custom_tools_tools_custom_public_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**CustomToolListResponse**](CustomToolListResponse.md)

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

# **get_tool_versions_tools_custom_tool_id_versions_get**
> CustomToolVersionListResponse get_tool_versions_tools_custom_tool_id_versions_get(tool_id, limit=limit, offset=offset, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Tool Versions

Get version history for a tool

### Example


```python
import odin_sdk
from odin_sdk.models.custom_tool_version_list_response import CustomToolVersionListResponse
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
    api_instance = odin_sdk.CustomToolsApi(api_client)
    tool_id = 'tool_id_example' # str | 
    limit = 20 # int |  (optional) (default to 20)
    offset = 0 # int |  (optional) (default to 0)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Tool Versions
        api_response = api_instance.get_tool_versions_tools_custom_tool_id_versions_get(tool_id, limit=limit, offset=offset, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of CustomToolsApi->get_tool_versions_tools_custom_tool_id_versions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomToolsApi->get_tool_versions_tools_custom_tool_id_versions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tool_id** | **str**|  | 
 **limit** | **int**|  | [optional] [default to 20]
 **offset** | **int**|  | [optional] [default to 0]
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**CustomToolVersionListResponse**](CustomToolVersionListResponse.md)

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

# **import_custom_tool_tools_custom_import_post**
> CustomToolResponse import_custom_tool_tools_custom_import_post(import_tool_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Import Custom Tool

Import a custom tool from JSON

### Example


```python
import odin_sdk
from odin_sdk.models.custom_tool_response import CustomToolResponse
from odin_sdk.models.import_tool_request import ImportToolRequest
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
    api_instance = odin_sdk.CustomToolsApi(api_client)
    import_tool_request = odin_sdk.ImportToolRequest() # ImportToolRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Import Custom Tool
        api_response = api_instance.import_custom_tool_tools_custom_import_post(import_tool_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of CustomToolsApi->import_custom_tool_tools_custom_import_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomToolsApi->import_custom_tool_tools_custom_import_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_tool_request** | [**ImportToolRequest**](ImportToolRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**CustomToolResponse**](CustomToolResponse.md)

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

# **publish_custom_tool_tools_custom_tool_id_publish_post**
> CustomToolResponse publish_custom_tool_tools_custom_tool_id_publish_post(tool_id, publish_tool_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Publish Custom Tool

Publish a draft tool version

### Example


```python
import odin_sdk
from odin_sdk.models.custom_tool_response import CustomToolResponse
from odin_sdk.models.publish_tool_request import PublishToolRequest
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
    api_instance = odin_sdk.CustomToolsApi(api_client)
    tool_id = 'tool_id_example' # str | 
    publish_tool_request = odin_sdk.PublishToolRequest() # PublishToolRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Publish Custom Tool
        api_response = api_instance.publish_custom_tool_tools_custom_tool_id_publish_post(tool_id, publish_tool_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of CustomToolsApi->publish_custom_tool_tools_custom_tool_id_publish_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomToolsApi->publish_custom_tool_tools_custom_tool_id_publish_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tool_id** | **str**|  | 
 **publish_tool_request** | [**PublishToolRequest**](PublishToolRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**CustomToolResponse**](CustomToolResponse.md)

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

# **revert_draft_to_version_tools_custom_tool_id_revert_to_version_post**
> CustomToolResponse revert_draft_to_version_tools_custom_tool_id_revert_to_version_post(tool_id, version, x_api_key=x_api_key, x_api_secret=x_api_secret)

Revert Draft To Version

Revert a draft to a specific published version

### Example


```python
import odin_sdk
from odin_sdk.models.custom_tool_response import CustomToolResponse
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
    api_instance = odin_sdk.CustomToolsApi(api_client)
    tool_id = 'tool_id_example' # str | 
    version = 'version_example' # str | The version to revert to
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Revert Draft To Version
        api_response = api_instance.revert_draft_to_version_tools_custom_tool_id_revert_to_version_post(tool_id, version, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of CustomToolsApi->revert_draft_to_version_tools_custom_tool_id_revert_to_version_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomToolsApi->revert_draft_to_version_tools_custom_tool_id_revert_to_version_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tool_id** | **str**|  | 
 **version** | **str**| The version to revert to | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**CustomToolResponse**](CustomToolResponse.md)

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

# **update_custom_tool_tools_custom_tool_id_put**
> CustomToolResponse update_custom_tool_tools_custom_tool_id_put(tool_id, update_custom_tool_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Update Custom Tool

Update a custom tool

### Example


```python
import odin_sdk
from odin_sdk.models.custom_tool_response import CustomToolResponse
from odin_sdk.models.update_custom_tool_request import UpdateCustomToolRequest
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
    api_instance = odin_sdk.CustomToolsApi(api_client)
    tool_id = 'tool_id_example' # str | 
    update_custom_tool_request = odin_sdk.UpdateCustomToolRequest() # UpdateCustomToolRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Update Custom Tool
        api_response = api_instance.update_custom_tool_tools_custom_tool_id_put(tool_id, update_custom_tool_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of CustomToolsApi->update_custom_tool_tools_custom_tool_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomToolsApi->update_custom_tool_tools_custom_tool_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tool_id** | **str**|  | 
 **update_custom_tool_request** | [**UpdateCustomToolRequest**](UpdateCustomToolRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**CustomToolResponse**](CustomToolResponse.md)

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

