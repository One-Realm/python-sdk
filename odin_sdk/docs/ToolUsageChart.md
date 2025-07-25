# ToolUsageChart

Model for tool usage chart data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tool_name** | **str** |  | 
**total_calls** | **int** |  | 
**successful_calls** | **int** |  | 
**failure_calls** | **int** |  | 

## Example

```python
from odin_sdk.models.tool_usage_chart import ToolUsageChart

# TODO update the JSON string below
json = "{}"
# create an instance of ToolUsageChart from a JSON string
tool_usage_chart_instance = ToolUsageChart.from_json(json)
# print the JSON string representation of the object
print(ToolUsageChart.to_json())

# convert the object into a dict
tool_usage_chart_dict = tool_usage_chart_instance.to_dict()
# create an instance of ToolUsageChart from a dict
tool_usage_chart_from_dict = ToolUsageChart.from_dict(tool_usage_chart_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


