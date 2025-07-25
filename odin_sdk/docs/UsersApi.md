# odin_sdk.UsersApi

All URIs are relative to *http://127.0.0.1:8001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accept_team_invitation_user_team_id_invitation_accept_post**](UsersApi.md#accept_team_invitation_user_team_id_invitation_accept_post) | **POST** /user/{team_id}/invitation/accept | Accept Team Invitation
[**add_api_key_to_team_teams_api_keys_post**](UsersApi.md#add_api_key_to_team_teams_api_keys_post) | **POST** /teams/api-keys | Add Api Key To Team
[**add_db_credential_to_team_teams_db_credential_post**](UsersApi.md#add_db_credential_to_team_teams_db_credential_post) | **POST** /teams/db-credential | Add Db Credential To Team
[**add_team_members_users_team_add_users_post**](UsersApi.md#add_team_members_users_team_add_users_post) | **POST** /users/team/add-users | Add Team Members
[**change_team_name_users_team_name_change_post**](UsersApi.md#change_team_name_users_team_name_change_post) | **POST** /users/team/name/change | Change Team Name
[**decline_team_invitation_user_team_id_invitation_decline_post**](UsersApi.md#decline_team_invitation_user_team_id_invitation_decline_post) | **POST** /user/{team_id}/invitation/decline | Decline Team Invitation
[**export_team_users_users_enterprise_export_get**](UsersApi.md#export_team_users_users_enterprise_export_get) | **GET** /users/enterprise/export | Export Team Users
[**export_user_events_user_enterprise_events_export_get**](UsersApi.md#export_user_events_user_enterprise_events_export_get) | **GET** /user/enterprise/events/export | Export User Events
[**get_all_user_tags_v1_users_tags_get**](UsersApi.md#get_all_user_tags_v1_users_tags_get) | **GET** /v1/users/tags | Get All User Tags
[**get_event_types_users_event_types_get**](UsersApi.md#get_event_types_users_event_types_get) | **GET** /users/event-types | Get Event Types
[**get_team_db_credential_teams_db_credential_get**](UsersApi.md#get_team_db_credential_teams_db_credential_get) | **GET** /teams/db-credential | Get Team Db Credential
[**get_user_events_user_enterprise_events_get**](UsersApi.md#get_user_events_user_enterprise_events_get) | **GET** /user/enterprise/events | Get User Events
[**get_user_events_users_events_get**](UsersApi.md#get_user_events_users_events_get) | **GET** /users/events | Get User Events
[**get_user_providers_user_auth_details_get**](UsersApi.md#get_user_providers_user_auth_details_get) | **GET** /user/auth/details | Get User Providers
[**get_user_tags_v1_user_user_id_tags_get**](UsersApi.md#get_user_tags_v1_user_user_id_tags_get) | **GET** /v1/user/{user_id}/tags | Get User Tags
[**granular_validate_api_key_teams_validate_api_key_post**](UsersApi.md#granular_validate_api_key_teams_validate_api_key_post) | **POST** /teams/validate-api-key | Granular Validate Api Key
[**read_notifications_user_notifications_read_post**](UsersApi.md#read_notifications_user_notifications_read_post) | **POST** /user/notifications/read | Read Notifications
[**remove_team_member_by_email_user_team_remove_by_email_post**](UsersApi.md#remove_team_member_by_email_user_team_remove_by_email_post) | **POST** /user/team/remove-by-email | Remove Team Member By Email
[**remove_user_from_team_user_user_id_team_remove_post**](UsersApi.md#remove_user_from_team_user_user_id_team_remove_post) | **POST** /user/{user_id}/team/remove | Remove User From Team
[**remove_user_tags_v1_user_tags_delete**](UsersApi.md#remove_user_tags_v1_user_tags_delete) | **DELETE** /v1/user/tags | Remove User Tags
[**update_team_member_role_users_teams_member_role_update_put**](UsersApi.md#update_team_member_role_users_teams_member_role_update_put) | **PUT** /users/teams/member/role/update | Update Team Member Role
[**update_team_settings_teams_settings_post**](UsersApi.md#update_team_settings_teams_settings_post) | **POST** /teams/settings | Update Team Settings
[**update_team_users_team_update_post**](UsersApi.md#update_team_users_team_update_post) | **POST** /users/team/update | Update Team
[**update_user_credit_limit_users_teams_member_credit_limit_update_put**](UsersApi.md#update_user_credit_limit_users_teams_member_credit_limit_update_put) | **PUT** /users/teams/member/credit-limit/update | Update User Credit Limit
[**update_user_tags_v1_user_tags_post**](UsersApi.md#update_user_tags_v1_user_tags_post) | **POST** /v1/user/tags | Update User Tags


# **accept_team_invitation_user_team_id_invitation_accept_post**
> UserTeamInviteResponse accept_team_invitation_user_team_id_invitation_accept_post(team_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Accept Team Invitation

### Example


```python
import odin_sdk
from odin_sdk.models.user_team_invite_response import UserTeamInviteResponse
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
    api_instance = odin_sdk.UsersApi(api_client)
    team_id = 'team_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Accept Team Invitation
        api_response = api_instance.accept_team_invitation_user_team_id_invitation_accept_post(team_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of UsersApi->accept_team_invitation_user_team_id_invitation_accept_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->accept_team_invitation_user_team_id_invitation_accept_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**UserTeamInviteResponse**](UserTeamInviteResponse.md)

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

# **add_api_key_to_team_teams_api_keys_post**
> RoutesUsersInsertModelResponse add_api_key_to_team_teams_api_keys_post(insert_team_api_key_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Add Api Key To Team

### Example


```python
import odin_sdk
from odin_sdk.models.insert_team_api_key_request import InsertTeamAPIKeyRequest
from odin_sdk.models.routes_users_insert_model_response import RoutesUsersInsertModelResponse
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
    api_instance = odin_sdk.UsersApi(api_client)
    insert_team_api_key_request = odin_sdk.InsertTeamAPIKeyRequest() # InsertTeamAPIKeyRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Add Api Key To Team
        api_response = api_instance.add_api_key_to_team_teams_api_keys_post(insert_team_api_key_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of UsersApi->add_api_key_to_team_teams_api_keys_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->add_api_key_to_team_teams_api_keys_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **insert_team_api_key_request** | [**InsertTeamAPIKeyRequest**](InsertTeamAPIKeyRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**RoutesUsersInsertModelResponse**](RoutesUsersInsertModelResponse.md)

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

# **add_db_credential_to_team_teams_db_credential_post**
> RoutesUsersInsertModelResponse add_db_credential_to_team_teams_db_credential_post(insert_team_db_credential_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Add Db Credential To Team

### Example


```python
import odin_sdk
from odin_sdk.models.insert_team_db_credential_request import InsertTeamDBCredentialRequest
from odin_sdk.models.routes_users_insert_model_response import RoutesUsersInsertModelResponse
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
    api_instance = odin_sdk.UsersApi(api_client)
    insert_team_db_credential_request = odin_sdk.InsertTeamDBCredentialRequest() # InsertTeamDBCredentialRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Add Db Credential To Team
        api_response = api_instance.add_db_credential_to_team_teams_db_credential_post(insert_team_db_credential_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of UsersApi->add_db_credential_to_team_teams_db_credential_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->add_db_credential_to_team_teams_db_credential_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **insert_team_db_credential_request** | [**InsertTeamDBCredentialRequest**](InsertTeamDBCredentialRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**RoutesUsersInsertModelResponse**](RoutesUsersInsertModelResponse.md)

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

# **add_team_members_users_team_add_users_post**
> AddTeamMembersResponse add_team_members_users_team_add_users_post(add_team_members_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Add Team Members

### Example


```python
import odin_sdk
from odin_sdk.models.add_team_members_request import AddTeamMembersRequest
from odin_sdk.models.add_team_members_response import AddTeamMembersResponse
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
    api_instance = odin_sdk.UsersApi(api_client)
    add_team_members_request = odin_sdk.AddTeamMembersRequest() # AddTeamMembersRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Add Team Members
        api_response = api_instance.add_team_members_users_team_add_users_post(add_team_members_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of UsersApi->add_team_members_users_team_add_users_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->add_team_members_users_team_add_users_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_team_members_request** | [**AddTeamMembersRequest**](AddTeamMembersRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**AddTeamMembersResponse**](AddTeamMembersResponse.md)

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

# **change_team_name_users_team_name_change_post**
> UserTeamNameChangeResponse change_team_name_users_team_name_change_post(user_team_name_change_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Change Team Name

### Example


```python
import odin_sdk
from odin_sdk.models.user_team_name_change_request import UserTeamNameChangeRequest
from odin_sdk.models.user_team_name_change_response import UserTeamNameChangeResponse
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
    api_instance = odin_sdk.UsersApi(api_client)
    user_team_name_change_request = odin_sdk.UserTeamNameChangeRequest() # UserTeamNameChangeRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Change Team Name
        api_response = api_instance.change_team_name_users_team_name_change_post(user_team_name_change_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of UsersApi->change_team_name_users_team_name_change_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->change_team_name_users_team_name_change_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_team_name_change_request** | [**UserTeamNameChangeRequest**](UserTeamNameChangeRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**UserTeamNameChangeResponse**](UserTeamNameChangeResponse.md)

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

# **decline_team_invitation_user_team_id_invitation_decline_post**
> UserTeamInviteResponse decline_team_invitation_user_team_id_invitation_decline_post(team_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Decline Team Invitation

### Example


```python
import odin_sdk
from odin_sdk.models.user_team_invite_response import UserTeamInviteResponse
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
    api_instance = odin_sdk.UsersApi(api_client)
    team_id = 'team_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Decline Team Invitation
        api_response = api_instance.decline_team_invitation_user_team_id_invitation_decline_post(team_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of UsersApi->decline_team_invitation_user_team_id_invitation_decline_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->decline_team_invitation_user_team_id_invitation_decline_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**UserTeamInviteResponse**](UserTeamInviteResponse.md)

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

# **export_team_users_users_enterprise_export_get**
> export_team_users_users_enterprise_export_get(x_api_key=x_api_key, x_api_secret=x_api_secret)

Export Team Users

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
    api_instance = odin_sdk.UsersApi(api_client)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Export Team Users
        api_instance.export_team_users_users_enterprise_export_get(x_api_key=x_api_key, x_api_secret=x_api_secret)
    except Exception as e:
        print("Exception when calling UsersApi->export_team_users_users_enterprise_export_get: %s\n" % e)
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

# **export_user_events_user_enterprise_events_export_get**
> export_user_events_user_enterprise_events_export_get(user_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Export User Events

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
    api_instance = odin_sdk.UsersApi(api_client)
    user_id = 'user_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Export User Events
        api_instance.export_user_events_user_enterprise_events_export_get(user_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
    except Exception as e:
        print("Exception when calling UsersApi->export_user_events_user_enterprise_events_export_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
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

# **get_all_user_tags_v1_users_tags_get**
> List[Optional[str]] get_all_user_tags_v1_users_tags_get(x_api_key=x_api_key, x_api_secret=x_api_secret)

Get All User Tags

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
    api_instance = odin_sdk.UsersApi(api_client)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get All User Tags
        api_response = api_instance.get_all_user_tags_v1_users_tags_get(x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of UsersApi->get_all_user_tags_v1_users_tags_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_all_user_tags_v1_users_tags_get: %s\n" % e)
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

# **get_event_types_users_event_types_get**
> object get_event_types_users_event_types_get(x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Event Types

Get all possible event types

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
    api_instance = odin_sdk.UsersApi(api_client)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Event Types
        api_response = api_instance.get_event_types_users_event_types_get(x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of UsersApi->get_event_types_users_event_types_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_event_types_users_event_types_get: %s\n" % e)
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

# **get_team_db_credential_teams_db_credential_get**
> object get_team_db_credential_teams_db_credential_get(x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Team Db Credential

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
    api_instance = odin_sdk.UsersApi(api_client)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Team Db Credential
        api_response = api_instance.get_team_db_credential_teams_db_credential_get(x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of UsersApi->get_team_db_credential_teams_db_credential_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_team_db_credential_teams_db_credential_get: %s\n" % e)
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

# **get_user_events_user_enterprise_events_get**
> UserEventResponse get_user_events_user_enterprise_events_get(user_id, timestamp=timestamp, limit=limit, event_type=event_type, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get User Events

### Example


```python
import odin_sdk
from odin_sdk.models.user_event_response import UserEventResponse
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
    api_instance = odin_sdk.UsersApi(api_client)
    user_id = 'user_id_example' # str | 
    timestamp = 3.4 # float |  (optional)
    limit = 56 # int |  (optional)
    event_type = 'event_type_example' # str |  (optional)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get User Events
        api_response = api_instance.get_user_events_user_enterprise_events_get(user_id, timestamp=timestamp, limit=limit, event_type=event_type, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of UsersApi->get_user_events_user_enterprise_events_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user_events_user_enterprise_events_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **timestamp** | **float**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **event_type** | **str**|  | [optional] 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**UserEventResponse**](UserEventResponse.md)

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

# **get_user_events_users_events_get**
> UserEventResponse get_user_events_users_events_get(timestamp=timestamp, limit=limit, event_type=event_type, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get User Events

Get user events

### Example


```python
import odin_sdk
from odin_sdk.models.user_event_response import UserEventResponse
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
    api_instance = odin_sdk.UsersApi(api_client)
    timestamp = 3.4 # float |  (optional)
    limit = 56 # int |  (optional)
    event_type = 'event_type_example' # str |  (optional)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get User Events
        api_response = api_instance.get_user_events_users_events_get(timestamp=timestamp, limit=limit, event_type=event_type, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of UsersApi->get_user_events_users_events_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user_events_users_events_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **float**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **event_type** | **str**|  | [optional] 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**UserEventResponse**](UserEventResponse.md)

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

# **get_user_providers_user_auth_details_get**
> UserProvidersResponse get_user_providers_user_auth_details_get(email)

Get User Providers

### Example


```python
import odin_sdk
from odin_sdk.models.user_providers_response import UserProvidersResponse
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
    api_instance = odin_sdk.UsersApi(api_client)
    email = 'email_example' # str | The user's email address

    try:
        # Get User Providers
        api_response = api_instance.get_user_providers_user_auth_details_get(email)
        print("The response of UsersApi->get_user_providers_user_auth_details_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user_providers_user_auth_details_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| The user&#39;s email address | 

### Return type

[**UserProvidersResponse**](UserProvidersResponse.md)

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

# **get_user_tags_v1_user_user_id_tags_get**
> UserTagResponse get_user_tags_v1_user_user_id_tags_get(user_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get User Tags

### Example


```python
import odin_sdk
from odin_sdk.models.user_tag_response import UserTagResponse
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
    api_instance = odin_sdk.UsersApi(api_client)
    user_id = 'user_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get User Tags
        api_response = api_instance.get_user_tags_v1_user_user_id_tags_get(user_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of UsersApi->get_user_tags_v1_user_user_id_tags_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user_tags_v1_user_user_id_tags_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**UserTagResponse**](UserTagResponse.md)

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

# **granular_validate_api_key_teams_validate_api_key_post**
> ValidateTeamKeyResponse granular_validate_api_key_teams_validate_api_key_post(insert_team_api_key_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Granular Validate Api Key

### Example


```python
import odin_sdk
from odin_sdk.models.insert_team_api_key_request import InsertTeamAPIKeyRequest
from odin_sdk.models.validate_team_key_response import ValidateTeamKeyResponse
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
    api_instance = odin_sdk.UsersApi(api_client)
    insert_team_api_key_request = odin_sdk.InsertTeamAPIKeyRequest() # InsertTeamAPIKeyRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Granular Validate Api Key
        api_response = api_instance.granular_validate_api_key_teams_validate_api_key_post(insert_team_api_key_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of UsersApi->granular_validate_api_key_teams_validate_api_key_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->granular_validate_api_key_teams_validate_api_key_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **insert_team_api_key_request** | [**InsertTeamAPIKeyRequest**](InsertTeamAPIKeyRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**ValidateTeamKeyResponse**](ValidateTeamKeyResponse.md)

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

# **read_notifications_user_notifications_read_post**
> object read_notifications_user_notifications_read_post(read_notifications_request, include_in_schema=include_in_schema, x_api_key=x_api_key, x_api_secret=x_api_secret)

Read Notifications

### Example


```python
import odin_sdk
from odin_sdk.models.read_notifications_request import ReadNotificationsRequest
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
    api_instance = odin_sdk.UsersApi(api_client)
    read_notifications_request = odin_sdk.ReadNotificationsRequest() # ReadNotificationsRequest | 
    include_in_schema = None # object |  (optional)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Read Notifications
        api_response = api_instance.read_notifications_user_notifications_read_post(read_notifications_request, include_in_schema=include_in_schema, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of UsersApi->read_notifications_user_notifications_read_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->read_notifications_user_notifications_read_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **read_notifications_request** | [**ReadNotificationsRequest**](ReadNotificationsRequest.md)|  | 
 **include_in_schema** | [**object**](.md)|  | [optional] 
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

# **remove_team_member_by_email_user_team_remove_by_email_post**
> UserTeamRemoveResponse remove_team_member_by_email_user_team_remove_by_email_post(remove_team_member_by_email_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Remove Team Member By Email

Remove a team member by their email address.

### Example


```python
import odin_sdk
from odin_sdk.models.remove_team_member_by_email_request import RemoveTeamMemberByEmailRequest
from odin_sdk.models.user_team_remove_response import UserTeamRemoveResponse
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
    api_instance = odin_sdk.UsersApi(api_client)
    remove_team_member_by_email_request = odin_sdk.RemoveTeamMemberByEmailRequest() # RemoveTeamMemberByEmailRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Remove Team Member By Email
        api_response = api_instance.remove_team_member_by_email_user_team_remove_by_email_post(remove_team_member_by_email_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of UsersApi->remove_team_member_by_email_user_team_remove_by_email_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->remove_team_member_by_email_user_team_remove_by_email_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remove_team_member_by_email_request** | [**RemoveTeamMemberByEmailRequest**](RemoveTeamMemberByEmailRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**UserTeamRemoveResponse**](UserTeamRemoveResponse.md)

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

# **remove_user_from_team_user_user_id_team_remove_post**
> UserTeamRemoveResponse remove_user_from_team_user_user_id_team_remove_post(user_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Remove User From Team

### Example


```python
import odin_sdk
from odin_sdk.models.user_team_remove_response import UserTeamRemoveResponse
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
    api_instance = odin_sdk.UsersApi(api_client)
    user_id = 'user_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Remove User From Team
        api_response = api_instance.remove_user_from_team_user_user_id_team_remove_post(user_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of UsersApi->remove_user_from_team_user_user_id_team_remove_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->remove_user_from_team_user_user_id_team_remove_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**UserTeamRemoveResponse**](UserTeamRemoveResponse.md)

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

# **remove_user_tags_v1_user_tags_delete**
> UserTagResponse remove_user_tags_v1_user_tags_delete(user_tag_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Remove User Tags

### Example


```python
import odin_sdk
from odin_sdk.models.user_tag_request import UserTagRequest
from odin_sdk.models.user_tag_response import UserTagResponse
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
    api_instance = odin_sdk.UsersApi(api_client)
    user_tag_request = odin_sdk.UserTagRequest() # UserTagRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Remove User Tags
        api_response = api_instance.remove_user_tags_v1_user_tags_delete(user_tag_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of UsersApi->remove_user_tags_v1_user_tags_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->remove_user_tags_v1_user_tags_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_tag_request** | [**UserTagRequest**](UserTagRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**UserTagResponse**](UserTagResponse.md)

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

# **update_team_member_role_users_teams_member_role_update_put**
> UpdateTeamMemberRoleResponse update_team_member_role_users_teams_member_role_update_put(update_team_member_role_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Update Team Member Role

### Example


```python
import odin_sdk
from odin_sdk.models.update_team_member_role_request import UpdateTeamMemberRoleRequest
from odin_sdk.models.update_team_member_role_response import UpdateTeamMemberRoleResponse
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
    api_instance = odin_sdk.UsersApi(api_client)
    update_team_member_role_request = odin_sdk.UpdateTeamMemberRoleRequest() # UpdateTeamMemberRoleRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Update Team Member Role
        api_response = api_instance.update_team_member_role_users_teams_member_role_update_put(update_team_member_role_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of UsersApi->update_team_member_role_users_teams_member_role_update_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->update_team_member_role_users_teams_member_role_update_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_team_member_role_request** | [**UpdateTeamMemberRoleRequest**](UpdateTeamMemberRoleRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**UpdateTeamMemberRoleResponse**](UpdateTeamMemberRoleResponse.md)

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

# **update_team_settings_teams_settings_post**
> RoutesUsersInsertModelResponse update_team_settings_teams_settings_post(update_settings_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Update Team Settings

### Example


```python
import odin_sdk
from odin_sdk.models.routes_users_insert_model_response import RoutesUsersInsertModelResponse
from odin_sdk.models.update_settings_request import UpdateSettingsRequest
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
    api_instance = odin_sdk.UsersApi(api_client)
    update_settings_request = odin_sdk.UpdateSettingsRequest() # UpdateSettingsRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Update Team Settings
        api_response = api_instance.update_team_settings_teams_settings_post(update_settings_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of UsersApi->update_team_settings_teams_settings_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->update_team_settings_teams_settings_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_settings_request** | [**UpdateSettingsRequest**](UpdateSettingsRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**RoutesUsersInsertModelResponse**](RoutesUsersInsertModelResponse.md)

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

# **update_team_users_team_update_post**
> AddTeamMembersResponse update_team_users_team_update_post(update_team_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Update Team

### Example


```python
import odin_sdk
from odin_sdk.models.add_team_members_response import AddTeamMembersResponse
from odin_sdk.models.update_team_request import UpdateTeamRequest
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
    api_instance = odin_sdk.UsersApi(api_client)
    update_team_request = odin_sdk.UpdateTeamRequest() # UpdateTeamRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Update Team
        api_response = api_instance.update_team_users_team_update_post(update_team_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of UsersApi->update_team_users_team_update_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->update_team_users_team_update_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_team_request** | [**UpdateTeamRequest**](UpdateTeamRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**AddTeamMembersResponse**](AddTeamMembersResponse.md)

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

# **update_user_credit_limit_users_teams_member_credit_limit_update_put**
> UpdateUserCreditLimitResponse update_user_credit_limit_users_teams_member_credit_limit_update_put(update_user_credit_limit_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Update User Credit Limit

Update credit limit for a specific team member

### Example


```python
import odin_sdk
from odin_sdk.models.update_user_credit_limit_request import UpdateUserCreditLimitRequest
from odin_sdk.models.update_user_credit_limit_response import UpdateUserCreditLimitResponse
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
    api_instance = odin_sdk.UsersApi(api_client)
    update_user_credit_limit_request = odin_sdk.UpdateUserCreditLimitRequest() # UpdateUserCreditLimitRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Update User Credit Limit
        api_response = api_instance.update_user_credit_limit_users_teams_member_credit_limit_update_put(update_user_credit_limit_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of UsersApi->update_user_credit_limit_users_teams_member_credit_limit_update_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->update_user_credit_limit_users_teams_member_credit_limit_update_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_user_credit_limit_request** | [**UpdateUserCreditLimitRequest**](UpdateUserCreditLimitRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**UpdateUserCreditLimitResponse**](UpdateUserCreditLimitResponse.md)

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

# **update_user_tags_v1_user_tags_post**
> UserTagResponse update_user_tags_v1_user_tags_post(user_tag_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Update User Tags

### Example


```python
import odin_sdk
from odin_sdk.models.user_tag_request import UserTagRequest
from odin_sdk.models.user_tag_response import UserTagResponse
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
    api_instance = odin_sdk.UsersApi(api_client)
    user_tag_request = odin_sdk.UserTagRequest() # UserTagRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Update User Tags
        api_response = api_instance.update_user_tags_v1_user_tags_post(user_tag_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of UsersApi->update_user_tags_v1_user_tags_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->update_user_tags_v1_user_tags_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_tag_request** | [**UserTagRequest**](UserTagRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**UserTagResponse**](UserTagResponse.md)

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

