# odin_sdk.V2CrawlerRunsApi

All URIs are relative to *http://127.0.0.1:8001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_run_crawl_runs_project_id_run_id_delete**](V2CrawlerRunsApi.md#delete_run_crawl_runs_project_id_run_id_delete) | **DELETE** /crawl-runs/{project_id}/{run_id} | Delete Run
[**get_crawl_runs_crawl_configs_project_id_crawl_id_runs_get**](V2CrawlerRunsApi.md#get_crawl_runs_crawl_configs_project_id_crawl_id_runs_get) | **GET** /crawl-configs/{project_id}/{crawl_id}/runs/ | Get Crawl Runs
[**get_run_crawl_runs_project_id_run_id_get**](V2CrawlerRunsApi.md#get_run_crawl_runs_project_id_run_id_get) | **GET** /crawl-runs/{project_id}/{run_id} | Get Run
[**get_run_results_crawl_runs_project_id_run_id_results_get**](V2CrawlerRunsApi.md#get_run_results_crawl_runs_project_id_run_id_results_get) | **GET** /crawl-runs/{project_id}/{run_id}/results | Get Run Results
[**restart_crawl_run_crawl_runs_project_id_run_id_restart_post**](V2CrawlerRunsApi.md#restart_crawl_run_crawl_runs_project_id_run_id_restart_post) | **POST** /crawl-runs/{project_id}/{run_id}/restart | Restart Crawl Run
[**resume_crawl_run_crawl_runs_project_id_run_id_resume_post**](V2CrawlerRunsApi.md#resume_crawl_run_crawl_runs_project_id_run_id_resume_post) | **POST** /crawl-runs/{project_id}/{run_id}/resume | Resume Crawl Run
[**start_new_run_crawl_configs_project_id_crawl_id_runs_new_post**](V2CrawlerRunsApi.md#start_new_run_crawl_configs_project_id_crawl_id_runs_new_post) | **POST** /crawl-configs/{project_id}/{crawl_id}/runs/new | Start New Run
[**stop_crawl_run_crawl_runs_project_id_run_id_stop_post**](V2CrawlerRunsApi.md#stop_crawl_run_crawl_runs_project_id_run_id_stop_post) | **POST** /crawl-runs/{project_id}/{run_id}/stop | Stop Crawl Run


# **delete_run_crawl_runs_project_id_run_id_delete**
> object delete_run_crawl_runs_project_id_run_id_delete(project_id, run_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Delete Run

Delete a crawl run and its results

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
    api_instance = odin_sdk.V2CrawlerRunsApi(api_client)
    project_id = 'project_id_example' # str | 
    run_id = 'run_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Delete Run
        api_response = api_instance.delete_run_crawl_runs_project_id_run_id_delete(project_id, run_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of V2CrawlerRunsApi->delete_run_crawl_runs_project_id_run_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2CrawlerRunsApi->delete_run_crawl_runs_project_id_run_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **run_id** | **str**|  | 
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

# **get_crawl_runs_crawl_configs_project_id_crawl_id_runs_get**
> List[CrawlRunResponse] get_crawl_runs_crawl_configs_project_id_crawl_id_runs_get(project_id, crawl_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Crawl Runs

Get all runs for a crawl configuration

### Example

* Api Key Authentication (APIKeyHeader):

```python
import odin_sdk
from odin_sdk.models.crawl_run_response import CrawlRunResponse
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
    api_instance = odin_sdk.V2CrawlerRunsApi(api_client)
    project_id = 'project_id_example' # str | 
    crawl_id = 'crawl_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Crawl Runs
        api_response = api_instance.get_crawl_runs_crawl_configs_project_id_crawl_id_runs_get(project_id, crawl_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of V2CrawlerRunsApi->get_crawl_runs_crawl_configs_project_id_crawl_id_runs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2CrawlerRunsApi->get_crawl_runs_crawl_configs_project_id_crawl_id_runs_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **crawl_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**List[CrawlRunResponse]**](CrawlRunResponse.md)

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

# **get_run_crawl_runs_project_id_run_id_get**
> CrawlRunResponse get_run_crawl_runs_project_id_run_id_get(project_id, run_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Run

Get a crawl run

### Example

* Api Key Authentication (APIKeyHeader):

```python
import odin_sdk
from odin_sdk.models.crawl_run_response import CrawlRunResponse
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
    api_instance = odin_sdk.V2CrawlerRunsApi(api_client)
    project_id = 'project_id_example' # str | 
    run_id = 'run_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Run
        api_response = api_instance.get_run_crawl_runs_project_id_run_id_get(project_id, run_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of V2CrawlerRunsApi->get_run_crawl_runs_project_id_run_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2CrawlerRunsApi->get_run_crawl_runs_project_id_run_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **run_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**CrawlRunResponse**](CrawlRunResponse.md)

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

# **get_run_results_crawl_runs_project_id_run_id_results_get**
> List[CrawlResultResponse] get_run_results_crawl_runs_project_id_run_id_results_get(project_id, run_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Run Results

Get all results for a crawl run

### Example

* Api Key Authentication (APIKeyHeader):

```python
import odin_sdk
from odin_sdk.models.crawl_result_response import CrawlResultResponse
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
    api_instance = odin_sdk.V2CrawlerRunsApi(api_client)
    project_id = 'project_id_example' # str | 
    run_id = 'run_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Run Results
        api_response = api_instance.get_run_results_crawl_runs_project_id_run_id_results_get(project_id, run_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of V2CrawlerRunsApi->get_run_results_crawl_runs_project_id_run_id_results_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2CrawlerRunsApi->get_run_results_crawl_runs_project_id_run_id_results_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **run_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**List[CrawlResultResponse]**](CrawlResultResponse.md)

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

# **restart_crawl_run_crawl_runs_project_id_run_id_restart_post**
> object restart_crawl_run_crawl_runs_project_id_run_id_restart_post(project_id, run_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Restart Crawl Run

Restart a crawl run

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
    api_instance = odin_sdk.V2CrawlerRunsApi(api_client)
    project_id = 'project_id_example' # str | 
    run_id = 'run_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Restart Crawl Run
        api_response = api_instance.restart_crawl_run_crawl_runs_project_id_run_id_restart_post(project_id, run_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of V2CrawlerRunsApi->restart_crawl_run_crawl_runs_project_id_run_id_restart_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2CrawlerRunsApi->restart_crawl_run_crawl_runs_project_id_run_id_restart_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **run_id** | **str**|  | 
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

# **resume_crawl_run_crawl_runs_project_id_run_id_resume_post**
> object resume_crawl_run_crawl_runs_project_id_run_id_resume_post(project_id, run_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Resume Crawl Run

Resume a paused crawl run

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
    api_instance = odin_sdk.V2CrawlerRunsApi(api_client)
    project_id = 'project_id_example' # str | 
    run_id = 'run_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Resume Crawl Run
        api_response = api_instance.resume_crawl_run_crawl_runs_project_id_run_id_resume_post(project_id, run_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of V2CrawlerRunsApi->resume_crawl_run_crawl_runs_project_id_run_id_resume_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2CrawlerRunsApi->resume_crawl_run_crawl_runs_project_id_run_id_resume_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **run_id** | **str**|  | 
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

# **start_new_run_crawl_configs_project_id_crawl_id_runs_new_post**
> CrawlRunResponse start_new_run_crawl_configs_project_id_crawl_id_runs_new_post(project_id, crawl_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Start New Run

Start a new run for a crawl configuration

### Example

* Api Key Authentication (APIKeyHeader):

```python
import odin_sdk
from odin_sdk.models.crawl_run_response import CrawlRunResponse
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
    api_instance = odin_sdk.V2CrawlerRunsApi(api_client)
    project_id = 'project_id_example' # str | 
    crawl_id = 'crawl_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Start New Run
        api_response = api_instance.start_new_run_crawl_configs_project_id_crawl_id_runs_new_post(project_id, crawl_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of V2CrawlerRunsApi->start_new_run_crawl_configs_project_id_crawl_id_runs_new_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2CrawlerRunsApi->start_new_run_crawl_configs_project_id_crawl_id_runs_new_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **crawl_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**CrawlRunResponse**](CrawlRunResponse.md)

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

# **stop_crawl_run_crawl_runs_project_id_run_id_stop_post**
> object stop_crawl_run_crawl_runs_project_id_run_id_stop_post(project_id, run_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Stop Crawl Run

Stop a crawl run

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
    api_instance = odin_sdk.V2CrawlerRunsApi(api_client)
    project_id = 'project_id_example' # str | 
    run_id = 'run_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Stop Crawl Run
        api_response = api_instance.stop_crawl_run_crawl_runs_project_id_run_id_stop_post(project_id, run_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of V2CrawlerRunsApi->stop_crawl_run_crawl_runs_project_id_run_id_stop_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V2CrawlerRunsApi->stop_crawl_run_crawl_runs_project_id_run_id_stop_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **run_id** | **str**|  | 
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

