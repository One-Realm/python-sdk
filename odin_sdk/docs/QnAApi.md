# odin_sdk.QnAApi

All URIs are relative to *http://127.0.0.1:8001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_update_qna_project_project_id_bulk_update_qna_post**](QnAApi.md#bulk_update_qna_project_project_id_bulk_update_qna_post) | **POST** /project/{project_id}/bulk_update_qna | Bulk Update Qna
[**create_qa_pair_project_project_id_qna_post**](QnAApi.md#create_qa_pair_project_project_id_qna_post) | **POST** /project/{project_id}/qna | Create Qa Pair
[**delete_qna_project_project_id_qna_qna_id_delete**](QnAApi.md#delete_qna_project_project_id_qna_qna_id_delete) | **DELETE** /project/{project_id}/qna/{qna_id} | Delete Qna
[**generate_qna_project_project_id_generate_qna_post**](QnAApi.md#generate_qna_project_project_id_generate_qna_post) | **POST** /project/{project_id}/generate_qna | Generate Qna
[**get_snippet_types_snippet_types_get**](QnAApi.md#get_snippet_types_snippet_types_get) | **GET** /snippet-types | Get Snippet Types
[**list_qnas_project_project_id_qna_get**](QnAApi.md#list_qnas_project_project_id_qna_get) | **GET** /project/{project_id}/qna | List Qnas
[**retrieve_qna_project_project_id_qna_qna_id_get**](QnAApi.md#retrieve_qna_project_project_id_qna_qna_id_get) | **GET** /project/{project_id}/qna/{qna_id} | Retrieve Qna
[**update_qna_project_project_id_qna_qna_id_put**](QnAApi.md#update_qna_project_project_id_qna_qna_id_put) | **PUT** /project/{project_id}/qna/{qna_id} | Update Qna


# **bulk_update_qna_project_project_id_bulk_update_qna_post**
> TaskStatusResponse bulk_update_qna_project_project_id_bulk_update_qna_post(project_id, bulk_update_qn_a_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Bulk Update Qna

Bulk update QnA pairs for a project

### Example


```python
import odin_sdk
from odin_sdk.models.bulk_update_qn_a_request import BulkUpdateQnARequest
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
    api_instance = odin_sdk.QnAApi(api_client)
    project_id = 'project_id_example' # str | 
    bulk_update_qn_a_request = odin_sdk.BulkUpdateQnARequest() # BulkUpdateQnARequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Bulk Update Qna
        api_response = api_instance.bulk_update_qna_project_project_id_bulk_update_qna_post(project_id, bulk_update_qn_a_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of QnAApi->bulk_update_qna_project_project_id_bulk_update_qna_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QnAApi->bulk_update_qna_project_project_id_bulk_update_qna_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **bulk_update_qn_a_request** | [**BulkUpdateQnARequest**](BulkUpdateQnARequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**TaskStatusResponse**](TaskStatusResponse.md)

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

# **create_qa_pair_project_project_id_qna_post**
> DbQnAPair create_qa_pair_project_project_id_qna_post(project_id, create_qa_pair_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Create Qa Pair

Create a single QnA pair for a document

### Example


```python
import odin_sdk
from odin_sdk.models.create_qa_pair_request import CreateQAPairRequest
from odin_sdk.models.db_qn_a_pair import DbQnAPair
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
    api_instance = odin_sdk.QnAApi(api_client)
    project_id = 'project_id_example' # str | 
    create_qa_pair_request = odin_sdk.CreateQAPairRequest() # CreateQAPairRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Create Qa Pair
        api_response = api_instance.create_qa_pair_project_project_id_qna_post(project_id, create_qa_pair_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of QnAApi->create_qa_pair_project_project_id_qna_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QnAApi->create_qa_pair_project_project_id_qna_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **create_qa_pair_request** | [**CreateQAPairRequest**](CreateQAPairRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**DbQnAPair**](DbQnAPair.md)

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

# **delete_qna_project_project_id_qna_qna_id_delete**
> DeleteQuestionOutput delete_qna_project_project_id_qna_qna_id_delete(project_id, qna_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Delete Qna

Delete a QnA pair by PK

### Example


```python
import odin_sdk
from odin_sdk.models.delete_question_output import DeleteQuestionOutput
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
    api_instance = odin_sdk.QnAApi(api_client)
    project_id = 'project_id_example' # str | 
    qna_id = 'qna_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Delete Qna
        api_response = api_instance.delete_qna_project_project_id_qna_qna_id_delete(project_id, qna_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of QnAApi->delete_qna_project_project_id_qna_qna_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QnAApi->delete_qna_project_project_id_qna_qna_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **qna_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**DeleteQuestionOutput**](DeleteQuestionOutput.md)

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

# **generate_qna_project_project_id_generate_qna_post**
> TaskStatusResponse generate_qna_project_project_id_generate_qna_post(project_id, generate_qn_a_input, x_api_key=x_api_key, x_api_secret=x_api_secret)

Generate Qna

Generate templates for a document and populate the database

### Example


```python
import odin_sdk
from odin_sdk.models.generate_qn_a_input import GenerateQnAInput
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
    api_instance = odin_sdk.QnAApi(api_client)
    project_id = 'project_id_example' # str | 
    generate_qn_a_input = odin_sdk.GenerateQnAInput() # GenerateQnAInput | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Generate Qna
        api_response = api_instance.generate_qna_project_project_id_generate_qna_post(project_id, generate_qn_a_input, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of QnAApi->generate_qna_project_project_id_generate_qna_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QnAApi->generate_qna_project_project_id_generate_qna_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **generate_qn_a_input** | [**GenerateQnAInput**](GenerateQnAInput.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**TaskStatusResponse**](TaskStatusResponse.md)

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

# **get_snippet_types_snippet_types_get**
> List[object] get_snippet_types_snippet_types_get()

Get Snippet Types

Get all available snippet types

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
    api_instance = odin_sdk.QnAApi(api_client)

    try:
        # Get Snippet Types
        api_response = api_instance.get_snippet_types_snippet_types_get()
        print("The response of QnAApi->get_snippet_types_snippet_types_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QnAApi->get_snippet_types_snippet_types_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_qnas_project_project_id_qna_get**
> List[DbQnAPair] list_qnas_project_project_id_qna_get(project_id, content_key=content_key, snippet_type=snippet_type, x_api_key=x_api_key, x_api_secret=x_api_secret)

List Qnas

List all templates for a project

### Example


```python
import odin_sdk
from odin_sdk.models.db_qn_a_pair import DbQnAPair
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
    api_instance = odin_sdk.QnAApi(api_client)
    project_id = 'project_id_example' # str | 
    content_key = 'content_key_example' # str |  (optional)
    snippet_type = 'snippet_type_example' # str |  (optional)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # List Qnas
        api_response = api_instance.list_qnas_project_project_id_qna_get(project_id, content_key=content_key, snippet_type=snippet_type, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of QnAApi->list_qnas_project_project_id_qna_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QnAApi->list_qnas_project_project_id_qna_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **content_key** | **str**|  | [optional] 
 **snippet_type** | **str**|  | [optional] 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**List[DbQnAPair]**](DbQnAPair.md)

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

# **retrieve_qna_project_project_id_qna_qna_id_get**
> DbQnAPair retrieve_qna_project_project_id_qna_qna_id_get(project_id, qna_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Retrieve Qna

Retrieve a QnA pair by PK

### Example


```python
import odin_sdk
from odin_sdk.models.db_qn_a_pair import DbQnAPair
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
    api_instance = odin_sdk.QnAApi(api_client)
    project_id = 'project_id_example' # str | 
    qna_id = 'qna_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Retrieve Qna
        api_response = api_instance.retrieve_qna_project_project_id_qna_qna_id_get(project_id, qna_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of QnAApi->retrieve_qna_project_project_id_qna_qna_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QnAApi->retrieve_qna_project_project_id_qna_qna_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **qna_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**DbQnAPair**](DbQnAPair.md)

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

# **update_qna_project_project_id_qna_qna_id_put**
> DbQnAPair update_qna_project_project_id_qna_qna_id_put(project_id, qna_id, update_qn_a_pair, x_api_key=x_api_key, x_api_secret=x_api_secret)

Update Qna

Update a QnA pair by PK

### Example


```python
import odin_sdk
from odin_sdk.models.db_qn_a_pair import DbQnAPair
from odin_sdk.models.update_qn_a_pair import UpdateQnAPair
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
    api_instance = odin_sdk.QnAApi(api_client)
    project_id = 'project_id_example' # str | 
    qna_id = 'qna_id_example' # str | 
    update_qn_a_pair = odin_sdk.UpdateQnAPair() # UpdateQnAPair | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Update Qna
        api_response = api_instance.update_qna_project_project_id_qna_qna_id_put(project_id, qna_id, update_qn_a_pair, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of QnAApi->update_qna_project_project_id_qna_qna_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QnAApi->update_qna_project_project_id_qna_qna_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **qna_id** | **str**|  | 
 **update_qn_a_pair** | [**UpdateQnAPair**](UpdateQnAPair.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**DbQnAPair**](DbQnAPair.md)

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

