# odin_sdk.AdminApi

All URIs are relative to *http://127.0.0.1:8001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clone_project_admin_projects_clone_post**](AdminApi.md#clone_project_admin_projects_clone_post) | **POST** /admin/projects/clone | Clone Project
[**create_app_license_admin_app_licenses_post**](AdminApi.md#create_app_license_admin_app_licenses_post) | **POST** /admin/app_licenses | Create App License
[**create_model_admin_models_post**](AdminApi.md#create_model_admin_models_post) | **POST** /admin/models | Create Model
[**create_team_admin_teams_create_post**](AdminApi.md#create_team_admin_teams_create_post) | **POST** /admin/teams/create | Create Team
[**delete_model_admin_models_model_id_delete**](AdminApi.md#delete_model_admin_models_model_id_delete) | **DELETE** /admin/models/{model_id} | Delete Model
[**delete_team_admin_teams_delete_delete**](AdminApi.md#delete_team_admin_teams_delete_delete) | **DELETE** /admin/teams/delete | Delete Team
[**evaluate_citation_admin_evaluate_citation_post**](AdminApi.md#evaluate_citation_admin_evaluate_citation_post) | **POST** /admin/evaluate/citation | Evaluate Citation
[**evaluate_retrieval_admin_evaluate_retrieval_post**](AdminApi.md#evaluate_retrieval_admin_evaluate_retrieval_post) | **POST** /admin/evaluate/retrieval | Evaluate Retrieval
[**generate_password_reset_admin_password_reset_user_identifier_post**](AdminApi.md#generate_password_reset_admin_password_reset_user_identifier_post) | **POST** /admin/password-reset/{user_identifier} | Generate Password Reset
[**get_active_tasks_endpoint_admin_celery_active_tasks_get**](AdminApi.md#get_active_tasks_endpoint_admin_celery_active_tasks_get) | **GET** /admin/celery/active-tasks | Get Active Tasks Endpoint
[**get_agents_count_by_project_endpoint_admin_agents_count_by_project_get**](AdminApi.md#get_agents_count_by_project_endpoint_admin_agents_count_by_project_get) | **GET** /admin/agents/count-by-project | Get Agents Count By Project Endpoint
[**get_app_license_admin_app_licenses_license_id_get**](AdminApi.md#get_app_license_admin_app_licenses_license_id_get) | **GET** /admin/app_licenses/{license_id} | Get App License
[**get_evaluation_tasks_admin_evaluation_tasks_get**](AdminApi.md#get_evaluation_tasks_admin_evaluation_tasks_get) | **GET** /admin/evaluation/tasks | Get Evaluation Tasks
[**get_knowledge_base_files_admin_knowledge_get**](AdminApi.md#get_knowledge_base_files_admin_knowledge_get) | **GET** /admin/knowledge | Get Knowledge Base Files
[**get_model_admin_models_model_id_get**](AdminApi.md#get_model_admin_models_model_id_get) | **GET** /admin/models/{model_id} | Get Model
[**get_onprem_token_admin_onprem_token_license_key_get**](AdminApi.md#get_onprem_token_admin_onprem_token_license_key_get) | **GET** /admin/onprem-token/{license_key} | Get Onprem Token
[**get_project_details_admin_projects_project_id_get**](AdminApi.md#get_project_details_admin_projects_project_id_get) | **GET** /admin/projects/{project_id} | Get Project Details
[**get_stats_admin_stats_get**](AdminApi.md#get_stats_admin_stats_get) | **GET** /admin/stats | Get Stats
[**get_task_info_admin_celery_task_task_id_get**](AdminApi.md#get_task_info_admin_celery_task_task_id_get) | **GET** /admin/celery/task/{task_id} | Get Task Info
[**get_task_stats_admin_celery_stats_get**](AdminApi.md#get_task_stats_admin_celery_stats_get) | **GET** /admin/celery/stats | Get Task Stats
[**get_tasks_admin_celery_tasks_get**](AdminApi.md#get_tasks_admin_celery_tasks_get) | **GET** /admin/celery/tasks | Get Tasks
[**get_team_info_admin_teams_team_id_get**](AdminApi.md#get_team_info_admin_teams_team_id_get) | **GET** /admin/teams/{team_id} | Get Team Info
[**get_user_details_admin_users_user_identifier_get**](AdminApi.md#get_user_details_admin_users_user_identifier_get) | **GET** /admin/users/{user_identifier} | Get User Details
[**get_user_team_info_admin_users_user_id_team_get**](AdminApi.md#get_user_team_info_admin_users_user_id_team_get) | **GET** /admin/users/{user_id}/team | Get User Team Info
[**get_workers_admin_celery_workers_get**](AdminApi.md#get_workers_admin_celery_workers_get) | **GET** /admin/celery/workers | Get Workers
[**list_app_licenses_admin_app_licenses_get**](AdminApi.md#list_app_licenses_admin_app_licenses_get) | **GET** /admin/app_licenses | List App Licenses
[**list_models_admin_models_get**](AdminApi.md#list_models_admin_models_get) | **GET** /admin/models | List Models
[**list_projects_paginated_admin_projects_get**](AdminApi.md#list_projects_paginated_admin_projects_get) | **GET** /admin/projects | List Projects Paginated
[**list_teams_admin_teams_get**](AdminApi.md#list_teams_admin_teams_get) | **GET** /admin/teams | List Teams
[**list_users_paginated_admin_users_get**](AdminApi.md#list_users_paginated_admin_users_get) | **GET** /admin/users | List Users Paginated
[**remove_team_member_admin_teams_team_id_members_user_id_delete**](AdminApi.md#remove_team_member_admin_teams_team_id_members_user_id_delete) | **DELETE** /admin/teams/{team_id}/members/{user_id} | Remove Team Member
[**retry_task_admin_celery_task_task_id_retry_post**](AdminApi.md#retry_task_admin_celery_task_task_id_retry_post) | **POST** /admin/celery/task/{task_id}/retry | Retry Task
[**search_projects_admin_projects_search_project_id_get**](AdminApi.md#search_projects_admin_projects_search_project_id_get) | **GET** /admin/projects/search/{project_id} | Search Projects
[**terminate_task_admin_celery_task_task_id_terminate_post**](AdminApi.md#terminate_task_admin_celery_task_task_id_terminate_post) | **POST** /admin/celery/task/{task_id}/terminate | Terminate Task
[**update_app_license_admin_app_licenses_license_id_put**](AdminApi.md#update_app_license_admin_app_licenses_license_id_put) | **PUT** /admin/app_licenses/{license_id} | Update App License
[**update_model_admin_models_model_id_put**](AdminApi.md#update_model_admin_models_model_id_put) | **PUT** /admin/models/{model_id} | Update Model
[**update_team_member_admin_teams_team_id_members_put**](AdminApi.md#update_team_member_admin_teams_team_id_members_put) | **PUT** /admin/teams/{team_id}/members | Update Team Member
[**update_team_settings_admin_teams_team_id_put**](AdminApi.md#update_team_settings_admin_teams_team_id_put) | **PUT** /admin/teams/{team_id} | Update Team Settings
[**update_user_admin_users_user_id_put**](AdminApi.md#update_user_admin_users_user_id_put) | **PUT** /admin/users/{user_id} | Update User
[**upgrade_subscription_admin_subscriptions_upgrade_post**](AdminApi.md#upgrade_subscription_admin_subscriptions_upgrade_post) | **POST** /admin/subscriptions/upgrade | Upgrade Subscription


# **clone_project_admin_projects_clone_post**
> ProjectResponse clone_project_admin_projects_clone_post(project_clone, x_api_key=x_api_key, x_api_secret=x_api_secret)

Clone Project

Clone a project for another user

### Example


```python
import odin_sdk
from odin_sdk.models.project_clone import ProjectClone
from odin_sdk.models.project_response import ProjectResponse
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
    api_instance = odin_sdk.AdminApi(api_client)
    project_clone = odin_sdk.ProjectClone() # ProjectClone | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Clone Project
        api_response = api_instance.clone_project_admin_projects_clone_post(project_clone, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of AdminApi->clone_project_admin_projects_clone_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->clone_project_admin_projects_clone_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_clone** | [**ProjectClone**](ProjectClone.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**ProjectResponse**](ProjectResponse.md)

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

# **create_app_license_admin_app_licenses_post**
> AppLicenseResponse create_app_license_admin_app_licenses_post(app_license_create, x_api_key=x_api_key, x_api_secret=x_api_secret)

Create App License

Create a new app license

### Example


```python
import odin_sdk
from odin_sdk.models.app_license_create import AppLicenseCreate
from odin_sdk.models.app_license_response import AppLicenseResponse
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
    api_instance = odin_sdk.AdminApi(api_client)
    app_license_create = odin_sdk.AppLicenseCreate() # AppLicenseCreate | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Create App License
        api_response = api_instance.create_app_license_admin_app_licenses_post(app_license_create, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of AdminApi->create_app_license_admin_app_licenses_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->create_app_license_admin_app_licenses_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_license_create** | [**AppLicenseCreate**](AppLicenseCreate.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**AppLicenseResponse**](AppLicenseResponse.md)

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

# **create_model_admin_models_post**
> ModelResponse create_model_admin_models_post(model_create, x_api_key=x_api_key, x_api_secret=x_api_secret)

Create Model

Create a new AI model

### Example


```python
import odin_sdk
from odin_sdk.models.model_create import ModelCreate
from odin_sdk.models.model_response import ModelResponse
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
    api_instance = odin_sdk.AdminApi(api_client)
    model_create = odin_sdk.ModelCreate() # ModelCreate | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Create Model
        api_response = api_instance.create_model_admin_models_post(model_create, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of AdminApi->create_model_admin_models_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->create_model_admin_models_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_create** | [**ModelCreate**](ModelCreate.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**ModelResponse**](ModelResponse.md)

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

# **create_team_admin_teams_create_post**
> object create_team_admin_teams_create_post(create_team_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Create Team

Create a new team for offline/on prem deployments that do not utilize Stripe/licenses.

### Example


```python
import odin_sdk
from odin_sdk.models.create_team_request import CreateTeamRequest
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
    api_instance = odin_sdk.AdminApi(api_client)
    create_team_request = odin_sdk.CreateTeamRequest() # CreateTeamRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Create Team
        api_response = api_instance.create_team_admin_teams_create_post(create_team_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of AdminApi->create_team_admin_teams_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->create_team_admin_teams_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_team_request** | [**CreateTeamRequest**](CreateTeamRequest.md)|  | 
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

# **delete_model_admin_models_model_id_delete**
> object delete_model_admin_models_model_id_delete(model_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Delete Model

Delete an AI model

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
    api_instance = odin_sdk.AdminApi(api_client)
    model_id = 'model_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Delete Model
        api_response = api_instance.delete_model_admin_models_model_id_delete(model_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of AdminApi->delete_model_admin_models_model_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->delete_model_admin_models_model_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_id** | **str**|  | 
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

# **delete_team_admin_teams_delete_delete**
> object delete_team_admin_teams_delete_delete(delete_team_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Delete Team

Delete a team

### Example


```python
import odin_sdk
from odin_sdk.models.delete_team_request import DeleteTeamRequest
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
    api_instance = odin_sdk.AdminApi(api_client)
    delete_team_request = odin_sdk.DeleteTeamRequest() # DeleteTeamRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Delete Team
        api_response = api_instance.delete_team_admin_teams_delete_delete(delete_team_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of AdminApi->delete_team_admin_teams_delete_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->delete_team_admin_teams_delete_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_team_request** | [**DeleteTeamRequest**](DeleteTeamRequest.md)|  | 
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

# **evaluate_citation_admin_evaluate_citation_post**
> object evaluate_citation_admin_evaluate_citation_post(project_id=project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Evaluate Citation

Creates evaluation tasks for the citation

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
    api_instance = odin_sdk.AdminApi(api_client)
    project_id = '...' # str | The project ID to evaluate the retrieval model for (optional) (default to '...')
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Evaluate Citation
        api_response = api_instance.evaluate_citation_admin_evaluate_citation_post(project_id=project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of AdminApi->evaluate_citation_admin_evaluate_citation_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->evaluate_citation_admin_evaluate_citation_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The project ID to evaluate the retrieval model for | [optional] [default to &#39;...&#39;]
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

# **evaluate_retrieval_admin_evaluate_retrieval_post**
> object evaluate_retrieval_admin_evaluate_retrieval_post(project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Evaluate Retrieval

Creates evaluation tasks for the retrieval

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
    api_instance = odin_sdk.AdminApi(api_client)
    project_id = 'project_id_example' # str | The project ID to evaluate the retrieval model for
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Evaluate Retrieval
        api_response = api_instance.evaluate_retrieval_admin_evaluate_retrieval_post(project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of AdminApi->evaluate_retrieval_admin_evaluate_retrieval_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->evaluate_retrieval_admin_evaluate_retrieval_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The project ID to evaluate the retrieval model for | 
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

# **generate_password_reset_admin_password_reset_user_identifier_post**
> object generate_password_reset_admin_password_reset_user_identifier_post(user_identifier, x_api_key=x_api_key, x_api_secret=x_api_secret)

Generate Password Reset

Generate password reset link for a user

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
    api_instance = odin_sdk.AdminApi(api_client)
    user_identifier = 'user_identifier_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Generate Password Reset
        api_response = api_instance.generate_password_reset_admin_password_reset_user_identifier_post(user_identifier, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of AdminApi->generate_password_reset_admin_password_reset_user_identifier_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->generate_password_reset_admin_password_reset_user_identifier_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_identifier** | **str**|  | 
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

# **get_active_tasks_endpoint_admin_celery_active_tasks_get**
> List[TaskInfoModel] get_active_tasks_endpoint_admin_celery_active_tasks_get(x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Active Tasks Endpoint

Get all currently running Celery tasks

### Example


```python
import odin_sdk
from odin_sdk.models.task_info_model import TaskInfoModel
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
    api_instance = odin_sdk.AdminApi(api_client)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Active Tasks Endpoint
        api_response = api_instance.get_active_tasks_endpoint_admin_celery_active_tasks_get(x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of AdminApi->get_active_tasks_endpoint_admin_celery_active_tasks_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_active_tasks_endpoint_admin_celery_active_tasks_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**List[TaskInfoModel]**](TaskInfoModel.md)

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

# **get_agents_count_by_project_endpoint_admin_agents_count_by_project_get**
> AgentCountResponse get_agents_count_by_project_endpoint_admin_agents_count_by_project_get(x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Agents Count By Project Endpoint

Get count of agents grouped by project_id

### Example


```python
import odin_sdk
from odin_sdk.models.agent_count_response import AgentCountResponse
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
    api_instance = odin_sdk.AdminApi(api_client)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Agents Count By Project Endpoint
        api_response = api_instance.get_agents_count_by_project_endpoint_admin_agents_count_by_project_get(x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of AdminApi->get_agents_count_by_project_endpoint_admin_agents_count_by_project_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_agents_count_by_project_endpoint_admin_agents_count_by_project_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**AgentCountResponse**](AgentCountResponse.md)

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

# **get_app_license_admin_app_licenses_license_id_get**
> AppLicenseResponse get_app_license_admin_app_licenses_license_id_get(license_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get App License

Get a specific app license by ID

### Example


```python
import odin_sdk
from odin_sdk.models.app_license_response import AppLicenseResponse
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
    api_instance = odin_sdk.AdminApi(api_client)
    license_id = 'license_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get App License
        api_response = api_instance.get_app_license_admin_app_licenses_license_id_get(license_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of AdminApi->get_app_license_admin_app_licenses_license_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_app_license_admin_app_licenses_license_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **license_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**AppLicenseResponse**](AppLicenseResponse.md)

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

# **get_evaluation_tasks_admin_evaluation_tasks_get**
> object get_evaluation_tasks_admin_evaluation_tasks_get(num_tasks=num_tasks, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Evaluation Tasks

Get the evaluation tasks for a project

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
    api_instance = odin_sdk.AdminApi(api_client)
    num_tasks = 10 # int |  (optional) (default to 10)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Evaluation Tasks
        api_response = api_instance.get_evaluation_tasks_admin_evaluation_tasks_get(num_tasks=num_tasks, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of AdminApi->get_evaluation_tasks_admin_evaluation_tasks_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_evaluation_tasks_admin_evaluation_tasks_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **num_tasks** | **int**|  | [optional] [default to 10]
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

# **get_knowledge_base_files_admin_knowledge_get**
> QueuedKBFileResponse get_knowledge_base_files_admin_knowledge_get(page=page, page_size=page_size, status=status, project_id=project_id, search=search, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Knowledge Base Files

Get knowledge base files with optional filtering parameters

- status: Filter by file status (e.g., "queued", "synced", "failed")
- project_id: Filter by specific project ID
- search: Search by file name or content

### Example


```python
import odin_sdk
from odin_sdk.models.queued_kb_file_response import QueuedKBFileResponse
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
    api_instance = odin_sdk.AdminApi(api_client)
    page = 1 # int |  (optional) (default to 1)
    page_size = 10 # int |  (optional) (default to 10)
    status = 'status_example' # str |  (optional)
    project_id = 'project_id_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Knowledge Base Files
        api_response = api_instance.get_knowledge_base_files_admin_knowledge_get(page=page, page_size=page_size, status=status, project_id=project_id, search=search, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of AdminApi->get_knowledge_base_files_admin_knowledge_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_knowledge_base_files_admin_knowledge_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 10]
 **status** | **str**|  | [optional] 
 **project_id** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**QueuedKBFileResponse**](QueuedKBFileResponse.md)

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

# **get_model_admin_models_model_id_get**
> ModelResponse get_model_admin_models_model_id_get(model_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Model

Get a specific AI model by ID

### Example


```python
import odin_sdk
from odin_sdk.models.model_response import ModelResponse
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
    api_instance = odin_sdk.AdminApi(api_client)
    model_id = 'model_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Model
        api_response = api_instance.get_model_admin_models_model_id_get(model_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of AdminApi->get_model_admin_models_model_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_model_admin_models_model_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**ModelResponse**](ModelResponse.md)

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

# **get_onprem_token_admin_onprem_token_license_key_get**
> object get_onprem_token_admin_onprem_token_license_key_get(license_key)

Get Onprem Token

Return a valid Docker Hub token for a valid enterprise license key.
If the license key exists in the teams_table, generate and return a Docker Hub token.

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
    api_instance = odin_sdk.AdminApi(api_client)
    license_key = 'license_key_example' # str | 

    try:
        # Get Onprem Token
        api_response = api_instance.get_onprem_token_admin_onprem_token_license_key_get(license_key)
        print("The response of AdminApi->get_onprem_token_admin_onprem_token_license_key_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_onprem_token_admin_onprem_token_license_key_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **license_key** | **str**|  | 

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

# **get_project_details_admin_projects_project_id_get**
> ProjectResponse get_project_details_admin_projects_project_id_get(project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Project Details

Get project details

### Example


```python
import odin_sdk
from odin_sdk.models.project_response import ProjectResponse
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
    api_instance = odin_sdk.AdminApi(api_client)
    project_id = 'project_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Project Details
        api_response = api_instance.get_project_details_admin_projects_project_id_get(project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of AdminApi->get_project_details_admin_projects_project_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_project_details_admin_projects_project_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**ProjectResponse**](ProjectResponse.md)

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

# **get_stats_admin_stats_get**
> StatsResponse get_stats_admin_stats_get(x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Stats

Get stats for the admin dashboard

### Example


```python
import odin_sdk
from odin_sdk.models.stats_response import StatsResponse
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
    api_instance = odin_sdk.AdminApi(api_client)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Stats
        api_response = api_instance.get_stats_admin_stats_get(x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of AdminApi->get_stats_admin_stats_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_stats_admin_stats_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**StatsResponse**](StatsResponse.md)

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

# **get_task_info_admin_celery_task_task_id_get**
> TaskInfoModel get_task_info_admin_celery_task_task_id_get(task_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Task Info

Get detailed information about a specific task by ID

### Example


```python
import odin_sdk
from odin_sdk.models.task_info_model import TaskInfoModel
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
    api_instance = odin_sdk.AdminApi(api_client)
    task_id = 'task_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Task Info
        api_response = api_instance.get_task_info_admin_celery_task_task_id_get(task_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of AdminApi->get_task_info_admin_celery_task_task_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_task_info_admin_celery_task_task_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**TaskInfoModel**](TaskInfoModel.md)

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

# **get_task_stats_admin_celery_stats_get**
> List[TaskStatsModel] get_task_stats_admin_celery_stats_get(timeframe=timeframe, project_ids=project_ids, user_ids=user_ids, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Task Stats

Get statistics about task execution (success rates, timing, etc.)
Supports filtering by project_ids, user_ids, and custom time intervals

### Example


```python
import odin_sdk
from odin_sdk.models.task_stats_model import TaskStatsModel
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
    api_instance = odin_sdk.AdminApi(api_client)
    timeframe = '7d' # str | Time frame: 24h, 7d, 30d (optional) (default to '7d')
    project_ids = 'project_ids_example' # str | Comma-separated list of project IDs (optional)
    user_ids = 'user_ids_example' # str | Comma-separated list of user IDs or emails (optional)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Task Stats
        api_response = api_instance.get_task_stats_admin_celery_stats_get(timeframe=timeframe, project_ids=project_ids, user_ids=user_ids, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of AdminApi->get_task_stats_admin_celery_stats_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_task_stats_admin_celery_stats_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeframe** | **str**| Time frame: 24h, 7d, 30d | [optional] [default to &#39;7d&#39;]
 **project_ids** | **str**| Comma-separated list of project IDs | [optional] 
 **user_ids** | **str**| Comma-separated list of user IDs or emails | [optional] 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**List[TaskStatsModel]**](TaskStatsModel.md)

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

# **get_tasks_admin_celery_tasks_get**
> List[TaskInfoModel] get_tasks_admin_celery_tasks_get(limit=limit, offset=offset, status=status, task_name=task_name, project_id=project_id, user_id=user_id, timeframe=timeframe, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Tasks

Get historical tasks with filtering options

### Example


```python
import odin_sdk
from odin_sdk.models.task_info_model import TaskInfoModel
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
    api_instance = odin_sdk.AdminApi(api_client)
    limit = 100 # int |  (optional) (default to 100)
    offset = 0 # int |  (optional) (default to 0)
    status = 'status_example' # str |  (optional)
    task_name = 'task_name_example' # str |  (optional)
    project_id = 'project_id_example' # str |  (optional)
    user_id = 'user_id_example' # str |  (optional)
    timeframe = '24h' # str | Time frame: 24h, 7d, 30d (optional) (default to '24h')
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Tasks
        api_response = api_instance.get_tasks_admin_celery_tasks_get(limit=limit, offset=offset, status=status, task_name=task_name, project_id=project_id, user_id=user_id, timeframe=timeframe, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of AdminApi->get_tasks_admin_celery_tasks_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_tasks_admin_celery_tasks_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 100]
 **offset** | **int**|  | [optional] [default to 0]
 **status** | **str**|  | [optional] 
 **task_name** | **str**|  | [optional] 
 **project_id** | **str**|  | [optional] 
 **user_id** | **str**|  | [optional] 
 **timeframe** | **str**| Time frame: 24h, 7d, 30d | [optional] [default to &#39;24h&#39;]
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**List[TaskInfoModel]**](TaskInfoModel.md)

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

# **get_team_info_admin_teams_team_id_get**
> TeamInfoDetails get_team_info_admin_teams_team_id_get(team_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Team Info

Get detailed information about a specific team

### Example


```python
import odin_sdk
from odin_sdk.models.team_info_details import TeamInfoDetails
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
    api_instance = odin_sdk.AdminApi(api_client)
    team_id = 'team_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Team Info
        api_response = api_instance.get_team_info_admin_teams_team_id_get(team_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of AdminApi->get_team_info_admin_teams_team_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_team_info_admin_teams_team_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**TeamInfoDetails**](TeamInfoDetails.md)

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

# **get_user_details_admin_users_user_identifier_get**
> UserResponse get_user_details_admin_users_user_identifier_get(user_identifier, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get User Details

Get user details by ID or email

### Example


```python
import odin_sdk
from odin_sdk.models.user_response import UserResponse
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
    api_instance = odin_sdk.AdminApi(api_client)
    user_identifier = 'user_identifier_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get User Details
        api_response = api_instance.get_user_details_admin_users_user_identifier_get(user_identifier, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of AdminApi->get_user_details_admin_users_user_identifier_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_user_details_admin_users_user_identifier_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_identifier** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**UserResponse**](UserResponse.md)

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

# **get_user_team_info_admin_users_user_id_team_get**
> TeamInfoDetails get_user_team_info_admin_users_user_id_team_get(user_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get User Team Info

Get team information for a specific user

### Example


```python
import odin_sdk
from odin_sdk.models.team_info_details import TeamInfoDetails
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
    api_instance = odin_sdk.AdminApi(api_client)
    user_id = 'user_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get User Team Info
        api_response = api_instance.get_user_team_info_admin_users_user_id_team_get(user_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of AdminApi->get_user_team_info_admin_users_user_id_team_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_user_team_info_admin_users_user_id_team_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**TeamInfoDetails**](TeamInfoDetails.md)

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

# **get_workers_admin_celery_workers_get**
> List[WorkerInfoModel] get_workers_admin_celery_workers_get(x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Workers

Get information about all active Celery workers

### Example


```python
import odin_sdk
from odin_sdk.models.worker_info_model import WorkerInfoModel
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
    api_instance = odin_sdk.AdminApi(api_client)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Workers
        api_response = api_instance.get_workers_admin_celery_workers_get(x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of AdminApi->get_workers_admin_celery_workers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_workers_admin_celery_workers_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**List[WorkerInfoModel]**](WorkerInfoModel.md)

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

# **list_app_licenses_admin_app_licenses_get**
> PaginatedAppLicensesResponse list_app_licenses_admin_app_licenses_get(page=page, page_size=page_size, search=search, status=status, x_api_key=x_api_key, x_api_secret=x_api_secret)

List App Licenses

List app licenses with pagination and optional filtering

### Example


```python
import odin_sdk
from odin_sdk.models.paginated_app_licenses_response import PaginatedAppLicensesResponse
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
    api_instance = odin_sdk.AdminApi(api_client)
    page = 1 # int |  (optional) (default to 1)
    page_size = 10 # int |  (optional) (default to 10)
    search = 'search_example' # str |  (optional)
    status = 'status_example' # str |  (optional)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # List App Licenses
        api_response = api_instance.list_app_licenses_admin_app_licenses_get(page=page, page_size=page_size, search=search, status=status, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of AdminApi->list_app_licenses_admin_app_licenses_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->list_app_licenses_admin_app_licenses_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 10]
 **search** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**PaginatedAppLicensesResponse**](PaginatedAppLicensesResponse.md)

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

# **list_models_admin_models_get**
> List[ModelResponse] list_models_admin_models_get(x_api_key=x_api_key, x_api_secret=x_api_secret)

List Models

List all AI models

### Example


```python
import odin_sdk
from odin_sdk.models.model_response import ModelResponse
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
    api_instance = odin_sdk.AdminApi(api_client)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # List Models
        api_response = api_instance.list_models_admin_models_get(x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of AdminApi->list_models_admin_models_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->list_models_admin_models_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**List[ModelResponse]**](ModelResponse.md)

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

# **list_projects_paginated_admin_projects_get**
> PaginatedProjectsResponse list_projects_paginated_admin_projects_get(page=page, page_size=page_size, x_api_key=x_api_key, x_api_secret=x_api_secret)

List Projects Paginated

List all projects with pagination

### Example


```python
import odin_sdk
from odin_sdk.models.paginated_projects_response import PaginatedProjectsResponse
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
    api_instance = odin_sdk.AdminApi(api_client)
    page = 1 # int |  (optional) (default to 1)
    page_size = 10 # int |  (optional) (default to 10)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # List Projects Paginated
        api_response = api_instance.list_projects_paginated_admin_projects_get(page=page, page_size=page_size, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of AdminApi->list_projects_paginated_admin_projects_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->list_projects_paginated_admin_projects_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 10]
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**PaginatedProjectsResponse**](PaginatedProjectsResponse.md)

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

# **list_teams_admin_teams_get**
> PaginatedTeamsResponse list_teams_admin_teams_get(page=page, page_size=page_size, search=search, status=status, x_api_key=x_api_key, x_api_secret=x_api_secret)

List Teams

List all teams with pagination and optional filtering

### Example


```python
import odin_sdk
from odin_sdk.models.paginated_teams_response import PaginatedTeamsResponse
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
    api_instance = odin_sdk.AdminApi(api_client)
    page = 1 # int |  (optional) (default to 1)
    page_size = 10 # int |  (optional) (default to 10)
    search = 'search_example' # str |  (optional)
    status = 'status_example' # str |  (optional)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # List Teams
        api_response = api_instance.list_teams_admin_teams_get(page=page, page_size=page_size, search=search, status=status, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of AdminApi->list_teams_admin_teams_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->list_teams_admin_teams_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 10]
 **search** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**PaginatedTeamsResponse**](PaginatedTeamsResponse.md)

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

# **list_users_paginated_admin_users_get**
> PaginatedUsersResponse list_users_paginated_admin_users_get(page=page, page_size=page_size, x_api_key=x_api_key, x_api_secret=x_api_secret)

List Users Paginated

Get paginated list of users with total count

### Example


```python
import odin_sdk
from odin_sdk.models.paginated_users_response import PaginatedUsersResponse
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
    api_instance = odin_sdk.AdminApi(api_client)
    page = 1 # int |  (optional) (default to 1)
    page_size = 10 # int |  (optional) (default to 10)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # List Users Paginated
        api_response = api_instance.list_users_paginated_admin_users_get(page=page, page_size=page_size, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of AdminApi->list_users_paginated_admin_users_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->list_users_paginated_admin_users_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 10]
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**PaginatedUsersResponse**](PaginatedUsersResponse.md)

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

# **remove_team_member_admin_teams_team_id_members_user_id_delete**
> TeamInfoDetails remove_team_member_admin_teams_team_id_members_user_id_delete(team_id, user_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Remove Team Member

Remove a member from a team

### Example


```python
import odin_sdk
from odin_sdk.models.team_info_details import TeamInfoDetails
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
    api_instance = odin_sdk.AdminApi(api_client)
    team_id = 'team_id_example' # str | 
    user_id = 'user_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Remove Team Member
        api_response = api_instance.remove_team_member_admin_teams_team_id_members_user_id_delete(team_id, user_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of AdminApi->remove_team_member_admin_teams_team_id_members_user_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->remove_team_member_admin_teams_team_id_members_user_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**|  | 
 **user_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**TeamInfoDetails**](TeamInfoDetails.md)

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

# **retry_task_admin_celery_task_task_id_retry_post**
> Dict[str, Optional[str]] retry_task_admin_celery_task_task_id_retry_post(task_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Retry Task

Retry a failed task

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
    api_instance = odin_sdk.AdminApi(api_client)
    task_id = 'task_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Retry Task
        api_response = api_instance.retry_task_admin_celery_task_task_id_retry_post(task_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of AdminApi->retry_task_admin_celery_task_task_id_retry_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->retry_task_admin_celery_task_task_id_retry_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

**Dict[str, Optional[str]]**

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

# **search_projects_admin_projects_search_project_id_get**
> PaginatedProjectsResponse search_projects_admin_projects_search_project_id_get(project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Search Projects

Search for projects by id

### Example


```python
import odin_sdk
from odin_sdk.models.paginated_projects_response import PaginatedProjectsResponse
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
    api_instance = odin_sdk.AdminApi(api_client)
    project_id = 'project_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Search Projects
        api_response = api_instance.search_projects_admin_projects_search_project_id_get(project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of AdminApi->search_projects_admin_projects_search_project_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->search_projects_admin_projects_search_project_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**PaginatedProjectsResponse**](PaginatedProjectsResponse.md)

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

# **terminate_task_admin_celery_task_task_id_terminate_post**
> Dict[str, Optional[str]] terminate_task_admin_celery_task_task_id_terminate_post(task_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Terminate Task

Terminate a running task with SIGTERM.

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
    api_instance = odin_sdk.AdminApi(api_client)
    task_id = 'task_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Terminate Task
        api_response = api_instance.terminate_task_admin_celery_task_task_id_terminate_post(task_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of AdminApi->terminate_task_admin_celery_task_task_id_terminate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->terminate_task_admin_celery_task_task_id_terminate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

**Dict[str, Optional[str]]**

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

# **update_app_license_admin_app_licenses_license_id_put**
> AppLicenseResponse update_app_license_admin_app_licenses_license_id_put(license_id, app_license_update, x_api_key=x_api_key, x_api_secret=x_api_secret)

Update App License

Update an existing app license

### Example


```python
import odin_sdk
from odin_sdk.models.app_license_response import AppLicenseResponse
from odin_sdk.models.app_license_update import AppLicenseUpdate
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
    api_instance = odin_sdk.AdminApi(api_client)
    license_id = 'license_id_example' # str | 
    app_license_update = odin_sdk.AppLicenseUpdate() # AppLicenseUpdate | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Update App License
        api_response = api_instance.update_app_license_admin_app_licenses_license_id_put(license_id, app_license_update, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of AdminApi->update_app_license_admin_app_licenses_license_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->update_app_license_admin_app_licenses_license_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **license_id** | **str**|  | 
 **app_license_update** | [**AppLicenseUpdate**](AppLicenseUpdate.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**AppLicenseResponse**](AppLicenseResponse.md)

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

# **update_model_admin_models_model_id_put**
> ModelResponse update_model_admin_models_model_id_put(model_id, model_update, x_api_key=x_api_key, x_api_secret=x_api_secret)

Update Model

Update an existing AI model

### Example


```python
import odin_sdk
from odin_sdk.models.model_response import ModelResponse
from odin_sdk.models.model_update import ModelUpdate
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
    api_instance = odin_sdk.AdminApi(api_client)
    model_id = 'model_id_example' # str | 
    model_update = odin_sdk.ModelUpdate() # ModelUpdate | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Update Model
        api_response = api_instance.update_model_admin_models_model_id_put(model_id, model_update, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of AdminApi->update_model_admin_models_model_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->update_model_admin_models_model_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_id** | **str**|  | 
 **model_update** | [**ModelUpdate**](ModelUpdate.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**ModelResponse**](ModelResponse.md)

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

# **update_team_member_admin_teams_team_id_members_put**
> TeamInfoDetails update_team_member_admin_teams_team_id_members_put(team_id, team_member_update_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Update Team Member

Add or update a team member

### Example


```python
import odin_sdk
from odin_sdk.models.team_info_details import TeamInfoDetails
from odin_sdk.models.team_member_update_request import TeamMemberUpdateRequest
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
    api_instance = odin_sdk.AdminApi(api_client)
    team_id = 'team_id_example' # str | 
    team_member_update_request = odin_sdk.TeamMemberUpdateRequest() # TeamMemberUpdateRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Update Team Member
        api_response = api_instance.update_team_member_admin_teams_team_id_members_put(team_id, team_member_update_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of AdminApi->update_team_member_admin_teams_team_id_members_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->update_team_member_admin_teams_team_id_members_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**|  | 
 **team_member_update_request** | [**TeamMemberUpdateRequest**](TeamMemberUpdateRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**TeamInfoDetails**](TeamInfoDetails.md)

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

# **update_team_settings_admin_teams_team_id_put**
> TeamInfoDetails update_team_settings_admin_teams_team_id_put(team_id, team_update_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Update Team Settings

Update team settings

### Example


```python
import odin_sdk
from odin_sdk.models.team_info_details import TeamInfoDetails
from odin_sdk.models.team_update_request import TeamUpdateRequest
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
    api_instance = odin_sdk.AdminApi(api_client)
    team_id = 'team_id_example' # str | 
    team_update_request = odin_sdk.TeamUpdateRequest() # TeamUpdateRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Update Team Settings
        api_response = api_instance.update_team_settings_admin_teams_team_id_put(team_id, team_update_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of AdminApi->update_team_settings_admin_teams_team_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->update_team_settings_admin_teams_team_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**|  | 
 **team_update_request** | [**TeamUpdateRequest**](TeamUpdateRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**TeamInfoDetails**](TeamInfoDetails.md)

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

# **update_user_admin_users_user_id_put**
> UserResponse update_user_admin_users_user_id_put(user_id, user_update, x_api_key=x_api_key, x_api_secret=x_api_secret)

Update User

Update user details

### Example


```python
import odin_sdk
from odin_sdk.models.user_response import UserResponse
from odin_sdk.models.user_update import UserUpdate
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
    api_instance = odin_sdk.AdminApi(api_client)
    user_id = 'user_id_example' # str | 
    user_update = odin_sdk.UserUpdate() # UserUpdate | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Update User
        api_response = api_instance.update_user_admin_users_user_id_put(user_id, user_update, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of AdminApi->update_user_admin_users_user_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->update_user_admin_users_user_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **user_update** | [**UserUpdate**](UserUpdate.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**UserResponse**](UserResponse.md)

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

# **upgrade_subscription_admin_subscriptions_upgrade_post**
> object upgrade_subscription_admin_subscriptions_upgrade_post(subscription_update, x_api_key=x_api_key, x_api_secret=x_api_secret)

Upgrade Subscription

Upgrade user subscription

### Example


```python
import odin_sdk
from odin_sdk.models.subscription_update import SubscriptionUpdate
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
    api_instance = odin_sdk.AdminApi(api_client)
    subscription_update = odin_sdk.SubscriptionUpdate() # SubscriptionUpdate | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Upgrade Subscription
        api_response = api_instance.upgrade_subscription_admin_subscriptions_upgrade_post(subscription_update, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of AdminApi->upgrade_subscription_admin_subscriptions_upgrade_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->upgrade_subscription_admin_subscriptions_upgrade_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_update** | [**SubscriptionUpdate**](SubscriptionUpdate.md)|  | 
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

