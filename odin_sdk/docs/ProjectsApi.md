# odin_sdk.ProjectsApi

All URIs are relative to *http://127.0.0.1:8001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accept_project_invite_link_project_invite_link_accept_invite_id_post**](ProjectsApi.md#accept_project_invite_link_project_invite_link_accept_invite_id_post) | **POST** /project/invite-link/accept/{invite_id} | Accept Project Invite Link
[**accept_project_invite_project_invitation_accept_post**](ProjectsApi.md#accept_project_invite_project_invitation_accept_post) | **POST** /project/invitation/accept | Accept Project Invite
[**add_api_key_to_project_project_project_id_api_key_post**](ProjectsApi.md#add_api_key_to_project_project_project_id_api_key_post) | **POST** /project/{project_id}/api-key | Add Api Key To Project
[**add_user_to_project_project_user_add_post**](ProjectsApi.md#add_user_to_project_project_user_add_post) | **POST** /project/user/add | Add User To Project
[**check_project_kb_version_switch_status_project_kb_version_switch_project_id_status_get**](ProjectsApi.md#check_project_kb_version_switch_status_project_kb_version_switch_project_id_status_get) | **GET** /project/kb_version/switch/{project_id}/status | Check Project Kb Version Switch Status
[**clone_project_project_clone_post**](ProjectsApi.md#clone_project_project_clone_post) | **POST** /project/clone | Clone Project
[**confluence_login_project_integrations_confluence_login_get**](ProjectsApi.md#confluence_login_project_integrations_confluence_login_get) | **GET** /project/integrations/confluence/login | Confluence Login
[**create_project_project_create_post**](ProjectsApi.md#create_project_project_create_post) | **POST** /project/create | Create Project
[**create_sql_connection_project_integrations_sql_create_post**](ProjectsApi.md#create_sql_connection_project_integrations_sql_create_post) | **POST** /project/integrations/sql/create | Create Sql Connection
[**delete_confluence_oauth_project_integrations_confluence_oauth_delete**](ProjectsApi.md#delete_confluence_oauth_project_integrations_confluence_oauth_delete) | **DELETE** /project/integrations/confluence/oauth | Delete Confluence Oauth
[**delete_onprem_confluence_connector_info_project_integrations_onprem_confluence_connector_info_delete**](ProjectsApi.md#delete_onprem_confluence_connector_info_project_integrations_onprem_confluence_connector_info_delete) | **DELETE** /project/integrations/onprem_confluence/connector/info | Delete Onprem Confluence Connector Info
[**delete_project_project_delete_delete**](ProjectsApi.md#delete_project_project_delete_delete) | **DELETE** /project/delete | Delete Project
[**delete_sharepoint_oauth_project_integrations_sharepoint_oauth_delete**](ProjectsApi.md#delete_sharepoint_oauth_project_integrations_sharepoint_oauth_delete) | **DELETE** /project/integrations/sharepoint/oauth | Delete Sharepoint Oauth
[**delete_sql_connection_project_integrations_sql_delete_delete**](ProjectsApi.md#delete_sql_connection_project_integrations_sql_delete_delete) | **DELETE** /project/integrations/sql/delete | Delete Sql Connection
[**delete_user_from_project_project_user_delete_delete**](ProjectsApi.md#delete_user_from_project_project_user_delete_delete) | **DELETE** /project/user/delete | Delete User From Project
[**delete_zoomin_connector_info_project_integrations_zoomin_connector_info_delete**](ProjectsApi.md#delete_zoomin_connector_info_project_integrations_zoomin_connector_info_delete) | **DELETE** /project/integrations/zoomin/connector/info | Delete Zoomin Connector Info
[**download_exported_project_project_export_export_id_download_get**](ProjectsApi.md#download_exported_project_project_export_export_id_download_get) | **GET** /project/export/{export_id}/download | Download Exported Project
[**edit_project_user_project_user_edit_post**](ProjectsApi.md#edit_project_user_project_user_edit_post) | **POST** /project/user/edit | Edit Project User
[**export_project_credits_csv_project_enterprise_monthly_credit_export_post**](ProjectsApi.md#export_project_credits_csv_project_enterprise_monthly_credit_export_post) | **POST** /project/enterprise/monthly/credit/export | Export Project Credits Csv
[**export_project_project_export_post**](ProjectsApi.md#export_project_project_export_post) | **POST** /project/export | Export Project
[**fetch_sharepoint_oauth_for_user_project_integrations_sharepoint_oauth_project_id_get**](ProjectsApi.md#fetch_sharepoint_oauth_for_user_project_integrations_sharepoint_oauth_project_id_get) | **GET** /project/integrations/sharepoint/oauth/{project_id} | Fetch Sharepoint Oauth For User
[**generate_project_invite_link_project_invite_link_generate_post**](ProjectsApi.md#generate_project_invite_link_project_invite_link_generate_post) | **POST** /project/invite-link/generate | Generate Project Invite Link
[**get_affected_chats_count_when_enabling_retention_project_affected_chats_count_retention_post**](ProjectsApi.md#get_affected_chats_count_when_enabling_retention_project_affected_chats_count_retention_post) | **POST** /project/affected-chats-count-retention | Get Affected Chats Count When Enabling Retention
[**get_available_teams_for_project_project_project_id_teams_get**](ProjectsApi.md#get_available_teams_for_project_project_project_id_teams_get) | **GET** /project/{project_id}/teams | Get Available Teams For Project
[**get_credit_analytics_project_project_id_credit_analytics_get**](ProjectsApi.md#get_credit_analytics_project_project_id_credit_analytics_get) | **GET** /project/{project_id}/credit/analytics | Get Credit Analytics
[**get_credits_used_last_days_endpoint_project_project_id_credit_analytics_stats_get**](ProjectsApi.md#get_credits_used_last_days_endpoint_project_project_id_credit_analytics_stats_get) | **GET** /project/{project_id}/credit/analytics/stats | Get Credits Used Last Days Endpoint
[**get_difficulty_level_project_replan_agent_difficulty_level_get**](ProjectsApi.md#get_difficulty_level_project_replan_agent_difficulty_level_get) | **GET** /project/replan-agent/difficulty-level | Get Difficulty Level
[**get_document_chunks_project_project_id_document_chunks_post**](ProjectsApi.md#get_document_chunks_project_project_id_document_chunks_post) | **POST** /project/{project_id}/document/chunks | Get Document Chunks
[**get_export_signed_url_project_export_export_id_signed_url_get**](ProjectsApi.md#get_export_signed_url_project_export_export_id_signed_url_get) | **GET** /project/export/{export_id}/signed-url | Get Export Signed Url
[**get_export_status_project_export_export_id_status_get**](ProjectsApi.md#get_export_status_project_export_export_id_status_get) | **GET** /project/export/{export_id}/status | Get Export Status
[**get_favorites_project_favorites_get**](ProjectsApi.md#get_favorites_project_favorites_get) | **GET** /project/favorites | Get Favorites
[**get_knowledge_base_analytics_project_project_id_analytics_get**](ProjectsApi.md#get_knowledge_base_analytics_project_project_id_analytics_get) | **GET** /project/{project_id}/analytics | Get Knowledge Base Analytics
[**get_project_chatbot_project_project_id_chatbot_get**](ProjectsApi.md#get_project_chatbot_project_project_id_chatbot_get) | **GET** /project/{project_id}/chatbot | Get Project Chatbot
[**get_project_members_project_project_id_members_get**](ProjectsApi.md#get_project_members_project_project_id_members_get) | **GET** /project/{project_id}/members | Get Project Members
[**get_project_project_project_id_get**](ProjectsApi.md#get_project_project_project_id_get) | **GET** /project/{project_id} | Get Project
[**get_projects_projects_get**](ProjectsApi.md#get_projects_projects_get) | **GET** /projects | Get Projects
[**get_security_logs_project_project_id_security_logs_get**](ProjectsApi.md#get_security_logs_project_project_id_security_logs_get) | **GET** /project/{project_id}/security/logs | Get Security Logs
[**get_test_groups_project_project_id_test_groups_get**](ProjectsApi.md#get_test_groups_project_project_id_test_groups_get) | **GET** /project/{project_id}/test/groups | Get Test Groups
[**get_user_chats_for_project_project_project_id_chats_get**](ProjectsApi.md#get_user_chats_for_project_project_project_id_chats_get) | **GET** /project/{project_id}/chats | Get User Chats For Project
[**hybrid_search_v2_project_search_post**](ProjectsApi.md#hybrid_search_v2_project_search_post) | **POST** /v2/project/search | Hybrid  Search
[**import_project_project_import_post**](ProjectsApi.md#import_project_project_import_post) | **POST** /project/import | Import Project
[**link_shopify_store_project_integrations_shopify_link_post**](ProjectsApi.md#link_shopify_store_project_integrations_shopify_link_post) | **POST** /project/integrations/shopify/link | Link Shopify Store
[**save_onprem_confluence_connector_info_project_integrations_onprem_confluence_connector_info_post**](ProjectsApi.md#save_onprem_confluence_connector_info_project_integrations_onprem_confluence_connector_info_post) | **POST** /project/integrations/onprem_confluence/connector/info | Save Onprem Confluence Connector Info
[**save_zoomin_connector_info_project_integrations_zoomin_connector_info_post**](ProjectsApi.md#save_zoomin_connector_info_project_integrations_zoomin_connector_info_post) | **POST** /project/integrations/zoomin/connector/info | Save Zoomin Connector Info
[**search_google_articles_project_search_google_post**](ProjectsApi.md#search_google_articles_project_search_google_post) | **POST** /project/search/google | Search Google Articles
[**search_kb_documents_by_name_project_id_search_documents_post**](ProjectsApi.md#search_kb_documents_by_name_project_id_search_documents_post) | **POST** /project/{id}/search/documents | Search Kb Documents By Name
[**search_linkedin_profiles_project_search_linkedin_post**](ProjectsApi.md#search_linkedin_profiles_project_search_linkedin_post) | **POST** /project/search/linkedin | Search Linkedin Profiles
[**search_project_search_post**](ProjectsApi.md#search_project_search_post) | **POST** /project/search | Search
[**sharepoint_login_project_integrations_sharepoint_login_get**](ProjectsApi.md#sharepoint_login_project_integrations_sharepoint_login_get) | **GET** /project/integrations/sharepoint/login | Sharepoint Login
[**switch_project_kb_version_project_kb_version_switch_post**](ProjectsApi.md#switch_project_kb_version_project_kb_version_switch_post) | **POST** /project/kb_version/switch | Switch Project Kb Version
[**unlink_shopify_store_project_integrations_shopify_unlink_post**](ProjectsApi.md#unlink_shopify_store_project_integrations_shopify_unlink_post) | **POST** /project/integrations/shopify/unlink | Unlink Shopify Store
[**update_favorite_project_favorite_update_post**](ProjectsApi.md#update_favorite_project_favorite_update_post) | **POST** /project/favorite/update | Update Favorite
[**update_project_project_update_post**](ProjectsApi.md#update_project_project_update_post) | **POST** /project/update | Update Project
[**validate_project_invite_link_project_invite_link_validate_invite_id_get**](ProjectsApi.md#validate_project_invite_link_project_invite_link_validate_invite_id_get) | **GET** /project/invite-link/validate/{invite_id} | Validate Project Invite Link


# **accept_project_invite_link_project_invite_link_accept_invite_id_post**
> AcceptInviteLinkResponse accept_project_invite_link_project_invite_link_accept_invite_id_post(invite_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Accept Project Invite Link

Accept a project invitation via invite link.

### Example


```python
import odin_sdk
from odin_sdk.models.accept_invite_link_response import AcceptInviteLinkResponse
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
    invite_id = 'invite_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Accept Project Invite Link
        api_response = api_instance.accept_project_invite_link_project_invite_link_accept_invite_id_post(invite_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ProjectsApi->accept_project_invite_link_project_invite_link_accept_invite_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->accept_project_invite_link_project_invite_link_accept_invite_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invite_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**AcceptInviteLinkResponse**](AcceptInviteLinkResponse.md)

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

# **accept_project_invite_project_invitation_accept_post**
> AcceptProjectInviteResponse accept_project_invite_project_invitation_accept_post(accept_project_invite_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Accept Project Invite

Accepting the invite for a Project. Will add the user to the project.

### Example


```python
import odin_sdk
from odin_sdk.models.accept_project_invite_request import AcceptProjectInviteRequest
from odin_sdk.models.accept_project_invite_response import AcceptProjectInviteResponse
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
    accept_project_invite_request = odin_sdk.AcceptProjectInviteRequest() # AcceptProjectInviteRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Accept Project Invite
        api_response = api_instance.accept_project_invite_project_invitation_accept_post(accept_project_invite_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ProjectsApi->accept_project_invite_project_invitation_accept_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->accept_project_invite_project_invitation_accept_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_project_invite_request** | [**AcceptProjectInviteRequest**](AcceptProjectInviteRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**AcceptProjectInviteResponse**](AcceptProjectInviteResponse.md)

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

# **add_api_key_to_project_project_project_id_api_key_post**
> InsertKeyResponse add_api_key_to_project_project_project_id_api_key_post(project_id, insert_project_api_key_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Add Api Key To Project

### Example


```python
import odin_sdk
from odin_sdk.models.insert_key_response import InsertKeyResponse
from odin_sdk.models.insert_project_api_key_request import InsertProjectAPIKeyRequest
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
    insert_project_api_key_request = odin_sdk.InsertProjectAPIKeyRequest() # InsertProjectAPIKeyRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Add Api Key To Project
        api_response = api_instance.add_api_key_to_project_project_project_id_api_key_post(project_id, insert_project_api_key_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ProjectsApi->add_api_key_to_project_project_project_id_api_key_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->add_api_key_to_project_project_project_id_api_key_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **insert_project_api_key_request** | [**InsertProjectAPIKeyRequest**](InsertProjectAPIKeyRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**InsertKeyResponse**](InsertKeyResponse.md)

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

# **check_project_kb_version_switch_status_project_kb_version_switch_project_id_status_get**
> ProjectVersionSwitchStatusCheckResponse check_project_kb_version_switch_status_project_kb_version_switch_project_id_status_get(project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Check Project Kb Version Switch Status

Checks the status of the project KB version switch.

### Example


```python
import odin_sdk
from odin_sdk.models.project_version_switch_status_check_response import ProjectVersionSwitchStatusCheckResponse
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
        # Check Project Kb Version Switch Status
        api_response = api_instance.check_project_kb_version_switch_status_project_kb_version_switch_project_id_status_get(project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ProjectsApi->check_project_kb_version_switch_status_project_kb_version_switch_project_id_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->check_project_kb_version_switch_status_project_kb_version_switch_project_id_status_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**ProjectVersionSwitchStatusCheckResponse**](ProjectVersionSwitchStatusCheckResponse.md)

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

# **clone_project_project_clone_post**
> CloneProjectResponse clone_project_project_clone_post(clone_project_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Clone Project

Cloning a Project

### Example


```python
import odin_sdk
from odin_sdk.models.clone_project_request import CloneProjectRequest
from odin_sdk.models.clone_project_response import CloneProjectResponse
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
    clone_project_request = odin_sdk.CloneProjectRequest() # CloneProjectRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Clone Project
        api_response = api_instance.clone_project_project_clone_post(clone_project_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ProjectsApi->clone_project_project_clone_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->clone_project_project_clone_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clone_project_request** | [**CloneProjectRequest**](CloneProjectRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**CloneProjectResponse**](CloneProjectResponse.md)

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

# **confluence_login_project_integrations_confluence_login_get**
> IntegrationLoginRedirectResponse confluence_login_project_integrations_confluence_login_get(project_id, redirect_uri_from_callback, use_aa_auth=use_aa_auth, x_api_key=x_api_key, x_api_secret=x_api_secret)

Confluence Login

Provides URL to Atlassian login screen.

### Example


```python
import odin_sdk
from odin_sdk.models.integration_login_redirect_response import IntegrationLoginRedirectResponse
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
    redirect_uri_from_callback = 'redirect_uri_from_callback_example' # str | 
    use_aa_auth = 'false' # str |  (optional) (default to 'false')
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Confluence Login
        api_response = api_instance.confluence_login_project_integrations_confluence_login_get(project_id, redirect_uri_from_callback, use_aa_auth=use_aa_auth, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ProjectsApi->confluence_login_project_integrations_confluence_login_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->confluence_login_project_integrations_confluence_login_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **redirect_uri_from_callback** | **str**|  | 
 **use_aa_auth** | **str**|  | [optional] [default to &#39;false&#39;]
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**IntegrationLoginRedirectResponse**](IntegrationLoginRedirectResponse.md)

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

# **create_sql_connection_project_integrations_sql_create_post**
> CreateSQLConnectionResponse create_sql_connection_project_integrations_sql_create_post(create_sql_connection_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Create Sql Connection

Creates a new SQL connection for the project.

### Example


```python
import odin_sdk
from odin_sdk.models.create_sql_connection_request import CreateSQLConnectionRequest
from odin_sdk.models.create_sql_connection_response import CreateSQLConnectionResponse
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
    create_sql_connection_request = odin_sdk.CreateSQLConnectionRequest() # CreateSQLConnectionRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Create Sql Connection
        api_response = api_instance.create_sql_connection_project_integrations_sql_create_post(create_sql_connection_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ProjectsApi->create_sql_connection_project_integrations_sql_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->create_sql_connection_project_integrations_sql_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_sql_connection_request** | [**CreateSQLConnectionRequest**](CreateSQLConnectionRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**CreateSQLConnectionResponse**](CreateSQLConnectionResponse.md)

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

# **delete_confluence_oauth_project_integrations_confluence_oauth_delete**
> DeleteConfluenceOauthResponse delete_confluence_oauth_project_integrations_confluence_oauth_delete(delete_confluence_oauth_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Delete Confluence Oauth

Deletes the Confluence OAuth credentials per user, on the given project.

### Example


```python
import odin_sdk
from odin_sdk.models.delete_confluence_oauth_request import DeleteConfluenceOauthRequest
from odin_sdk.models.delete_confluence_oauth_response import DeleteConfluenceOauthResponse
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
    delete_confluence_oauth_request = odin_sdk.DeleteConfluenceOauthRequest() # DeleteConfluenceOauthRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Delete Confluence Oauth
        api_response = api_instance.delete_confluence_oauth_project_integrations_confluence_oauth_delete(delete_confluence_oauth_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ProjectsApi->delete_confluence_oauth_project_integrations_confluence_oauth_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->delete_confluence_oauth_project_integrations_confluence_oauth_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_confluence_oauth_request** | [**DeleteConfluenceOauthRequest**](DeleteConfluenceOauthRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**DeleteConfluenceOauthResponse**](DeleteConfluenceOauthResponse.md)

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

# **delete_onprem_confluence_connector_info_project_integrations_onprem_confluence_connector_info_delete**
> DeleteOnPremConfluenceConnectorInfoResponse delete_onprem_confluence_connector_info_project_integrations_onprem_confluence_connector_info_delete(delete_on_prem_confluence_connector_info_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Delete Onprem Confluence Connector Info

Deletes the OnPrem Confluence connector info for the given user, on the given project.

### Example


```python
import odin_sdk
from odin_sdk.models.delete_on_prem_confluence_connector_info_request import DeleteOnPremConfluenceConnectorInfoRequest
from odin_sdk.models.delete_on_prem_confluence_connector_info_response import DeleteOnPremConfluenceConnectorInfoResponse
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
    delete_on_prem_confluence_connector_info_request = odin_sdk.DeleteOnPremConfluenceConnectorInfoRequest() # DeleteOnPremConfluenceConnectorInfoRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Delete Onprem Confluence Connector Info
        api_response = api_instance.delete_onprem_confluence_connector_info_project_integrations_onprem_confluence_connector_info_delete(delete_on_prem_confluence_connector_info_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ProjectsApi->delete_onprem_confluence_connector_info_project_integrations_onprem_confluence_connector_info_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->delete_onprem_confluence_connector_info_project_integrations_onprem_confluence_connector_info_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_on_prem_confluence_connector_info_request** | [**DeleteOnPremConfluenceConnectorInfoRequest**](DeleteOnPremConfluenceConnectorInfoRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**DeleteOnPremConfluenceConnectorInfoResponse**](DeleteOnPremConfluenceConnectorInfoResponse.md)

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

# **delete_project_project_delete_delete**
> DeleteProjectResponse delete_project_project_delete_delete(delete_project_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Delete Project

Deletes a project.

### Example


```python
import odin_sdk
from odin_sdk.models.delete_project_request import DeleteProjectRequest
from odin_sdk.models.delete_project_response import DeleteProjectResponse
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
    delete_project_request = odin_sdk.DeleteProjectRequest() # DeleteProjectRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Delete Project
        api_response = api_instance.delete_project_project_delete_delete(delete_project_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ProjectsApi->delete_project_project_delete_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->delete_project_project_delete_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_project_request** | [**DeleteProjectRequest**](DeleteProjectRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**DeleteProjectResponse**](DeleteProjectResponse.md)

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

# **delete_sharepoint_oauth_project_integrations_sharepoint_oauth_delete**
> DeleteSharePointOAuthResponse delete_sharepoint_oauth_project_integrations_sharepoint_oauth_delete(delete_share_point_o_auth_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Delete Sharepoint Oauth

Deletes the SharePoint OAuth credentials per user, on the given project.

### Example


```python
import odin_sdk
from odin_sdk.models.delete_share_point_o_auth_request import DeleteSharePointOAuthRequest
from odin_sdk.models.delete_share_point_o_auth_response import DeleteSharePointOAuthResponse
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
    delete_share_point_o_auth_request = odin_sdk.DeleteSharePointOAuthRequest() # DeleteSharePointOAuthRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Delete Sharepoint Oauth
        api_response = api_instance.delete_sharepoint_oauth_project_integrations_sharepoint_oauth_delete(delete_share_point_o_auth_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ProjectsApi->delete_sharepoint_oauth_project_integrations_sharepoint_oauth_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->delete_sharepoint_oauth_project_integrations_sharepoint_oauth_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_share_point_o_auth_request** | [**DeleteSharePointOAuthRequest**](DeleteSharePointOAuthRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**DeleteSharePointOAuthResponse**](DeleteSharePointOAuthResponse.md)

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

# **delete_sql_connection_project_integrations_sql_delete_delete**
> DeleteSQLConnectionResponse delete_sql_connection_project_integrations_sql_delete_delete(delete_sql_connection_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Delete Sql Connection

Deletes the SQL connection for the project.

### Example


```python
import odin_sdk
from odin_sdk.models.delete_sql_connection_request import DeleteSQLConnectionRequest
from odin_sdk.models.delete_sql_connection_response import DeleteSQLConnectionResponse
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
    delete_sql_connection_request = odin_sdk.DeleteSQLConnectionRequest() # DeleteSQLConnectionRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Delete Sql Connection
        api_response = api_instance.delete_sql_connection_project_integrations_sql_delete_delete(delete_sql_connection_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ProjectsApi->delete_sql_connection_project_integrations_sql_delete_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->delete_sql_connection_project_integrations_sql_delete_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_sql_connection_request** | [**DeleteSQLConnectionRequest**](DeleteSQLConnectionRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**DeleteSQLConnectionResponse**](DeleteSQLConnectionResponse.md)

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

# **delete_user_from_project_project_user_delete_delete**
> DeleteUserResponse delete_user_from_project_project_user_delete_delete(delete_user_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Delete User From Project

Delete user from a Project.

### Example


```python
import odin_sdk
from odin_sdk.models.delete_user_request import DeleteUserRequest
from odin_sdk.models.delete_user_response import DeleteUserResponse
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
    delete_user_request = odin_sdk.DeleteUserRequest() # DeleteUserRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Delete User From Project
        api_response = api_instance.delete_user_from_project_project_user_delete_delete(delete_user_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ProjectsApi->delete_user_from_project_project_user_delete_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->delete_user_from_project_project_user_delete_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_user_request** | [**DeleteUserRequest**](DeleteUserRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**DeleteUserResponse**](DeleteUserResponse.md)

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

# **delete_zoomin_connector_info_project_integrations_zoomin_connector_info_delete**
> DeleteZoominConnectorInfoResponse delete_zoomin_connector_info_project_integrations_zoomin_connector_info_delete(delete_zoomin_connector_info_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Delete Zoomin Connector Info

Deletes the Zoomin connector info for the given user, on the given project.

### Example


```python
import odin_sdk
from odin_sdk.models.delete_zoomin_connector_info_request import DeleteZoominConnectorInfoRequest
from odin_sdk.models.delete_zoomin_connector_info_response import DeleteZoominConnectorInfoResponse
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
    delete_zoomin_connector_info_request = odin_sdk.DeleteZoominConnectorInfoRequest() # DeleteZoominConnectorInfoRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Delete Zoomin Connector Info
        api_response = api_instance.delete_zoomin_connector_info_project_integrations_zoomin_connector_info_delete(delete_zoomin_connector_info_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ProjectsApi->delete_zoomin_connector_info_project_integrations_zoomin_connector_info_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->delete_zoomin_connector_info_project_integrations_zoomin_connector_info_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_zoomin_connector_info_request** | [**DeleteZoominConnectorInfoRequest**](DeleteZoominConnectorInfoRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**DeleteZoominConnectorInfoResponse**](DeleteZoominConnectorInfoResponse.md)

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

# **download_exported_project_project_export_export_id_download_get**
> download_exported_project_project_export_export_id_download_get(export_id)

Download Exported Project

Download exported project zip

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
    api_instance = odin_sdk.ProjectsApi(api_client)
    export_id = 'export_id_example' # str | 

    try:
        # Download Exported Project
        api_instance.download_exported_project_project_export_export_id_download_get(export_id)
    except Exception as e:
        print("Exception when calling ProjectsApi->download_exported_project_project_export_export_id_download_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **export_id** | **str**|  | 

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

# **export_project_credits_csv_project_enterprise_monthly_credit_export_post**
> export_project_credits_csv_project_enterprise_monthly_credit_export_post(credit_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Export Project Credits Csv

### Example


```python
import odin_sdk
from odin_sdk.models.credit_request import CreditRequest
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
    credit_request = odin_sdk.CreditRequest() # CreditRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Export Project Credits Csv
        api_instance.export_project_credits_csv_project_enterprise_monthly_credit_export_post(credit_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
    except Exception as e:
        print("Exception when calling ProjectsApi->export_project_credits_csv_project_enterprise_monthly_credit_export_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_request** | [**CreditRequest**](CreditRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

void (empty response body)

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

# **export_project_project_export_post**
> object export_project_project_export_post(export_project_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Export Project

Export project as zip file and return signed download URL

### Example


```python
import odin_sdk
from odin_sdk.models.export_project_request import ExportProjectRequest
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
    export_project_request = odin_sdk.ExportProjectRequest() # ExportProjectRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Export Project
        api_response = api_instance.export_project_project_export_post(export_project_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ProjectsApi->export_project_project_export_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->export_project_project_export_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **export_project_request** | [**ExportProjectRequest**](ExportProjectRequest.md)|  | 
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

# **fetch_sharepoint_oauth_for_user_project_integrations_sharepoint_oauth_project_id_get**
> SharePointOauthData fetch_sharepoint_oauth_for_user_project_integrations_sharepoint_oauth_project_id_get(project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Fetch Sharepoint Oauth For User

Fetches the SharePoint OAuth credentials for given user, on the given project.

### Example


```python
import odin_sdk
from odin_sdk.models.share_point_oauth_data import SharePointOauthData
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
        # Fetch Sharepoint Oauth For User
        api_response = api_instance.fetch_sharepoint_oauth_for_user_project_integrations_sharepoint_oauth_project_id_get(project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ProjectsApi->fetch_sharepoint_oauth_for_user_project_integrations_sharepoint_oauth_project_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->fetch_sharepoint_oauth_for_user_project_integrations_sharepoint_oauth_project_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**SharePointOauthData**](SharePointOauthData.md)

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

# **generate_project_invite_link_project_invite_link_generate_post**
> GenerateInviteLinkResponse generate_project_invite_link_project_invite_link_generate_post(generate_invite_link_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Generate Project Invite Link

Generate a shareable invite link for a project with a specific role.

### Example


```python
import odin_sdk
from odin_sdk.models.generate_invite_link_request import GenerateInviteLinkRequest
from odin_sdk.models.generate_invite_link_response import GenerateInviteLinkResponse
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
    generate_invite_link_request = odin_sdk.GenerateInviteLinkRequest() # GenerateInviteLinkRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Generate Project Invite Link
        api_response = api_instance.generate_project_invite_link_project_invite_link_generate_post(generate_invite_link_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ProjectsApi->generate_project_invite_link_project_invite_link_generate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->generate_project_invite_link_project_invite_link_generate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_invite_link_request** | [**GenerateInviteLinkRequest**](GenerateInviteLinkRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**GenerateInviteLinkResponse**](GenerateInviteLinkResponse.md)

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

# **get_affected_chats_count_when_enabling_retention_project_affected_chats_count_retention_post**
> GetAffectedChatsCountWhenEnablingRetentionResponse get_affected_chats_count_when_enabling_retention_project_affected_chats_count_retention_post(get_affected_chats_count_when_enabling_retention_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Affected Chats Count When Enabling Retention

Get the count of affected chats when enabling retention

### Example


```python
import odin_sdk
from odin_sdk.models.get_affected_chats_count_when_enabling_retention_request import GetAffectedChatsCountWhenEnablingRetentionRequest
from odin_sdk.models.get_affected_chats_count_when_enabling_retention_response import GetAffectedChatsCountWhenEnablingRetentionResponse
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
    get_affected_chats_count_when_enabling_retention_request = odin_sdk.GetAffectedChatsCountWhenEnablingRetentionRequest() # GetAffectedChatsCountWhenEnablingRetentionRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Affected Chats Count When Enabling Retention
        api_response = api_instance.get_affected_chats_count_when_enabling_retention_project_affected_chats_count_retention_post(get_affected_chats_count_when_enabling_retention_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ProjectsApi->get_affected_chats_count_when_enabling_retention_project_affected_chats_count_retention_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_affected_chats_count_when_enabling_retention_project_affected_chats_count_retention_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_affected_chats_count_when_enabling_retention_request** | [**GetAffectedChatsCountWhenEnablingRetentionRequest**](GetAffectedChatsCountWhenEnablingRetentionRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**GetAffectedChatsCountWhenEnablingRetentionResponse**](GetAffectedChatsCountWhenEnablingRetentionResponse.md)

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

# **get_available_teams_for_project_project_project_id_teams_get**
> List[object] get_available_teams_for_project_project_project_id_teams_get(project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Available Teams For Project

Get teams available for project assignment

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
    api_instance = odin_sdk.ProjectsApi(api_client)
    project_id = 'project_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Available Teams For Project
        api_response = api_instance.get_available_teams_for_project_project_project_id_teams_get(project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ProjectsApi->get_available_teams_for_project_project_project_id_teams_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_available_teams_for_project_project_project_id_teams_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

**List[object]**

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

# **get_credit_analytics_project_project_id_credit_analytics_get**
> CreditAnalyticsResponse get_credit_analytics_project_project_id_credit_analytics_get(project_id, timestamp=timestamp, email=email, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Credit Analytics

Shows the analytics of the credits used.

### Example


```python
import odin_sdk
from odin_sdk.models.credit_analytics_response import CreditAnalyticsResponse
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
    timestamp = 3.4 # float |  (optional)
    email = 'email_example' # str |  (optional)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Credit Analytics
        api_response = api_instance.get_credit_analytics_project_project_id_credit_analytics_get(project_id, timestamp=timestamp, email=email, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ProjectsApi->get_credit_analytics_project_project_id_credit_analytics_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_credit_analytics_project_project_id_credit_analytics_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **timestamp** | **float**|  | [optional] 
 **email** | **str**|  | [optional] 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**CreditAnalyticsResponse**](CreditAnalyticsResponse.md)

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

# **get_credits_used_last_days_endpoint_project_project_id_credit_analytics_stats_get**
> CreditDaysResponse get_credits_used_last_days_endpoint_project_project_id_credit_analytics_stats_get(project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Credits Used Last Days Endpoint

Shows the analytics of the credits used for a certain amount of days.

### Example


```python
import odin_sdk
from odin_sdk.models.credit_days_response import CreditDaysResponse
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
        # Get Credits Used Last Days Endpoint
        api_response = api_instance.get_credits_used_last_days_endpoint_project_project_id_credit_analytics_stats_get(project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ProjectsApi->get_credits_used_last_days_endpoint_project_project_id_credit_analytics_stats_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_credits_used_last_days_endpoint_project_project_id_credit_analytics_stats_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**CreditDaysResponse**](CreditDaysResponse.md)

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

# **get_difficulty_level_project_replan_agent_difficulty_level_get**
> AgentDifficultyLevelResponse get_difficulty_level_project_replan_agent_difficulty_level_get()

Get Difficulty Level

Difficulty level of the agent

### Example


```python
import odin_sdk
from odin_sdk.models.agent_difficulty_level_response import AgentDifficultyLevelResponse
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

    try:
        # Get Difficulty Level
        api_response = api_instance.get_difficulty_level_project_replan_agent_difficulty_level_get()
        print("The response of ProjectsApi->get_difficulty_level_project_replan_agent_difficulty_level_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_difficulty_level_project_replan_agent_difficulty_level_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AgentDifficultyLevelResponse**](AgentDifficultyLevelResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_chunks_project_project_id_document_chunks_post**
> GetDocumentChunksResponse get_document_chunks_project_project_id_document_chunks_post(project_id, get_document_chunks_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Document Chunks

Get paginated content chunks for a specific document in the knowledge base.

### Example


```python
import odin_sdk
from odin_sdk.models.get_document_chunks_request import GetDocumentChunksRequest
from odin_sdk.models.get_document_chunks_response import GetDocumentChunksResponse
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
    get_document_chunks_request = odin_sdk.GetDocumentChunksRequest() # GetDocumentChunksRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Document Chunks
        api_response = api_instance.get_document_chunks_project_project_id_document_chunks_post(project_id, get_document_chunks_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ProjectsApi->get_document_chunks_project_project_id_document_chunks_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_document_chunks_project_project_id_document_chunks_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **get_document_chunks_request** | [**GetDocumentChunksRequest**](GetDocumentChunksRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**GetDocumentChunksResponse**](GetDocumentChunksResponse.md)

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

# **get_export_signed_url_project_export_export_id_signed_url_get**
> object get_export_signed_url_project_export_export_id_signed_url_get(export_id)

Get Export Signed Url

Get signed URL for direct download from Supabase storage

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
    api_instance = odin_sdk.ProjectsApi(api_client)
    export_id = 'export_id_example' # str | 

    try:
        # Get Export Signed Url
        api_response = api_instance.get_export_signed_url_project_export_export_id_signed_url_get(export_id)
        print("The response of ProjectsApi->get_export_signed_url_project_export_export_id_signed_url_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_export_signed_url_project_export_export_id_signed_url_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **export_id** | **str**|  | 

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

# **get_export_status_project_export_export_id_status_get**
> ExportStatusResponse get_export_status_project_export_export_id_status_get(export_id)

Get Export Status

Check export status

### Example


```python
import odin_sdk
from odin_sdk.models.export_status_response import ExportStatusResponse
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
    export_id = 'export_id_example' # str | 

    try:
        # Get Export Status
        api_response = api_instance.get_export_status_project_export_export_id_status_get(export_id)
        print("The response of ProjectsApi->get_export_status_project_export_export_id_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_export_status_project_export_export_id_status_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **export_id** | **str**|  | 

### Return type

[**ExportStatusResponse**](ExportStatusResponse.md)

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

# **get_favorites_project_favorites_get**
> GetFavoriteResponse get_favorites_project_favorites_get(x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Favorites

Show all projects that where are added to favorites

### Example


```python
import odin_sdk
from odin_sdk.models.get_favorite_response import GetFavoriteResponse
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
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Favorites
        api_response = api_instance.get_favorites_project_favorites_get(x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ProjectsApi->get_favorites_project_favorites_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_favorites_project_favorites_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**GetFavoriteResponse**](GetFavoriteResponse.md)

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

# **get_knowledge_base_analytics_project_project_id_analytics_get**
> KnowledgeBaseAnalyticsResponse get_knowledge_base_analytics_project_project_id_analytics_get(project_id, days=days, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Knowledge Base Analytics

Provide the statistics related to the Knowledge Base's usage.

### Example


```python
import odin_sdk
from odin_sdk.models.knowledge_base_analytics_response import KnowledgeBaseAnalyticsResponse
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
    days = 56 # int |  (optional)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Knowledge Base Analytics
        api_response = api_instance.get_knowledge_base_analytics_project_project_id_analytics_get(project_id, days=days, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ProjectsApi->get_knowledge_base_analytics_project_project_id_analytics_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_knowledge_base_analytics_project_project_id_analytics_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **days** | **int**|  | [optional] 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**KnowledgeBaseAnalyticsResponse**](KnowledgeBaseAnalyticsResponse.md)

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

# **get_project_chatbot_project_project_id_chatbot_get**
> GetChatbotResponse get_project_chatbot_project_project_id_chatbot_get(project_id)

Get Project Chatbot

Get the Project's chatbot data by ID.

### Example


```python
import odin_sdk
from odin_sdk.models.get_chatbot_response import GetChatbotResponse
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

    try:
        # Get Project Chatbot
        api_response = api_instance.get_project_chatbot_project_project_id_chatbot_get(project_id)
        print("The response of ProjectsApi->get_project_chatbot_project_project_id_chatbot_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_project_chatbot_project_project_id_chatbot_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 

### Return type

[**GetChatbotResponse**](GetChatbotResponse.md)

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

# **get_project_project_project_id_get**
> GetProjectResponse get_project_project_project_id_get(project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Project

Get the Project by ID.

### Example


```python
import odin_sdk
from odin_sdk.models.get_project_response import GetProjectResponse
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
        # Get Project
        api_response = api_instance.get_project_project_project_id_get(project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ProjectsApi->get_project_project_project_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_project_project_project_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**GetProjectResponse**](GetProjectResponse.md)

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

# **get_security_logs_project_project_id_security_logs_get**
> SecurityLogsResponse get_security_logs_project_project_id_security_logs_get(project_id, timestamp=timestamp, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Security Logs

Shows the security logs information.

### Example


```python
import odin_sdk
from odin_sdk.models.security_logs_response import SecurityLogsResponse
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
    timestamp = 3.4 # float |  (optional)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Security Logs
        api_response = api_instance.get_security_logs_project_project_id_security_logs_get(project_id, timestamp=timestamp, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ProjectsApi->get_security_logs_project_project_id_security_logs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_security_logs_project_project_id_security_logs_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **timestamp** | **float**|  | [optional] 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**SecurityLogsResponse**](SecurityLogsResponse.md)

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

# **get_test_groups_project_project_id_test_groups_get**
> GetTestGroupsResponse get_test_groups_project_project_id_test_groups_get(project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Test Groups

Gets the Test Groups.

### Example


```python
import odin_sdk
from odin_sdk.models.get_test_groups_response import GetTestGroupsResponse
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
        # Get Test Groups
        api_response = api_instance.get_test_groups_project_project_id_test_groups_get(project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ProjectsApi->get_test_groups_project_project_id_test_groups_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_test_groups_project_project_id_test_groups_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**GetTestGroupsResponse**](GetTestGroupsResponse.md)

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

# **get_user_chats_for_project_project_project_id_chats_get**
> GetAllChatsResponse get_user_chats_for_project_project_project_id_chats_get(project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get User Chats For Project

Get all the chat responses of the Project ID.

### Example


```python
import odin_sdk
from odin_sdk.models.get_all_chats_response import GetAllChatsResponse
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
        # Get User Chats For Project
        api_response = api_instance.get_user_chats_for_project_project_project_id_chats_get(project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ProjectsApi->get_user_chats_for_project_project_project_id_chats_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_user_chats_for_project_project_project_id_chats_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**GetAllChatsResponse**](GetAllChatsResponse.md)

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

# **hybrid_search_v2_project_search_post**
> ProjectSearchResponse hybrid_search_v2_project_search_post(project_search_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Hybrid  Search

Searches through Projects Knowledgebase.

### Example


```python
import odin_sdk
from odin_sdk.models.project_search_request import ProjectSearchRequest
from odin_sdk.models.project_search_response import ProjectSearchResponse
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
    project_search_request = odin_sdk.ProjectSearchRequest() # ProjectSearchRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Hybrid  Search
        api_response = api_instance.hybrid_search_v2_project_search_post(project_search_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ProjectsApi->hybrid_search_v2_project_search_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->hybrid_search_v2_project_search_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_search_request** | [**ProjectSearchRequest**](ProjectSearchRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**ProjectSearchResponse**](ProjectSearchResponse.md)

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

# **import_project_project_import_post**
> ImportProjectResponse import_project_project_import_post(file, new_project_name, x_api_key=x_api_key, x_api_secret=x_api_secret)

Import Project

Import project from zip file

### Example


```python
import odin_sdk
from odin_sdk.models.import_project_response import ImportProjectResponse
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
    file = None # bytearray | 
    new_project_name = 'new_project_name_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Import Project
        api_response = api_instance.import_project_project_import_post(file, new_project_name, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ProjectsApi->import_project_project_import_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->import_project_project_import_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**|  | 
 **new_project_name** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**ImportProjectResponse**](ImportProjectResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_shopify_store_project_integrations_shopify_link_post**
> LinkShopifyStoreResponse link_shopify_store_project_integrations_shopify_link_post(link_shopify_store_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Link Shopify Store

Links the Shopify Store domain to ODIN AI.

### Example


```python
import odin_sdk
from odin_sdk.models.link_shopify_store_request import LinkShopifyStoreRequest
from odin_sdk.models.link_shopify_store_response import LinkShopifyStoreResponse
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
    link_shopify_store_request = odin_sdk.LinkShopifyStoreRequest() # LinkShopifyStoreRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Link Shopify Store
        api_response = api_instance.link_shopify_store_project_integrations_shopify_link_post(link_shopify_store_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ProjectsApi->link_shopify_store_project_integrations_shopify_link_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->link_shopify_store_project_integrations_shopify_link_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **link_shopify_store_request** | [**LinkShopifyStoreRequest**](LinkShopifyStoreRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**LinkShopifyStoreResponse**](LinkShopifyStoreResponse.md)

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

# **save_onprem_confluence_connector_info_project_integrations_onprem_confluence_connector_info_post**
> SaveOnPremConfluenceConnectorInfoResponse save_onprem_confluence_connector_info_project_integrations_onprem_confluence_connector_info_post(save_on_prem_confluence_connector_info_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Save Onprem Confluence Connector Info

Saves the OnPrem Confluence connector info for the given user, on the given project.

### Example


```python
import odin_sdk
from odin_sdk.models.save_on_prem_confluence_connector_info_request import SaveOnPremConfluenceConnectorInfoRequest
from odin_sdk.models.save_on_prem_confluence_connector_info_response import SaveOnPremConfluenceConnectorInfoResponse
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
    save_on_prem_confluence_connector_info_request = odin_sdk.SaveOnPremConfluenceConnectorInfoRequest() # SaveOnPremConfluenceConnectorInfoRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Save Onprem Confluence Connector Info
        api_response = api_instance.save_onprem_confluence_connector_info_project_integrations_onprem_confluence_connector_info_post(save_on_prem_confluence_connector_info_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ProjectsApi->save_onprem_confluence_connector_info_project_integrations_onprem_confluence_connector_info_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->save_onprem_confluence_connector_info_project_integrations_onprem_confluence_connector_info_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **save_on_prem_confluence_connector_info_request** | [**SaveOnPremConfluenceConnectorInfoRequest**](SaveOnPremConfluenceConnectorInfoRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**SaveOnPremConfluenceConnectorInfoResponse**](SaveOnPremConfluenceConnectorInfoResponse.md)

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

# **save_zoomin_connector_info_project_integrations_zoomin_connector_info_post**
> SaveZoominConnectorInfoResponse save_zoomin_connector_info_project_integrations_zoomin_connector_info_post(save_zoomin_connector_info_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Save Zoomin Connector Info

Saves the Zoomin connector info for the given user, on the given project.

### Example


```python
import odin_sdk
from odin_sdk.models.save_zoomin_connector_info_request import SaveZoominConnectorInfoRequest
from odin_sdk.models.save_zoomin_connector_info_response import SaveZoominConnectorInfoResponse
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
    save_zoomin_connector_info_request = odin_sdk.SaveZoominConnectorInfoRequest() # SaveZoominConnectorInfoRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Save Zoomin Connector Info
        api_response = api_instance.save_zoomin_connector_info_project_integrations_zoomin_connector_info_post(save_zoomin_connector_info_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ProjectsApi->save_zoomin_connector_info_project_integrations_zoomin_connector_info_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->save_zoomin_connector_info_project_integrations_zoomin_connector_info_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **save_zoomin_connector_info_request** | [**SaveZoominConnectorInfoRequest**](SaveZoominConnectorInfoRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**SaveZoominConnectorInfoResponse**](SaveZoominConnectorInfoResponse.md)

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

# **search_google_articles_project_search_google_post**
> GoogleSearchArticlesResponse search_google_articles_project_search_google_post(google_search_articles_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Search Google Articles

Search and retrieve articles via a Google query

### Example


```python
import odin_sdk
from odin_sdk.models.google_search_articles_request import GoogleSearchArticlesRequest
from odin_sdk.models.google_search_articles_response import GoogleSearchArticlesResponse
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
    google_search_articles_request = odin_sdk.GoogleSearchArticlesRequest() # GoogleSearchArticlesRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Search Google Articles
        api_response = api_instance.search_google_articles_project_search_google_post(google_search_articles_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ProjectsApi->search_google_articles_project_search_google_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->search_google_articles_project_search_google_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **google_search_articles_request** | [**GoogleSearchArticlesRequest**](GoogleSearchArticlesRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**GoogleSearchArticlesResponse**](GoogleSearchArticlesResponse.md)

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

# **search_kb_documents_by_name_project_id_search_documents_post**
> SearchKBDocumentsByNameResponse search_kb_documents_by_name_project_id_search_documents_post(id, search_kb_documents_by_name_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Search Kb Documents By Name

Look up document metadata in KB by partial names.

### Example


```python
import odin_sdk
from odin_sdk.models.search_kb_documents_by_name_request import SearchKBDocumentsByNameRequest
from odin_sdk.models.search_kb_documents_by_name_response import SearchKBDocumentsByNameResponse
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
    id = 'id_example' # str | Project ID on which to perform the search.
    search_kb_documents_by_name_request = odin_sdk.SearchKBDocumentsByNameRequest() # SearchKBDocumentsByNameRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Search Kb Documents By Name
        api_response = api_instance.search_kb_documents_by_name_project_id_search_documents_post(id, search_kb_documents_by_name_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ProjectsApi->search_kb_documents_by_name_project_id_search_documents_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->search_kb_documents_by_name_project_id_search_documents_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project ID on which to perform the search. | 
 **search_kb_documents_by_name_request** | [**SearchKBDocumentsByNameRequest**](SearchKBDocumentsByNameRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**SearchKBDocumentsByNameResponse**](SearchKBDocumentsByNameResponse.md)

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

# **search_linkedin_profiles_project_search_linkedin_post**
> LinkedInSearchResponse search_linkedin_profiles_project_search_linkedin_post(linked_in_scrape_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Search Linkedin Profiles

Search and retrieve LinkedIn profiles via SERPAPI

### Example


```python
import odin_sdk
from odin_sdk.models.linked_in_scrape_request import LinkedInScrapeRequest
from odin_sdk.models.linked_in_search_response import LinkedInSearchResponse
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
    linked_in_scrape_request = odin_sdk.LinkedInScrapeRequest() # LinkedInScrapeRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Search Linkedin Profiles
        api_response = api_instance.search_linkedin_profiles_project_search_linkedin_post(linked_in_scrape_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ProjectsApi->search_linkedin_profiles_project_search_linkedin_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->search_linkedin_profiles_project_search_linkedin_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **linked_in_scrape_request** | [**LinkedInScrapeRequest**](LinkedInScrapeRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**LinkedInSearchResponse**](LinkedInSearchResponse.md)

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

# **search_project_search_post**
> ProjectSearchResponse search_project_search_post(project_search_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Search

Searches through Projects.

### Example


```python
import odin_sdk
from odin_sdk.models.project_search_request import ProjectSearchRequest
from odin_sdk.models.project_search_response import ProjectSearchResponse
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
    project_search_request = odin_sdk.ProjectSearchRequest() # ProjectSearchRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Search
        api_response = api_instance.search_project_search_post(project_search_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ProjectsApi->search_project_search_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->search_project_search_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_search_request** | [**ProjectSearchRequest**](ProjectSearchRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**ProjectSearchResponse**](ProjectSearchResponse.md)

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

# **sharepoint_login_project_integrations_sharepoint_login_get**
> IntegrationLoginRedirectResponse sharepoint_login_project_integrations_sharepoint_login_get(project_id, redirect_uri_from_callback, use_aa_auth=use_aa_auth, x_api_key=x_api_key, x_api_secret=x_api_secret)

Sharepoint Login

Provides URL to Microsoft(Azure) login screen.

### Example


```python
import odin_sdk
from odin_sdk.models.integration_login_redirect_response import IntegrationLoginRedirectResponse
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
    redirect_uri_from_callback = 'redirect_uri_from_callback_example' # str | 
    use_aa_auth = 'false' # str |  (optional) (default to 'false')
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Sharepoint Login
        api_response = api_instance.sharepoint_login_project_integrations_sharepoint_login_get(project_id, redirect_uri_from_callback, use_aa_auth=use_aa_auth, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ProjectsApi->sharepoint_login_project_integrations_sharepoint_login_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->sharepoint_login_project_integrations_sharepoint_login_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **redirect_uri_from_callback** | **str**|  | 
 **use_aa_auth** | **str**|  | [optional] [default to &#39;false&#39;]
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**IntegrationLoginRedirectResponse**](IntegrationLoginRedirectResponse.md)

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

# **switch_project_kb_version_project_kb_version_switch_post**
> ProjectVersionSwitchResponse switch_project_kb_version_project_kb_version_switch_post(project_version_switch_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Switch Project Kb Version

Switches the project KB version.

### Example


```python
import odin_sdk
from odin_sdk.models.project_version_switch_request import ProjectVersionSwitchRequest
from odin_sdk.models.project_version_switch_response import ProjectVersionSwitchResponse
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
    project_version_switch_request = odin_sdk.ProjectVersionSwitchRequest() # ProjectVersionSwitchRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Switch Project Kb Version
        api_response = api_instance.switch_project_kb_version_project_kb_version_switch_post(project_version_switch_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ProjectsApi->switch_project_kb_version_project_kb_version_switch_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->switch_project_kb_version_project_kb_version_switch_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_version_switch_request** | [**ProjectVersionSwitchRequest**](ProjectVersionSwitchRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**ProjectVersionSwitchResponse**](ProjectVersionSwitchResponse.md)

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

# **unlink_shopify_store_project_integrations_shopify_unlink_post**
> UnlinkShopifyStoreResponse unlink_shopify_store_project_integrations_shopify_unlink_post(unlink_shopify_store_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Unlink Shopify Store

Unlinks the Shopify Store domain from ODIN AI.

### Example


```python
import odin_sdk
from odin_sdk.models.unlink_shopify_store_request import UnlinkShopifyStoreRequest
from odin_sdk.models.unlink_shopify_store_response import UnlinkShopifyStoreResponse
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
    unlink_shopify_store_request = odin_sdk.UnlinkShopifyStoreRequest() # UnlinkShopifyStoreRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Unlink Shopify Store
        api_response = api_instance.unlink_shopify_store_project_integrations_shopify_unlink_post(unlink_shopify_store_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ProjectsApi->unlink_shopify_store_project_integrations_shopify_unlink_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->unlink_shopify_store_project_integrations_shopify_unlink_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unlink_shopify_store_request** | [**UnlinkShopifyStoreRequest**](UnlinkShopifyStoreRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**UnlinkShopifyStoreResponse**](UnlinkShopifyStoreResponse.md)

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

# **update_favorite_project_favorite_update_post**
> AddFavoriteResponse update_favorite_project_favorite_update_post(add_favorite_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Update Favorite

Add a project as favorite

### Example


```python
import odin_sdk
from odin_sdk.models.add_favorite_request import AddFavoriteRequest
from odin_sdk.models.add_favorite_response import AddFavoriteResponse
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
    add_favorite_request = odin_sdk.AddFavoriteRequest() # AddFavoriteRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Update Favorite
        api_response = api_instance.update_favorite_project_favorite_update_post(add_favorite_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ProjectsApi->update_favorite_project_favorite_update_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->update_favorite_project_favorite_update_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_favorite_request** | [**AddFavoriteRequest**](AddFavoriteRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**AddFavoriteResponse**](AddFavoriteResponse.md)

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

# **validate_project_invite_link_project_invite_link_validate_invite_id_get**
> ValidateInviteLinkResponse validate_project_invite_link_project_invite_link_validate_invite_id_get(invite_id)

Validate Project Invite Link

Validate an invite link and get project information including role.

### Example


```python
import odin_sdk
from odin_sdk.models.validate_invite_link_response import ValidateInviteLinkResponse
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
    invite_id = 'invite_id_example' # str | 

    try:
        # Validate Project Invite Link
        api_response = api_instance.validate_project_invite_link_project_invite_link_validate_invite_id_get(invite_id)
        print("The response of ProjectsApi->validate_project_invite_link_project_invite_link_validate_invite_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->validate_project_invite_link_project_invite_link_validate_invite_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invite_id** | **str**|  | 

### Return type

[**ValidateInviteLinkResponse**](ValidateInviteLinkResponse.md)

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

