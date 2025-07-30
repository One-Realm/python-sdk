# ComputeColumnRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column_name** | **str** | The name of the column to compute values for | 
**row_id** | **int** |  | [optional] 
**recompute** | **bool** | Whether to recompute all rows or only empty rows | [optional] [default to False]

## Example

```python
from odin_sdk.models.compute_column_request import ComputeColumnRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ComputeColumnRequest from a JSON string
compute_column_request_instance = ComputeColumnRequest.from_json(json)
# print the JSON string representation of the object
print(ComputeColumnRequest.to_json())

# convert the object into a dict
compute_column_request_dict = compute_column_request_instance.to_dict()
# create an instance of ComputeColumnRequest from a dict
compute_column_request_from_dict = ComputeColumnRequest.from_dict(compute_column_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


