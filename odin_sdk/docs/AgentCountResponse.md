# AgentCountResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_counts** | [**List[AgentCountByProject]**](AgentCountByProject.md) |  | 
**total_projects** | **int** |  | 

## Example

```python
from odin_sdk.models.agent_count_response import AgentCountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AgentCountResponse from a JSON string
agent_count_response_instance = AgentCountResponse.from_json(json)
# print the JSON string representation of the object
print(AgentCountResponse.to_json())

# convert the object into a dict
agent_count_response_dict = agent_count_response_instance.to_dict()
# create an instance of AgentCountResponse from a dict
agent_count_response_from_dict = AgentCountResponse.from_dict(agent_count_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


