# CodeScriptListResponse

Response model for listing code scripts

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scripts** | [**List[CodeScriptResponse]**](CodeScriptResponse.md) |  | 
**total** | **int** |  | 

## Example

```python
from odin_sdk.models.code_script_list_response import CodeScriptListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CodeScriptListResponse from a JSON string
code_script_list_response_instance = CodeScriptListResponse.from_json(json)
# print the JSON string representation of the object
print(CodeScriptListResponse.to_json())

# convert the object into a dict
code_script_list_response_dict = code_script_list_response_instance.to_dict()
# create an instance of CodeScriptListResponse from a dict
code_script_list_response_from_dict = CodeScriptListResponse.from_dict(code_script_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


