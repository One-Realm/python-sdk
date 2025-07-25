# UserTeamNameChangeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 

## Example

```python
from odin_sdk.models.user_team_name_change_response import UserTeamNameChangeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserTeamNameChangeResponse from a JSON string
user_team_name_change_response_instance = UserTeamNameChangeResponse.from_json(json)
# print the JSON string representation of the object
print(UserTeamNameChangeResponse.to_json())

# convert the object into a dict
user_team_name_change_response_dict = user_team_name_change_response_instance.to_dict()
# create an instance of UserTeamNameChangeResponse from a dict
user_team_name_change_response_from_dict = UserTeamNameChangeResponse.from_dict(user_team_name_change_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


