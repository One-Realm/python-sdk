# RenameDataTypeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_title** | **str** | The new title for the data type | 

## Example

```python
from odin_sdk.models.rename_data_type_request import RenameDataTypeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RenameDataTypeRequest from a JSON string
rename_data_type_request_instance = RenameDataTypeRequest.from_json(json)
# print the JSON string representation of the object
print(RenameDataTypeRequest.to_json())

# convert the object into a dict
rename_data_type_request_dict = rename_data_type_request_instance.to_dict()
# create an instance of RenameDataTypeRequest from a dict
rename_data_type_request_from_dict = RenameDataTypeRequest.from_dict(rename_data_type_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


