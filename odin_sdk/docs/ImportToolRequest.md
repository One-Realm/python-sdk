# ImportToolRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tool_data** | **object** | The tool data to import | 
**project_id** | **str** | Target project ID for the imported tool | 
**new_name** | **str** |  | [optional] 
**import_as_draft** | **bool** | Whether to import as draft (default) or publish immediately | [optional] [default to True]

## Example

```python
from odin_sdk.models.import_tool_request import ImportToolRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ImportToolRequest from a JSON string
import_tool_request_instance = ImportToolRequest.from_json(json)
# print the JSON string representation of the object
print(ImportToolRequest.to_json())

# convert the object into a dict
import_tool_request_dict = import_tool_request_instance.to_dict()
# create an instance of ImportToolRequest from a dict
import_tool_request_from_dict = ImportToolRequest.from_dict(import_tool_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


