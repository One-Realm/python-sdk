# odin_sdk.MeetingsApi

All URIs are relative to *http://127.0.0.1:8001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_recording_recording_add_post**](MeetingsApi.md#add_recording_recording_add_post) | **POST** /recording/add | Add Recording
[**export_transcript_bot_bot_id_transcript_export_get**](MeetingsApi.md#export_transcript_bot_bot_id_transcript_export_get) | **GET** /bot/{bot_id}/transcript/export | Export Transcript
[**generate_meeting_title_meetings_bot_id_generate_title_post**](MeetingsApi.md#generate_meeting_title_meetings_bot_id_generate_title_post) | **POST** /meetings/{bot_id}/generate_title | Generate Meeting Title
[**get_user_storage_meetings_user_storage_get**](MeetingsApi.md#get_user_storage_meetings_user_storage_get) | **GET** /meetings/user/storage | Get User Storage
[**handle_get_meeting_info_by_title_meetings_info_get**](MeetingsApi.md#handle_get_meeting_info_by_title_meetings_info_get) | **GET** /meetings/info | Handle Get Meeting Info By Title
[**handle_get_meetings_by_title_meetings_title_get**](MeetingsApi.md#handle_get_meetings_by_title_meetings_title_get) | **GET** /meetings/title | Handle Get Meetings By Title
[**handle_get_meetings_meetings_post**](MeetingsApi.md#handle_get_meetings_meetings_post) | **POST** /meetings | Handle Get Meetings
[**handle_share_meeting_with_project_meeting_share_project_post**](MeetingsApi.md#handle_share_meeting_with_project_meeting_share_project_post) | **POST** /meeting/share/project | Handle Share Meeting With Project


# **add_recording_recording_add_post**
> AddRecordingResponse add_recording_recording_add_post(file, file_type=file_type, x_api_key=x_api_key, x_api_secret=x_api_secret)

Add Recording

Adds a recording to the meetings API.

Args:
    file (UploadFile): The uploaded file to be added as a recording.
    request (Request): The request object.
    response (Response): The response object.
    file_type (Optional[str], optional): The type of the file. Defaults to None.
    user (User, optional): The user object. Defaults to Depends(verify_token).

Returns:
    AddRecordingResponse: The response object containing the message and recording ID.

### Example


```python
import odin_sdk
from odin_sdk.models.add_recording_response import AddRecordingResponse
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
    api_instance = odin_sdk.MeetingsApi(api_client)
    file = None # bytearray | 
    file_type = 'file_type_example' # str |  (optional)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Add Recording
        api_response = api_instance.add_recording_recording_add_post(file, file_type=file_type, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of MeetingsApi->add_recording_recording_add_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeetingsApi->add_recording_recording_add_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**|  | 
 **file_type** | **str**|  | [optional] 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**AddRecordingResponse**](AddRecordingResponse.md)

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

# **export_transcript_bot_bot_id_transcript_export_get**
> export_transcript_bot_bot_id_transcript_export_get(bot_id, format, x_api_key=x_api_key, x_api_secret=x_api_secret)

Export Transcript

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
    api_instance = odin_sdk.MeetingsApi(api_client)
    bot_id = 'bot_id_example' # str | 
    format = 'format_example' # str | Export format: csv or txt
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Export Transcript
        api_instance.export_transcript_bot_bot_id_transcript_export_get(bot_id, format, x_api_key=x_api_key, x_api_secret=x_api_secret)
    except Exception as e:
        print("Exception when calling MeetingsApi->export_transcript_bot_bot_id_transcript_export_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bot_id** | **str**|  | 
 **format** | **str**| Export format: csv or txt | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

void (empty response body)

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

# **generate_meeting_title_meetings_bot_id_generate_title_post**
> object generate_meeting_title_meetings_bot_id_generate_title_post(bot_id, timestamp=timestamp, x_api_key=x_api_key, x_api_secret=x_api_secret)

Generate Meeting Title

Generates a meeting title based on the provided meeting summary.

Args:
    bot_id (str): The ID of the bot associated with the meeting.
    timestamp (Optional[float], optional): The timestamp of the request. Defaults to None.
    user (User, optional): The user making the request. Defaults to Depends(verify_token).

Raises:
    HTTPException: If the transcript does not exist or there is an error in getting the summary.

Returns:
    GenerateMeetingTitleResponse: The generated meeting title.

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
    api_instance = odin_sdk.MeetingsApi(api_client)
    bot_id = 'bot_id_example' # str | 
    timestamp = 3.4 # float |  (optional)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Generate Meeting Title
        api_response = api_instance.generate_meeting_title_meetings_bot_id_generate_title_post(bot_id, timestamp=timestamp, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of MeetingsApi->generate_meeting_title_meetings_bot_id_generate_title_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeetingsApi->generate_meeting_title_meetings_bot_id_generate_title_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bot_id** | **str**|  | 
 **timestamp** | **float**|  | [optional] 
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

# **get_user_storage_meetings_user_storage_get**
> MeetingStorageResponse get_user_storage_meetings_user_storage_get(x_api_key=x_api_key, x_api_secret=x_api_secret)

Get User Storage

### Example


```python
import odin_sdk
from odin_sdk.models.meeting_storage_response import MeetingStorageResponse
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
    api_instance = odin_sdk.MeetingsApi(api_client)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get User Storage
        api_response = api_instance.get_user_storage_meetings_user_storage_get(x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of MeetingsApi->get_user_storage_meetings_user_storage_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeetingsApi->get_user_storage_meetings_user_storage_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**MeetingStorageResponse**](MeetingStorageResponse.md)

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

# **handle_get_meeting_info_by_title_meetings_info_get**
> GetMeetingsByTitleSummariesResponse handle_get_meeting_info_by_title_meetings_info_get(title, summary_type, timestamp=timestamp, x_api_key=x_api_key, x_api_secret=x_api_secret)

Handle Get Meeting Info By Title

Retrieve meeting details, including a summary, based on the provided title.

### Example


```python
import odin_sdk
from odin_sdk.models.get_meetings_by_title_summaries_response import GetMeetingsByTitleSummariesResponse
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
    api_instance = odin_sdk.MeetingsApi(api_client)
    title = 'title_example' # str | 
    summary_type = 'summary_type_example' # str | 
    timestamp = 3.4 # float |  (optional)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Handle Get Meeting Info By Title
        api_response = api_instance.handle_get_meeting_info_by_title_meetings_info_get(title, summary_type, timestamp=timestamp, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of MeetingsApi->handle_get_meeting_info_by_title_meetings_info_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeetingsApi->handle_get_meeting_info_by_title_meetings_info_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title** | **str**|  | 
 **summary_type** | **str**|  | 
 **timestamp** | **float**|  | [optional] 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**GetMeetingsByTitleSummariesResponse**](GetMeetingsByTitleSummariesResponse.md)

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

# **handle_get_meetings_by_title_meetings_title_get**
> GetMeetingsByTitleResponse handle_get_meetings_by_title_meetings_title_get(title, timestamp=timestamp, x_api_key=x_api_key, x_api_secret=x_api_secret)

Handle Get Meetings By Title

Retrieve the meetings based on the provided title.

### Example


```python
import odin_sdk
from odin_sdk.models.get_meetings_by_title_response import GetMeetingsByTitleResponse
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
    api_instance = odin_sdk.MeetingsApi(api_client)
    title = 'title_example' # str | 
    timestamp = 3.4 # float |  (optional)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Handle Get Meetings By Title
        api_response = api_instance.handle_get_meetings_by_title_meetings_title_get(title, timestamp=timestamp, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of MeetingsApi->handle_get_meetings_by_title_meetings_title_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeetingsApi->handle_get_meetings_by_title_meetings_title_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title** | **str**|  | 
 **timestamp** | **float**|  | [optional] 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**GetMeetingsByTitleResponse**](GetMeetingsByTitleResponse.md)

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

# **handle_get_meetings_meetings_post**
> GetMeetingsResponse handle_get_meetings_meetings_post(get_meetings_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Handle Get Meetings

### Example


```python
import odin_sdk
from odin_sdk.models.get_meetings_request import GetMeetingsRequest
from odin_sdk.models.get_meetings_response import GetMeetingsResponse
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
    api_instance = odin_sdk.MeetingsApi(api_client)
    get_meetings_request = odin_sdk.GetMeetingsRequest() # GetMeetingsRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Handle Get Meetings
        api_response = api_instance.handle_get_meetings_meetings_post(get_meetings_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of MeetingsApi->handle_get_meetings_meetings_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeetingsApi->handle_get_meetings_meetings_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_meetings_request** | [**GetMeetingsRequest**](GetMeetingsRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**GetMeetingsResponse**](GetMeetingsResponse.md)

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

# **handle_share_meeting_with_project_meeting_share_project_post**
> object handle_share_meeting_with_project_meeting_share_project_post(share_meeting_with_project_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Handle Share Meeting With Project

### Example


```python
import odin_sdk
from odin_sdk.models.share_meeting_with_project_request import ShareMeetingWithProjectRequest
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
    api_instance = odin_sdk.MeetingsApi(api_client)
    share_meeting_with_project_request = odin_sdk.ShareMeetingWithProjectRequest() # ShareMeetingWithProjectRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Handle Share Meeting With Project
        api_response = api_instance.handle_share_meeting_with_project_meeting_share_project_post(share_meeting_with_project_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of MeetingsApi->handle_share_meeting_with_project_meeting_share_project_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeetingsApi->handle_share_meeting_with_project_meeting_share_project_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **share_meeting_with_project_request** | [**ShareMeetingWithProjectRequest**](ShareMeetingWithProjectRequest.md)|  | 
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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

