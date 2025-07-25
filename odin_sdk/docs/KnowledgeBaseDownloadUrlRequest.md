# KnowledgeBaseDownloadUrlRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | 
**url** | **str** |  | 
**path** | **str** |  | [optional] 
**doc_type** | **str** |  | [optional] 

## Example

```python
from odin_sdk.models.knowledge_base_download_url_request import KnowledgeBaseDownloadUrlRequest

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeBaseDownloadUrlRequest from a JSON string
knowledge_base_download_url_request_instance = KnowledgeBaseDownloadUrlRequest.from_json(json)
# print the JSON string representation of the object
print(KnowledgeBaseDownloadUrlRequest.to_json())

# convert the object into a dict
knowledge_base_download_url_request_dict = knowledge_base_download_url_request_instance.to_dict()
# create an instance of KnowledgeBaseDownloadUrlRequest from a dict
knowledge_base_download_url_request_from_dict = KnowledgeBaseDownloadUrlRequest.from_dict(knowledge_base_download_url_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


