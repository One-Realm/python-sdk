# CodeScriptUpdate

Request model for updating a code script

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**script** | **str** |  | [optional] 
**runtime** | **str** |  | [optional] 
**entry_point** | **str** |  | [optional] 
**dependencies** | **List[str]** |  | [optional] 
**custom_resource_settings** | **object** |  | [optional] 

## Example

```python
from odin_sdk.models.code_script_update import CodeScriptUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of CodeScriptUpdate from a JSON string
code_script_update_instance = CodeScriptUpdate.from_json(json)
# print the JSON string representation of the object
print(CodeScriptUpdate.to_json())

# convert the object into a dict
code_script_update_dict = code_script_update_instance.to_dict()
# create an instance of CodeScriptUpdate from a dict
code_script_update_from_dict = CodeScriptUpdate.from_dict(code_script_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


