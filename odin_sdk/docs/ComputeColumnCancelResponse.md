# ComputeColumnCancelResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**execution_id** | **str** |  | 
**cancelled** | **bool** |  | 

## Example

```python
from odin_sdk.models.compute_column_cancel_response import ComputeColumnCancelResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ComputeColumnCancelResponse from a JSON string
compute_column_cancel_response_instance = ComputeColumnCancelResponse.from_json(json)
# print the JSON string representation of the object
print(ComputeColumnCancelResponse.to_json())

# convert the object into a dict
compute_column_cancel_response_dict = compute_column_cancel_response_instance.to_dict()
# create an instance of ComputeColumnCancelResponse from a dict
compute_column_cancel_response_from_dict = ComputeColumnCancelResponse.from_dict(compute_column_cancel_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


