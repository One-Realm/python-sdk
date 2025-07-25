# AgentDifficultyLevelResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**difficulty_level** | **str** |  | 

## Example

```python
from odin_sdk.models.agent_difficulty_level_response import AgentDifficultyLevelResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AgentDifficultyLevelResponse from a JSON string
agent_difficulty_level_response_instance = AgentDifficultyLevelResponse.from_json(json)
# print the JSON string representation of the object
print(AgentDifficultyLevelResponse.to_json())

# convert the object into a dict
agent_difficulty_level_response_dict = agent_difficulty_level_response_instance.to_dict()
# create an instance of AgentDifficultyLevelResponse from a dict
agent_difficulty_level_response_from_dict = AgentDifficultyLevelResponse.from_dict(agent_difficulty_level_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


