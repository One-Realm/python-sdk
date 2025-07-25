# ComputeRowColumnsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column_names** | **List[str]** |  | [optional] 

## Example

```python
from odin_sdk.models.compute_row_columns_request import ComputeRowColumnsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ComputeRowColumnsRequest from a JSON string
compute_row_columns_request_instance = ComputeRowColumnsRequest.from_json(json)
# print the JSON string representation of the object
print(ComputeRowColumnsRequest.to_json())

# convert the object into a dict
compute_row_columns_request_dict = compute_row_columns_request_instance.to_dict()
# create an instance of ComputeRowColumnsRequest from a dict
compute_row_columns_request_from_dict = ComputeRowColumnsRequest.from_dict(compute_row_columns_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


