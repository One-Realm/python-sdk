# odin_sdk.DataTypesApi

All URIs are relative to *http://127.0.0.1:8001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_data_type_for_project_project_project_id_data_types_data_type_id_activate_put**](DataTypesApi.md#activate_data_type_for_project_project_project_id_data_types_data_type_id_activate_put) | **PUT** /project/{project_id}/data-types/{data_type_id}/activate | Activate Data Type For Project
[**add_column_project_project_id_data_type_data_type_id_column_post**](DataTypesApi.md#add_column_project_project_id_data_type_data_type_id_column_post) | **POST** /project/{project_id}/data-type/{data_type_id}/column | Add Column
[**add_data_type_row_project_project_id_data_type_data_type_id_row_post**](DataTypesApi.md#add_data_type_row_project_project_id_data_type_data_type_id_row_post) | **POST** /project/{project_id}/data-type/{data_type_id}/row | Add Data Type Row
[**add_multiple_columns_project_project_id_data_type_data_type_id_columns_post**](DataTypesApi.md#add_multiple_columns_project_project_id_data_type_data_type_id_columns_post) | **POST** /project/{project_id}/data-type/{data_type_id}/columns | Add Multiple Columns
[**add_multiple_data_type_rows_project_project_id_data_type_data_type_id_rows_post**](DataTypesApi.md#add_multiple_data_type_rows_project_project_id_data_type_data_type_id_rows_post) | **POST** /project/{project_id}/data-type/{data_type_id}/rows | Add Multiple Data Type Rows
[**cancel_compute_column_job_project_project_id_data_type_data_type_id_compute_column_cancel_execution_id_post**](DataTypesApi.md#cancel_compute_column_job_project_project_id_data_type_data_type_id_compute_column_cancel_execution_id_post) | **POST** /project/{project_id}/data-type/{data_type_id}/compute-column/cancel/{execution_id} | Cancel Compute Column Job
[**compute_all_rows_project_project_id_data_type_data_type_id_compute_all_rows_post**](DataTypesApi.md#compute_all_rows_project_project_id_data_type_data_type_id_compute_all_rows_post) | **POST** /project/{project_id}/data-type/{data_type_id}/compute-all-rows | Compute All Rows
[**compute_column_values_async_project_project_id_data_type_data_type_id_compute_column_async_post**](DataTypesApi.md#compute_column_values_async_project_project_id_data_type_data_type_id_compute_column_async_post) | **POST** /project/{project_id}/data-type/{data_type_id}/compute-column/async | Compute Column Values Async
[**compute_column_values_project_project_id_data_type_data_type_id_compute_column_post**](DataTypesApi.md#compute_column_values_project_project_id_data_type_data_type_id_compute_column_post) | **POST** /project/{project_id}/data-type/{data_type_id}/compute-column | Compute Column Values
[**compute_row_columns_project_project_id_data_type_data_type_id_row_row_id_compute_post**](DataTypesApi.md#compute_row_columns_project_project_id_data_type_data_type_id_row_row_id_compute_post) | **POST** /project/{project_id}/data-type/{data_type_id}/row/{row_id}/compute | Compute Row Columns
[**create_data_type_project_project_id_data_types_post**](DataTypesApi.md#create_data_type_project_project_id_data_types_post) | **POST** /project/{project_id}/data-types | Create Data Type
[**create_data_type_view_project_project_id_data_type_data_type_id_view_post**](DataTypesApi.md#create_data_type_view_project_project_id_data_type_data_type_id_view_post) | **POST** /project/{project_id}/data-type/{data_type_id}/view | Create Data Type View
[**delete_column_project_project_id_data_type_data_type_id_column_column_name_delete**](DataTypesApi.md#delete_column_project_project_id_data_type_data_type_id_column_column_name_delete) | **DELETE** /project/{project_id}/data-type/{data_type_id}/column/{column_name} | Delete Column
[**delete_data_type_by_id_project_project_id_data_types_data_type_id_delete**](DataTypesApi.md#delete_data_type_by_id_project_project_id_data_types_data_type_id_delete) | **DELETE** /project/{project_id}/data-types/{data_type_id} | Delete Data Type By Id
[**delete_data_type_row_project_project_id_data_type_data_type_id_row_row_id_delete**](DataTypesApi.md#delete_data_type_row_project_project_id_data_type_data_type_id_row_row_id_delete) | **DELETE** /project/{project_id}/data-type/{data_type_id}/row/{row_id} | Delete Data Type Row
[**export_data_type_config_project_project_id_data_type_data_type_id_export_get**](DataTypesApi.md#export_data_type_config_project_project_id_data_type_data_type_id_export_get) | **GET** /project/{project_id}/data-type/{data_type_id}/export | Export Data Type Config
[**extract_data_type_from_doc_project_project_id_extract_data_type_post**](DataTypesApi.md#extract_data_type_from_doc_project_project_id_extract_data_type_post) | **POST** /project/{project_id}/extract/data-type | Extract Data Type From Doc
[**get_available_records_for_linking_project_project_id_data_types_data_type_id_available_for_linking_get**](DataTypesApi.md#get_available_records_for_linking_project_project_id_data_types_data_type_id_available_for_linking_get) | **GET** /project/{project_id}/data-types/{data_type_id}/available-for-linking | Get Available Records For Linking
[**get_child_records_project_project_id_data_types_data_type_id_children_get**](DataTypesApi.md#get_child_records_project_project_id_data_types_data_type_id_children_get) | **GET** /project/{project_id}/data-types/{data_type_id}/children | Get Child Records
[**get_compute_column_jobs_project_project_id_data_type_data_type_id_compute_column_jobs_get**](DataTypesApi.md#get_compute_column_jobs_project_project_id_data_type_data_type_id_compute_column_jobs_get) | **GET** /project/{project_id}/data-type/{data_type_id}/compute-column/jobs | Get Compute Column Jobs
[**get_compute_column_status_project_project_id_data_type_data_type_id_compute_column_status_execution_id_get**](DataTypesApi.md#get_compute_column_status_project_project_id_data_type_data_type_id_compute_column_status_execution_id_get) | **GET** /project/{project_id}/data-type/{data_type_id}/compute-column/status/{execution_id} | Get Compute Column Status
[**get_dashboard_data_project_project_id_data_type_data_type_id_dashboard_data_post**](DataTypesApi.md#get_dashboard_data_project_project_id_data_type_data_type_id_dashboard_data_post) | **POST** /project/{project_id}/data-type/{data_type_id}/dashboard-data | Get Dashboard Data
[**get_data_type_by_id_project_project_id_data_types_data_type_id_get**](DataTypesApi.md#get_data_type_by_id_project_project_id_data_types_data_type_id_get) | **GET** /project/{project_id}/data-types/{data_type_id} | Get Data Type By Id
[**get_data_type_json_project_project_id_data_types_data_type_id_json_get**](DataTypesApi.md#get_data_type_json_project_project_id_data_types_data_type_id_json_get) | **GET** /project/{project_id}/data-types/{data_type_id}/json | Get Data Type Json
[**get_data_type_view_by_id_project_project_id_data_types_data_type_id_view_get**](DataTypesApi.md#get_data_type_view_by_id_project_project_id_data_types_data_type_id_view_get) | **GET** /project/{project_id}/data-types/{data_type_id}/view | Get Data Type View By Id
[**get_data_types_project_project_id_data_types_get**](DataTypesApi.md#get_data_types_project_project_id_data_types_get) | **GET** /project/{project_id}/data-types | Get Data Types
[**get_extraction_settings_project_project_id_data_types_data_type_id_extraction_settings_get**](DataTypesApi.md#get_extraction_settings_project_project_id_data_types_data_type_id_extraction_settings_get) | **GET** /project/{project_id}/data-types/{data_type_id}/extraction-settings | Get Extraction Settings
[**get_sql_user_info_project_project_id_sql_user_info_get**](DataTypesApi.md#get_sql_user_info_project_project_id_sql_user_info_get) | **GET** /project/{project_id}/sql-user-info | Get Sql User Info
[**get_template_details_project_project_id_data_type_templates_template_name_get**](DataTypesApi.md#get_template_details_project_project_id_data_type_templates_template_name_get) | **GET** /project/{project_id}/data-type-templates/{template_name} | Get Template Details
[**get_templates_project_project_id_data_type_templates_get**](DataTypesApi.md#get_templates_project_project_id_data_type_templates_get) | **GET** /project/{project_id}/data-type-templates | Get Templates
[**import_table_project_project_id_import_table_post**](DataTypesApi.md#import_table_project_project_id_import_table_post) | **POST** /project/{project_id}/import-table | Import Table
[**rename_data_type_project_project_id_data_type_data_type_id_rename_put**](DataTypesApi.md#rename_data_type_project_project_id_data_type_data_type_id_rename_put) | **PUT** /project/{project_id}/data-type/{data_type_id}/rename | Rename Data Type
[**run_extraction_endpoint_project_project_id_data_types_data_type_id_extraction_test_post**](DataTypesApi.md#run_extraction_endpoint_project_project_id_data_types_data_type_id_extraction_test_post) | **POST** /project/{project_id}/data-types/{data_type_id}/extraction-test | Run Extraction Endpoint
[**run_extraction_validation_project_project_id_data_types_data_type_id_extraction_validation_post**](DataTypesApi.md#run_extraction_validation_project_project_id_data_types_data_type_id_extraction_validation_post) | **POST** /project/{project_id}/data-types/{data_type_id}/extraction-validation | Run Extraction Validation
[**save_extraction_settings_project_project_id_data_types_data_type_id_extraction_settings_post**](DataTypesApi.md#save_extraction_settings_project_project_id_data_types_data_type_id_extraction_settings_post) | **POST** /project/{project_id}/data-types/{data_type_id}/extraction-settings | Save Extraction Settings
[**update_column_metadata_project_project_id_data_type_data_type_id_column_column_name_metadata_put**](DataTypesApi.md#update_column_metadata_project_project_id_data_type_data_type_id_column_column_name_metadata_put) | **PUT** /project/{project_id}/data-type/{data_type_id}/column/{column_name}/metadata | Update Column Metadata
[**update_column_value_project_project_id_data_type_data_type_id_row_row_id_column_put**](DataTypesApi.md#update_column_value_project_project_id_data_type_data_type_id_row_row_id_column_put) | **PUT** /project/{project_id}/data-type/{data_type_id}/row/{row_id}/column | Update Column Value
[**update_data_type_view_project_project_id_data_type_data_type_id_view_view_id_put**](DataTypesApi.md#update_data_type_view_project_project_id_data_type_data_type_id_view_view_id_put) | **PUT** /project/{project_id}/data-type/{data_type_id}/view/{view_id} | Update Data Type View
[**update_record_links_project_project_id_data_type_data_type_id_row_row_id_links_put**](DataTypesApi.md#update_record_links_project_project_id_data_type_data_type_id_row_row_id_links_put) | **PUT** /project/{project_id}/data-type/{data_type_id}/row/{row_id}/links | Update Record Links
[**update_row_order_endpoint_project_project_id_data_type_data_type_id_row_order_put**](DataTypesApi.md#update_row_order_endpoint_project_project_id_data_type_data_type_id_row_order_put) | **PUT** /project/{project_id}/data-type/{data_type_id}/row-order | Update Row Order Endpoint
[**use_template_project_project_id_data_type_templates_use_post**](DataTypesApi.md#use_template_project_project_id_data_type_templates_use_post) | **POST** /project/{project_id}/data-type-templates/use | Use Template


# **activate_data_type_for_project_project_project_id_data_types_data_type_id_activate_put**
> ActivateDataTypesResponse activate_data_type_for_project_project_project_id_data_types_data_type_id_activate_put(project_id, data_type_id, activate_data_types_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Activate Data Type For Project

Activate a Data Type

### Example


```python
import odin_sdk
from odin_sdk.models.activate_data_types_request import ActivateDataTypesRequest
from odin_sdk.models.activate_data_types_response import ActivateDataTypesResponse
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
    activate_data_types_request = odin_sdk.ActivateDataTypesRequest() # ActivateDataTypesRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Activate Data Type For Project
        api_response = api_instance.activate_data_type_for_project_project_project_id_data_types_data_type_id_activate_put(project_id, data_type_id, activate_data_types_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DataTypesApi->activate_data_type_for_project_project_project_id_data_types_data_type_id_activate_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTypesApi->activate_data_type_for_project_project_project_id_data_types_data_type_id_activate_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **data_type_id** | **str**|  | 
 **activate_data_types_request** | [**ActivateDataTypesRequest**](ActivateDataTypesRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**ActivateDataTypesResponse**](ActivateDataTypesResponse.md)

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

# **add_column_project_project_id_data_type_data_type_id_column_post**
> AddColumnResponse add_column_project_project_id_data_type_data_type_id_column_post(project_id, data_type_id, add_column_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Add Column

Add a new column to a data type table

### Example


```python
import odin_sdk
from odin_sdk.models.add_column_request import AddColumnRequest
from odin_sdk.models.add_column_response import AddColumnResponse
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
    add_column_request = odin_sdk.AddColumnRequest() # AddColumnRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Add Column
        api_response = api_instance.add_column_project_project_id_data_type_data_type_id_column_post(project_id, data_type_id, add_column_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DataTypesApi->add_column_project_project_id_data_type_data_type_id_column_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTypesApi->add_column_project_project_id_data_type_data_type_id_column_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **data_type_id** | **str**|  | 
 **add_column_request** | [**AddColumnRequest**](AddColumnRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**AddColumnResponse**](AddColumnResponse.md)

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

# **add_data_type_row_project_project_id_data_type_data_type_id_row_post**
> AddDataTypeRowResponse add_data_type_row_project_project_id_data_type_data_type_id_row_post(project_id, data_type_id, add_data_type_row_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Add Data Type Row

Add a new row to a data type table

### Example


```python
import odin_sdk
from odin_sdk.models.add_data_type_row_request import AddDataTypeRowRequest
from odin_sdk.models.add_data_type_row_response import AddDataTypeRowResponse
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
    add_data_type_row_request = odin_sdk.AddDataTypeRowRequest() # AddDataTypeRowRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Add Data Type Row
        api_response = api_instance.add_data_type_row_project_project_id_data_type_data_type_id_row_post(project_id, data_type_id, add_data_type_row_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DataTypesApi->add_data_type_row_project_project_id_data_type_data_type_id_row_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTypesApi->add_data_type_row_project_project_id_data_type_data_type_id_row_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **data_type_id** | **str**|  | 
 **add_data_type_row_request** | [**AddDataTypeRowRequest**](AddDataTypeRowRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**AddDataTypeRowResponse**](AddDataTypeRowResponse.md)

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

# **add_multiple_columns_project_project_id_data_type_data_type_id_columns_post**
> AddMultipleColumnsResponse add_multiple_columns_project_project_id_data_type_data_type_id_columns_post(project_id, data_type_id, add_multiple_columns_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Add Multiple Columns

Add multiple new columns to a data type table

### Example


```python
import odin_sdk
from odin_sdk.models.add_multiple_columns_request import AddMultipleColumnsRequest
from odin_sdk.models.add_multiple_columns_response import AddMultipleColumnsResponse
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
    add_multiple_columns_request = odin_sdk.AddMultipleColumnsRequest() # AddMultipleColumnsRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Add Multiple Columns
        api_response = api_instance.add_multiple_columns_project_project_id_data_type_data_type_id_columns_post(project_id, data_type_id, add_multiple_columns_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DataTypesApi->add_multiple_columns_project_project_id_data_type_data_type_id_columns_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTypesApi->add_multiple_columns_project_project_id_data_type_data_type_id_columns_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **data_type_id** | **str**|  | 
 **add_multiple_columns_request** | [**AddMultipleColumnsRequest**](AddMultipleColumnsRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**AddMultipleColumnsResponse**](AddMultipleColumnsResponse.md)

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

# **add_multiple_data_type_rows_project_project_id_data_type_data_type_id_rows_post**
> AddMultipleDataTypeRowsResponse add_multiple_data_type_rows_project_project_id_data_type_data_type_id_rows_post(project_id, data_type_id, add_multiple_data_type_rows_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Add Multiple Data Type Rows

Add multiple rows to a data type table

### Example


```python
import odin_sdk
from odin_sdk.models.add_multiple_data_type_rows_request import AddMultipleDataTypeRowsRequest
from odin_sdk.models.add_multiple_data_type_rows_response import AddMultipleDataTypeRowsResponse
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
    add_multiple_data_type_rows_request = odin_sdk.AddMultipleDataTypeRowsRequest() # AddMultipleDataTypeRowsRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Add Multiple Data Type Rows
        api_response = api_instance.add_multiple_data_type_rows_project_project_id_data_type_data_type_id_rows_post(project_id, data_type_id, add_multiple_data_type_rows_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DataTypesApi->add_multiple_data_type_rows_project_project_id_data_type_data_type_id_rows_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTypesApi->add_multiple_data_type_rows_project_project_id_data_type_data_type_id_rows_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **data_type_id** | **str**|  | 
 **add_multiple_data_type_rows_request** | [**AddMultipleDataTypeRowsRequest**](AddMultipleDataTypeRowsRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**AddMultipleDataTypeRowsResponse**](AddMultipleDataTypeRowsResponse.md)

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

# **compute_all_rows_project_project_id_data_type_data_type_id_compute_all_rows_post**
> ComputeAllRowsResponse compute_all_rows_project_project_id_data_type_data_type_id_compute_all_rows_post(project_id, data_type_id, bypass_celery=bypass_celery, x_api_key=x_api_key, x_api_secret=x_api_secret)

Compute All Rows

Compute values for all rows in a data type table using LLM

### Example


```python
import odin_sdk
from odin_sdk.models.compute_all_rows_response import ComputeAllRowsResponse
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
    bypass_celery = False # bool |  (optional) (default to False)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Compute All Rows
        api_response = api_instance.compute_all_rows_project_project_id_data_type_data_type_id_compute_all_rows_post(project_id, data_type_id, bypass_celery=bypass_celery, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DataTypesApi->compute_all_rows_project_project_id_data_type_data_type_id_compute_all_rows_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTypesApi->compute_all_rows_project_project_id_data_type_data_type_id_compute_all_rows_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **data_type_id** | **str**|  | 
 **bypass_celery** | **bool**|  | [optional] [default to False]
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**ComputeAllRowsResponse**](ComputeAllRowsResponse.md)

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

# **compute_column_values_project_project_id_data_type_data_type_id_compute_column_post**
> ComputeColumnResponse compute_column_values_project_project_id_data_type_data_type_id_compute_column_post(project_id, data_type_id, compute_column_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Compute Column Values

Compute values for a column using LLM if configured

### Example


```python
import odin_sdk
from odin_sdk.models.compute_column_request import ComputeColumnRequest
from odin_sdk.models.compute_column_response import ComputeColumnResponse
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
        # Compute Column Values
        api_response = api_instance.compute_column_values_project_project_id_data_type_data_type_id_compute_column_post(project_id, data_type_id, compute_column_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DataTypesApi->compute_column_values_project_project_id_data_type_data_type_id_compute_column_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTypesApi->compute_column_values_project_project_id_data_type_data_type_id_compute_column_post: %s\n" % e)
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

[**ComputeColumnResponse**](ComputeColumnResponse.md)

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

# **compute_row_columns_project_project_id_data_type_data_type_id_row_row_id_compute_post**
> ComputeRowColumnsResponse compute_row_columns_project_project_id_data_type_data_type_id_row_row_id_compute_post(project_id, data_type_id, row_id, compute_row_columns_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Compute Row Columns

Compute values for one or more columns in a specific row using LLM

### Example


```python
import odin_sdk
from odin_sdk.models.compute_row_columns_request import ComputeRowColumnsRequest
from odin_sdk.models.compute_row_columns_response import ComputeRowColumnsResponse
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
    row_id = 'row_id_example' # str | 
    compute_row_columns_request = odin_sdk.ComputeRowColumnsRequest() # ComputeRowColumnsRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Compute Row Columns
        api_response = api_instance.compute_row_columns_project_project_id_data_type_data_type_id_row_row_id_compute_post(project_id, data_type_id, row_id, compute_row_columns_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DataTypesApi->compute_row_columns_project_project_id_data_type_data_type_id_row_row_id_compute_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTypesApi->compute_row_columns_project_project_id_data_type_data_type_id_row_row_id_compute_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **data_type_id** | **str**|  | 
 **row_id** | **str**|  | 
 **compute_row_columns_request** | [**ComputeRowColumnsRequest**](ComputeRowColumnsRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**ComputeRowColumnsResponse**](ComputeRowColumnsResponse.md)

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

# **delete_column_project_project_id_data_type_data_type_id_column_column_name_delete**
> DeleteColumnResponse delete_column_project_project_id_data_type_data_type_id_column_column_name_delete(project_id, data_type_id, column_name, x_api_key=x_api_key, x_api_secret=x_api_secret)

Delete Column

Delete a column from a data type table

### Example


```python
import odin_sdk
from odin_sdk.models.delete_column_response import DeleteColumnResponse
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
    column_name = 'column_name_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Delete Column
        api_response = api_instance.delete_column_project_project_id_data_type_data_type_id_column_column_name_delete(project_id, data_type_id, column_name, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DataTypesApi->delete_column_project_project_id_data_type_data_type_id_column_column_name_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTypesApi->delete_column_project_project_id_data_type_data_type_id_column_column_name_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **data_type_id** | **str**|  | 
 **column_name** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**DeleteColumnResponse**](DeleteColumnResponse.md)

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

# **delete_data_type_row_project_project_id_data_type_data_type_id_row_row_id_delete**
> DeleteDataTypeResponse delete_data_type_row_project_project_id_data_type_data_type_id_row_row_id_delete(project_id, data_type_id, row_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Delete Data Type Row

Delete a row from a data type table

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
    row_id = 'row_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Delete Data Type Row
        api_response = api_instance.delete_data_type_row_project_project_id_data_type_data_type_id_row_row_id_delete(project_id, data_type_id, row_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DataTypesApi->delete_data_type_row_project_project_id_data_type_data_type_id_row_row_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTypesApi->delete_data_type_row_project_project_id_data_type_data_type_id_row_row_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **data_type_id** | **str**|  | 
 **row_id** | **str**|  | 
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

# **export_data_type_config_project_project_id_data_type_data_type_id_export_get**
> ExportDataTypeResponse export_data_type_config_project_project_id_data_type_data_type_id_export_get(project_id, data_type_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Export Data Type Config

Export a data type configuration for import elsewhere

### Example


```python
import odin_sdk
from odin_sdk.models.export_data_type_response import ExportDataTypeResponse
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
        # Export Data Type Config
        api_response = api_instance.export_data_type_config_project_project_id_data_type_data_type_id_export_get(project_id, data_type_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DataTypesApi->export_data_type_config_project_project_id_data_type_data_type_id_export_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTypesApi->export_data_type_config_project_project_id_data_type_data_type_id_export_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **data_type_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**ExportDataTypeResponse**](ExportDataTypeResponse.md)

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

# **extract_data_type_from_doc_project_project_id_extract_data_type_post**
> ExtractDataTypeResponse extract_data_type_from_doc_project_project_id_extract_data_type_post(project_id, extract_data_type_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Extract Data Type From Doc

Extract the data types from content

### Example


```python
import odin_sdk
from odin_sdk.models.extract_data_type_request import ExtractDataTypeRequest
from odin_sdk.models.extract_data_type_response import ExtractDataTypeResponse
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
    extract_data_type_request = odin_sdk.ExtractDataTypeRequest() # ExtractDataTypeRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Extract Data Type From Doc
        api_response = api_instance.extract_data_type_from_doc_project_project_id_extract_data_type_post(project_id, extract_data_type_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DataTypesApi->extract_data_type_from_doc_project_project_id_extract_data_type_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTypesApi->extract_data_type_from_doc_project_project_id_extract_data_type_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **extract_data_type_request** | [**ExtractDataTypeRequest**](ExtractDataTypeRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**ExtractDataTypeResponse**](ExtractDataTypeResponse.md)

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

# **get_available_records_for_linking_project_project_id_data_types_data_type_id_available_for_linking_get**
> GetAvailableRecordsResponse get_available_records_for_linking_project_project_id_data_types_data_type_id_available_for_linking_get(project_id, data_type_id, parent_data_type_id, parent_record_id, field_name, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Available Records For Linking

Fetch all records available for linking to a parent record

### Example


```python
import odin_sdk
from odin_sdk.models.get_available_records_response import GetAvailableRecordsResponse
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
    data_type_id = 'data_type_id_example' # str | ID of the target data type
    parent_data_type_id = 'parent_data_type_id_example' # str | ID of the parent data type
    parent_record_id = 56 # int | ID of the parent record
    field_name = 'field_name_example' # str | Name of the collection field in the parent table
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Available Records For Linking
        api_response = api_instance.get_available_records_for_linking_project_project_id_data_types_data_type_id_available_for_linking_get(project_id, data_type_id, parent_data_type_id, parent_record_id, field_name, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DataTypesApi->get_available_records_for_linking_project_project_id_data_types_data_type_id_available_for_linking_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTypesApi->get_available_records_for_linking_project_project_id_data_types_data_type_id_available_for_linking_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **data_type_id** | **str**| ID of the target data type | 
 **parent_data_type_id** | **str**| ID of the parent data type | 
 **parent_record_id** | **int**| ID of the parent record | 
 **field_name** | **str**| Name of the collection field in the parent table | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**GetAvailableRecordsResponse**](GetAvailableRecordsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Data type or parent record not found. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_child_records_project_project_id_data_types_data_type_id_children_get**
> GetChildRecordsResponse get_child_records_project_project_id_data_types_data_type_id_children_get(project_id, data_type_id, parent_data_type_id, parent_record_id, field_name, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Child Records

Fetch all child records related to a parent record through a foreign key relationship

### Example


```python
import odin_sdk
from odin_sdk.models.get_child_records_response import GetChildRecordsResponse
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
    data_type_id = 'data_type_id_example' # str | ID of the child data type
    parent_data_type_id = 'parent_data_type_id_example' # str | ID of the parent data type
    parent_record_id = 56 # int | ID of the parent record
    field_name = 'field_name_example' # str | Name of the collection field in the parent table
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Child Records
        api_response = api_instance.get_child_records_project_project_id_data_types_data_type_id_children_get(project_id, data_type_id, parent_data_type_id, parent_record_id, field_name, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DataTypesApi->get_child_records_project_project_id_data_types_data_type_id_children_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTypesApi->get_child_records_project_project_id_data_types_data_type_id_children_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **data_type_id** | **str**| ID of the child data type | 
 **parent_data_type_id** | **str**| ID of the parent data type | 
 **parent_record_id** | **int**| ID of the parent record | 
 **field_name** | **str**| Name of the collection field in the parent table | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**GetChildRecordsResponse**](GetChildRecordsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Data type or parent record not found. |  -  |
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

# **get_dashboard_data_project_project_id_data_type_data_type_id_dashboard_data_post**
> GetDashboardDataResponse get_dashboard_data_project_project_id_data_type_data_type_id_dashboard_data_post(project_id, data_type_id, get_dashboard_data_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Dashboard Data

Get aggregated dashboard data for a data type

### Example


```python
import odin_sdk
from odin_sdk.models.get_dashboard_data_request import GetDashboardDataRequest
from odin_sdk.models.get_dashboard_data_response import GetDashboardDataResponse
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
    get_dashboard_data_request = odin_sdk.GetDashboardDataRequest() # GetDashboardDataRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Dashboard Data
        api_response = api_instance.get_dashboard_data_project_project_id_data_type_data_type_id_dashboard_data_post(project_id, data_type_id, get_dashboard_data_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DataTypesApi->get_dashboard_data_project_project_id_data_type_data_type_id_dashboard_data_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTypesApi->get_dashboard_data_project_project_id_data_type_data_type_id_dashboard_data_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **data_type_id** | **str**|  | 
 **get_dashboard_data_request** | [**GetDashboardDataRequest**](GetDashboardDataRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**GetDashboardDataResponse**](GetDashboardDataResponse.md)

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

# **get_data_type_json_project_project_id_data_types_data_type_id_json_get**
> GetDataTypeJsonResponse get_data_type_json_project_project_id_data_types_data_type_id_json_get(project_id, data_type_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Data Type Json

Get the JSON version of a data type table

### Example


```python
import odin_sdk
from odin_sdk.models.get_data_type_json_response import GetDataTypeJsonResponse
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
        # Get Data Type Json
        api_response = api_instance.get_data_type_json_project_project_id_data_types_data_type_id_json_get(project_id, data_type_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DataTypesApi->get_data_type_json_project_project_id_data_types_data_type_id_json_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTypesApi->get_data_type_json_project_project_id_data_types_data_type_id_json_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **data_type_id** | **str**| ID of the data type | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**GetDataTypeJsonResponse**](GetDataTypeJsonResponse.md)

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

# **get_extraction_settings_project_project_id_data_types_data_type_id_extraction_settings_get**
> ExtractionSettingsResponse get_extraction_settings_project_project_id_data_types_data_type_id_extraction_settings_get(project_id, data_type_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Extraction Settings

Get extraction settings for a data type

### Example


```python
import odin_sdk
from odin_sdk.models.extraction_settings_response import ExtractionSettingsResponse
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
        # Get Extraction Settings
        api_response = api_instance.get_extraction_settings_project_project_id_data_types_data_type_id_extraction_settings_get(project_id, data_type_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DataTypesApi->get_extraction_settings_project_project_id_data_types_data_type_id_extraction_settings_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTypesApi->get_extraction_settings_project_project_id_data_types_data_type_id_extraction_settings_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **data_type_id** | **str**| ID of the data type | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**ExtractionSettingsResponse**](ExtractionSettingsResponse.md)

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

# **get_sql_user_info_project_project_id_sql_user_info_get**
> GetSQLUserInfoResponse get_sql_user_info_project_project_id_sql_user_info_get(project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Sql User Info

Get SQL user information for a project

### Example


```python
import odin_sdk
from odin_sdk.models.get_sql_user_info_response import GetSQLUserInfoResponse
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
        # Get Sql User Info
        api_response = api_instance.get_sql_user_info_project_project_id_sql_user_info_get(project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DataTypesApi->get_sql_user_info_project_project_id_sql_user_info_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTypesApi->get_sql_user_info_project_project_id_sql_user_info_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**GetSQLUserInfoResponse**](GetSQLUserInfoResponse.md)

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

# **rename_data_type_project_project_id_data_type_data_type_id_rename_put**
> RenameDataTypeResponse rename_data_type_project_project_id_data_type_data_type_id_rename_put(project_id, data_type_id, rename_data_type_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Rename Data Type

Rename a data type

### Example


```python
import odin_sdk
from odin_sdk.models.rename_data_type_request import RenameDataTypeRequest
from odin_sdk.models.rename_data_type_response import RenameDataTypeResponse
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
    rename_data_type_request = odin_sdk.RenameDataTypeRequest() # RenameDataTypeRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Rename Data Type
        api_response = api_instance.rename_data_type_project_project_id_data_type_data_type_id_rename_put(project_id, data_type_id, rename_data_type_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DataTypesApi->rename_data_type_project_project_id_data_type_data_type_id_rename_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTypesApi->rename_data_type_project_project_id_data_type_data_type_id_rename_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **data_type_id** | **str**|  | 
 **rename_data_type_request** | [**RenameDataTypeRequest**](RenameDataTypeRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**RenameDataTypeResponse**](RenameDataTypeResponse.md)

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

# **run_extraction_endpoint_project_project_id_data_types_data_type_id_extraction_test_post**
> RunExtractionTestResponse run_extraction_endpoint_project_project_id_data_types_data_type_id_extraction_test_post(project_id, data_type_id, run_extraction_test_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Run Extraction Endpoint

Run an extraction test on a sample document using custom extraction configuration

### Example


```python
import odin_sdk
from odin_sdk.models.run_extraction_test_request import RunExtractionTestRequest
from odin_sdk.models.run_extraction_test_response import RunExtractionTestResponse
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
    run_extraction_test_request = odin_sdk.RunExtractionTestRequest() # RunExtractionTestRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Run Extraction Endpoint
        api_response = api_instance.run_extraction_endpoint_project_project_id_data_types_data_type_id_extraction_test_post(project_id, data_type_id, run_extraction_test_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DataTypesApi->run_extraction_endpoint_project_project_id_data_types_data_type_id_extraction_test_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTypesApi->run_extraction_endpoint_project_project_id_data_types_data_type_id_extraction_test_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **data_type_id** | **str**| ID of the data type | 
 **run_extraction_test_request** | [**RunExtractionTestRequest**](RunExtractionTestRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**RunExtractionTestResponse**](RunExtractionTestResponse.md)

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

# **run_extraction_validation_project_project_id_data_types_data_type_id_extraction_validation_post**
> ValidationResultResponse run_extraction_validation_project_project_id_data_types_data_type_id_extraction_validation_post(project_id, data_type_id, run_extraction_test_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Run Extraction Validation

Run extraction validation against data type schema

### Example


```python
import odin_sdk
from odin_sdk.models.run_extraction_test_request import RunExtractionTestRequest
from odin_sdk.models.validation_result_response import ValidationResultResponse
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
    run_extraction_test_request = odin_sdk.RunExtractionTestRequest() # RunExtractionTestRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Run Extraction Validation
        api_response = api_instance.run_extraction_validation_project_project_id_data_types_data_type_id_extraction_validation_post(project_id, data_type_id, run_extraction_test_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DataTypesApi->run_extraction_validation_project_project_id_data_types_data_type_id_extraction_validation_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTypesApi->run_extraction_validation_project_project_id_data_types_data_type_id_extraction_validation_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **data_type_id** | **str**| ID of the data type | 
 **run_extraction_test_request** | [**RunExtractionTestRequest**](RunExtractionTestRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**ValidationResultResponse**](ValidationResultResponse.md)

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

# **save_extraction_settings_project_project_id_data_types_data_type_id_extraction_settings_post**
> ExtractionSettingsResponse save_extraction_settings_project_project_id_data_types_data_type_id_extraction_settings_post(project_id, data_type_id, save_extraction_settings_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Save Extraction Settings

Save extraction settings for a data type

### Example


```python
import odin_sdk
from odin_sdk.models.extraction_settings_response import ExtractionSettingsResponse
from odin_sdk.models.save_extraction_settings_request import SaveExtractionSettingsRequest
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
    save_extraction_settings_request = odin_sdk.SaveExtractionSettingsRequest() # SaveExtractionSettingsRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Save Extraction Settings
        api_response = api_instance.save_extraction_settings_project_project_id_data_types_data_type_id_extraction_settings_post(project_id, data_type_id, save_extraction_settings_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DataTypesApi->save_extraction_settings_project_project_id_data_types_data_type_id_extraction_settings_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTypesApi->save_extraction_settings_project_project_id_data_types_data_type_id_extraction_settings_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **data_type_id** | **str**| ID of the data type | 
 **save_extraction_settings_request** | [**SaveExtractionSettingsRequest**](SaveExtractionSettingsRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**ExtractionSettingsResponse**](ExtractionSettingsResponse.md)

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

# **update_column_metadata_project_project_id_data_type_data_type_id_column_column_name_metadata_put**
> UpdateColumnMetadataResponse update_column_metadata_project_project_id_data_type_data_type_id_column_column_name_metadata_put(project_id, data_type_id, column_name, update_column_metadata_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Update Column Metadata

Update a column's metadata in a data type table

### Example


```python
import odin_sdk
from odin_sdk.models.update_column_metadata_request import UpdateColumnMetadataRequest
from odin_sdk.models.update_column_metadata_response import UpdateColumnMetadataResponse
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
    column_name = 'column_name_example' # str | 
    update_column_metadata_request = odin_sdk.UpdateColumnMetadataRequest() # UpdateColumnMetadataRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Update Column Metadata
        api_response = api_instance.update_column_metadata_project_project_id_data_type_data_type_id_column_column_name_metadata_put(project_id, data_type_id, column_name, update_column_metadata_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DataTypesApi->update_column_metadata_project_project_id_data_type_data_type_id_column_column_name_metadata_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTypesApi->update_column_metadata_project_project_id_data_type_data_type_id_column_column_name_metadata_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **data_type_id** | **str**|  | 
 **column_name** | **str**|  | 
 **update_column_metadata_request** | [**UpdateColumnMetadataRequest**](UpdateColumnMetadataRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**UpdateColumnMetadataResponse**](UpdateColumnMetadataResponse.md)

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

# **update_column_value_project_project_id_data_type_data_type_id_row_row_id_column_put**
> UpdateColumnValueResponse update_column_value_project_project_id_data_type_data_type_id_row_row_id_column_put(project_id, data_type_id, row_id, update_column_value_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Update Column Value

Update a column value in a data type table row

### Example


```python
import odin_sdk
from odin_sdk.models.update_column_value_request import UpdateColumnValueRequest
from odin_sdk.models.update_column_value_response import UpdateColumnValueResponse
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
    row_id = 'row_id_example' # str | 
    update_column_value_request = odin_sdk.UpdateColumnValueRequest() # UpdateColumnValueRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Update Column Value
        api_response = api_instance.update_column_value_project_project_id_data_type_data_type_id_row_row_id_column_put(project_id, data_type_id, row_id, update_column_value_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DataTypesApi->update_column_value_project_project_id_data_type_data_type_id_row_row_id_column_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTypesApi->update_column_value_project_project_id_data_type_data_type_id_row_row_id_column_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **data_type_id** | **str**|  | 
 **row_id** | **str**|  | 
 **update_column_value_request** | [**UpdateColumnValueRequest**](UpdateColumnValueRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**UpdateColumnValueResponse**](UpdateColumnValueResponse.md)

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

# **update_record_links_project_project_id_data_type_data_type_id_row_row_id_links_put**
> UpdateRecordLinksResponse update_record_links_project_project_id_data_type_data_type_id_row_row_id_links_put(project_id, data_type_id, row_id, update_record_links_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Update Record Links

Update links between a record and target records

### Example


```python
import odin_sdk
from odin_sdk.models.update_record_links_request import UpdateRecordLinksRequest
from odin_sdk.models.update_record_links_response import UpdateRecordLinksResponse
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
    row_id = 'row_id_example' # str | 
    update_record_links_request = odin_sdk.UpdateRecordLinksRequest() # UpdateRecordLinksRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Update Record Links
        api_response = api_instance.update_record_links_project_project_id_data_type_data_type_id_row_row_id_links_put(project_id, data_type_id, row_id, update_record_links_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DataTypesApi->update_record_links_project_project_id_data_type_data_type_id_row_row_id_links_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTypesApi->update_record_links_project_project_id_data_type_data_type_id_row_row_id_links_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **data_type_id** | **str**|  | 
 **row_id** | **str**|  | 
 **update_record_links_request** | [**UpdateRecordLinksRequest**](UpdateRecordLinksRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**UpdateRecordLinksResponse**](UpdateRecordLinksResponse.md)

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

# **update_row_order_endpoint_project_project_id_data_type_data_type_id_row_order_put**
> UpdateRowOrderResponse update_row_order_endpoint_project_project_id_data_type_data_type_id_row_order_put(project_id, data_type_id, update_row_order_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Update Row Order Endpoint

Update the order of a row in a data type table

### Example


```python
import odin_sdk
from odin_sdk.models.update_row_order_request import UpdateRowOrderRequest
from odin_sdk.models.update_row_order_response import UpdateRowOrderResponse
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
    update_row_order_request = odin_sdk.UpdateRowOrderRequest() # UpdateRowOrderRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Update Row Order Endpoint
        api_response = api_instance.update_row_order_endpoint_project_project_id_data_type_data_type_id_row_order_put(project_id, data_type_id, update_row_order_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DataTypesApi->update_row_order_endpoint_project_project_id_data_type_data_type_id_row_order_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataTypesApi->update_row_order_endpoint_project_project_id_data_type_data_type_id_row_order_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **data_type_id** | **str**|  | 
 **update_row_order_request** | [**UpdateRowOrderRequest**](UpdateRowOrderRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**UpdateRowOrderResponse**](UpdateRowOrderResponse.md)

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

