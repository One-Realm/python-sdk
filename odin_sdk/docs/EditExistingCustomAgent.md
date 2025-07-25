# EditExistingCustomAgent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | ID of the project in which to create the agent. | 
**agent_name** | **str** | Custom name of the agent. | 
**edit_agent_id** | **str** | ID of the agent to edit. | 
**personality** | **str** | Personality definition of the agent. | [optional] [default to 'You are a helpful agent.']
**building_blocks** | **List[object]** |  | [optional] 
**temperature** | **float** |  | [optional] 
**mask_urls** | **bool** |  | [optional] 

## Example

```python
from odin_sdk.models.edit_existing_custom_agent import EditExistingCustomAgent

# TODO update the JSON string below
json = "{}"
# create an instance of EditExistingCustomAgent from a JSON string
edit_existing_custom_agent_instance = EditExistingCustomAgent.from_json(json)
# print the JSON string representation of the object
print(EditExistingCustomAgent.to_json())

# convert the object into a dict
edit_existing_custom_agent_dict = edit_existing_custom_agent_instance.to_dict()
# create an instance of EditExistingCustomAgent from a dict
edit_existing_custom_agent_from_dict = EditExistingCustomAgent.from_dict(edit_existing_custom_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


