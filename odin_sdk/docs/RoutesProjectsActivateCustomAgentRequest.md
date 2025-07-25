# RoutesProjectsActivateCustomAgentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | ID of the project in which to activate the agent. | 
**agent_id** | **str** | ID of the agent to activate. | 

## Example

```python
from odin_sdk.models.routes_projects_activate_custom_agent_request import RoutesProjectsActivateCustomAgentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RoutesProjectsActivateCustomAgentRequest from a JSON string
routes_projects_activate_custom_agent_request_instance = RoutesProjectsActivateCustomAgentRequest.from_json(json)
# print the JSON string representation of the object
print(RoutesProjectsActivateCustomAgentRequest.to_json())

# convert the object into a dict
routes_projects_activate_custom_agent_request_dict = routes_projects_activate_custom_agent_request_instance.to_dict()
# create an instance of RoutesProjectsActivateCustomAgentRequest from a dict
routes_projects_activate_custom_agent_request_from_dict = RoutesProjectsActivateCustomAgentRequest.from_dict(routes_projects_activate_custom_agent_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


