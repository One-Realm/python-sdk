# TaskStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** |  | 
**status** | **str** |  | 
**task_type** | **str** |  | 
**project_id** | **str** |  | 
**created_at** | **float** |  | 
**updated_at** | **float** |  | 

## Example

```python
from odin_sdk.models.task_status_response import TaskStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TaskStatusResponse from a JSON string
task_status_response_instance = TaskStatusResponse.from_json(json)
# print the JSON string representation of the object
print(TaskStatusResponse.to_json())

# convert the object into a dict
task_status_response_dict = task_status_response_instance.to_dict()
# create an instance of TaskStatusResponse from a dict
task_status_response_from_dict = TaskStatusResponse.from_dict(task_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


