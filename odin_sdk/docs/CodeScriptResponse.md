# CodeScriptResponse

Response model for code script

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**user_id** | **str** |  | 
**project_id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**script** | **str** |  | 
**runtime** | **str** |  | 
**entry_point** | **str** |  | 
**dependencies** | **List[str]** |  | 
**custom_resource_settings** | **object** |  | 
**is_published** | **bool** |  | 
**version** | **str** |  | 
**published_at** | **datetime** |  | 

## Example

```python
from odin_sdk.models.code_script_response import CodeScriptResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CodeScriptResponse from a JSON string
code_script_response_instance = CodeScriptResponse.from_json(json)
# print the JSON string representation of the object
print(CodeScriptResponse.to_json())

# convert the object into a dict
code_script_response_dict = code_script_response_instance.to_dict()
# create an instance of CodeScriptResponse from a dict
code_script_response_from_dict = CodeScriptResponse.from_dict(code_script_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


