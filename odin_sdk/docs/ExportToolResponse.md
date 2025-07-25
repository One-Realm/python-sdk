# ExportToolResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tool_data** | **object** | The exported tool data as JSON | 
**export_metadata** | **object** | Export metadata including version, timestamp, etc. | 

## Example

```python
from odin_sdk.models.export_tool_response import ExportToolResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExportToolResponse from a JSON string
export_tool_response_instance = ExportToolResponse.from_json(json)
# print the JSON string representation of the object
print(ExportToolResponse.to_json())

# convert the object into a dict
export_tool_response_dict = export_tool_response_instance.to_dict()
# create an instance of ExportToolResponse from a dict
export_tool_response_from_dict = ExportToolResponse.from_dict(export_tool_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


