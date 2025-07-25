# KnowledgeBaseItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**upload_date** | **float** |  | [optional] 
**doc_type** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**metadata** | [**MetaData**](MetaData.md) |  | [optional] 

## Example

```python
from odin_sdk.models.knowledge_base_item import KnowledgeBaseItem

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeBaseItem from a JSON string
knowledge_base_item_instance = KnowledgeBaseItem.from_json(json)
# print the JSON string representation of the object
print(KnowledgeBaseItem.to_json())

# convert the object into a dict
knowledge_base_item_dict = knowledge_base_item_instance.to_dict()
# create an instance of KnowledgeBaseItem from a dict
knowledge_base_item_from_dict = KnowledgeBaseItem.from_dict(knowledge_base_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


