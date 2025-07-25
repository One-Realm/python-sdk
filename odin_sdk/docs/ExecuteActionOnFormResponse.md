# ExecuteActionOnFormResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | The message of the response. | 
**success** | **bool** | Whether the action was executed successfully or not. | 
**chat_id** | **str** |  | [optional] 
**message_id** | **str** |  | [optional] 
**flow_run_id** | **str** |  | [optional] 
**action_response** | **object** |  | [optional] 

## Example

```python
from odin_sdk.models.execute_action_on_form_response import ExecuteActionOnFormResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExecuteActionOnFormResponse from a JSON string
execute_action_on_form_response_instance = ExecuteActionOnFormResponse.from_json(json)
# print the JSON string representation of the object
print(ExecuteActionOnFormResponse.to_json())

# convert the object into a dict
execute_action_on_form_response_dict = execute_action_on_form_response_instance.to_dict()
# create an instance of ExecuteActionOnFormResponse from a dict
execute_action_on_form_response_from_dict = ExecuteActionOnFormResponse.from_dict(execute_action_on_form_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


