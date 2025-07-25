# odin_sdk.TaskStatusApi

All URIs are relative to *http://127.0.0.1:8001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_project_task_statuses_project_id_tasks_get**](TaskStatusApi.md#get_project_task_statuses_project_id_tasks_get) | **GET** /{project_id}/tasks | Get Project Task Statuses
[**get_task_status_project_id_task_task_id_get**](TaskStatusApi.md#get_task_status_project_id_task_task_id_get) | **GET** /{project_id}/task/{task_id} | Get Task Status


# **get_project_task_statuses_project_id_tasks_get**
> TaskStatusListResponse get_project_task_statuses_project_id_tasks_get(project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Project Task Statuses

Get the status of all Celery tasks for a specific project

### Example


```python
import odin_sdk
from odin_sdk.models.task_status_list_response import TaskStatusListResponse
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
    api_instance = odin_sdk.TaskStatusApi(api_client)
    project_id = 'project_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Project Task Statuses
        api_response = api_instance.get_project_task_statuses_project_id_tasks_get(project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of TaskStatusApi->get_project_task_statuses_project_id_tasks_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskStatusApi->get_project_task_statuses_project_id_tasks_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**TaskStatusListResponse**](TaskStatusListResponse.md)

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

# **get_task_status_project_id_task_task_id_get**
> TaskStatusResponse get_task_status_project_id_task_task_id_get(project_id, task_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Task Status

Get the status of a specific Celery task by task ID

### Example


```python
import odin_sdk
from odin_sdk.models.task_status_response import TaskStatusResponse
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
    api_instance = odin_sdk.TaskStatusApi(api_client)
    project_id = 'project_id_example' # str | 
    task_id = 'task_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Task Status
        api_response = api_instance.get_task_status_project_id_task_task_id_get(project_id, task_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of TaskStatusApi->get_task_status_project_id_task_task_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskStatusApi->get_task_status_project_id_task_task_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **task_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**TaskStatusResponse**](TaskStatusResponse.md)

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

