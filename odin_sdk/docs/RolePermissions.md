# RolePermissions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_projects** | **bool** |  | [optional] [default to False]
**manage_team_members** | **bool** |  | [optional] [default to False]
**access_analytics** | **bool** |  | [optional] [default to False]
**manage_billing** | **bool** |  | [optional] [default to False]
**manage_team_settings** | **bool** |  | [optional] [default to False]

## Example

```python
from odin_sdk.models.role_permissions import RolePermissions

# TODO update the JSON string below
json = "{}"
# create an instance of RolePermissions from a JSON string
role_permissions_instance = RolePermissions.from_json(json)
# print the JSON string representation of the object
print(RolePermissions.to_json())

# convert the object into a dict
role_permissions_dict = role_permissions_instance.to_dict()
# create an instance of RolePermissions from a dict
role_permissions_from_dict = RolePermissions.from_dict(role_permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


