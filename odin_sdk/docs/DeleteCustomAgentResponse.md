# DeleteCustomAgentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Message describing the result of the operation. | 

## Example

```python
from odin_sdk.models.delete_custom_agent_response import DeleteCustomAgentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteCustomAgentResponse from a JSON string
delete_custom_agent_response_instance = DeleteCustomAgentResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteCustomAgentResponse.to_json())

# convert the object into a dict
delete_custom_agent_response_dict = delete_custom_agent_response_instance.to_dict()
# create an instance of DeleteCustomAgentResponse from a dict
delete_custom_agent_response_from_dict = DeleteCustomAgentResponse.from_dict(delete_custom_agent_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


