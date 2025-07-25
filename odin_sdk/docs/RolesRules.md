# RolesRules


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**view** | **bool** | view permission for roles | [optional] [default to False]
**edit** | **bool** | edit permission for roles | [optional] [default to False]

## Example

```python
from odin_sdk.models.roles_rules import RolesRules

# TODO update the JSON string below
json = "{}"
# create an instance of RolesRules from a JSON string
roles_rules_instance = RolesRules.from_json(json)
# print the JSON string representation of the object
print(RolesRules.to_json())

# convert the object into a dict
roles_rules_dict = roles_rules_instance.to_dict()
# create an instance of RolesRules from a dict
roles_rules_from_dict = RolesRules.from_dict(roles_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


