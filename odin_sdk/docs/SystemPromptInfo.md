# SystemPromptInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**instructions** | **str** |  | 
**temperature** | **float** |  | 
**type** | **str** |  | 
**id** | **str** |  | 

## Example

```python
from odin_sdk.models.system_prompt_info import SystemPromptInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SystemPromptInfo from a JSON string
system_prompt_info_instance = SystemPromptInfo.from_json(json)
# print the JSON string representation of the object
print(SystemPromptInfo.to_json())

# convert the object into a dict
system_prompt_info_dict = system_prompt_info_instance.to_dict()
# create an instance of SystemPromptInfo from a dict
system_prompt_info_from_dict = SystemPromptInfo.from_dict(system_prompt_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


