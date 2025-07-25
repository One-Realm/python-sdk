# ActionStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The status of the action | 
**message** | **str** | Status message | 
**result** | **object** | The result of the action | 

## Example

```python
from odin_sdk.models.action_status_response import ActionStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ActionStatusResponse from a JSON string
action_status_response_instance = ActionStatusResponse.from_json(json)
# print the JSON string representation of the object
print(ActionStatusResponse.to_json())

# convert the object into a dict
action_status_response_dict = action_status_response_instance.to_dict()
# create an instance of ActionStatusResponse from a dict
action_status_response_from_dict = ActionStatusResponse.from_dict(action_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


