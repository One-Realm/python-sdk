# odin_sdk.ClassificationsApi

All URIs are relative to *http://127.0.0.1:8001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_classification_classification_create_post**](ClassificationsApi.md#create_classification_classification_create_post) | **POST** /classification/create | Create Classification
[**delete_classification_classification_delete**](ClassificationsApi.md#delete_classification_classification_delete) | **DELETE** /classification | Delete Classification
[**edit_classification_classification_put**](ClassificationsApi.md#edit_classification_classification_put) | **PUT** /classification | Edit Classification
[**get_classification_classification_post**](ClassificationsApi.md#get_classification_classification_post) | **POST** /classification | Get Classification
[**get_classifications_classifications_post**](ClassificationsApi.md#get_classifications_classifications_post) | **POST** /classifications | Get Classifications


# **create_classification_classification_create_post**
> object create_classification_classification_create_post(classification_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Create Classification

### Example


```python
import odin_sdk
from odin_sdk.models.classification_request import ClassificationRequest
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
    api_instance = odin_sdk.ClassificationsApi(api_client)
    classification_request = odin_sdk.ClassificationRequest() # ClassificationRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Create Classification
        api_response = api_instance.create_classification_classification_create_post(classification_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ClassificationsApi->create_classification_classification_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClassificationsApi->create_classification_classification_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **classification_request** | [**ClassificationRequest**](ClassificationRequest.md)|  | 
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

# **delete_classification_classification_delete**
> DeleteClassificationResponse delete_classification_classification_delete(delete_classification_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Delete Classification

### Example


```python
import odin_sdk
from odin_sdk.models.delete_classification_request import DeleteClassificationRequest
from odin_sdk.models.delete_classification_response import DeleteClassificationResponse
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
    api_instance = odin_sdk.ClassificationsApi(api_client)
    delete_classification_request = odin_sdk.DeleteClassificationRequest() # DeleteClassificationRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Delete Classification
        api_response = api_instance.delete_classification_classification_delete(delete_classification_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ClassificationsApi->delete_classification_classification_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClassificationsApi->delete_classification_classification_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_classification_request** | [**DeleteClassificationRequest**](DeleteClassificationRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**DeleteClassificationResponse**](DeleteClassificationResponse.md)

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

# **edit_classification_classification_put**
> object edit_classification_classification_put(update_classification_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Edit Classification

### Example


```python
import odin_sdk
from odin_sdk.models.update_classification_request import UpdateClassificationRequest
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
    api_instance = odin_sdk.ClassificationsApi(api_client)
    update_classification_request = odin_sdk.UpdateClassificationRequest() # UpdateClassificationRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Edit Classification
        api_response = api_instance.edit_classification_classification_put(update_classification_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ClassificationsApi->edit_classification_classification_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClassificationsApi->edit_classification_classification_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_classification_request** | [**UpdateClassificationRequest**](UpdateClassificationRequest.md)|  | 
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

# **get_classification_classification_post**
> object get_classification_classification_post(get_classification_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Classification

### Example


```python
import odin_sdk
from odin_sdk.models.get_classification_request import GetClassificationRequest
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
    api_instance = odin_sdk.ClassificationsApi(api_client)
    get_classification_request = odin_sdk.GetClassificationRequest() # GetClassificationRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Classification
        api_response = api_instance.get_classification_classification_post(get_classification_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ClassificationsApi->get_classification_classification_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClassificationsApi->get_classification_classification_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_classification_request** | [**GetClassificationRequest**](GetClassificationRequest.md)|  | 
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

# **get_classifications_classifications_post**
> object get_classifications_classifications_post(get_classifications_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Classifications

### Example


```python
import odin_sdk
from odin_sdk.models.get_classifications_request import GetClassificationsRequest
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
    api_instance = odin_sdk.ClassificationsApi(api_client)
    get_classifications_request = odin_sdk.GetClassificationsRequest() # GetClassificationsRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Classifications
        api_response = api_instance.get_classifications_classifications_post(get_classifications_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ClassificationsApi->get_classifications_classifications_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClassificationsApi->get_classifications_classifications_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_classifications_request** | [**GetClassificationsRequest**](GetClassificationsRequest.md)|  | 
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

