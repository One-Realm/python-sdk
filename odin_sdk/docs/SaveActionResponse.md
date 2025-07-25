# SaveActionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flow_id** | **str** | The ID of the flow saved. | 
**msg** | **str** | The message of the response. | 

## Example

```python
from odin_sdk.models.save_action_response import SaveActionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SaveActionResponse from a JSON string
save_action_response_instance = SaveActionResponse.from_json(json)
# print the JSON string representation of the object
print(SaveActionResponse.to_json())

# convert the object into a dict
save_action_response_dict = save_action_response_instance.to_dict()
# create an instance of SaveActionResponse from a dict
save_action_response_from_dict = SaveActionResponse.from_dict(save_action_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


