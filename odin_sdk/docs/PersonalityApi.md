# odin_sdk.PersonalityApi

All URIs are relative to *http://127.0.0.1:8001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_personality_personality_add_post**](PersonalityApi.md#add_personality_personality_add_post) | **POST** /personality/add | Add Personality
[**delete_personality_personality_delete_delete**](PersonalityApi.md#delete_personality_personality_delete_delete) | **DELETE** /personality/delete | Delete Personality
[**get_all_personalities_personality_all_project_id_get**](PersonalityApi.md#get_all_personalities_personality_all_project_id_get) | **GET** /personality/all/{project_id} | Get All Personalities
[**select_personality_personality_select_post**](PersonalityApi.md#select_personality_personality_select_post) | **POST** /personality/select | Select Personality
[**update_personality_personality_update_post**](PersonalityApi.md#update_personality_personality_update_post) | **POST** /personality/update | Update Personality


# **add_personality_personality_add_post**
> AddPersonalityResponse add_personality_personality_add_post(add_personality_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Add Personality

Incorporate a distinct personality to the model.

### Example


```python
import odin_sdk
from odin_sdk.models.add_personality_request import AddPersonalityRequest
from odin_sdk.models.add_personality_response import AddPersonalityResponse
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
    api_instance = odin_sdk.PersonalityApi(api_client)
    add_personality_request = odin_sdk.AddPersonalityRequest() # AddPersonalityRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Add Personality
        api_response = api_instance.add_personality_personality_add_post(add_personality_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of PersonalityApi->add_personality_personality_add_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonalityApi->add_personality_personality_add_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_personality_request** | [**AddPersonalityRequest**](AddPersonalityRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**AddPersonalityResponse**](AddPersonalityResponse.md)

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

# **delete_personality_personality_delete_delete**
> DeletePersonalityResponse delete_personality_personality_delete_delete(delete_personality_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Delete Personality

Remove an existing personality.

### Example


```python
import odin_sdk
from odin_sdk.models.delete_personality_request import DeletePersonalityRequest
from odin_sdk.models.delete_personality_response import DeletePersonalityResponse
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
    api_instance = odin_sdk.PersonalityApi(api_client)
    delete_personality_request = odin_sdk.DeletePersonalityRequest() # DeletePersonalityRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Delete Personality
        api_response = api_instance.delete_personality_personality_delete_delete(delete_personality_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of PersonalityApi->delete_personality_personality_delete_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonalityApi->delete_personality_personality_delete_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_personality_request** | [**DeletePersonalityRequest**](DeletePersonalityRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**DeletePersonalityResponse**](DeletePersonalityResponse.md)

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

# **get_all_personalities_personality_all_project_id_get**
> GetAllPersonalitiesResponse get_all_personalities_personality_all_project_id_get(project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get All Personalities

Retrieve all personalities associated with the project.

### Example


```python
import odin_sdk
from odin_sdk.models.get_all_personalities_response import GetAllPersonalitiesResponse
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
    api_instance = odin_sdk.PersonalityApi(api_client)
    project_id = 'project_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get All Personalities
        api_response = api_instance.get_all_personalities_personality_all_project_id_get(project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of PersonalityApi->get_all_personalities_personality_all_project_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonalityApi->get_all_personalities_personality_all_project_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**GetAllPersonalitiesResponse**](GetAllPersonalitiesResponse.md)

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

# **select_personality_personality_select_post**
> SelectPersonalityResponse select_personality_personality_select_post(select_personality_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Select Personality

Choose a specific personality.

### Example


```python
import odin_sdk
from odin_sdk.models.select_personality_request import SelectPersonalityRequest
from odin_sdk.models.select_personality_response import SelectPersonalityResponse
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
    api_instance = odin_sdk.PersonalityApi(api_client)
    select_personality_request = odin_sdk.SelectPersonalityRequest() # SelectPersonalityRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Select Personality
        api_response = api_instance.select_personality_personality_select_post(select_personality_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of PersonalityApi->select_personality_personality_select_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonalityApi->select_personality_personality_select_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **select_personality_request** | [**SelectPersonalityRequest**](SelectPersonalityRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**SelectPersonalityResponse**](SelectPersonalityResponse.md)

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

# **update_personality_personality_update_post**
> UpdatePersonalityResponse update_personality_personality_update_post(update_personality_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Update Personality

Modify existing personalities.

### Example


```python
import odin_sdk
from odin_sdk.models.update_personality_request import UpdatePersonalityRequest
from odin_sdk.models.update_personality_response import UpdatePersonalityResponse
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
    api_instance = odin_sdk.PersonalityApi(api_client)
    update_personality_request = odin_sdk.UpdatePersonalityRequest() # UpdatePersonalityRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Update Personality
        api_response = api_instance.update_personality_personality_update_post(update_personality_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of PersonalityApi->update_personality_personality_update_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonalityApi->update_personality_personality_update_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_personality_request** | [**UpdatePersonalityRequest**](UpdatePersonalityRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**UpdatePersonalityResponse**](UpdatePersonalityResponse.md)

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

