# ScriptAnalyticsResponse

Response model for script analytics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**script_id** | **int** |  | 
**script_name** | **str** |  | 
**runtime** | **str** |  | 
**total_executions** | **int** |  | 
**successful_executions** | **int** |  | 
**failed_executions** | **int** |  | 
**timeout_executions** | **int** |  | 
**success_rate** | **float** |  | 
**avg_success_time_ms** | **float** |  | 
**min_success_time_ms** | **int** |  | 
**max_success_time_ms** | **int** |  | 
**avg_memory_used_mb** | **float** |  | 
**last_executed_at** | **datetime** |  | 
**first_executed_at** | **datetime** |  | 

## Example

```python
from odin_sdk.models.script_analytics_response import ScriptAnalyticsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ScriptAnalyticsResponse from a JSON string
script_analytics_response_instance = ScriptAnalyticsResponse.from_json(json)
# print the JSON string representation of the object
print(ScriptAnalyticsResponse.to_json())

# convert the object into a dict
script_analytics_response_dict = script_analytics_response_instance.to_dict()
# create an instance of ScriptAnalyticsResponse from a dict
script_analytics_response_from_dict = ScriptAnalyticsResponse.from_dict(script_analytics_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


