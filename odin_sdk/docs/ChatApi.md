# odin_sdk.ChatApi

All URIs are relative to *http://127.0.0.1:8001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_chat_chat_create_post**](ChatApi.md#create_chat_chat_create_post) | **POST** /chat/create | Create Chat
[**get_chat_project_project_id_chat_chat_id_get**](ChatApi.md#get_chat_project_project_id_chat_chat_id_get) | **GET** /project/{project_id}/chat/{chat_id} | Get Chat
[**get_chats_project_project_id_chat_get**](ChatApi.md#get_chats_project_project_id_chat_get) | **GET** /project/{project_id}/chat | Get Chats
[**get_default_models_chat_models_get**](ChatApi.md#get_default_models_chat_models_get) | **GET** /chat/models | Get Default Models


# **create_chat_chat_create_post**
> CreateChatPromptResponse create_chat_chat_create_post(create_chat_prompt_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Create Chat

Creates a new chat in the project

### Example


```python
import odin_sdk
from odin_sdk.models.create_chat_prompt_request import CreateChatPromptRequest
from odin_sdk.models.create_chat_prompt_response import CreateChatPromptResponse
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
    api_instance = odin_sdk.ChatApi(api_client)
    create_chat_prompt_request = odin_sdk.CreateChatPromptRequest() # CreateChatPromptRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Create Chat
        api_response = api_instance.create_chat_chat_create_post(create_chat_prompt_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ChatApi->create_chat_chat_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatApi->create_chat_chat_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_chat_prompt_request** | [**CreateChatPromptRequest**](CreateChatPromptRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**CreateChatPromptResponse**](CreateChatPromptResponse.md)

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

# **get_chat_project_project_id_chat_chat_id_get**
> GetChatResponse get_chat_project_project_id_chat_chat_id_get(chat_id, project_id, prompt_debug=prompt_debug, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Chat

Gets a chat from the project

### Example


```python
import odin_sdk
from odin_sdk.models.get_chat_response import GetChatResponse
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
    api_instance = odin_sdk.ChatApi(api_client)
    chat_id = 'chat_id_example' # str | 
    project_id = 'project_id_example' # str | 
    prompt_debug = 'prompt_debug_example' # str | Enable prompt debugging (optional)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Chat
        api_response = api_instance.get_chat_project_project_id_chat_chat_id_get(chat_id, project_id, prompt_debug=prompt_debug, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ChatApi->get_chat_project_project_id_chat_chat_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatApi->get_chat_project_project_id_chat_chat_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chat_id** | **str**|  | 
 **project_id** | **str**|  | 
 **prompt_debug** | **str**| Enable prompt debugging | [optional] 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**GetChatResponse**](GetChatResponse.md)

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

# **get_chats_project_project_id_chat_get**
> GetChatsResponse get_chats_project_project_id_chat_get(project_id, cursor=cursor, limit=limit, user_id=user_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Chats

Gets all the chats in a project with pagination

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
    api_instance = odin_sdk.ChatApi(api_client)
    project_id = 'project_id_example' # str | 
    cursor = 3.4 # float | Timestamp cursor for pagination (optional)
    limit = 30 # int | Number of chats to return (optional) (default to 30)
    user_id = 'user_id_example' # str | User ID to filter by (optional)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Chats
        api_response = api_instance.get_chats_project_project_id_chat_get(project_id, cursor=cursor, limit=limit, user_id=user_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ChatApi->get_chats_project_project_id_chat_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatApi->get_chats_project_project_id_chat_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **cursor** | **float**| Timestamp cursor for pagination | [optional] 
 **limit** | **int**| Number of chats to return | [optional] [default to 30]
 **user_id** | **str**| User ID to filter by | [optional] 
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

# **get_default_models_chat_models_get**
> ChatModelInfoResponse get_default_models_chat_models_get()

Get Default Models

Retrieves the list of default models available for the app.

### Example


```python
import odin_sdk
from odin_sdk.models.chat_model_info_response import ChatModelInfoResponse
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
    api_instance = odin_sdk.ChatApi(api_client)

    try:
        # Get Default Models
        api_response = api_instance.get_default_models_chat_models_get()
        print("The response of ChatApi->get_default_models_chat_models_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatApi->get_default_models_chat_models_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ChatModelInfoResponse**](ChatModelInfoResponse.md)

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

