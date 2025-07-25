# KnowledgeBaseAnalyticsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_messages** | **int** |  | 
**total_responses** | **int** |  | 
**failed_messages** | **int** |  | 
**avg_messages_per_user** | **float** |  | 
**avg_message_length** | **float** |  | 
**avg_response_length** | **float** |  | 
**avg_message_per_convo** | **float** |  | 
**positive_feedback** | **float** |  | 
**negative_feedback** | **float** |  | 
**similar_messages** | [**Dict[str, MessageGroup]**](MessageGroup.md) |  | 

## Example

```python
from odin_sdk.models.knowledge_base_analytics_response import KnowledgeBaseAnalyticsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeBaseAnalyticsResponse from a JSON string
knowledge_base_analytics_response_instance = KnowledgeBaseAnalyticsResponse.from_json(json)
# print the JSON string representation of the object
print(KnowledgeBaseAnalyticsResponse.to_json())

# convert the object into a dict
knowledge_base_analytics_response_dict = knowledge_base_analytics_response_instance.to_dict()
# create an instance of KnowledgeBaseAnalyticsResponse from a dict
knowledge_base_analytics_response_from_dict = KnowledgeBaseAnalyticsResponse.from_dict(knowledge_base_analytics_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


