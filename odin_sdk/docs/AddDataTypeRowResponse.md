# AddDataTypeRowResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**row_id** | **int** |  | 
**row** | **object** |  | 

## Example

```python
from odin_sdk.models.add_data_type_row_response import AddDataTypeRowResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddDataTypeRowResponse from a JSON string
add_data_type_row_response_instance = AddDataTypeRowResponse.from_json(json)
# print the JSON string representation of the object
print(AddDataTypeRowResponse.to_json())

# convert the object into a dict
add_data_type_row_response_dict = add_data_type_row_response_instance.to_dict()
# create an instance of AddDataTypeRowResponse from a dict
add_data_type_row_response_from_dict = AddDataTypeRowResponse.from_dict(add_data_type_row_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


