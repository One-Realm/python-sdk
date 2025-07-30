# SaveNewCustomAgent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | ID of the project in which to create the agent. | 
**agent_name** | **str** | Custom name of the agent. | 
**personality** | **str** | Personality definition of the agent. | [optional] [default to 'You are a helpful agent.']
**building_blocks** | **List[object]** |  | [optional] 
**temperature** | **float** |  | [optional] 

## Example

```python
from odin_sdk.models.save_new_custom_agent import SaveNewCustomAgent

# TODO update the JSON string below
json = "{}"
# create an instance of SaveNewCustomAgent from a JSON string
save_new_custom_agent_instance = SaveNewCustomAgent.from_json(json)
# print the JSON string representation of the object
print(SaveNewCustomAgent.to_json())

# convert the object into a dict
save_new_custom_agent_dict = save_new_custom_agent_instance.to_dict()
# create an instance of SaveNewCustomAgent from a dict
save_new_custom_agent_from_dict = SaveNewCustomAgent.from_dict(save_new_custom_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


