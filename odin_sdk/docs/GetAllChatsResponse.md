# GetAllChatsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chats** | [**List[ChatDetails]**](ChatDetails.md) |  | 

## Example

```python
from odin_sdk.models.get_all_chats_response import GetAllChatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllChatsResponse from a JSON string
get_all_chats_response_instance = GetAllChatsResponse.from_json(json)
# print the JSON string representation of the object
print(GetAllChatsResponse.to_json())

# convert the object into a dict
get_all_chats_response_dict = get_all_chats_response_instance.to_dict()
# create an instance of GetAllChatsResponse from a dict
get_all_chats_response_from_dict = GetAllChatsResponse.from_dict(get_all_chats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


