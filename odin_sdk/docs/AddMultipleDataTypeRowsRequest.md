# AddMultipleDataTypeRowsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rows** | **List[object]** | List of row metadata to add | 

## Example

```python
from odin_sdk.models.add_multiple_data_type_rows_request import AddMultipleDataTypeRowsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddMultipleDataTypeRowsRequest from a JSON string
add_multiple_data_type_rows_request_instance = AddMultipleDataTypeRowsRequest.from_json(json)
# print the JSON string representation of the object
print(AddMultipleDataTypeRowsRequest.to_json())

# convert the object into a dict
add_multiple_data_type_rows_request_dict = add_multiple_data_type_rows_request_instance.to_dict()
# create an instance of AddMultipleDataTypeRowsRequest from a dict
add_multiple_data_type_rows_request_from_dict = AddMultipleDataTypeRowsRequest.from_dict(add_multiple_data_type_rows_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


