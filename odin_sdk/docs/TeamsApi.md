# odin_sdk.TeamsApi

All URIs are relative to *http://127.0.0.1:8001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_team_tag_v1_users_team_tags_add_post**](TeamsApi.md#add_team_tag_v1_users_team_tags_add_post) | **POST** /v1/users/team/tags/add | Add Team Tag
[**export_team_members_team_members_export_get**](TeamsApi.md#export_team_members_team_members_export_get) | **GET** /team/members/export | Export Team Members
[**get_available_team_tags_v1_users_team_tags_available_get**](TeamsApi.md#get_available_team_tags_v1_users_team_tags_available_get) | **GET** /v1/users/team/tags/available | Get Available Team Tags
[**get_team_tags_v1_users_team_tags_get**](TeamsApi.md#get_team_tags_v1_users_team_tags_get) | **GET** /v1/users/team/tags | Get Team Tags
[**get_team_users_team_members_get**](TeamsApi.md#get_team_users_team_members_get) | **GET** /team/members | Get Team Users
[**remove_team_tag_v1_users_team_tags_remove_post**](TeamsApi.md#remove_team_tag_v1_users_team_tags_remove_post) | **POST** /v1/users/team/tags/remove | Remove Team Tag
[**update_team_tags_v1_users_team_tags_post**](TeamsApi.md#update_team_tags_v1_users_team_tags_post) | **POST** /v1/users/team/tags | Update Team Tags


# **add_team_tag_v1_users_team_tags_add_post**
> TeamTagResponse add_team_tag_v1_users_team_tags_add_post(single_tag_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Add Team Tag

Add a single tag to the team (only team admins can do this)

### Example


```python
import odin_sdk
from odin_sdk.models.single_tag_request import SingleTagRequest
from odin_sdk.models.team_tag_response import TeamTagResponse
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
    api_instance = odin_sdk.TeamsApi(api_client)
    single_tag_request = odin_sdk.SingleTagRequest() # SingleTagRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Add Team Tag
        api_response = api_instance.add_team_tag_v1_users_team_tags_add_post(single_tag_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of TeamsApi->add_team_tag_v1_users_team_tags_add_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->add_team_tag_v1_users_team_tags_add_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **single_tag_request** | [**SingleTagRequest**](SingleTagRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**TeamTagResponse**](TeamTagResponse.md)

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

# **export_team_members_team_members_export_get**
> export_team_members_team_members_export_get(x_api_key=x_api_key, x_api_secret=x_api_secret)

Export Team Members

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
    api_instance = odin_sdk.TeamsApi(api_client)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Export Team Members
        api_instance.export_team_members_team_members_export_get(x_api_key=x_api_key, x_api_secret=x_api_secret)
    except Exception as e:
        print("Exception when calling TeamsApi->export_team_members_team_members_export_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

void (empty response body)

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

# **get_available_team_tags_v1_users_team_tags_available_get**
> List[Optional[str]] get_available_team_tags_v1_users_team_tags_available_get(x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Available Team Tags

Get available tags for the user's team (same as get_team_tags)

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
    api_instance = odin_sdk.TeamsApi(api_client)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Available Team Tags
        api_response = api_instance.get_available_team_tags_v1_users_team_tags_available_get(x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of TeamsApi->get_available_team_tags_v1_users_team_tags_available_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->get_available_team_tags_v1_users_team_tags_available_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

**List[Optional[str]]**

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

# **get_team_tags_v1_users_team_tags_get**
> List[Optional[str]] get_team_tags_v1_users_team_tags_get(x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Team Tags

Get all tags defined for the user's team

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
    api_instance = odin_sdk.TeamsApi(api_client)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Team Tags
        api_response = api_instance.get_team_tags_v1_users_team_tags_get(x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of TeamsApi->get_team_tags_v1_users_team_tags_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->get_team_tags_v1_users_team_tags_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

**List[Optional[str]]**

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

# **get_team_users_team_members_get**
> MembersResponse get_team_users_team_members_get(x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Team Users

### Example


```python
import odin_sdk
from odin_sdk.models.members_response import MembersResponse
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
    api_instance = odin_sdk.TeamsApi(api_client)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Team Users
        api_response = api_instance.get_team_users_team_members_get(x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of TeamsApi->get_team_users_team_members_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->get_team_users_team_members_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**MembersResponse**](MembersResponse.md)

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

# **remove_team_tag_v1_users_team_tags_remove_post**
> TeamTagResponse remove_team_tag_v1_users_team_tags_remove_post(single_tag_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Remove Team Tag

Remove a single tag from the team (only team admins can do this)

### Example


```python
import odin_sdk
from odin_sdk.models.single_tag_request import SingleTagRequest
from odin_sdk.models.team_tag_response import TeamTagResponse
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
    api_instance = odin_sdk.TeamsApi(api_client)
    single_tag_request = odin_sdk.SingleTagRequest() # SingleTagRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Remove Team Tag
        api_response = api_instance.remove_team_tag_v1_users_team_tags_remove_post(single_tag_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of TeamsApi->remove_team_tag_v1_users_team_tags_remove_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->remove_team_tag_v1_users_team_tags_remove_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **single_tag_request** | [**SingleTagRequest**](SingleTagRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**TeamTagResponse**](TeamTagResponse.md)

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

# **update_team_tags_v1_users_team_tags_post**
> TeamTagResponse update_team_tags_v1_users_team_tags_post(team_tag_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Update Team Tags

Update team tags (replace all tags - only team admins can do this)

### Example


```python
import odin_sdk
from odin_sdk.models.team_tag_request import TeamTagRequest
from odin_sdk.models.team_tag_response import TeamTagResponse
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
    api_instance = odin_sdk.TeamsApi(api_client)
    team_tag_request = odin_sdk.TeamTagRequest() # TeamTagRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Update Team Tags
        api_response = api_instance.update_team_tags_v1_users_team_tags_post(team_tag_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of TeamsApi->update_team_tags_v1_users_team_tags_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->update_team_tags_v1_users_team_tags_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_tag_request** | [**TeamTagRequest**](TeamTagRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**TeamTagResponse**](TeamTagResponse.md)

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

