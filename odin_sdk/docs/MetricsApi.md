# odin_sdk.MetricsApi

All URIs are relative to *http://127.0.0.1:8001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_chart_metrics_metrics_charts_get**](MetricsApi.md#get_chart_metrics_metrics_charts_get) | **GET** /metrics/charts/ | Get Chart Metrics
[**get_tools_metrics_metrics_get**](MetricsApi.md#get_tools_metrics_metrics_get) | **GET** /metrics/ | Get Tools Metrics


# **get_chart_metrics_metrics_charts_get**
> ChartMetricsResponse get_chart_metrics_metrics_charts_get(project_id=project_id, start_date=start_date, end_date=end_date, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Chart Metrics

Get tool usage metrics formatted for charts visualization.

### Example


```python
import odin_sdk
from odin_sdk.models.chart_metrics_response import ChartMetricsResponse
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
    api_instance = odin_sdk.MetricsApi(api_client)
    project_id = 'project_id_example' # str | Project ID to filter metrics (optional)
    start_date = 56 # int | Start date filter (timestamp in seconds since epoch) (optional)
    end_date = 56 # int | End date filter (timestamp in seconds since epoch) (optional)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Chart Metrics
        api_response = api_instance.get_chart_metrics_metrics_charts_get(project_id=project_id, start_date=start_date, end_date=end_date, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of MetricsApi->get_chart_metrics_metrics_charts_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetricsApi->get_chart_metrics_metrics_charts_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID to filter metrics | [optional] 
 **start_date** | **int**| Start date filter (timestamp in seconds since epoch) | [optional] 
 **end_date** | **int**| End date filter (timestamp in seconds since epoch) | [optional] 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**ChartMetricsResponse**](ChartMetricsResponse.md)

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

# **get_tools_metrics_metrics_get**
> MetricsResponse get_tools_metrics_metrics_get(project_id=project_id, start_date=start_date, end_date=end_date, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Tools Metrics

Get tool usage and token metrics.

### Example


```python
import odin_sdk
from odin_sdk.models.metrics_response import MetricsResponse
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
    api_instance = odin_sdk.MetricsApi(api_client)
    project_id = 'project_id_example' # str | Project ID to filter metrics (optional)
    start_date = 56 # int | Start date filter (timestamp in seconds since epoch) (optional)
    end_date = 56 # int | End date filter (timestamp in seconds since epoch) (optional)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Tools Metrics
        api_response = api_instance.get_tools_metrics_metrics_get(project_id=project_id, start_date=start_date, end_date=end_date, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of MetricsApi->get_tools_metrics_metrics_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetricsApi->get_tools_metrics_metrics_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID to filter metrics | [optional] 
 **start_date** | **int**| Start date filter (timestamp in seconds since epoch) | [optional] 
 **end_date** | **int**| End date filter (timestamp in seconds since epoch) | [optional] 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**MetricsResponse**](MetricsResponse.md)

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

