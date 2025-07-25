# AgentsRules


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**view** | **bool** | view permission for agents | [optional] [default to False]
**edit** | **bool** | edit permission for agents | [optional] [default to False]

## Example

```python
from odin_sdk.models.agents_rules import AgentsRules

# TODO update the JSON string below
json = "{}"
# create an instance of AgentsRules from a JSON string
agents_rules_instance = AgentsRules.from_json(json)
# print the JSON string representation of the object
print(AgentsRules.to_json())

# convert the object into a dict
agents_rules_dict = agents_rules_instance.to_dict()
# create an instance of AgentsRules from a dict
agents_rules_from_dict = AgentsRules.from_dict(agents_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


