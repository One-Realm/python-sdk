# ExecuteActionOnAutomatorRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_name** | **str** | The name of the action to execute. | 
**flow_id** | **str** | The ID of the action flow. | 
**ui_form** | **object** | The UI form to execute the action with. | [optional] 
**project_id** | **str** | The ID of the project on which to execute the action. | 
**chat_id** | **str** |  | [optional] 
**message_id** | **str** |  | [optional] 
**return_response** | **bool** |  | [optional] 
**type** | **str** |  | [optional] 
**config** | **object** |  | [optional] 

## Example

```python
from odin_sdk.models.execute_action_on_automator_request import ExecuteActionOnAutomatorRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExecuteActionOnAutomatorRequest from a JSON string
execute_action_on_automator_request_instance = ExecuteActionOnAutomatorRequest.from_json(json)
# print the JSON string representation of the object
print(ExecuteActionOnAutomatorRequest.to_json())

# convert the object into a dict
execute_action_on_automator_request_dict = execute_action_on_automator_request_instance.to_dict()
# create an instance of ExecuteActionOnAutomatorRequest from a dict
execute_action_on_automator_request_from_dict = ExecuteActionOnAutomatorRequest.from_dict(execute_action_on_automator_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


