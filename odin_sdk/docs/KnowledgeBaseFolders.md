# KnowledgeBaseFolders


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**path** | **str** |  | 
**size** | **int** |  | 
**type** | **str** |  | 
**id** | **str** |  | 
**last_updated** | **datetime** |  | 
**external_link_info** | [**FolderExternalLinkInfo**](FolderExternalLinkInfo.md) |  | [optional] 

## Example

```python
from odin_sdk.models.knowledge_base_folders import KnowledgeBaseFolders

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeBaseFolders from a JSON string
knowledge_base_folders_instance = KnowledgeBaseFolders.from_json(json)
# print the JSON string representation of the object
print(KnowledgeBaseFolders.to_json())

# convert the object into a dict
knowledge_base_folders_dict = knowledge_base_folders_instance.to_dict()
# create an instance of KnowledgeBaseFolders from a dict
knowledge_base_folders_from_dict = KnowledgeBaseFolders.from_dict(knowledge_base_folders_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


