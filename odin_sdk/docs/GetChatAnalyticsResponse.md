# GetChatAnalyticsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metrics** | [**GetChatAnalyticsResponseMetrics**](GetChatAnalyticsResponseMetrics.md) |  | 
**time_series** | [**List[DailyQueryAndFeedbackCount]**](DailyQueryAndFeedbackCount.md) |  | 
**nlp_metrics** | [**GetChatAnalyticsResponseNLPMetrics**](GetChatAnalyticsResponseNLPMetrics.md) |  | 
**categories** | [**List[CategoryOutput]**](CategoryOutput.md) |  | 

## Example

```python
from odin_sdk.models.get_chat_analytics_response import GetChatAnalyticsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetChatAnalyticsResponse from a JSON string
get_chat_analytics_response_instance = GetChatAnalyticsResponse.from_json(json)
# print the JSON string representation of the object
print(GetChatAnalyticsResponse.to_json())

# convert the object into a dict
get_chat_analytics_response_dict = get_chat_analytics_response_instance.to_dict()
# create an instance of GetChatAnalyticsResponse from a dict
get_chat_analytics_response_from_dict = GetChatAnalyticsResponse.from_dict(get_chat_analytics_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


