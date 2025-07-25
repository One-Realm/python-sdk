# ExecutionHistoryItem

Model for execution history item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**code_script_id** | **int** |  | 
**version** | **str** |  | 
**execution_status** | **str** |  | 
**execution_time_ms** | **int** |  | 
**memory_used_mb** | **int** |  | 
**started_at** | **datetime** |  | 
**completed_at** | **datetime** |  | 
**error_message** | **str** |  | 
**error_type** | **str** |  | 

## Example

```python
from odin_sdk.models.execution_history_item import ExecutionHistoryItem

# TODO update the JSON string below
json = "{}"
# create an instance of ExecutionHistoryItem from a JSON string
execution_history_item_instance = ExecutionHistoryItem.from_json(json)
# print the JSON string representation of the object
print(ExecutionHistoryItem.to_json())

# convert the object into a dict
execution_history_item_dict = execution_history_item_instance.to_dict()
# create an instance of ExecutionHistoryItem from a dict
execution_history_item_from_dict = ExecutionHistoryItem.from_dict(execution_history_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


