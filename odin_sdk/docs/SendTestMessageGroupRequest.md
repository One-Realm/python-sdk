# SendTestMessageGroupRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | 
**system_prompt** | **object** |  | [optional] 
**test_chats** | [**List[TestChat]**](TestChat.md) |  | 

## Example

```python
from odin_sdk.models.send_test_message_group_request import SendTestMessageGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SendTestMessageGroupRequest from a JSON string
send_test_message_group_request_instance = SendTestMessageGroupRequest.from_json(json)
# print the JSON string representation of the object
print(SendTestMessageGroupRequest.to_json())

# convert the object into a dict
send_test_message_group_request_dict = send_test_message_group_request_instance.to_dict()
# create an instance of SendTestMessageGroupRequest from a dict
send_test_message_group_request_from_dict = SendTestMessageGroupRequest.from_dict(send_test_message_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


