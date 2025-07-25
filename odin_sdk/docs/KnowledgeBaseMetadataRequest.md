# KnowledgeBaseMetadataRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **object** |  | 

## Example

```python
from odin_sdk.models.knowledge_base_metadata_request import KnowledgeBaseMetadataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeBaseMetadataRequest from a JSON string
knowledge_base_metadata_request_instance = KnowledgeBaseMetadataRequest.from_json(json)
# print the JSON string representation of the object
print(KnowledgeBaseMetadataRequest.to_json())

# convert the object into a dict
knowledge_base_metadata_request_dict = knowledge_base_metadata_request_instance.to_dict()
# create an instance of KnowledgeBaseMetadataRequest from a dict
knowledge_base_metadata_request_from_dict = KnowledgeBaseMetadataRequest.from_dict(knowledge_base_metadata_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


