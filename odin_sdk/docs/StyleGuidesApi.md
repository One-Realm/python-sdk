# odin_sdk.StyleGuidesApi

All URIs are relative to *http://127.0.0.1:8001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_style_guide_style_guide_apply_post**](StyleGuidesApi.md#get_style_guide_style_guide_apply_post) | **POST** /style_guide/apply | Get Style Guide


# **get_style_guide_style_guide_apply_post**
> object get_style_guide_style_guide_apply_post(apply_style_guide_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Style Guide

### Example


```python
import odin_sdk
from odin_sdk.models.apply_style_guide_request import ApplyStyleGuideRequest
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
    api_instance = odin_sdk.StyleGuidesApi(api_client)
    apply_style_guide_request = odin_sdk.ApplyStyleGuideRequest() # ApplyStyleGuideRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Style Guide
        api_response = api_instance.get_style_guide_style_guide_apply_post(apply_style_guide_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of StyleGuidesApi->get_style_guide_style_guide_apply_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StyleGuidesApi->get_style_guide_style_guide_apply_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apply_style_guide_request** | [**ApplyStyleGuideRequest**](ApplyStyleGuideRequest.md)|  | 
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

