# odin_sdk.DocumentsApi

All URIs are relative to *http://127.0.0.1:8001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_document_document_create_post**](DocumentsApi.md#create_document_document_create_post) | **POST** /document/create | Create Document
[**delete_document_document_delete**](DocumentsApi.md#delete_document_document_delete) | **DELETE** /document | Delete Document
[**edit_document_document_put**](DocumentsApi.md#edit_document_document_put) | **PUT** /document | Edit Document
[**get_document_document_post**](DocumentsApi.md#get_document_document_post) | **POST** /document | Get Document
[**get_documents_documents_post**](DocumentsApi.md#get_documents_documents_post) | **POST** /documents | Get Documents
[**overwrite_document_document_replace_put**](DocumentsApi.md#overwrite_document_document_replace_put) | **PUT** /document/replace | Overwrite Document


# **create_document_document_create_post**
> CreateDocumentResponse create_document_document_create_post(create_document_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Create Document

### Example


```python
import odin_sdk
from odin_sdk.models.create_document_request import CreateDocumentRequest
from odin_sdk.models.create_document_response import CreateDocumentResponse
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
    api_instance = odin_sdk.DocumentsApi(api_client)
    create_document_request = odin_sdk.CreateDocumentRequest() # CreateDocumentRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Create Document
        api_response = api_instance.create_document_document_create_post(create_document_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DocumentsApi->create_document_document_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->create_document_document_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_document_request** | [**CreateDocumentRequest**](CreateDocumentRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**CreateDocumentResponse**](CreateDocumentResponse.md)

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

# **delete_document_document_delete**
> DeleteDocumentResponse delete_document_document_delete(delete_document_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Delete Document

### Example


```python
import odin_sdk
from odin_sdk.models.delete_document_request import DeleteDocumentRequest
from odin_sdk.models.delete_document_response import DeleteDocumentResponse
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
    api_instance = odin_sdk.DocumentsApi(api_client)
    delete_document_request = odin_sdk.DeleteDocumentRequest() # DeleteDocumentRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Delete Document
        api_response = api_instance.delete_document_document_delete(delete_document_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DocumentsApi->delete_document_document_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->delete_document_document_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_document_request** | [**DeleteDocumentRequest**](DeleteDocumentRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**DeleteDocumentResponse**](DeleteDocumentResponse.md)

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

# **edit_document_document_put**
> UpdateDocumentResponse edit_document_document_put(update_document_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Edit Document

### Example


```python
import odin_sdk
from odin_sdk.models.update_document_request import UpdateDocumentRequest
from odin_sdk.models.update_document_response import UpdateDocumentResponse
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
    api_instance = odin_sdk.DocumentsApi(api_client)
    update_document_request = odin_sdk.UpdateDocumentRequest() # UpdateDocumentRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Edit Document
        api_response = api_instance.edit_document_document_put(update_document_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DocumentsApi->edit_document_document_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->edit_document_document_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_document_request** | [**UpdateDocumentRequest**](UpdateDocumentRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**UpdateDocumentResponse**](UpdateDocumentResponse.md)

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

# **get_document_document_post**
> GetDocumentResponse get_document_document_post(get_document_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Document

### Example


```python
import odin_sdk
from odin_sdk.models.get_document_request import GetDocumentRequest
from odin_sdk.models.get_document_response import GetDocumentResponse
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
    api_instance = odin_sdk.DocumentsApi(api_client)
    get_document_request = odin_sdk.GetDocumentRequest() # GetDocumentRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Document
        api_response = api_instance.get_document_document_post(get_document_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DocumentsApi->get_document_document_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->get_document_document_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_document_request** | [**GetDocumentRequest**](GetDocumentRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**GetDocumentResponse**](GetDocumentResponse.md)

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

# **get_documents_documents_post**
> GetDocumentsResponse get_documents_documents_post(get_documents_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Documents

### Example


```python
import odin_sdk
from odin_sdk.models.get_documents_request import GetDocumentsRequest
from odin_sdk.models.get_documents_response import GetDocumentsResponse
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
    api_instance = odin_sdk.DocumentsApi(api_client)
    get_documents_request = odin_sdk.GetDocumentsRequest() # GetDocumentsRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Documents
        api_response = api_instance.get_documents_documents_post(get_documents_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DocumentsApi->get_documents_documents_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->get_documents_documents_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_documents_request** | [**GetDocumentsRequest**](GetDocumentsRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**GetDocumentsResponse**](GetDocumentsResponse.md)

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

# **overwrite_document_document_replace_put**
> UpdateDocumentResponse overwrite_document_document_replace_put(update_document_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Overwrite Document

### Example


```python
import odin_sdk
from odin_sdk.models.update_document_request import UpdateDocumentRequest
from odin_sdk.models.update_document_response import UpdateDocumentResponse
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
    api_instance = odin_sdk.DocumentsApi(api_client)
    update_document_request = odin_sdk.UpdateDocumentRequest() # UpdateDocumentRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Overwrite Document
        api_response = api_instance.overwrite_document_document_replace_put(update_document_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DocumentsApi->overwrite_document_document_replace_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->overwrite_document_document_replace_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_document_request** | [**UpdateDocumentRequest**](UpdateDocumentRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**UpdateDocumentResponse**](UpdateDocumentResponse.md)

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

