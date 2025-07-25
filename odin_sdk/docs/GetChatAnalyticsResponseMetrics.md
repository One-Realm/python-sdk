# GetChatAnalyticsResponseMetrics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**average_response_time** | **float** |  | 
**average_queries_per_chat** | **float** |  | 
**average_query_token_count** | **float** |  | 
**average_response_token_count** | **float** |  | 
**total_upvotes** | **int** |  | 
**total_downvotes** | **int** |  | 
**total_messages** | **int** |  | 
**average_images_generated** | **int** |  | 
**total_document_usage** | **int** |  | 
**total_kb_search** | **int** |  | 
**total_images_generated** | **int** |  | 
**top_keywords** | **List[object]** |  | 
**top_questions** | **List[object]** |  | 
**regenerated_requests** | **int** |  | 
**users_message_counts** | **object** |  | 
**top_documents** | [**List[DocumentAnalytic]**](DocumentAnalytic.md) |  | 

## Example

```python
from odin_sdk.models.get_chat_analytics_response_metrics import GetChatAnalyticsResponseMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of GetChatAnalyticsResponseMetrics from a JSON string
get_chat_analytics_response_metrics_instance = GetChatAnalyticsResponseMetrics.from_json(json)
# print the JSON string representation of the object
print(GetChatAnalyticsResponseMetrics.to_json())

# convert the object into a dict
get_chat_analytics_response_metrics_dict = get_chat_analytics_response_metrics_instance.to_dict()
# create an instance of GetChatAnalyticsResponseMetrics from a dict
get_chat_analytics_response_metrics_from_dict = GetChatAnalyticsResponseMetrics.from_dict(get_chat_analytics_response_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


