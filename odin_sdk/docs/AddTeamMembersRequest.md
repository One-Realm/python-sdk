# AddTeamMembersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team_members** | [**List[TeamMembersRequest]**](TeamMembersRequest.md) |  | 
**send_mail** | **bool** |  | [optional] 

## Example

```python
from odin_sdk.models.add_team_members_request import AddTeamMembersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddTeamMembersRequest from a JSON string
add_team_members_request_instance = AddTeamMembersRequest.from_json(json)
# print the JSON string representation of the object
print(AddTeamMembersRequest.to_json())

# convert the object into a dict
add_team_members_request_dict = add_team_members_request_instance.to_dict()
# create an instance of AddTeamMembersRequest from a dict
add_team_members_request_from_dict = AddTeamMembersRequest.from_dict(add_team_members_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


