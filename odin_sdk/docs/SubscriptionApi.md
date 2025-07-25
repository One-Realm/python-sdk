# odin_sdk.SubscriptionApi

All URIs are relative to *http://127.0.0.1:8001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_plan_user_cancel_plan_post**](SubscriptionApi.md#cancel_plan_user_cancel_plan_post) | **POST** /user/cancel/plan | Cancel Plan


# **cancel_plan_user_cancel_plan_post**
> object cancel_plan_user_cancel_plan_post(x_api_key=x_api_key, x_api_secret=x_api_secret)

Cancel Plan

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
    api_instance = odin_sdk.SubscriptionApi(api_client)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Cancel Plan
        api_response = api_instance.cancel_plan_user_cancel_plan_post(x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of SubscriptionApi->cancel_plan_user_cancel_plan_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionApi->cancel_plan_user_cancel_plan_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

