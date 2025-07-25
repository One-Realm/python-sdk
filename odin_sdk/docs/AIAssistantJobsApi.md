# odin_sdk.AIAssistantJobsApi

All URIs are relative to *http://127.0.0.1:8001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ai_assistant_job_v1_ai_jobs_create_post**](AIAssistantJobsApi.md#create_ai_assistant_job_v1_ai_jobs_create_post) | **POST** /ai/jobs/create | Create an AI Assistant Job
[**create_ai_assistant_job_v2_v2_ai_jobs_create_post**](AIAssistantJobsApi.md#create_ai_assistant_job_v2_v2_ai_jobs_create_post) | **POST** /v2/ai/jobs/create | Create an AI Assistant Job
[**delete_ai_assistant_job_ai_jobs_project_id_job_id_delete**](AIAssistantJobsApi.md#delete_ai_assistant_job_ai_jobs_project_id_job_id_delete) | **DELETE** /ai/jobs/{project_id}/{job_id} | Delete Job
[**directly_access_content_spinner_ai_content_spinner_post**](AIAssistantJobsApi.md#directly_access_content_spinner_ai_content_spinner_post) | **POST** /ai/content_spinner | Create Content from Instructions
[**directly_access_email_creator_ai_email_creator_post**](AIAssistantJobsApi.md#directly_access_email_creator_ai_email_creator_post) | **POST** /ai/email_creator | Create an Email from Instructions
[**fetch_ai_assistant_job_ai_jobs_project_id_job_id_fetch_get**](AIAssistantJobsApi.md#fetch_ai_assistant_job_ai_jobs_project_id_job_id_fetch_get) | **GET** /ai/jobs/{project_id}/{job_id}/fetch | Fetch Job Result
[**get_available_ai_job_types_ai_jobs_types_get**](AIAssistantJobsApi.md#get_available_ai_job_types_ai_jobs_types_get) | **GET** /ai/jobs/types | Get Available Job Types
[**get_jobs_status_ai_jobs_project_id_get**](AIAssistantJobsApi.md#get_jobs_status_ai_jobs_project_id_get) | **GET** /ai/jobs/{project_id} | Get Job Statuses


# **create_ai_assistant_job_v1_ai_jobs_create_post**
> CreateAssistentJobResponse create_ai_assistant_job_v1_ai_jobs_create_post(document_keys, job_type, project_id, x_api_key=x_api_key, x_api_secret=x_api_secret, extra_arguments=extra_arguments, job_name=job_name)

Create an AI Assistant Job

This endpoint is used to enqueue new AI assistant jobs. Each job type has their own set of arguments, which are documented in the job_info field of the /ai/jobs/types endpoint, as well as in the endpoint description below.<br>The valid job types are: deposition_summary, simple_summary, ab_content_creation, redline_summary, content_spinner, email_creator.
<br><br>
<b>Simple Summary</b>
<br>Odin simplifies information processing by creating concise summaries from lengthy texts, capturing main points and key ideas swiftly and efficiently.<br>
<u>Required arguments:</u>
<ul>
<li>objective: the objective prompt, explaining the task for the summary to the AI. For example: "Extract all key data points and information into a detailed summary."</li>
<li>model_name: the desired model name to use for the job. Options are: gpt-4-1106-preview, gpt-4o-mini. Note that gpt-4 models are currently limited to subscription users only.</li>
</ul>
<b>Deposition Summary</b>
<br>Odin proficiently creates deposition summaries, analyzes transcripts to highlight key evidence and testimonies, saving you time and effort.<br>
<u>Required arguments:</u>
<ul>
<li>type_of_law: the desired type of law to use for the deposition summary. Examples include, but are not limited to:<ul> <li>Civil Litigation Law</li><li>Criminal Defense Law</li><li>Corporate Law</li><li>Employment Law</li><li>Environmental Law</li><li>Estate Planning Law</li><li>Family Law</li><li>Immigration Law</li><li>Intellectual Property Law</li><li>Real Estate Law</li><li>Personal Injury Law</li>.</ul></li>
</ul>
<b>AB Content Creation</b>
<br>Create multiple versions of content based on your documents with unique tones. Great for email campaigns!<br>
<u>Required arguments:</u>
<ul>
<li>instructions: the instructions for the AI to follow. For example: "Write a blog post about the benefits of Odin."</li>
<li>tones: the tones to use for the content creation. Multiple can be selected, supplied as an array of strings. Examples include, but are not limited to:<ul> <li>Formal and Professional</li><li>Friendly and Approachable</li><li>Inquisitive and Curious</li><li>Enthusiastic and Exciting</li><li>Empathetic and Supportive</li><li>Casual and Informal</li><li>Concise and Direct</li><li>Inspirational and Motivational</li><li>Authoritative and Confident</li><li>Educational and Informative</li>.</ul></li>
<li>temperature: the desired creativity level to use for the content creation. A float between 0 and 1, with 0 being the least creative and 1 being the most creative.</li>
<li>model_name: the desired model name to use for the job. Options are: gpt-4-1106-preview, gpt-4o-mini. Note that gpt-4 models are currently limited to subscription users only.</li>
</ul>
<b>Redline Summary</b>
<br>Generate a summary of differences between two documents using Odin.<br>
<u>Required arguments:</u>
<ul>
<li>model_name: the desired model name to use for the job. Options are: gpt-4-1106-preview. Note that gpt-4 models are currently limited to subscription users only.</li>
<li>ignore_instructions: the instructions for the model on what changes to ignore. Provided as an array of strings.</li>
<li>ignore_pdf_headers_and_footers: whether to ignore PDF headers and footers. Provided as a boolean.</li>
<li>credit_usage_limit: the maximum number of credits to use for the job. Provided as an integer.</li>
<li>diff_ai_overide_limit: the maximum number of differences to track in a given block. Provided as an integer.</li>
</ul>
<b>Content Spinner</b>
<br>Have Odin generate new content based on your original text and instructions!<br>
<u>Required arguments:</u>
<ul>
<li>input_text: the input text to use for the content spinner. For example: "Odin is a great tool for summarizing documents."</li>
<li>temperature: the desired creativity level to use for the content spinner. A float between 0 and 1, with 0 being the least creative and 1 being the most creative.</li>
<li>model_name: the desired model name to use for the job. Options are: gpt-4-1106-preview, gpt-4o-mini. Note that gpt-4 models are currently limited to subscription users only.</li>
</ul>
<u>Optional arguments:</u>
<ul>
<li>additional_instructions: the additional instructions for the content spinner. Provided as an array of strings.</li>
</ul>
<b>Email Creator</b>
<br>Have Odin generate an email based on your instructions, either as plain text or HTML!<br>
<u>Required arguments:</u>
<ul>
<li>sender: the sender of the email.</li>
<li>content_instructions: the instructions for the content of the email. Provided as an array of strings.</li>
<li>formatting_example: the formatting example for the email. For example: "Please format the email as follows: Greetings, [sender]! I hope you are doing well. [content] Sincerely, [recipient]."</li>
<li>model_name: the desired model name to use for the job. Options are: gpt-4-1106-preview, gpt-4o-mini. Note that gpt-4 models are currently limited to subscription users only.</li>
</ul>
<u>Optional arguments:</u>
<ul>
<li>recipient: the recipient of the email.</li>
<li>generate_html: whether to generate the email as HTML. Provided as a boolean. False by default.</li>
</ul>

### Example


```python
import odin_sdk
from odin_sdk.models.create_assistent_job_response import CreateAssistentJobResponse
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
    api_instance = odin_sdk.AIAssistantJobsApi(api_client)
    document_keys = ['document_keys_example'] # List[str] | Array of strings defining document keys to use with the assistant job.<br>The document keys are full raw file names and full raw URLs. For example: [\\\"test.pdf\\\", \\\"https://www.google.com\\\"]
    job_type = 'job_type_example' # str | The type of job to run.<br>Valid job types are deposition_summary, simple_summary, ab_content_creation, redline_summary, content_spinner, email_creator.
    project_id = 'project_id_example' # str | The project ID to run the job in.
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)
    extra_arguments = 'extra_arguments_example' # str |  (optional)
    job_name = '536188a0-654f-4dee-b73e-90443ccc03cb' # str | The desired output name for the job. (optional) (default to '536188a0-654f-4dee-b73e-90443ccc03cb')

    try:
        # Create an AI Assistant Job
        api_response = api_instance.create_ai_assistant_job_v1_ai_jobs_create_post(document_keys, job_type, project_id, x_api_key=x_api_key, x_api_secret=x_api_secret, extra_arguments=extra_arguments, job_name=job_name)
        print("The response of AIAssistantJobsApi->create_ai_assistant_job_v1_ai_jobs_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIAssistantJobsApi->create_ai_assistant_job_v1_ai_jobs_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_keys** | [**List[str]**](str.md)| Array of strings defining document keys to use with the assistant job.&lt;br&gt;The document keys are full raw file names and full raw URLs. For example: [\\\&quot;test.pdf\\\&quot;, \\\&quot;https://www.google.com\\\&quot;] | 
 **job_type** | **str**| The type of job to run.&lt;br&gt;Valid job types are deposition_summary, simple_summary, ab_content_creation, redline_summary, content_spinner, email_creator. | 
 **project_id** | **str**| The project ID to run the job in. | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 
 **extra_arguments** | **str**|  | [optional] 
 **job_name** | **str**| The desired output name for the job. | [optional] [default to &#39;536188a0-654f-4dee-b73e-90443ccc03cb&#39;]

### Return type

[**CreateAssistentJobResponse**](CreateAssistentJobResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ai_assistant_job_v2_v2_ai_jobs_create_post**
> CreateAssistentJobResponse create_ai_assistant_job_v2_v2_ai_jobs_create_post(document_keys, job_type, project_id, x_api_key=x_api_key, x_api_secret=x_api_secret, extra_arguments=extra_arguments, job_name=job_name)

Create an AI Assistant Job

This endpoint is used to enqueue new AI assistant jobs. Each job type has their own set of arguments, which are documented in the job_info field of the /ai/jobs/types endpoint, as well as in the endpoint description below.<br>The valid job types are: deposition_summary, simple_summary, ab_content_creation, redline_summary, content_spinner, email_creator.
<br><br>
<b>Simple Summary</b>
<br>Odin simplifies information processing by creating concise summaries from lengthy texts, capturing main points and key ideas swiftly and efficiently.<br>
<u>Required arguments:</u>
<ul>
<li>objective: the objective prompt, explaining the task for the summary to the AI. For example: "Extract all key data points and information into a detailed summary."</li>
<li>model_name: the desired model name to use for the job. Options are: gpt-4-1106-preview, gpt-4o-mini. Note that gpt-4 models are currently limited to subscription users only.</li>
</ul>
<b>Deposition Summary</b>
<br>Odin proficiently creates deposition summaries, analyzes transcripts to highlight key evidence and testimonies, saving you time and effort.<br>
<u>Required arguments:</u>
<ul>
<li>type_of_law: the desired type of law to use for the deposition summary. Examples include, but are not limited to:<ul> <li>Civil Litigation Law</li><li>Criminal Defense Law</li><li>Corporate Law</li><li>Employment Law</li><li>Environmental Law</li><li>Estate Planning Law</li><li>Family Law</li><li>Immigration Law</li><li>Intellectual Property Law</li><li>Real Estate Law</li><li>Personal Injury Law</li>.</ul></li>
</ul>
<b>AB Content Creation</b>
<br>Create multiple versions of content based on your documents with unique tones. Great for email campaigns!<br>
<u>Required arguments:</u>
<ul>
<li>instructions: the instructions for the AI to follow. For example: "Write a blog post about the benefits of Odin."</li>
<li>tones: the tones to use for the content creation. Multiple can be selected, supplied as an array of strings. Examples include, but are not limited to:<ul> <li>Formal and Professional</li><li>Friendly and Approachable</li><li>Inquisitive and Curious</li><li>Enthusiastic and Exciting</li><li>Empathetic and Supportive</li><li>Casual and Informal</li><li>Concise and Direct</li><li>Inspirational and Motivational</li><li>Authoritative and Confident</li><li>Educational and Informative</li>.</ul></li>
<li>temperature: the desired creativity level to use for the content creation. A float between 0 and 1, with 0 being the least creative and 1 being the most creative.</li>
<li>model_name: the desired model name to use for the job. Options are: gpt-4-1106-preview, gpt-4o-mini. Note that gpt-4 models are currently limited to subscription users only.</li>
</ul>
<b>Redline Summary</b>
<br>Generate a summary of differences between two documents using Odin.<br>
<u>Required arguments:</u>
<ul>
<li>model_name: the desired model name to use for the job. Options are: gpt-4-1106-preview. Note that gpt-4 models are currently limited to subscription users only.</li>
<li>ignore_instructions: the instructions for the model on what changes to ignore. Provided as an array of strings.</li>
<li>ignore_pdf_headers_and_footers: whether to ignore PDF headers and footers. Provided as a boolean.</li>
<li>credit_usage_limit: the maximum number of credits to use for the job. Provided as an integer.</li>
<li>diff_ai_overide_limit: the maximum number of differences to track in a given block. Provided as an integer.</li>
</ul>
<b>Content Spinner</b>
<br>Have Odin generate new content based on your original text and instructions!<br>
<u>Required arguments:</u>
<ul>
<li>input_text: the input text to use for the content spinner. For example: "Odin is a great tool for summarizing documents."</li>
<li>temperature: the desired creativity level to use for the content spinner. A float between 0 and 1, with 0 being the least creative and 1 being the most creative.</li>
<li>model_name: the desired model name to use for the job. Options are: gpt-4-1106-preview, gpt-4o-mini. Note that gpt-4 models are currently limited to subscription users only.</li>
</ul>
<u>Optional arguments:</u>
<ul>
<li>additional_instructions: the additional instructions for the content spinner. Provided as an array of strings.</li>
</ul>
<b>Email Creator</b>
<br>Have Odin generate an email based on your instructions, either as plain text or HTML!<br>
<u>Required arguments:</u>
<ul>
<li>sender: the sender of the email.</li>
<li>content_instructions: the instructions for the content of the email. Provided as an array of strings.</li>
<li>formatting_example: the formatting example for the email. For example: "Please format the email as follows: Greetings, [sender]! I hope you are doing well. [content] Sincerely, [recipient]."</li>
<li>model_name: the desired model name to use for the job. Options are: gpt-4-1106-preview, gpt-4o-mini. Note that gpt-4 models are currently limited to subscription users only.</li>
</ul>
<u>Optional arguments:</u>
<ul>
<li>recipient: the recipient of the email.</li>
<li>generate_html: whether to generate the email as HTML. Provided as a boolean. False by default.</li>
</ul>

### Example


```python
import odin_sdk
from odin_sdk.models.create_assistent_job_response import CreateAssistentJobResponse
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
    api_instance = odin_sdk.AIAssistantJobsApi(api_client)
    document_keys = 'document_keys_example' # str | Stringified json array of strings defining document keys to use with the assistant job.<br>The document keys are full raw file names and full raw URLs. For example: [\\\"test.pdf\\\", \\\"https://www.google.com\\\"]
    job_type = 'job_type_example' # str | The type of job to run.<br>Valid job types are deposition_summary, simple_summary, ab_content_creation, redline_summary, content_spinner, email_creator.
    project_id = 'project_id_example' # str | The project ID to run the job in.
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)
    extra_arguments = 'extra_arguments_example' # str |  (optional)
    job_name = 'c0231c9b-b242-4ccf-84e8-16b6f6275f4c' # str | The desired output name for the job. (optional) (default to 'c0231c9b-b242-4ccf-84e8-16b6f6275f4c')

    try:
        # Create an AI Assistant Job
        api_response = api_instance.create_ai_assistant_job_v2_v2_ai_jobs_create_post(document_keys, job_type, project_id, x_api_key=x_api_key, x_api_secret=x_api_secret, extra_arguments=extra_arguments, job_name=job_name)
        print("The response of AIAssistantJobsApi->create_ai_assistant_job_v2_v2_ai_jobs_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIAssistantJobsApi->create_ai_assistant_job_v2_v2_ai_jobs_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_keys** | **str**| Stringified json array of strings defining document keys to use with the assistant job.&lt;br&gt;The document keys are full raw file names and full raw URLs. For example: [\\\&quot;test.pdf\\\&quot;, \\\&quot;https://www.google.com\\\&quot;] | 
 **job_type** | **str**| The type of job to run.&lt;br&gt;Valid job types are deposition_summary, simple_summary, ab_content_creation, redline_summary, content_spinner, email_creator. | 
 **project_id** | **str**| The project ID to run the job in. | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 
 **extra_arguments** | **str**|  | [optional] 
 **job_name** | **str**| The desired output name for the job. | [optional] [default to &#39;c0231c9b-b242-4ccf-84e8-16b6f6275f4c&#39;]

### Return type

[**CreateAssistentJobResponse**](CreateAssistentJobResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ai_assistant_job_ai_jobs_project_id_job_id_delete**
> DeleteAIJobsResponse delete_ai_assistant_job_ai_jobs_project_id_job_id_delete(project_id, job_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Delete Job

Delete a job and its result from storage.

### Example


```python
import odin_sdk
from odin_sdk.models.delete_ai_jobs_response import DeleteAIJobsResponse
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
    api_instance = odin_sdk.AIAssistantJobsApi(api_client)
    project_id = 'project_id_example' # str | Project ID of the project the job belongs to.
    job_id = 'job_id_example' # str | Job ID of the job to delete.
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Delete Job
        api_response = api_instance.delete_ai_assistant_job_ai_jobs_project_id_job_id_delete(project_id, job_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of AIAssistantJobsApi->delete_ai_assistant_job_ai_jobs_project_id_job_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIAssistantJobsApi->delete_ai_assistant_job_ai_jobs_project_id_job_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID of the project the job belongs to. | 
 **job_id** | **str**| Job ID of the job to delete. | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**DeleteAIJobsResponse**](DeleteAIJobsResponse.md)

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

# **directly_access_content_spinner_ai_content_spinner_post**
> ContentSpinnerResponse directly_access_content_spinner_ai_content_spinner_post(content_spinner_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Create Content from Instructions

Create content from instructions. Accesses the content_spinner job type directly.

### Example


```python
import odin_sdk
from odin_sdk.models.content_spinner_request import ContentSpinnerRequest
from odin_sdk.models.content_spinner_response import ContentSpinnerResponse
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
    api_instance = odin_sdk.AIAssistantJobsApi(api_client)
    content_spinner_request = odin_sdk.ContentSpinnerRequest() # ContentSpinnerRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Create Content from Instructions
        api_response = api_instance.directly_access_content_spinner_ai_content_spinner_post(content_spinner_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of AIAssistantJobsApi->directly_access_content_spinner_ai_content_spinner_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIAssistantJobsApi->directly_access_content_spinner_ai_content_spinner_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_spinner_request** | [**ContentSpinnerRequest**](ContentSpinnerRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**ContentSpinnerResponse**](ContentSpinnerResponse.md)

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

# **directly_access_email_creator_ai_email_creator_post**
> EmailCreatorResponse directly_access_email_creator_ai_email_creator_post(email_creator_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Create an Email from Instructions

Create an email from instructions, either as plain text or HTML. Accesses the email_creator job type directly.

### Example


```python
import odin_sdk
from odin_sdk.models.email_creator_request import EmailCreatorRequest
from odin_sdk.models.email_creator_response import EmailCreatorResponse
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
    api_instance = odin_sdk.AIAssistantJobsApi(api_client)
    email_creator_request = odin_sdk.EmailCreatorRequest() # EmailCreatorRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Create an Email from Instructions
        api_response = api_instance.directly_access_email_creator_ai_email_creator_post(email_creator_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of AIAssistantJobsApi->directly_access_email_creator_ai_email_creator_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIAssistantJobsApi->directly_access_email_creator_ai_email_creator_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_creator_request** | [**EmailCreatorRequest**](EmailCreatorRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**EmailCreatorResponse**](EmailCreatorResponse.md)

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

# **fetch_ai_assistant_job_ai_jobs_project_id_job_id_fetch_get**
> object fetch_ai_assistant_job_ai_jobs_project_id_job_id_fetch_get(project_id, job_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Fetch Job Result

Fetch the result of a job.

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
    api_instance = odin_sdk.AIAssistantJobsApi(api_client)
    project_id = 'project_id_example' # str | Project ID of the project the job belongs to.
    job_id = 'job_id_example' # str | Job ID of the job to fetch.
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Fetch Job Result
        api_response = api_instance.fetch_ai_assistant_job_ai_jobs_project_id_job_id_fetch_get(project_id, job_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of AIAssistantJobsApi->fetch_ai_assistant_job_ai_jobs_project_id_job_id_fetch_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIAssistantJobsApi->fetch_ai_assistant_job_ai_jobs_project_id_job_id_fetch_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID of the project the job belongs to. | 
 **job_id** | **str**| Job ID of the job to fetch. | 
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

# **get_available_ai_job_types_ai_jobs_types_get**
> AIJobTypesResponse get_available_ai_job_types_ai_jobs_types_get(x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Available Job Types

Get the information about available job types.

### Example


```python
import odin_sdk
from odin_sdk.models.ai_job_types_response import AIJobTypesResponse
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
    api_instance = odin_sdk.AIAssistantJobsApi(api_client)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Available Job Types
        api_response = api_instance.get_available_ai_job_types_ai_jobs_types_get(x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of AIAssistantJobsApi->get_available_ai_job_types_ai_jobs_types_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIAssistantJobsApi->get_available_ai_job_types_ai_jobs_types_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**AIJobTypesResponse**](AIJobTypesResponse.md)

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

# **get_jobs_status_ai_jobs_project_id_get**
> GetAssistentJobStatus get_jobs_status_ai_jobs_project_id_get(project_id, limit=limit, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Job Statuses

Get the statuses of all jobs in a project.

### Example


```python
import odin_sdk
from odin_sdk.models.get_assistent_job_status import GetAssistentJobStatus
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
    api_instance = odin_sdk.AIAssistantJobsApi(api_client)
    project_id = 'project_id_example' # str | The ID of the project for which to retrieve job statuses.
    limit = -1 # int | The limit of jobs to retrieve. Use -1 to retrieve all jobs. (optional) (default to -1)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Job Statuses
        api_response = api_instance.get_jobs_status_ai_jobs_project_id_get(project_id, limit=limit, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of AIAssistantJobsApi->get_jobs_status_ai_jobs_project_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIAssistantJobsApi->get_jobs_status_ai_jobs_project_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The ID of the project for which to retrieve job statuses. | 
 **limit** | **int**| The limit of jobs to retrieve. Use -1 to retrieve all jobs. | [optional] [default to -1]
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**GetAssistentJobStatus**](GetAssistentJobStatus.md)

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

