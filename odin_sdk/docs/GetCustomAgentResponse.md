# GetCustomAgentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent** | **object** | Dictionary representing the agent. | 

## Example

```python
from odin_sdk.models.get_custom_agent_response import GetCustomAgentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetCustomAgentResponse from a JSON string
get_custom_agent_response_instance = GetCustomAgentResponse.from_json(json)
# print the JSON string representation of the object
print(GetCustomAgentResponse.to_json())

# convert the object into a dict
get_custom_agent_response_dict = get_custom_agent_response_instance.to_dict()
# create an instance of GetCustomAgentResponse from a dict
get_custom_agent_response_from_dict = GetCustomAgentResponse.from_dict(get_custom_agent_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


