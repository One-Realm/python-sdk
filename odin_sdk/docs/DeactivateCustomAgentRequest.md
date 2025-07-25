# DeactivateCustomAgentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | ID of the project in which to deactivate the agent. | 

## Example

```python
from odin_sdk.models.deactivate_custom_agent_request import DeactivateCustomAgentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeactivateCustomAgentRequest from a JSON string
deactivate_custom_agent_request_instance = DeactivateCustomAgentRequest.from_json(json)
# print the JSON string representation of the object
print(DeactivateCustomAgentRequest.to_json())

# convert the object into a dict
deactivate_custom_agent_request_dict = deactivate_custom_agent_request_instance.to_dict()
# create an instance of DeactivateCustomAgentRequest from a dict
deactivate_custom_agent_request_from_dict = DeactivateCustomAgentRequest.from_dict(deactivate_custom_agent_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


