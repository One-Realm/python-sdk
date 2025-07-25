# DeleteChatResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 

## Example

```python
from odin_sdk.models.delete_chat_response import DeleteChatResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteChatResponse from a JSON string
delete_chat_response_instance = DeleteChatResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteChatResponse.to_json())

# convert the object into a dict
delete_chat_response_dict = delete_chat_response_instance.to_dict()
# create an instance of DeleteChatResponse from a dict
delete_chat_response_from_dict = DeleteChatResponse.from_dict(delete_chat_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


