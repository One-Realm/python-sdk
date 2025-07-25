# odin_sdk.ChatTestsApi

All URIs are relative to *http://127.0.0.1:8001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_chat_test_group_chat_create_test_group_post**](ChatTestsApi.md#create_chat_test_group_chat_create_test_group_post) | **POST** /chat/create/test/group | Create Chat Test Group
[**delete_chat_test_group_chat_delete_test_group_delete**](ChatTestsApi.md#delete_chat_test_group_chat_delete_test_group_delete) | **DELETE** /chat/delete/test/group | Delete Chat Test Group
[**get_chat_test_results_chat_test_results_get**](ChatTestsApi.md#get_chat_test_results_chat_test_results_get) | **GET** /chat/test/results | Get Chat Test Results
[**get_chat_tests_project_project_id_tests_get**](ChatTestsApi.md#get_chat_tests_project_project_id_tests_get) | **GET** /project/{project_id}/tests | Get Chat Tests
[**run_message_group_chat_message_group_post**](ChatTestsApi.md#run_message_group_chat_message_group_post) | **POST** /chat/message/group | Run Message Group
[**update_chat_test_chat_test_update_post**](ChatTestsApi.md#update_chat_test_chat_test_update_post) | **POST** /chat/test/update | Update Chat Test
[**update_chat_test_data_chat_test_update_testdata_post**](ChatTestsApi.md#update_chat_test_data_chat_test_update_testdata_post) | **POST** /chat/test/update/testdata | Update Chat Test Data


# **create_chat_test_group_chat_create_test_group_post**
> CreateTestGroupResponse create_chat_test_group_chat_create_test_group_post(create_test_group_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Create Chat Test Group

Creates a chat test group

### Example


```python
import odin_sdk
from odin_sdk.models.create_test_group_request import CreateTestGroupRequest
from odin_sdk.models.create_test_group_response import CreateTestGroupResponse
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
    api_instance = odin_sdk.ChatTestsApi(api_client)
    create_test_group_request = odin_sdk.CreateTestGroupRequest() # CreateTestGroupRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Create Chat Test Group
        api_response = api_instance.create_chat_test_group_chat_create_test_group_post(create_test_group_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ChatTestsApi->create_chat_test_group_chat_create_test_group_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatTestsApi->create_chat_test_group_chat_create_test_group_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_test_group_request** | [**CreateTestGroupRequest**](CreateTestGroupRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**CreateTestGroupResponse**](CreateTestGroupResponse.md)

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

# **delete_chat_test_group_chat_delete_test_group_delete**
> DeleteTestGroupResponse delete_chat_test_group_chat_delete_test_group_delete(delete_test_group_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Delete Chat Test Group

Deletes a chat test group

### Example


```python
import odin_sdk
from odin_sdk.models.delete_test_group_request import DeleteTestGroupRequest
from odin_sdk.models.delete_test_group_response import DeleteTestGroupResponse
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
    api_instance = odin_sdk.ChatTestsApi(api_client)
    delete_test_group_request = odin_sdk.DeleteTestGroupRequest() # DeleteTestGroupRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Delete Chat Test Group
        api_response = api_instance.delete_chat_test_group_chat_delete_test_group_delete(delete_test_group_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ChatTestsApi->delete_chat_test_group_chat_delete_test_group_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatTestsApi->delete_chat_test_group_chat_delete_test_group_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_test_group_request** | [**DeleteTestGroupRequest**](DeleteTestGroupRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**DeleteTestGroupResponse**](DeleteTestGroupResponse.md)

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

# **get_chat_test_results_chat_test_results_get**
> GetChatTestResultsResponse get_chat_test_results_chat_test_results_get(chat_tests_id, project_id, limit=limit, order_by=order_by, order_desc=order_desc, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Chat Test Results

Retrieves test results for a specific chat test

### Example


```python
import odin_sdk
from odin_sdk.models.get_chat_test_results_response import GetChatTestResultsResponse
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
    api_instance = odin_sdk.ChatTestsApi(api_client)
    chat_tests_id = 'chat_tests_id_example' # str | ID of the chat test to retrieve results for
    project_id = 'project_id_example' # str | ID of the project
    limit = 30 # int | Maximum number of results to return (optional) (default to 30)
    order_by = 'created_at' # str | Field to order results by (optional) (default to 'created_at')
    order_desc = True # bool | Whether to order in descending order (optional) (default to True)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Chat Test Results
        api_response = api_instance.get_chat_test_results_chat_test_results_get(chat_tests_id, project_id, limit=limit, order_by=order_by, order_desc=order_desc, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ChatTestsApi->get_chat_test_results_chat_test_results_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatTestsApi->get_chat_test_results_chat_test_results_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chat_tests_id** | **str**| ID of the chat test to retrieve results for | 
 **project_id** | **str**| ID of the project | 
 **limit** | **int**| Maximum number of results to return | [optional] [default to 30]
 **order_by** | **str**| Field to order results by | [optional] [default to &#39;created_at&#39;]
 **order_desc** | **bool**| Whether to order in descending order | [optional] [default to True]
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**GetChatTestResultsResponse**](GetChatTestResultsResponse.md)

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

# **get_chat_tests_project_project_id_tests_get**
> GetChatsResponse get_chat_tests_project_project_id_tests_get(project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Chat Tests

Gets all the chat tests in a project

### Example


```python
import odin_sdk
from odin_sdk.models.get_chats_response import GetChatsResponse
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
    api_instance = odin_sdk.ChatTestsApi(api_client)
    project_id = 'project_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Chat Tests
        api_response = api_instance.get_chat_tests_project_project_id_tests_get(project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ChatTestsApi->get_chat_tests_project_project_id_tests_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatTestsApi->get_chat_tests_project_project_id_tests_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**GetChatsResponse**](GetChatsResponse.md)

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

# **run_message_group_chat_message_group_post**
> SendMessageGroupResponse run_message_group_chat_message_group_post(send_test_message_group_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Run Message Group

Adds a group of test messages to the chat

### Example


```python
import odin_sdk
from odin_sdk.models.send_message_group_response import SendMessageGroupResponse
from odin_sdk.models.send_test_message_group_request import SendTestMessageGroupRequest
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
    api_instance = odin_sdk.ChatTestsApi(api_client)
    send_test_message_group_request = odin_sdk.SendTestMessageGroupRequest() # SendTestMessageGroupRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Run Message Group
        api_response = api_instance.run_message_group_chat_message_group_post(send_test_message_group_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ChatTestsApi->run_message_group_chat_message_group_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatTestsApi->run_message_group_chat_message_group_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_test_message_group_request** | [**SendTestMessageGroupRequest**](SendTestMessageGroupRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**SendMessageGroupResponse**](SendMessageGroupResponse.md)

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

# **update_chat_test_chat_test_update_post**
> UpdateChatTestResponse update_chat_test_chat_test_update_post(update_chat_test_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Update Chat Test

Updates a chat test in the project

### Example


```python
import odin_sdk
from odin_sdk.models.update_chat_test_request import UpdateChatTestRequest
from odin_sdk.models.update_chat_test_response import UpdateChatTestResponse
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
    api_instance = odin_sdk.ChatTestsApi(api_client)
    update_chat_test_request = odin_sdk.UpdateChatTestRequest() # UpdateChatTestRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Update Chat Test
        api_response = api_instance.update_chat_test_chat_test_update_post(update_chat_test_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ChatTestsApi->update_chat_test_chat_test_update_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatTestsApi->update_chat_test_chat_test_update_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_chat_test_request** | [**UpdateChatTestRequest**](UpdateChatTestRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**UpdateChatTestResponse**](UpdateChatTestResponse.md)

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

# **update_chat_test_data_chat_test_update_testdata_post**
> UpdateChatTestDataResponse update_chat_test_data_chat_test_update_testdata_post(update_chat_test_data, x_api_key=x_api_key, x_api_secret=x_api_secret)

Update Chat Test Data

Update the chat test data for the given chat id

### Example


```python
import odin_sdk
from odin_sdk.models.update_chat_test_data import UpdateChatTestData
from odin_sdk.models.update_chat_test_data_response import UpdateChatTestDataResponse
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
    api_instance = odin_sdk.ChatTestsApi(api_client)
    update_chat_test_data = odin_sdk.UpdateChatTestData() # UpdateChatTestData | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Update Chat Test Data
        api_response = api_instance.update_chat_test_data_chat_test_update_testdata_post(update_chat_test_data, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ChatTestsApi->update_chat_test_data_chat_test_update_testdata_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatTestsApi->update_chat_test_data_chat_test_update_testdata_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_chat_test_data** | [**UpdateChatTestData**](UpdateChatTestData.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**UpdateChatTestDataResponse**](UpdateChatTestDataResponse.md)

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

