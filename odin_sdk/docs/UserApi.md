# odin_sdk.UserApi

All URIs are relative to *http://127.0.0.1:8001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**complete_user_onboarding_user_onboarding_complete_post**](UserApi.md#complete_user_onboarding_user_onboarding_complete_post) | **POST** /user/onboarding/complete | Complete User Onboarding
[**get_onboarding_team_info_user_onboarding_team_info_get**](UserApi.md#get_onboarding_team_info_user_onboarding_team_info_get) | **GET** /user/onboarding/team-info | Get Onboarding Team Info
[**update_user_params_user_info_update_put**](UserApi.md#update_user_params_user_info_update_put) | **PUT** /user/info/update | Update User Params


# **complete_user_onboarding_user_onboarding_complete_post**
> UpdateUserOnboardingResponse complete_user_onboarding_user_onboarding_complete_post(update_user_onboarding_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Complete User Onboarding

Complete user onboarding and update profile with collected information

### Example


```python
import odin_sdk
from odin_sdk.models.update_user_onboarding_request import UpdateUserOnboardingRequest
from odin_sdk.models.update_user_onboarding_response import UpdateUserOnboardingResponse
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
    api_instance = odin_sdk.UserApi(api_client)
    update_user_onboarding_request = odin_sdk.UpdateUserOnboardingRequest() # UpdateUserOnboardingRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Complete User Onboarding
        api_response = api_instance.complete_user_onboarding_user_onboarding_complete_post(update_user_onboarding_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of UserApi->complete_user_onboarding_user_onboarding_complete_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->complete_user_onboarding_user_onboarding_complete_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_user_onboarding_request** | [**UpdateUserOnboardingRequest**](UpdateUserOnboardingRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**UpdateUserOnboardingResponse**](UpdateUserOnboardingResponse.md)

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

# **get_onboarding_team_info_user_onboarding_team_info_get**
> OnboardingTeamInfoResponse get_onboarding_team_info_user_onboarding_team_info_get(x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Onboarding Team Info

Get team information for onboarding prefill purposes.

### Example


```python
import odin_sdk
from odin_sdk.models.onboarding_team_info_response import OnboardingTeamInfoResponse
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
    api_instance = odin_sdk.UserApi(api_client)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Onboarding Team Info
        api_response = api_instance.get_onboarding_team_info_user_onboarding_team_info_get(x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of UserApi->get_onboarding_team_info_user_onboarding_team_info_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_onboarding_team_info_user_onboarding_team_info_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**OnboardingTeamInfoResponse**](OnboardingTeamInfoResponse.md)

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

# **update_user_params_user_info_update_put**
> UpdateUserResponse update_user_params_user_info_update_put(update_user_info, x_api_key=x_api_key, x_api_secret=x_api_secret)

Update User Params

### Example


```python
import odin_sdk
from odin_sdk.models.update_user_info import UpdateUserInfo
from odin_sdk.models.update_user_response import UpdateUserResponse
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
    api_instance = odin_sdk.UserApi(api_client)
    update_user_info = odin_sdk.UpdateUserInfo() # UpdateUserInfo | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Update User Params
        api_response = api_instance.update_user_params_user_info_update_put(update_user_info, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of UserApi->update_user_params_user_info_update_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->update_user_params_user_info_update_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_user_info** | [**UpdateUserInfo**](UpdateUserInfo.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**UpdateUserResponse**](UpdateUserResponse.md)

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

