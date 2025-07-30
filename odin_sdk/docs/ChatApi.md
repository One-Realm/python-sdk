# odin_sdk.ChatApi

All URIs are relative to *http://127.0.0.1:8001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_chat_chat_create_post**](ChatApi.md#create_chat_chat_create_post) | **POST** /chat/create | Create Chat
[**delete_chat_chat_delete_delete**](ChatApi.md#delete_chat_chat_delete_delete) | **DELETE** /chat/delete | Delete Chat
[**get_chat_project_project_id_chat_chat_id_get**](ChatApi.md#get_chat_project_project_id_chat_chat_id_get) | **GET** /project/{project_id}/chat/{chat_id} | Get Chat
[**get_chats_project_project_id_chat_get**](ChatApi.md#get_chats_project_project_id_chat_get) | **GET** /project/{project_id}/chat | Get Chats
[**get_default_models_chat_models_get**](ChatApi.md#get_default_models_chat_models_get) | **GET** /chat/models | Get Default Models
[**send_message_v3_v3_chat_message_post**](ChatApi.md#send_message_v3_v3_chat_message_post) | **POST** /v3/chat/message |  Send Message V3


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

# **delete_chat_chat_delete_delete**
> DeleteChatResponse delete_chat_chat_delete_delete(delete_chat_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Delete Chat

Deletes a chat from the project

### Example


```python
import odin_sdk
from odin_sdk.models.delete_chat_request import DeleteChatRequest
from odin_sdk.models.delete_chat_response import DeleteChatResponse
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
    delete_chat_request = odin_sdk.DeleteChatRequest() # DeleteChatRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Delete Chat
        api_response = api_instance.delete_chat_chat_delete_delete(delete_chat_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ChatApi->delete_chat_chat_delete_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatApi->delete_chat_chat_delete_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_chat_request** | [**DeleteChatRequest**](DeleteChatRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**DeleteChatResponse**](DeleteChatResponse.md)

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

# **send_message_v3_v3_chat_message_post**
> SendMessageResponse send_message_v3_v3_chat_message_post(message, project_id, x_api_key=x_api_key, x_api_secret=x_api_secret, chat_id=chat_id, document_keys=document_keys, google_search=google_search, is_test=is_test, personality_name=personality_name, return_message=return_message, ai_response=ai_response, model_name=model_name, agent_type=agent_type, chat_name=chat_name, agent_id=agent_id, personality_id=personality_id, use_knowledgebase=use_knowledgebase, is_regenerating=is_regenerating, message_id=message_id, ui_form=ui_form, images=images, threshold=threshold, use_kb_cache=use_kb_cache, ignore_chat_history=ignore_chat_history, quick_upload_file=quick_upload_file, format_instructions=format_instructions, example_json=example_json, multipart_document_keys=multipart_document_keys, quick_upload_multiple=quick_upload_multiple, sent_from_automator=sent_from_automator, skip_stream=skip_stream, request_metadata=request_metadata, artifact=artifact)

 Send Message V3

Sends a message to the chat

### Example


```python
import odin_sdk
from odin_sdk.models.images import Images
from odin_sdk.models.quick_upload_multiple import QuickUploadMultiple
from odin_sdk.models.send_message_response import SendMessageResponse
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
    message = 'message_example' # str | 
    project_id = 'project_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)
    chat_id = 'chat_id_example' # str |  (optional)
    document_keys = 'document_keys_example' # str |  (optional)
    google_search = True # bool |  (optional)
    is_test = True # bool |  (optional)
    personality_name = 'personality_name_example' # str |  (optional)
    return_message = True # bool |  (optional)
    ai_response = True # bool |  (optional)
    model_name = 'model_name_example' # str |  (optional)
    agent_type = 'agent_type_example' # str |  (optional)
    chat_name = 'chat_name_example' # str |  (optional)
    agent_id = 'agent_id_example' # str |  (optional)
    personality_id = 'personality_id_example' # str |  (optional)
    use_knowledgebase = True # bool |  (optional)
    is_regenerating = True # bool |  (optional)
    message_id = 'message_id_example' # str |  (optional)
    ui_form = None # object |  (optional)
    images = odin_sdk.Images() # Images |  (optional)
    threshold = 3.4 # float |  (optional)
    use_kb_cache = True # bool |  (optional)
    ignore_chat_history = True # bool |  (optional)
    quick_upload_file = None # bytearray |  (optional)
    format_instructions = 'format_instructions_example' # str |  (optional)
    example_json = 'example_json_example' # str |  (optional)
    multipart_document_keys = 'multipart_document_keys_example' # str |  (optional)
    quick_upload_multiple = odin_sdk.QuickUploadMultiple() # QuickUploadMultiple |  (optional)
    sent_from_automator = True # bool |  (optional)
    skip_stream = True # bool |  (optional)
    request_metadata = 'request_metadata_example' # str |  (optional)
    artifact = 'artifact_example' # str |  (optional)

    try:
        #  Send Message V3
        api_response = api_instance.send_message_v3_v3_chat_message_post(message, project_id, x_api_key=x_api_key, x_api_secret=x_api_secret, chat_id=chat_id, document_keys=document_keys, google_search=google_search, is_test=is_test, personality_name=personality_name, return_message=return_message, ai_response=ai_response, model_name=model_name, agent_type=agent_type, chat_name=chat_name, agent_id=agent_id, personality_id=personality_id, use_knowledgebase=use_knowledgebase, is_regenerating=is_regenerating, message_id=message_id, ui_form=ui_form, images=images, threshold=threshold, use_kb_cache=use_kb_cache, ignore_chat_history=ignore_chat_history, quick_upload_file=quick_upload_file, format_instructions=format_instructions, example_json=example_json, multipart_document_keys=multipart_document_keys, quick_upload_multiple=quick_upload_multiple, sent_from_automator=sent_from_automator, skip_stream=skip_stream, request_metadata=request_metadata, artifact=artifact)
        print("The response of ChatApi->send_message_v3_v3_chat_message_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatApi->send_message_v3_v3_chat_message_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message** | **str**|  | 
 **project_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 
 **chat_id** | **str**|  | [optional] 
 **document_keys** | **str**|  | [optional] 
 **google_search** | **bool**|  | [optional] 
 **is_test** | **bool**|  | [optional] 
 **personality_name** | **str**|  | [optional] 
 **return_message** | **bool**|  | [optional] 
 **ai_response** | **bool**|  | [optional] 
 **model_name** | **str**|  | [optional] 
 **agent_type** | **str**|  | [optional] 
 **chat_name** | **str**|  | [optional] 
 **agent_id** | **str**|  | [optional] 
 **personality_id** | **str**|  | [optional] 
 **use_knowledgebase** | **bool**|  | [optional] 
 **is_regenerating** | **bool**|  | [optional] 
 **message_id** | **str**|  | [optional] 
 **ui_form** | [**object**](object.md)|  | [optional] 
 **images** | [**Images**](Images.md)|  | [optional] 
 **threshold** | **float**|  | [optional] 
 **use_kb_cache** | **bool**|  | [optional] 
 **ignore_chat_history** | **bool**|  | [optional] 
 **quick_upload_file** | **bytearray**|  | [optional] 
 **format_instructions** | **str**|  | [optional] 
 **example_json** | **str**|  | [optional] 
 **multipart_document_keys** | **str**|  | [optional] 
 **quick_upload_multiple** | [**QuickUploadMultiple**](QuickUploadMultiple.md)|  | [optional] 
 **sent_from_automator** | **bool**|  | [optional] 
 **skip_stream** | **bool**|  | [optional] 
 **request_metadata** | **str**|  | [optional] 
 **artifact** | **str**|  | [optional] 

### Return type

[**SendMessageResponse**](SendMessageResponse.md)

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

