# CreateCodeRunnerActionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | The project ID | 
**script_name** | **str** | The name of the script | 
**script_description** | **str** |  | [optional] 
**script** | **str** | The script code | 
**runtime** | **str** | Runtime version (e.g., python3.11, nodejs20.x) | 
**entry_point** | **str** | Entry point function name | [optional] [default to 'main']
**kwargs** | **List[str]** | List of keyword argument names (deprecated, use parameters) | [optional] [default to []]
**parameters** | [**List[CodeRunnerParameter]**](CodeRunnerParameter.md) |  | [optional] 

## Example

```python
from odin_sdk.models.create_code_runner_action_request import CreateCodeRunnerActionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCodeRunnerActionRequest from a JSON string
create_code_runner_action_request_instance = CreateCodeRunnerActionRequest.from_json(json)
# print the JSON string representation of the object
print(CreateCodeRunnerActionRequest.to_json())

# convert the object into a dict
create_code_runner_action_request_dict = create_code_runner_action_request_instance.to_dict()
# create an instance of CreateCodeRunnerActionRequest from a dict
create_code_runner_action_request_from_dict = CreateCodeRunnerActionRequest.from_dict(create_code_runner_action_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


