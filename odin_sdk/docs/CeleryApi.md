# odin_sdk.CeleryApi

All URIs are relative to *http://127.0.0.1:8001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_active_tasks_endpoint_admin_celery_active_tasks_get**](CeleryApi.md#get_active_tasks_endpoint_admin_celery_active_tasks_get) | **GET** /admin/celery/active-tasks | Get Active Tasks Endpoint
[**get_task_info_admin_celery_task_task_id_get**](CeleryApi.md#get_task_info_admin_celery_task_task_id_get) | **GET** /admin/celery/task/{task_id} | Get Task Info
[**get_task_stats_admin_celery_stats_get**](CeleryApi.md#get_task_stats_admin_celery_stats_get) | **GET** /admin/celery/stats | Get Task Stats
[**get_tasks_admin_celery_tasks_get**](CeleryApi.md#get_tasks_admin_celery_tasks_get) | **GET** /admin/celery/tasks | Get Tasks
[**get_workers_admin_celery_workers_get**](CeleryApi.md#get_workers_admin_celery_workers_get) | **GET** /admin/celery/workers | Get Workers
[**retry_task_admin_celery_task_task_id_retry_post**](CeleryApi.md#retry_task_admin_celery_task_task_id_retry_post) | **POST** /admin/celery/task/{task_id}/retry | Retry Task
[**terminate_task_admin_celery_task_task_id_terminate_post**](CeleryApi.md#terminate_task_admin_celery_task_task_id_terminate_post) | **POST** /admin/celery/task/{task_id}/terminate | Terminate Task


# **get_active_tasks_endpoint_admin_celery_active_tasks_get**
> List[TaskInfoModel] get_active_tasks_endpoint_admin_celery_active_tasks_get(x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Active Tasks Endpoint

Get all currently running Celery tasks

### Example


```python
import odin_sdk
from odin_sdk.models.task_info_model import TaskInfoModel
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
    api_instance = odin_sdk.CeleryApi(api_client)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Active Tasks Endpoint
        api_response = api_instance.get_active_tasks_endpoint_admin_celery_active_tasks_get(x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of CeleryApi->get_active_tasks_endpoint_admin_celery_active_tasks_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CeleryApi->get_active_tasks_endpoint_admin_celery_active_tasks_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**List[TaskInfoModel]**](TaskInfoModel.md)

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

# **get_task_info_admin_celery_task_task_id_get**
> TaskInfoModel get_task_info_admin_celery_task_task_id_get(task_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Task Info

Get detailed information about a specific task by ID

### Example


```python
import odin_sdk
from odin_sdk.models.task_info_model import TaskInfoModel
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
    api_instance = odin_sdk.CeleryApi(api_client)
    task_id = 'task_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Task Info
        api_response = api_instance.get_task_info_admin_celery_task_task_id_get(task_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of CeleryApi->get_task_info_admin_celery_task_task_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CeleryApi->get_task_info_admin_celery_task_task_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**TaskInfoModel**](TaskInfoModel.md)

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

# **get_task_stats_admin_celery_stats_get**
> List[TaskStatsModel] get_task_stats_admin_celery_stats_get(timeframe=timeframe, project_ids=project_ids, user_ids=user_ids, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Task Stats

Get statistics about task execution (success rates, timing, etc.)
Supports filtering by project_ids, user_ids, and custom time intervals

### Example


```python
import odin_sdk
from odin_sdk.models.task_stats_model import TaskStatsModel
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
    api_instance = odin_sdk.CeleryApi(api_client)
    timeframe = '7d' # str | Time frame: 24h, 7d, 30d (optional) (default to '7d')
    project_ids = 'project_ids_example' # str | Comma-separated list of project IDs (optional)
    user_ids = 'user_ids_example' # str | Comma-separated list of user IDs or emails (optional)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Task Stats
        api_response = api_instance.get_task_stats_admin_celery_stats_get(timeframe=timeframe, project_ids=project_ids, user_ids=user_ids, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of CeleryApi->get_task_stats_admin_celery_stats_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CeleryApi->get_task_stats_admin_celery_stats_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeframe** | **str**| Time frame: 24h, 7d, 30d | [optional] [default to &#39;7d&#39;]
 **project_ids** | **str**| Comma-separated list of project IDs | [optional] 
 **user_ids** | **str**| Comma-separated list of user IDs or emails | [optional] 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**List[TaskStatsModel]**](TaskStatsModel.md)

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

# **get_tasks_admin_celery_tasks_get**
> List[TaskInfoModel] get_tasks_admin_celery_tasks_get(limit=limit, offset=offset, status=status, task_name=task_name, project_id=project_id, user_id=user_id, timeframe=timeframe, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Tasks

Get historical tasks with filtering options

### Example


```python
import odin_sdk
from odin_sdk.models.task_info_model import TaskInfoModel
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
    api_instance = odin_sdk.CeleryApi(api_client)
    limit = 100 # int |  (optional) (default to 100)
    offset = 0 # int |  (optional) (default to 0)
    status = 'status_example' # str |  (optional)
    task_name = 'task_name_example' # str |  (optional)
    project_id = 'project_id_example' # str |  (optional)
    user_id = 'user_id_example' # str |  (optional)
    timeframe = '24h' # str | Time frame: 24h, 7d, 30d (optional) (default to '24h')
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Tasks
        api_response = api_instance.get_tasks_admin_celery_tasks_get(limit=limit, offset=offset, status=status, task_name=task_name, project_id=project_id, user_id=user_id, timeframe=timeframe, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of CeleryApi->get_tasks_admin_celery_tasks_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CeleryApi->get_tasks_admin_celery_tasks_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 100]
 **offset** | **int**|  | [optional] [default to 0]
 **status** | **str**|  | [optional] 
 **task_name** | **str**|  | [optional] 
 **project_id** | **str**|  | [optional] 
 **user_id** | **str**|  | [optional] 
 **timeframe** | **str**| Time frame: 24h, 7d, 30d | [optional] [default to &#39;24h&#39;]
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**List[TaskInfoModel]**](TaskInfoModel.md)

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

# **get_workers_admin_celery_workers_get**
> List[WorkerInfoModel] get_workers_admin_celery_workers_get(x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Workers

Get information about all active Celery workers

### Example


```python
import odin_sdk
from odin_sdk.models.worker_info_model import WorkerInfoModel
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
    api_instance = odin_sdk.CeleryApi(api_client)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Workers
        api_response = api_instance.get_workers_admin_celery_workers_get(x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of CeleryApi->get_workers_admin_celery_workers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CeleryApi->get_workers_admin_celery_workers_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**List[WorkerInfoModel]**](WorkerInfoModel.md)

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

# **retry_task_admin_celery_task_task_id_retry_post**
> Dict[str, Optional[str]] retry_task_admin_celery_task_task_id_retry_post(task_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Retry Task

Retry a failed task

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
    api_instance = odin_sdk.CeleryApi(api_client)
    task_id = 'task_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Retry Task
        api_response = api_instance.retry_task_admin_celery_task_task_id_retry_post(task_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of CeleryApi->retry_task_admin_celery_task_task_id_retry_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CeleryApi->retry_task_admin_celery_task_task_id_retry_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

**Dict[str, Optional[str]]**

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

# **terminate_task_admin_celery_task_task_id_terminate_post**
> Dict[str, Optional[str]] terminate_task_admin_celery_task_task_id_terminate_post(task_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Terminate Task

Terminate a running task with SIGTERM.

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
    api_instance = odin_sdk.CeleryApi(api_client)
    task_id = 'task_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Terminate Task
        api_response = api_instance.terminate_task_admin_celery_task_task_id_terminate_post(task_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of CeleryApi->terminate_task_admin_celery_task_task_id_terminate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CeleryApi->terminate_task_admin_celery_task_task_id_terminate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

**Dict[str, Optional[str]]**

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

