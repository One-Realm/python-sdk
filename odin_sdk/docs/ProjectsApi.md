# odin_sdk.ProjectsApi

All URIs are relative to *http://127.0.0.1:8001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user_to_project_project_user_add_post**](ProjectsApi.md#add_user_to_project_project_user_add_post) | **POST** /project/user/add | Add User To Project
[**create_project_project_create_post**](ProjectsApi.md#create_project_project_create_post) | **POST** /project/create | Create Project
[**edit_project_user_project_user_edit_post**](ProjectsApi.md#edit_project_user_project_user_edit_post) | **POST** /project/user/edit | Edit Project User
[**get_project_members_project_project_id_members_get**](ProjectsApi.md#get_project_members_project_project_id_members_get) | **GET** /project/{project_id}/members | Get Project Members
[**get_projects_projects_get**](ProjectsApi.md#get_projects_projects_get) | **GET** /projects | Get Projects
[**update_project_project_update_post**](ProjectsApi.md#update_project_project_update_post) | **POST** /project/update | Update Project


# **add_user_to_project_project_user_add_post**
> AddUserToProjectResponse add_user_to_project_project_user_add_post(add_user_to_project_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Add User To Project

Adding users to a Project.

### Example


```python
import odin_sdk
from odin_sdk.models.add_user_to_project_request import AddUserToProjectRequest
from odin_sdk.models.add_user_to_project_response import AddUserToProjectResponse
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
    api_instance = odin_sdk.ProjectsApi(api_client)
    add_user_to_project_request = odin_sdk.AddUserToProjectRequest() # AddUserToProjectRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Add User To Project
        api_response = api_instance.add_user_to_project_project_user_add_post(add_user_to_project_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ProjectsApi->add_user_to_project_project_user_add_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->add_user_to_project_project_user_add_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_user_to_project_request** | [**AddUserToProjectRequest**](AddUserToProjectRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**AddUserToProjectResponse**](AddUserToProjectResponse.md)

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

# **create_project_project_create_post**
> CreateProjectResponse create_project_project_create_post(create_project_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Create Project

Creating a new project

### Example


```python
import odin_sdk
from odin_sdk.models.create_project_request import CreateProjectRequest
from odin_sdk.models.create_project_response import CreateProjectResponse
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
    api_instance = odin_sdk.ProjectsApi(api_client)
    create_project_request = odin_sdk.CreateProjectRequest() # CreateProjectRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Create Project
        api_response = api_instance.create_project_project_create_post(create_project_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ProjectsApi->create_project_project_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->create_project_project_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_project_request** | [**CreateProjectRequest**](CreateProjectRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**CreateProjectResponse**](CreateProjectResponse.md)

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

# **edit_project_user_project_user_edit_post**
> EditProjectResponse edit_project_user_project_user_edit_post(edit_project_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Edit Project User

Lets you edit the users that are added to the Projects

### Example


```python
import odin_sdk
from odin_sdk.models.edit_project_request import EditProjectRequest
from odin_sdk.models.edit_project_response import EditProjectResponse
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
    api_instance = odin_sdk.ProjectsApi(api_client)
    edit_project_request = odin_sdk.EditProjectRequest() # EditProjectRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Edit Project User
        api_response = api_instance.edit_project_user_project_user_edit_post(edit_project_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ProjectsApi->edit_project_user_project_user_edit_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->edit_project_user_project_user_edit_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edit_project_request** | [**EditProjectRequest**](EditProjectRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**EditProjectResponse**](EditProjectResponse.md)

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

# **get_project_members_project_project_id_members_get**
> GetProjectMembersResponse get_project_members_project_project_id_members_get(project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Project Members

### Example


```python
import odin_sdk
from odin_sdk.models.get_project_members_response import GetProjectMembersResponse
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
    api_instance = odin_sdk.ProjectsApi(api_client)
    project_id = 'project_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Project Members
        api_response = api_instance.get_project_members_project_project_id_members_get(project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ProjectsApi->get_project_members_project_project_id_members_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_project_members_project_project_id_members_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**GetProjectMembersResponse**](GetProjectMembersResponse.md)

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

# **get_projects_projects_get**
> GetAllProjectsResponse get_projects_projects_get(limit=limit, offset=offset, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Projects

Get all the Projects.

### Example


```python
import odin_sdk
from odin_sdk.models.get_all_projects_response import GetAllProjectsResponse
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
    api_instance = odin_sdk.ProjectsApi(api_client)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Projects
        api_response = api_instance.get_projects_projects_get(limit=limit, offset=offset, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ProjectsApi->get_projects_projects_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_projects_projects_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**GetAllProjectsResponse**](GetAllProjectsResponse.md)

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

# **update_project_project_update_post**
> UpdateProjectResponse update_project_project_update_post(update_project_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Update Project

Make updates to the Project

### Example


```python
import odin_sdk
from odin_sdk.models.update_project_request import UpdateProjectRequest
from odin_sdk.models.update_project_response import UpdateProjectResponse
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
    api_instance = odin_sdk.ProjectsApi(api_client)
    update_project_request = odin_sdk.UpdateProjectRequest() # UpdateProjectRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Update Project
        api_response = api_instance.update_project_project_update_post(update_project_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ProjectsApi->update_project_project_update_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->update_project_project_update_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_project_request** | [**UpdateProjectRequest**](UpdateProjectRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**UpdateProjectResponse**](UpdateProjectResponse.md)

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

