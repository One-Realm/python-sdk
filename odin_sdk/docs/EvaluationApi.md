# odin_sdk.EvaluationApi

All URIs are relative to *http://127.0.0.1:8001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_all_qna_pairs_project_project_id_eval_qna_delete**](EvaluationApi.md#delete_all_qna_pairs_project_project_id_eval_qna_delete) | **DELETE** /project/{project_id}/eval_qna/ | Delete All Qna Pairs
[**delete_eval_qna_project_project_id_eval_qna_qna_id_delete**](EvaluationApi.md#delete_eval_qna_project_project_id_eval_qna_qna_id_delete) | **DELETE** /project/{project_id}/eval_qna/{qna_id} | Delete Eval Qna
[**get_eval_qna_project_project_id_eval_qna_get**](EvaluationApi.md#get_eval_qna_project_project_id_eval_qna_get) | **GET** /project/{project_id}/eval_qna | Get Eval Qna
[**get_eval_qna_status_project_project_id_generate_qna_task_task_id_get**](EvaluationApi.md#get_eval_qna_status_project_project_id_generate_qna_task_task_id_get) | **GET** /project/{project_id}/generate_qna_task/{task_id} | Get Eval Qna Status
[**get_evaluation_summary_project_project_id_evaluation_summary_get**](EvaluationApi.md#get_evaluation_summary_project_project_id_evaluation_summary_get) | **GET** /project/{project_id}/evaluation_summary | Get Evaluation Summary
[**submit_eval_qna_task_project_project_id_generate_qna_task_post**](EvaluationApi.md#submit_eval_qna_task_project_project_id_generate_qna_task_post) | **POST** /project/{project_id}/generate_qna_task | Submit Eval Qna Task


# **delete_all_qna_pairs_project_project_id_eval_qna_delete**
> DeleteQuestionOutput delete_all_qna_pairs_project_project_id_eval_qna_delete(project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Delete All Qna Pairs

Delete all QnA pairs by from the evaluation table

### Example


```python
import odin_sdk
from odin_sdk.models.delete_question_output import DeleteQuestionOutput
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
    api_instance = odin_sdk.EvaluationApi(api_client)
    project_id = 'project_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Delete All Qna Pairs
        api_response = api_instance.delete_all_qna_pairs_project_project_id_eval_qna_delete(project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of EvaluationApi->delete_all_qna_pairs_project_project_id_eval_qna_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EvaluationApi->delete_all_qna_pairs_project_project_id_eval_qna_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**DeleteQuestionOutput**](DeleteQuestionOutput.md)

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

# **delete_eval_qna_project_project_id_eval_qna_qna_id_delete**
> DeleteQuestionOutput delete_eval_qna_project_project_id_eval_qna_qna_id_delete(project_id, qna_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Delete Eval Qna

Delete a QnA pair by PK from the evaluation table

### Example


```python
import odin_sdk
from odin_sdk.models.delete_question_output import DeleteQuestionOutput
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
    api_instance = odin_sdk.EvaluationApi(api_client)
    project_id = 'project_id_example' # str | 
    qna_id = 'qna_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Delete Eval Qna
        api_response = api_instance.delete_eval_qna_project_project_id_eval_qna_qna_id_delete(project_id, qna_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of EvaluationApi->delete_eval_qna_project_project_id_eval_qna_qna_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EvaluationApi->delete_eval_qna_project_project_id_eval_qna_qna_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **qna_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**DeleteQuestionOutput**](DeleteQuestionOutput.md)

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

# **get_eval_qna_project_project_id_eval_qna_get**
> List[DbEvalQnAPair] get_eval_qna_project_project_id_eval_qna_get(project_id, page, items_per_page, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Eval Qna

Get a list of QnA pairs by pagination

### Example


```python
import odin_sdk
from odin_sdk.models.db_eval_qn_a_pair import DbEvalQnAPair
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
    api_instance = odin_sdk.EvaluationApi(api_client)
    project_id = 'project_id_example' # str | 
    page = 56 # int | The page number to retrieve
    items_per_page = 56 # int | The number of items per page
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Eval Qna
        api_response = api_instance.get_eval_qna_project_project_id_eval_qna_get(project_id, page, items_per_page, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of EvaluationApi->get_eval_qna_project_project_id_eval_qna_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EvaluationApi->get_eval_qna_project_project_id_eval_qna_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **page** | **int**| The page number to retrieve | 
 **items_per_page** | **int**| The number of items per page | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**List[DbEvalQnAPair]**](DbEvalQnAPair.md)

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

# **get_eval_qna_status_project_project_id_generate_qna_task_task_id_get**
> TaskStatus get_eval_qna_status_project_project_id_generate_qna_task_task_id_get(project_id, task_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Eval Qna Status

Get the status of a task submit to generate the questions

### Example


```python
import odin_sdk
from odin_sdk.models.task_status import TaskStatus
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
    api_instance = odin_sdk.EvaluationApi(api_client)
    project_id = 'project_id_example' # str | 
    task_id = 'task_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Eval Qna Status
        api_response = api_instance.get_eval_qna_status_project_project_id_generate_qna_task_task_id_get(project_id, task_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of EvaluationApi->get_eval_qna_status_project_project_id_generate_qna_task_task_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EvaluationApi->get_eval_qna_status_project_project_id_generate_qna_task_task_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **task_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**TaskStatus**](TaskStatus.md)

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

# **get_evaluation_summary_project_project_id_evaluation_summary_get**
> EvaluationSummary get_evaluation_summary_project_project_id_evaluation_summary_get(project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Evaluation Summary

Get the summary of the evaluation

### Example


```python
import odin_sdk
from odin_sdk.models.evaluation_summary import EvaluationSummary
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
    api_instance = odin_sdk.EvaluationApi(api_client)
    project_id = 'project_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Evaluation Summary
        api_response = api_instance.get_evaluation_summary_project_project_id_evaluation_summary_get(project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of EvaluationApi->get_evaluation_summary_project_project_id_evaluation_summary_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EvaluationApi->get_evaluation_summary_project_project_id_evaluation_summary_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**EvaluationSummary**](EvaluationSummary.md)

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

# **submit_eval_qna_task_project_project_id_generate_qna_task_post**
> object submit_eval_qna_task_project_project_id_generate_qna_task_post(project_id, eval_task_input, x_api_key=x_api_key, x_api_secret=x_api_secret)

Submit Eval Qna Task

Submit a task to generate evaluation questions

### Example


```python
import odin_sdk
from odin_sdk.models.eval_task_input import EvalTaskInput
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
    api_instance = odin_sdk.EvaluationApi(api_client)
    project_id = 'project_id_example' # str | 
    eval_task_input = odin_sdk.EvalTaskInput() # EvalTaskInput | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Submit Eval Qna Task
        api_response = api_instance.submit_eval_qna_task_project_project_id_generate_qna_task_post(project_id, eval_task_input, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of EvaluationApi->submit_eval_qna_task_project_project_id_generate_qna_task_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EvaluationApi->submit_eval_qna_task_project_project_id_generate_qna_task_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **eval_task_input** | [**EvalTaskInput**](EvalTaskInput.md)|  | 
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

