# RoutesChatActivateCustomAgentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | ID of the project in which to look for the chat. | 
**agent_id** | **str** | ID of the agent to activate. | 
**chat_id** | **str** | ID of the chat in which to activate the agent. | 

## Example

```python
from odin_sdk.models.routes_chat_activate_custom_agent_request import RoutesChatActivateCustomAgentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RoutesChatActivateCustomAgentRequest from a JSON string
routes_chat_activate_custom_agent_request_instance = RoutesChatActivateCustomAgentRequest.from_json(json)
# print the JSON string representation of the object
print(RoutesChatActivateCustomAgentRequest.to_json())

# convert the object into a dict
routes_chat_activate_custom_agent_request_dict = routes_chat_activate_custom_agent_request_instance.to_dict()
# create an instance of RoutesChatActivateCustomAgentRequest from a dict
routes_chat_activate_custom_agent_request_from_dict = RoutesChatActivateCustomAgentRequest.from_dict(routes_chat_activate_custom_agent_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


