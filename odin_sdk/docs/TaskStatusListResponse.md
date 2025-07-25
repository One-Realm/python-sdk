# TaskStatusListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tasks** | [**List[TaskStatusResponse]**](TaskStatusResponse.md) |  | 

## Example

```python
from odin_sdk.models.task_status_list_response import TaskStatusListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TaskStatusListResponse from a JSON string
task_status_list_response_instance = TaskStatusListResponse.from_json(json)
# print the JSON string representation of the object
print(TaskStatusListResponse.to_json())

# convert the object into a dict
task_status_list_response_dict = task_status_list_response_instance.to_dict()
# create an instance of TaskStatusListResponse from a dict
task_status_list_response_from_dict = TaskStatusListResponse.from_dict(task_status_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


