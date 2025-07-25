# DeactivateCustomAgentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Message describing the result of the operation. | 

## Example

```python
from odin_sdk.models.deactivate_custom_agent_response import DeactivateCustomAgentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeactivateCustomAgentResponse from a JSON string
deactivate_custom_agent_response_instance = DeactivateCustomAgentResponse.from_json(json)
# print the JSON string representation of the object
print(DeactivateCustomAgentResponse.to_json())

# convert the object into a dict
deactivate_custom_agent_response_dict = deactivate_custom_agent_response_instance.to_dict()
# create an instance of DeactivateCustomAgentResponse from a dict
deactivate_custom_agent_response_from_dict = DeactivateCustomAgentResponse.from_dict(deactivate_custom_agent_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


