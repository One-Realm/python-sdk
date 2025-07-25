# odin_sdk.CodeScriptsApi

All URIs are relative to *http://127.0.0.1:8001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_script_code_scripts_post**](CodeScriptsApi.md#create_script_code_scripts_post) | **POST** /code-scripts | Create Script
[**delete_script_code_scripts_script_id_delete**](CodeScriptsApi.md#delete_script_code_scripts_script_id_delete) | **DELETE** /code-scripts/{script_id} | Delete Script
[**execute_script_code_scripts_script_id_execute_post**](CodeScriptsApi.md#execute_script_code_scripts_script_id_execute_post) | **POST** /code-scripts/{script_id}/execute | Execute Script
[**get_analytics_summary_code_scripts_analytics_summary_get**](CodeScriptsApi.md#get_analytics_summary_code_scripts_analytics_summary_get) | **GET** /code-scripts/analytics/summary | Get Analytics Summary
[**get_execution_detail_code_scripts_script_id_executions_execution_id_get**](CodeScriptsApi.md#get_execution_detail_code_scripts_script_id_executions_execution_id_get) | **GET** /code-scripts/{script_id}/executions/{execution_id} | Get Execution Detail
[**get_execution_history_code_scripts_script_id_executions_get**](CodeScriptsApi.md#get_execution_history_code_scripts_script_id_executions_get) | **GET** /code-scripts/{script_id}/executions | Get Execution History
[**get_script_analytics_code_scripts_script_id_analytics_get**](CodeScriptsApi.md#get_script_analytics_code_scripts_script_id_analytics_get) | **GET** /code-scripts/{script_id}/analytics | Get Script Analytics
[**get_script_code_scripts_script_id_get**](CodeScriptsApi.md#get_script_code_scripts_script_id_get) | **GET** /code-scripts/{script_id} | Get Script
[**get_script_versions_code_scripts_script_id_versions_get**](CodeScriptsApi.md#get_script_versions_code_scripts_script_id_versions_get) | **GET** /code-scripts/{script_id}/versions | Get Script Versions
[**list_scripts_code_scripts_get**](CodeScriptsApi.md#list_scripts_code_scripts_get) | **GET** /code-scripts | List Scripts
[**publish_script_code_scripts_script_id_publish_post**](CodeScriptsApi.md#publish_script_code_scripts_script_id_publish_post) | **POST** /code-scripts/{script_id}/publish | Publish Script
[**test_execute_script_code_scripts_test_execute_post**](CodeScriptsApi.md#test_execute_script_code_scripts_test_execute_post) | **POST** /code-scripts/test-execute | Test Execute Script
[**update_script_code_scripts_script_id_put**](CodeScriptsApi.md#update_script_code_scripts_script_id_put) | **PUT** /code-scripts/{script_id} | Update Script


# **create_script_code_scripts_post**
> CodeScriptResponse create_script_code_scripts_post(code_script_create, x_api_key=x_api_key, x_api_secret=x_api_secret)

Create Script

Create a new code script (draft)

### Example


```python
import odin_sdk
from odin_sdk.models.code_script_create import CodeScriptCreate
from odin_sdk.models.code_script_response import CodeScriptResponse
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
    api_instance = odin_sdk.CodeScriptsApi(api_client)
    code_script_create = odin_sdk.CodeScriptCreate() # CodeScriptCreate | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Create Script
        api_response = api_instance.create_script_code_scripts_post(code_script_create, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of CodeScriptsApi->create_script_code_scripts_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeScriptsApi->create_script_code_scripts_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code_script_create** | [**CodeScriptCreate**](CodeScriptCreate.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**CodeScriptResponse**](CodeScriptResponse.md)

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

# **delete_script_code_scripts_script_id_delete**
> object delete_script_code_scripts_script_id_delete(script_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Delete Script

Delete a code script

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
    api_instance = odin_sdk.CodeScriptsApi(api_client)
    script_id = 56 # int | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Delete Script
        api_response = api_instance.delete_script_code_scripts_script_id_delete(script_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of CodeScriptsApi->delete_script_code_scripts_script_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeScriptsApi->delete_script_code_scripts_script_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **script_id** | **int**|  | 
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

# **execute_script_code_scripts_script_id_execute_post**
> ExecuteScriptResponse execute_script_code_scripts_script_id_execute_post(script_id, execute_script_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Execute Script

Execute a published code script with args and kwargs

### Example


```python
import odin_sdk
from odin_sdk.models.execute_script_request import ExecuteScriptRequest
from odin_sdk.models.execute_script_response import ExecuteScriptResponse
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
    api_instance = odin_sdk.CodeScriptsApi(api_client)
    script_id = 56 # int | 
    execute_script_request = odin_sdk.ExecuteScriptRequest() # ExecuteScriptRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Execute Script
        api_response = api_instance.execute_script_code_scripts_script_id_execute_post(script_id, execute_script_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of CodeScriptsApi->execute_script_code_scripts_script_id_execute_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeScriptsApi->execute_script_code_scripts_script_id_execute_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **script_id** | **int**|  | 
 **execute_script_request** | [**ExecuteScriptRequest**](ExecuteScriptRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**ExecuteScriptResponse**](ExecuteScriptResponse.md)

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

# **get_analytics_summary_code_scripts_analytics_summary_get**
> List[ScriptAnalyticsResponse] get_analytics_summary_code_scripts_analytics_summary_get(project_id=project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Analytics Summary

Get analytics summary for all user's scripts

### Example


```python
import odin_sdk
from odin_sdk.models.script_analytics_response import ScriptAnalyticsResponse
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
    api_instance = odin_sdk.CodeScriptsApi(api_client)
    project_id = 'project_id_example' # str | Filter by project ID (optional)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Analytics Summary
        api_response = api_instance.get_analytics_summary_code_scripts_analytics_summary_get(project_id=project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of CodeScriptsApi->get_analytics_summary_code_scripts_analytics_summary_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeScriptsApi->get_analytics_summary_code_scripts_analytics_summary_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Filter by project ID | [optional] 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**List[ScriptAnalyticsResponse]**](ScriptAnalyticsResponse.md)

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

# **get_execution_detail_code_scripts_script_id_executions_execution_id_get**
> ExecutionDetailResponse get_execution_detail_code_scripts_script_id_executions_execution_id_get(script_id, execution_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Execution Detail

Get detailed execution information including input and output

### Example


```python
import odin_sdk
from odin_sdk.models.execution_detail_response import ExecutionDetailResponse
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
    api_instance = odin_sdk.CodeScriptsApi(api_client)
    script_id = 56 # int | 
    execution_id = 56 # int | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Execution Detail
        api_response = api_instance.get_execution_detail_code_scripts_script_id_executions_execution_id_get(script_id, execution_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of CodeScriptsApi->get_execution_detail_code_scripts_script_id_executions_execution_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeScriptsApi->get_execution_detail_code_scripts_script_id_executions_execution_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **script_id** | **int**|  | 
 **execution_id** | **int**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**ExecutionDetailResponse**](ExecutionDetailResponse.md)

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

# **get_execution_history_code_scripts_script_id_executions_get**
> ExecutionHistoryResponse get_execution_history_code_scripts_script_id_executions_get(script_id, page=page, page_size=page_size, status=status, start_date=start_date, end_date=end_date, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Execution History

Get execution history for a script

### Example


```python
import odin_sdk
from odin_sdk.models.execution_history_response import ExecutionHistoryResponse
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
    api_instance = odin_sdk.CodeScriptsApi(api_client)
    script_id = 56 # int | 
    page = 1 # int | Page number (optional) (default to 1)
    page_size = 50 # int | Items per page (optional) (default to 50)
    status = 'status_example' # str | Filter by execution status (optional)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | Filter executions after this date (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime | Filter executions before this date (optional)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Execution History
        api_response = api_instance.get_execution_history_code_scripts_script_id_executions_get(script_id, page=page, page_size=page_size, status=status, start_date=start_date, end_date=end_date, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of CodeScriptsApi->get_execution_history_code_scripts_script_id_executions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeScriptsApi->get_execution_history_code_scripts_script_id_executions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **script_id** | **int**|  | 
 **page** | **int**| Page number | [optional] [default to 1]
 **page_size** | **int**| Items per page | [optional] [default to 50]
 **status** | **str**| Filter by execution status | [optional] 
 **start_date** | **datetime**| Filter executions after this date | [optional] 
 **end_date** | **datetime**| Filter executions before this date | [optional] 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**ExecutionHistoryResponse**](ExecutionHistoryResponse.md)

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

# **get_script_analytics_code_scripts_script_id_analytics_get**
> ScriptAnalyticsResponse get_script_analytics_code_scripts_script_id_analytics_get(script_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Script Analytics

Get analytics for a script

### Example


```python
import odin_sdk
from odin_sdk.models.script_analytics_response import ScriptAnalyticsResponse
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
    api_instance = odin_sdk.CodeScriptsApi(api_client)
    script_id = 56 # int | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Script Analytics
        api_response = api_instance.get_script_analytics_code_scripts_script_id_analytics_get(script_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of CodeScriptsApi->get_script_analytics_code_scripts_script_id_analytics_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeScriptsApi->get_script_analytics_code_scripts_script_id_analytics_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **script_id** | **int**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**ScriptAnalyticsResponse**](ScriptAnalyticsResponse.md)

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

# **get_script_code_scripts_script_id_get**
> CodeScriptResponse get_script_code_scripts_script_id_get(script_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Script

Get a specific code script by ID

### Example


```python
import odin_sdk
from odin_sdk.models.code_script_response import CodeScriptResponse
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
    api_instance = odin_sdk.CodeScriptsApi(api_client)
    script_id = 56 # int | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Script
        api_response = api_instance.get_script_code_scripts_script_id_get(script_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of CodeScriptsApi->get_script_code_scripts_script_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeScriptsApi->get_script_code_scripts_script_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **script_id** | **int**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**CodeScriptResponse**](CodeScriptResponse.md)

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

# **get_script_versions_code_scripts_script_id_versions_get**
> List[CodeScriptResponse] get_script_versions_code_scripts_script_id_versions_get(script_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Script Versions

Get all published versions of a script by name and project

### Example


```python
import odin_sdk
from odin_sdk.models.code_script_response import CodeScriptResponse
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
    api_instance = odin_sdk.CodeScriptsApi(api_client)
    script_id = 56 # int | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Script Versions
        api_response = api_instance.get_script_versions_code_scripts_script_id_versions_get(script_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of CodeScriptsApi->get_script_versions_code_scripts_script_id_versions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeScriptsApi->get_script_versions_code_scripts_script_id_versions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **script_id** | **int**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**List[CodeScriptResponse]**](CodeScriptResponse.md)

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

# **list_scripts_code_scripts_get**
> CodeScriptListResponse list_scripts_code_scripts_get(project_id=project_id, is_published=is_published, runtime=runtime, limit=limit, offset=offset, x_api_key=x_api_key, x_api_secret=x_api_secret)

List Scripts

List user's code scripts with optional filtering

### Example


```python
import odin_sdk
from odin_sdk.models.code_script_list_response import CodeScriptListResponse
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
    api_instance = odin_sdk.CodeScriptsApi(api_client)
    project_id = 'project_id_example' # str | Filter by project ID (optional)
    is_published = True # bool | Filter by published status (optional)
    runtime = 'runtime_example' # str | Filter by runtime (optional)
    limit = 50 # int | Number of scripts to return (optional) (default to 50)
    offset = 0 # int | Number of scripts to skip (optional) (default to 0)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # List Scripts
        api_response = api_instance.list_scripts_code_scripts_get(project_id=project_id, is_published=is_published, runtime=runtime, limit=limit, offset=offset, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of CodeScriptsApi->list_scripts_code_scripts_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeScriptsApi->list_scripts_code_scripts_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Filter by project ID | [optional] 
 **is_published** | **bool**| Filter by published status | [optional] 
 **runtime** | **str**| Filter by runtime | [optional] 
 **limit** | **int**| Number of scripts to return | [optional] [default to 50]
 **offset** | **int**| Number of scripts to skip | [optional] [default to 0]
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**CodeScriptListResponse**](CodeScriptListResponse.md)

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

# **publish_script_code_scripts_script_id_publish_post**
> PublishResponse publish_script_code_scripts_script_id_publish_post(script_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Publish Script

Publish a draft script with auto-incrementing version

### Example


```python
import odin_sdk
from odin_sdk.models.publish_response import PublishResponse
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
    api_instance = odin_sdk.CodeScriptsApi(api_client)
    script_id = 56 # int | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Publish Script
        api_response = api_instance.publish_script_code_scripts_script_id_publish_post(script_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of CodeScriptsApi->publish_script_code_scripts_script_id_publish_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeScriptsApi->publish_script_code_scripts_script_id_publish_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **script_id** | **int**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**PublishResponse**](PublishResponse.md)

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

# **test_execute_script_code_scripts_test_execute_post**
> TestExecuteResponse test_execute_script_code_scripts_test_execute_post(test_execute_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Test Execute Script

Execute a code script without database persistence (for testing)

### Example


```python
import odin_sdk
from odin_sdk.models.test_execute_request import TestExecuteRequest
from odin_sdk.models.test_execute_response import TestExecuteResponse
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
    api_instance = odin_sdk.CodeScriptsApi(api_client)
    test_execute_request = odin_sdk.TestExecuteRequest() # TestExecuteRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Test Execute Script
        api_response = api_instance.test_execute_script_code_scripts_test_execute_post(test_execute_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of CodeScriptsApi->test_execute_script_code_scripts_test_execute_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeScriptsApi->test_execute_script_code_scripts_test_execute_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_execute_request** | [**TestExecuteRequest**](TestExecuteRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**TestExecuteResponse**](TestExecuteResponse.md)

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

# **update_script_code_scripts_script_id_put**
> CodeScriptResponse update_script_code_scripts_script_id_put(script_id, code_script_update, x_api_key=x_api_key, x_api_secret=x_api_secret)

Update Script

Update a code script (only drafts can be updated)

### Example


```python
import odin_sdk
from odin_sdk.models.code_script_response import CodeScriptResponse
from odin_sdk.models.code_script_update import CodeScriptUpdate
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
    api_instance = odin_sdk.CodeScriptsApi(api_client)
    script_id = 56 # int | 
    code_script_update = odin_sdk.CodeScriptUpdate() # CodeScriptUpdate | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Update Script
        api_response = api_instance.update_script_code_scripts_script_id_put(script_id, code_script_update, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of CodeScriptsApi->update_script_code_scripts_script_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeScriptsApi->update_script_code_scripts_script_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **script_id** | **int**|  | 
 **code_script_update** | [**CodeScriptUpdate**](CodeScriptUpdate.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**CodeScriptResponse**](CodeScriptResponse.md)

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

