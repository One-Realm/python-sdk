# odin_sdk.DefaultApi

All URIs are relative to *http://127.0.0.1:8001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**compare_documents_action_default_compare_documents_post**](DefaultApi.md#compare_documents_action_default_compare_documents_post) | **POST** /action/default/compare/documents | Compare Documents
[**create_bot_package_teams_create_bot_package_post**](DefaultApi.md#create_bot_package_teams_create_bot_package_post) | **POST** /teams/create_bot_package | Create Bot Package
[**create_custom_app_custom_apps_project_id_create_post**](DefaultApi.md#create_custom_app_custom_apps_project_id_create_post) | **POST** /custom_apps/{project_id}/create | Create Custom App
[**create_project_mcp_mcp_project_id_create_post**](DefaultApi.md#create_project_mcp_mcp_project_id_create_post) | **POST** /mcp/{project_id}/create | Create a new MCP connection
[**delete_asana_integration_user_integrations_asana_delete**](DefaultApi.md#delete_asana_integration_user_integrations_asana_delete) | **DELETE** /user/integrations/asana | Delete Asana Integration
[**delete_context_from_chat_v3_chat_context_delete**](DefaultApi.md#delete_context_from_chat_v3_chat_context_delete) | **DELETE** /v3/chat/context | Delete Context From Chat
[**delete_custom_app_custom_apps_project_id_app_id_delete**](DefaultApi.md#delete_custom_app_custom_apps_project_id_app_id_delete) | **DELETE** /custom_apps/{project_id}/{app_id} | Delete Custom App
[**delete_jira_integration_user_integrations_jira_delete**](DefaultApi.md#delete_jira_integration_user_integrations_jira_delete) | **DELETE** /user/integrations/jira | Delete Jira Integration
[**delete_project_mcp_mcp_project_id_delete_mcp_id_delete**](DefaultApi.md#delete_project_mcp_mcp_project_id_delete_mcp_id_delete) | **DELETE** /mcp/{project_id}/delete/{mcp_id} | Delete an MCP connection
[**delete_salesforce_integration_user_integrations_salesforce_delete**](DefaultApi.md#delete_salesforce_integration_user_integrations_salesforce_delete) | **DELETE** /user/integrations/salesforce | Delete Salesforce Integration
[**download_usage_report_reports_usage_report_report_uuid_download_get**](DefaultApi.md#download_usage_report_reports_usage_report_report_uuid_download_get) | **GET** /reports/usage_report/{report_uuid}/download | Download Usage Report
[**edit_custom_app_custom_apps_project_id_settings_edit_post**](DefaultApi.md#edit_custom_app_custom_apps_project_id_settings_edit_post) | **POST** /custom_apps/{project_id}/settings/edit | Edit Custom App
[**fetch_all_user_level_integrations_for_user_user_integrations_get**](DefaultApi.md#fetch_all_user_level_integrations_for_user_user_integrations_get) | **GET** /user/integrations | Fetch All User Level Integrations For User
[**force_refresh_asana_token_endpoint_user_integrations_asana_force_refresh_post**](DefaultApi.md#force_refresh_asana_token_endpoint_user_integrations_asana_force_refresh_post) | **POST** /user/integrations/asana/force-refresh | Force Refresh Asana Token Endpoint
[**force_refresh_jira_token_endpoint_user_integrations_jira_force_refresh_post**](DefaultApi.md#force_refresh_jira_token_endpoint_user_integrations_jira_force_refresh_post) | **POST** /user/integrations/jira/force-refresh | Force Refresh Jira Token Endpoint
[**force_refresh_salesforce_token_endpoint_user_integrations_salesforce_force_refresh_post**](DefaultApi.md#force_refresh_salesforce_token_endpoint_user_integrations_salesforce_force_refresh_post) | **POST** /user/integrations/salesforce/force-refresh | Force Refresh Salesforce Token Endpoint
[**get_asana_integrations_user_integrations_asana_get**](DefaultApi.md#get_asana_integrations_user_integrations_asana_get) | **GET** /user/integrations/asana | Get Asana Integrations
[**get_asana_login_user_integrations_asana_login_get**](DefaultApi.md#get_asana_login_user_integrations_asana_login_get) | **GET** /user/integrations/asana/login | Get Asana Login
[**get_context_for_chat_v3_chat_context_get**](DefaultApi.md#get_context_for_chat_v3_chat_context_get) | **GET** /v3/chat/context | Get Context For Chat
[**get_custom_app_api_custom_apps_project_id_app_id_get**](DefaultApi.md#get_custom_app_api_custom_apps_project_id_app_id_get) | **GET** /custom_apps/{project_id}/{app_id} | Get Custom App Api
[**get_custom_apps_custom_apps_project_id_get**](DefaultApi.md#get_custom_apps_custom_apps_project_id_get) | **GET** /custom_apps/{project_id} | Get Custom Apps
[**get_jira_integrations_user_integrations_jira_get**](DefaultApi.md#get_jira_integrations_user_integrations_jira_get) | **GET** /user/integrations/jira | Get Jira Integrations
[**get_jira_login_user_integrations_jira_login_post**](DefaultApi.md#get_jira_login_user_integrations_jira_login_post) | **POST** /user/integrations/jira/login | Get Jira Login
[**get_mcp_services_mcp_services_get**](DefaultApi.md#get_mcp_services_mcp_services_get) | **GET** /mcp/services | Get all available MCP services
[**get_oauth_url_v2_google_chat_bot_authorize_v2_post**](DefaultApi.md#get_oauth_url_v2_google_chat_bot_authorize_v2_post) | **POST** /google/chat/bot/authorize_v2 | Get Oauth Url V2
[**get_project_mcp_config_mcp_project_id_config_get**](DefaultApi.md#get_project_mcp_config_mcp_project_id_config_get) | **GET** /mcp/{project_id}/config | Get MCP configuration JSON for a project.          This can be used directly with Claude Desktop or Cursor for debugging.
[**get_project_mcps_mcp_project_id_get_get**](DefaultApi.md#get_project_mcps_mcp_project_id_get_get) | **GET** /mcp/{project_id}/get | Get MCP connections for a project
[**get_salesforce_integrations_user_integrations_salesforce_get**](DefaultApi.md#get_salesforce_integrations_user_integrations_salesforce_get) | **GET** /user/integrations/salesforce | Get Salesforce Integrations
[**get_salesforce_login_user_integrations_salesforce_login_get**](DefaultApi.md#get_salesforce_login_user_integrations_salesforce_login_get) | **GET** /user/integrations/salesforce/login | Get Salesforce Login
[**get_youtube_captions_json_tools_ai_extract_youtube_captions_post**](DefaultApi.md#get_youtube_captions_json_tools_ai_extract_youtube_captions_post) | **POST** /tools/ai/extract-youtube-captions | Get Youtube Captions Json
[**handle_get_upcoming_meetings_meetings_upcoming_get**](DefaultApi.md#handle_get_upcoming_meetings_meetings_upcoming_get) | **GET** /meetings/upcoming | Handle Get Upcoming Meetings
[**open_router_bring_own_open_router_post**](DefaultApi.md#open_router_bring_own_open_router_post) | **POST** /bring-own/open-router | Open Router
[**register_new_bot_teams_register_new_bot_post**](DefaultApi.md#register_new_bot_teams_register_new_bot_post) | **POST** /teams/register_new_bot | Register New Bot
[**run_usage_report_reports_usage_report_run_aa_post**](DefaultApi.md#run_usage_report_reports_usage_report_run_aa_post) | **POST** /reports/usage-report/run/aa | Run Usage Report
[**save_context_to_chat_v3_chat_context_post**](DefaultApi.md#save_context_to_chat_v3_chat_context_post) | **POST** /v3/chat/context | Save Context To Chat
[**test_asana_token_endpoint_user_integrations_asana_test_token_get**](DefaultApi.md#test_asana_token_endpoint_user_integrations_asana_test_token_get) | **GET** /user/integrations/asana/test-token | Test Asana Token Endpoint
[**test_jira_token_endpoint_user_integrations_jira_test_token_get**](DefaultApi.md#test_jira_token_endpoint_user_integrations_jira_test_token_get) | **GET** /user/integrations/jira/test-token | Test Jira Token Endpoint
[**test_mcp_server_mcp_test_post**](DefaultApi.md#test_mcp_server_mcp_test_post) | **POST** /mcp/test | Test an MCP server connection
[**test_salesforce_token_endpoint_user_integrations_salesforce_test_token_get**](DefaultApi.md#test_salesforce_token_endpoint_user_integrations_salesforce_test_token_get) | **GET** /user/integrations/salesforce/test-token | Test Salesforce Token Endpoint
[**update_project_mcp_mcp_project_id_update_mcp_id_put**](DefaultApi.md#update_project_mcp_mcp_project_id_update_mcp_id_put) | **PUT** /mcp/{project_id}/update/{mcp_id} | Update an MCP connection


# **compare_documents_action_default_compare_documents_post**
> object compare_documents_action_default_compare_documents_post(compare_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Compare Documents

Generate a diff summary using the OpenAI API

### Example


```python
import odin_sdk
from odin_sdk.models.compare_request import CompareRequest
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
    api_instance = odin_sdk.DefaultApi(api_client)
    compare_request = odin_sdk.CompareRequest() # CompareRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Compare Documents
        api_response = api_instance.compare_documents_action_default_compare_documents_post(compare_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DefaultApi->compare_documents_action_default_compare_documents_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->compare_documents_action_default_compare_documents_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **compare_request** | [**CompareRequest**](CompareRequest.md)|  | 
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

# **create_bot_package_teams_create_bot_package_post**
> object create_bot_package_teams_create_bot_package_post(display_name, short_description, full_description, portrait, x_api_key=x_api_key, x_api_secret=x_api_secret)

Create Bot Package

Create a new Teams bot and generate a deployment package.

Args:
    display_name: The display name for the bot
    short_description: Short description for Teams manifest
    full_description: Full description for Teams manifest
    portrait: 192x192 PNG image file for bot avatar

Returns:
    FileResponse: ZIP file containing manifest and images

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
    api_instance = odin_sdk.DefaultApi(api_client)
    display_name = 'display_name_example' # str | 
    short_description = 'short_description_example' # str | 
    full_description = 'full_description_example' # str | 
    portrait = None # bytearray | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Create Bot Package
        api_response = api_instance.create_bot_package_teams_create_bot_package_post(display_name, short_description, full_description, portrait, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DefaultApi->create_bot_package_teams_create_bot_package_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_bot_package_teams_create_bot_package_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **display_name** | **str**|  | 
 **short_description** | **str**|  | 
 **full_description** | **str**|  | 
 **portrait** | **bytearray**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

**object**

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

# **create_custom_app_custom_apps_project_id_create_post**
> object create_custom_app_custom_apps_project_id_create_post(project_id, create_custom_app_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Create Custom App

### Example


```python
import odin_sdk
from odin_sdk.models.create_custom_app_request import CreateCustomAppRequest
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
    api_instance = odin_sdk.DefaultApi(api_client)
    project_id = 'project_id_example' # str | 
    create_custom_app_request = odin_sdk.CreateCustomAppRequest() # CreateCustomAppRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Create Custom App
        api_response = api_instance.create_custom_app_custom_apps_project_id_create_post(project_id, create_custom_app_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DefaultApi->create_custom_app_custom_apps_project_id_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_custom_app_custom_apps_project_id_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **create_custom_app_request** | [**CreateCustomAppRequest**](CreateCustomAppRequest.md)|  | 
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

# **create_project_mcp_mcp_project_id_create_post**
> ProjectMCP create_project_mcp_mcp_project_id_create_post(project_id, create_mcp_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Create a new MCP connection

Create a new MCP connection for a specific project.

### Example


```python
import odin_sdk
from odin_sdk.models.create_mcp_request import CreateMCPRequest
from odin_sdk.models.project_mcp import ProjectMCP
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
    api_instance = odin_sdk.DefaultApi(api_client)
    project_id = 'project_id_example' # str | 
    create_mcp_request = odin_sdk.CreateMCPRequest() # CreateMCPRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Create a new MCP connection
        api_response = api_instance.create_project_mcp_mcp_project_id_create_post(project_id, create_mcp_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DefaultApi->create_project_mcp_mcp_project_id_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_project_mcp_mcp_project_id_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **create_mcp_request** | [**CreateMCPRequest**](CreateMCPRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**ProjectMCP**](ProjectMCP.md)

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

# **delete_asana_integration_user_integrations_asana_delete**
> DeleteAsanaIntegrationResponse delete_asana_integration_user_integrations_asana_delete(delete_asana_integration_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Delete Asana Integration

### Example


```python
import odin_sdk
from odin_sdk.models.delete_asana_integration_request import DeleteAsanaIntegrationRequest
from odin_sdk.models.delete_asana_integration_response import DeleteAsanaIntegrationResponse
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
    api_instance = odin_sdk.DefaultApi(api_client)
    delete_asana_integration_request = odin_sdk.DeleteAsanaIntegrationRequest() # DeleteAsanaIntegrationRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Delete Asana Integration
        api_response = api_instance.delete_asana_integration_user_integrations_asana_delete(delete_asana_integration_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DefaultApi->delete_asana_integration_user_integrations_asana_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_asana_integration_user_integrations_asana_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_asana_integration_request** | [**DeleteAsanaIntegrationRequest**](DeleteAsanaIntegrationRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**DeleteAsanaIntegrationResponse**](DeleteAsanaIntegrationResponse.md)

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

# **delete_context_from_chat_v3_chat_context_delete**
> object delete_context_from_chat_v3_chat_context_delete(project_id, chat_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Delete Context From Chat

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
    api_instance = odin_sdk.DefaultApi(api_client)
    project_id = 'project_id_example' # str | 
    chat_id = 'chat_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Delete Context From Chat
        api_response = api_instance.delete_context_from_chat_v3_chat_context_delete(project_id, chat_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DefaultApi->delete_context_from_chat_v3_chat_context_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_context_from_chat_v3_chat_context_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **chat_id** | **str**|  | 
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

# **delete_custom_app_custom_apps_project_id_app_id_delete**
> object delete_custom_app_custom_apps_project_id_app_id_delete(project_id, app_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Delete Custom App

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
    api_instance = odin_sdk.DefaultApi(api_client)
    project_id = 'project_id_example' # str | 
    app_id = 'app_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Delete Custom App
        api_response = api_instance.delete_custom_app_custom_apps_project_id_app_id_delete(project_id, app_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DefaultApi->delete_custom_app_custom_apps_project_id_app_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_custom_app_custom_apps_project_id_app_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **app_id** | **str**|  | 
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

# **delete_jira_integration_user_integrations_jira_delete**
> DeleteJiraIntegrationResponse delete_jira_integration_user_integrations_jira_delete(delete_jira_integration_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Delete Jira Integration

### Example


```python
import odin_sdk
from odin_sdk.models.delete_jira_integration_request import DeleteJiraIntegrationRequest
from odin_sdk.models.delete_jira_integration_response import DeleteJiraIntegrationResponse
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
    api_instance = odin_sdk.DefaultApi(api_client)
    delete_jira_integration_request = odin_sdk.DeleteJiraIntegrationRequest() # DeleteJiraIntegrationRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Delete Jira Integration
        api_response = api_instance.delete_jira_integration_user_integrations_jira_delete(delete_jira_integration_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DefaultApi->delete_jira_integration_user_integrations_jira_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_jira_integration_user_integrations_jira_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_jira_integration_request** | [**DeleteJiraIntegrationRequest**](DeleteJiraIntegrationRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**DeleteJiraIntegrationResponse**](DeleteJiraIntegrationResponse.md)

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

# **delete_project_mcp_mcp_project_id_delete_mcp_id_delete**
> object delete_project_mcp_mcp_project_id_delete_mcp_id_delete(project_id, mcp_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Delete an MCP connection

Delete an MCP connection for a specific project.

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
    api_instance = odin_sdk.DefaultApi(api_client)
    project_id = 'project_id_example' # str | Project ID
    mcp_id = 'mcp_id_example' # str | MCP connection ID
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Delete an MCP connection
        api_response = api_instance.delete_project_mcp_mcp_project_id_delete_mcp_id_delete(project_id, mcp_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DefaultApi->delete_project_mcp_mcp_project_id_delete_mcp_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_project_mcp_mcp_project_id_delete_mcp_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **mcp_id** | **str**| MCP connection ID | 
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

# **delete_salesforce_integration_user_integrations_salesforce_delete**
> DeleteSalesforceIntegrationResponse delete_salesforce_integration_user_integrations_salesforce_delete(delete_salesforce_integration_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Delete Salesforce Integration

### Example


```python
import odin_sdk
from odin_sdk.models.delete_salesforce_integration_request import DeleteSalesforceIntegrationRequest
from odin_sdk.models.delete_salesforce_integration_response import DeleteSalesforceIntegrationResponse
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
    api_instance = odin_sdk.DefaultApi(api_client)
    delete_salesforce_integration_request = odin_sdk.DeleteSalesforceIntegrationRequest() # DeleteSalesforceIntegrationRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Delete Salesforce Integration
        api_response = api_instance.delete_salesforce_integration_user_integrations_salesforce_delete(delete_salesforce_integration_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DefaultApi->delete_salesforce_integration_user_integrations_salesforce_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_salesforce_integration_user_integrations_salesforce_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_salesforce_integration_request** | [**DeleteSalesforceIntegrationRequest**](DeleteSalesforceIntegrationRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**DeleteSalesforceIntegrationResponse**](DeleteSalesforceIntegrationResponse.md)

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

# **download_usage_report_reports_usage_report_report_uuid_download_get**
> object download_usage_report_reports_usage_report_report_uuid_download_get(report_uuid, x_api_key=x_api_key, x_api_secret=x_api_secret)

Download Usage Report

Download generated usage reports as a zip file.

Args:
    report_uuid: The UUID of the report to download

Returns:
    A zip file containing the user report and domain report CSVs.

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
    api_instance = odin_sdk.DefaultApi(api_client)
    report_uuid = 'report_uuid_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Download Usage Report
        api_response = api_instance.download_usage_report_reports_usage_report_report_uuid_download_get(report_uuid, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DefaultApi->download_usage_report_reports_usage_report_report_uuid_download_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->download_usage_report_reports_usage_report_report_uuid_download_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_uuid** | **str**|  | 
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

# **edit_custom_app_custom_apps_project_id_settings_edit_post**
> object edit_custom_app_custom_apps_project_id_settings_edit_post(project_id, edit_custom_app_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Edit Custom App

### Example


```python
import odin_sdk
from odin_sdk.models.edit_custom_app_request import EditCustomAppRequest
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
    api_instance = odin_sdk.DefaultApi(api_client)
    project_id = 'project_id_example' # str | 
    edit_custom_app_request = odin_sdk.EditCustomAppRequest() # EditCustomAppRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Edit Custom App
        api_response = api_instance.edit_custom_app_custom_apps_project_id_settings_edit_post(project_id, edit_custom_app_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DefaultApi->edit_custom_app_custom_apps_project_id_settings_edit_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->edit_custom_app_custom_apps_project_id_settings_edit_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **edit_custom_app_request** | [**EditCustomAppRequest**](EditCustomAppRequest.md)|  | 
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

# **fetch_all_user_level_integrations_for_user_user_integrations_get**
> FetchAllUserLevelIntegrationsForUserResponse fetch_all_user_level_integrations_for_user_user_integrations_get(x_api_key=x_api_key, x_api_secret=x_api_secret)

Fetch All User Level Integrations For User

### Example


```python
import odin_sdk
from odin_sdk.models.fetch_all_user_level_integrations_for_user_response import FetchAllUserLevelIntegrationsForUserResponse
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
    api_instance = odin_sdk.DefaultApi(api_client)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Fetch All User Level Integrations For User
        api_response = api_instance.fetch_all_user_level_integrations_for_user_user_integrations_get(x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DefaultApi->fetch_all_user_level_integrations_for_user_user_integrations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->fetch_all_user_level_integrations_for_user_user_integrations_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**FetchAllUserLevelIntegrationsForUserResponse**](FetchAllUserLevelIntegrationsForUserResponse.md)

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

# **force_refresh_asana_token_endpoint_user_integrations_asana_force_refresh_post**
> object force_refresh_asana_token_endpoint_user_integrations_asana_force_refresh_post(delete_asana_integration_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Force Refresh Asana Token Endpoint

### Example


```python
import odin_sdk
from odin_sdk.models.delete_asana_integration_request import DeleteAsanaIntegrationRequest
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
    api_instance = odin_sdk.DefaultApi(api_client)
    delete_asana_integration_request = odin_sdk.DeleteAsanaIntegrationRequest() # DeleteAsanaIntegrationRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Force Refresh Asana Token Endpoint
        api_response = api_instance.force_refresh_asana_token_endpoint_user_integrations_asana_force_refresh_post(delete_asana_integration_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DefaultApi->force_refresh_asana_token_endpoint_user_integrations_asana_force_refresh_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->force_refresh_asana_token_endpoint_user_integrations_asana_force_refresh_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_asana_integration_request** | [**DeleteAsanaIntegrationRequest**](DeleteAsanaIntegrationRequest.md)|  | 
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

# **force_refresh_jira_token_endpoint_user_integrations_jira_force_refresh_post**
> object force_refresh_jira_token_endpoint_user_integrations_jira_force_refresh_post(delete_jira_integration_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Force Refresh Jira Token Endpoint

Force refresh Jira token. req.identifier should be user email.

### Example


```python
import odin_sdk
from odin_sdk.models.delete_jira_integration_request import DeleteJiraIntegrationRequest
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
    api_instance = odin_sdk.DefaultApi(api_client)
    delete_jira_integration_request = odin_sdk.DeleteJiraIntegrationRequest() # DeleteJiraIntegrationRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Force Refresh Jira Token Endpoint
        api_response = api_instance.force_refresh_jira_token_endpoint_user_integrations_jira_force_refresh_post(delete_jira_integration_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DefaultApi->force_refresh_jira_token_endpoint_user_integrations_jira_force_refresh_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->force_refresh_jira_token_endpoint_user_integrations_jira_force_refresh_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_jira_integration_request** | [**DeleteJiraIntegrationRequest**](DeleteJiraIntegrationRequest.md)|  | 
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

# **force_refresh_salesforce_token_endpoint_user_integrations_salesforce_force_refresh_post**
> object force_refresh_salesforce_token_endpoint_user_integrations_salesforce_force_refresh_post(delete_salesforce_integration_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Force Refresh Salesforce Token Endpoint

### Example


```python
import odin_sdk
from odin_sdk.models.delete_salesforce_integration_request import DeleteSalesforceIntegrationRequest
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
    api_instance = odin_sdk.DefaultApi(api_client)
    delete_salesforce_integration_request = odin_sdk.DeleteSalesforceIntegrationRequest() # DeleteSalesforceIntegrationRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Force Refresh Salesforce Token Endpoint
        api_response = api_instance.force_refresh_salesforce_token_endpoint_user_integrations_salesforce_force_refresh_post(delete_salesforce_integration_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DefaultApi->force_refresh_salesforce_token_endpoint_user_integrations_salesforce_force_refresh_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->force_refresh_salesforce_token_endpoint_user_integrations_salesforce_force_refresh_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_salesforce_integration_request** | [**DeleteSalesforceIntegrationRequest**](DeleteSalesforceIntegrationRequest.md)|  | 
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

# **get_asana_integrations_user_integrations_asana_get**
> GetUserAsanaIntegrationsResponse get_asana_integrations_user_integrations_asana_get(x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Asana Integrations

### Example


```python
import odin_sdk
from odin_sdk.models.get_user_asana_integrations_response import GetUserAsanaIntegrationsResponse
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
    api_instance = odin_sdk.DefaultApi(api_client)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Asana Integrations
        api_response = api_instance.get_asana_integrations_user_integrations_asana_get(x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DefaultApi->get_asana_integrations_user_integrations_asana_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_asana_integrations_user_integrations_asana_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**GetUserAsanaIntegrationsResponse**](GetUserAsanaIntegrationsResponse.md)

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

# **get_asana_login_user_integrations_asana_login_get**
> object get_asana_login_user_integrations_asana_login_get(redirect_uri_from_callback, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Asana Login

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
    api_instance = odin_sdk.DefaultApi(api_client)
    redirect_uri_from_callback = 'redirect_uri_from_callback_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Asana Login
        api_response = api_instance.get_asana_login_user_integrations_asana_login_get(redirect_uri_from_callback, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DefaultApi->get_asana_login_user_integrations_asana_login_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_asana_login_user_integrations_asana_login_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **redirect_uri_from_callback** | **str**|  | 
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

# **get_context_for_chat_v3_chat_context_get**
> object get_context_for_chat_v3_chat_context_get(project_id, chat_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Context For Chat

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
    api_instance = odin_sdk.DefaultApi(api_client)
    project_id = 'project_id_example' # str | 
    chat_id = 'chat_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Context For Chat
        api_response = api_instance.get_context_for_chat_v3_chat_context_get(project_id, chat_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DefaultApi->get_context_for_chat_v3_chat_context_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_context_for_chat_v3_chat_context_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **chat_id** | **str**|  | 
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

# **get_custom_app_api_custom_apps_project_id_app_id_get**
> object get_custom_app_api_custom_apps_project_id_app_id_get(project_id, app_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Custom App Api

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
    api_instance = odin_sdk.DefaultApi(api_client)
    project_id = 'project_id_example' # str | 
    app_id = 'app_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Custom App Api
        api_response = api_instance.get_custom_app_api_custom_apps_project_id_app_id_get(project_id, app_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DefaultApi->get_custom_app_api_custom_apps_project_id_app_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_custom_app_api_custom_apps_project_id_app_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **app_id** | **str**|  | 
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

# **get_custom_apps_custom_apps_project_id_get**
> object get_custom_apps_custom_apps_project_id_get(project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Custom Apps

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
    api_instance = odin_sdk.DefaultApi(api_client)
    project_id = 'project_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Custom Apps
        api_response = api_instance.get_custom_apps_custom_apps_project_id_get(project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DefaultApi->get_custom_apps_custom_apps_project_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_custom_apps_custom_apps_project_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
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

# **get_jira_integrations_user_integrations_jira_get**
> GetUserJiraIntegrationsResponse get_jira_integrations_user_integrations_jira_get(x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Jira Integrations

### Example


```python
import odin_sdk
from odin_sdk.models.get_user_jira_integrations_response import GetUserJiraIntegrationsResponse
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
    api_instance = odin_sdk.DefaultApi(api_client)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Jira Integrations
        api_response = api_instance.get_jira_integrations_user_integrations_jira_get(x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DefaultApi->get_jira_integrations_user_integrations_jira_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_jira_integrations_user_integrations_jira_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**GetUserJiraIntegrationsResponse**](GetUserJiraIntegrationsResponse.md)

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

# **get_jira_login_user_integrations_jira_login_post**
> object get_jira_login_user_integrations_jira_login_post(jira_login_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Jira Login

### Example


```python
import odin_sdk
from odin_sdk.models.jira_login_request import JiraLoginRequest
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
    api_instance = odin_sdk.DefaultApi(api_client)
    jira_login_request = odin_sdk.JiraLoginRequest() # JiraLoginRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Jira Login
        api_response = api_instance.get_jira_login_user_integrations_jira_login_post(jira_login_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DefaultApi->get_jira_login_user_integrations_jira_login_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_jira_login_user_integrations_jira_login_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jira_login_request** | [**JiraLoginRequest**](JiraLoginRequest.md)|  | 
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

# **get_mcp_services_mcp_services_get**
> List[MCPService] get_mcp_services_mcp_services_get(x_api_key=x_api_key, x_api_secret=x_api_secret)

Get all available MCP services

Get all available MCP services.

### Example


```python
import odin_sdk
from odin_sdk.models.mcp_service import MCPService
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
    api_instance = odin_sdk.DefaultApi(api_client)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get all available MCP services
        api_response = api_instance.get_mcp_services_mcp_services_get(x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DefaultApi->get_mcp_services_mcp_services_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_mcp_services_mcp_services_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**List[MCPService]**](MCPService.md)

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

# **get_oauth_url_v2_google_chat_bot_authorize_v2_post**
> object get_oauth_url_v2_google_chat_bot_authorize_v2_post(client_secret_file)

Get Oauth Url V2

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
    api_instance = odin_sdk.DefaultApi(api_client)
    client_secret_file = None # bytearray | 

    try:
        # Get Oauth Url V2
        api_response = api_instance.get_oauth_url_v2_google_chat_bot_authorize_v2_post(client_secret_file)
        print("The response of DefaultApi->get_oauth_url_v2_google_chat_bot_authorize_v2_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_oauth_url_v2_google_chat_bot_authorize_v2_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_secret_file** | **bytearray**|  | 

### Return type

**object**

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

# **get_project_mcp_config_mcp_project_id_config_get**
> object get_project_mcp_config_mcp_project_id_config_get(project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get MCP configuration JSON for a project.          This can be used directly with Claude Desktop or Cursor for debugging.

Get the complete MCP configuration JSON for a project.
This can be used directly with Claude Desktop.

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
    api_instance = odin_sdk.DefaultApi(api_client)
    project_id = 'project_id_example' # str | Project ID
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get MCP configuration JSON for a project.          This can be used directly with Claude Desktop or Cursor for debugging.
        api_response = api_instance.get_project_mcp_config_mcp_project_id_config_get(project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DefaultApi->get_project_mcp_config_mcp_project_id_config_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_project_mcp_config_mcp_project_id_config_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
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

# **get_project_mcps_mcp_project_id_get_get**
> List[ProjectMCP] get_project_mcps_mcp_project_id_get_get(project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get MCP connections for a project

Get all MCP connections for a specific project.

### Example


```python
import odin_sdk
from odin_sdk.models.project_mcp import ProjectMCP
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
    api_instance = odin_sdk.DefaultApi(api_client)
    project_id = 'project_id_example' # str | Project ID
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get MCP connections for a project
        api_response = api_instance.get_project_mcps_mcp_project_id_get_get(project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DefaultApi->get_project_mcps_mcp_project_id_get_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_project_mcps_mcp_project_id_get_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**List[ProjectMCP]**](ProjectMCP.md)

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

# **get_salesforce_integrations_user_integrations_salesforce_get**
> GetUserSalesforceIntegrationsResponse get_salesforce_integrations_user_integrations_salesforce_get(x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Salesforce Integrations

### Example


```python
import odin_sdk
from odin_sdk.models.get_user_salesforce_integrations_response import GetUserSalesforceIntegrationsResponse
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
    api_instance = odin_sdk.DefaultApi(api_client)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Salesforce Integrations
        api_response = api_instance.get_salesforce_integrations_user_integrations_salesforce_get(x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DefaultApi->get_salesforce_integrations_user_integrations_salesforce_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_salesforce_integrations_user_integrations_salesforce_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**GetUserSalesforceIntegrationsResponse**](GetUserSalesforceIntegrationsResponse.md)

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

# **get_salesforce_login_user_integrations_salesforce_login_get**
> object get_salesforce_login_user_integrations_salesforce_login_get(redirect_uri_from_callback, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Salesforce Login

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
    api_instance = odin_sdk.DefaultApi(api_client)
    redirect_uri_from_callback = 'redirect_uri_from_callback_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Salesforce Login
        api_response = api_instance.get_salesforce_login_user_integrations_salesforce_login_get(redirect_uri_from_callback, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DefaultApi->get_salesforce_login_user_integrations_salesforce_login_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_salesforce_login_user_integrations_salesforce_login_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **redirect_uri_from_callback** | **str**|  | 
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

# **get_youtube_captions_json_tools_ai_extract_youtube_captions_post**
> object get_youtube_captions_json_tools_ai_extract_youtube_captions_post(extract_youtube_captions_request)

Get Youtube Captions Json

### Example


```python
import odin_sdk
from odin_sdk.models.extract_youtube_captions_request import ExtractYoutubeCaptionsRequest
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
    api_instance = odin_sdk.DefaultApi(api_client)
    extract_youtube_captions_request = odin_sdk.ExtractYoutubeCaptionsRequest() # ExtractYoutubeCaptionsRequest | 

    try:
        # Get Youtube Captions Json
        api_response = api_instance.get_youtube_captions_json_tools_ai_extract_youtube_captions_post(extract_youtube_captions_request)
        print("The response of DefaultApi->get_youtube_captions_json_tools_ai_extract_youtube_captions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_youtube_captions_json_tools_ai_extract_youtube_captions_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extract_youtube_captions_request** | [**ExtractYoutubeCaptionsRequest**](ExtractYoutubeCaptionsRequest.md)|  | 

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

# **handle_get_upcoming_meetings_meetings_upcoming_get**
> MeetingsResponse handle_get_upcoming_meetings_meetings_upcoming_get(x_api_key=x_api_key, x_api_secret=x_api_secret)

Handle Get Upcoming Meetings

### Example


```python
import odin_sdk
from odin_sdk.models.meetings_response import MeetingsResponse
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
    api_instance = odin_sdk.DefaultApi(api_client)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Handle Get Upcoming Meetings
        api_response = api_instance.handle_get_upcoming_meetings_meetings_upcoming_get(x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DefaultApi->handle_get_upcoming_meetings_meetings_upcoming_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->handle_get_upcoming_meetings_meetings_upcoming_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**MeetingsResponse**](MeetingsResponse.md)

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

# **open_router_bring_own_open_router_post**
> object open_router_bring_own_open_router_post(bring_own_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Open Router

### Example


```python
import odin_sdk
from odin_sdk.models.bring_own_request import BringOwnRequest
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
    api_instance = odin_sdk.DefaultApi(api_client)
    bring_own_request = odin_sdk.BringOwnRequest() # BringOwnRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Open Router
        api_response = api_instance.open_router_bring_own_open_router_post(bring_own_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DefaultApi->open_router_bring_own_open_router_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->open_router_bring_own_open_router_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bring_own_request** | [**BringOwnRequest**](BringOwnRequest.md)|  | 
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

# **register_new_bot_teams_register_new_bot_post**
> RegisterNewBotResponse register_new_bot_teams_register_new_bot_post(register_new_bot_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Register New Bot

### Example


```python
import odin_sdk
from odin_sdk.models.register_new_bot_request import RegisterNewBotRequest
from odin_sdk.models.register_new_bot_response import RegisterNewBotResponse
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
    api_instance = odin_sdk.DefaultApi(api_client)
    register_new_bot_request = odin_sdk.RegisterNewBotRequest() # RegisterNewBotRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Register New Bot
        api_response = api_instance.register_new_bot_teams_register_new_bot_post(register_new_bot_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DefaultApi->register_new_bot_teams_register_new_bot_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->register_new_bot_teams_register_new_bot_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **register_new_bot_request** | [**RegisterNewBotRequest**](RegisterNewBotRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**RegisterNewBotResponse**](RegisterNewBotResponse.md)

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

# **run_usage_report_reports_usage_report_run_aa_post**
> object run_usage_report_reports_usage_report_run_aa_post(usage_report_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Run Usage Report

Enqueue a task to generate usage reports for Automation Anywhere users.

Optionally sends the reports to the specified email address.

Returns:
    The UUID of the generated report that can be used to download it later.

### Example


```python
import odin_sdk
from odin_sdk.models.usage_report_request import UsageReportRequest
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
    api_instance = odin_sdk.DefaultApi(api_client)
    usage_report_request = odin_sdk.UsageReportRequest() # UsageReportRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Run Usage Report
        api_response = api_instance.run_usage_report_reports_usage_report_run_aa_post(usage_report_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DefaultApi->run_usage_report_reports_usage_report_run_aa_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->run_usage_report_reports_usage_report_run_aa_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **usage_report_request** | [**UsageReportRequest**](UsageReportRequest.md)|  | 
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

# **save_context_to_chat_v3_chat_context_post**
> object save_context_to_chat_v3_chat_context_post(save_context_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Save Context To Chat

### Example


```python
import odin_sdk
from odin_sdk.models.save_context_request import SaveContextRequest
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
    api_instance = odin_sdk.DefaultApi(api_client)
    save_context_request = odin_sdk.SaveContextRequest() # SaveContextRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Save Context To Chat
        api_response = api_instance.save_context_to_chat_v3_chat_context_post(save_context_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DefaultApi->save_context_to_chat_v3_chat_context_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->save_context_to_chat_v3_chat_context_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **save_context_request** | [**SaveContextRequest**](SaveContextRequest.md)|  | 
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

# **test_asana_token_endpoint_user_integrations_asana_test_token_get**
> object test_asana_token_endpoint_user_integrations_asana_test_token_get(identifier, x_api_key=x_api_key, x_api_secret=x_api_secret)

Test Asana Token Endpoint

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
    api_instance = odin_sdk.DefaultApi(api_client)
    identifier = 'identifier_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Test Asana Token Endpoint
        api_response = api_instance.test_asana_token_endpoint_user_integrations_asana_test_token_get(identifier, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DefaultApi->test_asana_token_endpoint_user_integrations_asana_test_token_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->test_asana_token_endpoint_user_integrations_asana_test_token_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**|  | 
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

# **test_jira_token_endpoint_user_integrations_jira_test_token_get**
> object test_jira_token_endpoint_user_integrations_jira_test_token_get(user_email, instance_url=instance_url, x_api_key=x_api_key, x_api_secret=x_api_secret)

Test Jira Token Endpoint

Test Jira token. user_email is the integration identifier, instance_url is optional for testing specific instance.

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
    api_instance = odin_sdk.DefaultApi(api_client)
    user_email = 'user_email_example' # str | 
    instance_url = 'instance_url_example' # str |  (optional)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Test Jira Token Endpoint
        api_response = api_instance.test_jira_token_endpoint_user_integrations_jira_test_token_get(user_email, instance_url=instance_url, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DefaultApi->test_jira_token_endpoint_user_integrations_jira_test_token_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->test_jira_token_endpoint_user_integrations_jira_test_token_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_email** | **str**|  | 
 **instance_url** | **str**|  | [optional] 
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

# **test_mcp_server_mcp_test_post**
> MCPTestResponse test_mcp_server_mcp_test_post(mcp_test_request)

Test an MCP server connection

Test an MCP server connection.

### Example


```python
import odin_sdk
from odin_sdk.models.mcp_test_request import MCPTestRequest
from odin_sdk.models.mcp_test_response import MCPTestResponse
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
    api_instance = odin_sdk.DefaultApi(api_client)
    mcp_test_request = odin_sdk.MCPTestRequest() # MCPTestRequest | 

    try:
        # Test an MCP server connection
        api_response = api_instance.test_mcp_server_mcp_test_post(mcp_test_request)
        print("The response of DefaultApi->test_mcp_server_mcp_test_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->test_mcp_server_mcp_test_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mcp_test_request** | [**MCPTestRequest**](MCPTestRequest.md)|  | 

### Return type

[**MCPTestResponse**](MCPTestResponse.md)

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

# **test_salesforce_token_endpoint_user_integrations_salesforce_test_token_get**
> object test_salesforce_token_endpoint_user_integrations_salesforce_test_token_get(identifier, x_api_key=x_api_key, x_api_secret=x_api_secret)

Test Salesforce Token Endpoint

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
    api_instance = odin_sdk.DefaultApi(api_client)
    identifier = 'identifier_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Test Salesforce Token Endpoint
        api_response = api_instance.test_salesforce_token_endpoint_user_integrations_salesforce_test_token_get(identifier, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DefaultApi->test_salesforce_token_endpoint_user_integrations_salesforce_test_token_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->test_salesforce_token_endpoint_user_integrations_salesforce_test_token_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**|  | 
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

# **update_project_mcp_mcp_project_id_update_mcp_id_put**
> ProjectMCP update_project_mcp_mcp_project_id_update_mcp_id_put(project_id, mcp_id, create_mcp_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Update an MCP connection

Update an MCP connection for a specific project.

### Example


```python
import odin_sdk
from odin_sdk.models.create_mcp_request import CreateMCPRequest
from odin_sdk.models.project_mcp import ProjectMCP
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
    api_instance = odin_sdk.DefaultApi(api_client)
    project_id = 'project_id_example' # str | Project ID
    mcp_id = 'mcp_id_example' # str | MCP connection ID
    create_mcp_request = odin_sdk.CreateMCPRequest() # CreateMCPRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Update an MCP connection
        api_response = api_instance.update_project_mcp_mcp_project_id_update_mcp_id_put(project_id, mcp_id, create_mcp_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of DefaultApi->update_project_mcp_mcp_project_id_update_mcp_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_project_mcp_mcp_project_id_update_mcp_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **mcp_id** | **str**| MCP connection ID | 
 **create_mcp_request** | [**CreateMCPRequest**](CreateMCPRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**ProjectMCP**](ProjectMCP.md)

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

