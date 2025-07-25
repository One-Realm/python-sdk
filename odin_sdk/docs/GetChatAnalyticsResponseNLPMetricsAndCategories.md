# GetChatAnalyticsResponseNLPMetricsAndCategories


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nlp_metrics** | [**GetChatAnalyticsResponseNLPMetrics**](GetChatAnalyticsResponseNLPMetrics.md) |  | 
**categories** | [**List[CategoryOutput]**](CategoryOutput.md) |  | 

## Example

```python
from odin_sdk.models.get_chat_analytics_response_nlp_metrics_and_categories import GetChatAnalyticsResponseNLPMetricsAndCategories

# TODO update the JSON string below
json = "{}"
# create an instance of GetChatAnalyticsResponseNLPMetricsAndCategories from a JSON string
get_chat_analytics_response_nlp_metrics_and_categories_instance = GetChatAnalyticsResponseNLPMetricsAndCategories.from_json(json)
# print the JSON string representation of the object
print(GetChatAnalyticsResponseNLPMetricsAndCategories.to_json())

# convert the object into a dict
get_chat_analytics_response_nlp_metrics_and_categories_dict = get_chat_analytics_response_nlp_metrics_and_categories_instance.to_dict()
# create an instance of GetChatAnalyticsResponseNLPMetricsAndCategories from a dict
get_chat_analytics_response_nlp_metrics_and_categories_from_dict = GetChatAnalyticsResponseNLPMetricsAndCategories.from_dict(get_chat_analytics_response_nlp_metrics_and_categories_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


