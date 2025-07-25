# odin_sdk.QueryCacheApi

All URIs are relative to *http://127.0.0.1:8001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_query_project_project_id_caching_query_delete_query_id_delete**](QueryCacheApi.md#delete_query_project_project_id_caching_query_delete_query_id_delete) | **DELETE** /project/{project_id}/caching/query/delete/{query_id} | Delete Query
[**delete_table_project_project_id_caching_query_delete_by_ids_post**](QueryCacheApi.md#delete_table_project_project_id_caching_query_delete_by_ids_post) | **POST** /project/{project_id}/caching/query/delete_by_ids | Delete Table
[**get_all_queries_project_project_id_caching_query_get_all_get**](QueryCacheApi.md#get_all_queries_project_project_id_caching_query_get_all_get) | **GET** /project/{project_id}/caching/query/get_all | Get All Queries
[**get_all_queries_project_project_id_caching_query_get_by_ids_post**](QueryCacheApi.md#get_all_queries_project_project_id_caching_query_get_by_ids_post) | **POST** /project/{project_id}/caching/query/get_by_ids | Get All Queries
[**get_query_by_id_project_project_id_caching_query_get_by_doc_id_doc_id_get**](QueryCacheApi.md#get_query_by_id_project_project_id_caching_query_get_by_doc_id_doc_id_get) | **GET** /project/{project_id}/caching/query/get_by_doc_id/{doc_id} | Get Query By Id
[**get_query_by_id_project_project_id_caching_query_get_query_id_get**](QueryCacheApi.md#get_query_by_id_project_project_id_caching_query_get_query_id_get) | **GET** /project/{project_id}/caching/query/get/{query_id} | Get Query By Id
[**save_query_and_docs_project_project_id_caching_query_insert_post**](QueryCacheApi.md#save_query_and_docs_project_project_id_caching_query_insert_post) | **POST** /project/{project_id}/caching/query/insert | Save Query And Docs
[**update_query_docs_project_project_id_caching_query_update_query_id_post**](QueryCacheApi.md#update_query_docs_project_project_id_caching_query_update_query_id_post) | **POST** /project/{project_id}/caching/query/update/{query_id} | Update Query Docs


# **delete_query_project_project_id_caching_query_delete_query_id_delete**
> Queries delete_query_project_project_id_caching_query_delete_query_id_delete(query_id, project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Delete Query

Delete query from cache

### Example


```python
import odin_sdk
from odin_sdk.models.queries import Queries
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
    api_instance = odin_sdk.QueryCacheApi(api_client)
    query_id = 'query_id_example' # str | 
    project_id = 'project_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Delete Query
        api_response = api_instance.delete_query_project_project_id_caching_query_delete_query_id_delete(query_id, project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of QueryCacheApi->delete_query_project_project_id_caching_query_delete_query_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QueryCacheApi->delete_query_project_project_id_caching_query_delete_query_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_id** | **str**|  | 
 **project_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**Queries**](Queries.md)

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

# **delete_table_project_project_id_caching_query_delete_by_ids_post**
> Queries delete_table_project_project_id_caching_query_delete_by_ids_post(project_id, query_ids, x_api_key=x_api_key, x_api_secret=x_api_secret)

Delete Table

Delete queries from cache by ids

### Example


```python
import odin_sdk
from odin_sdk.models.queries import Queries
from odin_sdk.models.query_ids import QueryIds
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
    api_instance = odin_sdk.QueryCacheApi(api_client)
    project_id = 'project_id_example' # str | 
    query_ids = odin_sdk.QueryIds() # QueryIds | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Delete Table
        api_response = api_instance.delete_table_project_project_id_caching_query_delete_by_ids_post(project_id, query_ids, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of QueryCacheApi->delete_table_project_project_id_caching_query_delete_by_ids_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QueryCacheApi->delete_table_project_project_id_caching_query_delete_by_ids_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **query_ids** | [**QueryIds**](QueryIds.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**Queries**](Queries.md)

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

# **get_all_queries_project_project_id_caching_query_get_all_get**
> Queries get_all_queries_project_project_id_caching_query_get_all_get(project_id, page=page, items_per_page=items_per_page, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get All Queries

Get all queries from cache with pagination

### Example


```python
import odin_sdk
from odin_sdk.models.queries import Queries
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
    api_instance = odin_sdk.QueryCacheApi(api_client)
    project_id = 'project_id_example' # str | 
    page = 1 # int |  (optional) (default to 1)
    items_per_page = 10 # int |  (optional) (default to 10)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get All Queries
        api_response = api_instance.get_all_queries_project_project_id_caching_query_get_all_get(project_id, page=page, items_per_page=items_per_page, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of QueryCacheApi->get_all_queries_project_project_id_caching_query_get_all_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QueryCacheApi->get_all_queries_project_project_id_caching_query_get_all_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **page** | **int**|  | [optional] [default to 1]
 **items_per_page** | **int**|  | [optional] [default to 10]
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**Queries**](Queries.md)

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

# **get_all_queries_project_project_id_caching_query_get_by_ids_post**
> Queries get_all_queries_project_project_id_caching_query_get_by_ids_post(project_id, query_ids, page=page, items_per_page=items_per_page, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get All Queries

Get all queries from cache with pagination

### Example


```python
import odin_sdk
from odin_sdk.models.queries import Queries
from odin_sdk.models.query_ids import QueryIds
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
    api_instance = odin_sdk.QueryCacheApi(api_client)
    project_id = 'project_id_example' # str | 
    query_ids = odin_sdk.QueryIds() # QueryIds | 
    page = 1 # int |  (optional) (default to 1)
    items_per_page = 10 # int |  (optional) (default to 10)
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get All Queries
        api_response = api_instance.get_all_queries_project_project_id_caching_query_get_by_ids_post(project_id, query_ids, page=page, items_per_page=items_per_page, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of QueryCacheApi->get_all_queries_project_project_id_caching_query_get_by_ids_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QueryCacheApi->get_all_queries_project_project_id_caching_query_get_by_ids_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **query_ids** | [**QueryIds**](QueryIds.md)|  | 
 **page** | **int**|  | [optional] [default to 1]
 **items_per_page** | **int**|  | [optional] [default to 10]
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**Queries**](Queries.md)

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

# **get_query_by_id_project_project_id_caching_query_get_by_doc_id_doc_id_get**
> Queries get_query_by_id_project_project_id_caching_query_get_by_doc_id_doc_id_get(doc_id, project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Query By Id

Get query and doc_ids by ID

### Example


```python
import odin_sdk
from odin_sdk.models.queries import Queries
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
    api_instance = odin_sdk.QueryCacheApi(api_client)
    doc_id = 'doc_id_example' # str | 
    project_id = 'project_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Query By Id
        api_response = api_instance.get_query_by_id_project_project_id_caching_query_get_by_doc_id_doc_id_get(doc_id, project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of QueryCacheApi->get_query_by_id_project_project_id_caching_query_get_by_doc_id_doc_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QueryCacheApi->get_query_by_id_project_project_id_caching_query_get_by_doc_id_doc_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **doc_id** | **str**|  | 
 **project_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**Queries**](Queries.md)

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

# **get_query_by_id_project_project_id_caching_query_get_query_id_get**
> StoredQuery get_query_by_id_project_project_id_caching_query_get_query_id_get(query_id, project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)

Get Query By Id

Get query and doc_ids by ID

### Example


```python
import odin_sdk
from odin_sdk.models.stored_query import StoredQuery
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
    api_instance = odin_sdk.QueryCacheApi(api_client)
    query_id = 'query_id_example' # str | 
    project_id = 'project_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Get Query By Id
        api_response = api_instance.get_query_by_id_project_project_id_caching_query_get_query_id_get(query_id, project_id, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of QueryCacheApi->get_query_by_id_project_project_id_caching_query_get_query_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QueryCacheApi->get_query_by_id_project_project_id_caching_query_get_query_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_id** | **str**|  | 
 **project_id** | **str**|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**StoredQuery**](StoredQuery.md)

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

# **save_query_and_docs_project_project_id_caching_query_insert_post**
> InsertResponse save_query_and_docs_project_project_id_caching_query_insert_post(project_id, query_payload, x_api_key=x_api_key, x_api_secret=x_api_secret)

Save Query And Docs

Cache query and documents for later retrieval

### Example


```python
import odin_sdk
from odin_sdk.models.insert_response import InsertResponse
from odin_sdk.models.query_payload import QueryPayload
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
    api_instance = odin_sdk.QueryCacheApi(api_client)
    project_id = 'project_id_example' # str | 
    query_payload = odin_sdk.QueryPayload() # QueryPayload | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Save Query And Docs
        api_response = api_instance.save_query_and_docs_project_project_id_caching_query_insert_post(project_id, query_payload, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of QueryCacheApi->save_query_and_docs_project_project_id_caching_query_insert_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QueryCacheApi->save_query_and_docs_project_project_id_caching_query_insert_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **query_payload** | [**QueryPayload**](QueryPayload.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**InsertResponse**](InsertResponse.md)

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

# **update_query_docs_project_project_id_caching_query_update_query_id_post**
> InsertResponse update_query_docs_project_project_id_caching_query_update_query_id_post(project_id, query_id, query_payload, x_api_key=x_api_key, x_api_secret=x_api_secret)

Update Query Docs

Update stored query for knowledge base reranking

### Example


```python
import odin_sdk
from odin_sdk.models.insert_response import InsertResponse
from odin_sdk.models.query_payload import QueryPayload
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
    api_instance = odin_sdk.QueryCacheApi(api_client)
    project_id = 'project_id_example' # str | 
    query_id = 'query_id_example' # str | 
    query_payload = odin_sdk.QueryPayload() # QueryPayload | 
    x_api_key = 'x_api_key_example' # str | Your Odin API key. (optional)
    x_api_secret = 'x_api_secret_example' # str | Your Odin API secret. (optional)

    try:
        # Update Query Docs
        api_response = api_instance.update_query_docs_project_project_id_caching_query_update_query_id_post(project_id, query_id, query_payload, x_api_key=x_api_key, x_api_secret=x_api_secret)
        print("The response of QueryCacheApi->update_query_docs_project_project_id_caching_query_update_query_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QueryCacheApi->update_query_docs_project_project_id_caching_query_update_query_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **query_id** | **str**|  | 
 **query_payload** | [**QueryPayload**](QueryPayload.md)|  | 
 **x_api_key** | **str**| Your Odin API key. | [optional] 
 **x_api_secret** | **str**| Your Odin API secret. | [optional] 

### Return type

[**InsertResponse**](InsertResponse.md)

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

