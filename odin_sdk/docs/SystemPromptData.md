# SystemPromptData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**instructions** | **str** |  | 
**type** | **str** |  | 
**name** | **str** |  | 
**temperature** | **float** |  | 

## Example

```python
from odin_sdk.models.system_prompt_data import SystemPromptData

# TODO update the JSON string below
json = "{}"
# create an instance of SystemPromptData from a JSON string
system_prompt_data_instance = SystemPromptData.from_json(json)
# print the JSON string representation of the object
print(SystemPromptData.to_json())

# convert the object into a dict
system_prompt_data_dict = system_prompt_data_instance.to_dict()
# create an instance of SystemPromptData from a dict
system_prompt_data_from_dict = SystemPromptData.from_dict(system_prompt_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


