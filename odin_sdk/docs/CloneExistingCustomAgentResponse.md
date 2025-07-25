# CloneExistingCustomAgentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Whether the agent was saved successfully. | 
**msg** | **str** | Message describing the result of the operation. | 

## Example

```python
from odin_sdk.models.clone_existing_custom_agent_response import CloneExistingCustomAgentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CloneExistingCustomAgentResponse from a JSON string
clone_existing_custom_agent_response_instance = CloneExistingCustomAgentResponse.from_json(json)
# print the JSON string representation of the object
print(CloneExistingCustomAgentResponse.to_json())

# convert the object into a dict
clone_existing_custom_agent_response_dict = clone_existing_custom_agent_response_instance.to_dict()
# create an instance of CloneExistingCustomAgentResponse from a dict
clone_existing_custom_agent_response_from_dict = CloneExistingCustomAgentResponse.from_dict(clone_existing_custom_agent_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


