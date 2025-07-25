# odin_sdk.AuthenticationApi

All URIs are relative to *http://127.0.0.1:8001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_name_user_name_change_post**](AuthenticationApi.md#change_name_user_name_change_post) | **POST** /user/name/change | Change Name
[**get_api_secret_secret_get**](AuthenticationApi.md#get_api_secret_secret_get) | **GET** /secret | Get Api Secret
[**login_auth_post**](AuthenticationApi.md#login_auth_post) | **POST** /auth | Login


# **change_name_user_name_change_post**
> UserNameChangeResponse change_name_user_name_change_post(user_name_change_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Change Name

### Example


```python
import odin_sdk
from odin_sdk.models.user_name_change_request import UserNameChangeRequest
from odin_sdk.models.user_name_change_response import UserNameChangeResponse
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
    api_instance = odin_sdk.AuthenticationApi(api_client)
    user_name_change_request = odin_sdk.UserNameChangeRequest() # UserNameChangeRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Change Name
        api_response = api_instance.change_name_user_name_change_post(user_name_change_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of AuthenticationApi->change_name_user_name_change_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->change_name_user_name_change_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_name_change_request** | [**UserNameChangeRequest**](UserNameChangeRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**UserNameChangeResponse**](UserNameChangeResponse.md)

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

# **get_api_secret_secret_get**
> GetApiSecretResponse get_api_secret_secret_get(x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Api Secret

Get api secret after token verification

### Example


```python
import odin_sdk
from odin_sdk.models.get_api_secret_response import GetApiSecretResponse
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
    api_instance = odin_sdk.AuthenticationApi(api_client)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Api Secret
        api_response = api_instance.get_api_secret_secret_get(x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of AuthenticationApi->get_api_secret_secret_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->get_api_secret_secret_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**GetApiSecretResponse**](GetApiSecretResponse.md)

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

# **login_auth_post**
> AuthResponse login_auth_post(auth_request)

Login

Authenticates a user with Google

### Example


```python
import odin_sdk
from odin_sdk.models.auth_request import AuthRequest
from odin_sdk.models.auth_response import AuthResponse
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
    api_instance = odin_sdk.AuthenticationApi(api_client)
    auth_request = odin_sdk.AuthRequest() # AuthRequest | 

    try:
        # Login
        api_response = api_instance.login_auth_post(auth_request)
        print("The response of AuthenticationApi->login_auth_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->login_auth_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_request** | [**AuthRequest**](AuthRequest.md)|  | 

### Return type

[**AuthResponse**](AuthResponse.md)

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

