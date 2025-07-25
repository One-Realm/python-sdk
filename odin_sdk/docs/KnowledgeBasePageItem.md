# KnowledgeBasePageItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**content_key** | **str** |  | [optional] 
**upload_date** | **float** |  | [optional] 
**doc_type** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**document_id** | **str** |  | [optional] 
**metadata** | **object** |  | [optional] 

## Example

```python
from odin_sdk.models.knowledge_base_page_item import KnowledgeBasePageItem

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeBasePageItem from a JSON string
knowledge_base_page_item_instance = KnowledgeBasePageItem.from_json(json)
# print the JSON string representation of the object
print(KnowledgeBasePageItem.to_json())

# convert the object into a dict
knowledge_base_page_item_dict = knowledge_base_page_item_instance.to_dict()
# create an instance of KnowledgeBasePageItem from a dict
knowledge_base_page_item_from_dict = KnowledgeBasePageItem.from_dict(knowledge_base_page_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


