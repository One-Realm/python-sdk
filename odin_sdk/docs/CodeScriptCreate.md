# CodeScriptCreate

Request model for creating a new code script (draft)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Script name | 
**description** | **str** |  | [optional] 
**project_id** | **str** | Project ID | 
**script** | **str** | Script code | 
**runtime** | **str** | Runtime version | 
**entry_point** | **str** | Entry point function name | [optional] [default to 'main']
**dependencies** | **List[str]** | List of package dependencies | [optional] [default to []]
**custom_resource_settings** | **object** |  | [optional] 

## Example

```python
from odin_sdk.models.code_script_create import CodeScriptCreate

# TODO update the JSON string below
json = "{}"
# create an instance of CodeScriptCreate from a JSON string
code_script_create_instance = CodeScriptCreate.from_json(json)
# print the JSON string representation of the object
print(CodeScriptCreate.to_json())

# convert the object into a dict
code_script_create_dict = code_script_create_instance.to_dict()
# create an instance of CodeScriptCreate from a dict
code_script_create_from_dict = CodeScriptCreate.from_dict(code_script_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


