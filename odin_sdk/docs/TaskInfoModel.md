# TaskInfoModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** |  | 
**task_name** | **str** |  | 
**status** | **str** |  | 
**project_id** | **str** |  | [optional] 
**started_at** | **datetime** |  | [optional] 
**completed_at** | **datetime** |  | [optional] 
**duration_seconds** | **float** |  | [optional] 
**args** | **List[object]** |  | [optional] 
**kwargs** | **object** |  | [optional] 
**result** | [**AnyOf**](AnyOf.md) |  | [optional] 
**traceback** | **str** |  | [optional] 
**worker** | **str** |  | [optional] 
**retries** | **int** |  | [optional] 

## Example

```python
from odin_sdk.models.task_info_model import TaskInfoModel

# TODO update the JSON string below
json = "{}"
# create an instance of TaskInfoModel from a JSON string
task_info_model_instance = TaskInfoModel.from_json(json)
# print the JSON string representation of the object
print(TaskInfoModel.to_json())

# convert the object into a dict
task_info_model_dict = task_info_model_instance.to_dict()
# create an instance of TaskInfoModel from a dict
task_info_model_from_dict = TaskInfoModel.from_dict(task_info_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


