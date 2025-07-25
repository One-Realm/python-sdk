# MoveKnowledgeItemRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | 
**source** | **str** |  | 
**destination_path** | **str** |  | 
**is_folder** | **bool** |  | [optional] [default to False]

## Example

```python
from odin_sdk.models.move_knowledge_item_request import MoveKnowledgeItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MoveKnowledgeItemRequest from a JSON string
move_knowledge_item_request_instance = MoveKnowledgeItemRequest.from_json(json)
# print the JSON string representation of the object
print(MoveKnowledgeItemRequest.to_json())

# convert the object into a dict
move_knowledge_item_request_dict = move_knowledge_item_request_instance.to_dict()
# create an instance of MoveKnowledgeItemRequest from a dict
move_knowledge_item_request_from_dict = MoveKnowledgeItemRequest.from_dict(move_knowledge_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


