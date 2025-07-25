# SaveVoiceMessageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | 
**chat_id** | **str** |  | 
**message** | **str** |  | 
**response** | **str** |  | [optional] 
**user_name** | **str** |  | 
**user_id** | **str** |  | 
**message_type** | **str** |  | 
**agent_id** | **str** |  | [optional] 
**agent_name** | **str** |  | [optional] 
**conversation_id** | **str** |  | [optional] 

## Example

```python
from odin_sdk.models.save_voice_message_request import SaveVoiceMessageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SaveVoiceMessageRequest from a JSON string
save_voice_message_request_instance = SaveVoiceMessageRequest.from_json(json)
# print the JSON string representation of the object
print(SaveVoiceMessageRequest.to_json())

# convert the object into a dict
save_voice_message_request_dict = save_voice_message_request_instance.to_dict()
# create an instance of SaveVoiceMessageRequest from a dict
save_voice_message_request_from_dict = SaveVoiceMessageRequest.from_dict(save_voice_message_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


