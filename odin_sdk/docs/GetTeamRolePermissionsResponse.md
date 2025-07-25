# GetTeamRolePermissionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team_id** | **str** |  | 
**role_permissions** | **List[object]** |  | 

## Example

```python
from odin_sdk.models.get_team_role_permissions_response import GetTeamRolePermissionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTeamRolePermissionsResponse from a JSON string
get_team_role_permissions_response_instance = GetTeamRolePermissionsResponse.from_json(json)
# print the JSON string representation of the object
print(GetTeamRolePermissionsResponse.to_json())

# convert the object into a dict
get_team_role_permissions_response_dict = get_team_role_permissions_response_instance.to_dict()
# create an instance of GetTeamRolePermissionsResponse from a dict
get_team_role_permissions_response_from_dict = GetTeamRolePermissionsResponse.from_dict(get_team_role_permissions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


