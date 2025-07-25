# ExportDataTypeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**data_type_config** | **object** |  | 
**export_version** | **str** |  | [optional] [default to '1.0']

## Example

```python
from odin_sdk.models.export_data_type_response import ExportDataTypeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExportDataTypeResponse from a JSON string
export_data_type_response_instance = ExportDataTypeResponse.from_json(json)
# print the JSON string representation of the object
print(ExportDataTypeResponse.to_json())

# convert the object into a dict
export_data_type_response_dict = export_data_type_response_instance.to_dict()
# create an instance of ExportDataTypeResponse from a dict
export_data_type_response_from_dict = ExportDataTypeResponse.from_dict(export_data_type_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


