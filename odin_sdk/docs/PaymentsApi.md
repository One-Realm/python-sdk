# odin_sdk.PaymentsApi

All URIs are relative to *http://127.0.0.1:8001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**modify_seats_user_team_modify_seats_post**](PaymentsApi.md#modify_seats_user_team_modify_seats_post) | **POST** /user/team/modify/seats | Modify Seats


# **modify_seats_user_team_modify_seats_post**
> PurchaseSeatsResponse modify_seats_user_team_modify_seats_post(purchase_seats_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Modify Seats

Purchase additional seats for the organization

### Example


```python
import odin_sdk
from odin_sdk.models.purchase_seats_request import PurchaseSeatsRequest
from odin_sdk.models.purchase_seats_response import PurchaseSeatsResponse
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
    api_instance = odin_sdk.PaymentsApi(api_client)
    purchase_seats_request = odin_sdk.PurchaseSeatsRequest() # PurchaseSeatsRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Modify Seats
        api_response = api_instance.modify_seats_user_team_modify_seats_post(purchase_seats_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of PaymentsApi->modify_seats_user_team_modify_seats_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->modify_seats_user_team_modify_seats_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **purchase_seats_request** | [**PurchaseSeatsRequest**](PurchaseSeatsRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**PurchaseSeatsResponse**](PurchaseSeatsResponse.md)

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

