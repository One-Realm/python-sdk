# odin_sdk.ExtensiveSearchApi

All URIs are relative to *http://127.0.0.1:8001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_job_b2b_hcl_gf_extensive_search_cancel_job_id_delete**](ExtensiveSearchApi.md#cancel_job_b2b_hcl_gf_extensive_search_cancel_job_id_delete) | **DELETE** /b2b/hcl/gf/extensive-search/cancel/{job_id} | Cancel Job
[**get_job_status_b2b_hcl_gf_extensive_search_status_job_id_get**](ExtensiveSearchApi.md#get_job_status_b2b_hcl_gf_extensive_search_status_job_id_get) | **GET** /b2b/hcl/gf/extensive-search/status/{job_id} | Get Job Status
[**submit_extensive_search_job_b2b_hcl_gf_extensive_search_submit_post**](ExtensiveSearchApi.md#submit_extensive_search_job_b2b_hcl_gf_extensive_search_submit_post) | **POST** /b2b/hcl/gf/extensive-search/submit | Submit Extensive Search Job


# **cancel_job_b2b_hcl_gf_extensive_search_cancel_job_id_delete**
> object cancel_job_b2b_hcl_gf_extensive_search_cancel_job_id_delete(job_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Cancel Job

Cancel a running or pending extensive search job.

Args:
    job_id: The unique identifier of the job to cancel

Returns:
    Confirmation of cancellation

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
    api_instance = odin_sdk.ExtensiveSearchApi(api_client)
    job_id = 'job_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Cancel Job
        api_response = api_instance.cancel_job_b2b_hcl_gf_extensive_search_cancel_job_id_delete(job_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ExtensiveSearchApi->cancel_job_b2b_hcl_gf_extensive_search_cancel_job_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExtensiveSearchApi->cancel_job_b2b_hcl_gf_extensive_search_cancel_job_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**|  | 
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

# **get_job_status_b2b_hcl_gf_extensive_search_status_job_id_get**
> JobStatusResponse get_job_status_b2b_hcl_gf_extensive_search_status_job_id_get(job_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Job Status

Get the status and result of an extensive search job from the database.

Args:
    job_id: The unique identifier of the job

Returns:
    JobStatusResponse with current status and result if available

### Example


```python
import odin_sdk
from odin_sdk.models.job_status_response import JobStatusResponse
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
    api_instance = odin_sdk.ExtensiveSearchApi(api_client)
    job_id = 'job_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Job Status
        api_response = api_instance.get_job_status_b2b_hcl_gf_extensive_search_status_job_id_get(job_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ExtensiveSearchApi->get_job_status_b2b_hcl_gf_extensive_search_status_job_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExtensiveSearchApi->get_job_status_b2b_hcl_gf_extensive_search_status_job_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**JobStatusResponse**](JobStatusResponse.md)

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

# **submit_extensive_search_job_b2b_hcl_gf_extensive_search_submit_post**
> JobSubmissionResponse submit_extensive_search_job_b2b_hcl_gf_extensive_search_submit_post(extensive_search_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Submit Extensive Search Job

Submit an extensive search job for async processing.

Args:
    request: ExtensiveSearchRequest containing search parameters

Returns:
    JobSubmissionResponse with job ID and status

### Example


```python
import odin_sdk
from odin_sdk.models.extensive_search_request import ExtensiveSearchRequest
from odin_sdk.models.job_submission_response import JobSubmissionResponse
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
    api_instance = odin_sdk.ExtensiveSearchApi(api_client)
    extensive_search_request = odin_sdk.ExtensiveSearchRequest() # ExtensiveSearchRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Submit Extensive Search Job
        api_response = api_instance.submit_extensive_search_job_b2b_hcl_gf_extensive_search_submit_post(extensive_search_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ExtensiveSearchApi->submit_extensive_search_job_b2b_hcl_gf_extensive_search_submit_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExtensiveSearchApi->submit_extensive_search_job_b2b_hcl_gf_extensive_search_submit_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extensive_search_request** | [**ExtensiveSearchRequest**](ExtensiveSearchRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**JobSubmissionResponse**](JobSubmissionResponse.md)

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

