# DeleteChatBulkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | 
**start_timestamp** | **float** |  | [optional] 
**end_timestamp** | **float** |  | [optional] 
**chat_ids** | **List[object]** |  | [optional] 

## Example

```python
from odin_sdk.models.delete_chat_bulk_request import DeleteChatBulkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteChatBulkRequest from a JSON string
delete_chat_bulk_request_instance = DeleteChatBulkRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteChatBulkRequest.to_json())

# convert the object into a dict
delete_chat_bulk_request_dict = delete_chat_bulk_request_instance.to_dict()
# create an instance of DeleteChatBulkRequest from a dict
delete_chat_bulk_request_from_dict = DeleteChatBulkRequest.from_dict(delete_chat_bulk_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


