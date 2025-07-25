# WorkerInfoModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostname** | **str** |  | 
**status** | **str** |  | 
**active_tasks** | **int** |  | [optional] [default to 0]
**scheduled_tasks** | **int** |  | [optional] [default to 0]
**reserved_tasks** | **int** |  | [optional] [default to 0]
**processed** | **int** |  | [optional] 
**stats** | **object** |  | [optional] 

## Example

```python
from odin_sdk.models.worker_info_model import WorkerInfoModel

# TODO update the JSON string below
json = "{}"
# create an instance of WorkerInfoModel from a JSON string
worker_info_model_instance = WorkerInfoModel.from_json(json)
# print the JSON string representation of the object
print(WorkerInfoModel.to_json())

# convert the object into a dict
worker_info_model_dict = worker_info_model_instance.to_dict()
# create an instance of WorkerInfoModel from a dict
worker_info_model_from_dict = WorkerInfoModel.from_dict(worker_info_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


