# GetChatAnalyticsResponseNLPMetrics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**overall_keywords** | [**List[Keyword]**](Keyword.md) |  | 
**upvoted_keywords** | [**List[Keyword]**](Keyword.md) |  | 
**downvoted_keywords** | [**List[Keyword]**](Keyword.md) |  | 

## Example

```python
from odin_sdk.models.get_chat_analytics_response_nlp_metrics import GetChatAnalyticsResponseNLPMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of GetChatAnalyticsResponseNLPMetrics from a JSON string
get_chat_analytics_response_nlp_metrics_instance = GetChatAnalyticsResponseNLPMetrics.from_json(json)
# print the JSON string representation of the object
print(GetChatAnalyticsResponseNLPMetrics.to_json())

# convert the object into a dict
get_chat_analytics_response_nlp_metrics_dict = get_chat_analytics_response_nlp_metrics_instance.to_dict()
# create an instance of GetChatAnalyticsResponseNLPMetrics from a dict
get_chat_analytics_response_nlp_metrics_from_dict = GetChatAnalyticsResponseNLPMetrics.from_dict(get_chat_analytics_response_nlp_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


