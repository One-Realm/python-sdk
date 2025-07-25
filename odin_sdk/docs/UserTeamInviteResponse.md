# UserTeamInviteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 

## Example

```python
from odin_sdk.models.user_team_invite_response import UserTeamInviteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserTeamInviteResponse from a JSON string
user_team_invite_response_instance = UserTeamInviteResponse.from_json(json)
# print the JSON string representation of the object
print(UserTeamInviteResponse.to_json())

# convert the object into a dict
user_team_invite_response_dict = user_team_invite_response_instance.to_dict()
# create an instance of UserTeamInviteResponse from a dict
user_team_invite_response_from_dict = UserTeamInviteResponse.from_dict(user_team_invite_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


