# ClonePublicToolRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**public_tool_id** | **str** | ID of the public tool to clone | 
**target_project_id** | **str** | Project ID where the tool should be cloned | 
**new_name** | **str** |  | [optional] 

## Example

```python
from odin_sdk.models.clone_public_tool_request import ClonePublicToolRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ClonePublicToolRequest from a JSON string
clone_public_tool_request_instance = ClonePublicToolRequest.from_json(json)
# print the JSON string representation of the object
print(ClonePublicToolRequest.to_json())

# convert the object into a dict
clone_public_tool_request_dict = clone_public_tool_request_instance.to_dict()
# create an instance of ClonePublicToolRequest from a dict
clone_public_tool_request_from_dict = ClonePublicToolRequest.from_dict(clone_public_tool_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


