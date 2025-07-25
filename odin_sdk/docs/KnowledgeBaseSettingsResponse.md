# KnowledgeBaseSettingsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**data** | [**KnowledgeBaseSettings**](KnowledgeBaseSettings.md) |  | [optional] 
**message** | **str** |  | 

## Example

```python
from odin_sdk.models.knowledge_base_settings_response import KnowledgeBaseSettingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeBaseSettingsResponse from a JSON string
knowledge_base_settings_response_instance = KnowledgeBaseSettingsResponse.from_json(json)
# print the JSON string representation of the object
print(KnowledgeBaseSettingsResponse.to_json())

# convert the object into a dict
knowledge_base_settings_response_dict = knowledge_base_settings_response_instance.to_dict()
# create an instance of KnowledgeBaseSettingsResponse from a dict
knowledge_base_settings_response_from_dict = KnowledgeBaseSettingsResponse.from_dict(knowledge_base_settings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


