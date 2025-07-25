# GetKnowledgeBaseResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**knowledge_base** | [**Dict[str, KnowledgeBaseItem]**](KnowledgeBaseItem.md) |  | 

## Example

```python
from odin_sdk.models.get_knowledge_base_response import GetKnowledgeBaseResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetKnowledgeBaseResponse from a JSON string
get_knowledge_base_response_instance = GetKnowledgeBaseResponse.from_json(json)
# print the JSON string representation of the object
print(GetKnowledgeBaseResponse.to_json())

# convert the object into a dict
get_knowledge_base_response_dict = get_knowledge_base_response_instance.to_dict()
# create an instance of GetKnowledgeBaseResponse from a dict
get_knowledge_base_response_from_dict = GetKnowledgeBaseResponse.from_dict(get_knowledge_base_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


