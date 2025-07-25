# SaveActionResultOnMessageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**msg** | **str** | The message of the response. | 

## Example

```python
from odin_sdk.models.save_action_result_on_message_response import SaveActionResultOnMessageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SaveActionResultOnMessageResponse from a JSON string
save_action_result_on_message_response_instance = SaveActionResultOnMessageResponse.from_json(json)
# print the JSON string representation of the object
print(SaveActionResultOnMessageResponse.to_json())

# convert the object into a dict
save_action_result_on_message_response_dict = save_action_result_on_message_response_instance.to_dict()
# create an instance of SaveActionResultOnMessageResponse from a dict
save_action_result_on_message_response_from_dict = SaveActionResultOnMessageResponse.from_dict(save_action_result_on_message_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


