# GetChatAnalyticsResponseMetricsAndTimeseries


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metrics** | [**GetChatAnalyticsResponseMetrics**](GetChatAnalyticsResponseMetrics.md) |  | 
**time_series** | [**List[DailyQueryAndFeedbackCount]**](DailyQueryAndFeedbackCount.md) |  | 

## Example

```python
from odin_sdk.models.get_chat_analytics_response_metrics_and_timeseries import GetChatAnalyticsResponseMetricsAndTimeseries

# TODO update the JSON string below
json = "{}"
# create an instance of GetChatAnalyticsResponseMetricsAndTimeseries from a JSON string
get_chat_analytics_response_metrics_and_timeseries_instance = GetChatAnalyticsResponseMetricsAndTimeseries.from_json(json)
# print the JSON string representation of the object
print(GetChatAnalyticsResponseMetricsAndTimeseries.to_json())

# convert the object into a dict
get_chat_analytics_response_metrics_and_timeseries_dict = get_chat_analytics_response_metrics_and_timeseries_instance.to_dict()
# create an instance of GetChatAnalyticsResponseMetricsAndTimeseries from a dict
get_chat_analytics_response_metrics_and_timeseries_from_dict = GetChatAnalyticsResponseMetricsAndTimeseries.from_dict(get_chat_analytics_response_metrics_and_timeseries_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


