# SaveNewCustomAgentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Whether the agent was saved successfully. | 
**msg** | **str** | Message describing the result of the operation. | 
**agent_id** | **str** | ID of the agent that was saved. | 

## Example

```python
from odin_sdk.models.save_new_custom_agent_response import SaveNewCustomAgentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SaveNewCustomAgentResponse from a JSON string
save_new_custom_agent_response_instance = SaveNewCustomAgentResponse.from_json(json)
# print the JSON string representation of the object
print(SaveNewCustomAgentResponse.to_json())

# convert the object into a dict
save_new_custom_agent_response_dict = save_new_custom_agent_response_instance.to_dict()
# create an instance of SaveNewCustomAgentResponse from a dict
save_new_custom_agent_response_from_dict = SaveNewCustomAgentResponse.from_dict(save_new_custom_agent_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


