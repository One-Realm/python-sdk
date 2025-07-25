# ToolStep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the step | 
**tool_id** | **str** | The tool ID for this step | 
**type** | **str** | The type of step (api, etc.) | 
**label** | **str** | Display label for the step | 
**description** | **str** | Description of what the step does | 
**settings** | **object** | Step settings | [optional] 

## Example

```python
from odin_sdk.models.tool_step import ToolStep

# TODO update the JSON string below
json = "{}"
# create an instance of ToolStep from a JSON string
tool_step_instance = ToolStep.from_json(json)
# print the JSON string representation of the object
print(ToolStep.to_json())

# convert the object into a dict
tool_step_dict = tool_step_instance.to_dict()
# create an instance of ToolStep from a dict
tool_step_from_dict = ToolStep.from_dict(tool_step_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


