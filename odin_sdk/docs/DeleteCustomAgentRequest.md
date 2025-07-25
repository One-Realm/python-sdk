# DeleteCustomAgentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | ID of the project in which to delete the agent. | 
**agent_id** | **str** | ID of the agent to delete. | 

## Example

```python
from odin_sdk.models.delete_custom_agent_request import DeleteCustomAgentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteCustomAgentRequest from a JSON string
delete_custom_agent_request_instance = DeleteCustomAgentRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteCustomAgentRequest.to_json())

# convert the object into a dict
delete_custom_agent_request_dict = delete_custom_agent_request_instance.to_dict()
# create an instance of DeleteCustomAgentRequest from a dict
delete_custom_agent_request_from_dict = DeleteCustomAgentRequest.from_dict(delete_custom_agent_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


