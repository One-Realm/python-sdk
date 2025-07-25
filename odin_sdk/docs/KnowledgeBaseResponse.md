# KnowledgeBaseResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**content** | **str** |  | [optional] 

## Example

```python
from odin_sdk.models.knowledge_base_response import KnowledgeBaseResponse

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeBaseResponse from a JSON string
knowledge_base_response_instance = KnowledgeBaseResponse.from_json(json)
# print the JSON string representation of the object
print(KnowledgeBaseResponse.to_json())

# convert the object into a dict
knowledge_base_response_dict = knowledge_base_response_instance.to_dict()
# create an instance of KnowledgeBaseResponse from a dict
knowledge_base_response_from_dict = KnowledgeBaseResponse.from_dict(knowledge_base_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


