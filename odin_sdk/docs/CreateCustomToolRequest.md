# CreateCustomToolRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the custom tool | 
**description** | **str** |  | [optional] 
**inputs** | [**Dict[str, ToolInput]**](ToolInput.md) | Tool inputs configuration | [optional] 
**steps** | [**Dict[str, ToolStep]**](ToolStep.md) | Tool steps configuration | [optional] 
**project_id** | **str** | Project ID this tool belongs to | 

## Example

```python
from odin_sdk.models.create_custom_tool_request import CreateCustomToolRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCustomToolRequest from a JSON string
create_custom_tool_request_instance = CreateCustomToolRequest.from_json(json)
# print the JSON string representation of the object
print(CreateCustomToolRequest.to_json())

# convert the object into a dict
create_custom_tool_request_dict = create_custom_tool_request_instance.to_dict()
# create an instance of CreateCustomToolRequest from a dict
create_custom_tool_request_from_dict = CreateCustomToolRequest.from_dict(create_custom_tool_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


