# odin_sdk.TeamPermissionsApi

All URIs are relative to *http://127.0.0.1:8001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_user_permission_teams_team_id_users_user_id_permissions_permission_get**](TeamPermissionsApi.md#check_user_permission_teams_team_id_users_user_id_permissions_permission_get) | **GET** /teams/{team_id}/users/{user_id}/permissions/{permission} | Check User Permission
[**get_team_role_permissions_teams_team_id_role_permissions_get**](TeamPermissionsApi.md#get_team_role_permissions_teams_team_id_role_permissions_get) | **GET** /teams/{team_id}/role-permissions | Get Team Role Permissions
[**get_user_permissions_teams_team_id_users_user_id_permissions_get**](TeamPermissionsApi.md#get_user_permissions_teams_team_id_users_user_id_permissions_get) | **GET** /teams/{team_id}/users/{user_id}/permissions | Get User Permissions
[**initialize_team_permissions_teams_team_id_initialize_permissions_post**](TeamPermissionsApi.md#initialize_team_permissions_teams_team_id_initialize_permissions_post) | **POST** /teams/{team_id}/initialize-permissions | Initialize Team Permissions
[**update_team_role_permissions_teams_team_id_role_permissions_put**](TeamPermissionsApi.md#update_team_role_permissions_teams_team_id_role_permissions_put) | **PUT** /teams/{team_id}/role-permissions | Update Team Role Permissions


# **check_user_permission_teams_team_id_users_user_id_permissions_permission_get**
> CheckPermissionResponse check_user_permission_teams_team_id_users_user_id_permissions_permission_get(team_id, user_id, permission, x_api_key=x_api_key, x_api_secret=x_api_secret)

Check User Permission

Check if a user has a specific permission

### Example


```python
import odin_sdk
from odin_sdk.models.check_permission_response import CheckPermissionResponse
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
    api_instance = odin_sdk.TeamPermissionsApi(api_client)
    team_id = 'team_id_example' # str | 
    user_id = 'user_id_example' # str | 
    permission = 'permission_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Check User Permission
        api_response = api_instance.check_user_permission_teams_team_id_users_user_id_permissions_permission_get(team_id, user_id, permission, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of TeamPermissionsApi->check_user_permission_teams_team_id_users_user_id_permissions_permission_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamPermissionsApi->check_user_permission_teams_team_id_users_user_id_permissions_permission_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**|  | 
 **user_id** | **str**|  | 
 **permission** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**CheckPermissionResponse**](CheckPermissionResponse.md)

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

# **get_team_role_permissions_teams_team_id_role_permissions_get**
> GetTeamRolePermissionsResponse get_team_role_permissions_teams_team_id_role_permissions_get(team_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Team Role Permissions

Get all role permissions for a team

### Example


```python
import odin_sdk
from odin_sdk.models.get_team_role_permissions_response import GetTeamRolePermissionsResponse
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
    api_instance = odin_sdk.TeamPermissionsApi(api_client)
    team_id = 'team_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Team Role Permissions
        api_response = api_instance.get_team_role_permissions_teams_team_id_role_permissions_get(team_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of TeamPermissionsApi->get_team_role_permissions_teams_team_id_role_permissions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamPermissionsApi->get_team_role_permissions_teams_team_id_role_permissions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**GetTeamRolePermissionsResponse**](GetTeamRolePermissionsResponse.md)

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

# **get_user_permissions_teams_team_id_users_user_id_permissions_get**
> object get_user_permissions_teams_team_id_users_user_id_permissions_get(team_id, user_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get User Permissions

Get all permissions for a user

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
    api_instance = odin_sdk.TeamPermissionsApi(api_client)
    team_id = 'team_id_example' # str | 
    user_id = 'user_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get User Permissions
        api_response = api_instance.get_user_permissions_teams_team_id_users_user_id_permissions_get(team_id, user_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of TeamPermissionsApi->get_user_permissions_teams_team_id_users_user_id_permissions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamPermissionsApi->get_user_permissions_teams_team_id_users_user_id_permissions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**|  | 
 **user_id** | **str**|  | 
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

# **initialize_team_permissions_teams_team_id_initialize_permissions_post**
> object initialize_team_permissions_teams_team_id_initialize_permissions_post(team_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Initialize Team Permissions

Initialize default permissions for a team (admin only)

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
    api_instance = odin_sdk.TeamPermissionsApi(api_client)
    team_id = 'team_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Initialize Team Permissions
        api_response = api_instance.initialize_team_permissions_teams_team_id_initialize_permissions_post(team_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of TeamPermissionsApi->initialize_team_permissions_teams_team_id_initialize_permissions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamPermissionsApi->initialize_team_permissions_teams_team_id_initialize_permissions_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**|  | 
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

# **update_team_role_permissions_teams_team_id_role_permissions_put**
> UpdateRolePermissionsResponse update_team_role_permissions_teams_team_id_role_permissions_put(team_id, update_role_permissions_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Update Team Role Permissions

Update role permissions for a team

### Example


```python
import odin_sdk
from odin_sdk.models.update_role_permissions_request import UpdateRolePermissionsRequest
from odin_sdk.models.update_role_permissions_response import UpdateRolePermissionsResponse
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
    api_instance = odin_sdk.TeamPermissionsApi(api_client)
    team_id = 'team_id_example' # str | 
    update_role_permissions_request = odin_sdk.UpdateRolePermissionsRequest() # UpdateRolePermissionsRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Update Team Role Permissions
        api_response = api_instance.update_team_role_permissions_teams_team_id_role_permissions_put(team_id, update_role_permissions_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of TeamPermissionsApi->update_team_role_permissions_teams_team_id_role_permissions_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamPermissionsApi->update_team_role_permissions_teams_team_id_role_permissions_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**|  | 
 **update_role_permissions_request** | [**UpdateRolePermissionsRequest**](UpdateRolePermissionsRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**UpdateRolePermissionsResponse**](UpdateRolePermissionsResponse.md)

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

