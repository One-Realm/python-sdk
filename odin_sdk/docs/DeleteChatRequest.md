# DeleteChatRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | 
**chat_id** | **str** |  | 
**test_group_id** | **str** |  | [optional] 
**is_test** | **bool** |  | [optional] 

## Example

```python
from odin_sdk.models.delete_chat_request import DeleteChatRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteChatRequest from a JSON string
delete_chat_request_instance = DeleteChatRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteChatRequest.to_json())

# convert the object into a dict
delete_chat_request_dict = delete_chat_request_instance.to_dict()
# create an instance of DeleteChatRequest from a dict
delete_chat_request_from_dict = DeleteChatRequest.from_dict(delete_chat_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


