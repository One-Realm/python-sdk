# ExecutionDetailResponse

Response model for detailed execution information

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
**error_traceback** | **str** |  | 
**args** | **List[object]** |  | 
**kwargs** | **object** |  | 
**result** | [**AnyOf**](AnyOf.md) |  | 
**stdout** | **str** |  | 
**stderr** | **str** |  | 

## Example

```python
from odin_sdk.models.execution_detail_response import ExecutionDetailResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExecutionDetailResponse from a JSON string
execution_detail_response_instance = ExecutionDetailResponse.from_json(json)
# print the JSON string representation of the object
print(ExecutionDetailResponse.to_json())

# convert the object into a dict
execution_detail_response_dict = execution_detail_response_instance.to_dict()
# create an instance of ExecutionDetailResponse from a dict
execution_detail_response_from_dict = ExecutionDetailResponse.from_dict(execution_detail_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


