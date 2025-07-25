# ExportToolRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_metadata** | **bool** | Whether to include metadata like IDs, timestamps, etc. | [optional] [default to True]

## Example

```python
from odin_sdk.models.export_tool_request import ExportToolRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExportToolRequest from a JSON string
export_tool_request_instance = ExportToolRequest.from_json(json)
# print the JSON string representation of the object
print(ExportToolRequest.to_json())

# convert the object into a dict
export_tool_request_dict = export_tool_request_instance.to_dict()
# create an instance of ExportToolRequest from a dict
export_tool_request_from_dict = ExportToolRequest.from_dict(export_tool_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


