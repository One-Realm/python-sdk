# odin_sdk.DataTypesApi

All URIs are relative to *http://127.0.0.1:8001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_data_type_project_project_id_data_types_post**](DataTypesApi.md#create_data_type_project_project_id_data_types_post) | **POST** /project/{project_id}/data-types | Create Data Type
[**delete_data_type_by_id_project_project_id_data_types_data_type_id_delete**](DataTypesApi.md#delete_data_type_by_id_project_project_id_data_types_data_type_id_delete) | **DELETE** /project/{project_id}/data-types/{data_type_id} | Delete Data Type By Id
[**get_data_type_by_id_project_project_id_data_types_data_type_id_get**](DataTypesApi.md#get_data_type_by_id_project_project_id_data_types_data_type_id_get) | **GET** /project/{project_id}/data-types/{data_type_id} | Get Data Type By Id
[**get_data_types_project_project_id_data_types_get**](DataTypesApi.md#get_data_types_project_project_id_data_types_get) | **GET** /project/{project_id}/data-types | Get Data Types
[**import_table_project_project_id_import_table_post**](DataTypesApi.md#import_table_project_project_id_import_table_post) | **POST** /project/{project_id}/import-table | Import Table


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

