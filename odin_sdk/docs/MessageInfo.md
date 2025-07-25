# MessageInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**question** | **str** |  | 
**created_at** | **float** |  | 
**feedback_count** | **int** |  | 
**chat_id** | **str** |  | 
**message_id** | **str** |  | 

## Example

```python
from odin_sdk.models.message_info import MessageInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MessageInfo from a JSON string
message_info_instance = MessageInfo.from_json(json)
# print the JSON string representation of the object
print(MessageInfo.to_json())

# convert the object into a dict
message_info_dict = message_info_instance.to_dict()
# create an instance of MessageInfo from a dict
message_info_from_dict = MessageInfo.from_dict(message_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


