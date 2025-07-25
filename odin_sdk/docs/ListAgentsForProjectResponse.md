# ListAgentsForProjectResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agents** | **object** | Dictionary of agents in the project, by agent ID. | [optional] 

## Example

```python
from odin_sdk.models.list_agents_for_project_response import ListAgentsForProjectResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListAgentsForProjectResponse from a JSON string
list_agents_for_project_response_instance = ListAgentsForProjectResponse.from_json(json)
# print the JSON string representation of the object
print(ListAgentsForProjectResponse.to_json())

# convert the object into a dict
list_agents_for_project_response_dict = list_agents_for_project_response_instance.to_dict()
# create an instance of ListAgentsForProjectResponse from a dict
list_agents_for_project_response_from_dict = ListAgentsForProjectResponse.from_dict(list_agents_for_project_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


