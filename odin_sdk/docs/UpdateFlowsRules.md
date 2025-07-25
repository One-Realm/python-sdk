# UpdateFlowsRules


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**view** | **bool** |  | [optional] 
**edit** | **bool** |  | [optional] 

## Example

```python
from odin_sdk.models.update_flows_rules import UpdateFlowsRules

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateFlowsRules from a JSON string
update_flows_rules_instance = UpdateFlowsRules.from_json(json)
# print the JSON string representation of the object
print(UpdateFlowsRules.to_json())

# convert the object into a dict
update_flows_rules_dict = update_flows_rules_instance.to_dict()
# create an instance of UpdateFlowsRules from a dict
update_flows_rules_from_dict = UpdateFlowsRules.from_dict(update_flows_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


