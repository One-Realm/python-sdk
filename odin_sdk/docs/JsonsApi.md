# odin_sdk.JsonsApi

All URIs are relative to *http://127.0.0.1:8001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_json_json_delete**](JsonsApi.md#delete_json_json_delete) | **DELETE** /json | Delete Json
[**edit_json_json_put**](JsonsApi.md#edit_json_json_put) | **PUT** /json | Edit Json
[**get_json_json_post**](JsonsApi.md#get_json_json_post) | **POST** /json | Get Json
[**get_jsons_jsons_post**](JsonsApi.md#get_jsons_jsons_post) | **POST** /jsons | Get Jsons


# **delete_json_json_delete**
> DeleteJsonResponse delete_json_json_delete(delete_json_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Delete Json

### Example


```python
import odin_sdk
from odin_sdk.models.delete_json_request import DeleteJsonRequest
from odin_sdk.models.delete_json_response import DeleteJsonResponse
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
    api_instance = odin_sdk.JsonsApi(api_client)
    delete_json_request = odin_sdk.DeleteJsonRequest() # DeleteJsonRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Delete Json
        api_response = api_instance.delete_json_json_delete(delete_json_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of JsonsApi->delete_json_json_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JsonsApi->delete_json_json_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_json_request** | [**DeleteJsonRequest**](DeleteJsonRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**DeleteJsonResponse**](DeleteJsonResponse.md)

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

# **edit_json_json_put**
> object edit_json_json_put(update_json_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Edit Json

### Example


```python
import odin_sdk
from odin_sdk.models.update_json_request import UpdateJsonRequest
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
    api_instance = odin_sdk.JsonsApi(api_client)
    update_json_request = odin_sdk.UpdateJsonRequest() # UpdateJsonRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Edit Json
        api_response = api_instance.edit_json_json_put(update_json_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of JsonsApi->edit_json_json_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JsonsApi->edit_json_json_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_json_request** | [**UpdateJsonRequest**](UpdateJsonRequest.md)|  | 
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

# **get_json_json_post**
> object get_json_json_post(get_json_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Json

### Example


```python
import odin_sdk
from odin_sdk.models.get_json_request import GetJsonRequest
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
    api_instance = odin_sdk.JsonsApi(api_client)
    get_json_request = odin_sdk.GetJsonRequest() # GetJsonRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Json
        api_response = api_instance.get_json_json_post(get_json_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of JsonsApi->get_json_json_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JsonsApi->get_json_json_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_json_request** | [**GetJsonRequest**](GetJsonRequest.md)|  | 
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

# **get_jsons_jsons_post**
> object get_jsons_jsons_post(get_jsons_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Jsons

### Example


```python
import odin_sdk
from odin_sdk.models.get_jsons_request import GetJsonsRequest
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
    api_instance = odin_sdk.JsonsApi(api_client)
    get_jsons_request = odin_sdk.GetJsonsRequest() # GetJsonsRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Jsons
        api_response = api_instance.get_jsons_jsons_post(get_jsons_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of JsonsApi->get_jsons_jsons_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JsonsApi->get_jsons_jsons_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_jsons_request** | [**GetJsonsRequest**](GetJsonsRequest.md)|  | 
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

