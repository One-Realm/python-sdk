# TaskStatsModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_name** | **str** |  | 
**total_executions** | **int** |  | 
**successful_executions** | **int** |  | 
**failed_executions** | **int** |  | 
**terminated_executions** | **int** |  | [optional] [default to 0]
**avg_duration** | **float** |  | [optional] 
**median_duration** | **float** |  | [optional] 
**min_duration** | **float** |  | [optional] 
**max_duration** | **float** |  | [optional] 

## Example

```python
from odin_sdk.models.task_stats_model import TaskStatsModel

# TODO update the JSON string below
json = "{}"
# create an instance of TaskStatsModel from a JSON string
task_stats_model_instance = TaskStatsModel.from_json(json)
# print the JSON string representation of the object
print(TaskStatsModel.to_json())

# convert the object into a dict
task_stats_model_dict = task_stats_model_instance.to_dict()
# create an instance of TaskStatsModel from a dict
task_stats_model_from_dict = TaskStatsModel.from_dict(task_stats_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


