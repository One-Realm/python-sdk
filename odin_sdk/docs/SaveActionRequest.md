# SaveActionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | The ID of the project on which to save the action. | 
**flow_id** | **str** | The unique ID of the action flow. | 
**action_name** | **str** | The name of the action. | 
**action_description** | **str** | The description of the action. | 
**required_fields_for_flow** | [**List[FieldsForActionFlow]**](FieldsForActionFlow.md) | The list of fields required for the action flow. | [optional] [default to []]
**is_test** | **bool** | Whether the endpoint is being hit in test mode or not. | [optional] [default to False]
**confirm_button_label** | **str** |  | [optional] 
**cancel_button_label** | **str** |  | [optional] 
**autosend** | **bool** |  | [optional] 
**type** | **str** |  | [optional] 
**config** | **object** |  | [optional] 

## Example

```python
from odin_sdk.models.save_action_request import SaveActionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SaveActionRequest from a JSON string
save_action_request_instance = SaveActionRequest.from_json(json)
# print the JSON string representation of the object
print(SaveActionRequest.to_json())

# convert the object into a dict
save_action_request_dict = save_action_request_instance.to_dict()
# create an instance of SaveActionRequest from a dict
save_action_request_from_dict = SaveActionRequest.from_dict(save_action_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


