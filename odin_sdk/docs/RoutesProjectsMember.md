# RoutesProjectsMember


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**role** | **str** |  | [optional] 
**project_id** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**is_pending** | **bool** |  | [optional] 
**invited_by** | [**InvitedUser**](InvitedUser.md) |  | [optional] 

## Example

```python
from odin_sdk.models.routes_projects_member import RoutesProjectsMember

# TODO update the JSON string below
json = "{}"
# create an instance of RoutesProjectsMember from a JSON string
routes_projects_member_instance = RoutesProjectsMember.from_json(json)
# print the JSON string representation of the object
print(RoutesProjectsMember.to_json())

# convert the object into a dict
routes_projects_member_dict = routes_projects_member_instance.to_dict()
# create an instance of RoutesProjectsMember from a dict
routes_projects_member_from_dict = RoutesProjectsMember.from_dict(routes_projects_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


