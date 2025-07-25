# UpdateChatTestRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | 
**chat_id** | **str** |  | 
**messages** | **List[object]** |  | 

## Example

```python
from odin_sdk.models.update_chat_test_request import UpdateChatTestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateChatTestRequest from a JSON string
update_chat_test_request_instance = UpdateChatTestRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateChatTestRequest.to_json())

# convert the object into a dict
update_chat_test_request_dict = update_chat_test_request_instance.to_dict()
# create an instance of UpdateChatTestRequest from a dict
update_chat_test_request_from_dict = UpdateChatTestRequest.from_dict(update_chat_test_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


