# ChartMetricsResponse

Response model for chart metrics endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tool_usage_by_name** | [**List[ToolUsageChart]**](ToolUsageChart.md) |  | 
**tools_over_time** | **List[object]** |  | 
**success_rate_percentage** | **float** |  | 

## Example

```python
from odin_sdk.models.chart_metrics_response import ChartMetricsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChartMetricsResponse from a JSON string
chart_metrics_response_instance = ChartMetricsResponse.from_json(json)
# print the JSON string representation of the object
print(ChartMetricsResponse.to_json())

# convert the object into a dict
chart_metrics_response_dict = chart_metrics_response_instance.to_dict()
# create an instance of ChartMetricsResponse from a dict
chart_metrics_response_from_dict = ChartMetricsResponse.from_dict(chart_metrics_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


