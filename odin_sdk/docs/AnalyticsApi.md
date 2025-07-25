# odin_sdk.AnalyticsApi

All URIs are relative to *http://127.0.0.1:8001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_feedback_analytics_chat_project_id_chat_id_message_id_feedback_delete**](AnalyticsApi.md#delete_feedback_analytics_chat_project_id_chat_id_message_id_feedback_delete) | **DELETE** /analytics/chat/{project_id}/{chat_id}/{message_id}/feedback | Delete Feedback
[**get_chat_analytics_analytics_chats_project_id_post**](AnalyticsApi.md#get_chat_analytics_analytics_chats_project_id_post) | **POST** /analytics/chats/{project_id} | Get Chat Analytics 
[**get_chat_analytics_metrics_timeseries_analytics_chats_project_id_metrics_and_timeseries_post**](AnalyticsApi.md#get_chat_analytics_metrics_timeseries_analytics_chats_project_id_metrics_and_timeseries_post) | **POST** /analytics/chats/{project_id}/metrics_and_timeseries | Get Chat Analytics Metrics Timeseries 
[**get_chat_analytics_nlp_metrics_and_categories_analytics_chats_project_id_nlp_metrics_and_categories_post**](AnalyticsApi.md#get_chat_analytics_nlp_metrics_and_categories_analytics_chats_project_id_nlp_metrics_and_categories_post) | **POST** /analytics/chats/{project_id}/nlp_metrics_and_categories | Get Chat Analytics Nlp Metrics And Categories 
[**get_feedback_array_analytics_chat_project_id_chat_id_message_id_feedback_get**](AnalyticsApi.md#get_feedback_array_analytics_chat_project_id_chat_id_message_id_feedback_get) | **GET** /analytics/chat/{project_id}/{chat_id}/{message_id}/feedback | Get Feedback Array
[**get_feedback_table_analytics_chat_project_id_feedback_table_post**](AnalyticsApi.md#get_feedback_table_analytics_chat_project_id_feedback_table_post) | **POST** /analytics/chat/{project_id}/feedback_table | Get Feedback Table
[**get_kb_analytics_analytics_kb_project_id_get**](AnalyticsApi.md#get_kb_analytics_analytics_kb_project_id_get) | **GET** /analytics/kb/{project_id} | Get Kb Analytics 


# **delete_feedback_analytics_chat_project_id_chat_id_message_id_feedback_delete**
> DeleteFeedbackResponse delete_feedback_analytics_chat_project_id_chat_id_message_id_feedback_delete(project_id, chat_id, message_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Delete Feedback

Delete feedbacks for a message

### Example


```python
import odin_sdk
from odin_sdk.models.delete_feedback_response import DeleteFeedbackResponse
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
    api_instance = odin_sdk.AnalyticsApi(api_client)
    project_id = 'project_id_example' # str | 
    chat_id = 'chat_id_example' # str | 
    message_id = 'message_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Delete Feedback
        api_response = api_instance.delete_feedback_analytics_chat_project_id_chat_id_message_id_feedback_delete(project_id, chat_id, message_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of AnalyticsApi->delete_feedback_analytics_chat_project_id_chat_id_message_id_feedback_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->delete_feedback_analytics_chat_project_id_chat_id_message_id_feedback_delete: %s\n" % e)
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

[**DeleteFeedbackResponse**](DeleteFeedbackResponse.md)

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

# **get_chat_analytics_analytics_chats_project_id_post**
> GetChatAnalyticsResponse get_chat_analytics_analytics_chats_project_id_post(project_id, get_chat_analytics_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Chat Analytics 

### Example


```python
import odin_sdk
from odin_sdk.models.get_chat_analytics_request import GetChatAnalyticsRequest
from odin_sdk.models.get_chat_analytics_response import GetChatAnalyticsResponse
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
    api_instance = odin_sdk.AnalyticsApi(api_client)
    project_id = 'project_id_example' # str | 
    get_chat_analytics_request = odin_sdk.GetChatAnalyticsRequest() # GetChatAnalyticsRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Chat Analytics 
        api_response = api_instance.get_chat_analytics_analytics_chats_project_id_post(project_id, get_chat_analytics_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of AnalyticsApi->get_chat_analytics_analytics_chats_project_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->get_chat_analytics_analytics_chats_project_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **get_chat_analytics_request** | [**GetChatAnalyticsRequest**](GetChatAnalyticsRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**GetChatAnalyticsResponse**](GetChatAnalyticsResponse.md)

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

# **get_chat_analytics_metrics_timeseries_analytics_chats_project_id_metrics_and_timeseries_post**
> GetChatAnalyticsResponseMetricsAndTimeseries get_chat_analytics_metrics_timeseries_analytics_chats_project_id_metrics_and_timeseries_post(project_id, get_chat_analytics_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Chat Analytics Metrics Timeseries 

### Example


```python
import odin_sdk
from odin_sdk.models.get_chat_analytics_request import GetChatAnalyticsRequest
from odin_sdk.models.get_chat_analytics_response_metrics_and_timeseries import GetChatAnalyticsResponseMetricsAndTimeseries
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
    api_instance = odin_sdk.AnalyticsApi(api_client)
    project_id = 'project_id_example' # str | 
    get_chat_analytics_request = odin_sdk.GetChatAnalyticsRequest() # GetChatAnalyticsRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Chat Analytics Metrics Timeseries 
        api_response = api_instance.get_chat_analytics_metrics_timeseries_analytics_chats_project_id_metrics_and_timeseries_post(project_id, get_chat_analytics_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of AnalyticsApi->get_chat_analytics_metrics_timeseries_analytics_chats_project_id_metrics_and_timeseries_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->get_chat_analytics_metrics_timeseries_analytics_chats_project_id_metrics_and_timeseries_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **get_chat_analytics_request** | [**GetChatAnalyticsRequest**](GetChatAnalyticsRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**GetChatAnalyticsResponseMetricsAndTimeseries**](GetChatAnalyticsResponseMetricsAndTimeseries.md)

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

# **get_chat_analytics_nlp_metrics_and_categories_analytics_chats_project_id_nlp_metrics_and_categories_post**
> GetChatAnalyticsResponseNLPMetricsAndCategories get_chat_analytics_nlp_metrics_and_categories_analytics_chats_project_id_nlp_metrics_and_categories_post(project_id, get_chat_analytics_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Chat Analytics Nlp Metrics And Categories 

### Example


```python
import odin_sdk
from odin_sdk.models.get_chat_analytics_request import GetChatAnalyticsRequest
from odin_sdk.models.get_chat_analytics_response_nlp_metrics_and_categories import GetChatAnalyticsResponseNLPMetricsAndCategories
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
    api_instance = odin_sdk.AnalyticsApi(api_client)
    project_id = 'project_id_example' # str | 
    get_chat_analytics_request = odin_sdk.GetChatAnalyticsRequest() # GetChatAnalyticsRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Chat Analytics Nlp Metrics And Categories 
        api_response = api_instance.get_chat_analytics_nlp_metrics_and_categories_analytics_chats_project_id_nlp_metrics_and_categories_post(project_id, get_chat_analytics_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of AnalyticsApi->get_chat_analytics_nlp_metrics_and_categories_analytics_chats_project_id_nlp_metrics_and_categories_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->get_chat_analytics_nlp_metrics_and_categories_analytics_chats_project_id_nlp_metrics_and_categories_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **get_chat_analytics_request** | [**GetChatAnalyticsRequest**](GetChatAnalyticsRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**GetChatAnalyticsResponseNLPMetricsAndCategories**](GetChatAnalyticsResponseNLPMetricsAndCategories.md)

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

# **get_feedback_array_analytics_chat_project_id_chat_id_message_id_feedback_get**
> MessageFeedback get_feedback_array_analytics_chat_project_id_chat_id_message_id_feedback_get(project_id, chat_id, message_id)

Get Feedback Array

Get feedbacks for a message

### Example


```python
import odin_sdk
from odin_sdk.models.message_feedback import MessageFeedback
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
    api_instance = odin_sdk.AnalyticsApi(api_client)
    project_id = 'project_id_example' # str | 
    chat_id = 'chat_id_example' # str | 
    message_id = 'message_id_example' # str | 

    try:
        # Get Feedback Array
        api_response = api_instance.get_feedback_array_analytics_chat_project_id_chat_id_message_id_feedback_get(project_id, chat_id, message_id)
        print("The response of AnalyticsApi->get_feedback_array_analytics_chat_project_id_chat_id_message_id_feedback_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->get_feedback_array_analytics_chat_project_id_chat_id_message_id_feedback_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **chat_id** | **str**|  | 
 **message_id** | **str**|  | 

### Return type

[**MessageFeedback**](MessageFeedback.md)

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

# **get_feedback_table_analytics_chat_project_id_feedback_table_post**
> FeedbackTable get_feedback_table_analytics_chat_project_id_feedback_table_post(project_id, get_chat_analytics_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Feedback Table

Get feedback table for a project

### Example


```python
import odin_sdk
from odin_sdk.models.feedback_table import FeedbackTable
from odin_sdk.models.get_chat_analytics_request import GetChatAnalyticsRequest
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
    api_instance = odin_sdk.AnalyticsApi(api_client)
    project_id = 'project_id_example' # str | 
    get_chat_analytics_request = odin_sdk.GetChatAnalyticsRequest() # GetChatAnalyticsRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Feedback Table
        api_response = api_instance.get_feedback_table_analytics_chat_project_id_feedback_table_post(project_id, get_chat_analytics_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of AnalyticsApi->get_feedback_table_analytics_chat_project_id_feedback_table_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->get_feedback_table_analytics_chat_project_id_feedback_table_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **get_chat_analytics_request** | [**GetChatAnalyticsRequest**](GetChatAnalyticsRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**FeedbackTable**](FeedbackTable.md)

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

# **get_kb_analytics_analytics_kb_project_id_get**
> object get_kb_analytics_analytics_kb_project_id_get(project_id, x_api_key=x_api_key, x_api_secret=x_api_secret, request_body=request_body)

Get Kb Analytics 

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
    api_instance = odin_sdk.AnalyticsApi(api_client)
    project_id = 'project_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)
    request_body = ['request_body_example'] # List[str] |  (optional)

    try:
        # Get Kb Analytics 
        api_response = api_instance.get_kb_analytics_analytics_kb_project_id_get(project_id, x_api_key=x_api_key, x_api_secret=x_api_secret, request_body=request_body)
        print("The response of AnalyticsApi->get_kb_analytics_analytics_kb_project_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->get_kb_analytics_analytics_kb_project_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 
 **request_body** | [**List[str]**](str.md)|  | [optional] 

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

