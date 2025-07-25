# ActivateCustomAgentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Message describing the result of the operation. | 

## Example

```python
from odin_sdk.models.activate_custom_agent_response import ActivateCustomAgentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ActivateCustomAgentResponse from a JSON string
activate_custom_agent_response_instance = ActivateCustomAgentResponse.from_json(json)
# print the JSON string representation of the object
print(ActivateCustomAgentResponse.to_json())

# convert the object into a dict
activate_custom_agent_response_dict = activate_custom_agent_response_instance.to_dict()
# create an instance of ActivateCustomAgentResponse from a dict
activate_custom_agent_response_from_dict = ActivateCustomAgentResponse.from_dict(activate_custom_agent_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


