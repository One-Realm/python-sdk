# CloneExistingCustomAgentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | ID of the project in which to create the agent. | 
**agent_id** | **str** | ID of the agent to clone. | 
**agent_name** | **str** |  | [optional] 

## Example

```python
from odin_sdk.models.clone_existing_custom_agent_request import CloneExistingCustomAgentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CloneExistingCustomAgentRequest from a JSON string
clone_existing_custom_agent_request_instance = CloneExistingCustomAgentRequest.from_json(json)
# print the JSON string representation of the object
print(CloneExistingCustomAgentRequest.to_json())

# convert the object into a dict
clone_existing_custom_agent_request_dict = clone_existing_custom_agent_request_instance.to_dict()
# create an instance of CloneExistingCustomAgentRequest from a dict
clone_existing_custom_agent_request_from_dict = CloneExistingCustomAgentRequest.from_dict(clone_existing_custom_agent_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


