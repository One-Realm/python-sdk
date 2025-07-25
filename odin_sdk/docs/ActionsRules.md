# ActionsRules


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**view** | **bool** | view permission for actions | [optional] [default to False]
**edit** | **bool** | edit permission for actions | [optional] [default to False]

## Example

```python
from odin_sdk.models.actions_rules import ActionsRules

# TODO update the JSON string below
json = "{}"
# create an instance of ActionsRules from a JSON string
actions_rules_instance = ActionsRules.from_json(json)
# print the JSON string representation of the object
print(ActionsRules.to_json())

# convert the object into a dict
actions_rules_dict = actions_rules_instance.to_dict()
# create an instance of ActionsRules from a dict
actions_rules_from_dict = ActionsRules.from_dict(actions_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


