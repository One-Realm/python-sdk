# AddMultipleDataTypeRowsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**rows_added** | **int** |  | 
**row_ids** | **List[int]** |  | 

## Example

```python
from odin_sdk.models.add_multiple_data_type_rows_response import AddMultipleDataTypeRowsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddMultipleDataTypeRowsResponse from a JSON string
add_multiple_data_type_rows_response_instance = AddMultipleDataTypeRowsResponse.from_json(json)
# print the JSON string representation of the object
print(AddMultipleDataTypeRowsResponse.to_json())

# convert the object into a dict
add_multiple_data_type_rows_response_dict = add_multiple_data_type_rows_response_instance.to_dict()
# create an instance of AddMultipleDataTypeRowsResponse from a dict
add_multiple_data_type_rows_response_from_dict = AddMultipleDataTypeRowsResponse.from_dict(add_multiple_data_type_rows_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


