# odin_sdk.ActionsApi

All URIs are relative to *http://127.0.0.1:8001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_tool_tools_api_post**](ActionsApi.md#api_tool_tools_api_post) | **POST** /tools/api | Api Tool
[**apply_action_to_table_actions_table_apply_post**](ActionsApi.md#apply_action_to_table_actions_table_apply_post) | **POST** /actions/table/apply | Apply Action To Table
[**check_action_status_and_update_actions_status_table_post**](ActionsApi.md#check_action_status_and_update_actions_status_table_post) | **POST** /actions/status/table | Check Action Status And Update
[**create_code_runner_action_actions_create_code_runner_post**](ActionsApi.md#create_code_runner_action_actions_create_code_runner_post) | **POST** /actions/create-code-runner | Create Code Runner Action
[**delete_odin_action_actions_delete_project_id_flow_id_delete**](ActionsApi.md#delete_odin_action_actions_delete_project_id_flow_id_delete) | **DELETE** /actions/delete/{project_id}/{flow_id} | Delete Odin Action
[**deploy_bot_tool_tools_deploy_bot_post**](ActionsApi.md#deploy_bot_tool_tools_deploy_bot_post) | **POST** /tools/deploy-bot | Deploy Bot Tool
[**execute_action_on_form_actions_execute_post**](ActionsApi.md#execute_action_on_form_actions_execute_post) | **POST** /actions/execute | Execute Action On Form
[**execute_action_on_form_direct_actions_execute_direct_post**](ActionsApi.md#execute_action_on_form_direct_actions_execute_direct_post) | **POST** /actions/execute/direct | Execute Action On Form Direct
[**execute_action_on_form_direct_v2_v2_actions_execute_direct_post**](ActionsApi.md#execute_action_on_form_direct_v2_v2_actions_execute_direct_post) | **POST** /v2/actions/execute/direct | Execute Action On Form Direct V2
[**execute_action_on_form_generic_actions_execute_generic_post**](ActionsApi.md#execute_action_on_form_generic_actions_execute_generic_post) | **POST** /actions/execute/generic | Execute Action On Form Generic
[**execute_action_on_table_actions_execute_table_data_type_id_row_id_post**](ActionsApi.md#execute_action_on_table_actions_execute_table_data_type_id_row_id_post) | **POST** /actions/execute/table/{data_type_id}/{row_id} | Execute Action On Table
[**export_odin_api_tool_as_json_actions_project_id_flow_flow_id_export_get**](ActionsApi.md#export_odin_api_tool_as_json_actions_project_id_flow_flow_id_export_get) | **GET** /actions/{project_id}/flow/{flow_id}/export | Export Odin Api Tool As Json
[**get_action_result_standalone_actions_result_project_id_flow_run_id_get**](ActionsApi.md#get_action_result_standalone_actions_result_project_id_flow_run_id_get) | **GET** /actions/result/{project_id}/{flow_run_id} | Get Action Result Standalone
[**get_action_status_actions_status_project_id_flow_run_id_get**](ActionsApi.md#get_action_status_actions_status_project_id_flow_run_id_get) | **GET** /actions/status/{project_id}/{flow_run_id} | Get Action Status
[**get_odin_action_by_id_actions_project_id_flow_flow_id_get**](ActionsApi.md#get_odin_action_by_id_actions_project_id_flow_flow_id_get) | **GET** /actions/{project_id}/flow/{flow_id} | Get Odin Action By Id
[**get_odin_actions_for_user_actions_project_id_blocks_get**](ActionsApi.md#get_odin_actions_for_user_actions_project_id_blocks_get) | **GET** /actions/{project_id}/blocks | Get Odin Actions For User
[**get_odin_actions_for_user_legacy_actions_project_id_get**](ActionsApi.md#get_odin_actions_for_user_legacy_actions_project_id_get) | **GET** /actions/{project_id} | Get Odin Actions For User Legacy
[**link_action_columns_actions_table_link_columns_post**](ActionsApi.md#link_action_columns_actions_table_link_columns_post) | **POST** /actions/table/link-columns | Link Action Columns
[**save_action_result_on_message_actions_result_save_post**](ActionsApi.md#save_action_result_on_message_actions_result_save_post) | **POST** /actions/result/save | Save Action Result On Message
[**save_odin_action_actions_save_post**](ActionsApi.md#save_odin_action_actions_save_post) | **POST** /actions/save | Save Odin Action
[**test_api_tool_actions_execute_api_post**](ActionsApi.md#test_api_tool_actions_execute_api_post) | **POST** /actions/execute/api | Test Api Tool
[**update_code_runner_action_actions_update_code_runner_put**](ActionsApi.md#update_code_runner_action_actions_update_code_runner_put) | **PUT** /actions/update-code-runner | Update Code Runner Action


# **api_tool_tools_api_post**
> ApiToolResponse api_tool_tools_api_post(api_tool_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Api Tool

Execute the API tool

### Example


```python
import odin_sdk
from odin_sdk.models.api_tool_request import ApiToolRequest
from odin_sdk.models.api_tool_response import ApiToolResponse
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
    api_instance = odin_sdk.ActionsApi(api_client)
    api_tool_request = odin_sdk.ApiToolRequest() # ApiToolRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Api Tool
        api_response = api_instance.api_tool_tools_api_post(api_tool_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ActionsApi->api_tool_tools_api_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->api_tool_tools_api_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_tool_request** | [**ApiToolRequest**](ApiToolRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**ApiToolResponse**](ApiToolResponse.md)

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

# **apply_action_to_table_actions_table_apply_post**
> ApplyActionTableResponse apply_action_to_table_actions_table_apply_post(apply_action_table_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Apply Action To Table

Map the output of an action to a table

### Example


```python
import odin_sdk
from odin_sdk.models.apply_action_table_request import ApplyActionTableRequest
from odin_sdk.models.apply_action_table_response import ApplyActionTableResponse
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
    api_instance = odin_sdk.ActionsApi(api_client)
    apply_action_table_request = odin_sdk.ApplyActionTableRequest() # ApplyActionTableRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Apply Action To Table
        api_response = api_instance.apply_action_to_table_actions_table_apply_post(apply_action_table_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ActionsApi->apply_action_to_table_actions_table_apply_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->apply_action_to_table_actions_table_apply_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apply_action_table_request** | [**ApplyActionTableRequest**](ApplyActionTableRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**ApplyActionTableResponse**](ApplyActionTableResponse.md)

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

# **check_action_status_and_update_actions_status_table_post**
> ActionStatusResponse check_action_status_and_update_actions_status_table_post(action_status_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Check Action Status And Update

Check action status and update table row cell values

### Example


```python
import odin_sdk
from odin_sdk.models.action_status_request import ActionStatusRequest
from odin_sdk.models.action_status_response import ActionStatusResponse
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
    api_instance = odin_sdk.ActionsApi(api_client)
    action_status_request = odin_sdk.ActionStatusRequest() # ActionStatusRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Check Action Status And Update
        api_response = api_instance.check_action_status_and_update_actions_status_table_post(action_status_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ActionsApi->check_action_status_and_update_actions_status_table_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->check_action_status_and_update_actions_status_table_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action_status_request** | [**ActionStatusRequest**](ActionStatusRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**ActionStatusResponse**](ActionStatusResponse.md)

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

# **create_code_runner_action_actions_create_code_runner_post**
> object create_code_runner_action_actions_create_code_runner_post(create_code_runner_action_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Create Code Runner Action

Create a code runner action from a script

### Example


```python
import odin_sdk
from odin_sdk.models.create_code_runner_action_request import CreateCodeRunnerActionRequest
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
    api_instance = odin_sdk.ActionsApi(api_client)
    create_code_runner_action_request = odin_sdk.CreateCodeRunnerActionRequest() # CreateCodeRunnerActionRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Create Code Runner Action
        api_response = api_instance.create_code_runner_action_actions_create_code_runner_post(create_code_runner_action_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ActionsApi->create_code_runner_action_actions_create_code_runner_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->create_code_runner_action_actions_create_code_runner_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_code_runner_action_request** | [**CreateCodeRunnerActionRequest**](CreateCodeRunnerActionRequest.md)|  | 
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

# **delete_odin_action_actions_delete_project_id_flow_id_delete**
> DeleteActionResponse delete_odin_action_actions_delete_project_id_flow_id_delete(project_id, flow_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Delete Odin Action

Delete an action.

### Example


```python
import odin_sdk
from odin_sdk.models.delete_action_response import DeleteActionResponse
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
    api_instance = odin_sdk.ActionsApi(api_client)
    project_id = 'project_id_example' # str | 
    flow_id = 'flow_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Delete Odin Action
        api_response = api_instance.delete_odin_action_actions_delete_project_id_flow_id_delete(project_id, flow_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ActionsApi->delete_odin_action_actions_delete_project_id_flow_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->delete_odin_action_actions_delete_project_id_flow_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **flow_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**DeleteActionResponse**](DeleteActionResponse.md)

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

# **deploy_bot_tool_tools_deploy_bot_post**
> DeployBotToolResponse deploy_bot_tool_tools_deploy_bot_post(deploy_bot_tool_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Deploy Bot Tool

Execute the Deploy Bot tool

### Example


```python
import odin_sdk
from odin_sdk.models.deploy_bot_tool_request import DeployBotToolRequest
from odin_sdk.models.deploy_bot_tool_response import DeployBotToolResponse
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
    api_instance = odin_sdk.ActionsApi(api_client)
    deploy_bot_tool_request = odin_sdk.DeployBotToolRequest() # DeployBotToolRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Deploy Bot Tool
        api_response = api_instance.deploy_bot_tool_tools_deploy_bot_post(deploy_bot_tool_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ActionsApi->deploy_bot_tool_tools_deploy_bot_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->deploy_bot_tool_tools_deploy_bot_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deploy_bot_tool_request** | [**DeployBotToolRequest**](DeployBotToolRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**DeployBotToolResponse**](DeployBotToolResponse.md)

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

# **execute_action_on_form_actions_execute_post**
> ExecuteActionOnFormResponse execute_action_on_form_actions_execute_post(execute_action_on_form_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Execute Action On Form

Execute an action on a form.

### Example


```python
import odin_sdk
from odin_sdk.models.execute_action_on_form_request import ExecuteActionOnFormRequest
from odin_sdk.models.execute_action_on_form_response import ExecuteActionOnFormResponse
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
    api_instance = odin_sdk.ActionsApi(api_client)
    execute_action_on_form_request = odin_sdk.ExecuteActionOnFormRequest() # ExecuteActionOnFormRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Execute Action On Form
        api_response = api_instance.execute_action_on_form_actions_execute_post(execute_action_on_form_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ActionsApi->execute_action_on_form_actions_execute_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->execute_action_on_form_actions_execute_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execute_action_on_form_request** | [**ExecuteActionOnFormRequest**](ExecuteActionOnFormRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**ExecuteActionOnFormResponse**](ExecuteActionOnFormResponse.md)

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

# **execute_action_on_form_direct_actions_execute_direct_post**
> ExecuteActionOnFormResponse execute_action_on_form_direct_actions_execute_direct_post(execute_action_on_automator_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Execute Action On Form Direct

Execute an action on a form directly.

### Example


```python
import odin_sdk
from odin_sdk.models.execute_action_on_automator_request import ExecuteActionOnAutomatorRequest
from odin_sdk.models.execute_action_on_form_response import ExecuteActionOnFormResponse
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
    api_instance = odin_sdk.ActionsApi(api_client)
    execute_action_on_automator_request = odin_sdk.ExecuteActionOnAutomatorRequest() # ExecuteActionOnAutomatorRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Execute Action On Form Direct
        api_response = api_instance.execute_action_on_form_direct_actions_execute_direct_post(execute_action_on_automator_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ActionsApi->execute_action_on_form_direct_actions_execute_direct_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->execute_action_on_form_direct_actions_execute_direct_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execute_action_on_automator_request** | [**ExecuteActionOnAutomatorRequest**](ExecuteActionOnAutomatorRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**ExecuteActionOnFormResponse**](ExecuteActionOnFormResponse.md)

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

# **execute_action_on_form_direct_v2_v2_actions_execute_direct_post**
> ExecuteActionOnFormResponse execute_action_on_form_direct_v2_v2_actions_execute_direct_post(execute_action_on_automator_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Execute Action On Form Direct V2

Execute an action on a form directly.

### Example


```python
import odin_sdk
from odin_sdk.models.execute_action_on_automator_request import ExecuteActionOnAutomatorRequest
from odin_sdk.models.execute_action_on_form_response import ExecuteActionOnFormResponse
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
    api_instance = odin_sdk.ActionsApi(api_client)
    execute_action_on_automator_request = odin_sdk.ExecuteActionOnAutomatorRequest() # ExecuteActionOnAutomatorRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Execute Action On Form Direct V2
        api_response = api_instance.execute_action_on_form_direct_v2_v2_actions_execute_direct_post(execute_action_on_automator_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ActionsApi->execute_action_on_form_direct_v2_v2_actions_execute_direct_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->execute_action_on_form_direct_v2_v2_actions_execute_direct_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execute_action_on_automator_request** | [**ExecuteActionOnAutomatorRequest**](ExecuteActionOnAutomatorRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**ExecuteActionOnFormResponse**](ExecuteActionOnFormResponse.md)

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

# **execute_action_on_form_generic_actions_execute_generic_post**
> ExecuteActionOnFormResponse execute_action_on_form_generic_actions_execute_generic_post(execute_action_generic_on_form_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Execute Action On Form Generic

Execute an action on a form. Handles automatic routing to automator or API tool action

### Example


```python
import odin_sdk
from odin_sdk.models.execute_action_generic_on_form_request import ExecuteActionGenericOnFormRequest
from odin_sdk.models.execute_action_on_form_response import ExecuteActionOnFormResponse
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
    api_instance = odin_sdk.ActionsApi(api_client)
    execute_action_generic_on_form_request = odin_sdk.ExecuteActionGenericOnFormRequest() # ExecuteActionGenericOnFormRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Execute Action On Form Generic
        api_response = api_instance.execute_action_on_form_generic_actions_execute_generic_post(execute_action_generic_on_form_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ActionsApi->execute_action_on_form_generic_actions_execute_generic_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->execute_action_on_form_generic_actions_execute_generic_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execute_action_generic_on_form_request** | [**ExecuteActionGenericOnFormRequest**](ExecuteActionGenericOnFormRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**ExecuteActionOnFormResponse**](ExecuteActionOnFormResponse.md)

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

# **execute_action_on_table_actions_execute_table_data_type_id_row_id_post**
> ExecuteActionOnTableResponse execute_action_on_table_actions_execute_table_data_type_id_row_id_post(data_type_id, row_id, execute_action_on_table_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Execute Action On Table

Execute an action from a table row.

### Example


```python
import odin_sdk
from odin_sdk.models.execute_action_on_table_request import ExecuteActionOnTableRequest
from odin_sdk.models.execute_action_on_table_response import ExecuteActionOnTableResponse
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
    api_instance = odin_sdk.ActionsApi(api_client)
    data_type_id = 'data_type_id_example' # str | 
    row_id = 'row_id_example' # str | 
    execute_action_on_table_request = odin_sdk.ExecuteActionOnTableRequest() # ExecuteActionOnTableRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Execute Action On Table
        api_response = api_instance.execute_action_on_table_actions_execute_table_data_type_id_row_id_post(data_type_id, row_id, execute_action_on_table_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ActionsApi->execute_action_on_table_actions_execute_table_data_type_id_row_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->execute_action_on_table_actions_execute_table_data_type_id_row_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_type_id** | **str**|  | 
 **row_id** | **str**|  | 
 **execute_action_on_table_request** | [**ExecuteActionOnTableRequest**](ExecuteActionOnTableRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**ExecuteActionOnTableResponse**](ExecuteActionOnTableResponse.md)

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

# **export_odin_api_tool_as_json_actions_project_id_flow_flow_id_export_get**
> object export_odin_api_tool_as_json_actions_project_id_flow_flow_id_export_get(project_id, flow_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Export Odin Api Tool As Json

Export an action as a JSON file for download.

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
    api_instance = odin_sdk.ActionsApi(api_client)
    project_id = 'project_id_example' # str | 
    flow_id = 'flow_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Export Odin Api Tool As Json
        api_response = api_instance.export_odin_api_tool_as_json_actions_project_id_flow_flow_id_export_get(project_id, flow_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ActionsApi->export_odin_api_tool_as_json_actions_project_id_flow_flow_id_export_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->export_odin_api_tool_as_json_actions_project_id_flow_flow_id_export_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **flow_id** | **str**|  | 
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

# **get_action_result_standalone_actions_result_project_id_flow_run_id_get**
> object get_action_result_standalone_actions_result_project_id_flow_run_id_get(project_id, flow_run_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Action Result Standalone

Get the result of an action.

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
    api_instance = odin_sdk.ActionsApi(api_client)
    project_id = 'project_id_example' # str | 
    flow_run_id = 'flow_run_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Action Result Standalone
        api_response = api_instance.get_action_result_standalone_actions_result_project_id_flow_run_id_get(project_id, flow_run_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ActionsApi->get_action_result_standalone_actions_result_project_id_flow_run_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->get_action_result_standalone_actions_result_project_id_flow_run_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **flow_run_id** | **str**|  | 
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

# **get_action_status_actions_status_project_id_flow_run_id_get**
> object get_action_status_actions_status_project_id_flow_run_id_get(project_id, flow_run_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Action Status

Get the status of an action.

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
    api_instance = odin_sdk.ActionsApi(api_client)
    project_id = 'project_id_example' # str | 
    flow_run_id = 'flow_run_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Action Status
        api_response = api_instance.get_action_status_actions_status_project_id_flow_run_id_get(project_id, flow_run_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ActionsApi->get_action_status_actions_status_project_id_flow_run_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->get_action_status_actions_status_project_id_flow_run_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **flow_run_id** | **str**|  | 
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

# **get_odin_action_by_id_actions_project_id_flow_flow_id_get**
> GetActionResponse get_odin_action_by_id_actions_project_id_flow_flow_id_get(project_id, flow_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Odin Action By Id

Get an action by flow ID.

### Example


```python
import odin_sdk
from odin_sdk.models.get_action_response import GetActionResponse
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
    api_instance = odin_sdk.ActionsApi(api_client)
    project_id = 'project_id_example' # str | 
    flow_id = 'flow_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Odin Action By Id
        api_response = api_instance.get_odin_action_by_id_actions_project_id_flow_flow_id_get(project_id, flow_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ActionsApi->get_odin_action_by_id_actions_project_id_flow_flow_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->get_odin_action_by_id_actions_project_id_flow_flow_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **flow_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**GetActionResponse**](GetActionResponse.md)

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

# **get_odin_actions_for_user_actions_project_id_blocks_get**
> GetActionAsBlockResponse get_odin_actions_for_user_actions_project_id_blocks_get(project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Odin Actions For User

Get all actions on a project as formatted agent blocks.

### Example


```python
import odin_sdk
from odin_sdk.models.get_action_as_block_response import GetActionAsBlockResponse
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
    api_instance = odin_sdk.ActionsApi(api_client)
    project_id = 'project_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Odin Actions For User
        api_response = api_instance.get_odin_actions_for_user_actions_project_id_blocks_get(project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ActionsApi->get_odin_actions_for_user_actions_project_id_blocks_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->get_odin_actions_for_user_actions_project_id_blocks_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**GetActionAsBlockResponse**](GetActionAsBlockResponse.md)

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

# **get_odin_actions_for_user_legacy_actions_project_id_get**
> GetActionResponse get_odin_actions_for_user_legacy_actions_project_id_get(project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Odin Actions For User Legacy

Get all actions on a project.

### Example


```python
import odin_sdk
from odin_sdk.models.get_action_response import GetActionResponse
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
    api_instance = odin_sdk.ActionsApi(api_client)
    project_id = 'project_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Odin Actions For User Legacy
        api_response = api_instance.get_odin_actions_for_user_legacy_actions_project_id_get(project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ActionsApi->get_odin_actions_for_user_legacy_actions_project_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->get_odin_actions_for_user_legacy_actions_project_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**GetActionResponse**](GetActionResponse.md)

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

# **link_action_columns_actions_table_link_columns_post**
> LinkActionColumnResponse link_action_columns_actions_table_link_columns_post(link_action_column_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Link Action Columns

Link an action column to a target column using a key path

### Example


```python
import odin_sdk
from odin_sdk.models.link_action_column_request import LinkActionColumnRequest
from odin_sdk.models.link_action_column_response import LinkActionColumnResponse
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
    api_instance = odin_sdk.ActionsApi(api_client)
    link_action_column_request = odin_sdk.LinkActionColumnRequest() # LinkActionColumnRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Link Action Columns
        api_response = api_instance.link_action_columns_actions_table_link_columns_post(link_action_column_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ActionsApi->link_action_columns_actions_table_link_columns_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->link_action_columns_actions_table_link_columns_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **link_action_column_request** | [**LinkActionColumnRequest**](LinkActionColumnRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**LinkActionColumnResponse**](LinkActionColumnResponse.md)

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

# **save_action_result_on_message_actions_result_save_post**
> SaveActionResultOnMessageResponse save_action_result_on_message_actions_result_save_post(save_action_result_on_message_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Save Action Result On Message

Save an action result on a message.

### Example


```python
import odin_sdk
from odin_sdk.models.save_action_result_on_message_request import SaveActionResultOnMessageRequest
from odin_sdk.models.save_action_result_on_message_response import SaveActionResultOnMessageResponse
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
    api_instance = odin_sdk.ActionsApi(api_client)
    save_action_result_on_message_request = odin_sdk.SaveActionResultOnMessageRequest() # SaveActionResultOnMessageRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Save Action Result On Message
        api_response = api_instance.save_action_result_on_message_actions_result_save_post(save_action_result_on_message_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ActionsApi->save_action_result_on_message_actions_result_save_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->save_action_result_on_message_actions_result_save_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **save_action_result_on_message_request** | [**SaveActionResultOnMessageRequest**](SaveActionResultOnMessageRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**SaveActionResultOnMessageResponse**](SaveActionResultOnMessageResponse.md)

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

# **save_odin_action_actions_save_post**
> SaveActionResponse save_odin_action_actions_save_post(save_action_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Save Odin Action

Save an action.

### Example


```python
import odin_sdk
from odin_sdk.models.save_action_request import SaveActionRequest
from odin_sdk.models.save_action_response import SaveActionResponse
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
    api_instance = odin_sdk.ActionsApi(api_client)
    save_action_request = odin_sdk.SaveActionRequest() # SaveActionRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Save Odin Action
        api_response = api_instance.save_odin_action_actions_save_post(save_action_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ActionsApi->save_odin_action_actions_save_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->save_odin_action_actions_save_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **save_action_request** | [**SaveActionRequest**](SaveActionRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**SaveActionResponse**](SaveActionResponse.md)

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

# **test_api_tool_actions_execute_api_post**
> TestApiToolResponse test_api_tool_actions_execute_api_post(test_api_tool_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Test Api Tool

Test an API tool by executing it directly

### Example


```python
import odin_sdk
from odin_sdk.models.test_api_tool_request import TestApiToolRequest
from odin_sdk.models.test_api_tool_response import TestApiToolResponse
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
    api_instance = odin_sdk.ActionsApi(api_client)
    test_api_tool_request = odin_sdk.TestApiToolRequest() # TestApiToolRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Test Api Tool
        api_response = api_instance.test_api_tool_actions_execute_api_post(test_api_tool_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ActionsApi->test_api_tool_actions_execute_api_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->test_api_tool_actions_execute_api_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_api_tool_request** | [**TestApiToolRequest**](TestApiToolRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**TestApiToolResponse**](TestApiToolResponse.md)

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

# **update_code_runner_action_actions_update_code_runner_put**
> object update_code_runner_action_actions_update_code_runner_put(update_code_runner_action_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Update Code Runner Action

Update a code runner action by updating the existing script and parameters

### Example


```python
import odin_sdk
from odin_sdk.models.update_code_runner_action_request import UpdateCodeRunnerActionRequest
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
    api_instance = odin_sdk.ActionsApi(api_client)
    update_code_runner_action_request = odin_sdk.UpdateCodeRunnerActionRequest() # UpdateCodeRunnerActionRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Update Code Runner Action
        api_response = api_instance.update_code_runner_action_actions_update_code_runner_put(update_code_runner_action_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ActionsApi->update_code_runner_action_actions_update_code_runner_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->update_code_runner_action_actions_update_code_runner_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_code_runner_action_request** | [**UpdateCodeRunnerActionRequest**](UpdateCodeRunnerActionRequest.md)|  | 
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

