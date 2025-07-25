# odin_sdk.ChatApi

All URIs are relative to *http://127.0.0.1:8001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_chat_chat_create_post**](ChatApi.md#create_chat_chat_create_post) | **POST** /chat/create | Create Chat
[**create_chat_test_chat_create_test_post**](ChatApi.md#create_chat_test_chat_create_test_post) | **POST** /chat/create/test | Create Chat Test
[**create_mock_chat_project_project_id_chat_chat_id_message_id_mock_post**](ChatApi.md#create_mock_chat_project_project_id_chat_chat_id_message_id_mock_post) | **POST** /project/{project_id}/chat/{chat_id}/{message_id}/mock | Create Mock Chat
[**delete_chat_bulk_chat_delete_bulk_delete**](ChatApi.md#delete_chat_bulk_chat_delete_bulk_delete) | **DELETE** /chat/delete_bulk | Delete Chat Bulk
[**delete_chat_chat_delete_delete**](ChatApi.md#delete_chat_chat_delete_delete) | **DELETE** /chat/delete | Delete Chat
[**delete_quick_upload_file_project_project_id_chat_chat_id_quick_upload_file_name_delete**](ChatApi.md#delete_quick_upload_file_project_project_id_chat_chat_id_quick_upload_file_name_delete) | **DELETE** /project/{project_id}/chat/{chat_id}/quick-upload/{file_name} | Delete Quick Upload File
[**delete_ui_form_chat_ui_form_delete**](ChatApi.md#delete_ui_form_chat_ui_form_delete) | **DELETE** /chat/ui_form | Delete Ui Form
[**generate_suggestions_chat_suggestions_post**](ChatApi.md#generate_suggestions_chat_suggestions_post) | **POST** /chat/suggestions | Generate Suggestions
[**get_audit_chat_project_project_id_chat_chat_id_audit_get**](ChatApi.md#get_audit_chat_project_project_id_chat_chat_id_audit_get) | **GET** /project/{project_id}/chat/{chat_id}/audit | Get Audit Chat
[**get_chat_all_project_project_id_chat_chat_id_all_get**](ChatApi.md#get_chat_all_project_project_id_chat_chat_id_all_get) | **GET** /project/{project_id}/chat/{chat_id}/all | Get Chat All
[**get_chat_project_project_id_chat_chat_id_get**](ChatApi.md#get_chat_project_project_id_chat_chat_id_get) | **GET** /project/{project_id}/chat/{chat_id} | Get Chat
[**get_chats_for_user_project_project_id_user_chats_get**](ChatApi.md#get_chats_for_user_project_project_id_user_chats_get) | **GET** /project/{project_id}/user/chats | Get Chats For User
[**get_chats_project_project_id_chat_get**](ChatApi.md#get_chats_project_project_id_chat_get) | **GET** /project/{project_id}/chat | Get Chats
[**get_chats_v2_v2_project_project_id_chat_get**](ChatApi.md#get_chats_v2_v2_project_project_id_chat_get) | **GET** /v2/project/{project_id}/chat | Get Chats V2
[**get_default_models_chat_models_get**](ChatApi.md#get_default_models_chat_models_get) | **GET** /chat/models | Get Default Models
[**get_document_chat_project_project_id_document_chat_document_id_get**](ChatApi.md#get_document_chat_project_project_id_document_chat_document_id_get) | **GET** /project/{project_id}/document-chat/{document_id} | Get Document Chat
[**get_kb_analytics_chat_get_kb_analytics_project_id_get**](ChatApi.md#get_kb_analytics_chat_get_kb_analytics_project_id_get) | **GET** /chat/get_kb_analytics/{project_id} | Get Kb Analytics
[**send_message_chat_message_post**](ChatApi.md#send_message_chat_message_post) | **POST** /chat/message |  Send Message
[**send_message_v2_v2_chat_message_post**](ChatApi.md#send_message_v2_v2_chat_message_post) | **POST** /v2/chat/message |  Send Message V2
[**send_message_v3_v3_chat_message_post**](ChatApi.md#send_message_v3_v3_chat_message_post) | **POST** /v3/chat/message |  Send Message V3
[**send_user_feedback_chat_message_user_feedback_post**](ChatApi.md#send_user_feedback_chat_message_user_feedback_post) | **POST** /chat/message/user/feedback | Send User Feedback
[**update_chat_name_chat_update_name_post**](ChatApi.md#update_chat_name_chat_update_name_post) | **POST** /chat/update/name | Update Chat Name


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

# **create_chat_test_chat_create_test_post**
> CreateChatTestResponse create_chat_test_chat_create_test_post(create_chat_test_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Create Chat Test

Creates a new chat test in the project

### Example


```python
import odin_sdk
from odin_sdk.models.create_chat_test_request import CreateChatTestRequest
from odin_sdk.models.create_chat_test_response import CreateChatTestResponse
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
    create_chat_test_request = odin_sdk.CreateChatTestRequest() # CreateChatTestRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Create Chat Test
        api_response = api_instance.create_chat_test_chat_create_test_post(create_chat_test_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ChatApi->create_chat_test_chat_create_test_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatApi->create_chat_test_chat_create_test_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_chat_test_request** | [**CreateChatTestRequest**](CreateChatTestRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**CreateChatTestResponse**](CreateChatTestResponse.md)

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

# **create_mock_chat_project_project_id_chat_chat_id_message_id_mock_post**
> object create_mock_chat_project_project_id_chat_chat_id_message_id_mock_post(project_id, chat_id, message_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Create Mock Chat

creates a new chat in the project

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
    api_instance = odin_sdk.ChatApi(api_client)
    project_id = 'project_id_example' # str | 
    chat_id = 'chat_id_example' # str | 
    message_id = 'message_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Create Mock Chat
        api_response = api_instance.create_mock_chat_project_project_id_chat_chat_id_message_id_mock_post(project_id, chat_id, message_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ChatApi->create_mock_chat_project_project_id_chat_chat_id_message_id_mock_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatApi->create_mock_chat_project_project_id_chat_chat_id_message_id_mock_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **chat_id** | **str**|  | 
 **message_id** | **str**|  | 
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

# **delete_chat_bulk_chat_delete_bulk_delete**
> DeleteChatResponse delete_chat_bulk_chat_delete_bulk_delete(delete_chat_bulk_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Delete Chat Bulk

Deletes chats from the project within range

### Example


```python
import odin_sdk
from odin_sdk.models.delete_chat_bulk_request import DeleteChatBulkRequest
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
    delete_chat_bulk_request = odin_sdk.DeleteChatBulkRequest() # DeleteChatBulkRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Delete Chat Bulk
        api_response = api_instance.delete_chat_bulk_chat_delete_bulk_delete(delete_chat_bulk_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ChatApi->delete_chat_bulk_chat_delete_bulk_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatApi->delete_chat_bulk_chat_delete_bulk_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_chat_bulk_request** | [**DeleteChatBulkRequest**](DeleteChatBulkRequest.md)|  | 
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

# **delete_quick_upload_file_project_project_id_chat_chat_id_quick_upload_file_name_delete**
> Dict[str, Optional[str]] delete_quick_upload_file_project_project_id_chat_chat_id_quick_upload_file_name_delete(project_id, chat_id, file_name, x_api_key=x_api_key, x_api_secret=x_api_secret)

Delete Quick Upload File

Deletes a quick upload file from the chat and knowledge base

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
    api_instance = odin_sdk.ChatApi(api_client)
    project_id = 'project_id_example' # str | 
    chat_id = 'chat_id_example' # str | 
    file_name = 'file_name_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Delete Quick Upload File
        api_response = api_instance.delete_quick_upload_file_project_project_id_chat_chat_id_quick_upload_file_name_delete(project_id, chat_id, file_name, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ChatApi->delete_quick_upload_file_project_project_id_chat_chat_id_quick_upload_file_name_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatApi->delete_quick_upload_file_project_project_id_chat_chat_id_quick_upload_file_name_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **chat_id** | **str**|  | 
 **file_name** | **str**|  | 
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

# **delete_ui_form_chat_ui_form_delete**
> UIForm delete_ui_form_chat_ui_form_delete(delete_ui_form_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Delete Ui Form

Deletes the current active UI form for actions

### Example


```python
import odin_sdk
from odin_sdk.models.delete_ui_form_request import DeleteUIFormRequest
from odin_sdk.models.ui_form import UIForm
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
    delete_ui_form_request = odin_sdk.DeleteUIFormRequest() # DeleteUIFormRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Delete Ui Form
        api_response = api_instance.delete_ui_form_chat_ui_form_delete(delete_ui_form_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ChatApi->delete_ui_form_chat_ui_form_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatApi->delete_ui_form_chat_ui_form_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_ui_form_request** | [**DeleteUIFormRequest**](DeleteUIFormRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**UIForm**](UIForm.md)

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

# **generate_suggestions_chat_suggestions_post**
> GenerateSuggestionsResponse generate_suggestions_chat_suggestions_post(generate_suggestions_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Generate Suggestions

Generates suggestions for a chat or email conversation

### Example


```python
import odin_sdk
from odin_sdk.models.generate_suggestions_request import GenerateSuggestionsRequest
from odin_sdk.models.generate_suggestions_response import GenerateSuggestionsResponse
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
    generate_suggestions_request = odin_sdk.GenerateSuggestionsRequest() # GenerateSuggestionsRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Generate Suggestions
        api_response = api_instance.generate_suggestions_chat_suggestions_post(generate_suggestions_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ChatApi->generate_suggestions_chat_suggestions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatApi->generate_suggestions_chat_suggestions_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_suggestions_request** | [**GenerateSuggestionsRequest**](GenerateSuggestionsRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**GenerateSuggestionsResponse**](GenerateSuggestionsResponse.md)

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

# **get_audit_chat_project_project_id_chat_chat_id_audit_get**
> GetChatAuditHistoryResponse get_audit_chat_project_project_id_chat_chat_id_audit_get(chat_id, project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Audit Chat

Returns audit of a chat

### Example


```python
import odin_sdk
from odin_sdk.models.get_chat_audit_history_response import GetChatAuditHistoryResponse
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
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Audit Chat
        api_response = api_instance.get_audit_chat_project_project_id_chat_chat_id_audit_get(chat_id, project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ChatApi->get_audit_chat_project_project_id_chat_chat_id_audit_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatApi->get_audit_chat_project_project_id_chat_chat_id_audit_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chat_id** | **str**|  | 
 **project_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**GetChatAuditHistoryResponse**](GetChatAuditHistoryResponse.md)

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

# **get_chat_all_project_project_id_chat_chat_id_all_get**
> GetChatResponse get_chat_all_project_project_id_chat_chat_id_all_get(chat_id, project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Chat All

Gets a chat from the project without limiting length of message history

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
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Chat All
        api_response = api_instance.get_chat_all_project_project_id_chat_chat_id_all_get(chat_id, project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ChatApi->get_chat_all_project_project_id_chat_chat_id_all_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatApi->get_chat_all_project_project_id_chat_chat_id_all_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chat_id** | **str**|  | 
 **project_id** | **str**|  | 
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

# **get_chats_for_user_project_project_id_user_chats_get**
> GetChatsForUserResponse get_chats_for_user_project_project_id_user_chats_get(project_id, cursor=cursor, limit=limit, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Chats For User

Gets all the chats for a user in a project

### Example


```python
import odin_sdk
from odin_sdk.models.get_chats_for_user_response import GetChatsForUserResponse
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
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Chats For User
        api_response = api_instance.get_chats_for_user_project_project_id_user_chats_get(project_id, cursor=cursor, limit=limit, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ChatApi->get_chats_for_user_project_project_id_user_chats_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatApi->get_chats_for_user_project_project_id_user_chats_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **cursor** | **float**| Timestamp cursor for pagination | [optional] 
 **limit** | **int**| Number of chats to return | [optional] [default to 30]
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**GetChatsForUserResponse**](GetChatsForUserResponse.md)

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

# **get_chats_v2_v2_project_project_id_chat_get**
> GetChatsResponse get_chats_v2_v2_project_project_id_chat_get(project_id, page=page, page_size=page_size, chat_name=chat_name, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Chats V2

Gets all the chats in a project with optional pagination and name filtering

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
    page = 1 # int | The page number starting from 1 (optional) (default to 1)
    page_size = 10 # int | The number of items per page, max 1000 (optional) (default to 10)
    chat_name = 'chat_name_example' # str | Optional filter by chat name (optional)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Chats V2
        api_response = api_instance.get_chats_v2_v2_project_project_id_chat_get(project_id, page=page, page_size=page_size, chat_name=chat_name, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ChatApi->get_chats_v2_v2_project_project_id_chat_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatApi->get_chats_v2_v2_project_project_id_chat_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **page** | **int**| The page number starting from 1 | [optional] [default to 1]
 **page_size** | **int**| The number of items per page, max 1000 | [optional] [default to 10]
 **chat_name** | **str**| Optional filter by chat name | [optional] 
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

# **get_document_chat_project_project_id_document_chat_document_id_get**
> GetChatResponse get_document_chat_project_project_id_document_chat_document_id_get(document_id, project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Document Chat

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
    document_id = 'document_id_example' # str | 
    project_id = 'project_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Document Chat
        api_response = api_instance.get_document_chat_project_project_id_document_chat_document_id_get(document_id, project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ChatApi->get_document_chat_project_project_id_document_chat_document_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatApi->get_document_chat_project_project_id_document_chat_document_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**|  | 
 **project_id** | **str**|  | 
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

# **get_kb_analytics_chat_get_kb_analytics_project_id_get**
> GetKbAnalyticsResponse get_kb_analytics_chat_get_kb_analytics_project_id_get(project_id, request_body=request_body)

Get Kb Analytics

Retrieves analytics for a knowledge base (KB) in the chat application.

Args:
    project_id (str): The ID of the project.
    doc_ids (List[str], optional): A list of document IDs. Defaults to None.

Returns:
    dict: A dictionary containing the following analytics:
        - doc_type_count (List[DocTypeCount]): A list of objects representing the count of each document type.
        - average_word_count_per_doc (float): The average word count per document.
        - words_and_docs_added_per_day (List[dict]): A list of dictionaries representing the number of words and documents added per day.
        - Categories (List[dict]): A list of dictionaries representing each category and its associated keywords.
            - category (str): The name of the category.
            - keywords (List[str]): A list of keywords associated with the category.
        - sources_usage_count (List[dict]): A list of dictionaries representing the number of times each source was used.

### Example


```python
import odin_sdk
from odin_sdk.models.get_kb_analytics_response import GetKbAnalyticsResponse
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
    request_body = ['request_body_example'] # List[str] |  (optional)

    try:
        # Get Kb Analytics
        api_response = api_instance.get_kb_analytics_chat_get_kb_analytics_project_id_get(project_id, request_body=request_body)
        print("The response of ChatApi->get_kb_analytics_chat_get_kb_analytics_project_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatApi->get_kb_analytics_chat_get_kb_analytics_project_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **request_body** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**GetKbAnalyticsResponse**](GetKbAnalyticsResponse.md)

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

# **send_message_chat_message_post**
> SendMessageResponse send_message_chat_message_post(send_message_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

 Send Message

Sends a message to the chat

### Example


```python
import odin_sdk
from odin_sdk.models.send_message_request import SendMessageRequest
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
    send_message_request = odin_sdk.SendMessageRequest() # SendMessageRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        #  Send Message
        api_response = api_instance.send_message_chat_message_post(send_message_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ChatApi->send_message_chat_message_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatApi->send_message_chat_message_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_message_request** | [**SendMessageRequest**](SendMessageRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**SendMessageResponse**](SendMessageResponse.md)

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

# **send_message_v2_v2_chat_message_post**
> SendMessageResponse send_message_v2_v2_chat_message_post(message, project_id, x_api_key=x_api_key, x_api_secret=x_api_secret, chat_id=chat_id, document_keys=document_keys, google_search=google_search, is_test=is_test, personality_name=personality_name, return_message=return_message, ai_response=ai_response, model_name=model_name, agent_type=agent_type, chat_name=chat_name, agent_id=agent_id, personality_id=personality_id, use_knowledgebase=use_knowledgebase, is_regenerating=is_regenerating, message_id=message_id, ui_form=ui_form, images=images, threshold=threshold, use_kb_cache=use_kb_cache, ignore_chat_history=ignore_chat_history, quick_upload_file=quick_upload_file, format_instructions=format_instructions, example_json=example_json, multipart_document_keys=multipart_document_keys, sent_from_automator=sent_from_automator, skip_stream=skip_stream, request_metadata=request_metadata)

 Send Message V2

Sends a message to the chat

### Example


```python
import odin_sdk
from odin_sdk.models.images import Images
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
    sent_from_automator = True # bool |  (optional)
    skip_stream = True # bool |  (optional)
    request_metadata = 'request_metadata_example' # str |  (optional)

    try:
        #  Send Message V2
        api_response = api_instance.send_message_v2_v2_chat_message_post(message, project_id, x_api_key=x_api_key, x_api_secret=x_api_secret, chat_id=chat_id, document_keys=document_keys, google_search=google_search, is_test=is_test, personality_name=personality_name, return_message=return_message, ai_response=ai_response, model_name=model_name, agent_type=agent_type, chat_name=chat_name, agent_id=agent_id, personality_id=personality_id, use_knowledgebase=use_knowledgebase, is_regenerating=is_regenerating, message_id=message_id, ui_form=ui_form, images=images, threshold=threshold, use_kb_cache=use_kb_cache, ignore_chat_history=ignore_chat_history, quick_upload_file=quick_upload_file, format_instructions=format_instructions, example_json=example_json, multipart_document_keys=multipart_document_keys, sent_from_automator=sent_from_automator, skip_stream=skip_stream, request_metadata=request_metadata)
        print("The response of ChatApi->send_message_v2_v2_chat_message_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatApi->send_message_v2_v2_chat_message_post: %s\n" % e)
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
 **sent_from_automator** | **bool**|  | [optional] 
 **skip_stream** | **bool**|  | [optional] 
 **request_metadata** | **str**|  | [optional] 

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

# **send_user_feedback_chat_message_user_feedback_post**
> UserFeedbackResponse send_user_feedback_chat_message_user_feedback_post(user_feedback_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Send User Feedback

Accepts user feedback for a message

### Example


```python
import odin_sdk
from odin_sdk.models.user_feedback_request import UserFeedbackRequest
from odin_sdk.models.user_feedback_response import UserFeedbackResponse
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
    user_feedback_request = odin_sdk.UserFeedbackRequest() # UserFeedbackRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Send User Feedback
        api_response = api_instance.send_user_feedback_chat_message_user_feedback_post(user_feedback_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ChatApi->send_user_feedback_chat_message_user_feedback_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatApi->send_user_feedback_chat_message_user_feedback_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_feedback_request** | [**UserFeedbackRequest**](UserFeedbackRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**UserFeedbackResponse**](UserFeedbackResponse.md)

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

# **update_chat_name_chat_update_name_post**
> ChatUpdateNameResponse update_chat_name_chat_update_name_post(chat_update_name, x_api_key=x_api_key, x_api_secret=x_api_secret)

Update Chat Name

Update the chat name for the given chat id

### Example


```python
import odin_sdk
from odin_sdk.models.chat_update_name import ChatUpdateName
from odin_sdk.models.chat_update_name_response import ChatUpdateNameResponse
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
    chat_update_name = odin_sdk.ChatUpdateName() # ChatUpdateName | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Update Chat Name
        api_response = api_instance.update_chat_name_chat_update_name_post(chat_update_name, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ChatApi->update_chat_name_chat_update_name_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatApi->update_chat_name_chat_update_name_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chat_update_name** | [**ChatUpdateName**](ChatUpdateName.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**ChatUpdateNameResponse**](ChatUpdateNameResponse.md)

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

