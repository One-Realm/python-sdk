# odin_sdk.RolesApi

All URIs are relative to *http://127.0.0.1:8001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_default_roles_project_project_id_default_roles_post**](RolesApi.md#create_default_roles_project_project_id_default_roles_post) | **POST** /project/{project_id}/default_roles | Create Default Roles
[**create_role_project_project_id_roles_post**](RolesApi.md#create_role_project_project_id_roles_post) | **POST** /project/{project_id}/roles | Create Role
[**delete_role_project_project_id_roles_role_id_delete**](RolesApi.md#delete_role_project_project_id_roles_role_id_delete) | **DELETE** /project/{project_id}/roles/{role_id} | Delete Role
[**get_all_role_ids_project_project_id_roles_get**](RolesApi.md#get_all_role_ids_project_project_id_roles_get) | **GET** /project/{project_id}/roles | Get All Role Ids
[**get_role_project_project_id_roles_role_id_get**](RolesApi.md#get_role_project_project_id_roles_role_id_get) | **GET** /project/{project_id}/roles/{role_id} | Get Role
[**update_role_project_project_id_roles_role_id_post**](RolesApi.md#update_role_project_project_id_roles_role_id_post) | **POST** /project/{project_id}/roles/{role_id} | Update Role


# **create_default_roles_project_project_id_default_roles_post**
> GetAllRoleNamesResponse create_default_roles_project_project_id_default_roles_post(project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Create Default Roles

Creates default roles

### Example


```python
import odin_sdk
from odin_sdk.models.get_all_role_names_response import GetAllRoleNamesResponse
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
    api_instance = odin_sdk.RolesApi(api_client)
    project_id = 'project_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Create Default Roles
        api_response = api_instance.create_default_roles_project_project_id_default_roles_post(project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of RolesApi->create_default_roles_project_project_id_default_roles_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->create_default_roles_project_project_id_default_roles_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**GetAllRoleNamesResponse**](GetAllRoleNamesResponse.md)

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

# **create_role_project_project_id_roles_post**
> CreateRoleResponse create_role_project_project_id_roles_post(project_id, create_role_request, sent_internally=sent_internally, x_api_key=x_api_key, x_api_secret=x_api_secret)

Create Role

Create a new role for a project

### Example


```python
import odin_sdk
from odin_sdk.models.create_role_request import CreateRoleRequest
from odin_sdk.models.create_role_response import CreateRoleResponse
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
    api_instance = odin_sdk.RolesApi(api_client)
    project_id = 'project_id_example' # str | 
    create_role_request = odin_sdk.CreateRoleRequest() # CreateRoleRequest | 
    sent_internally = False # bool |  (optional) (default to False)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Create Role
        api_response = api_instance.create_role_project_project_id_roles_post(project_id, create_role_request, sent_internally=sent_internally, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of RolesApi->create_role_project_project_id_roles_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->create_role_project_project_id_roles_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **create_role_request** | [**CreateRoleRequest**](CreateRoleRequest.md)|  | 
 **sent_internally** | **bool**|  | [optional] [default to False]
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**CreateRoleResponse**](CreateRoleResponse.md)

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

# **delete_role_project_project_id_roles_role_id_delete**
> object delete_role_project_project_id_roles_role_id_delete(project_id, role_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Delete Role

Delete the role by name.

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
    api_instance = odin_sdk.RolesApi(api_client)
    project_id = 'project_id_example' # str | 
    role_id = 'role_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Delete Role
        api_response = api_instance.delete_role_project_project_id_roles_role_id_delete(project_id, role_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of RolesApi->delete_role_project_project_id_roles_role_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->delete_role_project_project_id_roles_role_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **role_id** | **str**|  | 
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

# **get_all_role_ids_project_project_id_roles_get**
> GetAllRoleNamesResponse get_all_role_ids_project_project_id_roles_get(project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get All Role Ids

Get all role names

### Example


```python
import odin_sdk
from odin_sdk.models.get_all_role_names_response import GetAllRoleNamesResponse
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
    api_instance = odin_sdk.RolesApi(api_client)
    project_id = 'project_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get All Role Ids
        api_response = api_instance.get_all_role_ids_project_project_id_roles_get(project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of RolesApi->get_all_role_ids_project_project_id_roles_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->get_all_role_ids_project_project_id_roles_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**GetAllRoleNamesResponse**](GetAllRoleNamesResponse.md)

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

# **get_role_project_project_id_roles_role_id_get**
> GetRoleResponse get_role_project_project_id_roles_role_id_get(project_id, role_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Role

Get the role by name.

### Example


```python
import odin_sdk
from odin_sdk.models.get_role_response import GetRoleResponse
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
    api_instance = odin_sdk.RolesApi(api_client)
    project_id = 'project_id_example' # str | 
    role_id = 'role_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Role
        api_response = api_instance.get_role_project_project_id_roles_role_id_get(project_id, role_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of RolesApi->get_role_project_project_id_roles_role_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->get_role_project_project_id_roles_role_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **role_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**GetRoleResponse**](GetRoleResponse.md)

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

# **update_role_project_project_id_roles_role_id_post**
> CreateRoleResponse update_role_project_project_id_roles_role_id_post(project_id, role_id, update_rules_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Update Role

Update the role by Id.

### Example


```python
import odin_sdk
from odin_sdk.models.create_role_response import CreateRoleResponse
from odin_sdk.models.update_rules_request import UpdateRulesRequest
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
    api_instance = odin_sdk.RolesApi(api_client)
    project_id = 'project_id_example' # str | 
    role_id = 'role_id_example' # str | 
    update_rules_request = odin_sdk.UpdateRulesRequest() # UpdateRulesRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Update Role
        api_response = api_instance.update_role_project_project_id_roles_role_id_post(project_id, role_id, update_rules_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of RolesApi->update_role_project_project_id_roles_role_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->update_role_project_project_id_roles_role_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **role_id** | **str**|  | 
 **update_rules_request** | [**UpdateRulesRequest**](UpdateRulesRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**CreateRoleResponse**](CreateRoleResponse.md)

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

