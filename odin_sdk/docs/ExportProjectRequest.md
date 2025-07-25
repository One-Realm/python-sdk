# ExportProjectRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | 
**include_files** | **bool** |  | [optional] 
**export_name** | **str** |  | [optional] 

## Example

```python
from odin_sdk.models.export_project_request import ExportProjectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExportProjectRequest from a JSON string
export_project_request_instance = ExportProjectRequest.from_json(json)
# print the JSON string representation of the object
print(ExportProjectRequest.to_json())

# convert the object into a dict
export_project_request_dict = export_project_request_instance.to_dict()
# create an instance of ExportProjectRequest from a dict
export_project_request_from_dict = ExportProjectRequest.from_dict(export_project_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


