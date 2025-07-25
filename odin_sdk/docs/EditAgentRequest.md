# EditAgentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_id** | **str** |  | 
**prompt** | **str** |  | 

## Example

```python
from odin_sdk.models.edit_agent_request import EditAgentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EditAgentRequest from a JSON string
edit_agent_request_instance = EditAgentRequest.from_json(json)
# print the JSON string representation of the object
print(EditAgentRequest.to_json())

# convert the object into a dict
edit_agent_request_dict = edit_agent_request_instance.to_dict()
# create an instance of EditAgentRequest from a dict
edit_agent_request_from_dict = EditAgentRequest.from_dict(edit_agent_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


