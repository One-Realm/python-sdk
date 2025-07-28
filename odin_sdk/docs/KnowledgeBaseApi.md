# odin_sdk.KnowledgeBaseApi

All URIs are relative to *http://127.0.0.1:8001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_file_to_knowledge_base_v3_v3_project_knowledge_add_file_post**](KnowledgeBaseApi.md#add_file_to_knowledge_base_v3_v3_project_knowledge_add_file_post) | **POST** /v3/project/knowledge/add/file | Add File To Knowledge Base V3
[**batch_delete_project_knowledge_delete_delete**](KnowledgeBaseApi.md#batch_delete_project_knowledge_delete_delete) | **DELETE** /project/knowledge/delete | Batch Delete


# **add_file_to_knowledge_base_v3_v3_project_knowledge_add_file_post**
> RoutesKnowledgebaseKnowledgeBaseDataResponse add_file_to_knowledge_base_v3_v3_project_knowledge_add_file_post(file, project_id, metadata, x_api_key=x_api_key, x_api_secret=x_api_secret, file_type=file_type, force=force, resource_type_id=resource_type_id, is_quick_upload=is_quick_upload, data_type_id=data_type_id, upload_signifier=upload_signifier, csv_delimiter=csv_delimiter, path=path)

Add File To Knowledge Base V3

Add files to the Knowledge Base with metadata extraction.

### Example


```python
import odin_sdk
from odin_sdk.models.routes_knowledgebase_knowledge_base_data_response import RoutesKnowledgebaseKnowledgeBaseDataResponse
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
    api_instance = odin_sdk.KnowledgeBaseApi(api_client)
    file = None # bytearray | 
    project_id = 'project_id_example' # str | 
    metadata = None # object | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)
    file_type = 'file_type_example' # str |  (optional)
    force = True # bool |  (optional)
    resource_type_id = 'resource_type_id_example' # str |  (optional)
    is_quick_upload = True # bool |  (optional)
    data_type_id = 'data_type_id_example' # str |  (optional)
    upload_signifier = 'upload_signifier_example' # str |  (optional)
    csv_delimiter = 'csv_delimiter_example' # str |  (optional)
    path = 'path_example' # str |  (optional)

    try:
        # Add File To Knowledge Base V3
        api_response = api_instance.add_file_to_knowledge_base_v3_v3_project_knowledge_add_file_post(file, project_id, metadata, x_api_key=x_api_key, x_api_secret=x_api_secret, file_type=file_type, force=force, resource_type_id=resource_type_id, is_quick_upload=is_quick_upload, data_type_id=data_type_id, upload_signifier=upload_signifier, csv_delimiter=csv_delimiter, path=path)
        print("The response of KnowledgeBaseApi->add_file_to_knowledge_base_v3_v3_project_knowledge_add_file_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBaseApi->add_file_to_knowledge_base_v3_v3_project_knowledge_add_file_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**|  | 
 **project_id** | **str**|  | 
 **metadata** | [**object**](object.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 
 **file_type** | **str**|  | [optional] 
 **force** | **bool**|  | [optional] 
 **resource_type_id** | **str**|  | [optional] 
 **is_quick_upload** | **bool**|  | [optional] 
 **data_type_id** | **str**|  | [optional] 
 **upload_signifier** | **str**|  | [optional] 
 **csv_delimiter** | **str**|  | [optional] 
 **path** | **str**|  | [optional] 

### Return type

[**RoutesKnowledgebaseKnowledgeBaseDataResponse**](RoutesKnowledgebaseKnowledgeBaseDataResponse.md)

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

# **batch_delete_project_knowledge_delete_delete**
> BatchDeleteResponse batch_delete_project_knowledge_delete_delete(batch_delete_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Batch Delete

Deletes the selected resources.

### Example


```python
import odin_sdk
from odin_sdk.models.batch_delete_request import BatchDeleteRequest
from odin_sdk.models.batch_delete_response import BatchDeleteResponse
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
    api_instance = odin_sdk.KnowledgeBaseApi(api_client)
    batch_delete_request = odin_sdk.BatchDeleteRequest() # BatchDeleteRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Batch Delete
        api_response = api_instance.batch_delete_project_knowledge_delete_delete(batch_delete_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of KnowledgeBaseApi->batch_delete_project_knowledge_delete_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBaseApi->batch_delete_project_knowledge_delete_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_delete_request** | [**BatchDeleteRequest**](BatchDeleteRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**BatchDeleteResponse**](BatchDeleteResponse.md)

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

