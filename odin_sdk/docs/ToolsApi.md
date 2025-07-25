# odin_sdk.ToolsApi

All URIs are relative to *http://127.0.0.1:8001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ai_classify_tools_ai_classify_post**](ToolsApi.md#ai_classify_tools_ai_classify_post) | **POST** /tools/ai/classify | Ai Classify
[**ai_summary_tools_ai_summarize_post**](ToolsApi.md#ai_summary_tools_ai_summarize_post) | **POST** /tools/ai/summarize | Ai Summary
[**check_pii_in_documents_tools_pii_check_post**](ToolsApi.md#check_pii_in_documents_tools_pii_check_post) | **POST** /tools/pii-check | Check Pii In Documents
[**convert_md_html_tools_md_html_conversion_post**](ToolsApi.md#convert_md_html_tools_md_html_conversion_post) | **POST** /tools/md-html-conversion | Convert Md Html
[**create_blog_from_title_tools_ai_blog_create_auto_post**](ToolsApi.md#create_blog_from_title_tools_ai_blog_create_auto_post) | **POST** /tools/ai/blog/create/auto | Create Blog From Title
[**create_blog_key_points_tools_ai_blog_ideas_post**](ToolsApi.md#create_blog_key_points_tools_ai_blog_ideas_post) | **POST** /tools/ai/blog/ideas | Create Blog Key Points
[**create_blog_sections_tools_ai_blog_sections_post**](ToolsApi.md#create_blog_sections_tools_ai_blog_sections_post) | **POST** /tools/ai/blog/sections | Create Blog Sections
[**create_blog_title_tools_ai_blog_title_post**](ToolsApi.md#create_blog_title_tools_ai_blog_title_post) | **POST** /tools/ai/blog/title | Create Blog Title
[**create_blog_tools_ai_blog_create_post**](ToolsApi.md#create_blog_tools_ai_blog_create_post) | **POST** /tools/ai/blog/create | Create Blog
[**execute_toolkit_tool_step_tools_execute_step_post**](ToolsApi.md#execute_toolkit_tool_step_tools_execute_step_post) | **POST** /tools/execute-step | Execute Toolkit Tool Step
[**extract_data_tools_extract_data_post**](ToolsApi.md#extract_data_tools_extract_data_post) | **POST** /tools/extract_data | Extract Data
[**extract_info_from_file_tools_file_extract_start_post**](ToolsApi.md#extract_info_from_file_tools_file_extract_start_post) | **POST** /tools/file/extract/start | Extract Info From File
[**fetch_data_tools_file_extract_fetch_post**](ToolsApi.md#fetch_data_tools_file_extract_fetch_post) | **POST** /tools/file/extract/fetch | Fetch Data
[**fetch_kb_documents_tools_kb_fetch_documents_post**](ToolsApi.md#fetch_kb_documents_tools_kb_fetch_documents_post) | **POST** /tools/kb/fetch_documents | Fetch Kb Documents
[**find_prospeo_data_tools_prospeo_post**](ToolsApi.md#find_prospeo_data_tools_prospeo_post) | **POST** /tools/prospeo | Find Prospeo Data
[**get_available_tools_by_category_tools_available_by_category_get**](ToolsApi.md#get_available_tools_by_category_tools_available_by_category_get) | **GET** /tools/available/by-category | Get Available Tools By Category
[**get_available_tools_tools_available_get**](ToolsApi.md#get_available_tools_tools_available_get) | **GET** /tools/available | Get Available Tools
[**get_step_result_tools_step_result_project_id_tool_id_step_id_get**](ToolsApi.md#get_step_result_tools_step_result_project_id_tool_id_step_id_get) | **GET** /tools/step-result/{project_id}/{tool_id}/{step_id} | Get Step Result
[**get_stock_data_tools_v2_yahoo_finance_stock_data_post**](ToolsApi.md#get_stock_data_tools_v2_yahoo_finance_stock_data_post) | **POST** /tools/v2/yahoo-finance/stock/data | Get Stock Data
[**recreate_blog_section_tools_ai_blog_regenerate_post**](ToolsApi.md#recreate_blog_section_tools_ai_blog_regenerate_post) | **POST** /tools/ai/blog/regenerate | Recreate Blog Section
[**recreate_blog_section_tools_ai_blog_section_regenerate_post**](ToolsApi.md#recreate_blog_section_tools_ai_blog_section_regenerate_post) | **POST** /tools/ai/blog/section/regenerate | Recreate Blog Section
[**search_available_tools_tools_available_search_get**](ToolsApi.md#search_available_tools_tools_available_search_get) | **GET** /tools/available/search | Search Available Tools
[**translate_texts_tools_ai_translate_post**](ToolsApi.md#translate_texts_tools_ai_translate_post) | **POST** /tools/ai/translate | Translate Texts
[**write_blog_section_tools_create_blog_section_post**](ToolsApi.md#write_blog_section_tools_create_blog_section_post) | **POST** /tools/create_blog_section | Write Blog Section
[**write_blog_tools_ai_blog_write_post**](ToolsApi.md#write_blog_tools_ai_blog_write_post) | **POST** /tools/ai/blog/write | Write Blog


# **ai_classify_tools_ai_classify_post**
> AIClassifyResponse ai_classify_tools_ai_classify_post(ai_classify_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Ai Classify

### Example


```python
import odin_sdk
from odin_sdk.models.ai_classify_request import AIClassifyRequest
from odin_sdk.models.ai_classify_response import AIClassifyResponse
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
    api_instance = odin_sdk.ToolsApi(api_client)
    ai_classify_request = odin_sdk.AIClassifyRequest() # AIClassifyRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Ai Classify
        api_response = api_instance.ai_classify_tools_ai_classify_post(ai_classify_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ToolsApi->ai_classify_tools_ai_classify_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->ai_classify_tools_ai_classify_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_classify_request** | [**AIClassifyRequest**](AIClassifyRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**AIClassifyResponse**](AIClassifyResponse.md)

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

# **ai_summary_tools_ai_summarize_post**
> AISummarizeResponse ai_summary_tools_ai_summarize_post(ai_summarize_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Ai Summary

Create a summary of a message based on provided instructions.

### Example


```python
import odin_sdk
from odin_sdk.models.ai_summarize_request import AISummarizeRequest
from odin_sdk.models.ai_summarize_response import AISummarizeResponse
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
    api_instance = odin_sdk.ToolsApi(api_client)
    ai_summarize_request = odin_sdk.AISummarizeRequest() # AISummarizeRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Ai Summary
        api_response = api_instance.ai_summary_tools_ai_summarize_post(ai_summarize_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ToolsApi->ai_summary_tools_ai_summarize_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->ai_summary_tools_ai_summarize_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_summarize_request** | [**AISummarizeRequest**](AISummarizeRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**AISummarizeResponse**](AISummarizeResponse.md)

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

# **check_pii_in_documents_tools_pii_check_post**
> object check_pii_in_documents_tools_pii_check_post(pii_check_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Check Pii In Documents

### Example


```python
import odin_sdk
from odin_sdk.models.pii_check_request import PIICheckRequest
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
    api_instance = odin_sdk.ToolsApi(api_client)
    pii_check_request = odin_sdk.PIICheckRequest() # PIICheckRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Check Pii In Documents
        api_response = api_instance.check_pii_in_documents_tools_pii_check_post(pii_check_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ToolsApi->check_pii_in_documents_tools_pii_check_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->check_pii_in_documents_tools_pii_check_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pii_check_request** | [**PIICheckRequest**](PIICheckRequest.md)|  | 
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

# **convert_md_html_tools_md_html_conversion_post**
> object convert_md_html_tools_md_html_conversion_post(md_html_conversion_request)

Convert Md Html

### Example


```python
import odin_sdk
from odin_sdk.models.md_html_conversion_request import MdHTMLConversionRequest
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
    api_instance = odin_sdk.ToolsApi(api_client)
    md_html_conversion_request = odin_sdk.MdHTMLConversionRequest() # MdHTMLConversionRequest | 

    try:
        # Convert Md Html
        api_response = api_instance.convert_md_html_tools_md_html_conversion_post(md_html_conversion_request)
        print("The response of ToolsApi->convert_md_html_tools_md_html_conversion_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->convert_md_html_tools_md_html_conversion_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **md_html_conversion_request** | [**MdHTMLConversionRequest**](MdHTMLConversionRequest.md)|  | 

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

# **create_blog_from_title_tools_ai_blog_create_auto_post**
> BlogResponse create_blog_from_title_tools_ai_blog_create_auto_post(blog_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Create Blog From Title

### Example


```python
import odin_sdk
from odin_sdk.models.blog_request import BlogRequest
from odin_sdk.models.blog_response import BlogResponse
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
    api_instance = odin_sdk.ToolsApi(api_client)
    blog_request = odin_sdk.BlogRequest() # BlogRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Create Blog From Title
        api_response = api_instance.create_blog_from_title_tools_ai_blog_create_auto_post(blog_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ToolsApi->create_blog_from_title_tools_ai_blog_create_auto_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->create_blog_from_title_tools_ai_blog_create_auto_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blog_request** | [**BlogRequest**](BlogRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**BlogResponse**](BlogResponse.md)

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

# **create_blog_key_points_tools_ai_blog_ideas_post**
> BlogResponse create_blog_key_points_tools_ai_blog_ideas_post(blog_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Create Blog Key Points

### Example


```python
import odin_sdk
from odin_sdk.models.blog_request import BlogRequest
from odin_sdk.models.blog_response import BlogResponse
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
    api_instance = odin_sdk.ToolsApi(api_client)
    blog_request = odin_sdk.BlogRequest() # BlogRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Create Blog Key Points
        api_response = api_instance.create_blog_key_points_tools_ai_blog_ideas_post(blog_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ToolsApi->create_blog_key_points_tools_ai_blog_ideas_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->create_blog_key_points_tools_ai_blog_ideas_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blog_request** | [**BlogRequest**](BlogRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**BlogResponse**](BlogResponse.md)

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

# **create_blog_sections_tools_ai_blog_sections_post**
> BlogResponse create_blog_sections_tools_ai_blog_sections_post(blog_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Create Blog Sections

### Example


```python
import odin_sdk
from odin_sdk.models.blog_request import BlogRequest
from odin_sdk.models.blog_response import BlogResponse
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
    api_instance = odin_sdk.ToolsApi(api_client)
    blog_request = odin_sdk.BlogRequest() # BlogRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Create Blog Sections
        api_response = api_instance.create_blog_sections_tools_ai_blog_sections_post(blog_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ToolsApi->create_blog_sections_tools_ai_blog_sections_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->create_blog_sections_tools_ai_blog_sections_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blog_request** | [**BlogRequest**](BlogRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**BlogResponse**](BlogResponse.md)

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

# **create_blog_title_tools_ai_blog_title_post**
> object create_blog_title_tools_ai_blog_title_post(blog_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Create Blog Title

### Example


```python
import odin_sdk
from odin_sdk.models.blog_request import BlogRequest
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
    api_instance = odin_sdk.ToolsApi(api_client)
    blog_request = odin_sdk.BlogRequest() # BlogRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Create Blog Title
        api_response = api_instance.create_blog_title_tools_ai_blog_title_post(blog_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ToolsApi->create_blog_title_tools_ai_blog_title_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->create_blog_title_tools_ai_blog_title_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blog_request** | [**BlogRequest**](BlogRequest.md)|  | 
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

# **create_blog_tools_ai_blog_create_post**
> BlogResponse create_blog_tools_ai_blog_create_post(blog_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Create Blog

### Example


```python
import odin_sdk
from odin_sdk.models.blog_request import BlogRequest
from odin_sdk.models.blog_response import BlogResponse
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
    api_instance = odin_sdk.ToolsApi(api_client)
    blog_request = odin_sdk.BlogRequest() # BlogRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Create Blog
        api_response = api_instance.create_blog_tools_ai_blog_create_post(blog_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ToolsApi->create_blog_tools_ai_blog_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->create_blog_tools_ai_blog_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blog_request** | [**BlogRequest**](BlogRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**BlogResponse**](BlogResponse.md)

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

# **execute_toolkit_tool_step_tools_execute_step_post**
> object execute_toolkit_tool_step_tools_execute_step_post(body, x_api_key=x_api_key, x_api_secret=x_api_secret)

Execute Toolkit Tool Step

Execute a single toolkit tool step for custom tool testing

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
    api_instance = odin_sdk.ToolsApi(api_client)
    body = None # object | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Execute Toolkit Tool Step
        api_response = api_instance.execute_toolkit_tool_step_tools_execute_step_post(body, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ToolsApi->execute_toolkit_tool_step_tools_execute_step_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->execute_toolkit_tool_step_tools_execute_step_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**|  | 
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

# **extract_data_tools_extract_data_post**
> object extract_data_tools_extract_data_post(extract_meta_data_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Extract Data

Extracts information from the given text based on the specified information to extract.

Args:
    req: The request object containing the text and information to extract.

Returns:
    dict: A JSON object containing the extracted information with the keys as the specified information to extract. If the specified information is not found in the text, it returns "None".

### Example


```python
import odin_sdk
from odin_sdk.models.extract_meta_data_request import ExtractMetaDataRequest
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
    api_instance = odin_sdk.ToolsApi(api_client)
    extract_meta_data_request = odin_sdk.ExtractMetaDataRequest() # ExtractMetaDataRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Extract Data
        api_response = api_instance.extract_data_tools_extract_data_post(extract_meta_data_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ToolsApi->extract_data_tools_extract_data_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->extract_data_tools_extract_data_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extract_meta_data_request** | [**ExtractMetaDataRequest**](ExtractMetaDataRequest.md)|  | 
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

# **extract_info_from_file_tools_file_extract_start_post**
> ExtractDataResponse extract_info_from_file_tools_file_extract_start_post(file, prompt, project_id, extract_commands, x_api_key=x_api_key, x_api_secret=x_api_secret)

Extract Info From File

Gets the data from the file based on the commands provided.

### Example


```python
import odin_sdk
from odin_sdk.models.extract_data_response import ExtractDataResponse
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
    api_instance = odin_sdk.ToolsApi(api_client)
    file = None # bytearray | 
    prompt = 'prompt_example' # str | 
    project_id = 'project_id_example' # str | 
    extract_commands = 'extract_commands_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Extract Info From File
        api_response = api_instance.extract_info_from_file_tools_file_extract_start_post(file, prompt, project_id, extract_commands, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ToolsApi->extract_info_from_file_tools_file_extract_start_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->extract_info_from_file_tools_file_extract_start_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**|  | 
 **prompt** | **str**|  | 
 **project_id** | **str**|  | 
 **extract_commands** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**ExtractDataResponse**](ExtractDataResponse.md)

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

# **fetch_data_tools_file_extract_fetch_post**
> FetchDataResponse fetch_data_tools_file_extract_fetch_post(fetch_data_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Fetch Data

Retrieves data from a specific project and job..

### Example


```python
import odin_sdk
from odin_sdk.models.fetch_data_request import FetchDataRequest
from odin_sdk.models.fetch_data_response import FetchDataResponse
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
    api_instance = odin_sdk.ToolsApi(api_client)
    fetch_data_request = odin_sdk.FetchDataRequest() # FetchDataRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Fetch Data
        api_response = api_instance.fetch_data_tools_file_extract_fetch_post(fetch_data_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ToolsApi->fetch_data_tools_file_extract_fetch_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->fetch_data_tools_file_extract_fetch_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fetch_data_request** | [**FetchDataRequest**](FetchDataRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**FetchDataResponse**](FetchDataResponse.md)

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

# **fetch_kb_documents_tools_kb_fetch_documents_post**
> FetchKBDocumentsResponse fetch_kb_documents_tools_kb_fetch_documents_post(fetch_kb_documents_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Fetch Kb Documents

Retrieves documents from the KB.

### Example


```python
import odin_sdk
from odin_sdk.models.fetch_kb_documents_request import FetchKBDocumentsRequest
from odin_sdk.models.fetch_kb_documents_response import FetchKBDocumentsResponse
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
    api_instance = odin_sdk.ToolsApi(api_client)
    fetch_kb_documents_request = odin_sdk.FetchKBDocumentsRequest() # FetchKBDocumentsRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Fetch Kb Documents
        api_response = api_instance.fetch_kb_documents_tools_kb_fetch_documents_post(fetch_kb_documents_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ToolsApi->fetch_kb_documents_tools_kb_fetch_documents_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->fetch_kb_documents_tools_kb_fetch_documents_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fetch_kb_documents_request** | [**FetchKBDocumentsRequest**](FetchKBDocumentsRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**FetchKBDocumentsResponse**](FetchKBDocumentsResponse.md)

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

# **find_prospeo_data_tools_prospeo_post**
> object find_prospeo_data_tools_prospeo_post(body_find_prospeo_data_tools_prospeo_post, x_api_key=x_api_key, x_api_secret=x_api_secret)

Find Prospeo Data

### Example


```python
import odin_sdk
from odin_sdk.models.body_find_prospeo_data_tools_prospeo_post import BodyFindProspeoDataToolsProspeoPost
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
    api_instance = odin_sdk.ToolsApi(api_client)
    body_find_prospeo_data_tools_prospeo_post = odin_sdk.BodyFindProspeoDataToolsProspeoPost() # BodyFindProspeoDataToolsProspeoPost | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Find Prospeo Data
        api_response = api_instance.find_prospeo_data_tools_prospeo_post(body_find_prospeo_data_tools_prospeo_post, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ToolsApi->find_prospeo_data_tools_prospeo_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->find_prospeo_data_tools_prospeo_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body_find_prospeo_data_tools_prospeo_post** | [**BodyFindProspeoDataToolsProspeoPost**](BodyFindProspeoDataToolsProspeoPost.md)|  | 
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

# **get_available_tools_by_category_tools_available_by_category_get**
> object get_available_tools_by_category_tools_available_by_category_get(project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Available Tools By Category

Get all available toolkit tools organized by category

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
    api_instance = odin_sdk.ToolsApi(api_client)
    project_id = 'project_id_example' # str | Project ID
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Available Tools By Category
        api_response = api_instance.get_available_tools_by_category_tools_available_by_category_get(project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ToolsApi->get_available_tools_by_category_tools_available_by_category_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->get_available_tools_by_category_tools_available_by_category_get: %s\n" % e)
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

# **get_available_tools_tools_available_get**
> object get_available_tools_tools_available_get(project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Available Tools

Get all available toolkit tools with their input schemas for custom tool creation

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
    api_instance = odin_sdk.ToolsApi(api_client)
    project_id = 'project_id_example' # str | Project ID
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Available Tools
        api_response = api_instance.get_available_tools_tools_available_get(project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ToolsApi->get_available_tools_tools_available_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->get_available_tools_tools_available_get: %s\n" % e)
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

# **get_step_result_tools_step_result_project_id_tool_id_step_id_get**
> StepExecutionResult get_step_result_tools_step_result_project_id_tool_id_step_id_get(project_id, tool_id, step_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Step Result

Get step execution result

### Example


```python
import odin_sdk
from odin_sdk.models.step_execution_result import StepExecutionResult
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
    api_instance = odin_sdk.ToolsApi(api_client)
    project_id = 'project_id_example' # str | 
    tool_id = 'tool_id_example' # str | 
    step_id = 'step_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Step Result
        api_response = api_instance.get_step_result_tools_step_result_project_id_tool_id_step_id_get(project_id, tool_id, step_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ToolsApi->get_step_result_tools_step_result_project_id_tool_id_step_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->get_step_result_tools_step_result_project_id_tool_id_step_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **tool_id** | **str**|  | 
 **step_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**StepExecutionResult**](StepExecutionResult.md)

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

# **get_stock_data_tools_v2_yahoo_finance_stock_data_post**
> object get_stock_data_tools_v2_yahoo_finance_stock_data_post(stock_data_request)

Get Stock Data

Get stock data for a given symbol and metrics

### Example


```python
import odin_sdk
from odin_sdk.models.stock_data_request import StockDataRequest
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
    api_instance = odin_sdk.ToolsApi(api_client)
    stock_data_request = odin_sdk.StockDataRequest() # StockDataRequest | 

    try:
        # Get Stock Data
        api_response = api_instance.get_stock_data_tools_v2_yahoo_finance_stock_data_post(stock_data_request)
        print("The response of ToolsApi->get_stock_data_tools_v2_yahoo_finance_stock_data_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->get_stock_data_tools_v2_yahoo_finance_stock_data_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stock_data_request** | [**StockDataRequest**](StockDataRequest.md)|  | 

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

# **recreate_blog_section_tools_ai_blog_regenerate_post**
> BlogRegenerateResponse recreate_blog_section_tools_ai_blog_regenerate_post(blog_regenerate_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Recreate Blog Section

### Example


```python
import odin_sdk
from odin_sdk.models.blog_regenerate_request import BlogRegenerateRequest
from odin_sdk.models.blog_regenerate_response import BlogRegenerateResponse
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
    api_instance = odin_sdk.ToolsApi(api_client)
    blog_regenerate_request = odin_sdk.BlogRegenerateRequest() # BlogRegenerateRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Recreate Blog Section
        api_response = api_instance.recreate_blog_section_tools_ai_blog_regenerate_post(blog_regenerate_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ToolsApi->recreate_blog_section_tools_ai_blog_regenerate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->recreate_blog_section_tools_ai_blog_regenerate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blog_regenerate_request** | [**BlogRegenerateRequest**](BlogRegenerateRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**BlogRegenerateResponse**](BlogRegenerateResponse.md)

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

# **recreate_blog_section_tools_ai_blog_section_regenerate_post**
> BlogRegenerateSectionResponse recreate_blog_section_tools_ai_blog_section_regenerate_post(blog_regenerate_section_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Recreate Blog Section

### Example


```python
import odin_sdk
from odin_sdk.models.blog_regenerate_section_request import BlogRegenerateSectionRequest
from odin_sdk.models.blog_regenerate_section_response import BlogRegenerateSectionResponse
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
    api_instance = odin_sdk.ToolsApi(api_client)
    blog_regenerate_section_request = odin_sdk.BlogRegenerateSectionRequest() # BlogRegenerateSectionRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Recreate Blog Section
        api_response = api_instance.recreate_blog_section_tools_ai_blog_section_regenerate_post(blog_regenerate_section_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ToolsApi->recreate_blog_section_tools_ai_blog_section_regenerate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->recreate_blog_section_tools_ai_blog_section_regenerate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blog_regenerate_section_request** | [**BlogRegenerateSectionRequest**](BlogRegenerateSectionRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**BlogRegenerateSectionResponse**](BlogRegenerateSectionResponse.md)

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

# **search_available_tools_tools_available_search_get**
> object search_available_tools_tools_available_search_get(project_id, q, x_api_key=x_api_key, x_api_secret=x_api_secret)

Search Available Tools

Search available toolkit tools by name or description

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
    api_instance = odin_sdk.ToolsApi(api_client)
    project_id = 'project_id_example' # str | Project ID
    q = 'q_example' # str | Search query
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Search Available Tools
        api_response = api_instance.search_available_tools_tools_available_search_get(project_id, q, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ToolsApi->search_available_tools_tools_available_search_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->search_available_tools_tools_available_search_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **q** | **str**| Search query | 
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

# **translate_texts_tools_ai_translate_post**
> TranslateTextsResponse translate_texts_tools_ai_translate_post(translate_texts_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Translate Texts

Translates the text from one language to another language.

### Example


```python
import odin_sdk
from odin_sdk.models.translate_texts_request import TranslateTextsRequest
from odin_sdk.models.translate_texts_response import TranslateTextsResponse
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
    api_instance = odin_sdk.ToolsApi(api_client)
    translate_texts_request = odin_sdk.TranslateTextsRequest() # TranslateTextsRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Translate Texts
        api_response = api_instance.translate_texts_tools_ai_translate_post(translate_texts_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ToolsApi->translate_texts_tools_ai_translate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->translate_texts_tools_ai_translate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **translate_texts_request** | [**TranslateTextsRequest**](TranslateTextsRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**TranslateTextsResponse**](TranslateTextsResponse.md)

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

# **write_blog_section_tools_create_blog_section_post**
> CreateBlogSectionResponse write_blog_section_tools_create_blog_section_post(create_blog_section_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Write Blog Section

### Example


```python
import odin_sdk
from odin_sdk.models.create_blog_section_request import CreateBlogSectionRequest
from odin_sdk.models.create_blog_section_response import CreateBlogSectionResponse
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
    api_instance = odin_sdk.ToolsApi(api_client)
    create_blog_section_request = odin_sdk.CreateBlogSectionRequest() # CreateBlogSectionRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Write Blog Section
        api_response = api_instance.write_blog_section_tools_create_blog_section_post(create_blog_section_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ToolsApi->write_blog_section_tools_create_blog_section_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->write_blog_section_tools_create_blog_section_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_blog_section_request** | [**CreateBlogSectionRequest**](CreateBlogSectionRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**CreateBlogSectionResponse**](CreateBlogSectionResponse.md)

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

# **write_blog_tools_ai_blog_write_post**
> BlogResponse write_blog_tools_ai_blog_write_post(blog_request, x_api_key=x_api_key, x_api_secret=x_api_secret)

Write Blog

### Example


```python
import odin_sdk
from odin_sdk.models.blog_request import BlogRequest
from odin_sdk.models.blog_response import BlogResponse
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
    api_instance = odin_sdk.ToolsApi(api_client)
    blog_request = odin_sdk.BlogRequest() # BlogRequest | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Write Blog
        api_response = api_instance.write_blog_tools_ai_blog_write_post(blog_request, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of ToolsApi->write_blog_tools_ai_blog_write_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->write_blog_tools_ai_blog_write_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blog_request** | [**BlogRequest**](BlogRequest.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**BlogResponse**](BlogResponse.md)

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

