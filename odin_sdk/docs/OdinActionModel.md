# OdinActionModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flow_id** | **str** | The ID of the action flow. | 
**action_name** | **str** | The name of the action. | 
**action_description** | **str** | The description of the action. | 
**required_fields_for_flow** | [**List[FieldsForActionFlow]**](FieldsForActionFlow.md) | The list of fields required for the action flow. | [optional] [default to []]
**autosend** | **bool** | Whether the action is autosendable or not. | 
**type** | **str** |  | [optional] 
**config** | **object** |  | [optional] 

## Example

```python
from odin_sdk.models.odin_action_model import OdinActionModel

# TODO update the JSON string below
json = "{}"
# create an instance of OdinActionModel from a JSON string
odin_action_model_instance = OdinActionModel.from_json(json)
# print the JSON string representation of the object
print(OdinActionModel.to_json())

# convert the object into a dict
odin_action_model_dict = odin_action_model_instance.to_dict()
# create an instance of OdinActionModel from a dict
odin_action_model_from_dict = OdinActionModel.from_dict(odin_action_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


