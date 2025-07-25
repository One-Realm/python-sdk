# CustomToolResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the custom tool | 
**name** | **str** | Name of the custom tool | 
**description** | **str** |  | [optional] 
**inputs** | [**Dict[str, ToolInput]**](ToolInput.md) | Tool inputs configuration | 
**steps** | [**Dict[str, ToolStep]**](ToolStep.md) | Tool steps configuration | 
**test_step_results** | **object** | Test step execution results | [optional] 
**project_id** | **str** | Project ID this tool belongs to | 
**created_by** | **str** | User ID who created this tool | 
**created_at** | **str** | Creation timestamp | 
**updated_at** | **str** | Last update timestamp | 
**is_published** | **bool** | Whether this tool is published | 
**version** | **str** |  | [optional] 
**published_at** | **str** |  | [optional] 
**is_draft** | **bool** | Whether this tool has unsaved draft changes | 
**is_public** | **bool** | Whether this tool is publicly available to all users | 

## Example

```python
from odin_sdk.models.custom_tool_response import CustomToolResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomToolResponse from a JSON string
custom_tool_response_instance = CustomToolResponse.from_json(json)
# print the JSON string representation of the object
print(CustomToolResponse.to_json())

# convert the object into a dict
custom_tool_response_dict = custom_tool_response_instance.to_dict()
# create an instance of CustomToolResponse from a dict
custom_tool_response_from_dict = CustomToolResponse.from_dict(custom_tool_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


