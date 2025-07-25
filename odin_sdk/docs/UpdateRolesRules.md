# UpdateRolesRules


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**view** | **bool** |  | [optional] 
**edit** | **bool** |  | [optional] 

## Example

```python
from odin_sdk.models.update_roles_rules import UpdateRolesRules

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRolesRules from a JSON string
update_roles_rules_instance = UpdateRolesRules.from_json(json)
# print the JSON string representation of the object
print(UpdateRolesRules.to_json())

# convert the object into a dict
update_roles_rules_dict = update_roles_rules_instance.to_dict()
# create an instance of UpdateRolesRules from a dict
update_roles_rules_from_dict = UpdateRolesRules.from_dict(update_roles_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


