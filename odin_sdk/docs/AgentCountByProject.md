# AgentCountByProject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | 
**agent_count** | **int** |  | 

## Example

```python
from odin_sdk.models.agent_count_by_project import AgentCountByProject

# TODO update the JSON string below
json = "{}"
# create an instance of AgentCountByProject from a JSON string
agent_count_by_project_instance = AgentCountByProject.from_json(json)
# print the JSON string representation of the object
print(AgentCountByProject.to_json())

# convert the object into a dict
agent_count_by_project_dict = agent_count_by_project_instance.to_dict()
# create an instance of AgentCountByProject from a dict
agent_count_by_project_from_dict = AgentCountByProject.from_dict(agent_count_by_project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


