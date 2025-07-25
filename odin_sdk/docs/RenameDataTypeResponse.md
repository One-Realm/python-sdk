# RenameDataTypeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**data_type_id** | **str** |  | 
**new_title** | **str** |  | 

## Example

```python
from odin_sdk.models.rename_data_type_response import RenameDataTypeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RenameDataTypeResponse from a JSON string
rename_data_type_response_instance = RenameDataTypeResponse.from_json(json)
# print the JSON string representation of the object
print(RenameDataTypeResponse.to_json())

# convert the object into a dict
rename_data_type_response_dict = rename_data_type_response_instance.to_dict()
# create an instance of RenameDataTypeResponse from a dict
rename_data_type_response_from_dict = RenameDataTypeResponse.from_dict(rename_data_type_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


