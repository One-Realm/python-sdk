# odin_sdk.APIKeysApi

All URIs are relative to *http://127.0.0.1:8001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_api_key_api_keys_key_id_delete**](APIKeysApi.md#delete_api_key_api_keys_key_id_delete) | **DELETE** /api/keys/{key_id} | Delete Api Key
[**generate_new_key_api_keys_post**](APIKeysApi.md#generate_new_key_api_keys_post) | **POST** /api/keys | Generate New Key
[**retrieve_api_keys_api_keys_get**](APIKeysApi.md#retrieve_api_keys_api_keys_get) | **GET** /api/keys | Retrieve Api Keys


# **delete_api_key_api_keys_key_id_delete**
> DeleteApiKeyResponse delete_api_key_api_keys_key_id_delete(key_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Delete Api Key

Remove an active API key.

### Example


```python
import odin_sdk
from odin_sdk.models.delete_api_key_response import DeleteApiKeyResponse
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
    api_instance = odin_sdk.APIKeysApi(api_client)
    key_id = 'key_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Delete Api Key
        api_response = api_instance.delete_api_key_api_keys_key_id_delete(key_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of APIKeysApi->delete_api_key_api_keys_key_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIKeysApi->delete_api_key_api_keys_key_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**DeleteApiKeyResponse**](DeleteApiKeyResponse.md)

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

# **generate_new_key_api_keys_post**
> GenerateApiKeyResponse generate_new_key_api_keys_post(generate_api_key_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Generate New Key

Generate a new API key.

### Example


```python
import odin_sdk
from odin_sdk.models.generate_api_key_request import GenerateApiKeyRequest
from odin_sdk.models.generate_api_key_response import GenerateApiKeyResponse
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
    api_instance = odin_sdk.APIKeysApi(api_client)
    generate_api_key_request = odin_sdk.GenerateApiKeyRequest() # GenerateApiKeyRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Generate New Key
        api_response = api_instance.generate_new_key_api_keys_post(generate_api_key_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of APIKeysApi->generate_new_key_api_keys_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIKeysApi->generate_new_key_api_keys_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_api_key_request** | [**GenerateApiKeyRequest**](GenerateApiKeyRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**GenerateApiKeyResponse**](GenerateApiKeyResponse.md)

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

# **retrieve_api_keys_api_keys_get**
> GetApiKeysResponse retrieve_api_keys_api_keys_get(x_api_key=x_api_key, x_api_secret=x_api_secret)

Retrieve Api Keys

Retrieve the API key.

### Example


```python
import odin_sdk
from odin_sdk.models.get_api_keys_response import GetApiKeysResponse
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
    api_instance = odin_sdk.APIKeysApi(api_client)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Retrieve Api Keys
        api_response = api_instance.retrieve_api_keys_api_keys_get(x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of APIKeysApi->retrieve_api_keys_api_keys_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIKeysApi->retrieve_api_keys_api_keys_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**GetApiKeysResponse**](GetApiKeysResponse.md)

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

