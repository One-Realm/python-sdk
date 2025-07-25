# EditExistingCustomAgentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Whether the agent was saved successfully. | 
**msg** | **str** | Message describing the result of the operation. | 
**agent_id** | **str** | ID of the agent that was saved. | 

## Example

```python
from odin_sdk.models.edit_existing_custom_agent_response import EditExistingCustomAgentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EditExistingCustomAgentResponse from a JSON string
edit_existing_custom_agent_response_instance = EditExistingCustomAgentResponse.from_json(json)
# print the JSON string representation of the object
print(EditExistingCustomAgentResponse.to_json())

# convert the object into a dict
edit_existing_custom_agent_response_dict = edit_existing_custom_agent_response_instance.to_dict()
# create an instance of EditExistingCustomAgentResponse from a dict
edit_existing_custom_agent_response_from_dict = EditExistingCustomAgentResponse.from_dict(edit_existing_custom_agent_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


