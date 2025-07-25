# ComputeColumnResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**updated_rows** | **int** |  | 

## Example

```python
from odin_sdk.models.compute_column_response import ComputeColumnResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ComputeColumnResponse from a JSON string
compute_column_response_instance = ComputeColumnResponse.from_json(json)
# print the JSON string representation of the object
print(ComputeColumnResponse.to_json())

# convert the object into a dict
compute_column_response_dict = compute_column_response_instance.to_dict()
# create an instance of ComputeColumnResponse from a dict
compute_column_response_from_dict = ComputeColumnResponse.from_dict(compute_column_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


