# KnowledgeBaseCustomMetadataRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_metadata** | **object** |  | 

## Example

```python
from odin_sdk.models.knowledge_base_custom_metadata_request import KnowledgeBaseCustomMetadataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeBaseCustomMetadataRequest from a JSON string
knowledge_base_custom_metadata_request_instance = KnowledgeBaseCustomMetadataRequest.from_json(json)
# print the JSON string representation of the object
print(KnowledgeBaseCustomMetadataRequest.to_json())

# convert the object into a dict
knowledge_base_custom_metadata_request_dict = knowledge_base_custom_metadata_request_instance.to_dict()
# create an instance of KnowledgeBaseCustomMetadataRequest from a dict
knowledge_base_custom_metadata_request_from_dict = KnowledgeBaseCustomMetadataRequest.from_dict(knowledge_base_custom_metadata_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


