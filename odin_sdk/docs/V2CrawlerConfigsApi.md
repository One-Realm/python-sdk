# odin_sdk.V2CrawlerConfigsApi

All URIs are relative to *http://127.0.0.1:8001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_crawl_config_endpoint_crawl_configs_project_id_create_new_post**](V2CrawlerConfigsApi.md#create_crawl_config_endpoint_crawl_configs_project_id_create_new_post) | **POST** /crawl-configs/{project_id}/create/new/ | Create Crawl Config Endpoint
[**delete_crawl_config_crawl_configs_project_id_crawl_id_delete**](V2CrawlerConfigsApi.md#delete_crawl_config_crawl_configs_project_id_crawl_id_delete) | **DELETE** /crawl-configs/{project_id}/{crawl_id} | Delete Crawl Config
[**get_project_crawl_configs_crawl_configs_project_id_get**](V2CrawlerConfigsApi.md#get_project_crawl_configs_crawl_configs_project_id_get) | **GET** /crawl-configs/{project_id} | Get Project Crawl Configs
[**update_crawl_config_crawl_configs_project_id_crawl_id_put**](V2CrawlerConfigsApi.md#update_crawl_config_crawl_configs_project_id_crawl_id_put) | **PUT** /crawl-configs/{project_id}/{crawl_id} | Update Crawl Config


# **create_crawl_config_endpoint_crawl_configs_project_id_create_new_post**
> CrawlConfigResponse create_crawl_config_endpoint_crawl_configs_project_id_create_new_post(project_id, crawl_config_create, x_api_key=x_api_key, x_api_secret=x_api_secret)

Create Crawl Config Endpoint

Create a new crawl configuration

### Example

* Api Key Authentication (APIKeyHeader):

```python
import odin_sdk
from odin_sdk.models.crawl_config_create import CrawlConfigCreate
from odin_sdk.models.crawl_config_response import CrawlConfigResponse
from odin_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = odin_sdk.Configuration(
    host = "http://127.0.0.1:8001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with odin_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = odin_sdk.V2CrawlerConfigsApi(api_client)
    project_id = 'project_id_example' # str | 
    crawl_config_create = odin_sdk.CrawlConfigCreate() # CrawlConfigCreate | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Create Crawl Config Endpoint
        api_response = api_instance.create_crawl_config_endpoint_crawl_configs_project_id_create_new_post(project_id, crawl_config_create, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of V2CrawlerConfigsApi->create_crawl_config_endpoint_crawl_configs_project_id_create_new_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2CrawlerConfigsApi->create_crawl_config_endpoint_crawl_configs_project_id_create_new_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **crawl_config_create** | [**CrawlConfigCreate**](CrawlConfigCreate.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**CrawlConfigResponse**](CrawlConfigResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_crawl_config_crawl_configs_project_id_crawl_id_delete**
> object delete_crawl_config_crawl_configs_project_id_crawl_id_delete(project_id, crawl_id, force=force, x_api_key=x_api_key, x_api_secret=x_api_secret)

Delete Crawl Config

Delete a crawl configuration and all associated data

### Example

* Api Key Authentication (APIKeyHeader):

```python
import odin_sdk
from odin_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = odin_sdk.Configuration(
    host = "http://127.0.0.1:8001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with odin_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = odin_sdk.V2CrawlerConfigsApi(api_client)
    project_id = 'project_id_example' # str | 
    crawl_id = 'crawl_id_example' # str | 
    force = False # bool | Force deletion, stopping any ongoing crawls (optional) (default to False)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Delete Crawl Config
        api_response = api_instance.delete_crawl_config_crawl_configs_project_id_crawl_id_delete(project_id, crawl_id, force=force, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of V2CrawlerConfigsApi->delete_crawl_config_crawl_configs_project_id_crawl_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2CrawlerConfigsApi->delete_crawl_config_crawl_configs_project_id_crawl_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **crawl_id** | **str**|  | 
 **force** | **bool**| Force deletion, stopping any ongoing crawls | [optional] [default to False]
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

**object**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_crawl_configs_crawl_configs_project_id_get**
> List[CrawlConfigResponse] get_project_crawl_configs_crawl_configs_project_id_get(project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Project Crawl Configs

Get all crawl configurations for a project

### Example

* Api Key Authentication (APIKeyHeader):

```python
import odin_sdk
from odin_sdk.models.crawl_config_response import CrawlConfigResponse
from odin_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = odin_sdk.Configuration(
    host = "http://127.0.0.1:8001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with odin_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = odin_sdk.V2CrawlerConfigsApi(api_client)
    project_id = 'project_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Project Crawl Configs
        api_response = api_instance.get_project_crawl_configs_crawl_configs_project_id_get(project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of V2CrawlerConfigsApi->get_project_crawl_configs_crawl_configs_project_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2CrawlerConfigsApi->get_project_crawl_configs_crawl_configs_project_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**List[CrawlConfigResponse]**](CrawlConfigResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_crawl_config_crawl_configs_project_id_crawl_id_put**
> CrawlConfigResponse update_crawl_config_crawl_configs_project_id_crawl_id_put(project_id, crawl_id, crawl_config_update, x_api_key=x_api_key, x_api_secret=x_api_secret)

Update Crawl Config

Update an existing crawl configuration

### Example

* Api Key Authentication (APIKeyHeader):

```python
import odin_sdk
from odin_sdk.models.crawl_config_response import CrawlConfigResponse
from odin_sdk.models.crawl_config_update import CrawlConfigUpdate
from odin_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = odin_sdk.Configuration(
    host = "http://127.0.0.1:8001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with odin_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = odin_sdk.V2CrawlerConfigsApi(api_client)
    project_id = 'project_id_example' # str | 
    crawl_id = 'crawl_id_example' # str | 
    crawl_config_update = odin_sdk.CrawlConfigUpdate() # CrawlConfigUpdate | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Update Crawl Config
        api_response = api_instance.update_crawl_config_crawl_configs_project_id_crawl_id_put(project_id, crawl_id, crawl_config_update, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of V2CrawlerConfigsApi->update_crawl_config_crawl_configs_project_id_crawl_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2CrawlerConfigsApi->update_crawl_config_crawl_configs_project_id_crawl_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **crawl_id** | **str**|  | 
 **crawl_config_update** | [**CrawlConfigUpdate**](CrawlConfigUpdate.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**CrawlConfigResponse**](CrawlConfigResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

