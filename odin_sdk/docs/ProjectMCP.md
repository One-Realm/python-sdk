# ProjectMCP


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**project_id** | **str** |  | 
**mcp_ref_id** | **str** |  | 
**service_name** | **str** |  | 
**service_configuration** | **object** |  | 
**platform** | **str** |  | 
**enabled** | **bool** |  | 
**created_timestamp** | **float** |  | 
**last_modified_timestamp** | **float** |  | 

## Example

```python
from odin_sdk.models.project_mcp import ProjectMCP

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectMCP from a JSON string
project_mcp_instance = ProjectMCP.from_json(json)
# print the JSON string representation of the object
print(ProjectMCP.to_json())

# convert the object into a dict
project_mcp_dict = project_mcp_instance.to_dict()
# create an instance of ProjectMCP from a dict
project_mcp_from_dict = ProjectMCP.from_dict(project_mcp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


