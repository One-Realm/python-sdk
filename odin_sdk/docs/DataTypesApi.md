# odin_sdk.DataTypesApi

All URIs are relative to *http://127.0.0.1:8001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_compute_column_job_project_project_id_data_type_data_type_id_compute_column_cancel_execution_id_post**](DataTypesApi.md#cancel_compute_column_job_project_project_id_data_type_data_type_id_compute_column_cancel_execution_id_post) | **POST** /project/{project_id}/data-type/{data_type_id}/compute-column/cancel/{execution_id} | Cancel Compute Column Job
[**compute_column_values_async_project_project_id_data_type_data_type_id_compute_column_async_post**](DataTypesApi.md#compute_column_values_async_project_project_id_data_type_data_type_id_compute_column_async_post) | **POST** /project/{project_id}/data-type/{data_type_id}/compute-column/async | Compute Column Values Async
[**create_data_type_project_project_id_data_types_post**](DataTypesApi.md#create_data_type_project_project_id_data_types_post) | **POST** /project/{project_id}/data-types | Create Data Type
[**create_data_type_view_project_project_id_data_type_data_type_id_view_post**](DataTypesApi.md#create_data_type_view_project_project_id_data_type_data_type_id_view_post) | **POST** /project/{project_id}/data-type/{data_type_id}/view | Create Data Type View
[**delete_data_type_by_id_project_project_id_data_types_data_type_id_delete**](DataTypesApi.md#delete_data_type_by_id_project_project_id_data_types_data_type_id_delete) | **DELETE** /project/{project_id}/data-types/{data_type_id} | Delete Data Type By Id
[**get_compute_column_jobs_project_project_id_data_type_data_type_id_compute_column_jobs_get**](DataTypesApi.md#get_compute_column_jobs_project_project_id_data_type_data_type_id_compute_column_jobs_get) | **GET** /project/{project_id}/data-type/{data_type_id}/compute-column/jobs | Get Compute Column Jobs
[**get_compute_column_status_project_project_id_data_type_data_type_id_compute_column_status_execution_id_get**](DataTypesApi.md#get_compute_column_status_project_project_id_data_type_data_type_id_compute_column_status_execution_id_get) | **GET** /project/{project_id}/data-type/{data_type_id}/compute-column/status/{execution_id} | Get Compute Column Status
[**get_data_type_by_id_project_project_id_data_types_data_type_id_get**](DataTypesApi.md#get_data_type_by_id_project_project_id_data_types_data_type_id_get) | **GET** /project/{project_id}/data-types/{data_type_id} | Get Data Type By Id
[**get_data_type_view_by_id_project_project_id_data_types_data_type_id_view_get**](DataTypesApi.md#get_data_type_view_by_id_project_project_id_data_types_data_type_id_view_get) | **GET** /project/{project_id}/data-types/{data_type_id}/view | Get Data Type View By Id
[**get_data_types_project_project_id_data_types_get**](DataTypesApi.md#get_data_types_project_project_id_data_types_get) | **GET** /project/{project_id}/data-types | Get Data Types
[**get_grouped_data_type_view_by_id_project_project_id_data_types_data_type_id_view_grouped_get**](DataTypesApi.md#get_grouped_data_type_view_by_id_project_project_id_data_types_data_type_id_view_grouped_get) | **GET** /project/{project_id}/data-types/{data_type_id}/view/grouped | Get Grouped Data Type View By Id
[**get_template_details_project_project_id_data_type_templates_template_name_get**](DataTypesApi.md#get_template_details_project_project_id_data_type_templates_template_name_get) | **GET** /project/{project_id}/data-type-templates/{template_name} | Get Template Details
[**get_templates_project_project_id_data_type_templates_get**](DataTypesApi.md#get_templates_project_project_id_data_type_templates_get) | **GET** /project/{project_id}/data-type-templates | Get Templates
[**import_table_project_project_id_import_table_post**](DataTypesApi.md#import_table_project_project_id_import_table_post) | **POST** /project/{project_id}/import-table | Import Table
[**update_data_type_view_project_project_id_data_type_data_type_id_view_view_id_put**](DataTypesApi.md#update_data_type_view_project_project_id_data_type_data_type_id_view_view_id_put) | **PUT** /project/{project_id}/data-type/{data_type_id}/view/{view_id} | Update Data Type View
[**use_template_project_project_id_data_type_templates_use_post**](DataTypesApi.md#use_template_project_project_id_data_type_templates_use_post) | **POST** /project/{project_id}/data-type-templates/use | Use Template


# **cancel_compute_column_job_project_project_id_data_type_data_type_id_compute_column_cancel_execution_id_post**
> ComputeColumnCancelResponse cancel_compute_column_job_project_project_id_data_type_data_type_id_compute_column_cancel_execution_id_post(project_id, data_type_id, execution_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Cancel Compute Column Job

Cancel a running column computation job

### Example


```python
import odin_sdk
from odin_sdk.models.compute_column_cancel_response import ComputeColumnCancelResponse
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
    api_instance = odin_sdk.DataTypesApi(api_client)
    project_id = 'project_id_example' # str | 
    data_type_id = 'data_type_id_example' # str | 
    execution_id = 'execution_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Cancel Compute Column Job
        api_response = api_instance.cancel_compute_column_job_project_project_id_data_type_data_type_id_compute_column_cancel_execution_id_post(project_id, data_type_id, execution_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DataTypesApi->cancel_compute_column_job_project_project_id_data_type_data_type_id_compute_column_cancel_execution_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTypesApi->cancel_compute_column_job_project_project_id_data_type_data_type_id_compute_column_cancel_execution_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **data_type_id** | **str**|  | 
 **execution_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**ComputeColumnCancelResponse**](ComputeColumnCancelResponse.md)

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

# **compute_column_values_async_project_project_id_data_type_data_type_id_compute_column_async_post**
> ComputeColumnAsyncResponse compute_column_values_async_project_project_id_data_type_data_type_id_compute_column_async_post(project_id, data_type_id, compute_column_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Compute Column Values Async

Start async computation of column values using LLM

### Example


```python
import odin_sdk
from odin_sdk.models.compute_column_async_response import ComputeColumnAsyncResponse
from odin_sdk.models.compute_column_request import ComputeColumnRequest
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
    api_instance = odin_sdk.DataTypesApi(api_client)
    project_id = 'project_id_example' # str | 
    data_type_id = 'data_type_id_example' # str | 
    compute_column_request = odin_sdk.ComputeColumnRequest() # ComputeColumnRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Compute Column Values Async
        api_response = api_instance.compute_column_values_async_project_project_id_data_type_data_type_id_compute_column_async_post(project_id, data_type_id, compute_column_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DataTypesApi->compute_column_values_async_project_project_id_data_type_data_type_id_compute_column_async_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTypesApi->compute_column_values_async_project_project_id_data_type_data_type_id_compute_column_async_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **data_type_id** | **str**|  | 
 **compute_column_request** | [**ComputeColumnRequest**](ComputeColumnRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**ComputeColumnAsyncResponse**](ComputeColumnAsyncResponse.md)

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

# **create_data_type_project_project_id_data_types_post**
> RoutesDataTypesAddDataTypeResponse create_data_type_project_project_id_data_types_post(project_id, routes_data_types_add_data_type_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Create Data Type

Create a Data Type

### Example


```python
import odin_sdk
from odin_sdk.models.routes_data_types_add_data_type_request import RoutesDataTypesAddDataTypeRequest
from odin_sdk.models.routes_data_types_add_data_type_response import RoutesDataTypesAddDataTypeResponse
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
    api_instance = odin_sdk.DataTypesApi(api_client)
    project_id = 'project_id_example' # str | 
    routes_data_types_add_data_type_request = odin_sdk.RoutesDataTypesAddDataTypeRequest() # RoutesDataTypesAddDataTypeRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Create Data Type
        api_response = api_instance.create_data_type_project_project_id_data_types_post(project_id, routes_data_types_add_data_type_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DataTypesApi->create_data_type_project_project_id_data_types_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTypesApi->create_data_type_project_project_id_data_types_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **routes_data_types_add_data_type_request** | [**RoutesDataTypesAddDataTypeRequest**](RoutesDataTypesAddDataTypeRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**RoutesDataTypesAddDataTypeResponse**](RoutesDataTypesAddDataTypeResponse.md)

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

# **create_data_type_view_project_project_id_data_type_data_type_id_view_post**
> CreateViewResponse create_data_type_view_project_project_id_data_type_data_type_id_view_post(project_id, data_type_id, create_view_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Create Data Type View

Create a new view for a data type

### Example


```python
import odin_sdk
from odin_sdk.models.create_view_request import CreateViewRequest
from odin_sdk.models.create_view_response import CreateViewResponse
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
    api_instance = odin_sdk.DataTypesApi(api_client)
    project_id = 'project_id_example' # str | 
    data_type_id = 'data_type_id_example' # str | 
    create_view_request = odin_sdk.CreateViewRequest() # CreateViewRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Create Data Type View
        api_response = api_instance.create_data_type_view_project_project_id_data_type_data_type_id_view_post(project_id, data_type_id, create_view_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DataTypesApi->create_data_type_view_project_project_id_data_type_data_type_id_view_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTypesApi->create_data_type_view_project_project_id_data_type_data_type_id_view_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **data_type_id** | **str**|  | 
 **create_view_request** | [**CreateViewRequest**](CreateViewRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**CreateViewResponse**](CreateViewResponse.md)

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

# **delete_data_type_by_id_project_project_id_data_types_data_type_id_delete**
> DeleteDataTypeResponse delete_data_type_by_id_project_project_id_data_types_data_type_id_delete(project_id, data_type_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Delete Data Type By Id

Delete a Data Type

### Example


```python
import odin_sdk
from odin_sdk.models.delete_data_type_response import DeleteDataTypeResponse
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
    api_instance = odin_sdk.DataTypesApi(api_client)
    project_id = 'project_id_example' # str | 
    data_type_id = 'data_type_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Delete Data Type By Id
        api_response = api_instance.delete_data_type_by_id_project_project_id_data_types_data_type_id_delete(project_id, data_type_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DataTypesApi->delete_data_type_by_id_project_project_id_data_types_data_type_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTypesApi->delete_data_type_by_id_project_project_id_data_types_data_type_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **data_type_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**DeleteDataTypeResponse**](DeleteDataTypeResponse.md)

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

# **get_compute_column_jobs_project_project_id_data_type_data_type_id_compute_column_jobs_get**
> ComputeColumnJobsResponse get_compute_column_jobs_project_project_id_data_type_data_type_id_compute_column_jobs_get(project_id, data_type_id, limit=limit, offset=offset, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Compute Column Jobs

Get all column computation jobs for a data type

### Example


```python
import odin_sdk
from odin_sdk.models.compute_column_jobs_response import ComputeColumnJobsResponse
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
    api_instance = odin_sdk.DataTypesApi(api_client)
    project_id = 'project_id_example' # str | 
    data_type_id = 'data_type_id_example' # str | 
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Compute Column Jobs
        api_response = api_instance.get_compute_column_jobs_project_project_id_data_type_data_type_id_compute_column_jobs_get(project_id, data_type_id, limit=limit, offset=offset, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DataTypesApi->get_compute_column_jobs_project_project_id_data_type_data_type_id_compute_column_jobs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTypesApi->get_compute_column_jobs_project_project_id_data_type_data_type_id_compute_column_jobs_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **data_type_id** | **str**|  | 
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**ComputeColumnJobsResponse**](ComputeColumnJobsResponse.md)

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

# **get_compute_column_status_project_project_id_data_type_data_type_id_compute_column_status_execution_id_get**
> ComputeColumnStatusResponse get_compute_column_status_project_project_id_data_type_data_type_id_compute_column_status_execution_id_get(project_id, data_type_id, execution_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Compute Column Status

Get the status of a column computation job

### Example


```python
import odin_sdk
from odin_sdk.models.compute_column_status_response import ComputeColumnStatusResponse
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
    api_instance = odin_sdk.DataTypesApi(api_client)
    project_id = 'project_id_example' # str | 
    data_type_id = 'data_type_id_example' # str | 
    execution_id = 'execution_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Compute Column Status
        api_response = api_instance.get_compute_column_status_project_project_id_data_type_data_type_id_compute_column_status_execution_id_get(project_id, data_type_id, execution_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DataTypesApi->get_compute_column_status_project_project_id_data_type_data_type_id_compute_column_status_execution_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTypesApi->get_compute_column_status_project_project_id_data_type_data_type_id_compute_column_status_execution_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **data_type_id** | **str**|  | 
 **execution_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**ComputeColumnStatusResponse**](ComputeColumnStatusResponse.md)

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

# **get_data_type_by_id_project_project_id_data_types_data_type_id_get**
> RoutesDataTypesGetDataTypeResponse get_data_type_by_id_project_project_id_data_types_data_type_id_get(project_id, data_type_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Data Type By Id

Fetch a specific data type by id

### Example


```python
import odin_sdk
from odin_sdk.models.routes_data_types_get_data_type_response import RoutesDataTypesGetDataTypeResponse
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
    api_instance = odin_sdk.DataTypesApi(api_client)
    project_id = 'project_id_example' # str | 
    data_type_id = 'data_type_id_example' # str | ID of the data type
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Data Type By Id
        api_response = api_instance.get_data_type_by_id_project_project_id_data_types_data_type_id_get(project_id, data_type_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DataTypesApi->get_data_type_by_id_project_project_id_data_types_data_type_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTypesApi->get_data_type_by_id_project_project_id_data_types_data_type_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **data_type_id** | **str**| ID of the data type | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**RoutesDataTypesGetDataTypeResponse**](RoutesDataTypesGetDataTypeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Data type not found. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_type_view_by_id_project_project_id_data_types_data_type_id_view_get**
> GetDataTypeViewResponse get_data_type_view_by_id_project_project_id_data_types_data_type_id_view_get(project_id, data_type_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Data Type View By Id

Fetch a specific data type view by id with pagination support. Default: 100 records per page. Query params: page (int), limit (int), search (string), sort_column (string), sort_direction (asc/desc)

### Example


```python
import odin_sdk
from odin_sdk.models.get_data_type_view_response import GetDataTypeViewResponse
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
    api_instance = odin_sdk.DataTypesApi(api_client)
    project_id = 'project_id_example' # str | 
    data_type_id = 'data_type_id_example' # str | ID of the data type
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Data Type View By Id
        api_response = api_instance.get_data_type_view_by_id_project_project_id_data_types_data_type_id_view_get(project_id, data_type_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DataTypesApi->get_data_type_view_by_id_project_project_id_data_types_data_type_id_view_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTypesApi->get_data_type_view_by_id_project_project_id_data_types_data_type_id_view_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **data_type_id** | **str**| ID of the data type | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**GetDataTypeViewResponse**](GetDataTypeViewResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Data type view not found. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_types_project_project_id_data_types_get**
> RoutesDataTypesGetDataTypesResponse get_data_types_project_project_id_data_types_get(project_id, sent_internally=sent_internally, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Data Types

Fetch the data types for the specified project

### Example


```python
import odin_sdk
from odin_sdk.models.routes_data_types_get_data_types_response import RoutesDataTypesGetDataTypesResponse
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
    api_instance = odin_sdk.DataTypesApi(api_client)
    project_id = 'project_id_example' # str | 
    sent_internally = True # bool |  (optional)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Data Types
        api_response = api_instance.get_data_types_project_project_id_data_types_get(project_id, sent_internally=sent_internally, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DataTypesApi->get_data_types_project_project_id_data_types_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTypesApi->get_data_types_project_project_id_data_types_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **sent_internally** | **bool**|  | [optional] 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**RoutesDataTypesGetDataTypesResponse**](RoutesDataTypesGetDataTypesResponse.md)

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

# **get_grouped_data_type_view_by_id_project_project_id_data_types_data_type_id_view_grouped_get**
> GetGroupedDataTypeViewResponse get_grouped_data_type_view_by_id_project_project_id_data_types_data_type_id_view_grouped_get(project_id, data_type_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Grouped Data Type View By Id

Fetch a specific data type view grouped by a column with pagination support. Query params: group_column (string), group_column_type (string), search (string), sort_column (string), sort_direction (asc/desc)

### Example


```python
import odin_sdk
from odin_sdk.models.get_grouped_data_type_view_response import GetGroupedDataTypeViewResponse
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
    api_instance = odin_sdk.DataTypesApi(api_client)
    project_id = 'project_id_example' # str | 
    data_type_id = 'data_type_id_example' # str | ID of the data type
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Grouped Data Type View By Id
        api_response = api_instance.get_grouped_data_type_view_by_id_project_project_id_data_types_data_type_id_view_grouped_get(project_id, data_type_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DataTypesApi->get_grouped_data_type_view_by_id_project_project_id_data_types_data_type_id_view_grouped_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTypesApi->get_grouped_data_type_view_by_id_project_project_id_data_types_data_type_id_view_grouped_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **data_type_id** | **str**| ID of the data type | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**GetGroupedDataTypeViewResponse**](GetGroupedDataTypeViewResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Data type view not found. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template_details_project_project_id_data_type_templates_template_name_get**
> object get_template_details_project_project_id_data_type_templates_template_name_get(project_id, template_name, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Template Details

Get detailed information about a specific template

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
    api_instance = odin_sdk.DataTypesApi(api_client)
    project_id = 'project_id_example' # str | 
    template_name = 'template_name_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Template Details
        api_response = api_instance.get_template_details_project_project_id_data_type_templates_template_name_get(project_id, template_name, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DataTypesApi->get_template_details_project_project_id_data_type_templates_template_name_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTypesApi->get_template_details_project_project_id_data_type_templates_template_name_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **template_name** | **str**|  | 
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

# **get_templates_project_project_id_data_type_templates_get**
> GetTemplatesResponse get_templates_project_project_id_data_type_templates_get(project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Templates

Get all available data type templates

### Example


```python
import odin_sdk
from odin_sdk.models.get_templates_response import GetTemplatesResponse
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
    api_instance = odin_sdk.DataTypesApi(api_client)
    project_id = 'project_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Templates
        api_response = api_instance.get_templates_project_project_id_data_type_templates_get(project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DataTypesApi->get_templates_project_project_id_data_type_templates_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTypesApi->get_templates_project_project_id_data_type_templates_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**GetTemplatesResponse**](GetTemplatesResponse.md)

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

# **import_table_project_project_id_import_table_post**
> ImportTableResponse import_table_project_project_id_import_table_post(project_id, title, description, column_mappings, file, x_api_key=x_api_key, x_api_secret=x_api_secret, delimiter=delimiter)

Import Table

Import a CSV, XLSX, or JSON file as a data table

### Example


```python
import odin_sdk
from odin_sdk.models.import_table_response import ImportTableResponse
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
    api_instance = odin_sdk.DataTypesApi(api_client)
    project_id = 'project_id_example' # str | 
    title = 'title_example' # str | 
    description = 'description_example' # str | 
    column_mappings = 'column_mappings_example' # str | 
    file = None # bytearray | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)
    delimiter = ',' # str | The delimiter used in the file (optional) (default to ',')

    try:
        # Import Table
        api_response = api_instance.import_table_project_project_id_import_table_post(project_id, title, description, column_mappings, file, x_api_key=x_api_key, x_api_secret=x_api_secret, delimiter=delimiter)
        print("The response of DataTypesApi->import_table_project_project_id_import_table_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTypesApi->import_table_project_project_id_import_table_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **title** | **str**|  | 
 **description** | **str**|  | 
 **column_mappings** | **str**|  | 
 **file** | **bytearray**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 
 **delimiter** | **str**| The delimiter used in the file | [optional] [default to &#39;,&#39;]

### Return type

[**ImportTableResponse**](ImportTableResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_data_type_view_project_project_id_data_type_data_type_id_view_view_id_put**
> UpdateViewResponse update_data_type_view_project_project_id_data_type_data_type_id_view_view_id_put(project_id, data_type_id, view_id, update_view_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Update Data Type View

Update a data type view configuration

### Example


```python
import odin_sdk
from odin_sdk.models.update_view_request import UpdateViewRequest
from odin_sdk.models.update_view_response import UpdateViewResponse
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
    api_instance = odin_sdk.DataTypesApi(api_client)
    project_id = 'project_id_example' # str | 
    data_type_id = 'data_type_id_example' # str | 
    view_id = 'view_id_example' # str | 
    update_view_request = odin_sdk.UpdateViewRequest() # UpdateViewRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Update Data Type View
        api_response = api_instance.update_data_type_view_project_project_id_data_type_data_type_id_view_view_id_put(project_id, data_type_id, view_id, update_view_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DataTypesApi->update_data_type_view_project_project_id_data_type_data_type_id_view_view_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTypesApi->update_data_type_view_project_project_id_data_type_data_type_id_view_view_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **data_type_id** | **str**|  | 
 **view_id** | **str**|  | 
 **update_view_request** | [**UpdateViewRequest**](UpdateViewRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**UpdateViewResponse**](UpdateViewResponse.md)

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

# **use_template_project_project_id_data_type_templates_use_post**
> UseTemplateResponse use_template_project_project_id_data_type_templates_use_post(project_id, use_template_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Use Template

Use a template to create a new data type with custom title

### Example


```python
import odin_sdk
from odin_sdk.models.use_template_request import UseTemplateRequest
from odin_sdk.models.use_template_response import UseTemplateResponse
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
    api_instance = odin_sdk.DataTypesApi(api_client)
    project_id = 'project_id_example' # str | 
    use_template_request = odin_sdk.UseTemplateRequest() # UseTemplateRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Use Template
        api_response = api_instance.use_template_project_project_id_data_type_templates_use_post(project_id, use_template_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DataTypesApi->use_template_project_project_id_data_type_templates_use_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTypesApi->use_template_project_project_id_data_type_templates_use_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **use_template_request** | [**UseTemplateRequest**](UseTemplateRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**UseTemplateResponse**](UseTemplateResponse.md)

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

