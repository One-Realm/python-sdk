# odin_sdk.ElevenLabsApi

All URIs are relative to *http://127.0.0.1:8001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**edit_agent_elevenlabs_agent_edit_post**](ElevenLabsApi.md#edit_agent_elevenlabs_agent_edit_post) | **POST** /elevenlabs/agent/edit | Edit Agent
[**get_signed_url_elevenlabs_signed_url_get**](ElevenLabsApi.md#get_signed_url_elevenlabs_signed_url_get) | **GET** /elevenlabs/signed-url | Get Signed Url
[**save_voice_conversation_pair_elevenlabs_voice_conversation_save_pair_post**](ElevenLabsApi.md#save_voice_conversation_pair_elevenlabs_voice_conversation_save_pair_post) | **POST** /elevenlabs/voice-conversation/save-pair | Save Voice Conversation Pair
[**save_voice_message_elevenlabs_voice_message_save_post**](ElevenLabsApi.md#save_voice_message_elevenlabs_voice_message_save_post) | **POST** /elevenlabs/voice-message/save | Save Voice Message


# **edit_agent_elevenlabs_agent_edit_post**
> object edit_agent_elevenlabs_agent_edit_post(edit_agent_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Edit Agent

Edit an agent's prompt.

### Example


```python
import odin_sdk
from odin_sdk.models.edit_agent_request import EditAgentRequest
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
    api_instance = odin_sdk.ElevenLabsApi(api_client)
    edit_agent_request = odin_sdk.EditAgentRequest() # EditAgentRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Edit Agent
        api_response = api_instance.edit_agent_elevenlabs_agent_edit_post(edit_agent_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ElevenLabsApi->edit_agent_elevenlabs_agent_edit_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ElevenLabsApi->edit_agent_elevenlabs_agent_edit_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edit_agent_request** | [**EditAgentRequest**](EditAgentRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**401** | Unauthorized |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_signed_url_elevenlabs_signed_url_get**
> object get_signed_url_elevenlabs_signed_url_get(agent_id=agent_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Signed Url

Get a signed URL for ElevenLabs conversation.
This endpoint requires authentication and fetches a signed URL from ElevenLabs API.

Args:
    agent_id: Optional ElevenLabs agent ID. If not provided, uses the default from environment.
    user: Authenticated user (handled by dependency injection)

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
    api_instance = odin_sdk.ElevenLabsApi(api_client)
    agent_id = 'agent_id_example' # str | ElevenLabs agent ID (optional)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Signed Url
        api_response = api_instance.get_signed_url_elevenlabs_signed_url_get(agent_id=agent_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ElevenLabsApi->get_signed_url_elevenlabs_signed_url_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ElevenLabsApi->get_signed_url_elevenlabs_signed_url_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**| ElevenLabs agent ID | [optional] 
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
**401** | Unauthorized |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_voice_conversation_pair_elevenlabs_voice_conversation_save_pair_post**
> object save_voice_conversation_pair_elevenlabs_voice_conversation_save_pair_post(user_message, ai_response, project_id, chat_id, user_name, user_id, agent_id=agent_id, agent_name=agent_name, conversation_id=conversation_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Save Voice Conversation Pair

Save a complete voice conversation pair (user message + AI response) in one call.
This is useful for saving complete exchanges from voice conversations.

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
    api_instance = odin_sdk.ElevenLabsApi(api_client)
    user_message = 'user_message_example' # str | 
    ai_response = 'ai_response_example' # str | 
    project_id = 'project_id_example' # str | 
    chat_id = 'chat_id_example' # str | 
    user_name = 'user_name_example' # str | 
    user_id = 'user_id_example' # str | 
    agent_id = 'agent_id_example' # str |  (optional)
    agent_name = 'agent_name_example' # str |  (optional)
    conversation_id = 'conversation_id_example' # str |  (optional)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Save Voice Conversation Pair
        api_response = api_instance.save_voice_conversation_pair_elevenlabs_voice_conversation_save_pair_post(user_message, ai_response, project_id, chat_id, user_name, user_id, agent_id=agent_id, agent_name=agent_name, conversation_id=conversation_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ElevenLabsApi->save_voice_conversation_pair_elevenlabs_voice_conversation_save_pair_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ElevenLabsApi->save_voice_conversation_pair_elevenlabs_voice_conversation_save_pair_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_message** | **str**|  | 
 **ai_response** | **str**|  | 
 **project_id** | **str**|  | 
 **chat_id** | **str**|  | 
 **user_name** | **str**|  | 
 **user_id** | **str**|  | 
 **agent_id** | **str**|  | [optional] 
 **agent_name** | **str**|  | [optional] 
 **conversation_id** | **str**|  | [optional] 
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
**401** | Unauthorized |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_voice_message_elevenlabs_voice_message_save_post**
> object save_voice_message_elevenlabs_voice_message_save_post(save_voice_message_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Save Voice Message

Save a voice conversation message to the database.
This handles user transcripts, AI responses, or complete conversation pairs.

### Example


```python
import odin_sdk
from odin_sdk.models.save_voice_message_request import SaveVoiceMessageRequest
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
    api_instance = odin_sdk.ElevenLabsApi(api_client)
    save_voice_message_request = odin_sdk.SaveVoiceMessageRequest() # SaveVoiceMessageRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Save Voice Message
        api_response = api_instance.save_voice_message_elevenlabs_voice_message_save_post(save_voice_message_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ElevenLabsApi->save_voice_message_elevenlabs_voice_message_save_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ElevenLabsApi->save_voice_message_elevenlabs_voice_message_save_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **save_voice_message_request** | [**SaveVoiceMessageRequest**](SaveVoiceMessageRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**401** | Unauthorized |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

